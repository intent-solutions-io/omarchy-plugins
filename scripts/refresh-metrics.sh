#!/usr/bin/env bash
# refresh-metrics.sh: regenerate the live metrics table in README.md from the two
# real marketplace endpoints.
#
# WHY THIS EXISTS
#   A hand-maintained view/copy/heart column in a README rots inside a week at this
#   marketplace's pace. This script is the only thing allowed to write that table.
#
# HOW IT STAYS HONEST
#   * The id list comes from plugins.json, never from the catalog. If the marketplace
#     renames or drops an id, the row survives and reads "not listed" instead of
#     silently vanishing from the table.
#   * The install command is READ FROM THE CATALOG, not authored here. A README that
#     prints an install command the marketplace does not agree with is worse than one
#     with no install command.
#   * The freshness stamp is the catalog's OWN generatedAt, not the local clock, so
#     two runs against the same upstream data produce a byte-identical block.
#
# Usage:
#   bash scripts/refresh-metrics.sh            # rewrite README.md in place
#   bash scripts/refresh-metrics.sh --check    # exit 1 if the table is stale (CI)
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."

MODE="${1:-write}"
TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT

CATALOG_URL="$(python3 -c 'import json;print(json.load(open("plugins.json"))["marketplace"]["catalog"])')"
STATS_URL="$(python3 -c 'import json;print(json.load(open("plugins.json"))["marketplace"]["stats"])')"

fetch() { # url dest: fail loudly, never write a partial file
  local code
  code="$(curl -sS --max-time 60 -o "$2" -w '%{http_code}' "$1")" || { echo "FETCH FAILED: $1" >&2; exit 2; }
  [ "$code" = "200" ] || { echo "FETCH $1 returned HTTP $code" >&2; exit 2; }
  python3 -c "import json,sys;json.load(open(sys.argv[1]))" "$2" || { echo "FETCH $1 is not JSON" >&2; exit 2; }
}
fetch "$CATALOG_URL" "$TMP/catalog.json"
fetch "$STATS_URL"   "$TMP/stats.json"

python3 - "$TMP/catalog.json" "$TMP/stats.json" "$MODE" <<'PY'
import json, sys, re, pathlib

catalog_p, stats_p, mode = sys.argv[1], sys.argv[2], sys.argv[3]
cat = json.load(open(catalog_p))
stats = json.load(open(stats_p))["plugins"]
by_id = {p["id"]: p for p in cat["plugins"]}
cfg = json.load(open("plugins.json"))
page = cfg["marketplace"]["pluginPage"]

rows, install_rows, unlisted = [], [], []
for e in cfg["plugins"]:
    pid, name, repo = e["id"], e["name"], e["repo"]
    gh = f"https://github.com/jeremylongshore/{repo}"
    c = by_id.get(pid)
    s = stats.get(pid)
    if c is None:
        unlisted.append(name)
        rows.append(f"| **{name}** | {e['pitch']} | [repo]({gh}) | not listed | not listed | not listed | not listed |")
        continue
    v = s.get("views", 0) if s else 0
    cp = s.get("copies", 0) if s else 0
    h = s.get("hearts", 0) if s else 0
    rows.append(
        f"| **{name}** | {e['pitch']} | [repo]({gh}) | [{c['category']}]({page}{pid}) | {v} | {cp} | {h} |")
    install_rows.append((name, c.get("installCommand", "")))

tmpl = cfg["template"]
gh_t = f"https://github.com/jeremylongshore/{tmpl['repo']}"
rows.append(f"| **Widget Template** | {tmpl['pitch']} | [repo]({gh_t}) | not a listing | n/a | n/a | n/a |")

listed = [e for e in cfg["plugins"] if e["id"] in by_id]
tot_v = sum(stats.get(e["id"], {}).get("views", 0) for e in listed)
tot_c = sum(stats.get(e["id"], {}).get("copies", 0) for e in listed)
tot_h = sum(stats.get(e["id"], {}).get("hearts", 0) for e in listed)

block = []
block.append(f"Marketplace data generated at `{cat['generatedAt']}`, across "
             f"{len(cat['plugins'])} listed plugins. Regenerate with "
             f"`bash scripts/refresh-metrics.sh`; do not edit this table by hand.")
block.append("")
block.append("| Plugin | What it does | Source | Category | Views | Copies | Hearts |")
block.append("| --- | --- | --- | --- | --: | --: | --: |")
block.extend(rows)
block.append("")
block.append(f"**{len(listed)} of {len(cfg['plugins'])} listed and verified** on the marketplace, "
             f"{tot_v} views, {tot_c} copies, {tot_h} hearts.")
if unlisted:
    block.append("")
    block.append(f"Not currently in the catalog: {', '.join(unlisted)}. See "
                 "[000-docs/002-LS-BLOK-listening-post-listing-blocked.md]"
                 "(000-docs/002-LS-BLOK-listening-post-listing-blocked.md) for why, and what unblocks it.")
block.append("")
block.append("### Install")
block.append("")
block.append("Every command below is read from the marketplace catalog's own `installCommand` "
             "field at refresh time, so it cannot drift from what the listing says.")
block.append("")
block.append("```bash")
for name, cmdline in install_rows:
    block.append(f"# {name}")
    block.append(cmdline)
block.append("```")

new = "\n".join(block)
readme = pathlib.Path("README.md")
text = readme.read_text()
START, END = "<!-- METRICS:START -->", "<!-- METRICS:END -->"
if START not in text or END not in text:
    print("README.md is missing the METRICS markers", file=sys.stderr); sys.exit(3)
out = re.sub(re.escape(START) + r".*?" + re.escape(END),
             START + "\n" + new + "\n" + END, text, flags=re.S)

if mode == "--check":
    if out != text:
        print("STALE: README metrics table does not match live marketplace data.", file=sys.stderr)
        sys.exit(1)
    print("fresh: README metrics table matches live marketplace data.")
    sys.exit(0)

if out == text:
    print("no change: README metrics table already current.")
else:
    readme.write_text(out)
    print(f"updated: {len(listed)}/{len(cfg['plugins'])} listed, {tot_v} views, {tot_c} copies, {tot_h} hearts.")
PY
