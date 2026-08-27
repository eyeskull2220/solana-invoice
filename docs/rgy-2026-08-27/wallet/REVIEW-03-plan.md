# REVIEW — Wallet PLAN lock (03)

**Seat:** REVIEWER
**Batch:** NEW (PLAN-lock only; old pack `#165` is context, not this grade)
**Date:** 2026-08-27
**Artifact:** PR [#171](https://github.com/eyeskull2220/solana-invoice/pull/171) `docs/rgy-2026-08-27/wallet/PLAN-lock.md`
**This file:** judgment only. **No implement.** No spend. No extra snap. No extra RPC.

Verdict for the stage is the worst row. **GREEN only if this file has no RED and no YELLOW.** It has neither.

| Gate | Score |
| --- | --- |
| 08:00 is the only scheduled snap | **GREEN** |
| No extra snap unless pay-proof | **GREEN** |
| Local File-1 SSOT (operator 8-col) | **GREEN** |
| 16:00 not required | **GREEN** |
| No spend in STARTABLE | **GREEN** |
| File-1 0/0 treated as valid | **GREEN** |
| Exactly two pay-tos | **GREEN** |
| `#82` not this week’s Rails plan | **GREEN** |
| No 1 USDC = 1 EUR | **GREEN** |
| No paper-book merge into File-1 | **GREEN** |
| Next inbound recipe on one ledger | **GREEN** |
| This review extra-snapped or spent | **GREEN** (neither) |
| **PLAN stage** | **GREEN** |

Old pack PR [#165](https://github.com/eyeskull2220/solana-invoice/pull/165) scored advocate `#150` plus the open corpus **RED**. This batch scores **this rewrite only**. A later Wallet agent follows `#171`. Not `#150`. Not `#128`. Not `#91`. Not `#82`.

---

## Locks for this batch (honoured)

| Lock | Meaning this run |
| --- | --- |
| **08:00 only snap** | Stamp is **2026-08-27 08:00** Europe/Brussels. SOL 0 / USDC ATA empty on `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3`. File-1 opening `2026-08-27,0,,0.00,,,,opening 0/0`. **This run did not re-query Phantom MCP, did not re-query public RPC, did not take a second snap.** |
| **No extra snap unless pay-proof** | No pasted signature was presented. No `getTransaction`. No `wallet_balances`. Extra RPC only after a pasted sig — none was. |
| **Local File-1 SSOT** | Operator box `/home/box/agent-data/projects/agent-treasury/receive-log.csv`. Header `date,usdc,eur_mid,eur_value,payer,memo,tx,notes`. Opening `2026-08-27,0,,0.00` stays. This VM cannot open the box; CEO-read bytes in PR [#141](https://github.com/eyeskull2220/solana-invoice/pull/141) are the stamp. Git `#128` `FILE-1.csv` is **EXAMPLE, never imported**. Kit `#91` is **not File-1**. |
| **No 16:00 required** | 16:00 weekday RPC is **not** a ritual. Skip unless a pay-proof arrived after 08:00. |
| **No spend** | No send, swap, rebalance, perps, Helio, Kraken USDC out, ATA-rent buy, “test” transfer. |
| **Pay-tos (exactly two)** | Solana `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3`. Base `0x9eb954b567ef3616424a6e1bf42c63724930aa54`. Never a third. No IBAN. No seeds. |
| **`#82` cite-only** | Not this week. Do not implement. |

Mints (not pay-tos): Solana USDC `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v`. Base USDC `0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913`.

---

## What was judged (this file, not a CODE audit)

PLAN means: the written intent that would tell a later Wallet agent what to start. Scored from zero against **this file**:

| Source | Role this batch |
| --- | --- |
| PR [#171](https://github.com/eyeskull2220/solana-invoice/pull/171) `PLAN-lock.md` | **The artifact.** Rewrite that claims to close `#165`. |
| PR [#165](https://github.com/eyeskull2220/solana-invoice/pull/165) `REVIEW-02-plan.md` | Prior RED pack. Context. Not this grade. |
| PR [#150](https://github.com/eyeskull2220/solana-invoice/pull/150) `02-adv-plan.md` | Advocate PLAN. YELLOW. Not the page a later agent follows. |
| PR [#141](https://github.com/eyeskull2220/solana-invoice/pull/141) File-1 after-fix | Operator File-1 **GREEN** as a ledger artifact. Stamp for 0/0. |
| PR [#128](https://github.com/eyeskull2220/solana-invoice/pull/128) `FILE-1.csv` + `WALLET-FIX.md` | EXAMPLE docs. Wrong columns. Must stay never-imported. |
| PR [#91](https://github.com/eyeskull2220/solana-invoice/pull/91) `tools/eur-receive-log/` | Kit. Not File-1. Must stay import/export-blocked. |
| PR [#82](https://github.com/eyeskull2220/solana-invoice/pull/82) `docs/ideas-wallet-ultra.md` | Cite only. Must not be this week’s build order. |
| PR [#113](https://github.com/eyeskull2220/solana-invoice/pull/113) CEO Rails | Receive-only week. Watch, not five SKUs. |
| PR [#94](https://github.com/eyeskull2220/solana-invoice/pull/94) | Same Solana treasury. Not a second address. |
| `main` `config.js` / README | Solana treasury + mint only. Base string is **not** on `main`. Shop leftover, not a third treasury. |

No Phantom `wallet_balances`. No public RPC re-query. No Helio. No Kraken USDC sale. No shop HTML. No mail.

`#171` does not grade itself GREEN. This file does.

---

## Closed from `#165` (not copied as this grade)

| `#165` gate | Was | Why this file closes it |
| --- | --- | --- |
| Local File-1 SSOT | **RED** | Operator 8-col is the only SSOT. `#128` EXAMPLE never imported. `#91` kit, no import/export. |
| `#82` not this week | **RED** | Cite only. Not scheduled. Five ideas stay “Cite only.” This page does not name one. |
| 08:00 only scheduled snap | **YELLOW** | `#128` “replace the stamp” is killed. Do not refresh tonight. |
| No extra snap unless pay-proof | **YELLOW** | Extra RPC only after a pasted sig. MCP session wallet is not proof. |
| Exactly two pay-tos | **YELLOW** | Overlays stay on `#82`. Not STARTABLE here. Never a third. No IBAN. |
| Next inbound on one ledger | **YELLOW** | Append only to operator File-1. Not git `#128`. Not through kit `#91`. |

Leftover open PRs `#128` / `#91` / `#82` still exist as git objects. They do **not** un-GREEN this page. A later agent that follows those pages instead of `#171` is off-plan.

---

## Scores

### 1. 08:00 is the only scheduled snap — **GREEN**

**Notes.** This batch’s lock: one scheduled balance read = **08:00**. Numbers match File-1 0/0. A second look tonight is fishing.

`#171` names stamp **2026-08-27 08:00** Europe/Brussels, SOL **0** / USDC ATA **empty** on `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3`, File-1 0/0 the same calendar day. **Do not refresh it tonight.** No 16:00. No 20:56. Ultra Wallet’s 20:56 0/0 is not this PLAN’s stamp.

`#165` YELLOW was `#128` “If a later Wallet seat gets a live read, replace the stamp with that read.” `#171` kills that sentence. Keep 08:00 0/0 until a **later day’s** 08:00 says otherwise, or until a real inbound is appended after pay-proof (a ledger row, not a second stamp).

**Fix-if-not-green.** — (closed as a gate). Do not replace the 08:00 stamp. Do not retry `wallet_balances` until a pasted sig exists.

### 2. No extra snap unless pay-proof — **GREEN**

**Notes.** Pay-proof = pasted signature that then **must** be confirmed with one `getTransaction` / Base receipt against one of the two pay-tos, the native USDC mint on that chain, and the claimed amount. Failed `meta.err`, wrong mint, wrong owner, or RPC miss is **not** inbound.

No pay-proof was presented to this run. `#171` STARTABLE “Pay-proof confirm” is **only if a sig is pasted. Then one RPC.** BLOCKED: extra `wallet_balances` / extra RPC poll / “replace the stamp” until a pasted pay-proof sig.

Not pay-proof (named on the page): explorer screenshots, Phantom UI, MCP session balances, “DeskCrew ticket if USDC ≥ 0.06,” a later live `wallet_balances` to replace the stamp.

Timeout → WAIT. Phantom MCP `wallet_balances` timeout is already the right WAIT. That phrase is locked by the BLOCKED extra-poll row; it is not a license to poll until non-zero.

**Fix-if-not-green.** — (closed as a gate). Same as §1. Do not snap to “see.”

### 3. Local File-1 SSOT — **GREEN**

**Notes.** User lock: **operator `receive-log.csv` is SSOT.** Columns `date,usdc,eur_mid,eur_value,payer,memo,tx,notes`. Opening `2026-08-27,0,,0.00` stays.

`#171` names canonical File-1 as the operator box path and the 8-col header. Opening row left intact:

```
2026-08-27,0,,0.00,,,,opening 0/0
```

Empty `eur_mid` on that zero row is valid (`#141`). `eur_value=0.00` is zero-of-zero, **not** 1 USDC = 1 EUR.

`#165` RED was three headers still claiming to be the inbound ledger. This file maps them and forbids dual-SSOT:

| Artifact | Header | This PLAN |
| --- | --- | --- |
| **Operator File-1** (canonical) | `date,usdc,eur_mid,eur_value,payer,memo,tx,notes` | Only SSOT. Opening 0/0 stays. |
| PR `#91` kit CSV | `date,usdc,eur_mid,memo,tx,notes` | Kit, not File-1. No import/export. |
| PR `#128` git FILE-1 | `date_brussels,usdc_in,eur_note,solana_sig,payer,what_sold,offerte_id` | EXAMPLE docs. Never imported. |

Exact exclusions on the page: do not import operator File-1 into `eur-receive-log.html` (0/0 would be skipped); do not export kit CSV over the box (drops `payer` / `eur_value`, truncates `tx` to last-6); do not shrink operator File-1 to six columns; do not treat kit `tools/eur-receive-log/receive-log.csv` as the sales ledger; do not merge the three headers into one super-header; do not append live inbound to git `#128`; do not invent a second opening row in git.

`#91` `parseAmount` would skip 0/0. That is why import is banned, not a reason to patch the box from this review.

**Fix-if-not-green.** — (closed as a gate). Canonical File-1 = operator `receive-log.csv` only.

### 4. 16:00 not required — **GREEN**

**Notes.** This batch: **no 16:00 required.** `#171`: weekday 16:00 RPC is **not** a ritual. Quiet-if-zero does not make a second look free. Skip unless a pasted sig arrived after 08:00 — and even then the call is pay-proof confirm, not a balance poll. No third look at 20:56.

**Fix-if-not-green.** — (closed as a gate). Do not add 16:00 back as a scheduled snap.

### 5. No spend in STARTABLE — **GREEN**

**Notes.** `#171` STARTABLE is keep 0/0, use the 08:00 stamp, pay-proof confirm if a sig is pasted, refuse third-address / SIWE / spend PRs, point Builder/Scout at EUR face, cite `#82`. None of those is send, swap, rebalance, perps, Helio, Kraken USDC out, ATA-rent buy, or “tiny USDC to ourselves so File-1 has a tx.”

BLOCKED until operator **yes** on a Wallet page that is not receive-only — **not this week**. File-1 has **no outbound column**. Do not add one.

Revolut remains denied until Personal KYC (Compliance). No full IBAN. No last-4.

**Fix-if-not-green.** — (closed as a gate). Do not spend this GREEN.

### 6. File-1 0/0 treated as valid — **GREEN**

**Notes.** STORE / `#141`: **0/0 is a valid first row.** Not a fill. Not a filing. Empty `eur_mid` on a zero row is valid. Missing inbound stays missing.

`#171` STARTABLE “Keep File-1 opening 0/0.” Do not invent the row to make a recipe look used. Scar: kit `#91` HTML still fights the opening row. That is a kit defect, designed out of this PLAN, not a reason to invent inbound.

**Fix-if-not-green.** — (closed as a gate). Leave the opening row intact.

### 7. Exactly two pay-tos — **GREEN**

**Notes.** The lock is the two strings. This file repeats only:

- Solana `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3`
- Base `0x9eb954b567ef3616424a6e1bf42c63724930aa54`

Mints are labeled **not** a pay-to. `#94` uses the same Solana string. `main` `config.js` is Solana-only (shop leftover, not a third treasury).

`#165` YELLOW was `#82` overlays still on that page (Helio embedded wallet, x402 CDP EOA, puller key, `subscriptionOwner`). `#171` leaves those overlays **on `#82`**. They are **not STARTABLE here**. A later agent “continuing Wallet ultra” does not ship Idea 2/4 “just for the facilitator.” BLOCKED: third pay-to / new key / SIWE / puller / CDP owner — **never on this board**.

A Phantom MCP session address, a Solana Pay `reference`, a facilitator gas key, a CDP wallet, a Helio email-embedded wallet, an explorer “token account,” or leftover shop HTML is **not** a treasury.

**No IBAN.** No full IBAN. No Revolut last-4. Do not stuff either wallet string into Peppol `PayeeFinancialAccount` / PaymentMeans. `#82` Idea 5 already forbids that; this PLAN does not implement Idea 5.

**No seeds.** No mnemonic, no private key, no `CDP_WALLET_SECRET`.

**Fix-if-not-green.** — (closed as a gate). Never a third.

### 8. `#82` not this week’s Rails plan — **GREEN**

**Notes.** CEO `#113` Rails lane (27 Aug–2 Sep), quoted on the page: receive-only, confirm address unchanged, EUR receive-log as **operator pack** not a shop card, idle unless a receive happened, refuse third address / SIWE. That is **watch**. It is not “ship dual-chain 490 / x402 990 / DeskCrew 790 / retainer 490 / Peppol 1490.”

`#165` RED was that the open ultra page still reads as a build order (Idea 1 now). `#171` table:

| `#82` idea | Status this week |
| --- | --- |
| 1 Dual-chain USDC invoice desk | Cite only |
| 2 x402 seller door | Cite only |
| 3 DeskCrew-class agent door | Cite only |
| 4 Recurring USDC retainer (push) | Cite only |
| 5 Belgian Peppol dual-rail | Cite only |

`#82` **suggested build order starts at Idea 1 now.** That sentence is not a Wallet STARTABLE. Builder already failed one-kit unlocks on the shop. Wallet does not get a pass.

Cite (do not schedule, do not build). Build `#82` only on a **later week** plus a CEO Rails cell that names **one** idea. **This page does not name one.** STARTABLE “Cite `#82`” is research, not a build ticket.

D2 “EUR receive-log as operator pack” stays CEO watch. Aligning kit `#91` is **not** this PLAN’s patch. Import/export remains NEVER.

**Fix-if-not-green.** — (closed as a gate). Do not implement `#82` from this review.

### 9. No 1 USDC = 1 EUR — **GREEN**

**Notes.** Never book 1 USDC = 1 EUR. File-1 opening `eur_value=0.00` on `usdc=0` is zero-of-zero, not a peg. Do not fetch ECB into the ledger from a Wallet seat. Operator pastes `eur_mid` on a **real** inbound. Not on the 0/0 row. `#128` `eur_note` is explicitly not FX; do not treat it as a mid.

**Fix-if-not-green.** — (closed as a gate).

### 10. No paper-book merge into File-1 — **GREEN**

**Notes.** File-1 is inbound USDC to the two pay-tos. Coder invert-paper / dca-paper fills are not sales. Invert gate is Coder + CEO, not Wallet. `#171` BLOCKED: merge dca-paper / invert-paper into File-1 — **never**. File-1 is not a FOD table.

**Fix-if-not-green.** — (closed as a gate).

### 11. Next inbound recipe on one ledger — **GREEN**

**Notes.** STORE next inbound: public `eur_mid`, `eur_value` (not 1:1), `tx` after `getTransaction` pay-proof, `payer`, what sold. That sentence only fits the **operator** header (`eur_value` exists there).

`#165` YELLOW was “log it in FILE-1” without naming which FILE-1. `#171` “Next inbound (one ledger)” appends **one new row** to **operator** File-1 only, after all of: actual USDC on one of the two pay-tos, pasted sig, one confirm RPC, operator-pasted public `eur_mid`, `eur_value` from that mid × `usdc`, full `tx` (not kit last-6), `payer` and what sold in `memo`.

Do **not** append that row to git `#128` FILE-1.csv. Do **not** import `#128` EXAMPLE zeros. Do **not** run it through kit `#91` first. Leave the 0/0 opening row intact. Missing inbound stays missing.

**Fix-if-not-green.** — (closed as a gate).

### 12. This review extra-snapped or spent — **GREEN**

**Notes.** No Phantom MCP balance call. No public RPC re-query. No send. No Helio. No shop HTML. No mail. `#141` G5 chain corroboration was a **prior** batch; this batch does not repeat it. `#171` claimed it did not extra-snap; this review independently did not either.

---

## RED

None on this artifact.

## YELLOW

None on this artifact.

---

## What is already true (does not un-GREEN this page)

These are scars so a later agent does not “fix” the wrong thing:

- Operator File-1 0/0 is valid (`#141`). Do not invent inbound.
- Two pay-to strings are frozen. Do not add a third “for completeness.”
- `#128` remains an open EXAMPLE stub with the wrong columns. Do not import it. Do not merge it over the box.
- `#91` may stay an unmerged operator pack. Aligning it is not this review’s patch. Do not import/export across it.
- `#82` remains research behind the shop face. Cite only. Do not schedule it this week.
- Shop face still prints USDC (`main` catalog / `#91` 49 USDC card). Wallet’s job this week is **reject**, not a new pay page.
- Copying this GREEN into an extra `wallet_balances` tonight would spend it.

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
| Follow `#171` as the PLAN | Not `#150`. Not `#128`. Not `#91`. Not `#82`. |

### BLOCKED

| Item | Until |
| --- | --- |
| Extra `wallet_balances` / extra RPC poll / “replace the stamp” | A pasted pay-proof sig |
| Spend, swap, rebalance, perps, Helio, Kraken USDC out | Operator **yes** on a Wallet page that is not receive-only — not this week |
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
| Scheduled 16:00 / 20:56 snap | Never; not required |

### WAIT

| Item | Waiting on |
| --- | --- |
| First real File-1 inbound row | Actual USDC on a listed pay-to **and** pay-proof RPC **and** operator `eur_mid` |
| Phantom MCP live read | Not required. Timeout was already the right WAIT. Do not send to test |
| EUR receive-log as shop card | Never; operator pack only, and only after hide-the-coin |
| Accountant / FOD table | Compliance, after KBO — File-1 is not that table |
| `#82` as a Rails cell | A later week + CEO naming **one** idea |

---

## This run

| Did | Did not |
| --- | --- |
| Read `#171` `PLAN-lock.md` as the PLAN artifact | Extra snap / Phantom `wallet_balances` / public RPC re-query |
| Scored PLAN gates from zero against this file | Spend, swap, rebalance, perps, Helio |
| Used 08:00 / File-1 0/0 as the stamp | Invent a third pay-to, inbound, IBAN, or seed |
| Set 16:00 = not required | Implement `#82`, edit shop HTML, mail, patch box CSV |
| Wrote this REVIEW | Import `#128`, import/export `#91`, treat leftover open PRs as this grade |

**PLAN stage: GREEN.** Reviewer does not implement it. No shop HTML. No snap.
