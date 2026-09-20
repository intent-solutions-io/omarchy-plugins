#!/usr/bin/env python3
"""Put the canonical estate bar into the hand-authored Omarchy pages. Idempotent.

The 16 plugin detail pages are generated and get the bar from
build-site-pages.py; this script owns every other carrier. The bar goes first in
<body>, after the skip link. The stylesheet link reuses the page's own path
prefix to assets/ (relative on most pages, absolute on 404.html) and is placed
before styles.css so the site's accent override wins.

    python3 scripts/stamp-estate-bar.py          # stamp every carrier
    python3 scripts/stamp-estate-bar.py --list   # print carriers, one per line
    python3 scripts/stamp-estate-bar.py --audit  # fail on a page that is neither carrier nor exempt
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FRAGMENT = (ROOT / "vendor/estate-bar/fragments/estate-bar.omarchy.html").read_text().strip()

# Hand-authored first-party pages that carry the bar.
CARRIERS = [
    "site/index.html",
    "site/404.html",
    "site/bluegoldblue/index.html",
    "site/the-beacon-wakes/index.html",
    "site/privacy/index.html",
    "site/terms/index.html",
    "site/acceptable-use/index.html",
    "site/app-privacy/index.html",
]
# Deliberately without the bar. --audit fails on any page that is neither a
# carrier, a generated plugin page, nor under one of these prefixes:
#   site/the-beacon-wakes/play/   child-facing game, build output of another repo
#   site/the-beacon-wakes/thanks/ post-signup confirmation, a dead-end by design
#   site/perception/              hashed build bundle of another repo
#   site/omaquest/                instant redirect to the-beacon-wakes, never rendered

EXEMPT = ["site/the-beacon-wakes/play/", "site/the-beacon-wakes/thanks/", "site/perception/", "site/omaquest/"]
GENERATED = "site/plugins/"

BLOCK = re.compile(r"[ \t]*<!-- estate-bar:start[^>]*-->.*?<!-- estate-bar:end -->\n?", re.S)
BODY = re.compile(r"(<body[^>]*>\s*(?:<a[^>]*class=\"[^\"]*skip[^\"]*\"[^>]*>.*?</a>[ \t]*\n?)?)", re.S | re.I)
STYLES = re.compile(r'([ \t]*)<link rel="stylesheet" href="([^"]*?)assets/styles\.css">')


def stamp(path: Path) -> str:
    html = path.read_text(encoding="utf-8")
    original = html
    bar = "\n".join("  " + line for line in FRAGMENT.splitlines()) + "\n"
    html = BLOCK.sub("", html)
    if not BODY.search(html):
        raise SystemExit(f"{path}: no <body> tag found")
    html = BODY.sub(lambda m: m.group(1).rstrip(" \t") + ("" if m.group(1).endswith("\n") else "\n") + bar, html, count=1)
    if "assets/estate-bar/estate-bar.css" not in html:
        match = STYLES.search(html)
        if not match:
            raise SystemExit(f"{path}: no styles.css link to anchor the estate bar stylesheet")
        indent, prefix = match.group(1), match.group(2)
        link = f'{indent}<link rel="stylesheet" href="{prefix}assets/estate-bar/estate-bar.css">\n'
        html = html[: match.start()] + link + html[match.start():]
    if html != original:
        path.write_text(html, encoding="utf-8")
        return "stamped"
    return "already current"


if __name__ == "__main__":
    if "--audit" in sys.argv:
        unknown = [
            str(page.relative_to(ROOT))
            for page in sorted((ROOT / "site").rglob("*.html"))
            if str(page.relative_to(ROOT)) not in CARRIERS
            and not str(page.relative_to(ROOT)).startswith(GENERATED)
            and not any(str(page.relative_to(ROOT)).startswith(prefix) for prefix in EXEMPT)
        ]
        for page in unknown:
            print(f"FAIL: {page} neither carries the estate bar nor is a named exemption", file=sys.stderr)
        raise SystemExit(1 if unknown else 0)
    if "--list" in sys.argv:
        print("\n".join(CARRIERS))
        raise SystemExit(0)
    for rel in CARRIERS:
        print(f"{stamp(ROOT / rel)}: {rel}")
