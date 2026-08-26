#!/usr/bin/env bash
# Guard the public club-site kit: no live club inboxes, no personal webmail,
# no identity-tenant leftovers, no unexpected pay-tos.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
FAIL=0

hit() {
  local label="$1"
  local pattern="$2"
  if grep -RInE --exclude=scan-pii.sh --exclude=README.md "$pattern" "$ROOT" >/dev/null 2>&1; then
    echo "PII FAIL: $label"
    grep -RInE --exclude=scan-pii.sh --exclude=README.md "$pattern" "$ROOT" || true
    FAIL=1
  fi
}

# Personal / live mailboxes
hit "gmail address" '[[:alnum:]._%+-]+@gmail\.com'
hit "googlemail address" '[[:alnum:]._%+-]+@googlemail\.com'
hit "hotmail/live/outlook address" '[[:alnum:]._%+-]+@(hotmail|live|outlook)\.'
hit "non-example mailbox" '[[:alnum:]._%+-]+@[A-Za-z0-9.-]+\.(be|com|net|org)'

# Named live clubs that must never land in this public kit
hit "forbidden club token" '(KWZC|kwzc|[Dd]olfijnen)'

# Identity / leftover stacks
hit "Azure AD / Entra / SharePoint" '(Azure AD|azuread|login\.microsoftonline|entra\.microsoft|sharepoint\.com)'
hit "wallet connect" 'wallet.?connect'

# Pay-tos: only the known treasury address may appear
if grep -RInE --exclude=scan-pii.sh '0x[a-fA-F0-9]{40}' "$ROOT" >/dev/null 2>&1; then
  echo "PII FAIL: EVM pay address"
  grep -RInE --exclude=scan-pii.sh '0x[a-fA-F0-9]{40}' "$ROOT" || true
  FAIL=1
fi

# Belgian mobile / landline-looking numbers
hit "phone number" '(?:\+32|0032)[\s./-]*[0-9]{8,9}|0[1-9][0-9]{7,8}'

if [[ "$FAIL" -ne 0 ]]; then
  echo "scan-pii: FAILED"
  exit 1
fi

echo "scan-pii: OK (generic demo only)"
exit 0
