#!/usr/bin/env python3
"""Generate stable plugin detail pages and the no-JavaScript catalogue."""

from __future__ import annotations

import html
import json
import pathlib
import shutil
import sys


ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "site" / "data" / "plugins.json"
PAGES_ROOT = ROOT / "site" / "plugins"
INDEX_PATH = ROOT / "site" / "index.html"
STATIC_START = "<!-- STATIC_CATALOG:START -->"
STATIC_END = "<!-- STATIC_CATALOG:END -->"
LIFECYCLE_LABELS = {
    "listed": "Officially listed",
    "under-review": "In marketplace review",
    "developing": "In development",
    "unreleased": "Unreleased",
    "not-listed": "Not listed",
    "retired": "Retired",
}


def esc(value: object) -> str:
    """Escape a value for safe inclusion in generated HTML."""
    return html.escape(str(value if value is not None else ""), quote=True)


def lifecycle_label(value: object) -> str:
    lifecycle = str(value or "not-listed")
    return LIFECYCLE_LABELS.get(lifecycle, lifecycle.replace("-", " ").title())


def iso_day(value: object) -> str:
    text = str(value or "")
    return text[:10] if len(text) >= 10 else "Unknown"


def preview_markup(plugin: dict[str, object]) -> str:
    preview = plugin.get("preview") if isinstance(plugin.get("preview"), dict) else {}
    github = plugin.get("github") if isinstance(plugin.get("github"), dict) else {}
    if preview.get("status") != "verified" or not preview.get("url"):
        return f"""<div class="detail-preview preview-missing" role="img" aria-label="No verified preview is currently available for {esc(plugin['name'])}">
        <strong>Preview unavailable</strong><span>The repository remains the source of truth.</span>
      </div>"""
    source_url = f"{plugin['repoUrl']}/blob/{github.get('defaultBranch', 'main')}/{preview.get('path', 'preview.png')}"
    short_sha = str(preview.get("sha") or "")[:12]
    provenance = f"Repository preview, blob {short_sha}" if short_sha else "Repository preview"
    return f"""<figure class="detail-preview">
        <a href="{esc(source_url)}"><img src="{esc(preview['url'])}" alt="{esc(plugin['name'])} plugin interface" width="1280" height="720"></a>
        <figcaption>{esc(provenance)}. Open the image source to verify it.</figcaption>
      </figure>"""


def marketplace_markup(plugin: dict[str, object]) -> tuple[str, str]:
    marketplace_url = plugin.get("marketplaceUrl")
    submission_url = plugin.get("submissionUrl")
    if marketplace_url:
        link = f'<a class="button button-primary" href="{esc(marketplace_url)}">Official marketplace listing</a>'
        proof = f'<a href="{esc(marketplace_url)}"><strong>Official marketplace listing</strong><span>Lifecycle status and verified install command</span></a>'
        return link, proof
    if submission_url:
        link = f'<a class="button button-primary" href="{esc(submission_url)}">Marketplace review record</a>'
        proof = f'<a href="{esc(submission_url)}"><strong>Marketplace review record</strong><span>Public review status while the listing is pending</span></a>'
        return link, proof
    state = lifecycle_label(plugin.get("lifecycle"))
    return (
        f'<span class="detail-lifecycle-note">Marketplace: {esc(state)}</span>',
        f'<div class="proof-status"><strong>Marketplace</strong><span>{esc(state)}. No official listing link is published.</span></div>',
    )


def install_markup(plugin: dict[str, object]) -> str:
    install = plugin.get("installCommand")
    if install:
        return f"""<section class="detail-install" aria-labelledby="install-title">
          <h2 id="install-title">Add it from the verified source.</h2>
          <div class="install-command"><code>{esc(install)}</code><button type="button" data-detail-copy>Copy command</button></div>
          <p>Review the source and requested capabilities before installing any community plugin.</p>
        </section>"""
    return f"""<section class="detail-install review-panel" aria-labelledby="install-title">
          <h2 id="install-title">No official install command yet.</h2>
          <p>{esc(lifecycle_label(plugin.get('lifecycle')))}. Inspect the public repository while marketplace status develops.</p>
          <a class="button button-quiet" href="{esc(plugin['repoUrl'])}">Inspect GitHub source</a>
        </section>"""


