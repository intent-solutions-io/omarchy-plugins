#!/usr/bin/env python3
"""Generate one stable, shareable portfolio page for every Omarchy plugin."""

from __future__ import annotations

import html
import json
import pathlib
import shutil
import sys


ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "site" / "data" / "plugins.json"
PAGES_ROOT = ROOT / "site" / "plugins"


def esc(value: object) -> str:
    """Escape a value for safe inclusion in generated HTML."""
    return html.escape(str(value if value is not None else ""), quote=True)


def page_for(plugin: dict[str, object]) -> str:
    """Render the permanent public detail page for one plugin."""
    listed = plugin["lifecycle"] == "listed"
    status = "Listed" if listed else "In review"
    status_class = "listed" if listed else "review"
    primary_url = plugin["marketplaceUrl"] if listed else plugin["submissionUrl"]
    primary_label = "Official marketplace listing" if listed else "Marketplace review record"
    install = plugin.get("installCommand")
    install_block = (
        f"""<section class="detail-install" aria-labelledby="install-title">
          <p class="eyebrow">Install</p>
          <h2 id="install-title">Add it from the verified source.</h2>
          <div class="install-command"><code>{esc(install)}</code><button type="button" data-detail-copy>Copy command</button></div>
          <p>Review the source and requested capabilities before installing any community plugin.</p>
        </section>"""
        if install
        else f"""<section class="detail-install review-panel" aria-labelledby="install-title">
          <p class="eyebrow">Marketplace status</p>
          <h2 id="install-title">Review is still in progress.</h2>
          <p>There is no official marketplace install command yet. Follow the public review record for the current decision.</p>
          <a class="button button-primary" href="{esc(primary_url)}">Open review record</a>
        </section>"""
    )
    metrics = plugin.get("metrics")
    metrics_markup = (
        f"""<dl class="detail-facts">
          <div><dt>Views</dt><dd>{esc(metrics['views'])}</dd></div>
          <div><dt>Copies</dt><dd>{esc(metrics['copies'])}</dd></div>
          <div><dt>Hearts</dt><dd>{esc(metrics['hearts'])}</dd></div>
          <div><dt>Version</dt><dd>{esc(plugin.get('version') or 'Current source')}</dd></div>
        </dl>"""
        if metrics
        else """<dl class="detail-facts">
          <div><dt>Stage</dt><dd>Human review</dd></div>
          <div><dt>Source</dt><dd>Public</dd></div>
          <div><dt>Preview</dt><dd>Published</dd></div>
          <div><dt>Install</dt><dd>Pending</dd></div>
        </dl>"""
    )
    canonical = f"https://oma.intentsolutions.io/plugins/{plugin['slug']}/"
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
  <meta property="og:image" content="{esc(plugin['previewUrl'])}">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="canonical" href="{esc(canonical)}">
  <title>{esc(plugin['name'])} | Intent Solutions Omarchy Plugins</title>
  <link rel="icon" href="../../assets/mark.svg" type="image/svg+xml">
  <link rel="stylesheet" href="../../assets/styles.css">
  <script src="../../assets/detail.js" defer></script>
</head>
<body class="detail-page" data-install-command="{esc(install)}">
  <a class="skip-link" href="#plugin-detail">Skip to plugin details</a>
  <header class="site-header">
    <a class="wordmark" href="../../" aria-label="Intent Solutions Omarchy Plugins home"><span class="wordmark-company">Intent Solutions</span><span class="wordmark-product">Omarchy Plugins</span></a>
    <nav aria-label="Primary navigation"><a href="../../#catalog">All plugins</a><a href="{esc(plugin['repoUrl'])}">GitHub</a><a href="{esc(primary_url)}">Marketplace</a></nav>
  </header>
  <main id="plugin-detail" class="plugin-detail">
    <p class="detail-breadcrumb"><a href="../../#catalog">All plugins</a> / {esc(plugin['category'])}</p>
    <section class="detail-hero">
      <div>
        <span class="status-badge {status_class}">{status}</span>
        <h1>{esc(plugin['name'])}</h1>
        <p class="detail-lede">{esc(plugin['pitch'])}</p>
        <div class="hero-actions">
          <a class="button button-primary" href="{esc(primary_url)}">{primary_label}</a>
          <a class="button button-quiet" href="{esc(plugin['repoUrl'])}">Inspect source</a>
        </div>
      </div>
      <figure class="detail-preview"><img src="{esc(plugin['previewUrl'])}" alt="{esc(plugin['name'])} plugin interface" width="1280" height="720"><figcaption>Interface preview from the public repository.</figcaption></figure>
    </section>
    {metrics_markup}
    {install_block}
    <section class="detail-proof" aria-labelledby="proof-title">
      <p class="eyebrow">Verify it yourself</p>
      <h2 id="proof-title">Follow the work to the source.</h2>
      <div><a href="{esc(plugin['repoUrl'])}"><strong>GitHub repository</strong><span>Code, tests, documentation, and release history</span></a><a href="{esc(primary_url)}"><strong>{primary_label}</strong><span>The authority for marketplace lifecycle status</span></a></div>
    </section>
  </main>
  <footer><div><p class="footer-brand">Intent Solutions Omarchy Plugins</p><p>Open source, real screenshots, and marketplace status with receipts.</p></div><p><a href="https://intentsolutions.io">Intent Solutions</a></p></footer>
  <div class="toast" id="toast" role="status" aria-live="polite"></div>
</body>
</html>
"""


def main() -> int:
    """Write detail pages or verify that committed pages are current."""
    mode = sys.argv[1] if len(sys.argv) > 1 else "write"
    data = json.loads(DATA_PATH.read_text())
    expected = {plugin["slug"]: page_for(plugin) for plugin in data["plugins"]}

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
        print(f"fresh: {len(expected)} individual plugin pages match site data.")
        return 0

    PAGES_ROOT.mkdir(parents=True, exist_ok=True)
    for child in PAGES_ROOT.iterdir():
        if child.is_dir() and child.name not in expected:
            shutil.rmtree(child)
    for slug, content in expected.items():
        path = PAGES_ROOT / slug / "index.html"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)
    print(f"updated: {len(expected)} individual plugin pages.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
