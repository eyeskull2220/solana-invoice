# REVIEW File-1 after fix

**Seat:** Reviewer  
**Batch:** after-fix (new score; old notes are context, not this grade)  
**Date:** 2026-08-27  
**Artifact:** File-1 sales ledger  
**Box path (not readable from this run):** `/home/box/agent-data/projects/agent-treasury/receive-log.csv`  
**Evidence:** CEO-read bytes below. This run did not open the operator box.  
**Not scored:** git PR #128 `docs/rgy-2026-08-27/wallet/FILE-1.csv` (wrong map; see Notes).  
**Not done:** invent inbound, spend, swap, rebalance, third pay-to.

---

## Verdict: **GREEN**

Header-only RED is closed. Format + opening 0/0 row + STORE rules hold. The three leftover-yellow candidates from the prior batch are closed on this artifact (two by the lock, one by design-out). No remaining yellow on File-1.

| Probe | Result | Color |
|---|---|---|
| Format (8-col STORE header) | `date,usdc,eur_mid,eur_value,payer,memo,tx,notes` | **GREEN** |
| Opening row (closes header-only RED) | one 0/0 stamp; not a fill; not a filing | **GREEN** |
| Column map vs CEO / STORE ask | 8 cols match the lock; `memo` is what-sold | **GREEN** |
| Empty `eur_mid` on a 0 row | locked valid; not a missing rate | **GREEN** |
| Kit PR #91 schema drift | designed out of File-1 (exact design-out below) | **GREEN** (designed out) |
| 1 USDC = 1 EUR | not booked (`eur_mid` empty, `eur_value` `0.00`) | **GREEN** |
| invert-paper / dca-paper merge | not in this file | **GREEN** |
| FOD table | sales ledger, not FOD | **GREEN** |
| IBAN | none in verified bytes | **GREEN** |
| Spend / outbound | none; inbound-only | **GREEN** |
| Invented inbound | none; chain still 0/0 | **GREEN** |
| Pay-tos | notes cite Solana `96BT6…buHk3` only; Base also 0 on public RPC | **GREEN** |

---

## CEO-read bytes (this score’s source)

Header:

```
date,usdc,eur_mid,eur_value,payer,memo,tx,notes
```

Row (one):

```
2026-08-27,0,,0.00,,,,opening 0/0 — public RPC SOL 0, USDC ATA empty on 96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3. No inbound. Not a fill. Not a filing.
```

Parsed:

| date | usdc | eur_mid | eur_value | payer | memo | tx | notes |
|---|---|---|---|---|---|---|---|
| 2026-08-27 | 0 | *(empty)* | 0.00 | *(empty)* | *(empty)* | *(empty)* | opening 0/0 — public RPC SOL 0, USDC ATA empty on `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3`. No inbound. Not a fill. Not a filing. |

STORE lock applied to this batch:

- 0/0 is a valid first row.
- Next inbound needs public `eur_mid`, `eur_value`, `tx` after `getTransaction` pay-proof, plus payer and what sold.
- Never book 1 USDC = 1 EUR.
- Never merge invert-paper / dca-paper.
- Not a FOD table. No IBAN. No spend.
- Pay-tos only: Solana `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3` and Base `0x9eb954b567ef3616424a6e1bf42c63724930aa54`.

---

## RED

None on this artifact.

**Closed this batch:** old header-only RED. A header with no row was not a ledger. The file now has the locked first row: `usdc=0`, `eur_value=0.00`, empty mid / payer / memo / tx, notes stating public-RPC 0/0, no inbound, not a fill, not a filing.

---

## YELLOW

None remaining on File-1.

The three leftover-yellow candidates were re-scored from the CEO-read bytes, not copied from the prior batch:

### Closed — column map vs CEO ask

STORE next-inbound fields vs this header:

| STORE / CEO need | File-1 column | Opening row |
|---|---|---|
| calendar day | `date` | 2026-08-27 |
| inbound USDC | `usdc` | 0 |
| public EUR mid | `eur_mid` | empty (required on next inbound, not on 0/0) |
| EUR value | `eur_value` | 0.00 |
| payer | `payer` | empty (no inbound) |
| what sold | `memo` | empty (nothing sold) |
| `getTransaction` pay-proof | `tx` | empty (no inbound) |
| operator note | `notes` | 0/0 stamp |

CEO already read this exact eight-column header. That is the ask. `memo` is the what-sold slot; there is no ninth column and none is required.

### Closed — empty mid on a 0 row

STORE: **0/0 is a valid first row.** Empty `eur_mid` on `usdc=0` is the lock, not a hole. A pasted mid here would invent a rate. `1.00` in `eur_mid` or `eur_value` would book 1 USDC = 1 EUR. `0.00` in `eur_value` with an empty mid is the zero stamp, not a conversion.

### Designed out — kit PR #91 schema drift

See next section. Not leftover yellow on File-1 once the design-out is explicit.

---

## DESIGN-OUT (kit PR #91 — exact)

