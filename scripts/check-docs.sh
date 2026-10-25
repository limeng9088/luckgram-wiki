#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

required=(
  README.md
  SUMMARY.md
  en/README.md
  en/SUMMARY.md
  docs/DOCMAP.md
  docs/ux/foundation.md
  docs/ux/scenarios.md
  docs/brand/voice.md
  docs/brand/terminology.md
  docs/brand/facts.md
  features/README.md
)

for file in "${required[@]}"; do
  test -f "$file" || { echo "missing required file: $file" >&2; exit 1; }
done

if rg -n 'luckgram[.]app' --glob '*.md' .; then
  echo "retired public domain found" >&2
  exit 1
fi

test "$(tr -d '\r\n' < CNAME)" = "wiki.luckgram.cc" || {
  echo "unexpected CNAME" >&2
  exit 1
}

test ! -e .well-known/assetlinks.json || {
  echo "Android association belongs on luckgram.cc, not the Wiki host" >&2
  exit 1
}

test ! -e .well-known/apple-app-site-association || {
  echo "Apple association belongs on luckgram.cc, not the Wiki host" >&2
  exit 1
}

# Chinese pages live at the root, English pages under en/; both trees must match.
for root in . en; do
  while IFS= read -r link; do
    target="${link%%#*}"
    case "$target" in
      ''|http://*|https://*|mailto:*|tel:* ) continue ;;
    esac
    test -e "$root/$target" || { echo "broken navigation target: $root/$target" >&2; exit 1; }
  done < <(sed -n 's/.*](\([^)]*\)).*/\1/p' "$root/SUMMARY.md")

  missing_navigation="$(comm -3 \
    <(cd "$root" && find getting-started features help reference -name '*.md' -type f | sort) \
    <(sed -n 's/.*](\([^)]*\.md\)).*/\1/p' "$root/SUMMARY.md" | grep -v '^README.md$' | sort))"

  if [[ -n "$missing_navigation" ]]; then
    echo "public pages and navigation differ in $root:" >&2
    echo "$missing_navigation" >&2
    exit 1
  fi
done

if ! diff <(find getting-started features help reference README.md -name '*.md' | sort) \
          <(cd en && find getting-started features help reference README.md -name '*.md' | sort) >/dev/null; then
  echo "Chinese and English page sets differ" >&2
  exit 1
fi

echo "docs check passed"
