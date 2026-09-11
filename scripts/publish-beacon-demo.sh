#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
app_root="${1:-}"
target="$repo_root/site/the-beacon-wakes/play"

if [[ -z "$app_root" || ! -f "$app_root/package.json" || ! -f "$app_root/src/main.ts" ]]; then
  echo "usage: $0 /absolute/path/to/omarchy-typing-adventure" >&2
  exit 2
fi

npm --prefix "$app_root" run build:demo

rm -rf "$target"
mkdir -p "$target"
cp -rf "$app_root/dist-web/." "$target/"

if find "$target" -type f -name '*.map' | grep -q .; then
  echo "public demo must not contain source maps" >&2
  exit 1
fi

echo "Published browser demo to $target"
