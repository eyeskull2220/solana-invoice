# EUR receive log

Operator pack that matches Wallet’s empty `receive-log.csv` template.

Open [`eur-receive-log.html`](eur-receive-log.html) in a browser (works offline). Keep [`receive-log.csv`](receive-log.csv) as the column template, or export a filled copy from the page.

This pack does **not** invent exchange rates and does **not** file taxes.

## Columns

Exact header (do not rename):

```
date,usdc,eur_mid,memo,tx,notes
```

| Column | What to enter |
|---|---|
| `date` | Calendar day the USDC arrived (ISO `YYYY-MM-DD`). Same-day. |
| `usdc` | Inbound USDC amount. |
| `eur_mid` | EUR per 1 USDC mid **you** used that day. No default. |
| `memo` | Internal label (invoice id, batch tag). No names or emails. |
| `tx` | Last six characters of the transaction id only. |
| `notes` | Optional operator note. No names, emails, or full hashes. |

The HTML can show `usdc × eur_mid` as a books check. That product is not a rate feed and is not a tax figure. **If you do not have a mid, leave the row unlogged.**

## Pay note

- **Internal use:** free.
- **If billed:** 49 USDC on Solana, due on receipt.

Pay-to (USDC on Solana only): `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3`

Mint: `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v`

Memo if paying: `eur-receive-log`

No wallet connect. No account. Do not send XRP or SOL.

## PII

Do not put personal Gmail or any personal email in this pack, the CSV, `memo`, or `notes`. Store last-6 in `tx` — never a full transaction id. The page truncates pasted signatures before save and export.
