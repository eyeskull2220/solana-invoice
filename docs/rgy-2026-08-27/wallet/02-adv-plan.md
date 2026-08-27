# Adversarial plan review — Wallet

**Seat:** RGY 02 (adv-plan)  
**Date:** 2026-08-27  
**Verdict:** **YELLOW**  
**This file does not implement.** It does not spend. It does not take an extra snap. It does not invent a third pay-to, an IBAN, a seed, or an inbound.

Wallet plans are treated as a **bad spend / extra-snap / third-address queue** until proven empty. This review is not a rewrite of `#82` rail SKUs. It attacks whether a Wallet agent could still **send, snap, or book** from those plans after File-1’s opening **0/0**.

Operator locks for this score: **08:00 snap. File-1. No spend. No extra snap unless pay-proof.**

---

## What was scored (from zero)

| Source | What it is |
| --- | --- |
| **08:00 snap** (this file’s only balance stamp) | Operator File-1 opening + CEO-verified public RPC: **SOL 0**, **USDC ATA empty** on `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3`. **0 inbound.** Not a fill. Not a filing. **This run did not re-query Phantom MCP, did not re-query RPC, did not take a second snap.** |
| File-1 (operator box; this run cannot read the box) | `/home/box/agent-data/projects/agent-treasury/receive-log.csv`. Header: `date,usdc,eur_mid,eur_value,payer,memo,tx,notes`. Opening row CEO already read: `2026-08-27,0,,0.00,,,,opening 0/0`. **STORE lock: 0/0 is a valid first row.** |
| PR #128 `FILE-1.csv` + `WALLET-FIX.md` | FIX for “no File-1 in git.” **Different columns.** EXAMPLE `usdc_in=0`. Invites a later live `wallet_balances` to “replace the stamp.” |
| PR #91 `tools/eur-receive-log/` | Operator pack. Header `date,usdc,eur_mid,memo,tx,notes` (**no** `eur_value`, **no** `payer`). HTML **refuses** `usdc ≤ 0` and empty `eur_mid`. Catalog card still priced **49 USDC**. |
| PR #82 `docs/ideas-wallet-ultra.md` | Five rail offers at **490–1490 USDC**. Pins the two pay-tos. Optional Helio overlay. x402 / DeskCrew door / push retainer / Peppol annex. Not this week’s board. |
| PR #94 Solana Pay URLs | Wallet-drafted `solana:` URLs to the **same** Solana treasury. Not Helio. Not a second address. |
| PR #113 CEO page | Phantom **receive-only**. Rails never contain send. EUR receive-log is an **operator pack**, not a shop card. Refuse third address / SIWE. |
| `main` README / `config.js` / pay page | Solana treasury + mint only. Base string is **not** on `main`. USDC-on-face is Builder, not a Wallet spend. |

No Phantom `wallet_balances`. No `wallet_rebalance`. No send. No Helio. No Kraken USDC sale. No IBAN.

---

## 08:00 snap + File-1 (locked facts)

These are the **only** numbers this PLAN may use. They are not a reason to snap again.

| Field | Value |
| --- | --- |
| Stamp | **2026-08-27 08:00** (Europe/Brussels ops check). File-1 opening is the same calendar day. |
| Solana pay-to | `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3` |
| Solana USDC mint | `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v` |
| Base pay-to | `0x9eb954b567ef3616424a6e1bf42c63724930aa54` |
| Base USDC (mint, **not** a third pay-to) | `0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913` |
| SOL | **0** |
| USDC (Solana ATA) | **empty / 0** |
| File-1 `usdc` | **0** |
| File-1 `eur_mid` | **empty** (valid on a zero row) |
| File-1 `eur_value` | **0.00** (zero of zero; **not** “1 USDC = 1 EUR”) |
| Inbound txs | **none** |
| Extra snap this run | **none** (no pay-proof was presented) |

