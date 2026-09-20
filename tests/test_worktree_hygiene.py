from __future__ import annotations

import importlib.util
import io
import json
import os
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest import mock


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "worktree-hygiene.py"
SPEC = importlib.util.spec_from_file_location("worktree_hygiene", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def git(repo: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(["git", *args], cwd=repo, text=True, capture_output=True, check=True)


class WorktreeHygieneTest(unittest.TestCase):
    def test_porcelain_parser_preserves_flags(self) -> None:
        parsed = MODULE.parse_porcelain(
            "worktree /tmp/main\nHEAD abc\nbranch refs/heads/main\n\n"
            "worktree /tmp/gone\nHEAD def\ndetached\nprunable gitdir file points to non-existent location\n"
        )
        self.assertEqual(2, len(parsed))
        self.assertEqual("main", parsed[0].branch)
        self.assertTrue(parsed[1].detached)
        self.assertTrue(parsed[1].prunable)

    def test_audit_protects_current_and_dirty_worktrees(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary) / "repo"
            root.mkdir()
            git(root, "init", "-b", "main")
            git(root, "config", "user.name", "Test")
            git(root, "config", "user.email", "test@example.invalid")
            (root / "README.md").write_text("initial\n", encoding="utf-8")
            git(root, "add", "README.md")
            git(root, "commit", "-m", "initial")
            sibling = Path(temporary) / "sibling"
            git(root, "branch", "topic")
            git(root, "worktree", "add", str(sibling), "topic")
            (sibling / "dirty.txt").write_text("keep me\n", encoding="utf-8")

            report = MODULE.audit(root, {"review_after_days": 0, "protected_branch_globs": ["main"]})
            by_branch = {item["branch"]: item for item in report["worktrees"]}
            self.assertEqual("protected", by_branch["main"]["classification"])
            self.assertEqual("dirty-protected", by_branch["topic"]["classification"])

    def test_missing_worktree_is_metadata_only_candidate(self) -> None:
        parsed = MODULE.parse_porcelain(
            "worktree /definitely/not/present\nHEAD abc\nbranch refs/heads/topic\nprunable missing\n"
        )
        self.assertTrue(parsed[0].prunable)
        self.assertFalse(Path(parsed[0].path).exists())

    def test_audit_invokes_no_worktree_or_branch_deletion(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary) / "repo"
            root.mkdir()
            git(root, "init", "-b", "main")
            git(root, "config", "user.name", "Test")
            git(root, "config", "user.email", "test@example.invalid")
            (root / "README.md").write_text("initial\n", encoding="utf-8")
            git(root, "add", "README.md")
            git(root, "commit", "-m", "initial")

            calls: list[list[str]] = []
            original_run = MODULE.run

            def recording_run(args, cwd=None, check=True):
                calls.append(list(args))
                return original_run(args, cwd, check)

            with mock.patch.object(MODULE, "run", side_effect=recording_run):
                MODULE.audit(root, {"review_after_days": 14, "protected_branch_globs": ["main"]})

            self.assertFalse(any(command[:3] == ["git", "worktree", "remove"] for command in calls))
            self.assertFalse(any(command[:3] == ["git", "branch", "-D"] for command in calls))
            prune_calls = [command for command in calls if command[:3] == ["git", "worktree", "prune"]]
            self.assertEqual([["git", "worktree", "prune", "--dry-run", "--verbose"]], prune_calls)

    def test_locked_and_protected_branch_worktrees_are_protected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary) / "repo"
            root.mkdir()
            git(root, "init", "-b", "main")
            git(root, "config", "user.name", "Test")
            git(root, "config", "user.email", "test@example.invalid")
            (root / "README.md").write_text("initial\n", encoding="utf-8")
            git(root, "add", "README.md")
            git(root, "commit", "-m", "initial")
            locked = Path(temporary) / "locked"
            release = Path(temporary) / "release"
            git(root, "branch", "locked-topic")
            git(root, "branch", "release/test")
            git(root, "worktree", "add", str(locked), "locked-topic")
            git(root, "worktree", "lock", str(locked))
            git(root, "worktree", "add", str(release), "release/test")

            report = MODULE.audit(root, {"review_after_days": 0, "protected_branch_globs": ["main", "release/*"]})
            by_branch = {item["branch"]: item for item in report["worktrees"]}
            self.assertEqual("protected", by_branch["locked-topic"]["classification"])
            self.assertEqual("protected", by_branch["release/test"]["classification"])

    def test_prune_metadata_requires_apply_to_drop_dry_run(self) -> None:
        completed = subprocess.CompletedProcess(["git"], 0, "", "")
        for apply, expected in ((False, True), (True, False)):
            calls: list[list[str]] = []

            def fake_run(args, cwd=None, check=True):
                calls.append(list(args))
                return completed

            argv = [str(SCRIPT), "prune-metadata"] + (["--apply"] if apply else [])
            with mock.patch.object(MODULE, "repo_root", return_value=Path("/tmp/repo")), \
                 mock.patch.object(MODULE, "load_config", return_value={}), \
                 mock.patch.object(MODULE, "run", side_effect=fake_run), \
                 mock.patch.object(sys, "argv", argv), redirect_stdout(io.StringIO()):
                self.assertEqual(0, MODULE.main())
            self.assertEqual(expected, "--dry-run" in calls[-1])

    def test_receipt_uses_atomic_replace_and_contains_report(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            common = Path(temporary) / "git-common"
            common.mkdir()
            completed = subprocess.CompletedProcess(["git"], 0, str(common) + "\n", "")
            report = {"schema_version": 1, "worktrees": []}
            original_replace = os.replace

            with mock.patch.object(MODULE, "run", return_value=completed), \
                 mock.patch.object(MODULE.os, "replace", wraps=original_replace) as replace:
                destination = MODULE.write_receipt(Path(temporary), report)

            replace.assert_called_once()
            self.assertEqual(common / "intent-worktree-hygiene.json", destination)
            self.assertEqual(report, json.loads(destination.read_text(encoding="utf-8")))


if __name__ == "__main__":
    unittest.main()
