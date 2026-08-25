#!/usr/bin/env python3
"""campaign-baseline.py: snapshot what the numbers were before a promotion campaign.

WHY THIS AND NOT UTM TAGS
  The obvious move is to UTM tag the marketplace links. It does not work here: the analytics
  for omarchyplugins.com belong to the marketplace, not to us, so a utm_source we attach is
  a parameter nobody on our side can ever read back. Attaching one would look like
  measurement without being measurement.

  Two things ARE readable:
    1. The marketplace's own per plugin views, copies and hearts, from the public stats
       endpoint. Snapshot before, compare after. That is the conversion metric that matters,
       because copies is the closest thing the marketplace has to an install.
    2. GitHub's traffic API on repos we own, which reports referrer hostnames natively.
       x.com versus linkedin.com arrives already separated, with no tagging required, which
       is why the packets do not carry UTM parameters on the GitHub links either.

  GitHub traffic data is a rolling 14 day window and is not backfillable, so the baseline
  has to be taken on the day the campaign starts. That is what this script is for.

Usage:
  campaign-baseline.py --out 000-docs/003-RP-BASE-showcase-campaign-baseline.md
  campaign-baseline.py --compare 000-docs/003-RP-BASE-showcase-campaign-baseline.md
"""
from __future__ import annotations
import argparse, json, re, subprocess, sys, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
UA = {"User-Agent": "omarchy-plugins-campaign-baseline (+https://github.com/intent-solutions-io/omarchy-plugins)",
      "Accept": "application/json"}

def fetch(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
        return json.loads(r.read())

def gh_traffic(repo):
    """Clones and unique cloners for a repo we own. Returns None if the API refuses."""
    try:
        out = subprocess.run(["gh", "api", f"repos/jeremylongshore/{repo}/traffic/views"],
                             capture_output=True, text=True, timeout=40)
        if out.returncode != 0:
            return None
        d = json.loads(out.stdout)
        return {"views": d.get("count", 0), "uniques": d.get("uniques", 0)}
    except Exception:
        return None

def collect():
    cfg = json.loads((ROOT / "plugins.json").read_text())
    cat = fetch(cfg["marketplace"]["catalog"])
    stats = fetch(cfg["marketplace"]["stats"])["plugins"]
    by_id = {p["id"]: p for p in cat["plugins"]}
    rows = []
    for e in cfg["plugins"] + [{"id": None, "name": "Widget Template", "repo": cfg["template"]["repo"]}]:
        s = stats.get(e["id"], {}) if e["id"] else {}
        rows.append({
            "name": e["name"],
            "repo": e["repo"],
            "listed": e["id"] in by_id if e["id"] else None,
            "views": s.get("views"), "copies": s.get("copies"), "hearts": s.get("hearts"),
            "gh": gh_traffic(e["repo"]),
        })
    return cat["generatedAt"], len(cat["plugins"]), rows

def fmt(v):
    return "n/a" if v is None else str(v)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out")
    ap.add_argument("--compare")
    a = ap.parse_args()
    gen, total, rows = collect()

    if a.compare:
        prior = Path(a.compare).read_text()
        base = {m.group(1).strip(): m for m in re.finditer(
            r"^\| \*\*(.+?)\*\* \| (\S+) \| (\S+) \| (\S+) \|", prior, re.M)}
        print(f"{'plugin':18} {'views':>16} {'copies':>16} {'hearts':>16}")
        for r in rows:
            m = base.get(r["name"])
            if not m:
                continue
            def d(now, was):
                if now is None or was in ("n/a", "not listed"):
                    return "n/a"
                return f"{was} -> {now} ({int(now) - int(was):+d})"
            print(f"{r['name']:18} {d(r['views'], m.group(2)):>16} "
                  f"{d(r['copies'], m.group(3)):>16} {d(r['hearts'], m.group(4)):>16}")
        return

    lines = [
        "# Showcase campaign baseline",
        "",
        f"**Taken:** marketplace snapshot `{gen}`, across {total} listed plugins.",
        "**Campaign:** `omarchy-showcase-2026-08`, nine packets to Ezekiel on 2026-08-25.",
        "",
        "## Why a baseline instead of UTM tags",
        "",
        "The marketplace links in the packets carry no UTM parameters, on purpose. The",
        "analytics for omarchyplugins.com belong to the marketplace, so a `utm_source` we",
        "attach is a parameter nobody on this side can read back. It would be the appearance",
        "of measurement rather than measurement.",
        "",
        "Two signals are genuinely readable, and both are captured below.",
        "",
        "1. **The marketplace's own counters.** Views, copies and hearts per plugin, from the",
        "   public stats endpoint. Copies is the closest thing the marketplace exposes to an",
        "   install, so copies is the conversion metric.",
        "2. **GitHub traffic on repos we own.** GitHub reports referrer hostnames natively, so",
        "   x.com and linkedin.com arrive already separated with no tagging needed. That is",
        "   also why the GitHub links in the packets are untagged.",
        "",
        "GitHub traffic is a rolling 14 day window and cannot be backfilled, which is why this",
        "had to be taken on the day the packets went out.",
        "",
        "## Baseline",
        "",
        "| Plugin | Views | Copies | Hearts | GitHub views (14d) | GitHub uniques |",
        "| --- | --: | --: | --: | --: | --: |",
    ]
    for r in rows:
        gh = r["gh"] or {}
        v = "not listed" if r["listed"] is False else fmt(r["views"])
        c = "not listed" if r["listed"] is False else fmt(r["copies"])
        h = "not listed" if r["listed"] is False else fmt(r["hearts"])
        lines.append(f"| **{r['name']}** | {v} | {c} | {h} | "
                     f"{fmt(gh.get('views'))} | {fmt(gh.get('uniques'))} |")
    lines += [
        "",
        "## How to read it afterwards",
        "",
        "```bash",
        "python3 scripts/campaign-baseline.py --compare 000-docs/003-RP-BASE-showcase-campaign-baseline.md",
        "gh api repos/jeremylongshore/omarchy-bazaar-entry/traffic/popular/referrers",
        "```",
        "",
        "The second command is the one that answers which voice moved anything, because it",
        "splits by referrer hostname. Run it inside 14 days of the posts or the window will",
        "have rolled past them.",
        "",
        "## The two questions worth answering",
        "",
        "1. **Do hearts move at all?** Bazaar and Wait State are at zero on 199 and 100 views.",
        "   Hearts are the social proof the listing page renders, and nothing in the product",
        "   asks for one. If a campaign cannot move that number, the fix is on the listing",
        "   page, not in the posting.",
        "2. **Does X or LinkedIn convert better here?** The audience is Arch and Hyprland",
        "   users, which argues for X, but the LinkedIn copy carries the engineering argument",
        "   and this set's differentiator is engineering. The referrer split settles it, and",
        "   it settles it for every campaign after this one.",
    ]
    Path(a.out).write_text("\n".join(lines) + "\n")
    print(a.out)

if __name__ == "__main__":
    main()
