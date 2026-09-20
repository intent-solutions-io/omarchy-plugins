#!/usr/bin/env python3
"""Inventory Git worktrees and identify safe cleanup candidates.

The hook never deletes a worktree or branch. It may prune metadata for paths
that are already missing only when a human runs `prune-metadata --apply`.
"""

from __future__ import annotations

import argparse
import fnmatch
import json
import os
import subprocess
import sys
import tempfile
import time
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


@dataclass
class Worktree:
    path: str
    head: str = ""
    branch: str = ""
    bare: bool = False
    detached: bool = False
    locked: bool = False
    prunable: bool = False
    exists: bool = False
    dirty: bool | None = None
    upstream: str | None = None
    upstream_gone: bool = False
    ahead_of_default: int | None = None
    behind_default: int | None = None
    head_age_days: int | None = None
    classification: str = "active"
    reasons: list[str] | None = None


def run(args: list[str], cwd: Path | None = None, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, cwd=cwd, text=True, capture_output=True, check=check)


def repo_root() -> Path:
    result = run(["git", "rev-parse", "--show-toplevel"])
    return Path(result.stdout.strip()).resolve()


def load_config(root: Path, explicit: str | None) -> dict[str, Any]:
    path = Path(explicit).resolve() if explicit else root / ".worktree-hygiene.json"
    defaults: dict[str, Any] = {
        "review_after_days": 14,
        "protected_branch_globs": ["main", "master", "release/*"],
    }
    if not path.exists():
        return defaults
    loaded = json.loads(path.read_text(encoding="utf-8"))
    defaults.update(loaded)
    if not isinstance(defaults["review_after_days"], int) or defaults["review_after_days"] < 0:
        raise ValueError("review_after_days must be a non-negative integer")
    if not all(isinstance(item, str) for item in defaults["protected_branch_globs"]):
        raise ValueError("protected_branch_globs must contain only strings")
    return defaults


def parse_porcelain(text: str) -> list[Worktree]:
    worktrees: list[Worktree] = []
    current: Worktree | None = None
    for line in text.splitlines() + [""]:
        if not line:
            if current is not None:
                worktrees.append(current)
                current = None
            continue
        key, _, value = line.partition(" ")
        if key == "worktree":
            current = Worktree(path=value)
        elif current is not None and key == "HEAD":
            current.head = value
        elif current is not None and key == "branch":
            current.branch = value.removeprefix("refs/heads/")
        elif current is not None and key == "bare":
            current.bare = True
        elif current is not None and key == "detached":
            current.detached = True
        elif current is not None and key == "locked":
            current.locked = True
        elif current is not None and key == "prunable":
            current.prunable = True
    return worktrees


def default_ref(root: Path) -> str | None:
    remote = run(["git", "symbolic-ref", "--quiet", "refs/remotes/origin/HEAD"], root, check=False)
    if remote.returncode == 0:
        return remote.stdout.strip()
    for candidate in ("refs/heads/main", "refs/heads/master"):
        if run(["git", "show-ref", "--verify", "--quiet", candidate], root, check=False).returncode == 0:
            return candidate
    return None


