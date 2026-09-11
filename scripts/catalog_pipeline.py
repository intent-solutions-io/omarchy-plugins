#!/usr/bin/env python3
"""Build the public Omarchy catalogue from inventory and live snapshots."""

from __future__ import annotations

import argparse
import json
import pathlib
import re
from typing import Any


ROOT = pathlib.Path(__file__).resolve().parents[1]
README_START = "<!-- METRICS:START -->"
README_END = "<!-- METRICS:END -->"
ALLOWED_LIFECYCLES = {"listed", "under-review", "developing", "unreleased", "retired", "not-listed"}
ID_RE = re.compile(r"^io\.github\.jeremylongshore\.[a-z0-9-]+$")
REPO_RE = re.compile(r"^omarchy-[a-z0-9-]+-entry$")


class CatalogError(ValueError):
    """Raised when source or upstream catalogue data is not trustworthy."""


def require_string(value: object, label: str, maximum: int = 500) -> str:
    if not isinstance(value, str) or not value.strip() or len(value) > maximum:
        raise CatalogError(f"{label} must be a non-empty string of at most {maximum} characters")
    return value.strip()


def validate_config(config: dict[str, Any]) -> None:
    plugins = config.get("plugins")
    families = config.get("families")
    if not isinstance(plugins, list) or not plugins:
        raise CatalogError("plugins.json must contain a non-empty plugins array")
    if not isinstance(families, list) or not families:
        raise CatalogError("plugins.json must contain a non-empty families array")
    known_families = {require_string(value, "family", 60) for value in families}
    if len(known_families) != len(families):
        raise CatalogError("plugins.json contains duplicate families")
    ids: set[str] = set()
    repos: set[str] = set()
    for index, entry in enumerate(plugins):
        if not isinstance(entry, dict):
            raise CatalogError(f"plugins[{index}] must be an object")
        plugin_id = require_string(entry.get("id"), f"plugins[{index}].id", 120)
        repo = require_string(entry.get("repo"), f"plugins[{index}].repo", 120)
        family = require_string(entry.get("family"), f"plugins[{index}].family", 60)
        lifecycle = require_string(entry.get("lifecycle"), f"plugins[{index}].lifecycle", 40)
        require_string(entry.get("name"), f"plugins[{index}].name", 80)
        require_string(entry.get("pitch"), f"plugins[{index}].pitch", 500)
        if "tags" in entry and (
            not isinstance(entry["tags"], list)
            or any(not isinstance(tag, str) or not tag.strip() or len(tag) > 60 for tag in entry["tags"])
        ):
            raise CatalogError(f"plugins[{index}].tags must be an array of short strings")
        if not ID_RE.fullmatch(plugin_id):
            raise CatalogError(f"invalid plugin id: {plugin_id}")
        if not REPO_RE.fullmatch(repo):
            raise CatalogError(f"invalid plugin repository: {repo}")
        if family not in known_families:
            raise CatalogError(f"unknown family for {plugin_id}: {family}")
        if lifecycle not in ALLOWED_LIFECYCLES:
            raise CatalogError(f"invalid lifecycle for {plugin_id}: {lifecycle}")
        if plugin_id in ids or repo in repos:
            raise CatalogError(f"duplicate plugin id or repository: {plugin_id}")
        ids.add(plugin_id)
        repos.add(repo)


