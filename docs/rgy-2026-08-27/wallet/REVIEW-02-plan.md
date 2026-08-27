# REVIEW — Wallet PLAN (02)

**Seat:** REVIEWER
**Batch:** NEW (PLAN only; old notes are context, not this grade)
**Date:** 2026-08-27
**Artifact:** PR [#150](https://github.com/eyeskull2220/solana-invoice/pull/150) `docs/rgy-2026-08-27/wallet/02-adv-plan.md`
**This file:** judgment only. **No implement.** No spend. No extra snap.

Verdict for the stage is the worst row. **GREEN only if the plan has no RED and no YELLOW.** It has both. PLAN is not closed.

| Gate | Score |
| --- | --- |
| 08:00 is the only scheduled snap | **YELLOW** |
| No extra snap unless pay-proof | **YELLOW** |
| Local File-1 SSOT (operator 8-col) | **RED** |
| 16:00 not required | **GREEN** |
| No spend in STARTABLE | **GREEN** |
| File-1 0/0 treated as valid | **GREEN** |
| Exactly two pay-tos | **YELLOW** |
| `#82` not this week’s Rails plan | **RED** |
| No 1 USDC = 1 EUR | **GREEN** |
| No paper-book merge into File-1 | **GREEN** |
| Next inbound recipe on one ledger | **YELLOW** |
| This review extra-snapped or spent | **GREEN** (neither) |
| **PLAN stage** | **RED** (not GREEN) |

Advocate `#150` overall **YELLOW** is not a pass. Two RED rows remain in the plan corpus. Watch is startable. PLAN is not GREEN.

---

## Locks for this batch (honoured)

| Lock | Meaning this run |
| --- | --- |
| **08:00 only snap** | Stamp is **2026-08-27 08:00** Europe/Brussels. SOL 0 / USDC ATA empty on `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3`. File-1 opening `2026-08-27,0,,0.00,,,,opening 0/0`. **This run did not re-query Phantom MCP, did not re-query public RPC, did not take a second snap.** |
| **No extra snap unless pay-proof** | No pasted signature was presented. No `getTransaction`. No `wallet_balances`. |
| **Local File-1 SSOT** | Operator box `/home/box/agent-data/projects/agent-treasury/receive-log.csv`. Header `date,usdc,eur_mid,eur_value,payer,memo,tx,notes`. This VM cannot open the box; CEO-read bytes in PR [#141](https://github.com/eyeskull2220/solana-invoice/pull/141) are the stamp. Git `#128` `FILE-1.csv` is **not** SSOT. |
| **No 16:00 required** | 16:00 weekday RPC is **not** a ritual. Skip unless a pay-proof arrived after 08:00. |
| **No spend** | No send, swap, rebalance, perps, Helio, Kraken USDC out, ATA-rent buy, “test” transfer. |
| **Pay-tos (exactly two)** | Solana `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3`. Base `0x9eb954b567ef3616424a6e1bf42c63724930aa54`. Never a third. No IBAN. No seeds. |

Mints (not pay-tos): Solana USDC `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v`. Base USDC `0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913`.

---

## What was judged (PLAN sources, not a CODE audit)

PLAN means: the written intent that would tell a later Wallet agent what to start. Scored from zero against:

| Source | What it plans |
| --- | --- |
| PR [#150](https://github.com/eyeskull2220/solana-invoice/pull/150) `02-adv-plan.md` | Advocate adversarial PLAN. Overall YELLOW. Design-outs: 08:00 stamp, pay-proof-only RPC, operator File-1 SSOT, do not ship `#82`. |
| PR [#149](https://github.com/eyeskull2220/solana-invoice/pull/149) `01-adv-research.md` | Research. 0/0 valid. Two pay-tos. Did not write a ledger. |
| PR [#141](https://github.com/eyeskull2220/solana-invoice/pull/141) File-1 after-fix | Operator File-1 **GREEN** as a ledger artifact. Not a week plan. |
| PR [#128](https://github.com/eyeskull2220/solana-invoice/pull/128) `WALLET-FIX.md` + `FILE-1.csv` | Git “File-1”. **Wrong columns.** Invites a later live `wallet_balances` to “replace the stamp.” |
| PR [#91](https://github.com/eyeskull2220/solana-invoice/pull/91) `tools/eur-receive-log/` | Operator pack. Header `date,usdc,eur_mid,memo,tx,notes`. HTML `parseAmount` rejects `usdc ≤ 0` and requires `eur_mid`. Catalog card **49 USDC**. |
| PR [#82](https://github.com/eyeskull2220/solana-invoice/pull/82) `docs/ideas-wallet-ultra.md` | Five rail SKUs at **490–1490 USDC**. Pins the two pay-tos. Optional Helio overlay. x402 / DeskCrew door / push retainer / Peppol annex. Suggested build order starts at Idea 1. |
| PR [#113](https://github.com/eyeskull2220/solana-invoice/pull/113) `docs/ultra-seats/CEO.md` | 7-day Rails: receive-only, confirm address unchanged, EUR receive-log as **operator pack**, refuse third address / SIWE. `#82` stays **behind** the shop face. |
| PR [#94](https://github.com/eyeskull2220/solana-invoice/pull/94) Solana Pay URLs | Same Solana treasury. Not Helio. Not a second address. |
| `main` `config.js` / README | Solana treasury + mint only. Base string is **not** on `main`. |

No Phantom `wallet_balances`. No public RPC re-query. No Helio. No Kraken USDC sale. No shop HTML. No mail.

---

## Scores

### 1. 08:00 is the only scheduled snap — **YELLOW**

**Notes.** This batch’s lock: one scheduled balance read = **08:00**. Numbers match File-1 0/0. A second look tonight is fishing.

`#150` states that lock and did not extra-snap. The PLAN corpus still licenses a later read:

- `#128` `WALLET-FIX.md`: “If a later Wallet seat gets a live read, replace the stamp with that read.” That is a second snap with no pasted signature.
- Phantom MCP `wallet_balances` is the **session wallet**, not the two published treasuries. Using it as a “confirm” is extra snap and possibly a third address.

**Fix-if-not-green.** Kill the replace-the-stamp sentence in `#128`. Next RPC is only `getTransaction` / Base receipt after a pasted sig. Timeout → WAIT. Keep 08:00 0/0. Do not retry until it looks non-zero.

### 2. No extra snap unless pay-proof — **YELLOW**

**Notes.** Pay-proof = pasted signature that then **must** be confirmed with `getTransaction` / Base receipt against one of the two pay-tos, the native USDC mint on that chain, and the claimed amount. Failed `meta.err`, wrong mint, wrong owner, or RPC miss is **not** inbound.

No pay-proof was presented to this run. `#150` honours the lock. `#128` still invites a live read without one. Same yellow as §1; not a second defect to “fix” with a snap.

**Fix-if-not-green.** Same as §1. Explorer screenshots, Phantom UI, MCP session balances, and “DeskCrew ticket if USDC ≥ 0.06” are not pay-proof.

### 3. Local File-1 SSOT — **RED**

**Notes.** User lock: **local File-1 is SSOT.** Three headers still claim to be the inbound ledger:

| Artifact | Header | Opening |
| --- | --- | --- |
| **Operator File-1** (canonical) | `date,usdc,eur_mid,eur_value,payer,memo,tx,notes` | `2026-08-27,0,,0.00,,,,opening 0/0` |
| PR `#91` kit CSV | `date,usdc,eur_mid,memo,tx,notes` | header only |
| PR `#128` git FILE-1 | `date_brussels,usdc_in,eur_note,solana_sig,payer,what_sold,offerte_id` | EXAMPLE zeros |

`#141` already GREEN’d the operator file and designed `#91` out of File-1. That does **not** close PLAN. `#128` is still titled “Wallet FIX: File-1 inbound ledger.” A later agent that “logs the next inbound in FILE-1” without naming **which** FILE-1 will split the books.

`#91` `parseAmount` rejects `usdc ≤ 0`; `validRow` requires `eur_mid` and `tx`. Import of the operator 0/0 row would be **skipped**. That is how 0/0 dies.

**Fix-if-not-green.** Canonical File-1 = operator `receive-log.csv` only. Do not append live inbound to git `#128`. Do not shrink operator File-1 to six columns. Do not treat kit `tools/eur-receive-log/receive-log.csv` as the sales ledger. Do not merge the three files into one super-header.

### 4. 16:00 not required — **GREEN**

**Notes.** This batch: **no 16:00 required.** `#150` WAIT already says 16:00 RPC only if a pay-proof arrived since 08:00; else skip. Quiet-if-zero does not make a second ritual free, and this review does not require that ritual.

Advocate A9 (skip **08:00** because 16:00 quiet-if-zero) stays a valid attack on any later plan that drops the morning stamp. It is not a reason to poll at 16:00 tonight. Ultra Wallet’s 20:56 0/0 is **not** this PLAN’s stamp.

**Fix-if-not-green.** — (closed as a gate). Do not add 16:00 back as a scheduled snap.

### 5. No spend in STARTABLE — **GREEN**

**Notes.** CEO `#113`: Phantom receive-only. `#82` bans perps, new keys, SIWE unless named as a blocker. `#128`: no spend column. `#150` STARTABLE is watch + File-1 0/0 + pay-proof confirm + refuse PRs. None of the plans scored here name send-to-test, Helio, rebalance, or Kraken USDC out as STARTABLE.

A spend would look like: “tiny USDC to ourselves so File-1 has a tx,” “buy SOL for ATA rent,” “Helio Pay Link to see if it lands.” Do not add it.

Revolut remains denied until Personal KYC (Compliance). No full IBAN. No last-4.

### 6. File-1 0/0 treated as valid — **GREEN**

**Notes.** STORE / `#141`: **0/0 is a valid first row.** Not a fill. Not a filing. Empty `eur_mid` on a zero row is valid. Missing inbound stays missing.

`#150` A2 GREEN holds. Scar: `#91` HTML still fights the opening row (see §3). That is a kit defect, not a reason to invent inbound.

### 7. Exactly two pay-tos — **YELLOW**

**Notes.** The lock is GREEN. The open ideas file is not.

Every scored Wallet page repeats:

- Solana `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3`
- Base `0x9eb954b567ef3616424a6e1bf42c63724930aa54`

`#94` does not invent a second Solana. `main` `config.js` is Solana-only (shop leftover, not a third treasury).

`#82` correctly freezes the two strings, then still offers:

- Helio payout-wallet overlay (email signup = **embedded wallet** = third address; called out as blocked, still on the page as optional).
- x402 `payTo` via Dexter (allowed **if** `payTo` stays the two strings; CDP `createX402Server` default mints an EOA — blocked only if Wallet remembers).
- Solana Subscriptions **puller key** and Base CDP `subscriptionOwner` — blocked for automation, still documented as rails.

A later agent “continuing Wallet ultra” can ship Idea 2/4 and mint a key “just for the facilitator.”

**Fix-if-not-green.** `#82` is research behind the shop face, not this week’s plan. STARTABLE Wallet work is watch + File-1 + refuse PRs that add a third string or SIWE. Not a seller door.

### 8. `#82` not this week’s Rails plan — **RED**

**Notes.** CEO `#113` Rails lane (27 Aug–2 Sep):

| Day | Rails cell |
| --- | --- |
| D0 | Phantom receive-only. No rebalance. |
| D1 | Confirm receive address unchanged; do not print it on the OFFERTE. |
| D2 | EUR receive-log as **operator pack**, not a shop card. |
| D3 | Idle unless a receive happened. |
| D4 | Refuse any PR that adds a third address or SIWE. |

That is not “ship dual-chain 490 / x402 990 / DeskCrew 790 / retainer 490 / Peppol 1490.”

`#82` is the right *class* of later rail work and correctly bans new keys. Using it as the Wallet PLAN for this week is a one-kit unlock on the rail side: five SKUs, USDC prices, Helio in the text, x402 facilitator choices. `#82` **suggested build order** starts with Idea 1 now. Builder already failed that pattern on the shop. Wallet does not get a pass.

`#150` correctly says cite, do not build. The page `#82` is still an open Wallet ultra PLAN. A later agent can schedule it.

**Fix-if-not-green.** `#82` stays cited, not scheduled. This week Wallet **watches**. Do not implement from this review.

### 9. No 1 USDC = 1 EUR — **GREEN**

**Notes.** STORE: never book 1 USDC = 1 EUR. File-1 opening `eur_value=0.00` on `usdc=0` is zero-of-zero, not a peg. `#91`: no baked rate. `#128` `eur_note` is explicitly not FX.

Do not fetch ECB into the ledger from a Wallet seat. Operator pastes `eur_mid` on a **real** inbound. Not on the 0/0 row.

### 10. No paper-book merge into File-1 — **GREEN**

**Notes.** File-1 is inbound USDC to the two pay-tos. Coder invert-paper / dca-paper fills are not sales. CEO invert gate is Coder + CEO, not Wallet. No plan scored here copies paper equity into `usdc`. Keep it that way.

### 11. Next inbound recipe on one ledger — **YELLOW**

**Notes.** STORE next inbound: public `eur_mid`, `eur_value` (not 1:1), `tx` after `getTransaction` pay-proof, `payer`, what sold. That sentence only fits the **operator** header (`eur_value` exists there). `#128` has `eur_note`. `#91` stores last-6 in `tx` (pay-proof needs the full sig at verify time).

Until §3 RED is closed, “log the next inbound” is ambiguous. Do not invent the row to make the recipe look used.

**Fix-if-not-green.** Same as §3. Append only to operator File-1 after pay-proof. Leave the 0/0 row intact.

### 12. This review extra-snapped or spent — **GREEN**

**Notes.** No Phantom MCP balance call. No public RPC re-query. No send. No Helio. No shop HTML. No mail. `#141` G5 chain corroboration was a **prior** batch; this batch does not repeat it.

---

## What is already true (does not save PLAN)

These are not GREEN for the **stage**. They are notes so a later agent does not “fix” the wrong thing:

- Operator File-1 0/0 is valid (`#141`). Do not invent inbound.
- Two pay-to strings are frozen across `#82` / `#94` / `#128` / `#150`. Do not add a third “for completeness.”
- `#150` did not spend and did not extra-snap. Copying that GREEN into an extra `wallet_balances` tonight would spend it.
- `#91` may stay an unmerged operator pack. Aligning it is not this review’s patch.
- Shop face still prints USDC (`main` catalog / `#91` 49 USDC card). Wallet’s job this week is **reject**, not a new pay page.

---

## GREEN looks like (acceptance for a later PLAN rewrite)

A single Wallet PLAN page, merged before CODE, that a later agent can follow without inventing a snap, a schema, or a SKU:

1. **08:00 snap** is named, dated, and is the only scheduled balance read. Numbers match File-1 0/0 unless a **later day’s** 08:00 says otherwise.
2. **No extra snap unless pay-proof.** Pay-proof = pasted sig + `getTransaction` / receipt on one of the two pay-tos + native USDC mint + amount. MCP session wallet is not proof.
3. **Canonical File-1** = operator header `date,usdc,eur_mid,eur_value,payer,memo,tx,notes` with opening `2026-08-27,0,,0.00,,,,opening 0/0` left intact. `#128` / `#91` headers are mapped or retired, not dual-SSOT.
4. **16:00 is not required.** No third look at 20:56.
5. **No spend** in STARTABLE. Helio, rebalance, send-to-test, Kraken USDC sale, ATA-rent buy are in BLOCKED.
6. **Exactly two pay-tos.** The strings above. Never a third.
7. **`#82` not scheduled** on the 27 Aug–2 Sep Rails lane.
8. Next inbound recipe matches STORE: public mid, `eur_value` not 1:1, tx after proof, payer, what sold. No paper-book merge. No FOD claim.

Until §3 (schema) and §8 (`#82` as the week) are locked out of the plan, Wallet PLAN stays **RED**. A3/§5 (no spend) and §12 (this review) are already GREEN. Do not spend that GREEN with an extra snap.

---

## STARTABLE / BLOCKED / WAIT (this judgment)

### STARTABLE

| Item | Note |
| --- | --- |
| Keep File-1 opening 0/0 | Valid. Not a fill. Not a filing. |
| 08:00 stamp as the day’s snap | Already taken / CEO-verified. Use it. Do not refresh it tonight. |
| Pay-proof confirm | Only if a sig is pasted. Then one RPC. |
| Refuse third-address / SIWE / spend PRs | Wallet yes/no on Rails. |
| Point Builder/Scout at EUR face | Strings stay off shop/mail. |

### BLOCKED

| Item | Until |
| --- | --- |
| Extra `wallet_balances` / extra RPC poll | A pasted pay-proof sig |
| Spend, swap, rebalance, perps, Helio, Kraken USDC out | Operator **yes** on a Wallet page that is not receive-only — not this week |
| Third pay-to / new key / SIWE / puller / CDP owner | Never on this board |
| Full IBAN / Revolut last-4 | Personal KYC + Compliance, not Wallet invention |
| Book 1 USDC = 1 EUR | Never |
| Merge dca-paper / invert-paper into File-1 | Never |
| Build `#82` SKUs | A later week + CEO Rails cell that names **one** idea |
| Replace operator File-1 with `#128` columns | Never without an operator yes that this review does not give |
| Scheduled 16:00 / 20:56 snap | Never; not required |

### WAIT

| Item | Waiting on |
| --- | --- |
| First real File-1 inbound row | Actual USDC on a listed pay-to **and** pay-proof RPC **and** operator `eur_mid` |
| Phantom MCP live read | Not required. Timeout was already the right WAIT. Do not send to test |
| EUR receive-log as shop card | Never; operator pack only, and only after hide-the-coin |
| Accountant / FOD table | Compliance, after KBO — File-1 is not that table |
| PLAN stage GREEN | A rewrite with **zero** RED and **zero** YELLOW on the gates above |

---

## This run

| Did | Did not |
| --- | --- |
| Read `#150` `02-adv-plan.md` as the PLAN artifact | Extra snap / Phantom `wallet_balances` / public RPC re-query |
| Scored PLAN gates from zero against `#82` / `#91` / `#94` / `#113` / `#128` / `#141` / `#149` | Spend, swap, rebalance, perps, Helio |
| Used 08:00 / File-1 0/0 as the stamp | Invent a third pay-to, inbound, IBAN, or seed |
| Set 16:00 = not required | Implement `#82`, edit shop HTML, mail, patch box CSV |
| Wrote this REVIEW | Treat advocate YELLOW as a GREEN pass |

**PLAN stage: RED (not GREEN).** Reviewer does not implement it.
