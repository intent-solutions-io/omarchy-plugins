#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."

node --check site/assets/app.js
node --check site/assets/detail.js
node --check site/assets/beacon-signup.js
node --check site/assets/bluegold-interest.js
python3 -m py_compile scripts/catalog_pipeline.py scripts/fetch_github_metadata.py scripts/build-site-pages.py tests/test_catalog_pipeline.py
python3 -m unittest discover -s tests -p 'test_*.py'
node --test tests/site-data.test.mjs
python3 scripts/build-site-pages.py --check

for required in site/404.html site/robots.txt site/sitemap.xml site/assets/mark.svg; do
  test -s "$required" || { echo "FAIL: missing $required" >&2; exit 1; }
done

while IFS= read -r page; do
  rg -q '<title>[^<]+' "$page" || { echo "FAIL: $page has no title" >&2; exit 1; }
  rg -q '<meta name="description" content="[^"]+' "$page" || { echo "FAIL: $page has no meta description" >&2; exit 1; }
  rg -q '<link rel="icon"' "$page" || { echo "FAIL: $page has no favicon" >&2; exit 1; }
  case "$page" in
    site/privacy/*|site/app-privacy/*|site/acceptable-use/*|site/terms/*) ;;
    *) rg -q 'analytics\.intentsolutions\.io/script\.js' "$page" || { echo "FAIL: $page has no analytics" >&2; exit 1; } ;;
  esac
  if rg -q '<img\b' "$page" && rg '<img\b' "$page" | rg -vq '\balt="[^"]*"'; then
    echo "FAIL: $page contains an image without alt text" >&2
    exit 1
  fi
done < <(find site -type f -name '*.html' -print | LC_ALL=C sort)

rg -q 'Sitemap: https://oma\.intentsolutions\.io/sitemap\.xml' site/robots.txt || {
  echo "FAIL: robots.txt does not advertise the sitemap" >&2
  exit 1
}

if rg -n '[–—]' site README.md plugins.json; then
  echo "FAIL: public portfolio copy contains an em dash or en dash." >&2
  exit 1
fi

echo "PASS: static portfolio checks are clean."