def enrich(root: Path, items: list[Worktree], config: dict[str, Any]) -> list[Worktree]:
    current_path = root.resolve()
    primary_path = Path(items[0].path).resolve() if items else current_path
    baseline = default_ref(root)
    now = int(time.time())
    for item in items:
        path = Path(item.path)
        item.exists = path.is_dir()
        item.reasons = []
        is_current = path.resolve() == current_path if item.exists else False
        is_primary = path.resolve() == primary_path if item.exists else False
        protected_branch = any(fnmatch.fnmatch(item.branch, pattern) for pattern in config["protected_branch_globs"])

        if item.exists and not item.bare:
            status = run(["git", "status", "--porcelain", "--untracked-files=normal"], path, check=False)
            item.dirty = bool(status.stdout.strip()) if status.returncode == 0 else None
            upstream = run(["git", "rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{upstream}"], path, check=False)
            if upstream.returncode == 0:
                item.upstream = upstream.stdout.strip()
            elif item.branch:
                item.upstream_gone = True
            timestamp = run(["git", "show", "-s", "--format=%ct", item.head], path, check=False)
            if timestamp.returncode == 0 and timestamp.stdout.strip().isdigit():
                item.head_age_days = max(0, (now - int(timestamp.stdout.strip())) // 86400)

        if baseline and item.head:
            counts = run(["git", "rev-list", "--left-right", "--count", f"{baseline}...{item.head}"], root, check=False)
            if counts.returncode == 0:
                behind, ahead = (int(value) for value in counts.stdout.split())
                item.ahead_of_default = ahead
                item.behind_default = behind

        if not item.exists or item.prunable:
            item.classification = "prunable-metadata"
            item.reasons.append("registered path is missing or Git marks it prunable")
        elif is_current or is_primary or item.locked or protected_branch:
            item.classification = "protected"
            item.reasons.append("current, primary, locked, or protected branch")
        elif item.dirty:
            item.classification = "dirty-protected"
            item.reasons.append("uncommitted or untracked work must be reviewed by a human")
        elif item.detached:
            item.classification = "review"
            item.reasons.append("clean detached worktree")
        elif item.ahead_of_default and item.ahead_of_default > 0:
            item.classification = "active"
            item.reasons.append(f"branch has {item.ahead_of_default} commit(s) not in the default branch")
        elif item.upstream_gone:
            item.classification = "review"
            item.reasons.append("clean branch has no resolvable upstream")
        elif item.ahead_of_default == 0 and (item.head_age_days or 0) >= config["review_after_days"]:
            item.classification = "review"
            item.reasons.append("clean branch is merged into default and its head is past the review age")
        else:
            item.classification = "active"
            item.reasons.append("no safe stale-worktree signal")
    return items


def audit(root: Path, config: dict[str, Any]) -> dict[str, Any]:
    listed = run(["git", "worktree", "list", "--porcelain"], root)
    items = enrich(root, parse_porcelain(listed.stdout), config)
    dry_run = run(["git", "worktree", "prune", "--dry-run", "--verbose"], root, check=False)
    return {
        "schema_version": 1,
        "repository": str(root),
        "generated_at_epoch": int(time.time()),
        "policy": config,
        "worktrees": [asdict(item) for item in items],
        "counts": {
            key: sum(item.classification == key for item in items)
            for key in ("protected", "active", "dirty-protected", "review", "prunable-metadata")
        },
        "prune_dry_run": dry_run.stdout.strip(),
    }


def write_receipt(root: Path, report: dict[str, Any]) -> Path:
    common = run(["git", "rev-parse", "--path-format=absolute", "--git-common-dir"], root).stdout.strip()
    destination = Path(common) / "intent-worktree-hygiene.json"
    destination.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=".intent-worktree-hygiene-", dir=destination.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(report, handle, indent=2, sort_keys=True)
            handle.write("\n")
        os.replace(temporary, destination)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)
    return destination


def print_human(report: dict[str, Any], hook: bool) -> None:
    candidates = [item for item in report["worktrees"] if item["classification"] in {"review", "prunable-metadata", "dirty-protected"}]
    if hook:
        if candidates:
            print(f"Worktree hygiene: {len(candidates)} item(s) need review. Run scripts/worktree-hygiene.py audit for details. No worktree or branch was deleted.")
        return
    print("CLASSIFICATION       BRANCH                              PATH")
    for item in report["worktrees"]:
        print(f"{item['classification']:<20} {item['branch'] or '(detached)':<35} {item['path']}")
        for reason in item["reasons"] or []:
            print(f"  reason: {reason}")
    if report["prune_dry_run"]:
        print("Metadata Git would prune:")
        print(report["prune_dry_run"])
    print("No worktree or branch was deleted.")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("audit", "prune-metadata"))
    parser.add_argument("--config")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--hook", action="store_true")
    parser.add_argument("--apply", action="store_true", help="Apply metadata pruning for already missing paths")
    args = parser.parse_args()
    root = repo_root()
    config = load_config(root, args.config)

    if args.command == "prune-metadata":
        command = ["git", "worktree", "prune", "--verbose"]
        if not args.apply:
            command.insert(3, "--dry-run")
        result = run(command, root, check=False)
        sys.stdout.write(result.stdout)
        sys.stderr.write(result.stderr)
        if not args.apply:
            print("Dry run only. Re-run with --apply to prune metadata for paths that are already missing.")
        return result.returncode

    report = audit(root, config)
    receipt = write_receipt(root, report)
    report["receipt"] = str(receipt)
    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        print_human(report, args.hook)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
