# EUR receive log

Operator pack for recording each inbound USDC as EUR on the same day it arrived.

Open [`eur-receive-log.html`](eur-receive-log.html) in a browser (works offline). Keep [`receive-log.csv`](receive-log.csv) as the column template, or export a filled copy from the page.

## Columns

| Column | What to enter |
|---|---|
| `date` | Calendar day the USDC arrived (ISO `YYYY-MM-DD`). Same-day. |
| `chain` | Chain the inbound landed on (Solana, Ethereum, Base, …). |
| `tx_last6` | Last six characters of the transaction id only. |
| `usdc_amount` | Inbound USDC amount. |
| `eur_mid` | EUR per 1 USDC mid **you** used that day. |
| `source_memo` | Internal label only (invoice id, batch tag). No names, emails, or full hashes. |

The HTML can compute a display EUR amount as `usdc_amount × eur_mid`. That product is not a rate feed. **This pack does not fetch, guess, or bake an exchange rate.** If you do not have a mid, leave the row unlogged until you do.

## Pay note

- **Internal use:** free.
- **If billed:** 49 USDC on Solana, due on receipt.

Pay-to (USDC on Solana only): `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3`

Mint: `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v`

Memo if paying: `eur-receive-log`

No wallet connect. No account. Do not send XRP or SOL.

## PII

Do not put personal Gmail or any personal email in this pack, the CSV, or `source_memo`. Store last-6 only — never a full transaction id. The page truncates pasted signatures before save and export.