def facts_markup(plugin: dict[str, object]) -> str:
    metrics = plugin.get("metrics") if isinstance(plugin.get("metrics"), dict) else {}
    github = plugin.get("github") if isinstance(plugin.get("github"), dict) else {}
    manifest = plugin.get("manifest") if isinstance(plugin.get("manifest"), dict) else {}
    items = [
        ("GitHub stars", github.get("stars", 0)),
        ("Repository updated", iso_day(github.get("pushedAt"))),
        ("Manifest", str(manifest.get("status", "unknown")).replace("-", " ").title()),
        ("Version", plugin.get("version") or manifest.get("version") or "Current source"),
    ]
    if metrics:
        items.extend([
            ("Marketplace views", metrics.get("views", 0)),
            ("Install copies", metrics.get("copies", 0)),
        ])
    return '<dl class="detail-facts">' + "".join(
        f"<div><dt>{esc(label)}</dt><dd>{esc(value)}</dd></div>" for label, value in items
    ) + "</dl>"


def source_status_markup(plugin: dict[str, object]) -> str:
    manifest = plugin.get("manifest") if isinstance(plugin.get("manifest"), dict) else {}
    preview = plugin.get("preview") if isinstance(plugin.get("preview"), dict) else {}
    issues = manifest.get("issues") if isinstance(manifest.get("issues"), list) else []
    issue_markup = "".join(f"<li>{esc(issue)}</li>" for issue in issues)
    if not issue_markup:
        issue_markup = "<li>Repository identity and version agree with the canonical inventory and marketplace.</li>"
    return f"""<section class="detail-source-status" aria-labelledby="source-status-title">
      <div><h2 id="source-status-title">Source status</h2><p>Derived from the repository root during the catalogue refresh.</p></div>
      <dl>
        <div><dt>Manifest</dt><dd data-manifest-status="{esc(manifest.get('status'))}">{esc(str(manifest.get('status', 'unknown')).replace('-', ' ').title())}</dd></div>
        <div><dt>Screenshot</dt><dd>{esc(str(preview.get('status', 'unknown')).replace('-', ' ').title())}</dd></div>
      </dl>
      <ul>{issue_markup}</ul>
    </section>"""


def page_for(plugin: dict[str, object]) -> str:
    """Render the permanent public detail page for one plugin."""
    lifecycle = str(plugin.get("lifecycle", "not-listed"))
    marketplace_action, marketplace_proof = marketplace_markup(plugin)
    canonical = f"https://oma.intentsolutions.io/plugins/{plugin['slug']}/"
    marketplace_nav = f'<a href="{esc(plugin["marketplaceUrl"])}">Marketplace</a>' if plugin.get("marketplaceUrl") else ""
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{esc(plugin['pitch'])}">
  <meta name="theme-color" content="#f6f6f4">
  <meta property="og:title" content="{esc(plugin['name'])} | Intent Solutions Omarchy Plugins">
  <meta property="og:description" content="{esc(plugin['pitch'])}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{esc(canonical)}">
  <meta property="og:image" content="{esc(plugin.get('previewUrl') or 'https://oma.intentsolutions.io/assets/og-card.png')}">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="canonical" href="{esc(canonical)}">
  <title>{esc(plugin['name'])} | Intent Solutions Omarchy Plugins</title>
  <link rel="icon" href="../../assets/mark.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600&family=JetBrains+Mono:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../../assets/styles.css">
  <script src="../../assets/detail.js" defer></script>