def nonnegative_integer(value: object, label: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise CatalogError(f"{label} must be a non-negative integer")
    return value


def lifecycle_for(entry: dict[str, Any], marketplace: dict[str, Any] | None) -> str:
    if marketplace is not None:
        return "listed"
    configured = entry.get("lifecycle", "developing")
    return "not-listed" if configured == "listed" else configured


def manifest_assessment(entry: dict[str, Any], marketplace: dict[str, Any] | None, github: dict[str, Any]) -> dict[str, Any]:
    manifest = github.get("manifest")
    issues: list[str] = []
    if not isinstance(manifest, dict):
        return {"status": "missing", "version": None, "sha": github.get("manifestSha"), "issues": ["manifest.json is missing or unreadable"]}
    for key in ("id", "name"):
        if manifest.get(key) != entry.get(key):
            issues.append(f"{key} differs from plugins.json")
    manifest_version = manifest.get("version")
    if not isinstance(manifest_version, str) or not manifest_version:
        issues.append("version is missing from manifest.json")
    catalog_version = marketplace.get("version") if marketplace else None
    if catalog_version and manifest_version != catalog_version:
        issues.append("version differs from the official marketplace")
    return {
        "status": "drift" if issues else "aligned",
        "version": manifest_version if isinstance(manifest_version, str) else None,
        "sha": github.get("manifestSha"),
        "issues": issues,
    }


def build_catalog(config: dict[str, Any], catalog: dict[str, Any], stats_body: dict[str, Any], github_snapshot: dict[str, Any]) -> dict[str, Any]:
    validate_config(config)
    catalog_plugins = catalog.get("plugins")
    stats = stats_body.get("plugins")
    github_repos = github_snapshot.get("repos")
    if not isinstance(catalog_plugins, list) or not isinstance(stats, dict) or not isinstance(github_repos, dict):
        raise CatalogError("upstream snapshots do not match the required schema")
    generated_at = require_string(catalog.get("generatedAt"), "catalog.generatedAt", 80)
    by_id = {entry.get("id"): entry for entry in catalog_plugins if isinstance(entry, dict)}
    page = require_string(config["marketplace"].get("pluginPage"), "marketplace.pluginPage", 300)
    owner = require_string(config["github"].get("owner"), "github.owner", 80)
    public_plugins: list[dict[str, Any]] = []
    for entry in config["plugins"]:
        plugin_id = entry["id"]
        repo = entry["repo"]
        marketplace = by_id.get(plugin_id)
        github = github_repos.get(repo)
        if not isinstance(github, dict):
            raise CatalogError(f"GitHub snapshot is missing repository: {repo}")
        expected_repo_url = f"https://github.com/{owner}/{repo}"
        if github.get("repoUrl") != expected_repo_url:
            raise CatalogError(f"GitHub repository URL differs for {repo}")
        stars = nonnegative_integer(github.get("stars"), f"{repo}.stars")
        open_issues = nonnegative_integer(github.get("openIssues"), f"{repo}.openIssues")
        pushed_at = require_string(github.get("pushedAt"), f"{repo}.pushedAt", 80)
        default_branch = require_string(github.get("defaultBranch"), f"{repo}.defaultBranch", 120)
        preview_source = github.get("preview") if isinstance(github.get("preview"), dict) else {}
        preview_available = preview_source.get("available") is True
        preview_url = preview_source.get("url") if preview_available else None
        if preview_url is not None and not str(preview_url).startswith(f"https://raw.githubusercontent.com/{owner}/{repo}/"):
            raise CatalogError(f"unexpected preview URL for {repo}")
        lifecycle = lifecycle_for(entry, marketplace)
        marketplace_url = f"{page}{plugin_id}" if marketplace else None
        submission_url = entry.get("submissionUrl") if lifecycle == "under-review" else None
        if submission_url is not None and not str(submission_url).startswith("https://github.com/"):
            raise CatalogError(f"unexpected submission URL for {repo}")
        metric_source = stats.get(plugin_id) if marketplace else None
        metrics = None
        if isinstance(metric_source, dict):
            metrics = {
                "views": nonnegative_integer(metric_source.get("views", 0), f"{plugin_id}.views"),
                "copies": nonnegative_integer(metric_source.get("copies", 0), f"{plugin_id}.copies"),
                "hearts": nonnegative_integer(metric_source.get("hearts", 0), f"{plugin_id}.hearts"),
            }
        marketplace_tags = marketplace.get("tags") if marketplace else None
        tags = marketplace_tags if isinstance(marketplace_tags, list) else entry.get("tags", [])
        if any(not isinstance(tag, str) or not tag.strip() or len(tag) > 60 for tag in tags):
            raise CatalogError(f"unexpected tags for {plugin_id}")
        public_plugins.append({
            "id": plugin_id,
            "name": entry["name"],
            "slug": repo.removeprefix("omarchy-").removesuffix("-entry"),
            "repo": repo,
            "repoUrl": expected_repo_url,
            "pitch": entry["pitch"],
            "family": entry["family"],
            "lifecycle": lifecycle,
            "category": marketplace.get("category", entry.get("category", "Other")) if marketplace else entry.get("category", "Other"),
            "tags": tags,
            "marketplaceUrl": marketplace_url,
            "submissionUrl": submission_url,
            "installCommand": marketplace.get("installCommand") if marketplace else None,
            "verificationStatus": marketplace.get("verificationStatus", "unverified") if marketplace else "not-listed",
            "version": marketplace.get("version") if marketplace else None,
            "previewUrl": preview_url,
            "preview": {
                "status": "verified" if preview_available else "missing",
                "url": preview_url,
                "path": preview_source.get("path", "preview.png"),
                "sha": preview_source.get("sha"),
            },
            "github": {
                "stars": stars,
                "pushedAt": pushed_at,
                "defaultBranch": default_branch,
                "archived": github.get("archived") is True,
                "openIssues": open_issues,
            },
            "manifest": manifest_assessment(entry, marketplace, github),
            "metrics": metrics,
        })
    template = config["template"]
    template_repo = template["repo"]
    template_github = github_repos.get(template_repo)
    if not isinstance(template_github, dict):
        raise CatalogError(f"GitHub snapshot is missing template: {template_repo}")
    template_repo_url = f"https://github.com/{owner}/{template_repo}"
    if template_github.get("repoUrl") != template_repo_url:
        raise CatalogError("template GitHub repository URL differs")
    return {
        "generatedAt": generated_at,
        "catalogSize": len(catalog_plugins),
        "publisher": {
            "name": "Jeremy Longshore",
            "githubUrl": f"https://github.com/{owner}",
            "marketplaceUrl": config["marketplace"]["authorPage"],
        },
        "families": config["families"],
        "plugins": public_plugins,
        "template": {
            "name": template.get("name", "Widget Template"),
            "repo": template_repo,
            "repoUrl": template_repo_url,
            "pitch": template["pitch"],
            "github": {
                "stars": nonnegative_integer(template_github.get("stars"), f"{template_repo}.stars"),
                "pushedAt": require_string(template_github.get("pushedAt"), f"{template_repo}.pushedAt", 80),
                "archived": template_github.get("archived") is True,
            },
            "preview": {
                "status": "verified" if template_github.get("preview", {}).get("available") is True else "missing",
                "url": template_github.get("preview", {}).get("url"),
                "sha": template_github.get("preview", {}).get("sha"),
            },
        },
    }


def lifecycle_label(value: str) -> str:
    return {
        "listed": "listed",
        "under-review": "under review",
        "developing": "developing",
        "unreleased": "unreleased",
        "retired": "retired",
        "not-listed": "not listed",
    }.get(value, value.replace("-", " "))


def render_readme_block(data: dict[str, Any]) -> str:
    rows: list[str] = []
    install_rows: list[tuple[str, str]] = []
    for plugin in data["plugins"]:
        github = plugin["github"]
        source = f"[repo]({plugin['repoUrl']})"
        if plugin["marketplaceUrl"]:
            authority = f"[{plugin['category']}]({plugin['marketplaceUrl']})"
        elif plugin["submissionUrl"]:
            authority = f"[{lifecycle_label(plugin['lifecycle'])}]({plugin['submissionUrl']})"
        else:
            authority = lifecycle_label(plugin["lifecycle"])
        metrics = plugin["metrics"] or {"views": "n/a", "copies": "n/a", "hearts": "n/a"}
        rows.append(
            f"| **{plugin['name']}** | {plugin['family']} | {plugin['pitch']} | {source} | {authority} | "
            f"{github['stars']} | {metrics['views']} | {metrics['copies']} | {metrics['hearts']} |"
        )
        if plugin["installCommand"]:
            install_rows.append((plugin["name"], plugin["installCommand"]))
    template = data["template"]
    rows.append(
        f"| **{template['name']}** | Build system | {template['pitch']} | [repo]({template['repoUrl']}) | "
        f"not a listing | {template['github']['stars']} | n/a | n/a | n/a |"
    )
    listed = [plugin for plugin in data["plugins"] if plugin["lifecycle"] == "listed"]
    totals = {
        key: sum((plugin["metrics"] or {}).get(key, 0) for plugin in listed)
        for key in ("views", "copies", "hearts")
    }
    stars = sum(plugin["github"]["stars"] for plugin in data["plugins"])
    lines = [
        f"Marketplace data generated at `{data['generatedAt']}`, across {data['catalogSize']} listed plugins. "
        "GitHub stars, repository freshness, root manifest, and preview metadata are derived during the same refresh.",
        "",
        "| Plugin | Family | What it does | Source | Marketplace | Stars | Views | Copies | Hearts |",
        "| --- | --- | --- | --- | --- | --: | --: | --: | --: |",
        *rows,
        "",
        f"**{len(listed)} of {len(data['plugins'])} listed** on the marketplace, "
        f"{totals['views']} views, {totals['copies']} copies, {totals['hearts']} hearts, and {stars} GitHub stars.",
    ]
    pending = [plugin["name"] for plugin in data["plugins"] if plugin["lifecycle"] != "listed"]
    if pending:
        lines.extend(["", f"Not currently listed: {', '.join(pending)}. Lifecycle labels come from the canonical inventory when no official listing exists."])
    lines.extend([
        "",
        "### Install",
        "",
        "Every command below is read from the marketplace catalog's own `installCommand` field at refresh time.",
        "",
        "```bash",
    ])
    for name, command in install_rows:
        lines.extend([f"# {name}", command])
    lines.extend(["```", "", "Manifest and screenshot status are checked from each repository root. Any mismatch stays visible in the generated site rather than being silently corrected here."])
    return "\n".join(lines)


def replace_generated_block(text: str, replacement: str) -> str:
    pattern = re.escape(README_START) + r".*?" + re.escape(README_END)
    if README_START not in text or README_END not in text:
        raise CatalogError("README.md is missing the METRICS markers")
    return re.sub(pattern, f"{README_START}\n{replacement}\n{README_END}", text, flags=re.S)


def write_or_check(data: dict[str, Any], mode: str) -> int:
    readme_path = ROOT / "README.md"
    site_path = ROOT / "site" / "data" / "plugins.json"
    readme = readme_path.read_text()
    expected_readme = replace_generated_block(readme, render_readme_block(data))
    expected_site = json.dumps(data, indent=2, ensure_ascii=True) + "\n"
    if mode == "--check":
        stale = False
        if expected_readme != readme:
            print("STALE: README metrics table does not match live source snapshots.")
            stale = True
        if not site_path.exists() or site_path.read_text() != expected_site:
            print("STALE: public site data does not match live source snapshots.")
            stale = True
        if stale:
            return 1
        print("fresh: README and public site data match marketplace and GitHub snapshots.")
        return 0
    changed: list[str] = []
    if expected_readme != readme:
        readme_path.write_text(expected_readme)
        changed.append("README.md")
    if not site_path.exists() or site_path.read_text() != expected_site:
        site_path.parent.mkdir(parents=True, exist_ok=True)
        site_path.write_text(expected_site)
        changed.append("site/data/plugins.json")
    listed = sum(plugin["lifecycle"] == "listed" for plugin in data["plugins"])
    print(f"updated: {listed}/{len(data['plugins'])} listed; files: {', '.join(changed) if changed else 'none'}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=pathlib.Path, required=True)
    parser.add_argument("--catalog", type=pathlib.Path, required=True)
    parser.add_argument("--stats", type=pathlib.Path, required=True)
    parser.add_argument("--github", type=pathlib.Path, required=True)
    parser.add_argument("--mode", choices=("write", "check"), default="write")
    args = parser.parse_args()
    data = build_catalog(
        json.loads(args.config.read_text()),
        json.loads(args.catalog.read_text()),
        json.loads(args.stats.read_text()),
        json.loads(args.github.read_text()),
    )
    return write_or_check(data, "--check" if args.mode == "check" else "write")


if __name__ == "__main__":
    raise SystemExit(main())