**Never invent a third.** A Phantom MCP session address, a Solana Pay `reference`, a facilitator gas key, a CDP wallet, a Helio email-embedded wallet, or an explorer “token account” is not a treasury.

**Pay-proof** (the only legal extra snap): a pasted signature that then **must** be confirmed with `getTransaction` / Base receipt against one of the two pay-tos, the native USDC mint on that chain, and the claimed amount. Failed `meta.err`, wrong mint, wrong owner, or RPC miss is **not** inbound. Do not book it. Do not snap “just to see.”

---

## Scorecard

| # | Attack | Score |
| --- | --- | --- |
| A1 | Extra snap without pay-proof | **YELLOW** |
| A2 | Treat File-1 **0/0** as broken / invent inbound | **GREEN** (lock holds; #91 HTML still fights it) |
| A3 | Spend / send-to-test / Helio / rebalance / Kraken USDC sale | **GREEN** |
| A4 | Third address / SIWE / puller / CDP / Helio embedded | **YELLOW** |
| A5 | File-1 schema drift (operator box vs #91 vs #128) | **RED** |
| A6 | Book **1 USDC = 1 EUR** | **GREEN** |
| A7 | Merge invert-paper / dca-paper into File-1 | **GREEN** |
| A8 | Treasury string as shop face or Peppol IBAN | **YELLOW** |
| A9 | Skip **08:00** because 16:00 quiet-if-zero | **YELLOW** |
| A10 | Ship `#82` rail SKUs as this week’s Wallet plan | **RED** |
| B1 | Two pay-tos frozen | **GREEN** |
| B2 | Seeds / full IBAN in the plan | **GREEN** |
| B3 | This review spends or extra-snaps | **GREEN** (neither) |

**Overall: YELLOW.** Do not spend. Do not extra-snap. Do not implement `#82`. Do not replace operator File-1 with `#128`’s columns. The PLAN is **startable as a watch**: 08:00 stamp + File-1 0/0 + pay-proof-only RPC. It is **not** a hard lock that a later agent cannot walk around with “just one `wallet_balances` to replace the stamp.”

---

## A1 — Extra snap without pay-proof — YELLOW

Named attack: if the PLAN still licenses a **second balance read** after the 08:00 / File-1 0/0 stamp, it is not receive-only discipline. It is fishing.

Evidence:

- Operator lock: **no extra snap unless pay-proof.**
- This run honours it: no Phantom MCP balance call, no public RPC re-query.
- PR #128: “If a later Wallet seat gets a live read, replace the stamp with that read.” That **is** an extra snap with no pasted signature.
- Ultra Wallet seat (same day) already planned weekday **16:00 RPC quiet-if-zero** *and* “08:00 still required.” A 16:00 RPC after a 08:00 zero is a second snap. Quiet-if-zero does not make it free.
- Phantom MCP `wallet_balances` is the **session wallet**, not the two published treasuries. Using it as the 08:00 stamp **and** as a later “confirm” is two errors: extra snap, and possibly a **third address**.

Design-out: **one** scheduled snap = **08:00** (public RPC on the two pay-tos, or the operator File-1 opening). Next RPC is **only** `getTransaction` / receipt after a pasted sig. Timeout ≠ retry with a different provider “until it looks non-zero.” If MCP times out, **WAIT** and keep the 08:00 0/0. Do not send to test.

---

## A2 — File-1 0/0 treated as broken — GREEN (with a #91 scar)

STORE lock: **0/0 is a valid first row.** Not a fill. Not a filing. Empty `eur_mid` on a zero row is valid. Missing inbound stays missing.

#128 EXAMPLE `usdc_in=0` agrees on the number. CEO File-1 opening agrees.

Scar: PR #91’s HTML `parseAmount` **rejects** `usdc ≤ 0` and **requires** `eur_mid`. Import of the operator 0/0 row would be **skipped**. A Wallet agent that “opens the pack to log today” will be pushed to invent a mid or skip the opening row. That is how 0/0 dies.

Design-out: operator File-1 is the ledger. The #91 pack is an **operator tool**, not the SSOT, and must not be the gate that deletes the opening row. Do not invent inbound to make the HTML happy.

---

## A3 — Spend / send-to-test — GREEN

CEO: receive-only. #113 miss §3.10. #82 bans perps, new keys, SIWE unless named as a blocker. #128: no spend column. This review: no send, no swap, no rebalance, no Helio, no sales USDC to Kraken.

A spend would look like: “tiny USDC to ourselves so File-1 has a tx,” “buy SOL for ATA rent,” “Helio Pay Link to see if it lands,” “rebalance dust.” **None of the plans scored here name that as STARTABLE.** Do not add it.

Revolut remains **denied** until Personal KYC (Compliance). No full IBAN. No last-4.

---

## A4 — Third address / SIWE / puller / CDP — YELLOW

The lock is GREEN. The **open ideas file is not**.

#82 correctly freezes the two strings, then still offers:

- Helio payout-wallet overlay (email signup = **embedded wallet** = third address; called out as blocked, still on the page as optional).
- x402 `payTo` via Dexter (allowed **if** `payTo` stays the two strings; CDP `createX402Server` default mints an EOA — blocked only if Wallet remembers).
- Solana Subscriptions **puller key** and Base CDP `subscriptionOwner` — blocked for automation, still documented as rails.

A later agent “continuing Wallet ultra” can ship Idea 2/4 and mint a key “just for the facilitator.” That is A4.

Design-out: `#82` is **research behind the shop face**, not this week’s plan. STARTABLE Wallet work is watch + File-1 + refuse PRs that add a third string or SIWE. Not a seller door.

---

## A5 — File-1 schema drift — RED

Three headers claim to be the inbound ledger:

| Artifact | Header | Opening row |
| --- | --- | --- |
| **Operator File-1** (canonical) | `date,usdc,eur_mid,eur_value,payer,memo,tx,notes` | `2026-08-27,0,,0.00,,,,opening 0/0` |
| PR #91 kit CSV | `date,usdc,eur_mid,memo,tx,notes` | header only |
| PR #128 git FILE-1 | `date_brussels,usdc_in,eur_note,solana_sig,payer,what_sold,offerte_id` | EXAMPLE zeros |

Next inbound (STORE): **public `eur_mid`, `eur_value`, `tx` after `getTransaction` pay-proof, `payer` + what sold.** Never book 1 USDC = 1 EUR. That sentence only fits the **operator** header (`eur_value` exists there). `#128` has `eur_note` (explicitly not FX). `#91` has `eur_mid` but no `eur_value` and stores **last-6** in `tx` (pay-proof needs the full sig at verify time; last-6 is PII-safe storage **after** proof).

A Wallet PLAN that says “log the next inbound in FILE-1” without naming **which** FILE-1 will split the books.

Design-out: **canonical File-1 = operator `receive-log.csv`.** Git `#128` is a RED-clearing stub with the wrong map; do not append real inbound there. `#91` may import **after** pay-proof, with operator-entered mid, last-6 in `tx`, and **must accept** the 0/0 opening (today it does not). Do not merge the three files into one “helpful” super-header.

---

## A6 — 1 USDC = 1 EUR — GREEN

STORE: never book 1 USDC = 1 EUR. File-1 opening `eur_value=0.00` on `usdc=0` is zero-of-zero, not a peg.

#91: no baked rate; empty mid → do not log a **positive** inbound. Compliance: EUR on receipt **after** KBO; File-1 is not a FOD table.

Do not fetch ECB into the ledger from this seat. Operator pastes `eur_mid` on a **real** inbound. Not on the 0/0 row.

---

## A7 — Kraken paper into File-1 — GREEN

STORE: never merge invert-paper / dca-paper. File-1 is **inbound USDC to the two pay-tos**. Coder paper fills are not sales. 3x sleeve FAIL is not a fund gate and is not a File-1 row.

No plan scored here copies paper equity `9995.71` into `usdc`. Keep it that way.

---

## A8 — Treasury on shop face / Peppol IBAN — YELLOW

Wallet owns the strings. Wallet does **not** print them on mails or the EUR shop. CEO miss §3.7 / §3.13.

Live `main` and Surge still lead with USDC. `#82` Idea 5 forbids stuffing the Solana string into `PayeeFinancialAccount`. `#91` catalog card still says **49 USDC**. `#128` correctly says shop stays EUR-first.

Yellow because: Wallet plans **refuse** the miss, but the face is still dirty, and kit PRs keep reprinting the Solana pay-to next to a USDC price. Wallet’s job this week is **reject**, not a new pay page.

---

## A9 — Skip 08:00 because quiet-if-zero — YELLOW

08:00 is **still required** when the stamp is already 0. That is the point of a morning check: confirm empty, file File-1, stop.

16:00 weekday RPC as “quiet-if-zero” is a second ritual. If 08:00 ran and File-1 is 0/0, 16:00 is an **extra snap** unless a pay-proof arrived after 08:00.

Design-out: **08:00 = the snap.** 16:00 = only if a sig was pasted since 08:00 (pay-proof confirm). No third look at 20:56. Ultra Wallet’s 20:56 0/0 is **not** this PLAN’s stamp and is not a reason to poll tonight.

---

## A10 — `#82` as this week’s Wallet plan — RED

CEO 7-day Rails lane: receive-only, confirm address unchanged, EUR receive-log as **operator pack**, refuse third address. Not “ship dual-chain 490 / x402 990 / DeskCrew 790 / retainer 490 / Peppol 1490.”

`#82` is the right *class* of later rail work and correctly bans new keys. Using it as the Wallet PLAN for 27 Aug–2 Sep is a one-kit unlock on the rail side: five SKUs, USDC prices, Helio in the text, x402 facilitator choices. Builder already failed that pattern on the shop. Wallet does not get a pass.

Design-out: `#82` stays cited, not scheduled. This week Wallet **watches**.

---

## B — Adjacent scores

### B1 Two pay-tos — GREEN

Solana `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3`. Base `0x9eb954b567ef3616424a6e1bf42c63724930aa54`. Every scored Wallet page repeats them. `#94` does not invent a second Solana. This review does not invent a third.

### B2 Seeds / full IBAN — GREEN

#128: no seeds, no full IBAN. #91: last-6 in `tx`. Revolut denied. Peppol PaymentMeans is not a wallet string.

### B3 This review — GREEN

No spend. No extra snap. No Helio. No mail. No shop HTML.

---

## NOTES

1. **0/0 is the plan, not the bug.** A Wallet agent that “fixes empty” will spend, snap, or invent. File-1 first row 0/0 is **done** for 2026-08-27.

2. **Pay-proof is a signature, not a vibe.** Explorer screenshots, Phantom UI, MCP session balances, and “DeskCrew ticket 239 if USDC ≥ 0.06” are not pay-proof. `getTransaction` (or Base receipt) against the published owner + native USDC mint + amount is.

3. **Schema drift is how inbound gets booked twice or never.** Operator File-1 vs git `#128` vs kit `#91` must not all receive the first real row.

4. **Session wallet ≠ treasury.** If Phantom MCP returns an address that is not one of the two pay-tos, that is a third address. Do not watch it. Do not log it.

5. **Do not implement from A5/A10 RED.** Next Wallet write after this file is either (a) a real inbound row on **operator** File-1 after pay-proof, or (b) a schema-lock page that names operator File-1 as SSOT. Not a seller door. Not a second snap.

---

## Design-outs (do these, or the PLAN stays YELLOW)

1. **08:00 snap is the stamp.** SOL 0 / USDC 0 / File-1 0/0 on 2026-08-27. Do not refresh it tonight.
2. **No extra snap unless pay-proof.** Pasted sig → one `getTransaction` / receipt. Timeout → WAIT. Not a retry storm.
3. **No spend.** No send, swap, rebalance, perps, Helio, Kraken USDC sale, “test” transfer, ATA-rent SOL buy.
4. **Canonical File-1 = operator `receive-log.csv`.** Columns `date,usdc,eur_mid,eur_value,payer,memo,tx,notes`. Opening 0/0 stays. Empty `eur_mid` on that row stays.
5. **`#128` is not SSOT.** Wrong header. Do not append live inbound there. Do not “replace the stamp” with a new MCP read.
6. **`#91` is the operator pack, not the ledger.** Do not require `eur_mid` on the zero row. Do not put the pack on the EUR shop face (it still says 49 USDC).
7. **`#82` is not this week.** Cite, do not build. No x402 door, no Helio overlay, no puller, no CDP owner.
8. **Next inbound row** needs: public `eur_mid`, `eur_value` (not 1:1), `tx` after pay-proof, `payer`, what sold. Never merge paper books. Not a FOD table.
9. **Refuse** PRs that add a third address, SIWE, or a wallet string in Peppol IBAN / shop/mail copy.
10. **Do not snap from RGY.** This file is the deliverable.

---

## STARTABLE / BLOCKED / WAIT

### STARTABLE

| Item | Note |
| --- | --- |
| Keep File-1 opening 0/0 | Valid. Not a fill. Not a filing. |
| 08:00 stamp as the day’s snap | Already taken / CEO-verified. Use it. |
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

### WAIT

| Item | Waiting on |
| --- | --- |
| First real File-1 inbound row | Actual USDC on a listed pay-to **and** pay-proof RPC **and** operator `eur_mid` |
| 16:00 RPC | A pay-proof since 08:00; else skip |
| Phantom MCP live read | Not required. Timeout was already the right WAIT. Do not send to test |
| EUR receive-log as shop card | Never; operator pack only, and only after hide-the-coin |
| Accountant / FOD table | Compliance, after KBO — File-1 is not that table |

---

## Bar for GREEN (plan only)

A later Wallet **plan** (not this file, not a spend) is GREEN only if it states, in one pass:

1. **08:00 snap** is named, dated, and is the only scheduled balance read. Numbers match File-1 0/0 unless a **later day’s** 08:00 says otherwise.
2. **No extra snap unless pay-proof.** Pay-proof = pasted sig + `getTransaction` / receipt on one of the two pay-tos + native USDC mint + amount. MCP session wallet is not proof.
3. **Canonical File-1** = operator header `date,usdc,eur_mid,eur_value,payer,memo,tx,notes` with opening `2026-08-27,0,,0.00,,,,opening 0/0` left intact. `#128` / `#91` headers are mapped or retired, not dual-SSOT.
4. **No spend** in STARTABLE. Helio, rebalance, send-to-test, Kraken USDC sale, ATA-rent buy are in BLOCKED.
5. **Exactly two pay-tos.** The strings above. Never a third.
6. **`#82` not scheduled** on the 27 Aug–2 Sep Rails lane.
7. Next inbound recipe matches STORE: public mid, `eur_value` not 1:1, tx after proof, payer, what sold. No paper-book merge. No FOD claim.

Until A5 (schema) and A10 (`#82` as the week) are locked out of the plan, Wallet PLAN stays **YELLOW**. A3 (no spend) and B3 (this review) are already GREEN. Do not spend that GREEN with an extra snap.

---

## What this run did / did not do

| Did | Did not |
| --- | --- |
| Wrote this adversarial PLAN | Extra snap / Phantom `wallet_balances` / public RPC re-query |
| Used 08:00 / File-1 0/0 as the stamp | Spend, swap, rebalance, perps |
| Named schema drift #91 vs #128 vs operator File-1 | Invent a third pay-to, inbound, IBAN, or seed |
| Set extra snap = pay-proof only | Implement `#82`, edit shop HTML, mail |

---

End. No implementation. No spend. No extra snap.
