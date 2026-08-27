# File-1 ledger — VOORBEELD

Example ledger format for the WALLET seat. Not a FACTUUR. Not an INVOICE. Not a tax filing. Not a seed backup. Not a bank statement.

**Stamp:** `VOORBEELD`  
**Seat:** [`WALLET.md`](WALLET.md)  
**KBO/BTW:** nog niet toegekend — do not invent enterprise digits.

Fill real inbound rows only after pay-proof confirm. Until then the live content is the header plus the zero snapshot.

## Forbidden columns and values

Do not add these. Do not paste them into `notes`.

| Forbidden | Rule |
|---|---|
| Full IBAN | Revolut **denied**. No IBAN field. |
| IBAN last-4 | No last-4 until KYC. |
| Seed / mnemonic / private key / derivation path | Never. This file is a receive log, not a backup. |
| Full tx id / signature | Store **last-6** only. |
| Names, personal email, phone | No PII. |
| Helio payment id | Helio is not a land path. |
| Kraken order / trade id | No sales USDC to Kraken. |
| MCP session address | Not a treasury. Do not invent a third receive string. |

There is no bank rail on File-1.

## Header (do not rename)

```
when,rail,asset,amount,tx_last6,proof,notes
```

| Column | What to enter |
|---|---|
| `when` | `YYYY-MM-DD HH:MM` of the snapshot or of the confirmed landing. |
| `rail` | `solana` or `base` only. |
| `asset` | `SOL` or `USDC`. Catalog inbound is `USDC`. `SOL` rows are watch snapshots, not SKUs. |
| `amount` | Number. `0` is a snapshot / quiet-if-zero, not an inbound. |
| `tx_last6` | Last six characters of the confirmed tx. Use `—` on snapshot / quiet rows. Never a full hash. |
| `proof` | `snapshot` · `quiet-if-zero` · `confirmed` · `ambiguous` · `rpc-fail` |
| `notes` | Operator label (sku, memo). No names, no email, no IBAN, no seed. |

Do not add `iban`, `last4`, `seed`, `eur`, or `kraken` columns.

## Snapshot rows — 2026-08-27 20:56

Operator snapshot: **0 SOL / 0 USDC**. RPC re-check (read-only) matched: Solana 0 lamports, no USDC ATA, no signatures; Base ETH `0x0`, USDC `0x0`.

```
when,rail,asset,amount,tx_last6,proof,notes
2026-08-27 20:56,solana,SOL,0,—,snapshot,listed Phantom receive — no spend
2026-08-27 20:56,solana,USDC,0,—,snapshot,mint EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v — no ATA yet
2026-08-27 20:56,base,USDC,0,—,snapshot,native USDC — no inbound
```

These three rows are the current File-1. They are not payments.

## Quiet-if-zero (weekday 16:00)

If Monday–Friday 16:00 Europe/Brussels RPC still shows 0 SOL / 0 USDC and no new signatures, either write nothing or append:

```
2026-08-28 16:00,solana,USDC,0,—,quiet-if-zero,weekday 16:00 — stay quiet
2026-08-28 16:00,base,USDC,0,—,quiet-if-zero,weekday 16:00 — stay quiet
```

The dates above are format only (`2026-08-28` is the next weekday after the snapshot). Do not pre-fill them until that 16:00 check has actually run.

RPC fail is **not** quiet-if-zero:

```
2026-08-28 16:00,base,USDC,,—,rpc-fail,node 403 — retry publicnode — do not invent 0
```

Leave `amount` empty on `rpc-fail`. Empty is not zero.

## 08:00 still required

Daily 08:00 Europe/Brussels uses the same header. A zero 08:00 is written as `proof=snapshot` (or omitted if the operator keeps zeros only on the dated snapshot). Skipping 08:00 because 16:00 exists is a miss.

## Inbound row — VOORBEELD format only

Not a real payment. Do not copy into a live log as `confirmed`. Replace every `<…>` after RPC pay-proof. Last-6 is six placeholder X’s here so this cannot be mistaken for a hash fragment.

```
when,rail,asset,amount,tx_last6,proof,notes
<YYYY-MM-DD HH:MM>,solana,USDC,<amount>,XXXXXX,confirmed,<sku-or-memo — no PII>
<YYYY-MM-DD HH:MM>,base,USDC,<amount>,XXXXXX,confirmed,<sku-or-memo — no PII>
```

Rules for a live inbound row:

1. `proof=confirmed` only after WALLET pay-proof (RPC token-delta / receipt to a **listed** address).
2. `rail` matches the address that actually received USDC.
3. `amount` is the USDC that landed, not SOL, not ETH.
4. `tx_last6` is last-6 of that tx, never the full id, never `XXXXXX` on a live row.
5. Ambiguous RPC → `proof=ambiguous`, no spend, no retry send.

## Watched addresses (copy, do not invent)

Not columns. Repeat here so File-1 never grows a third pay-to.

- Solana Phantom USDC: `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3`
- Base Phantom receive: `0x9eb954b567ef3616424a6e1bf42c63724930aa54`

## Worked empty CSV

Copy-paste start. Header + snapshot only.

```csv
when,rail,asset,amount,tx_last6,proof,notes
2026-08-27 20:56,solana,SOL,0,—,snapshot,listed Phantom receive — no spend
2026-08-27 20:56,solana,USDC,0,—,snapshot,mint EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v — no ATA yet
2026-08-27 20:56,base,USDC,0,—,snapshot,native USDC — no inbound
```
