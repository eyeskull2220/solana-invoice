#!/bin/sh
# Fail if live inboxes, fake KBO, FACTUUR stamp, USDC-on-the-face, or leftover toys appear.
set -eu
ROOT=$(CDPATH= cd -- "$(dirname "$0")" && pwd)
FAIL=0

scan() {
  pattern=$1
  label=$2
  hits=$(grep -R -n -E -i --exclude="scan-pii.sh" --exclude="README.md" -- "$pattern" "$ROOT" || true)
  if [ -n "$hits" ]; then
    echo "PII FAIL ($label):"
    echo "$hits"
    FAIL=1
  fi
}

scan 'De[[:space:]]*Meutter' "real surname De Meutter"
scan 'Meeussen' "real surname Meeussen"
scan 'gmail\.com' "Gmail inbox"
scan 'googlemail\.com' "Googlemail inbox"
scan 'outlook\.com' "Outlook inbox"
scan 'hotmail\.com' "Hotmail inbox"
scan 'telenet\.be' "Telenet inbox"
scan 'skynet\.be' "Skynet inbox"
scan 'hello@studio\.example' "freelancer studio placeholder"
scan 'Voorbeeldharmonie' "generic Voorbeeldharmonie"
scan 'lidmaatschap 2023' "stale lidmaatschap 2023"
scan 'GDPR-compliant' "GDPR-compliant badge"
scan 'USDC' "USDC on the face"
scan 'Solana' "Solana on the face"
scan '96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3' "treasury address on the face"
scan '0999\.999\.992' "placeholder seller VAT/KBO"
scan '0888\.888\.888' "placeholder client VAT/KBO"
scan 'BE[[:space:]]*0[0-9]{3}[.\s]?[0-9]{3}[.\s]?[0-9]{3}' "any BE VAT/KBO number"

if grep -nE 'FACTUUR' "$ROOT/index.html" >/dev/null 2>&1; then
  echo "PII FAIL (printed FACTUUR stamp in index.html; use VOORBEELD):"
  grep -nE 'FACTUUR' "$ROOT/index.html" || true
  FAIL=1
fi

if [ "$FAIL" -ne 0 ]; then
  echo "PII scan failed."
  exit 1
fi

echo "PII scan clean: named-club VOORBEELD, no fake KBO, no FACTUUR, no USDC on the face."
