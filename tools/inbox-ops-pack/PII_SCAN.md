# PII scan — inbox-ops pack

**Date:** 2026-08-26  
**Folder:** `tools/inbox-ops-pack/`  
**Verdict:** **PASS**

Scanned every file in this pack for personal Gmail, live inboxes, phones, home addresses, keys, leftover restack of the 9 USDC Solana Invoice toy, and Base/ETH paste-addresses.

## Allowed placeholders (RFC 2606)

| Kind | Value | Why it is allowed |
| --- | --- | --- |
| Studio mail | `you@studio.example` | User-specified RFC 2606 placeholder. Not Gmail. |
| Client mail | `billing@client.example` | RFC 2606 placeholder. |
| Studio | Studio Noord · Voorbeeldlaan 1, 2000 Antwerpen | Fake demo practice / street. |
| Client | Client BV · Klantplein 8, 1000 Brussel | Fake demo company. |
| KBO/BTW | `KBO/BTW: nog niet toegekend` | No invented VAT digits. |
| Phone field | `+32 0 000 00 00` | Zeroed placeholder in the intake hint only. |
| Intake name hint | Alex Example | Form placeholder, not a real person. |
| Pay-to | `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3` | Public treasury Solana USDC address already on the catalog / pay page. |
| Solana Pay memo | `inbox-ops-299` | Identifies this pack on the 299 USDC payment. |

## Fail patterns (must be absent)

| Pattern | Result |
| --- | --- |
| `gmail.com` / personal Gmail | **absent** |
| Operator mail (`eyeskull…`) | **absent** |
| Live company inboxes | **absent** |
| Real mobile / landline numbers | **absent** (only the zeroed `+32 0 000 00 00` hint) |
| Home addresses of real people | **absent** |
| Private keys / seed phrases | **absent** |
| Base / ETH address `0x9eb954b567ef3616424a6e1bf42c63724930aa54` | **absent** |
| Invented VAT/KBO digits (`BE 0999…`, `BE0123…`) | **absent** (demo uses `KBO/BTW: nog niet toegekend`) |
| Leftover 9 USDC Solana Invoice restack (wallet-connect, `solana-invoice.html` embed, 9 USDC unlock) | **absent** |

## Notes

- Downloaded intake / factuur / reminder HTML must not contain the treasury address (checked in the download builders).
- Rebrand step 4 in `README.md` forbids pasting Gmail into a still-fake demo.
