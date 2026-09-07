#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."

node --check site/assets/app.js
node --test tests/site-data.test.mjs

if rg -n '[–—]' site README.md plugins.json; then
  echo "FAIL: public portfolio copy contains an em dash or en dash." >&2
  exit 1
fi

echo "PASS: static portfolio checks are clean."