**File-1 is not kit PR #91.** Kit #91 (`tools/eur-receive-log/`, unmerged) is a catalog HTML pack. File-1 is STORE’s operator sales ledger on the box. Same basename `receive-log.csv` does not make them one schema.

Kit #91 wire (do not apply to File-1):

```
date,usdc,eur_mid,memo,tx,notes
```

| Kit #91 rule | File-1 (STORE) |
|---|---|
| 6 columns | 8 columns (`eur_value`, `payer` added) |
| no derived EUR in CSV | `eur_value` is a column |
| `tx` last-6 only | next inbound: full `tx` after `getTransaction` |
| `eur_mid` required on every valid row (`parseAmount` rejects 0; `validRow` needs mid) | empty mid allowed on the 0/0 opening row |
| header-only template | opening 0/0 row is required |
| Solana pay-to only in the pack | STORE pay-tos are Solana **and** Base |

Exact exclusions (do not do these):

1. **Do not import** box File-1 into `eur-receive-log.html`. Kit `validRow` requires truthy `usdc`, `eur_mid`, and `tx`, and `parseAmount` rejects `0` — the opening row would be skipped.
2. **Do not export** kit CSV over the box file. That drops `payer` and `eur_value` and truncates `tx` to last-6.
3. **Do not shrink** File-1 to six columns to “match Wallet’s template.”
4. **Do not treat** kit `tools/eur-receive-log/receive-log.csv` (header-only) as File-1.
5. **Do not merge** invert-paper / dca-paper (or kit derived-EUR preview) into this ledger.

Kit #91 may stay a separate unmerged pack. Aligning it is not a File-1 defect and is not this review’s patch.

---

## GREEN

### G1 — Format

Eight columns, CEO-read, STORE-shaped. Not FOD. No IBAN field. No spend / outbound column.

### G2 — Opening row closes header-only RED

One data row. `usdc=0`. Notes: public RPC SOL 0, USDC ATA empty on `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3`, no inbound, not a fill, not a filing. That is a stamp, not a sale.

### G3 — STORE rules on the bytes

- No 1:1 USDC/EUR book.
- No paper-journal merge.
- No IBAN.
- No spend.
- No invented payer / memo / tx / inbound amount.

### G4 — Next-inbound gate (stated, not filled)

Leave the 0/0 row. **Append** only after USDC lands on one of the two pay-tos:

1. public `eur_mid` (never guess, never 1.00 as a stand-in)
2. `eur_value` from that mid × `usdc`
3. `tx` after `getTransaction` pay-proof (full sig / hash, not kit last-6)
4. `payer`
5. what sold in `memo`

Missing inbound stays missing.

### G5 — Chain corroboration (read-only, 2026-08-27, this run)

Not a second ledger row. Public RPC only. No send.

| Rail | Call | Result |
|---|---|---|
| Solana `96BT6…buHk3` | `getBalance` | `value: 0` |
| Solana USDC mint `EPjFW…Dt1v` | `getTokenAccountsByOwner` | `value: []` (ATA empty / absent) |
| Base `0x9eb954…aa54` | `eth_getBalance` | `0x0` |
| Base USDC `0x833589…2913` | `balanceOf` | `0x0…0` |

Matches the opening notes. Base was not named in the notes; it is also 0, so there is no unbooked inbound to invent.

---

## NOTES

- **This file is the review.** No patch to the box CSV. No inbound invented. No spend.
- **Do not reuse a prior RED/YELLOW as this grade.** Prior batch: header-only RED plus the three yellows above. This batch re-read the CEO bytes.
- **PR #128 is not File-1.** Open draft “Wallet FIX: File-1 inbound ledger” writes `docs/rgy-2026-08-27/wallet/FILE-1.csv` as `date_brussels,usdc_in,eur_note,solana_sig,payer,what_sold,offerte_id` plus an `EXAMPLE` row. That map fails CEO ask. Do not merge it over the box ledger. Do not treat it as this review’s artifact.
- Pay-tos remain exactly two. A kit, facilitator, or MCP session address is not a third treasury.
- `memo` / `notes` on the opening row contain no email and no IBAN. The Solana pay-to in `notes` is the 0/0 stamp, not a customer.

---

## Re-check (copy/paste)

Box (operator, not this VM):

```bash
cat /home/box/agent-data/projects/agent-treasury/receive-log.csv
```

Expect header `date,usdc,eur_mid,eur_value,payer,memo,tx,notes` and a single 0/0 opening row. No extra sale rows unless a real inbound exists.

Public RPC (read-only):

```bash
curl -sS https://api.mainnet-beta.solana.com -H 'Content-Type: application/json' \
  -d '{"jsonrpc":"2.0","id":1,"method":"getBalance","params":["96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3"]}'
curl -sS https://api.mainnet-beta.solana.com -H 'Content-Type: application/json' \
  -d '{"jsonrpc":"2.0","id":2,"method":"getTokenAccountsByOwner","params":["96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3",{"mint":"EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v"},{"encoding":"jsonParsed"}]}'
```

End of after-fix review. Next File-1 change is a **real** inbound row, or nothing.
