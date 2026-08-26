#!/bin/sh
# Fail if real client names or live inboxes appear in this kit (except this scanner).
set -eu
ROOT=$(CDPATH= cd -- "$(dirname "$0")" && pwd)
FAIL=0

scan() {
  pattern=$1
  label=$2
  hits=$(grep -R -n -E -i --exclude="scan-pii.sh" -- "$pattern" "$ROOT" || true)
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
scan '0x9eb954b567ef3616424a6e1bf42c63724930aa54' "Base pay-to (wrong chain)"
scan '0999\.999\.992' "placeholder seller VAT/KBO"
scan '0888\.888\.888' "placeholder client VAT/KBO"
scan 'BE[[:space:]]*0[0-9]{3}[.\s]?[0-9]{3}[.\s]?[0-9]{3}' "any BE VAT/KBO number in kit files"

# Printed stamp must be VOORBEELD (all-caps). Case-sensitive, HTML only —
# Peppol notes may say lowercase "factuur"; README may name the banned stamp.
if grep -nE 'FACTUUR' "$ROOT/index.html" >/dev/null 2>&1; then
  echo "PII FAIL (printed FACTUUR stamp in index.html; use VOORBEELD):"
  grep -nE 'FACTUUR' "$ROOT/index.html" || true
  FAIL=1
fi

if [ "$FAIL" -ne 0 ]; then
  echo "PII scan failed."
  exit 1
fi

echo "PII scan clean: no De Meutter/Meeussen, no live inboxes, no placeholder KBO, no FACTUUR stamp."
echo "Demo allowlist: Studio Noord, Client BV, RFC 2606 (.example), KBO/BTW: nog niet toegekend."
