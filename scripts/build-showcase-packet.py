#!/usr/bin/env python3
"""build-showcase-packet.py: turn one authored packet into a rendered Ezekiel email.

THE SPLIT THIS FILE ENFORCES
  scripts/showcase-packets.json holds ONLY the words. It contains no URL and no install
  command, and a lint here fails if one appears. Every link, install command and metric in
  the finished packet is appended by this script from the live marketplace catalog. That is
  the same rule blog-posting-packet.sh follows, for the same reason: a link is a fact, and a
  fact must not depend on prose being right.

  The install command in particular is read from the catalog's own installCommand field, so
  a packet can never tell Ezekiel to post a command the listing disagrees with.

Usage:
  build-showcase-packet.py <key> --out /path/email.html
  build-showcase-packet.py --list
"""
from __future__ import annotations
import argparse, json, re, subprocess, sys, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RENDERER = Path("/home/jeremy/.claude/skills/email/scripts/render-email.py")
GH_USER = "jeremylongshore"
GH_ORG = "intent-solutions-io"

def fetch(url: str):
    # A bare urllib User-Agent gets 403 from both marketplace endpoints. Identify the
    # tool honestly rather than impersonating a browser.
    req = urllib.request.Request(url, headers={
        "User-Agent": "omarchy-plugins-packet-builder (+https://github.com/intent-solutions-io/omarchy-plugins)",
        "Accept": "application/json",
    })
    with urllib.request.urlopen(req, timeout=60) as r:
        if r.status != 200:
            sys.exit(f"FETCH {url} returned HTTP {r.status}")
        return json.loads(r.read())

