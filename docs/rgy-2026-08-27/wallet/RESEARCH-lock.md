# Wallet RESEARCH lock

**Seat:** Wallet (RESEARCH rewrite)  
**Date:** 2026-08-27  
**Closes:** reviewer PR [#176](https://github.com/eyeskull2220/solana-invoice/pull/176) RESEARCH stage **YELLOW**  
**This file is the RESEARCH.** It does not implement. It does not spend. It does not snap. It does not re-query RPC. It does not invent a third pay-to, an IBAN, a seed, or an inbound.

A later Wallet agent follows **this page** for File-1 current-state and columns. Not `#149` (advocate YELLOW). Not `#128` (EXAMPLE git stub). PLAN-stage SSOT / 08:00 snap already live on [PR #171](https://github.com/eyeskull2220/solana-invoice/pull/171) `PLAN-lock.md` — cite, do not reopen as a second book.

**GREEN here is pack cleanliness, not inbound. There is no inbound.**

---

## Why this page exists

PR [#176](https://github.com/eyeskull2220/solana-invoice/pull/176) scored Wallet RESEARCH **YELLOW (not GREEN)**. GREEN count **10 / 12**. Stage not closed. GREEN on that page — and on this one — means the **pack is clean**. It does not mean USDC landed.

Two hygiene rows stayed YELLOW in `#149` `01-adv-research.md`:

| Gate | Why it was YELLOW | This page |
| --- | --- | --- |
| File-1 current-state vs book | Pack live-desk: **“Header only. No inbound row.”** Book ([#141](https://github.com/eyeskull2220/solana-invoice/pull/141) GREEN): eight-column header **plus** opening `2026-08-27,0,,0.00,,,,opening 0/0` | SSOT is operator `receive-log.csv`. It is **not** header-only. Opening 0/0 stays. Empty inbound is valid. Not a parse fail. Not a sale. |
| File-1 later-FIX columns | Pack NOTES prescribe [#128](https://github.com/eyeskull2220/solana-invoice/pull/128) `date_brussels,usdc_in,eur_note,solana_sig,payer,what_sold,offerte_id` | Canonical columns are `date,usdc,eur_mid,eur_value,payer,memo,tx,notes`. `#128` is EXAMPLE docs, **never imported**. Do not prescribe `#128` columns. |

Until this lock, a later FIX that “writes File-1” from `#149` NOTES would still describe a header-only stub and split the books onto `#128` names.

Do **not** treat `#176` YELLOW as permission to send, to snap again, or to invent a sale so the CSV “looks used.”

---

## GREENS kept (do not bargain these away)

`#176` already closed these. This rewrite does **not** reopen them.

| Lock | Value |
| --- | --- |
| Two pay-tos only | Solana `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3` · Base `0x9eb954b567ef3616424a6e1bf42c63724930aa54` |
| No third address | Never. MCP session, Pay `reference`, gas key, CDP, Helio, EIP-55 recase, leftover shop HTML: not treasury |
| No spend | No send / swap / rebalance / perps / Helio / Kraken USDC out / ATA-create / rent-fund / test tx |
| No IBAN | No full IBAN. No Bancontact. No Peppol `PayeeFinancialAccount` stuffed with base58 / `0x`. No seed |
| 08:00-only snap | Stamp **2026-08-27 08:00** Europe/Brussels. No 16:00. No extra RPC. No Phantom MCP this run. Cite [#171](https://github.com/eyeskull2220/solana-invoice/pull/171) |
| File-1 **0/0 valid** | Empty inbound is not a parse fail, not a sale, not a reason to send |

Also kept from `#176` (pack already clean on these): mints ≠ pay-tos; no invented inbound; agent wallet ≠ treasury; leftover shop Solana-only is documented, **not** patched from Wallet; this sitting does not extra-snap.

---

## Designed out — File-1 current-state

### SSOT

**Canonical File-1** is the operator box:

```
/home/box/agent-data/projects/agent-treasury/receive-log.csv
```

It is **not** header-only. Header-only was the old RED [#141](https://github.com/eyeskull2220/solana-invoice/pull/141) closed. `#149` live-desk “Header only. No inbound row.” is a **stale shape**. Empty inbound is still true. The file already has a first data row.

**Opening row (leave intact):**

```
2026-08-27,0,,0.00,,,,opening 0/0
```

CEO-read bytes in `#141` may continue the `notes` field after `opening 0/0`. Leave that row. Do not truncate it. Do not invent a second opening row in git. Do not patch the box CSV from a RESEARCH page. This VM cannot open the box.

| Field on that row | Meaning |
| --- | --- |
| `date` | `2026-08-27` |
| `usdc` | `0` |
| `eur_mid` | **empty** — valid on a zero row |
| `eur_value` | `0.00` — zero-of-zero, **not** 1 USDC = 1 EUR |
| `payer` / `memo` / `tx` | empty |
| `notes` | `opening 0/0` (and any CEO-read suffix) |
| Inbound | **none** |

Empty inbound is **valid**. Not a parse fail. Not a sale. Not a fill. Not a filing. Not a license to send, to airdrop rent, to open an ATA, or to invent a payer / offerte / signature / positive `usdc`.

Do **not** describe File-1 as header-only. Do **not** describe a first-row 0/0 as “missing, so write a header-only git stub.” The book has the opening row. Keep it.

---

## Designed out — columns (do not prescribe `#128`)

**Exact columns (8):**

```
date,usdc,eur_mid,eur_value,payer,memo,tx,notes
```

That is the only File-1 header. PLAN-lock [#171](https://github.com/eyeskull2220/solana-invoice/pull/171) already named it as SSOT. RESEARCH names it again so a later FIX cannot follow `#149` NOTES instead.

PR [#128](https://github.com/eyeskull2220/solana-invoice/pull/128) `docs/rgy-2026-08-27/wallet/FILE-1.csv` uses:

```
date_brussels,usdc_in,eur_note,solana_sig,payer,what_sold,offerte_id
```

That file is **EXAMPLE documentation**. It is **not** SSOT. It is **never imported** into operator File-1. It is never exported over operator File-1. Live inbound is **never appended** there.

**Do not prescribe `#128` columns.** `#149` Y3 correctly called `#128` EXAMPLE-not-income, then told a later FIX to write those names. That prescription is **killed**.

Wrong map:

| Operator (SSOT) | `#128` EXAMPLE | Do not |
| --- | --- | --- |
| `date` | `date_brussels` | Do not rename the SSOT |
| `usdc` | `usdc_in` | Do not dual-book |
| `eur_mid` / `eur_value` | `eur_note` (explicitly not FX) | Do not treat `eur_note` as a mid; do not fetch ECB onto the 0/0 row |
| `tx` (full sig after pay-proof) | `solana_sig` | Do not copy EXAMPLE into `tx`; do not ignore Base |
| `memo` (what sold) | `what_sold` + `offerte_id` | Do not grow a ninth column on the box |

Kit PR [#91](https://github.com/eyeskull2220/solana-invoice/pull/91) `tools/eur-receive-log/` is a **kit, not File-1** (six columns; `parseAmount` would skip 0/0). Designed out of the ledger artifact in `#141` and of the week plan in `#171`. RESEARCH does not import/export across it.

---

## Two pay-tos only. No third. No IBAN.

| Rail | Pay-to | Asset (mint, **not** a pay-to) |
| --- | --- | --- |
| Solana | `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3` | USDC `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v` |
| Base | `0x9eb954b567ef3616424a6e1bf42c63724930aa54` | USDC `0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913` |

Never a third. A Phantom MCP session address, a Solana Pay `reference`, a facilitator gas key, a CDP wallet, a Helio email-embedded wallet, an explorer “token account,” Ethereum-mainnet USDC `0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`, bridged USDC.e, or `main` leftover Solana-only shop HTML is **not** a treasury.

Leftover `README.md` / `config.js` / `index.html` list the Solana string only. Wallet still has Base. This RESEARCH does **not** patch the shop and does **not** drop Base.

**No IBAN.** No full IBAN. No Revolut last-4. Do not stuff either wallet string into Peppol PaymentMeans. **No seeds.**

---

## No spend. 08:00-only snap. No extra RPC.

Receive-only. File-1 has **no outbound column**. Do not add one. Timeout, null account, empty ATA, and `#176` YELLOW are **not** licenses to send.

**08:00 is the only scheduled snap.** Numbers already taken / CEO-verified. **Do not refresh.** This run did **not** call Phantom `wallet_balances`, did **not** re-query public RPC, did **not** take an environment snapshot. `#128` “replace the stamp” stays killed ([#171](https://github.com/eyeskull2220/solana-invoice/pull/171)).

| Field | Value (already stamped — do not re-read) |
| --- | --- |
| Stamp | **2026-08-27 08:00** Europe/Brussels |
| SOL on Solana pay-to | **0** |
| USDC ATA | **empty / 0** |
| File-1 `usdc` | **0** |
| Inbound txs | **none** |
| Extra snap this RESEARCH | **none** |

Extra RPC only after a **pasted** signature (or Base tx hash), then one `getTransaction` / Base receipt against **one of the two pay-tos**, the native USDC mint on that chain, and the claimed amount. MCP session wallet is not proof. No pay-proof was presented. **Do not snap “just to see.”**

---

## Next inbound (one ledger — still none)

There is **no** inbound. Do not invent one to exercise this recipe.

When (and only when) USDC actually lands, append **one new row** to **operator** File-1 only, after all of:

1. Actual USDC on **one of the two pay-tos**.
2. A **pasted sig** (pay-proof).
3. One confirm RPC: `getTransaction` / Base receipt matches that pay-to + native USDC mint + amount.
4. Operator-pasted public `eur_mid` (never guess, never `1.00` as a stand-in). Not on the 0/0 row.
5. `eur_value` from that mid × `usdc` (not 1:1).
6. Full `tx` (not kit last-6, not `#128` `solana_sig`).
7. `payer` and what sold in `memo`.

Leave the opening 0/0 row intact. Do **not** append to git `#128` FILE-1.csv. Do **not** import `#128` EXAMPLE zeros. Do **not** run it through kit `#91` first. Do **not** merge invert-paper / dca-paper. File-1 is not a FOD table.

---

## STARTABLE / BLOCKED / WAIT (RESEARCH scope)

### STARTABLE

| Item | Note |
| --- | --- |
| Name operator File-1 as SSOT | 8-col header + opening 0/0. Not header-only |
| Keep opening `2026-08-27,0,,0.00,,,,opening 0/0` | Valid empty inbound. Not a sale |
| Cite `#128` as EXAMPLE, never imported | Do not prescribe its columns |
| Cite [#171](https://github.com/eyeskull2220/solana-invoice/pull/171) PLAN-lock | Same SSOT / two pay-tos / 08:00-only snap |
| Refuse third-address / spend / IBAN PRs | Wallet yes/no |

### BLOCKED

| Item | Until |
| --- | --- |
| Describe File-1 as header-only | Never — that RED is closed |
| Prescribe `#128` `date_brussels,usdc_in,…` for a later FIX | Never |
| Import `#128` FILE-1.csv into the box | Never |
| Extra snap / Phantom MCP / public RPC re-query / “replace the stamp” | A pasted pay-proof sig |
| Spend, swap, rebalance, ATA-create, test tx | Never on this RESEARCH |
| Third pay-to / IBAN / seed | Never |
| Invent inbound so the CSV looks used | Never |
| Book 1 USDC = 1 EUR | Never |
| Patch leftover shop HTML from Wallet | Never (Builder / CEO own the face) |

### WAIT

| Item | Waiting on |
| --- | --- |
| First real File-1 inbound row | Actual USDC on a listed pay-to **and** pay-proof **and** operator `eur_mid` |
| Phantom MCP live read | Not required. Timeout was already WAIT. Do not send to test |

---

## Bar this RESEARCH meets (reviewer `#176` acceptance)

A Wallet RESEARCH pack is GREEN only if it states, in one pass:

1. **File-1 current-state** = operator `receive-log.csv`, **not** header-only, opening `2026-08-27,0,,0.00,,,,opening 0/0` left intact. Empty inbound is valid. Not a parse fail. Not a sale. **Met.**
2. **Columns** = `date,usdc,eur_mid,eur_value,payer,memo,tx,notes`. `#128` `date_brussels,usdc_in,…` is EXAMPLE docs, never imported. Do not prescribe those columns. **Met.**
3. **Exactly two pay-tos.** The strings above. Never a third. No IBAN. **Met.**
4. **No spend** in STARTABLE. **Met.**
5. **08:00-only snap.** No extra RPC this sitting. **Met.**
6. **GREEN = pack cleanliness, not inbound.** There is no inbound. **Met.**

RESEARCH stage after this page: **locked.** A later reviewer scores the stage. This file does not grade itself GREEN. Clean pack ≠ funded treasury.

---

## Sources (cite, do not re-open as SSOT)

| Source | Use here |
| --- | --- |
| PR [#176](https://github.com/eyeskull2220/solana-invoice/pull/176) `REVIEW-01-research.md` | YELLOW to close. Two File-1 hygiene rows. GREENS kept. |
| PR [#171](https://github.com/eyeskull2220/solana-invoice/pull/171) `PLAN-lock.md` | PLAN already locked the same SSOT, `#128` never-imported, 08:00-only snap, two pay-tos. Cite. Do not fork a second book. |
| PR [#149](https://github.com/eyeskull2220/solana-invoice/pull/149) `01-adv-research.md` | Advocate RESEARCH. YELLOW. 0/0 valid and two pay-tos kept; header-only live-desk and `#128` NOTES prescription designed out. |
| PR [#141](https://github.com/eyeskull2220/solana-invoice/pull/141) File-1 after-fix | Operator File-1 GREEN as a ledger artifact. Opening 0/0. Kit `#91` designed out of that artifact. |
| PR [#128](https://github.com/eyeskull2220/solana-invoice/pull/128) `FILE-1.csv` | EXAMPLE docs. Wrong columns. Never imported. Not a FIX recipe. |
| PR [#91](https://github.com/eyeskull2220/solana-invoice/pull/91) `tools/eur-receive-log/` | Kit. Not File-1. |
| leftover `main` `README.md` / `config.js` | Solana treasury + mint only. Base is Wallet, not a shop patch from this file. |

No shop HTML. No mail. No CODE from this RESEARCH. No CSV written in git.

---

## What this run did / did not do

| Did | Did not |
| --- | --- |
| Wrote this RESEARCH lock | Extra snap / Phantom `wallet_balances` / public RPC re-query |
| Named operator File-1 as SSOT, **not** header-only | Patch box CSV / invent a second opening row |
| Left opening `2026-08-27,0,,0.00,,,,opening 0/0` | Treat 0/0 as a parse fail or a sale |
| Retired `#128` columns from any later-FIX recipe | Import or append to `#128` FILE-1.csv |
| Cited [#171](https://github.com/eyeskull2220/solana-invoice/pull/171) PLAN-lock | Re-score PLAN; implement `#150` / `#128` / `#91` |
| Froze two pay-tos; no IBAN; no spend | Invent inbound, a third pay-to, an IBAN, or a seed |
| | Edit shop HTML, catalog, kit files, mail |

---

End. Docs only. No spend. No snap. No RPC. No IBAN. Two pay-tos. Empty inbound valid. GREEN = pack cleanliness, not inbound. There is no inbound.
