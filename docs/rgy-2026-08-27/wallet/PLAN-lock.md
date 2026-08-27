# Wallet PLAN lock

**Seat:** Wallet (PLAN rewrite)  
**Date:** 2026-08-27  
**Closes:** reviewer PR [#165](https://github.com/eyeskull2220/solana-invoice/pull/165) PLAN stage **RED**  
**This file is the PLAN.** It does not implement. It does not spend. It does not snap. It does not invent a third pay-to, an IBAN, a seed, or an inbound.

A later Wallet agent follows **this page**. Not `#150` (advocate YELLOW). Not `#128` (EXAMPLE git stub). Not `#91` (kit). Not `#82` (later-week research).

---

## Why this page exists

PR [#165](https://github.com/eyeskull2220/solana-invoice/pull/165) scored Wallet PLAN **RED (not GREEN)**. GREEN only if the plan has no RED and no YELLOW. `#150` overall YELLOW is not a pass.

Two RED rows remained in the plan corpus:

| Gate | Why it was RED | This page |
| --- | --- | --- |
| Local File-1 SSOT | Operator vs `#91` vs `#128` all claimed to be the inbound ledger | Operator `receive-log.csv` is the only SSOT. `#128` is EXAMPLE docs, never imported. `#91` is a kit, not File-1. |
| `#82` not this week | Open ultra page still reads as a build order (Idea 1 now) | `#82` is cited. Not scheduled. Do not implement. |

YELLOW rows that a later agent could still walk around:

| Gate | Why it was YELLOW | This page |
| --- | --- | --- |
| 08:00 is the only scheduled snap | `#128` still invites a later live read to “replace the stamp” | Killed. 08:00 is the only scheduled snap. |
| No extra snap unless pay-proof | Same `#128` live-read license | Extra RPC only after a pasted sig. |
| Exactly two pay-tos | `#82` overlays (Helio / x402 / puller / CDP) still on that page | Those overlays stay on `#82`. They are not STARTABLE here. |
| Next inbound recipe on one ledger | “Log it in FILE-1” without naming which FILE-1 | Append only to operator File-1. |

Until this lock, a later agent that “logs the next inbound in FILE-1” or “continues Wallet ultra” could split the books or ship a SKU.

---

## Hard locks (do not bargain)

These override `#82`, `#91`, `#128`, `#150`, leftover shop HTML, and every “just this once.”

### 1. SSOT is operator File-1

**Canonical File-1** is the operator box:

```
/home/box/agent-data/projects/agent-treasury/receive-log.csv
```

**Exact columns (8):**

```
date,usdc,eur_mid,eur_value,payer,memo,tx,notes
```

**Opening row (leave intact):**

```
2026-08-27,0,,0.00,,,,opening 0/0
```

CEO-read bytes (PR [#141](https://github.com/eyeskull2220/solana-invoice/pull/141), GREEN as a ledger artifact): empty `eur_mid` on that zero row is valid. `eur_value=0.00` is zero-of-zero, **not** 1 USDC = 1 EUR. Not a fill. Not a filing. Not inbound.

This VM cannot open the box. Do not patch the box CSV from a PLAN page. Do not invent a second opening row in git.

### 2. PR `#128` FILE-1.csv is EXAMPLE docs, never imported

PR [#128](https://github.com/eyeskull2220/solana-invoice/pull/128) writes `docs/rgy-2026-08-27/wallet/FILE-1.csv`:

```
date_brussels,usdc_in,eur_note,solana_sig,payer,what_sold,offerte_id
2026-08-27,0,EXAMPLE Phantom 0/0 no inbound USDC,EXAMPLE,EXAMPLE,EXAMPLE,EXAMPLE
```

That file is **EXAMPLE documentation**. It is **not** SSOT. It is **never imported** into operator File-1. It is never exported over operator File-1. Live inbound is **never appended** there.

Wrong map vs the operator header:

| Operator (SSOT) | `#128` EXAMPLE | Do not |
| --- | --- | --- |
| `date` | `date_brussels` | Do not rename the SSOT |
| `usdc` | `usdc_in` | Do not dual-book |
| `eur_mid` / `eur_value` | `eur_note` (explicitly not FX) | Do not treat `eur_note` as a mid |
| `tx` (full sig after pay-proof) | `solana_sig` | Do not copy EXAMPLE into `tx` |
| `memo` (what sold) | `what_sold` + `offerte_id` | Do not grow a ninth column on the box |

`#128` `WALLET-FIX.md` sentence **killed by this PLAN:** “If a later Wallet seat gets a live read, replace the stamp with that read.” That is a second snap with no pasted signature. **Do not replace the 08:00 stamp.** Keep 08:00 0/0 until a **later day’s** 08:00 says otherwise, or until a real inbound is appended after pay-proof.

### 3. Kit PR `#91` schema is a kit, not File-1

PR [#91](https://github.com/eyeskull2220/solana-invoice/pull/91) `tools/eur-receive-log/` is an **operator pack / catalog kit**. Header:

```
date,usdc,eur_mid,memo,tx,notes
```

Same basename `receive-log.csv` does not make it File-1. `#141` already designed the kit out of the ledger artifact. This PLAN designs it out of the **week plan**.

| Kit `#91` | Operator File-1 (SSOT) |
| --- | --- |
| 6 columns | 8 columns (`eur_value`, `payer` exist only here) |
| no derived EUR in CSV | `eur_value` is a column |
| `tx` last-6 only | next inbound: full `tx` after `getTransaction` / Base receipt |
| `parseAmount` rejects `usdc ≤ 0`; `validRow` requires `eur_mid` and `tx` | empty mid allowed on the 0/0 opening row; `usdc=0` is valid |
| header-only template | opening 0/0 row is required |
| catalog card **49 USDC** | not a shop card; Wallet this week **rejects** USDC-on-face, does not ship a new pack |

Exact exclusions:

1. **Do not import** operator File-1 into `eur-receive-log.html`. The 0/0 row would be **skipped**. That is how 0/0 dies.
2. **Do not export** kit CSV over the box file. That drops `payer` and `eur_value` and truncates `tx` to last-6.
3. **Do not shrink** operator File-1 to six columns to “match Wallet’s template.”
4. **Do not treat** kit `tools/eur-receive-log/receive-log.csv` as the sales ledger.
5. **Do not merge** the three headers into one super-header.

`#91` may stay an unmerged operator pack. Aligning it is not this PLAN’s patch.

### 4. PR `#82` is not this week. Do not implement. Cite only.

PR [#82](https://github.com/eyeskull2220/solana-invoice/pull/82) `docs/ideas-wallet-ultra.md` is **research behind the shop face**. It pins the two pay-tos and bans new keys. It is the right *class* of later rail work. It is **not** the Wallet PLAN for **27 Aug–2 Sep 2026**.

CEO Rails lane (PR [#113](https://github.com/eyeskull2220/solana-invoice/pull/113), this week):

| Day | Rails cell |
| --- | --- |
| D0 | Phantom receive-only. No rebalance. |
| D1 | Confirm receive address unchanged; do not print it on the OFFERTE. |
| D2 | EUR receive-log as **operator pack**, not a shop card. |
| D3 | Idle unless a receive happened. |
| D4 | Refuse any PR that adds a third address or SIWE. |

That is **watch**. It is not “ship dual-chain 490 / x402 990 / DeskCrew 790 / retainer 490 / Peppol 1490.”

Cite (do not schedule, do not build):

| `#82` idea | Price | Status this week |
| --- | --- | --- |
| 1 Dual-chain USDC invoice desk | 490 USDC | Cite only |
| 2 x402 seller door | 990 USDC | Cite only |
| 3 DeskCrew-class agent door | 790 USDC kit | Cite only |
| 4 Recurring USDC retainer (push) | 490 USDC + 190/period | Cite only |
| 5 Belgian Peppol dual-rail | 1490 USDC | Cite only |

`#82` **suggested build order starts at Idea 1 now.** That sentence is not a Wallet STARTABLE. Builder already failed one-kit unlocks on the shop. Wallet does not get a pass.

Helio payout-wallet overlay, x402 facilitator defaults that mint an EOA, Solana Subscriptions **puller** key, Base CDP `subscriptionOwner`, DeskCrew board-ownership keys: documented on `#82` as blocked or optional. **Not STARTABLE here.** A later agent “continuing Wallet ultra” does not ship Idea 2/4 “just for the facilitator.”

Build `#82` only on a **later week** plus a CEO Rails cell that names **one** idea. This page does not name one.

### 5. 08:00 is the only scheduled snap. No 16:00. Extra RPC only after a pasted sig.

| Rule | Meaning |
| --- | --- |
| **08:00 only scheduled snap** | Stamp is **2026-08-27 08:00** Europe/Brussels. SOL **0** / USDC ATA **empty** on `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3`. File-1 opening 0/0 is the same calendar day. **Do not refresh it tonight.** |
| **No 16:00** | Weekday 16:00 RPC is **not** a ritual. Quiet-if-zero does not make a second look free. Skip unless a pasted sig arrived after 08:00 — and even then the call is pay-proof confirm, not a balance poll. |
| **No 20:56** | Ultra Wallet’s 20:56 0/0 is **not** this PLAN’s stamp. No third look. |
| **No extra snap unless pay-proof** | Pay-proof = a **pasted signature** (or Base tx hash) that then **must** be confirmed with one `getTransaction` / Base receipt against **one of the two pay-tos**, the **native USDC mint on that chain**, and the claimed amount. |
| **Timeout → WAIT** | Phantom MCP `wallet_balances` timeout is already the right WAIT. Do not retry until it looks non-zero. Do not send to test. |
| **MCP session wallet is not the treasury** | `wallet_balances` / `wallet_addresses` is the **session wallet**. If it is not one of the two pay-tos, that is a third address. Do not watch it. Do not log it. Do not use it as a “confirm.” |

Not pay-proof: explorer screenshots, Phantom UI, MCP session balances, “DeskCrew ticket if USDC ≥ 0.06,” a later live `wallet_balances` to replace the stamp.

Failed `meta.err`, wrong mint, wrong owner, or RPC miss is **not** inbound. Do not book it. Do not snap “just to see.”

**This run did not call Phantom `wallet_balances`, did not re-query public RPC, did not take a second snap.** No pay-proof was presented.

### 6. Exactly two pay-tos. No IBAN.

| Rail | Pay-to | Asset (mint, **not** a pay-to) |
| --- | --- | --- |
| Solana | `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3` | USDC `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v` |
| Base | `0x9eb954b567ef3616424a6e1bf42c63724930aa54` | USDC `0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913` |

Never a third. A Phantom MCP session address, a Solana Pay `reference`, a facilitator gas key, a CDP wallet, a Helio email-embedded wallet, an explorer “token account,” or `main` leftover Solana-only shop HTML is **not** a treasury.

PR [#94](https://github.com/eyeskull2220/solana-invoice/pull/94) Solana Pay URLs use the **same** Solana string. Not Helio. Not a second address.

**No IBAN.** No full IBAN. No Revolut last-4. Revolut remains denied until Personal KYC (Compliance). Do not invent a bank rail. Do not stuff either wallet string into Peppol `PayeeFinancialAccount` / PaymentMeans. `#82` Idea 5 already forbids that; this PLAN does not implement Idea 5.

**No seeds.** No mnemonic, no private key, no `CDP_WALLET_SECRET`.

Shop / mail copy stays EUR-first. These strings are Wallet rails, not the public face. Wallet’s job this week is **reject** PRs that print them on shop/mail, not a new pay page.

### 7. No spend

Receive-only. No send, swap, rebalance, perps, Helio, Kraken USDC out, ATA-rent SOL buy, “tiny USDC to ourselves so File-1 has a tx,” “Helio Pay Link to see if it lands.”

File-1 has **no outbound column**. Do not add one.

### 8. No 1 USDC = 1 EUR. No paper-book merge.

Never book 1 USDC = 1 EUR. Do not fetch ECB into the ledger from a Wallet seat. Operator pastes `eur_mid` on a **real** inbound. Not on the 0/0 row.

File-1 is inbound USDC to the two pay-tos. Coder invert-paper / dca-paper fills are not sales. Never copy paper equity into `usdc`. Invert gate is Coder + CEO, not Wallet. File-1 is not a FOD table.

---

## 08:00 stamp (the only numbers this PLAN may use)

Already taken / CEO-verified. **Do not refresh.**

| Field | Value |
| --- | --- |
| Stamp | **2026-08-27 08:00** Europe/Brussels |
| Solana pay-to | `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3` |
| SOL | **0** |
| USDC (Solana ATA) | **empty / 0** |
| File-1 `usdc` | **0** |
| File-1 `eur_mid` | **empty** (valid on a zero row) |
| File-1 `eur_value` | **0.00** (zero of zero) |
| Inbound txs | **none** |
| Extra snap this PLAN | **none** (no pay-proof presented) |

`#141` G5 public-RPC corroboration was a **prior** batch. This PLAN does not repeat it.

---

## Next inbound (one ledger)

Append **one new row** to **operator** File-1 only, after all of:

1. Actual USDC on **one of the two pay-tos**.
2. A **pasted sig** (pay-proof).
3. One confirm RPC: `getTransaction` / Base receipt matches that pay-to + native USDC mint + amount.
4. Operator-pasted public `eur_mid` (never guess, never `1.00` as a stand-in).
5. `eur_value` from that mid × `usdc` (not 1:1).
6. Full `tx` (not kit last-6).
7. `payer` and what sold in `memo`.

Leave the 0/0 opening row intact. Missing inbound stays missing. Do not invent the row to make a recipe look used.

Do **not** append that row to git `#128` FILE-1.csv. Do **not** import `#128` EXAMPLE zeros. Do **not** run it through kit `#91` first.

---

## STARTABLE / BLOCKED / WAIT

### STARTABLE

| Item | Note |
| --- | --- |
| Keep File-1 opening 0/0 | Valid. Not a fill. Not a filing. |
| 08:00 stamp as the day’s snap | Already taken. Use it. Do not refresh it tonight. |
| Pay-proof confirm | Only if a sig is pasted. Then **one** RPC. |
| Refuse third-address / SIWE / spend PRs | Wallet yes/no on Rails. |
| Point Builder/Scout at EUR face | Strings stay off shop/mail. |
| Cite `#82` | Research. Not a build ticket. |

### BLOCKED

| Item | Until |
| --- | --- |
| Extra `wallet_balances` / extra RPC poll / “replace the stamp” | A pasted pay-proof sig |
| Scheduled 16:00 / 20:56 snap | Never; not required |
| Spend, swap, rebalance, perps, Helio, Kraken USDC out, ATA-rent buy | Operator **yes** on a Wallet page that is not receive-only — not this week |
| Third pay-to / new key / SIWE / puller / CDP owner | Never on this board |
| Full IBAN / Revolut last-4 | Personal KYC + Compliance, not Wallet invention |
| Book 1 USDC = 1 EUR | Never |
| Merge dca-paper / invert-paper into File-1 | Never |
| Build `#82` SKUs (any of the five) | A later week + CEO Rails cell that names **one** idea |
| Replace operator File-1 with `#128` columns | Never |
| Import `#128` FILE-1.csv into the box | Never |
| Import/export operator File-1 through kit `#91` | Never (0/0 would be skipped) |
| Shrink operator File-1 to six columns | Never |
| Treat kit `tools/eur-receive-log/receive-log.csv` as the sales ledger | Never |
| Merge the three headers into one super-header | Never |

### WAIT

| Item | Waiting on |
| --- | --- |
| First real File-1 inbound row | Actual USDC on a listed pay-to **and** pay-proof RPC **and** operator `eur_mid` |
| Phantom MCP live read | Not required. Timeout was already the right WAIT. Do not send to test |
| EUR receive-log as shop card | Never; operator pack only, and only after hide-the-coin |
| Accountant / FOD table | Compliance, after KBO — File-1 is not that table |
| `#82` as a Rails cell | A later week + CEO naming **one** idea |

---

## Bar this PLAN meets (reviewer `#165` acceptance)

A Wallet PLAN is GREEN only if it states, in one pass:

1. **08:00 snap** is named, dated, and is the only scheduled balance read. Numbers match File-1 0/0 unless a **later day’s** 08:00 says otherwise. **Met.**
2. **No extra snap unless pay-proof.** Pay-proof = pasted sig + `getTransaction` / receipt on one of the two pay-tos + native USDC mint + amount. MCP session wallet is not proof. **Met.** `#128` replace-the-stamp is killed.
3. **Canonical File-1** = operator header `date,usdc,eur_mid,eur_value,payer,memo,tx,notes` with opening `2026-08-27,0,,0.00,,,,opening 0/0` left intact. `#128` is EXAMPLE docs, never imported. `#91` is a kit, not File-1. Not dual-SSOT. **Met.**
4. **16:00 is not required.** No third look at 20:56. **Met.**
5. **No spend** in STARTABLE. Helio, rebalance, send-to-test, Kraken USDC sale, ATA-rent buy are in BLOCKED. **Met.**
6. **Exactly two pay-tos.** The strings above. Never a third. No IBAN. **Met.**
7. **`#82` not scheduled** on the 27 Aug–2 Sep Rails lane. Cite only. Do not implement. **Met.**
8. Next inbound recipe matches STORE: public mid, `eur_value` not 1:1, tx after proof, payer, what sold. On **operator** File-1 only. No paper-book merge. No FOD claim. **Met.**

PLAN stage after this page: **locked.** A later reviewer scores the stage. This file does not grade itself GREEN.

---

## Sources (cite, do not re-open as SSOT)

| Source | Use here |
| --- | --- |
| PR [#165](https://github.com/eyeskull2220/solana-invoice/pull/165) `REVIEW-02-plan.md` | RED to close. Acceptance bar copied into the section above. |
| PR [#150](https://github.com/eyeskull2220/solana-invoice/pull/150) `02-adv-plan.md` | Advocate PLAN. YELLOW. Design-outs kept; this page is the lock, not another scorecard. |
| PR [#149](https://github.com/eyeskull2220/solana-invoice/pull/149) `01-adv-research.md` | Research. 0/0 valid. Two pay-tos. Did not write a ledger. |
| PR [#141](https://github.com/eyeskull2220/solana-invoice/pull/141) File-1 after-fix | Operator File-1 GREEN as a ledger artifact. Kit `#91` already designed out of that artifact. |
| PR [#128](https://github.com/eyeskull2220/solana-invoice/pull/128) `FILE-1.csv` + `WALLET-FIX.md` | EXAMPLE docs. Wrong columns. Never imported. Replace-the-stamp killed. |
| PR [#91](https://github.com/eyeskull2220/solana-invoice/pull/91) `tools/eur-receive-log/` | Kit. Not File-1. |
| PR [#82](https://github.com/eyeskull2220/solana-invoice/pull/82) `docs/ideas-wallet-ultra.md` | Cite only. Not this week. Do not implement. |
| PR [#113](https://github.com/eyeskull2220/solana-invoice/pull/113) CEO Rails | Receive-only week. `#82` stays behind the shop face. |
| PR [#94](https://github.com/eyeskull2220/solana-invoice/pull/94) | Same Solana treasury. Not a second address. |
| `main` `config.js` / README | Solana treasury + mint only. Base string is **not** on `main`. Shop leftover, not a third treasury. |

No shop HTML. No mail. No CODE from this PLAN.

---

## What this run did / did not do

| Did | Did not |
| --- | --- |
| Wrote this PLAN lock | Extra snap / Phantom `wallet_balances` / public RPC re-query |
| Named operator File-1 as the only SSOT | Import `#128` FILE-1.csv |
| Designed `#91` out as a kit | Shrink or patch box CSV |
| Cited `#82`; did not schedule it | Implement `#82`, Helio, x402, puller, CDP owner |
| Set 08:00 = only scheduled snap; no 16:00 | Spend, swap, rebalance, perps |
| Froze two pay-tos; no IBAN | Invent a third pay-to, inbound, IBAN, or seed |
| | Edit shop HTML, catalog, kit files, mail |

---

End. Docs only. No spend. No snap. No IBAN. Two pay-tos. `#82` cite only.
