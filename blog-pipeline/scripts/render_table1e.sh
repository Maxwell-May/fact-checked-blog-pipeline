#!/bin/bash
# Render the Oregon OESC Table 1-E page that mentions a given NEC section as a PNG so the
# underline (Oregon added) and strikethrough (Oregon deleted) marks can be READ as an image.
# Text extraction strips both marks and has produced a published misattribution.
#
# Usage:  render_table1e.sh 680.42        -> prints PNG path(s); then Read the image
#         render_table1e.sh 210.12 --all  -> every page mentioning the section
# Deps: curl, poppler (pdfinfo, pdftotext, pdftoppm). Network: one HTTPS GET to oregon.gov, cached 7 days.
set -euo pipefail
SECTION="${1:?usage: render_table1e.sh <nec-section> [--all]}"
ALL="${2:-}"
case "$SECTION" in *[!0-9A-Za-z.\(\)]*|"") echo "bad section string: '$SECTION' (digits, letters, dots, parentheses only)"; exit 2;; esac
URL="https://www.oregon.gov/bcd/codes-stand/Documents/26oesc-table1-E.pdf"   # 2026 OESC, effective Oct 1, 2026
CACHE="${OESC_CACHE:-$HOME/.cache/oesc-table1e}"
mkdir -p "$CACHE"
EDITION="$(basename "$URL" .pdf)"
PDF="$CACHE/$EDITION.pdf"   # cache keyed by edition so an old table can never be reused
for t in curl pdfinfo pdftotext pdftoppm; do command -v "$t" >/dev/null || { echo "$t missing (brew install poppler)"; exit 2; }; done
if [ ! -s "$PDF" ] || [ -n "$(find "$PDF" -mtime +7 2>/dev/null)" ]; then
  curl -sSL --fail --proto '=https' --max-time 60 "$URL" -o "$PDF.tmp" && mv "$PDF.tmp" "$PDF" \
    || { rm -f "$PDF.tmp"; echo "download failed: $URL"; exit 4; }
fi
PAGES=$(pdfinfo "$PDF" | awk '/^Pages:/{print $2}')
HEAD=$(pdftotext -l 1 "$PDF" - | sed -n '1,4p' | tr '\n' ' ')
echo "TABLE: $HEAD"
FOUND=0
for p in $(seq 1 "$PAGES"); do
  if pdftotext -f "$p" -l "$p" -layout "$PDF" - | grep -q -F -- "$SECTION"; then
    OUT="$CACHE/$EDITION-$(printf '%s' "$SECTION" | tr -c 'A-Za-z0-9' '_')-p$p"
    pdftoppm -r 200 -f "$p" -l "$p" -png "$PDF" "$OUT" >/dev/null
    ls "$OUT"*.png
    FOUND=1
    [ "$ALL" = "--all" ] || break
  fi
done
if [ "$FOUND" != 1 ]; then
  echo "NO TEXT MATCH for '$SECTION' in Table 1-E. Likely unamended (NEC text applies), but layout or hyphenation can hide a match:"
  echo "confirm by searching the parent article number (e.g. 680) with --all before writing 'Oregon has not amended'."
  exit 3
fi
echo "Now Read the PNG. Underlined = Oregon added. Struck through = Oregon deleted. Quote only underlined words as Oregon's amendment."
