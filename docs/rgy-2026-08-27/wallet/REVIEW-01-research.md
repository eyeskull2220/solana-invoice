# REVIEWER — Wallet RESEARCH stage RGY

Seat: **REVIEWER**. Stage: **Wallet RESEARCH** only. Date: **2026-08-27**.

Score **starts at 0**. A row is GREEN only when the research pack is sourced, internally consistent with the locked book, and a later Wallet plan/FIX can proceed **without inventing inbound, a third pay-to, a spend, an extra snap, an IBAN, or a File-1 schema**. This file does not implement. No spend. No extra snap. No Phantom MCP. No public RPC re-query. No shop HTML. No mail.

**Artifact judged:** [PR #149](https://github.com/eyeskull2220/solana-invoice/pull/149) `docs/rgy-2026-08-27/wallet/01-adv-research.md` (branch `cursor/wallet-adv-research-1755`, leftover repo HEAD `2170952`).

**Book (this batch):** operator `receive-log.csv` as scored GREEN in [PR #141](https://github.com/eyeskull2220/solana-invoice/pull/141) `REVIEW-file1-after-fix.md`. Path `/home/box/agent-data/projects/agent-treasury/receive-log.csv` (this run cannot open the box). CEO-read bytes in #141 are the File-1 source of truth.

**Not judged this batch:** Wallet PLAN ([#150](https://github.com/eyeskull2220/solana-invoice/pull/150) `02-adv-plan.md`), Wallet FIX ([#128](https://github.com/eyeskull2220/solana-invoice/pull/128) `FILE-1.csv`), kit [#91](https://github.com/eyeskull2220/solana-invoice/pull/91), shop/Builder.

**GREEN on this page means the research pack is clean. It does not mean there is inbound. There is no inbound.**

**GREEN count: 10 / 12. Stage: not closed. Overall: YELLOW.**

| item | RED/YELLOW/GREEN | note | fix-if-not-green |
| --- | --- | --- | --- |
| File-1 0/0 is valid | GREEN | Pack scores header-only **and** first-row 0/0 as **valid empty inbound**, not a parse fail, not a sale, not a reason to send. Matches this batch lock and STORE: 0/0 is a valid first row. Do not invent a payer, offerte, signature, or positive `usdc`. | — |
| File-1 current-state vs book | YELLOW | Pack live-desk: **“Header only. No inbound row.”** Book (#141 GREEN): eight-column header **plus** opening row `2026-08-27,0,,0.00,,,,opening 0/0 — public RPC SOL 0, USDC ATA empty on 96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3. No inbound. Not a fill. Not a filing.` Header-only was the old RED #141 closed. Empty inbound is still true. The **shape** of File-1 in the pack is stale. | Name the book: operator `receive-log.csv`, opening 0/0 row left intact. Do not describe File-1 as header-only. |
| File-1 later-FIX columns | YELLOW | Pack NOTES: “if a later FIX writes the CSV” use `date_brussels, usdc_in, eur_note, solana_sig, payer, what_sold, offerte_id` — the [#128](https://github.com/eyeskull2220/solana-invoice/pull/128) map. Pack Y3 calls #128 EXAMPLE not income (correct) then **prescribes those columns**. Book header is `date,usdc,eur_mid,eur_value,payer,memo,tx,notes`. `eur_note` is not `eur_mid`/`eur_value`. `solana_sig` is not full `tx` after pay-proof and ignores Base. A later FIX that follows #149 NOTES splits the books. | Retire #128 columns from any Wallet FIX recipe. Canonical File-1 = operator 8-col header. #128 stays a stub, not SSOT. Next inbound: public `eur_mid`, `eur_value` (never 1:1), `tx` after `getTransaction` / Base receipt, `payer`, what sold in `memo`. |
| two pay-tos only | GREEN | Solana `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3`. Base `0x9eb954b567ef3616424a6e1bf42c63724930aa54`. Pack writes **exactly those two** as receive addresses. Third pay-to is a stop (Phantom extra chains, Pay `reference`, gas key, CDP/Helio/MCP session, EIP-55 recase). No third string invented in the file. | — |
| mints ≠ pay-tos | GREEN | Circle native USDC cited as mints: Solana `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v` (matches leftover `config.js`), Base `0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913`. Ethereum USDC `0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48` named as **wrong token**, not a rail. Bridged USDC.e out. CCTP / Gateway / Circle developer wallets designed out as a third custody path. | — |
| no spend this pack | GREEN | Pack is report-only. No `buy`, `wallet_rebalance`, `solana_send` confirmed, CCTP, Gateway, Helio, Kraken USDC out, ATA-create, rent-fund, test tx. Timeout / null account / empty ATA are **not** licenses to send. This reviewer run did not send either. | — |
| no invented inbound | GREEN | No fake payer, offerte, signature, or `usdc>0`. 9/49 leftover SKUs not marked received. Unlock-by-signature unused. Stamp VOORBEELD / receive-only / not FACTUUR / not INVOICE / not a sale. 0 inbound is not a fill and not a filing. | — |
| no IBAN / seeds | GREEN | No full IBAN digits. No Bancontact. No Peppol `PayeeFinancialAccount` stuffed with base58/`0x`. No seed, private key, or `CDP_WALLET_SECRET`. Kraken MCP error is not a bank-rail fallback. | — |
| Phantom 0/0; timeout ≠ funds | GREEN | Operator stamp **0 SOL / 0 USDC**. Pack: agent wallet starts empty; MCP `wallet_addresses` / `wallet_balances` **-32001** twice; did not send to test. Timeout ≠ hidden balance. Agent wallet ≠ personal Phantom ≠ the two pay-tos. Do not replace treasury with whatever MCP would return. | — |
| shop leftover Solana-only | GREEN | Pack documents leftover `README.md` / `config.js` / `index.html` listing Solana only, and **does not** drop Base from Wallet or patch the shop. This checkout confirms: `config.js` / README / `index.html` / `catalog.html` carry `96BT6…buHk3` only; Base is absent on `main`. Desk yellow, pack hygiene closed. Builder/CEO own the face. | — |
| no extra snap this review | GREEN | This sitting did **not** call Phantom MCP, did **not** re-query Solana/Base RPC, did **not** take an environment snapshot. Chain zeros in #149 (slot ~442169910 / ~442170162) and #141 G5 are already-taken stamps. Pack re-check curls are **not** run here. A later live `wallet_balances` “to replace the stamp” is extra snap without pay-proof — out. | — |
| scope hygiene | GREEN | #149 is a single new markdown under `docs/rgy-2026-08-27/wallet/`. Adversarial section before RGY tables. No CSV written. No shop/catalog/kit edit. No mail. Sibling PLAN (#150) and FIX (#128) out of this batch. Paper books not merged into File-1. | — |

## Book vs pack (why not GREEN)

#141 CEO-read File-1 (the book):

```
date,usdc,eur_mid,eur_value,payer,memo,tx,notes
2026-08-27,0,,0.00,,,,opening 0/0 — public RPC SOL 0, USDC ATA empty on 96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3. No inbound. Not a fill. Not a filing.
```

#149 scores the **zero** correctly and then points a later FIX at a **different file**: git `FILE-1.csv` with `usdc_in` / `eur_note` / `solana_sig`. That is the cleanliness miss. 0/0 valid is not the same as “any 7-col EXAMPLE CSV is File-1.”

## Design-out (every YELLOW on the pack)

Until the matching research row is GREEN, a later Wallet file **must not**:

1. **Describe File-1 as header-only.** The book has the opening 0/0 row. Leave that row. Append only after USDC lands on one of the two pay-tos **and** pay-proof.
2. **Write or append inbound on #128 columns.** Canonical header remains `date,usdc,eur_mid,eur_value,payer,memo,tx,notes`. Empty `eur_mid` on the 0/0 row stays. Never book 1 USDC = 1 EUR. Never merge invert-paper / dca-paper. Not a FOD table.
3. **Treat pack YELLOW (MCP timeout, leftover shop HTML, #128 EXAMPLE) as permission to send, snap, or merge schemas.** Those are desk notes. They are not this review’s leftover except where they steer the wrong ledger.

GREEN locks the pack already holds (research of these is closed even though the pack is YELLOW): exactly two pay-tos; no spend; no invented inbound; no IBAN/seed; 0/0 is valid; mints are mints; agent wallet is not treasury; do not patch leftover shop HTML from Wallet; do not extra-snap without a pasted sig + `getTransaction` / receipt.

## Cites (this reviewer sitting — no extra snap)

| Source | What was opened |
| --- | --- |
| [#149](https://github.com/eyeskull2220/solana-invoice/pull/149) `01-adv-research.md` | Artifact — adversarial first; two pay-tos; 0/0 valid; header-only live-desk; #128 columns in NOTES |
| [#141](https://github.com/eyeskull2220/solana-invoice/pull/141) `REVIEW-file1-after-fix.md` | Book GREEN — 8-col `receive-log.csv`, opening 0/0, #128 wrong map designed out |
| leftover `main` `README.md` / `config.js` / `index.html` / `catalog.html` | Solana pay-to + mint only; Base absent (pack Y2 holds) |
| Phantom MCP / public RPC this sitting | **not called** (no extra snap) |
| [#150](https://github.com/eyeskull2220/solana-invoice/pull/150) / [#128](https://github.com/eyeskull2220/solana-invoice/pull/128) | Out of this batch (PLAN / FIX) |

## Verdict

Wallet RESEARCH pack (#149) is **not GREEN**.

Ten rows closed: **0/0 is valid**, **exactly two pay-tos**, **mints ≠ rails**, **no spend**, **no invented inbound**, **no IBAN/seeds**, **Phantom 0/0 + timeout ≠ send (agent ≠ treasury)**, **shop leftover documented not patched**, **this review did not extra-snap**, **single-file scope**.

Two hygiene rows stay **YELLOW**: the pack’s File-1 is still “header only” plus a #128 column recipe, while the book is operator `receive-log.csv` with an opening 0/0 row (#141 GREEN). A later FIX that follows #149 NOTES would write the wrong ledger.

GREEN only when those two File-1 rows name the book and retire the #128 map — still without a spend and still without an extra snap.

No implementation in this PR. No spend. No extra snap.