</head>
<body class="detail-page" data-install-command="{esc(plugin.get('installCommand'))}">
  <a class="skip-link" href="#plugin-detail">Skip to plugin details</a>
  <header class="site-header">
    <a class="wordmark" href="../../" aria-label="Intent Solutions Omarchy Plugins home"><span class="wordmark-company">Intent Solutions</span><span class="wordmark-product">Omarchy Plugins</span></a>
    <nav aria-label="Primary navigation"><a href="../../#catalog">All plugins</a><a href="{esc(plugin['repoUrl'])}">GitHub</a>{marketplace_nav}</nav>
  </header>
  <main id="plugin-detail" class="plugin-detail">
    <p class="detail-breadcrumb"><a href="../../#catalog">All plugins</a> / {esc(plugin['family'])}</p>
    <section class="detail-hero">
      <div>
        <span class="status-badge {esc(lifecycle)}">{esc(lifecycle_label(lifecycle))}</span>
        <h1>{esc(plugin['name'])}</h1>
        <p class="detail-family">{esc(plugin['family'])}</p>
        <p class="detail-lede">{esc(plugin['pitch'])}</p>
        <div class="hero-actions">{marketplace_action}<a class="button button-quiet" href="{esc(plugin['repoUrl'])}">GitHub repository</a></div>
      </div>
      {preview_markup(plugin)}
    </section>
    {facts_markup(plugin)}
    {source_status_markup(plugin)}
    {install_markup(plugin)}
    <section class="detail-proof" aria-labelledby="proof-title">
      <h2 id="proof-title">Follow the work to the source.</h2>
      <div><a href="{esc(plugin['repoUrl'])}"><strong>GitHub repository</strong><span>Code, tests, documentation, releases, and issue history</span></a>{marketplace_proof}</div>
    </section>
  </main>
  <footer><div><p class="footer-brand">Intent Solutions Omarchy Plugins</p><p>Open source, repository screenshots, and marketplace status with receipts.</p></div><div class="footer-meta"><p><a href="https://intentsolutions.io">Intent Solutions</a></p><nav class="footer-links" aria-label="Legal"><a href="../../privacy/">Privacy</a><a href="../../app-privacy/">App privacy</a><a href="../../acceptable-use/">Acceptable use</a><a href="../../terms/">Terms</a></nav></div></footer>
  <div class="toast" id="toast" role="status" aria-live="polite"></div>
</body>
</html>
"""


def static_catalog(data: dict[str, object]) -> str:
    items = []
    for plugin in data["plugins"]:
        marketplace = (
            f' <a href="{esc(plugin["marketplaceUrl"])}">Marketplace</a>'
            if plugin.get("marketplaceUrl")
            else ""
        )
        items.append(
            f'<li><a href="plugins/{esc(plugin["slug"])}/"><strong>{esc(plugin["name"])}</strong></a> '
            f'<span>{esc(plugin["family"])}. {esc(lifecycle_label(plugin["lifecycle"]))}.</span> '
            f'<a href="{esc(plugin["repoUrl"])}">GitHub</a>{marketplace}</li>'
        )
    return """<noscript>
        <section class="static-catalog" aria-labelledby="static-catalog-title">
          <h3 id="static-catalog-title">Complete plugin index</h3>
          <p>JavaScript is off. Every plugin and source link remains available.</p>
          <ul>""" + "".join(items) + """</ul>
        </section>
      </noscript>"""


def replace_static_catalog(index: str, generated: str) -> str:
    if STATIC_START not in index or STATIC_END not in index:
        raise ValueError("site/index.html is missing STATIC_CATALOG markers")
    before, remainder = index.split(STATIC_START, 1)
    _, after = remainder.split(STATIC_END, 1)
    return f"{before}{STATIC_START}\n      {generated}\n      {STATIC_END}{after}"


def main() -> int:
    """Write generated surfaces or verify that committed surfaces are current."""
    mode = sys.argv[1] if len(sys.argv) > 1 else "write"
    data = json.loads(DATA_PATH.read_text())
    expected = {plugin["slug"]: page_for(plugin) for plugin in data["plugins"]}
    current_index = INDEX_PATH.read_text()
    expected_index = replace_static_catalog(current_index, static_catalog(data))

    if mode == "--check":
        actual_slugs = {path.name for path in PAGES_ROOT.iterdir() if path.is_dir()} if PAGES_ROOT.exists() else set()
        if actual_slugs != set(expected):
            print("STALE: generated plugin page set does not match site data.", file=sys.stderr)
            return 1
        for slug, content in expected.items():
            path = PAGES_ROOT / slug / "index.html"
            if not path.exists() or path.read_text() != content:
                print(f"STALE: generated plugin page differs: {slug}", file=sys.stderr)
                return 1
        if current_index != expected_index:
            print("STALE: no-JavaScript catalogue differs from site data.", file=sys.stderr)
            return 1
        print(f"fresh: {len(expected)} individual plugin pages and static catalogue match site data.")
        return 0

    PAGES_ROOT.mkdir(parents=True, exist_ok=True)
    for child in PAGES_ROOT.iterdir():
        if child.is_dir() and child.name not in expected:
            shutil.rmtree(child)
    for slug, content in expected.items():
        path = PAGES_ROOT / slug / "index.html"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)
    if current_index != expected_index:
        INDEX_PATH.write_text(expected_index)
    print(f"updated: {len(expected)} individual plugin pages and static catalogue.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
