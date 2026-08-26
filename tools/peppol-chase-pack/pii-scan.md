# PII scan report

Pack: `tools/peppol-chase-pack/`
Date: **2026-08-26**
Scanner: `./scan-pii.sh` (exit 0)

## Scope

All files in this folder except this report and the scanner script.

## Checks

| Check | Result |
|---|---|
| Email addresses | None |
| Belgian VAT-like `BE` + digits | None |
| Dotted KBO (`xxxx.xxx.xxx`) | None |
| Bare 10-digit KBO values | None |
| Belgian IBAN values | None |
| Phone numbers | None |
| OpenPeppol registry contact-person names | None |
| Pay-to treasury address present | `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3` |

## Allowed (not PII)

- Public company trade names and legal names from the OpenPeppol certified / members lists
- Public websites from the OpenPeppol members list
- Official documentation URLs (OpenPeppol, BOSA, FPS Finance, Peppol Directory, KBO public search, Peppol BIS docs)
- Country code `BE` in UBL `IdentificationCode`
- Scheme `0208` (Belgian enterprise number ICD)
- `REPLACE_WITH_*` tokens (not real identifiers)
- Sample party labels `SAMPLE SELLER (NOT A REAL ENTERPRISE)` / `SAMPLE BUYER (NOT A REAL ENTERPRISE)`
- Treasury Solana address and USDC mint (public pay-to, not personal data)

## HARD rules verified in this folder

- Publisher is described as **not** an Access Point
- Pack does **not** claim Peppol / EN 16931 compliance for the sample or the buyer
- No invented VAT or KBO numbers (placeholders only)
- AP shortlist is public Belgian APs from OpenPeppol (BOSA / Belgium / AP certified), snapshot 2026-08-26

Re-run: `./scan-pii.sh`
