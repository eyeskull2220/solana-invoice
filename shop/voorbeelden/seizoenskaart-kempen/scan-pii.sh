#!/bin/sh
# Fail the pack on leftover payment rails, invented KBO digits, FAVV stamps, or inbox PII.
set -eu
ROOT=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
cd "$ROOT"
fail=0

hit() {
  printf 'FAIL: %s\n' "$1"
  fail=1
}

# HTML/CSS/JS only — README may name the folder.
FILES=$(find . -type f \( -name '*.html' -o -name '*.css' -o -name '*.js' \) ! -name 'qrcode.min.js')

if grep -R -n -E 'USDC|usdc|Solana Pay|spl-token' -- $FILES; then
  hit 'payment rail other than EUR on the face (USDC/Solana)'
fi

if grep -R -n -E 'BE[[:space:]]?0[0-9]{3}[.]?[0-9]{3}[.]?[0-9]{3}|BE0[0-9]{9}' -- $FILES README.md; then
  hit 'invented or copied KBO/BTW digits'
fi

# Positive FAVV claims only. Denials ("geen FAVV-…") are required, not a fail.
if grep -R -n -E 'voldoet aan FAVV|FAVV-compliant|FAVV-conform|FAVV-gecertificeerd|FAVV-proof|FAVV-ok' -- $FILES README.md; then
  hit 'FAVV compliance claim'
fi
if grep -R -n -E 'FAVV[[:space:]-]*(compliant|conform|gecertificeerd)' -- $FILES README.md; then
  hit 'FAVV compliance claim'
fi

# Stamp must not be FACTUUR (denials in running text use lowercase "factuur").
if grep -R -n -E '<p class="stamp">[^<]*FACTUUR|>FACTUUR<' -- $FILES; then
  hit 'FACTUUR stamp'
fi

if ! grep -q '€199' index.html; then
  hit '€199 missing on offerte face'
fi

if ! grep -q -E 'class="stamp">Offerte' index.html; then
  hit 'OFFERTE stamp missing'
fi

if [ ! -f print.css ]; then
  hit 'print.css missing'
fi

if ! grep -q '@media print' print.css; then
  hit 'print.css has no @media print'
fi

if ! grep -q 'kaart.html' index.html; then
  hit 'offerte does not link the kaart'
fi

if grep -R -n -E 'gmail\.com|@depeesteker' -- $FILES README.md; then
  hit 'live or personal inbox'
fi

if grep -R -n -E 'IBAN[[:space:]]*BE[0-9]' -- $FILES README.md; then
  hit 'invented IBAN digits'
fi

if [ "$fail" -ne 0 ]; then
  exit 1
fi

printf 'PASS\n'
exit 0
