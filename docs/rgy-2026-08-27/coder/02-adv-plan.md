# 02 — Adversarial plan review (Coder)

**Seat:** RGY 02 (adv-plan) · Coder  
**Lens:** ADVERSARIAL **first**, then RED / YELLOW / GREEN.  
**Date:** 2026-08-27  
**Stamp:** VOORBEELD · paper / simulated · not FACTUUR · not INVOICE · not live-trade advice  
**This file does not implement.** It does not place paper or live orders. It does not reseal. It does not reset `dca-paper`. It does not send mail. It does not invent a KBO.

Coder plans are treated as a **bad layout** until the named locks survive attack. Research that this plan sits on: [PR #132](https://github.com/eyeskull2220/solana-invoice/pull/132) `docs/rgy-2026-08-27/coder/01-adv-research.md`.

**Verdict: GREEN on the four locks. RED on promotion.** Still paper. Gate on `invert-paper` only — **NOT MET**.

| Lock this plan endorses | Score |
| --- | --- |
| Leave `c9689f5d` (do not reseal) | **GREEN** |
| `dca-paper` stay (do not reset) | **GREEN** |
| Gate on `invert-paper` only | **GREEN** |
| Still paper | **GREEN** |
| Reseal temptation / reset / wrong-book gate / live | **RED** |
| Walk-forward funding / live invert | **RED** |

---

## ADVERSARIAL (first)

A Coder “plan” that can ship is a page a later agent could follow **without** turning a lab clip, a hold book, or a stale journal into live money. Attack the temptations that would do that.

### A1 — Reseal temptation vs leave `c9689f5d`

The sealed lab clip already **looks** like a fund memo:

- Name `fib-grid-invert-xrpeur-15m`
- Window 2026-08-18 21:00 → 2026-08-26 08:00 Europe/Brussels
- Spot: 20 fills · +0.681154% · maxDD 0.890854% · PASS vs  
  `sha256:c9689f5d7d583320e724900b0ce4ef68193878c880d11939badd1dd59016e390`

A bad plan reseals. Ways it already happened in this desk’s history:

1. **Restamp the PASS as today’s walk-forward.** Add 20+1 (`PAPER-00029`) and call it 21 fills. Gate language is new prints on `invert-paper` **after** the seal, not clip arithmetic.
2. **Rotate the hash** so the journal looks newer after a prettier rerun, a mixed sleeve, or a reset.
3. **Revive a retired hash.** `2bfb1b68` fill-every-rung · `9056f296` entry-waits-TP · `094513` arming-only (**99 fills PASS** on that old hash is not live). The temptation is the pattern: old hash passed → keep using it or reseal a new one.
4. **Reseal to “fix” Surge.** Live journal still prints **0 fills** while the operator book is fill 1. Resealing does not ping `PAPER-00029`. It launders the clip.

**Leave `c9689f5d`:** cite it. Do not rewrite, rotate, or rehash. Lab clip is **not** funding proof. Sleeve FAIL on the same lock (6 fills, −2.729078%, maxDD 5.326685%) is **not** a reason to reseal either.

### A2 — Reset `dca-paper` vs stay

`dca-paper` is five held BTCUSD slices (PAPER-00002…00010 @ 78900.6, equity ~9995.71, fees already bit). A bad plan resets it because:

- fills 5 < 8 looks ugly next to a gate
- USD grandfather vs EUR invert looks “wrong”
- fib/grid recipes want a clean `paper init`
- converting BTC to EUR would “unify” books

Reset, sell, or convert is a **stop**. Fib → `fib-paper`. Grid → `grid-paper`. Invert stays `invert-paper`. Official `recipe-launch-grid-bot` `paper init` is banned on `dca-paper`. Stay = read-only `status` / `history` / `balance` on that workspace. Not a sixth slice. Not the gate.

### A3 — Gate on the wrong book vs `invert-paper` only

A bad plan shops for a green row:

| Wrong book | Why a later agent would pick it | Why it is not the gate |
| --- | --- | --- |
| Lab clip `c9689f5d` | 20 fills, +0.68%, maxDD 0.89% already PASS | Sealed lab, not walk-forward |
| `dca-paper` | 5 fills, “almost 8,” long-term hold | USD hold; not invert; return not > 0 after fees |
| 3x sleeve | Same invert story, futures | FAIL fills<8; separate book; mixing PnL is journal fraud |
| Leftover `fib-paper` BTCUSD | Invert-adjacent name | Not the named EUR 10000 book |
| CODER.md scoreboard as a **menu** | Lists `dca-paper` in a Gate column | Inventory, not a pick-list. Promote **one** named book: `invert-paper` |

**Gate (all three, same book, `invert-paper` only):**

1. Return > 0 after fees (0.26% taker + fee shadow; not mark-to-market).
2. **≥ 8 fills** (`PAPER-*` **prints**. Resting limits are not fills).
3. maxDD ≤ 8% from peak equity on **that** book.

Live walk-forward now: **fill 1** `PAPER-00029` buy XRPEUR @ **1.24496**. `PAPER-00030` sell LIMIT TP @ **1.26778** — not a fill. `PAPER-00028` open @ **1.23084** — not a fill. **NOT MET.**

Do not count 00030/00028. Do not add extra clips or extra pairs to rush 8. Do not flatten 00030/00028 “to clean the book.” Re-arm only on the opposite fill of the invert pair.

### A4 — Live vs still paper

A bad plan goes live because:

- the lab clip already PASS
- Kraken MCP is dead so “we’ll CLI it”
- 10k paper capital is misread as a SEPA deposit
- live XRPEUR tagged 1.26778 (exact TP) so “the paper TP would have filled”
- autonomy skip from level 2 → 3 without CEO **and** gate

**Still paper.** Autonomy **level 2**. No `kraken order` / `kraken futures order`. No API keys in git, HTML, or this plan. No Phantom spend from treasury. No `--validate` then live. Paper-to-live (10–25% size, dead-man, human yes) is a **later** page **after** the invert-paper gate is green. This week it is not.

---

## What was scored (from zero)

| Source | What it is |
| --- | --- |
| This prompt | Score reseal temptation vs leave `c9689f5d`; `dca-paper` stay; gate on invert-paper only; still paper. |
| PR #132 `01-adv-research.md` | Adversarial research: gate **RED** (1 fill); Surge stale at 0; locks GREEN. |
| PR #118 `docs/ultra-seats/CODER.md` | Seat contract: inventory, STARTABLE (fee shadow, honest journal, fill ping), WAIT (live / extra pairs / extra clips). Scoreboard still lists `dca-paper` under Gate — attack A3. |
| Live https://dca-paper-journal.surge.sh/ | Invert-gate page. Prints **NOT MET (0 fills)**. LIVE LOCK `c9689f5d` shown, not resealed. Walk-forward named as `invert-paper` only. |
| PR #110 `dca-paper-journal/` | Older VOORBEELD DCA checklist in git. Not the live invert scoreboard. |
| PR #113 CEO | Invert gate closed until all three numbers + human yes + healthy connector. Do not reset `dca-paper`. |
| Kraken skills | `kraken-paper-strategy` (no slippage/partials); `kraken-paper-to-live` (no silent live); `kraken-autonomy-levels` (level 2 = paper). |
| This run | Kraken MCP **error**. No `kraken` binary. No `/workspace/paper-recipes/` in this git tree. |

---

## Scorecard (RGY)

| # | Attack / lock | Score |
| --- | --- | --- |
| A1a | Reseal temptation (`c9689f5d` as funding proof / new hash / 20+1) | **RED** |
| A1b | Leave `c9689f5d` (cite, do not rotate) | **GREEN** |
| A2a | Reset / convert / recycle `dca-paper` | **RED** |
| A2b | `dca-paper` stay (hold five BTC slices) | **GREEN** |
| A3a | Gate on lab clip / DCA / sleeve / leftover fib | **RED** |
| A3b | Gate on `invert-paper` only | **GREEN** |
| A4a | Live / CLI-while-MCP-dead / 10k as deposit | **RED** |
| A4b | Still paper (autonomy 2) | **GREEN** |
| B1 | Count 00030 / 00028 as fills | **RED** if a plan does; **GREEN** if count stays 1 |
| B2 | Surge journal stale at 0 | **YELLOW** (plan must ping, not reseal) |
| B3 | Sleeve FAIL recorded, excluded from gate | **GREEN** |
| B4 | Extra pairs / extra clips to rush 8 | **RED** as plan; WAIT as lock |
| B5 | CODER.md Gate column listing `dca-paper` | **YELLOW** (inventory leak; not a second gate) |
| B6 | Fake KBO / FACTUUR / mail / Phantom bot | **GREEN** (out of this plan) |

**Overall: GREEN on locks. RED on promotion.** Do not implement live from this file. Do not reseal. Do not reset `dca-paper`.

---

## A1 — Reseal temptation vs leave `c9689f5d`

**Reseal temptation — RED.** The clip is the cleanest number on the desk (20 fills, +0.68%, maxDD < 1%). That is exactly why it is sealed. A plan that restamps it, adds 00029 into the 20, or rotates the hash to match a journal republish is promoting a lab window as walk-forward. Retired `094513` (99 fills PASS, not live) proves the desk already learned this the hard way.

**Leave `c9689f5d` — GREEN.** Coder may *read* and *cite* the full sha256. Coder may not reseal, rewrite, or rescore the lock. Sleeve FAIL on the same seal stays FAIL. Next work is fill-ping on `invert-paper`, not a new hash.

---

## A2 — `dca-paper` stay

**Reset — RED.** Init/reset/buy/sell/cancel/convert-to-EUR on `dca-paper` destroys the hold ledger and invites fib/grid to land on the wrong workspace.

**Stay — GREEN.** Five slices held. Grandfathered BTCUSD. Not the EUR gate. Not a sixth clip. Recipes that need a new book use a **new** workspace name. Plan: leave running.

---

## A3 — Gate on `invert-paper` only

**Wrong-book gate — RED.** Lab PASS, DCA “almost,” sleeve FAIL-as-story, leftover fib, or “any book that eventually hits 8” are all promotion cheats.

**Invert-paper only — GREEN as the lock, RED as the current score.** Named book: `invert-paper`, EUR 10000, XRPEUR 15m invert (full fib rungs; after any fill swap those two prices; spot no naked short). Current walk-forward: **1 print**. Return-after-fees unknown until a round-trip prints **and** both fees + shadow are subtracted. maxDD unsampled. Hypothetical net on 00030 @ 1.26778 (~+1.31% after two 0.26% takers, zero slippage) is **not** a fill and would still be 2 < 8. Do not write it into the scoreboard.

If 00030 or 00028 prints: journal as fill 2, fee-shadow, re-read the three conjuncts, **stop**. Still paper.

---

## A4 — Still paper

**Live — RED.** Connector unhealthy. n=1. Journal lying about 0. No qty/maxDD path in this git tree. Paper engine does not model slippage or partials. CEO + paper-to-live both require human yes **after** the gate.

**Still paper — GREEN.** STARTABLE from #118, still not implementation in *this* file:

1. **Fee shadow** on every `PAPER-*` print (engine 0.26% + conservative extra + round-trip).
2. **Honest journal** — VOORBEELD; print fill **1**, open 00028, resting 00030, DCA hold, sleeve FAIL, lab clip cited not resealed. Do not trust Surge at 0 as the score.
3. **Fill ping** — only when a print happens. Not when a live candle tags 1.26778.

WAIT: live, extra pairs, extra clips, fib/grid clips until CEO names that book.

---

## B — Adjacent scores

### B1 Fills honesty — GREEN only at 1

Plan language must say **1**, not 0 (Surge), not 3 (resting+open), not 21 (clip+00029), not 5 (`dca-paper`).

### B2 Stale journal — YELLOW

https://dca-paper-journal.surge.sh/ still: `NOT MET (0 fills on invert-paper)`. Git #110 is the older DCA page. #118 already has fill 1. A later Coder **journal** ticket may ping 00029. This plan does not patch HTML. Reseal/reset is not the ping.

### B3 Sleeve — GREEN (excluded)

FAIL fills<8. Not the fund gate. Never mix into spot journals. Kill: flatten + cancel-all on kill file, 10% sleeve DD, or leverage > 3x. Do not reopen at 5x.

### B4 Extra clips / pairs — RED if planned, WAIT if locked

Allowlist fork (journal seven EUR pairs vs CODER.md wider list) is not a shopping list. XRPEUR is on both. Expanding while n=1 cheats the gate.

### B5 CODER.md Gate column — YELLOW

Keep the inventory table. Do not let a later agent promote `dca-paper` because it has a Gate cell. One named funding book: `invert-paper`.

### B6 Identity / mail / Phantom — GREEN

No fake KBO. No FACTUUR title. No mail. No Phantom bot against `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3` or Base `0x9eb954b567ef3616424a6e1bf42c63724930aa54`. Sales-USDC is not Kraken float.

---

## NOTES

1. **Do not implement from this plan.** No paper order, no live order, no journal HTML patch, no shop edit, no reseal, no `dca-paper` reset. Sibling 01 (#132) is research. This 02 is the lock page. Later Coder work is fill-ping / fee-shadow copy — still paper.

2. **Head-to-head (this prompt).** Reseal temptation **loses**. Leave `c9689f5d` **wins**. `dca-paper` stay **wins**. Gate on invert-paper only **wins**. Still paper **wins**. Promotion **loses**.

3. **Three surfaces, one book.** Operator/Coder: fill 1. Surge: 0. Git #110: DCA checklist. Plan source of truth for the gate is the **operator invert-paper prints**, not Surge, not the lab clip.

4. **Paper is not proof.** Instant full fills, slippage 0, Starter taker only, no queue. One XRPEUR print is a story. Gate is ≥ 8 shadowed prints on `invert-paper` with return > 0 after fees and maxDD ≤ 8%.

5. **Tax (not advice).** Paper is not a tax event. Phantom sales-USDC = beroepsinkomen. Live Kraken later = apart handelsdossier. No invented FIFO. No CAP from paper JSON.

6. **PII.** No personal mailbox, no IBAN, no invented KBO. Operator: natural person, Geel. **KBO/BTW: nog niet toegekend.**

---

## Bar for GREEN (plan only)

This **plan** (the locks) is already GREEN if a later Coder page repeats, verbatim in spirit:

1. **Do not reseal** `sha256:c9689f5d7d583320e724900b0ce4ef68193878c880d11939badd1dd59016e390`. Cite only. Lab clip ≠ walk-forward. Retired hashes stay retired.
2. **Do not reset `dca-paper`.** Five BTCUSD slices stay held. New recipes → new workspaces.
3. **Fund gate = `invert-paper` only.** All three conjuncts on that book. Sleeve / DCA / fib leftover / lab clip are not the gate.
4. **Count prints, not rests.** 00029 = 1. 00030 and 00028 do not count until they print.
5. **Still paper** until CEO says live **and** the invert-paper gate is green **and** Kraken connector is healthy. Autonomy 2. No keys in git.
6. **Honest journal** may ping 00029; it may not “fix” Surge by reseal or reset.
7. **No extra pairs, no extra clips, no memecoins, no Phantom bot, no FACTUUR.**

**Promotion stays RED** until invert-paper itself is GREEN on the three conjuncts. That is a later scoreboard, not this file.

---

End. Still paper. No reseal. No `dca-paper` reset. Gate on `invert-paper` only. No live. No mail. No KBO.
