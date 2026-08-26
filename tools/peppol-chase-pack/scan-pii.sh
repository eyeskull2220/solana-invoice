#!/usr/bin/env bash
# PII + invented-identifier scan for tools/peppol-chase-pack/
# Pack date: 2026-08-26
# Exit 0 = clean. Exit 1 = hits that must be removed.

set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"

fail=0
hits() { fail=1; echo "FAIL: $*"; }

echo "PII scan — $ROOT"
echo "Pack date 2026-08-26"
echo

# 1. Email addresses (personal or role inboxes). Official https URLs are not emails.
if grep -RInE --exclude='scan-pii.sh' --exclude='pii-scan.md' \
  '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' .; then
  hits "email address found"
else
  echo "OK: no email addresses"
fi

# 2. Invented or real Belgian VAT (BE + 8–12 digits, optional dots/spaces).
# Country code element <cbc:IdentificationCode>BE</cbc:IdentificationCode> is allowed.
# Token REPLACE_WITH_SELLER_VAT is allowed (no digits after BE).
if grep -RInE --exclude='scan-pii.sh' --exclude='pii-scan.md' \
  'BE[[:space:].]*[0-9]{8,}' .; then
  hits "BE + digits (VAT-like) found"
else
  echo "OK: no BE+digits VAT"
fi

# 3. Dotted KBO (xxxx.xxx.xxx)
if grep -RInE --exclude='scan-pii.sh' --exclude='pii-scan.md' \
  '[0-9]{4}\.[0-9]{3}\.[0-9]{3}' .; then
  hits "dotted KBO-like number found"
else
  echo "OK: no dotted KBO"
fi

# 4. Bare 10-digit blocks that look like a filled KBO (not in comments about '10 digits').
# Flag 10 consecutive digits anywhere except scan docs.
if grep -RInE --exclude='scan-pii.sh' --exclude='pii-scan.md' \
  --exclude='README.md' \
  '[^0-9][0-9]{10}[^0-9]' .; then
  hits "10 consecutive digits (possible KBO) found"
else
  echo "OK: no 10-digit KBO values"
fi

# 5. IBAN starting with BE and digits
if grep -RInE --exclude='scan-pii.sh' --exclude='pii-scan.md' \
  'BE[0-9][0-9][0-9 ]{10,}' .; then
  hits "Belgian IBAN-like value found"
else
  echo "OK: no Belgian IBAN values"
fi

# 6. Phone numbers
if grep -RInE --exclude='scan-pii.sh' --exclude='pii-scan.md' \
  --exclude='README.md' \
  '\+32|tel:|[0-9]{2,3}[[:space:]][0-9]{2,3}[[:space:]][0-9]{2,3}[[:space:]][0-9]{2,3}' .; then
  hits "phone-like value found"
else
  echo "OK: no phone numbers"
fi

# 7. Personal given names copied from the OpenPeppol contact column (do not ship).
if grep -RInE --exclude='scan-pii.sh' --exclude='pii-scan.md' -i \
  'Jente Bosmans|Cosmin Baciu|Bertrand Verlaine|Michel Gilis|Dany De Bontridder|Robrecht Mosselmans|Joris Ballet|Mark Van Hamme|Daan Lenaerts|Geoffrey Crombez|Koen Decorte|Géry Lambrechts|Eddy Mommen|Cindy Salden|Jurgen Heinis|David Michaluk|Rob Vermeulen|Cedric Neve|Katrien De Wolf|Atilla Ozpala|Andrej Belcijan|Christoph Hillegeer|Willem De Groef|Floryan Simar|Jean-Luc Walem|Cosmin Antofie|Marc Joostens|Gediz Aksit|David Vandekerckhove|Gil Ghislain|Bryan Steyns|Kevin Van Gyseghem|Olivier Mascia|Bert Leeman|Guy De Smet|Luc De Deyn|Thomas Van Hoezen|Linsay Leroy|Stijn Claes|Robert Kowinski|Philippe Dingemans|Leentje De Brouwer|Wim Maerevoet|Benjamin Stiénon|Ogun Ates|Mathieu Pasture|Sebastien Libert|Michaël Van Robaeys|Mike Vandamme|Jeffrey Baeke|Lionel Hermans|Khalid Makhloufi|Ben Pintens|Pierre van Weereld|Frédéric Hayertz|Pieter Meyvaert|Tom Myny|Julien Gobiet|Jonas Six|Frie Vanparijs|Charles Convent|Laurent Oosters|Patrick Mast' .; then
  hits "OpenPeppol contact-person name found"
else
  echo "OK: no OpenPeppol contact-person names"
fi

# 8. Pay-to must be the treasury address, unchanged.
if ! grep -R --quiet '96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3' index.html README.md; then
  hits "treasury pay-to address missing from index.html / README.md"
else
  echo "OK: pay-to treasury address present"
fi

echo
if [ "$fail" -ne 0 ]; then
  echo "PII scan FAILED"
  exit 1
fi
echo "PII scan PASSED"
exit 0
