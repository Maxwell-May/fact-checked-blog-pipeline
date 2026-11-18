#!/bin/bash
# Regression suite for the gates. Every case is a real or adversarial input that once passed or failed wrongly.
# Usage: test_fixtures.sh   (exit 0 = all expectations met)
set -u
D="$(cd "$(dirname "$0")" && pwd)"; T="$(mktemp -d)"; pass=0; fail=0
expect(){ local want="$1"; shift; if "$@" >/dev/null 2>&1; then got=0; else got=$?; fi
  if { [ "$want" = open ] && [ "$got" = 0 ]; } || { [ "$want" = block ] && [ "$got" != 0 ]; }; then pass=$((pass+1)); else fail=$((fail+1)); echo "FAIL: expected $want, got exit $got: $*"; fi; }
H='| # | Claim | J | Source URL | Quote | Status | Verified on | Check result | Checker note |'
S='|---|---|---|---|---|---|---|---|---|'
mk(){ printf '%s\n%s\n%s\n' "$H" "$S" "$2" > "$T/$1.md"; }
mk good      '| 1 | x | OR | https://a.gov/p | q | VERIFIED | 2026-09-04 | CONFIRMED | ok |'
mk short_row '| 1 | x | OR | https://a.gov/p | q | VERIFIED | 2026-09-04 |'
printf '%s\n%s\n  %s\n' "$H" "$S" '| 1 | x | OR | https://a.gov/p | q | VERIFIED | 2026-09-04 | UNVERIFIED | no |' > "$T/indented_bad.md"
printf '%s\n%s\n' "$H" "$S" > "$T/empty.md"
mk two_pipes '| 1 | x `a|b` c | d | OR | https://a.gov/p | q | VERIFIED | 2026-09-04 | UNVERIFIED | n |'
mk tick_pipe '| 1 | x `a|b` | OR | https://a.gov/p | q | VERIFIED | 2026-09-04 | CONFIRMED | ok |'
mk note_word '| 1 | x | OR | https://a.gov/p | q | VERIFIED | 2026-09-04 | UNVERIFIED | was CONFIRMED before |'
mk std_only  '| 1 | x | OR | research-standards.md | q | VERIFIED | 2026-09-04 | CONFIRMED | memory |'
mk url_note  '| 1 | x | OR | none | q | VERIFIED | 2026-09-04 | CONFIRMED | see https://a.gov |'
mk secondary '| 1 | x | US | https://forums.mikeholt.com/t | q | SECONDARY | 2026-09-04 | CONFIRMED-SECONDARY | NEC text |'
mk estimate  '| 1 | x costs $700 | OR | contractor pricing | n/a | ESTIMATE | 2026-09-04 | ESTIMATE | label |'
mk dropped   '| 1 | x | OR | | | UNVERIFIED | 2026-09-04 | DROPPED | gone |
| 2 | y | OR | https://a.gov/p | q | VERIFIED | 2026-09-04 | CONFIRMED | ok |'
mk empty_res '| 1 | x | OR | https://a.gov/p | q | VERIFIED | 2026-09-04 |  | forgot |'
printf '%s\n%s\n%s\n%s\n%s\n' "$H" "$S" '| 1 | x | OR | https://a.gov/p | q | VERIFIED | 2026-09-04 | CONFIRMED | ok |' "$H" "$S" > "$T/two_headers.md"
G="$D/check_ledger.py"
expect open  python3 "$G" "$T/good.md";        expect block python3 "$G" "$T/short_row.md"
expect block python3 "$G" "$T/indented_bad.md"; expect block python3 "$G" "$T/empty.md"
expect block python3 "$G" "$T/two_pipes.md";    expect open  python3 "$G" "$T/tick_pipe.md"
expect block python3 "$G" "$T/note_word.md";    expect block python3 "$G" "$T/std_only.md"
expect block python3 "$G" "$T/url_note.md";     expect open  python3 "$G" "$T/secondary.md"
expect open  python3 "$G" "$T/estimate.md";     expect open  python3 "$G" "$T/dropped.md"
expect block python3 "$G" "$T/empty_res.md";    expect block python3 "$G" "$T/two_headers.md"
# lint fixtures: start from the reference post (must be CLEAN), then break it one way at a time
P="$D/../fixtures/reference-post.html"
Q="$D/../fixtures/reference-schema.txt"
L="$D/lint_post.py"
if [ -f "$P" ]; then
  expect open python3 "$L" "$P" "$Q"
  sed 's|<p class="ea-updated">Last updated September 4, 2026</p>|&\n<p>Is your hot tub wired?</p>|' "$P" > "$T/q.html"; expect block python3 "$L" "$T/q.html"
  sed 's|locally owned|Master <strong>Electrician</strong> owned|' "$P" > "$T/m.html"; expect block python3 "$L" "$T/m.html"
  sed 's|<div class="ea-final-cta">|<figure><img src="IMAGE_URL" alt="a b c d e f g h"></figure>&|' "$P" > "$T/i.html"; expect block python3 "$L" "$T/i.html"
  sed 's|<div class="ea-final-cta">|<figure><img src="https://example.com/x.jpg" alt="a b c d e f g h"></figure>&|' "$P" > "$T/h.html"; expect block python3 "$L" "$T/h.html"
  sed 's|"description": "|"description": "Free estimates. |' "$Q" > "$T/s1.txt"; expect block python3 "$L" "$P" "$T/s1.txt"
  sed 's|"headline": "[^"]*"|"headline": "[WP title]"|' "$Q" > "$T/s2.txt"; expect block python3 "$L" "$P" "$T/s2.txt"
  sed 's|standard 240V|free-standing 240V|' "$P" > "$T/fs.html"; expect open python3 "$L" "$T/fs.html" "$Q"
else
  echo "lint fixtures skipped: the reference post is a real client page and is not included in this public copy"
fi
echo "fixtures: $pass passed, $fail failed"; rm -rf "$T"; [ "$fail" = 0 ]