def lint(t: dict) -> None:
    """Refuse to build a packet whose authored copy broke the voice contract."""
    fields = ("x_post", "li_personal", "li_company")
    for f in fields:
        v = t[f]
        # Escapes, not the literal characters, so a repo-wide grep for a dash stays meaningful.
        if re.search("[\u2013\u2014]", v):
            sys.exit(f"{t['key']}/{f}: contains an em or en dash")
        if re.search(r"https?://|omarchy plugin add", v):
            sys.exit(f"{t['key']}/{f}: contains a link or install command, which this script appends")
    openers = [t[f].split("\n")[0].strip().lower() for f in fields]
    if len(set(openers)) < 3:
        sys.exit(f"{t['key']}: X and LinkedIn share an opening sentence")

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("key", nargs="?")
    ap.add_argument("--out")
    ap.add_argument("--list", action="store_true")
    a = ap.parse_args()

    packets = json.loads((ROOT / "scripts" / "showcase-packets.json").read_text())
    cfg = json.loads((ROOT / "plugins.json").read_text())
    if a.list:
        print("\n".join(t["key"] for t in packets["targets"]))
        return
    if not a.key or not a.out:
        sys.exit("need <key> and --out")

    t = next((x for x in packets["targets"] if x["key"] == a.key), None)
    if t is None:
        sys.exit(f"unknown key {a.key}")
    lint(t)

    cat = fetch(cfg["marketplace"]["catalog"])
    stats = fetch(cfg["marketplace"]["stats"])["plugins"]
    by_id = {p["id"]: p for p in cat["plugins"]}

    # --- the deterministic half: links, install command, live metrics -------------------
    links, install, tiles, listing_note = [], None, [], None
    if t.get("org_repo"):
        gh = f"https://github.com/{GH_ORG}/{t['org_repo']}"
    else:
        gh = f"https://github.com/{GH_USER}/{t['repo']}"
    links.append(("GitHub", gh))

    pid = t.get("id")
    if pid:
        entry = by_id.get(pid)
        if entry is None:
            listing_note = (
                "This plugin is NOT in the marketplace catalog right now, so there is no "
                "listing page to link. Do not post this packet.")
        else:
            links.append(("Marketplace listing",
                          cfg["marketplace"]["pluginPage"] + pid))
            install = entry.get("installCommand", "")
            s = stats.get(pid, {})
            tiles = [
                {"value": str(s.get("views", 0)), "label": "views"},
                {"value": str(s.get("copies", 0)), "label": "copies"},
                {"value": str(s.get("hearts", 0)), "label": "hearts",
                 "color": "#1a7f37" if s.get("hearts", 0) else "#9a6700"},
            ]
    else:
        links.append(("Marketplace", "https://omarchyplugins.com"))

    # --- the email spec ------------------------------------------------------------------
    blocks = []
    blocks.append({"type": "summary", "text":
        f"Posting packet for {t['subject'].split(': ',1)[1]}. Same shape as the blog packets "
        f"you run daily: the copy below is written for you, one version per platform. Copy, "
        f"paste, post. Do not rewrite it and do not mix the versions up."})
    if listing_note:
        blocks.append({"type": "card", "variant": "amber", "title": "HOLD, do not post",
                       "body": listing_note})
    if tiles:
        blocks.append({"type": "heading", "text": "Where it stands on the marketplace today"})
        blocks.append({"type": "tiles", "items": tiles})

    blocks.append({"type": "heading", "text": "Destinations for this packet"})
    blocks.append({"type": "table",
        "columns": ["Surface", "Post", "Notes"],
        "rows": [
            ["X / Twitter", "Yes", "Single post, not a thread. Jeremy's account."],
            ["LinkedIn personal", "Yes", "Jeremy's profile. Links go in the FIRST COMMENT, not the post."],
            ["LinkedIn company", "Yes", "Intent Solutions page. Links in the first comment."],
            ["X Article", "No", "Not this packet."],
            ["Substack / Medium", "No", "Not this packet."],
        ]})

    blocks.append({"type": "heading", "text": "1. X post"})
    blocks.append({"type": "card", "variant": "plain", "title": "Copy this verbatim",
                   "body": t["x_post"].replace("\n", "<br>"), "html": True})

    blocks.append({"type": "heading", "text": "2. LinkedIn, Jeremy's personal profile"})
    blocks.append({"type": "card", "variant": "plain", "title": "Copy this verbatim",
                   "body": t["li_personal"].replace("\n", "<br>"), "html": True})

    blocks.append({"type": "heading", "text": "3. LinkedIn, Intent Solutions company page"})
    blocks.append({"type": "card", "variant": "plain", "title": "Copy this verbatim",
                   "body": t["li_company"].replace("\n", "<br>"), "html": True})

    blocks.append({"type": "heading", "text": "Links (appended by the packet, not written into the copy)"})
    blocks.append({"type": "paragraph", "text":
        "These go in the FIRST COMMENT on both LinkedIn posts, so they do not suppress reach. "
        "On X, put them in a reply to your own post."})
    # Plain strings, not the renderer's {text, note} form: that form joins the two halves
    # with an em dash, and the house rule bans em dashes in anything shipped.
    link_items = [f"{name}: {url}" for name, url in links]
    if install:
        link_items.append(f"Install command (read from the marketplace catalog at build time): {install}")
    blocks.append({"type": "list", "ordered": False, "items": link_items})

    blocks.append({"type": "heading", "text": "Posting note from Jeremy"})
    blocks.append({"type": "card", "variant": "green", "title": "Read before you post",
                   "body": t["posting_note"]})

    blocks.append({"type": "divider"})
    blocks.append({"type": "paragraph", "text":
        "When you have posted, reply to this email with the three resulting URLs. That reply "
        "is how the campaign gets measured against the baseline snapshot taken today."})

    spec = {
        "title": t["subject"],
        "subtitle": t["angle"],
        "accent": "#0969da",
        "preheader": f"Three voices, ready to post. {t['angle']}",
        "blocks": blocks,
        "footer": (f"Omarchy showcase campaign {packets['campaign']}. "
                   f"Marketplace data generated at {cat['generatedAt']}. "
                   "Generated by scripts/build-showcase-packet.py in "
                   "intent-solutions-io/omarchy-plugins."),
    }

    spec_path = Path(a.out).with_suffix(".spec.json")
    spec_path.write_text(json.dumps(spec, indent=1))
    subprocess.run([sys.executable, str(RENDERER), str(spec_path), "--out", a.out], check=True)
    print(a.out)

if __name__ == "__main__":
    main()
