# REVIEW-06 — PLAN lock invert-wf (PR 207)

**Seat:** REVIEWER (adversarial, Coder PLAN only). **Different reviewer from the PLAN author of [PR #207](https://github.com/eyeskull2220/solana-invoice/pull/207).** Start from zero.
**Date:** 2026-08-27
**Stamp:** VOORBEELD · paper / simulated · not FACTUUR · not INVOICE · not live-trade advice
**Artifact scored:** [PR #207](https://github.com/eyeskull2220/solana-invoice/pull/207) `docs/rgy-2026-08-27/coder/PLAN-lock-wf.md` (sha `368960a`, 679 lines, **one markdown file**, no CODE)
**Priors read:** [PR #203](https://github.com/eyeskull2220/solana-invoice/pull/203) `REVIEW-05-plan-wf.md` (RED on #196); [PR #196](https://github.com/eyeskull2220/solana-invoice/pull/196) `PLAN-invert-wf-2023.md` (retired arming table)
**HEAD cited by the PLAN:** `2170952` (leftover `main` at write; matches this review’s `origin/main`)

**This file is judgment only.** It does not implement. It does not place paper or live orders. It does not reseal `c9689f5d`. It does not reset `invert-paper` or `dca-paper`. It does not patch Surge. It does not send mail. It does not invent a KBO. It does not start CODE. It does not merge #207. It does not edit the PLAN.

GREEN for this stage only if **this PLAN lock file** has **no red and no yellow**. World-state (live `invert-paper` still NOT MET, fill 1) is recorded below and is **not** this grade. Slogans are not a pass. The **recipe CODE would follow** is.

---

## Verdict: **GREEN**

#203 R1–R3 and Y1–Y4 are **designed out in the operational table**, not restated as slogans next to a ladder. #196’s “pair each buy rung below close” / “other lots may fill the same bar” / `on_bar` “refresh unfilled buys from new rails” is **gone**. This lock’s table is one invert pair, hard EUR 200 skip, grind fingerprint fails the run, named venue, derived empty bars, buy `Lo` only after sell `Hi`.

Do **not** start CODE from this review. Do **not** start CODE from #196. Do **not** start CODE from #207 (docs only). CODE is a **later** PR after this GREEN, still paper, still not the gate. Do **not** merge #196 (retired ladder). This review does not merge #207.

| Probe | Score |
| --- | --- |
| Named book `invert-wf-2023` EUR 10000 · not the fund gate · `is_fund_gate: false` | **GREEN** |
| `invert-paper` fill 1 stays · no reseal `c9689f5d` · no `dca-paper` reset | **GREEN** |
| 15m bar-close · no lookahead · rails from prior 96 bars (exclude `i`) | **GREEN** |
| Invert: those two prices swap jobs · re-arm filled price only on opposite fill · no naked short · **no ladder** · default `MAX_RESTING_LIMITS = 1` · PAPER-00028 extra **only if named** · `Hi` = 24h H | **GREEN** (prose **and** arming table) |
| Clip EUR 200 **hard** · skip leftover cash · not 100% equity · not whole-book deploy · fees 0.26% primary + 0.40 / 0.80 shadow | **GREEN** |
| Combined = one sequential 10000 book, not the sum of year slices | **GREEN** |
| Grind fingerprint FAILS the run · 9097 and invert-v2 day0 7923 are warnings, not scores | **GREEN** |
| Venue labeled `BINANCE-VISION-XRPEUR` or later `KRAKEN-TRADES` / `KRAKEN-OHLCVT` · not Bitstamp as named score | **GREEN** |
| Synthesized empty bars `derived: true` · clock only · no fills | **GREEN** |
| Dual-touch skip · touch at `P` · armed `t` eligible `t+1` · close-model fails · no future high · REST OHLC 720-cap is a stop | **GREEN** |
| Still paper · no keys · no orders · VOORBEELD · no second journal domain · operator is not the freelancer | **GREEN** |
| Would a CODE seat following **only** this lock still emit fill-every-rung / 100% equity / 9097 grind? | **No** — table forbids it; fail codes kill it if CODE does it anyway |
| **PLAN stage** | **GREEN** |

**Promotion stays RED** on live `invert-paper` (fill **1**, gate NOT MET). This review does not convert that. A pretty 2023–2026 curve from a later CODE PR would not convert it either.

---

## ADVERSARIAL (first)

A PLAN that can ship is a page a later CODE seat could follow **without** reprinting fill-every-rung, 100% equity, leftover-cash sizing, adjacent-fib fee mill, unlabeled Bitstamp, close-model, future high, or 14-pair revival — and without turning a research book into the fund gate. #203 already proved slogans can sit on top of a ladder. This review scores the **table**, not the header.

### A0 — Machine (held; not this grade)

SovereignForge is **one Belgian income machine**. Operator is not the freelancer. Still paper.

| Object | Held |
| --- | --- |
| **`invert-paper`** | **Fund gate.** Fill **1** `PAPER-00029` @ **1.24496** stays. TP `PAPER-00030` @ **1.26778** resting. `PAPER-00028` open. Gate **NOT MET**. |
| **`invert-wf-2023`** | 15m walk-forward from 2023. **Not** the gate. Named book EUR 10000. |
| **9097-fill** | Fill-every-rung **close-model** on `BINANCE-VISION-XRPEUR`: 9097 / −99.99% / end €1. **Not invert.** Warning. |
| **invert-v2 day0** | **FAIL (−41%, 7923 fills).** Not invert. Not this book. Not the gate. |
| **invert-v2-1LIMIT** | **FAIL (−15.2%, maxDD 15.5%, 2779 fills, max concurrent limits 1).** Not invert. Not this book. Not the gate. Not the 9097 grind family. |
| Lab clip | `sha256:c9689f5d7d583320e724900b0ce4ef68193878c880d11939badd1dd59016e390` — cite, **do not reseal**. |
| `dca-paper` | Five BTCUSD slices stay held. **No reset.** |

None of 9097 / 7923 / 1LIMIT is this book. None is the fund gate. No keys. No orders. No shop HTML. No journal republish.

### A1 — Did the arming table actually change, or did #207 restated #203?

#196 §4.4 (retired), the recipe CODE would have implemented:

> Candidate buy rungs = fib set strictly **below** bar `i-1` close
> **Pair each buy rung `E`** with a TP `T` = the **next higher** unique rung
> Other lots may fill the same bar
> `on_bar`: “Evaluate fills … **then refresh unfilled buys from new rails.**”

That is fill-every-rung (`2bfb1b68`) plus a sliding ladder. #203 R1. Slogan “this book does not” was false.

#207 §4 (this lock), the recipe CODE would implement:

```text
MAX_RESTING_LIMITS     = 1
PAPER_00028_EXTRA      = named only
MAX_OPEN_BUY_LOTS      = 1 + (1 if run names extra=true else 0)
```

| Inventory | Armed | Not armed |
| --- | --- | --- |
| Flat | **one** buy LIMIT at `Lo` | every other buy; any sell |
| Optional extra, **only if named** | at most **one** additional lower buy | a third buy; pair each remaining rung; **14 pairs** |
| Long | sell `Hi` for that qty; named extra may stay | re-arm `Lo`; pyramid; sell `Lo`; buy `Hi` breakout |

`on_bar`: “Evaluate fills on this closed bar. **Do not refresh a ladder of unfilled buys.**”

`Hi` = **24h rail `H[i]`**, not next retracement. Fail `FILL_EVERY_RUNG` / `LADDER_ARM` if CODE arms or fills more buy prices than the cap.

That is a **different table**. Not a restated slogan. R1 closed.

### A2 — 9097 grind family: fail, or a scorecard row?

#203 R2: clip text does not kill a ladder; 9097 fingerprint must **fail the run**.

#207 §7: a slice or combined that prints any of (thousands of fills **and** fees ≈ capital **and** end ~€1) / (end ≤ €100 with fills ≥ 1000) / (return ≤ −50% with fills ≥ 1000) / (fill at bar **close**) / (one bar buys > `MAX_OPEN_BUY_LOTS`) / (calendar year ≥ 5000 fills without a named extra that still respects §4.1) writes `GRIND_FINGERPRINT` / `CLOSE_MODEL` / `FILL_EVERY_RUNG` and **must not** publish a GREEN-looking SCORECARD. 9097 and invert-v2 day0 7923 are cited as **warnings**, not this book’s score.

With the §4 cap, a CODE seat following the table cannot emit 9097/7923-class ladders without tripping `LADDER_ARM` / `FILL_EVERY_RUNG` first. R2 closed.

**1LIMIT cousin (held, not a remaining hole):** invert-v2-1LIMIT (−15.2%, maxDD 15.5%, 2779 fills, max concurrent 1) would **not** trip this grind kill (return is not ≤ −50%, end is not ~€1, year fills < 5000). That is correct. 1LIMIT is a **one-pair** FAIL vs 8% DD, not fee-compounded ruin. This lock does not cite 1LIMIT by name; it also does not claim one-pair invert PASSES. Combined `max_dd_vs_8pct` remains a **flag**, not promotion. A later CODE print in that family is a scorecard row with `over`, not invert-as-GREEN and not this book. See Notes.

### A3 — Clip hard, or `min(200, cash)` in a trench coat?

#196: `qty = CLIP_QUOTE_EUR / limit_price` next to “never buy more than cash” and a cash cap that permitted `floor(cash/200)` lots and leftover `min(200, cash)`. #203 Y1.

#207 §5:

```text
CLIP_QUOTE_EUR = 200
fee = CLIP_QUOTE_EUR * 0.0026
if cash < CLIP_QUOTE_EUR + fee: skip   # do not shrink, do not "use the rest"
qty = CLIP_QUOTE_EUR / limit_price     # not cash/price, not equity/price
```

**Never:** 100% equity; whole book as `floor(cash/200)` lots; leftover-cash `min(200, cash)`; a fill whose quote is not 200. Fail `FULL_EQUITY_SIZE`. Lot count is already 1 (or 2 if extra named). Y1 closed.

### A4 — Adjacent-fib fee mill vs rail H

#196 paired each `E` with **next higher unique rung** (often inside the 0.52% round-trip). Live fill 1 TP is **24h H** (`PAPER-00030` @ 1.26778), not a neighbour retracement.

#207: `Hi` = 24h rail `H[i]`. Adjacent-fib TP **forbidden**. If `Hi <= Lo`, **skip** — do not drop to the next fib as a substitute TP. `test_tp_is_rail_h.py` required. Closed.

### A5 — Dual-touch, armed t, close-model, future high, REST OHLC

| Attack | #196 | #207 lock | This review |
| --- | --- | --- | --- |
| Same-bar both-sides as a round-trip | one fill **per lot**; **other lots may fill** the same bar (ladder sweep) | **Fill neither** if a bar could touch both `Lo` and `Hi` of the same lot. `DUAL_TOUCH_SKIP`. Global fills ≤ armed lots (capped by §4.1) | Closed |
| Armed `t` fills on `t` | newly armed opposite skips; arming vs eval timing loose | Resting at open of `b` only if armed at close of `u` with `u < b`. Eligible from `t+1`. Never bar `t` | Closed |
| Fill at close / remaining cash | fill at **limit** (this part held) | Fill at **`P`**. A fill whose price is the bar **close** is `CLOSE_MODEL` and **fails** | Closed |
| Future high of the year as rails | rails `i-96..i-1` (clock held) | Same clock. Illegal: `H = max(high)` over the whole file / slice / year. `FUTURE_HIGH` / `LOOKAHEAD` | Closed |
| Page REST OHLC, claim 2023 | 720-cap named as stop | Same stop. `since` does not lift the cap | Closed |
| 14-pair revival | table **was** many pairs | “Fourteen pairs is forbidden.” `LADDER_ARM` | Closed |
| Combined = sum of slices | sequential combined; `test_combined_not_sum.py` | Kept. Combined = one cash pile, one inventory, **one invert pair** | Closed |
| `is_fund_gate: true` | false | false. Combined maxDD vs 8% is a **flag**, not promotion | Closed |

### A6 — Venue / derived / naked short

#203 Y2: no `venue` field; Vision-on-disk unnamed; Bitstamp not banned. Y3: synthesized empties unlabeled. Y4: “swap jobs” vs geometric Lo/Hi (naive short).

#207 §3: `venue` **required**. Allowed named scores **only** `BINANCE-VISION-XRPEUR` | `KRAKEN-TRADES` | `KRAKEN-OHLCVT`. **Not** `BITSTAMP-XRPEUR` / Bitstamp / Coinbase / XRPUSD. Unlabelled mix = `DATA_BAD`. Synthesized rows `derived: true`; rails may use them for **clock**; fills forbidden; do not write them into a file labeled as Kraken OHLCVT verbatim.

#207 §4: after sell `Hi`, next armed order is **buy `Lo` only** — never sell `Lo`, never sell `Hi` with 0 XRP, never buy `Hi`. Naive swap that would rest a sell while flat is **discarded**; `NAKED_SHORT` fails the run. Y2–Y4 closed.

Venue **strings** differ from #203 D4 (`BINANCE-VISION-XRPEUR+KRAKEN-TAIL` / `KRAKEN-OHLCVT-XRPEUR`). This lock’s strings are the ones the current bar named (`BINANCE-VISION-XRPEUR` or later `KRAKEN-TRADES` / `KRAKEN-OHLCVT`). Kraken tail on Vision history keeps the **named score** as Vision. That is a label, not an unlabeled mix. Not a yellow.

### A7 — R3: would this page start CODE from #196?

#207 is **one markdown file**. Unchecked CODE tasks sit under “later PR, not this one.” Sequence: this lock → different reviewer (this file) → CODE later. **Do not start CODE from this PR. Do not start CODE from #196.** Scoring this page GREEN is **not** permission to start CODE from #207, from this review, or from #196.

R3 closed. This GREEN is a PLAN-stage pass, not a CODE licence and not a merge of #207.

### A8 — Desk cheats (would a later agent promote / reseal / reset / go live?)

| Cheat | PLAN lock | Reviewer |
| --- | --- | --- |
| Treat combined PASS as fund gate | Gate stays `invert-paper` until CEO names a change. `is_fund_gate: false` | Holds |
| Add clip fills into `c9689f5d` (20+n) | Cite full sha256; this book has its own scorecard | Holds |
| Reset `invert-paper` to match the replay | Fill 1 `PAPER-00029` @ 1.24496 stays; 00030 / 00028 stay | Holds |
| Reset `dca-paper` | Five BTCUSD slices stay held | Holds |
| Page REST OHLC and claim 2023 | 720-cap named as **stop** | Holds |
| Naked short after sell-TP | Flat cash; buy-back only; `NAKED_SHORT` fails the run | Holds (table + fail) |
| Sum four slice returns | Combined replays bars itself; `test_combined_not_sum.py` | Holds |
| New Surge / live CLI / keys / shop HTML / journal republish | Forbidden | Holds |
| Operator-as-freelancer / invented KBO | Operator is not the freelancer. `KBO/BTW: nog niet toegekend.` | Holds |
| **Fill every fib / 14 pairs / 100% book / leftover cash / close-model / Bitstamp named score** | Table + fail codes | **Holds** (this was the #196 fail) |

---

## What was judged (from zero)

| Source | What it is |
| --- | --- |
| PR #207 `PLAN-lock-wf.md` (sha `368960a`, 679 lines, 1 file) | The artifact. Docs only. |
| PR #203 `REVIEW-05-plan-wf.md` | Prior RED. Design-out D1–D6. This review checks **design-out**, not copy-paste of D-slogans. |
| PR #196 `PLAN-invert-wf-2023.md` | Retired arming table. Still open. **Do not merge. Do not start CODE from it.** |
| This prompt | Score #207 only. GREEN iff no red and no yellow. Adversarial. Keep every #196 GREEN slogan if still true. |
| Machine held | Gate NOT MET. Fill 1 stays. 9097 / 7923 / 1LIMIT are not this book. No reseal. No DCA reset. |
| This run | No `kraken` binary used. No keys. No orders. No Phantom. Kraken MCP not used. PLAN not edited. #207 not merged. |

`main` still has no Coder RGY tree. The PLAN exists only on #207. This review does not merge it.

---

## RED

None.

#203 R1 (pair-each-fib / fill-every-rung), R2 (9097 grind family as a publishable score), R3 (CODE from #196) do not survive on this page.

---

## YELLOW

None.

#203 Y1 (clip not hard vs 100% deploy), Y2 (venue / Bitstamp), Y3 (unlabeled synthesized bars), Y4 (naive short after “swap jobs”) do not survive on this page.

---

## GREEN (kept from #196 — still true; do not bargain away)

### G1 — Named book, not the gate

`invert-wf-2023`, EUR **10000**, XRPEUR 15m, 2023-01-01 00:00 Europe/Brussels → last **fully closed** 15m bar. **Not** the fund gate until CEO says. Gate remains `invert-paper` only (return > 0 after fees **and** ≥ 8 prints **and** maxDD ≤ 8%). `is_fund_gate: false`. Combined maxDD vs 8% is a **flag**, not promotion.

### G2 — invert-paper fill 1 stays

`PAPER-00029` buy 160.64773 @ **1.24496** = fill **1**. Resting `PAPER-00030` @ 1.26778 is not a fill. Open `PAPER-00028` @ 1.23084 is not a fill. Do not flatten, cancel, or “clean” that book. Do not add 20+1.

### G3 — No reseal · no `dca-paper` reset

Cite `sha256:c9689f5d7d583320e724900b0ce4ef68193878c880d11939badd1dd59016e390`. Lab clip (20 fills · +0.681154% · maxDD 0.890854% · 2026-08-18 21:00 → 2026-08-26 08:00 BXL) ≠ this walk-forward. Five BTCUSD slices on `dca-paper` stay held. Retired hashes stay retired **in name and in the arming table** (`2bfb1b68` fill-every-rung · `9056f296` · `094513`).

### G4 — Clock: 15m bar-close, no lookahead, rails `i-96..i-1`

```text
H[i] = max(high[j] for j in i-96 .. i-1)
L[i] = min(low[j]  for j in i-96 .. i-1)
```

Do not include bar `i` in its own rails. Do not read `i+1`. Warmup 96 bars seed rails only (no fills, no fees). `DATA_GAP` rather than invent a future swing. Fill price = **limit** inside `[low, high]`, not the close. Newly armed opposite **skips this bar**. Brussels tz via `zoneinfo`. Start of book UTC: `2022-12-31 23:00:00Z`. The 9097 run was a **close-model**; this clock is the correct one.

### G5 — Invert job rule · no naked short

After **any** fill: the **other** of those two prices becomes the working order; **re-arm the filled price only on the opposite fill**. Spot: no naked short. After sell-TP: flat cash; next entry is **buy-back**. Same-bar re-arm forbidden (`SAME_BAR_REARM`). **#196 had this prose and a ladder table. This lock has the prose and a one-pair table.**

### G6 — Fees 0.26 primary + 0.40 / 0.80 shadows · clip number 200

Primary hits cash. Shadows are parallel ledgers on the same fills. Round-trip primary = two 0.26% events. Journal check: EUR 200 @ 1.24496 → primary fee **0.52**. The **number** 200 stays. The **hardness** is now §5 (was Y1; now GREEN).

### G7 — Combined is sequential, not the sum

Year slices 2023 / 2024 / 2025 / 2026-to-now may run **in parallel**, each flat EUR 10000 at slice open (diagnostics). **Combined** is one cash pile, one inventory, **one invert pair**, 2023-01-01 → now. CODE may not define combined as `sum(slice returns)` or `mean(slice maxDD)`. `test_combined_not_sum.py` stays.

### G8 — Still paper · hygiene · VOORBEELD

Autonomy **level 2**. No `kraken order`. No keys. No Phantom against `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3` or Base `0x9eb954b567ef3616424a6e1bf42c63724930aa54`. No new Surge host. Scorecards in git as markdown/JSON. VOORBEELD. Fail the run on `TOUCHED_INVERT_PAPER` / `TOUCHED_DCA_PAPER`. No shop HTML. XRPEUR only. **Operator is not the freelancer.**

---

## #203 holes — designed out vs restated

| #203 | Required design-out | On this PLAN lock | Restated or designed out? |
| --- | --- | --- | --- |
| **R1** | ONE invert pair; at most one resting limit; optional PAPER-00028 extra **only if named** | §4.1–4.3 constants, operational table, `LADDER_ARM` / `FILL_EVERY_RUNG`; `on_bar` must **not** refresh a ladder | **Designed out** |
| **R2** | Grind fingerprint **fails** the run; 9097 and 7923 are warnings, not scores | §7 fail codes; warnings named; grind SCORECARD without fail code is a **stop** | **Designed out** |
| **R3** | No CODE from #196 | §10–§11; this PR is markdown only | **Designed out** |
| **Y1** | Clip **hard** EUR 200; skip leftover cash; not 100% equity; not whole-book deploy | §5 skip; `FULL_EQUITY_SIZE`; never `min(200, cash)` / `floor(cash/200)` | **Designed out** |
| **Y2** | Venue labeled `BINANCE-VISION-XRPEUR` or later `KRAKEN-TRADES` / `KRAKEN-OHLCVT`; not Bitstamp as named score | §3 + scorecard `venue` required; `BITSTAMP-XRPEUR` → `DATA_BAD` | **Designed out** |
| **Y3** | Synthesized empty bars marked derived; clock only; no fills | `derived: true`; no fill in bucket; not written as verbatim OHLCVT | **Designed out** |
| **Y4** | After sell `Hi`, next armed order is buy `Lo` only; no naked short | §4.3 sentence + `NAKED_SHORT` + `test_no_naked_short.py` | **Designed out** |

---

## Notes (not yellow)

These are held facts and CODE-seat cautions. They do **not** reopen a red or yellow on this PLAN page.

1. **invert-v2-1LIMIT** (−15.2%, maxDD 15.5%, 2779 fills, max concurrent limits 1) is **not cited** on the lock page. It is **not this book** and **not the fund gate**. The grind kill is tuned for 9097/7923-class ruin, not for an honest one-pair FAIL vs 8% DD. A later CODE print of that cousin is a scorecard with `max_dd_vs_8pct: over`, not a licence to publish grind-as-invert and not a reason to reject this PLAN.

2. **§6.3 N = 8 swing objects** are a lookahead guard **if** CODE uses swing objects. They are **not** a second TP definition. `Hi` stays 24h rail `H`. CODE must not replace rail H with an N=8 confirmed swing high.

3. **#196 remains open** with the retired pair-each-fib table. This lock says teammates read **this** file. Do **not** merge #196. Do **not** start CODE from #196. Conflict of two PLAN pages is process, not a hole in this recipe.

4. **No min-edge vs 0.52%** when `Lo` is a shallow retracement and `Hi` is still rail H on a quiet 24h. Adjacent-fib TP (ticks apart) is the mill that was banned. Live invert-paper does not skip on fee-width. Not a #203 hole.

5. **GREEN of this PLAN is not:** permission to start CODE from this review or from #207; a merge of #207; a fund-gate conversion; a reseal; a `dca-paper` or `invert-paper` reset; paper or live orders; shop/journal HTML; an invented KBO.

---

## Bar for this GREEN (this PLAN lock)

This page has **no red and no yellow**, including:

1. Named book `invert-wf-2023` EUR 10000. **Not** the fund gate. `invert-paper` fill **1** stays. No reseal `c9689f5d`. No `dca-paper` reset.
2. 15m bar-close. No lookahead. Rails from prior **96** bars, not bar `i`. Causal swing. No future high.
3. Invert: after fill, swap jobs of **those two** prices; re-arm filled price **only** on opposite fill. **No naked short.** **No ladder.** Default `MAX_RESTING_LIMITS = 1`. Optional PAPER-00028 extra **only if named**. `Hi` = 24h H.
4. Clip **EUR 200** hard. Fees **0.26%** primary + **0.40 / 0.80** shadow. No leftover-cash sizing. No 100% equity. Not the whole book deployed.
5. Same-bar both-sides = skip, not a round-trip. Touch at `P`. Armed `t` eligible `t+1`.
6. Combined = one sequential book, not the sum of slices.
7. Close-model / fill-every-rung / 9097 / 7923 grind fingerprint **fails the run**. Do not publish as invert.
8. `venue` required. Named score: **`BINANCE-VISION-XRPEUR`** or later **`KRAKEN-TRADES` / `KRAKEN-OHLCVT`**. **Not Bitstamp as the named score.**
9. Still paper. No keys. No orders. VOORBEELD. No second journal domain. Operator is not the freelancer.

**PLAN stage: GREEN.** Next seat, if any, is a **later CODE PR** — not this review, not #196, not #207. Still paper. Still not the gate.

---

## This run

| Did | Did not |
| --- | --- |
| Read #207 PLAN lock from zero (679 lines) against #203 RED and #196 retired table | Implement replay, fetch ZIP, place orders |
| Scored the **arming table**, not the header slogans | Reseal `c9689f5d` |
| Checked R1–R3 / Y1–Y4 as design-out vs restatement | Reset `invert-paper` or `dca-paper` |
| Attacked rail-H vs adjacent-fib, dual-touch, t/t+1, combined, leftover cash, 14-pair, close-model, future high, REST OHLC, 1LIMIT cousin | Patch Surge / shop HTML / start CODE / merge #207 / edit the PLAN |
| Wrote this review on a new branch from `main` | Mail, KBO, Phantom spend, keys in git |

**PLAN stage: GREEN.** Still paper. `invert-wf-2023` is not the fund gate. invert-paper fill 1 stays. Do not reseal `c9689f5d`. Do not reset `dca-paper`. 9097-fill was fill-every-rung, not invert. invert-v2 day0 still FAIL (−41%, 7923 fills). invert-v2-1LIMIT still FAIL (−15.2%, 2779 fills). Operator is not the freelancer. Do not start CODE from #196. Do not start CODE from this review.

---

## Re-check (copy/paste)

```bash
# This review must exist and must green only if the lock table (not slogans) closed #203:
rg -n 'Verdict|Designed out|YELLOW|RED|MAX_RESTING_LIMITS|pair each|BITSTAMP|CLIP_QUOTE_EUR|GRIND_FINGERPRINT' \
  docs/rgy-2026-08-27/coder/REVIEW-06-plan-lock-wf.md

# PLAN under review (other branch — do not merge from this PR, do not edit it):
# https://github.com/eyeskull2220/solana-invoice/pull/207

# Retired ladder (do not start CODE from it, do not merge it):
# https://github.com/eyeskull2220/solana-invoice/pull/196

# Never from this seat:
# kraken paper reset --workspace invert-paper
# kraken paper reset --workspace dca-paper
# kraken order …
```

End of REVIEW-06. Still paper. No orders. No keys. **GREEN.**
