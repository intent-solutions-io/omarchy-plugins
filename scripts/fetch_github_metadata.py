#!/usr/bin/env python3
"""Fetch bounded GitHub repository, manifest, and preview metadata."""

from __future__ import annotations

import argparse
import base64
import concurrent.futures
import json
import os
import pathlib
import re
import urllib.error
import urllib.parse
import urllib.request


REPO_RE = re.compile(r"^[a-zA-Z0-9._-]+$")
ALLOWED_API_HOST = "api.github.com"
ALLOWED_RAW_HOST = "raw.githubusercontent.com"


class MetadataError(RuntimeError):
    """Raised when live GitHub metadata cannot be trusted."""


def request_json(url: str, token: str | None = None) -> object:
    """Fetch one bounded JSON response from an allowlisted GitHub host."""
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme != "https" or parsed.hostname not in {ALLOWED_API_HOST, ALLOWED_RAW_HOST}:
        raise MetadataError(f"refusing non-GitHub metadata URL: {url}")
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "intent-solutions-omarchy-catalog/1",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token and parsed.hostname == ALLOWED_API_HOST:
        headers["Authorization"] = f"Bearer {token}"
    request = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            if response.status != 200:
                raise MetadataError(f"GitHub returned HTTP {response.status} for {url}")
            body = response.read(2_000_001)
    except urllib.error.HTTPError as error:
        raise MetadataError(f"GitHub returned HTTP {error.code} for {url}") from error
    except urllib.error.URLError as error:
        raise MetadataError(f"GitHub request failed for {url}: {error.reason}") from error
    if len(body) > 2_000_000:
        raise MetadataError(f"GitHub response exceeded 2 MB for {url}")
    try:
        return json.loads(body)
    except json.JSONDecodeError as error:
        raise MetadataError(f"GitHub returned invalid JSON for {url}") from error


def raw_manifest(download_url: str, owner: str, repo: str) -> tuple[dict[str, object] | None, str | None]:
    """Fetch and parse the exact manifest referenced by the contents API."""
    parsed = urllib.parse.urlparse(download_url)
    required_prefix = f"/{owner}/{repo}/"
    if parsed.scheme != "https" or parsed.hostname != ALLOWED_RAW_HOST or not parsed.path.startswith(required_prefix):
        raise MetadataError(f"refusing unexpected manifest URL for {repo}")
    request = urllib.request.Request(download_url, headers={"User-Agent": "intent-solutions-omarchy-catalog/1"})
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            body = response.read(200_001)
    except (urllib.error.HTTPError, urllib.error.URLError) as error:
        raise MetadataError(f"manifest fetch failed for {repo}: {error}") from error
    if len(body) > 200_000:
        raise MetadataError(f"manifest exceeded 200 KB for {repo}")
    try:
        return json.loads(body), base64.b64encode(body).decode("ascii")
    except json.JSONDecodeError as error:
        raise MetadataError(f"manifest is invalid JSON for {repo}") from error


def fetch_repo(api_base: str, owner: str, repo: str, token: str | None) -> tuple[str, dict[str, object]]:
    """Fetch the repository record and its bounded root file inventory."""
    if not REPO_RE.fullmatch(owner) or not REPO_RE.fullmatch(repo):
        raise MetadataError(f"invalid GitHub owner or repository name: {owner}/{repo}")
    repo_url = f"{api_base}/repos/{owner}/{repo}"
    metadata = request_json(repo_url, token)
    if not isinstance(metadata, dict):
        raise MetadataError(f"repository metadata is not an object: {repo}")
    default_branch = metadata.get("default_branch")
    if not isinstance(default_branch, str) or not default_branch:
        raise MetadataError(f"repository has no default branch: {repo}")
    encoded_branch = urllib.parse.quote(default_branch, safe="")
    head = request_json(f"{repo_url}/commits/{encoded_branch}", token)
    if not isinstance(head, dict):
        raise MetadataError(f"default branch metadata is not an object: {repo}")
    commit = head.get("commit")
    committer = commit.get("committer") if isinstance(commit, dict) else None
    default_branch_updated_at = committer.get("date") if isinstance(committer, dict) else None
    if not isinstance(default_branch_updated_at, str) or not default_branch_updated_at:
        raise MetadataError(f"default branch commit has no committer date: {repo}")
    root = request_json(f"{repo_url}/contents?ref={urllib.parse.quote(default_branch)}", token)
    if not isinstance(root, list):
        raise MetadataError(f"repository root is not a file list: {repo}")
    by_name = {item.get("name"): item for item in root if isinstance(item, dict)}
    manifest_meta = by_name.get("manifest.json")
    preview_meta = by_name.get("preview.png")
    manifest = None
    manifest_body = None
    if isinstance(manifest_meta, dict) and isinstance(manifest_meta.get("download_url"), str):
        manifest, manifest_body = raw_manifest(manifest_meta["download_url"], owner, repo)
    return repo, {
        "repoUrl": metadata.get("html_url"),
        "stars": metadata.get("stargazers_count"),
        "defaultBranchUpdatedAt": default_branch_updated_at,
        "defaultBranch": default_branch,
        "archived": metadata.get("archived"),
        "openIssues": metadata.get("open_issues_count"),
        "manifest": manifest,
        "manifestBodyBase64": manifest_body,
        "manifestSha": manifest_meta.get("sha") if isinstance(manifest_meta, dict) else None,
        "preview": {
            "available": isinstance(preview_meta, dict),
            "sha": preview_meta.get("sha") if isinstance(preview_meta, dict) else None,
            "url": preview_meta.get("download_url") if isinstance(preview_meta, dict) else None,
            "path": "preview.png",
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("config", type=pathlib.Path)
    parser.add_argument("output", type=pathlib.Path)
    args = parser.parse_args()
    config = json.loads(args.config.read_text())
    github = config.get("github", {})
    api_base = github.get("api", "https://api.github.com").rstrip("/")
    parsed_api = urllib.parse.urlparse(api_base)
    if parsed_api.scheme != "https" or parsed_api.hostname != ALLOWED_API_HOST or parsed_api.path:
        raise MetadataError("plugins.json github.api must be exactly https://api.github.com")
    owner = github.get("owner")
    if not isinstance(owner, str) or not REPO_RE.fullmatch(owner):
        raise MetadataError("plugins.json github.owner is invalid")
    repos = [entry["repo"] for entry in config.get("plugins", [])]
    repos.append(config["template"]["repo"])
    if len(repos) != len(set(repos)):
        raise MetadataError("plugins.json contains a duplicate repository")
    token = os.environ.get("GITHUB_TOKEN") or None
    results: dict[str, object] = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
        futures = [executor.submit(fetch_repo, api_base, owner, repo, token) for repo in repos]
        for future in concurrent.futures.as_completed(futures):
            repo, payload = future.result()
            results[repo] = payload
    snapshot = {
        "owner": owner,
        "repos": {repo: results[repo] for repo in repos},
    }
    args.output.write_text(json.dumps(snapshot, indent=2, sort_keys=True) + "\n")
    print(f"github: fetched {len(repos)} repositories with bounded manifest and preview metadata")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
