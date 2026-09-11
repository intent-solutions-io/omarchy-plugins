#!/usr/bin/env bash
# Regenerate README and public catalogue data from marketplace and GitHub truth.
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."

MODE="${1:-write}"
if [[ "$MODE" != "write" && "$MODE" != "--check" ]]; then
  echo "usage: bash scripts/refresh-metrics.sh [--check]" >&2
  exit 64
fi

REFRESH_DIR="$(mktemp -d)"
trap 'rm -rf "$REFRESH_DIR"' EXIT

CATALOG_URL="$(python3 -c 'import json;print(json.load(open("plugins.json"))["marketplace"]["catalog"])')"
STATS_URL="$(python3 -c 'import json;print(json.load(open("plugins.json"))["marketplace"]["stats"])')"

fetch_json() {
  local url="$1"
  local destination="$2"
  local code
  code="$(curl -sS --location --max-redirs 5 --max-time 60 --max-filesize 10000000 -o "$destination" -w '%{http_code}' "$url")" || {
    echo "FETCH FAILED: $url" >&2
    exit 2
  }
  [[ "$code" == "200" ]] || {
    echo "FETCH $url returned HTTP $code" >&2
    exit 2
  }
  python3 -c "import json,sys;json.load(open(sys.argv[1]))" "$destination" || {
    echo "FETCH $url is not JSON" >&2
    exit 2
  }
}

fetch_json "$CATALOG_URL" "$REFRESH_DIR/catalog.json"
fetch_json "$STATS_URL" "$REFRESH_DIR/stats.json"
python3 scripts/fetch_github_metadata.py plugins.json "$REFRESH_DIR/github.json"

PIPELINE_MODE="write"
[[ "$MODE" == "--check" ]] && PIPELINE_MODE="check"
python3 scripts/catalog_pipeline.py \
  --config plugins.json \
  --catalog "$REFRESH_DIR/catalog.json" \
  --stats "$REFRESH_DIR/stats.json" \
  --github "$REFRESH_DIR/github.json" \
  --mode "$PIPELINE_MODE"

python3 scripts/build-site-pages.py "$MODE"
