# REVIEW-05 — PLAN invert-wf-2023 (PR 196)

**Seat:** REVIEWER (adversarial, Coder PLAN only). **New reviewer. Start from zero.**  
**Date:** 2026-08-27  
**Stamp:** VOORBEELD · paper / simulated · not FACTUUR · not INVOICE · not live-trade advice  
**Artifact:** [PR #196](https://github.com/eyeskull2220/solana-invoice/pull/196) `docs/rgy-2026-08-27/coder/PLAN-invert-wf-2023.md`  
**HEAD cited by the PLAN:** `2170952` (leftover `main` at write; matches this review’s `origin/main`)

**This file is judgment only.** It does not implement. It does not place paper or live orders. It does not reseal `c9689f5d`. It does not reset `invert-paper` or `dca-paper`. It does not patch Surge. It does not send mail. It does not invent a KBO. It does not start CODE.

GREEN for this stage only if **this PLAN file** has **no red and no yellow**. World-state (live `invert-paper` still NOT MET, fill 1) is recorded below and is **not** this grade.

---

## Verdict: **RED**

Do **not** start CODE from PR 196. Rewrite the PLAN. Re-review. Then CODE.

The lock *slogans* are mostly right. The **operational engine** in §4.4 would still run a **fill-every-rung ladder** that can deploy **100% of the EUR 10000 book** across fibs. That is the same family as the Coder close-model already printed on **`BINANCE-VISION-XRPEUR`**: **fills 9097 / −99.99% / end €1**. This PLAN names clip EUR 200 and “not 2bfb1b68,” then tells CODE to **pair each buy rung below close**. Slogan ≠ recipe. Recipe wins. Recipe is RED.

| Probe | Score |
| --- | --- |
| Named book `invert-wf-2023` EUR 10000 · not the fund gate | **GREEN** |
| `invert-paper` fill 1 stays · no reseal `c9689f5d` · no `dca-paper` reset | **GREEN** |
| 15m bar-close · no lookahead · rails from prior 96 bars (exclude `i`) | **GREEN** (clock) |
| Invert: those two prices swap jobs · re-arm filled price only on opposite fill · no naked short | **GREEN** as prose · **RED** as arming table |
| Clip EUR 200 per rung · fees 0.26% primary + 0.40 / 0.80 shadow | **GREEN** as numbers · **YELLOW** as size-cap (cash cap = 100% book) |
| Combined = one sequential 10000 book, not the sum of year slices | **GREEN** |
| Would this PLAN produce the 9097 / −99.99% / end €1 grind? | **RED** (fill-every-rung + full-book deploy). Clip text does **not** kill it. |
| Venue labeled · Vision+Kraken-tail **or** Kraken OHLCVT ZIP · not Bitstamp as the named score | **YELLOW** (missing `venue` field; Vision-on-disk unnamed; Bitstamp not banned as named score) |
| Still paper · no keys · no orders · VOORBEELD · no second journal domain | **GREEN** |
| **PLAN stage** | **RED** |

**Promotion stays RED** on live `invert-paper` (fill **1**). This review does not convert that. A pretty 2023–2026 curve from this PLAN would not convert it either.

---

## ADVERSARIAL (first)

A PLAN that can ship is a page a later CODE seat could follow **without** reprinting fill-every-rung, 100% equity, no-clip ruin — and without turning a research book into the fund gate.

### A0 — Close-model death already printed (this sitting’s warning)

Coder already printed a **close-model** score on **`BINANCE-VISION-XRPEUR`**:

| | |
| --- | --- |
| Fills | **9097** |
| Return | **−99.99%** |
| End | **€1** |
| Fingerprint | fill-every-rung · 100% equity · no clip · fill at close / full remaining cash |

That is not invert. That is fee-compounded ruin. `(1 - 0.0026)^9097` on full remaining notional is the €1 fingerprint. **Missing positions are recoverable; this curve is not a strategy.**

**Bar for this PLAN:** if a CODE agent following **only** PR 196 could still emit that fingerprint (or its clipped cousin: thousands of fills, fee-negative adjacent fibs, book emptied into the ladder), the PLAN is **not GREEN**.

### A1 — Fill-every-rung vs invert pair

Retired `2bfb1b68` filled every rung. The PLAN says this book **does not**. Then §4.4 **Arming**:

> Candidate buy rungs = fib set strictly **below** bar `i-1` close  
> **Pair each buy rung `E`** with a TP `T` = the **next higher** unique rung

That is a **full ladder**. Every unique tick below close becomes a lot. `on_bar` then **refreshes unfilled buys from new rails** every bar, so as 24h H/L slides, **new `E` prices appear forever**. “Do not arm a second lot at the same `E`” only blocks duplicates at one tick. It does not cap lots.

Live `invert-paper` is **not** that ladder. After fill 1:

| Id | Role | Price |
| --- | --- | --- |
| PAPER-00029 | FILL 1 · buy | **1.24496** |
| PAPER-00030 | Resting TP · sell LIMIT | **1.26778** (24h **H**, a rail) |
| PAPER-00028 | One extra open buy | **1.23084** |

Two prices in the working invert pair, plus **at most one** extra lower buy (00028). TP of the filled lot is **24h H**, not “next higher unique fib” (often a few ticks, **inside the 0.52% round-trip fee**).

Method pack (#199) locks the same invert as **at most one resting limit**. This PLAN’s operational table is the opposite: many lots, many fills per bar (one per lot), sells then buys.

**Same-bar rule in the PLAN:** at most one fill **per lot** per bar; **other lots may fill the same bar**. A wick that sweeps the fib set fills **the whole ladder**. That **is** fill-every-rung.

### A2 — 100% equity vs clip EUR 200

§4.3 writes:

```text
CLIP_QUOTE_EUR = 200
qty = CLIP_QUOTE_EUR / limit_price
```

That would have blocked the €1 close-model **if it were the only size rule**. It is not. Same section:

> Never buy more quote than `cash` after the primary fee haircut.

§4.4 cash cap:

> sum of working buy notionals + held cost basis + primary fees must stay ≤ cash

Together: a CODE seat may (1) size a lot at `min(200, cash)` — last lot eats the remainder; or (2) arm `floor(cash/200)` lots and **deploy the entire 10000**. Aggregate is **100% equity**. Per-rung clip without a **hard max lot count** is a ladder that uses the whole book.

The 9097 death needs **no clip + full remaining cash per fill**. This PLAN still allows **full remaining cash across fills**. Design it out: clip is 200, **never cash, never % of equity, never “use the rest.”** If `cash < 200 * (1 + 0.0026)`, **skip**. Do not shrink the clip. Do not raise it.

### A3 — Adjacent-fib TP is a fee mill

“Next higher unique rung” as TP makes round-trips whose gross is often **< 0.52%** (two primary fees). Chop then prints thousands of **losing** invert pairs. That is a slower grind than 100% equity, still a grind. Live pairing: buy Lo, sell **24h H**. Do not pair adjacent retracements as a round-trip.

### A4 — Venue unlabeled; Bitstamp must not be the named score

User lock for this review: data path **may** be **Vision + Kraken tail (already on disk)** **or** **Kraken OHLCVT ZIP**. **Label venue.** **Not Bitstamp as the named score.**

PLAN §3: source of record is **only** Kraken OHLCVT ZIP. Scorecard JSON has `pair: XRPEUR` and `data_sha256`. **No `venue` field.**

Holes:

1. On-disk **BINANCE-VISION-XRPEUR** (the 9097 tape) is unnamed. CODE may re-use it without labeling, or mix it with Kraken and call it Kraken.
2. Sibling research #198 already offers a **labeled `BITSTAMP-XRPEUR` fallback** because Bitstamp `step=900` pages from 2023. This PLAN never says the **named score is not Bitstamp**. A later CODE seat that “just needs 2023 bars” will take #198’s fallback.
3. Cross-venue unlabeled = the 9097 curve can be pasted onto a Kraken scorecard.

Kraken OHLCVT as *an* allowed path is fine. Exclusive + unlabeled is not.

### A5 — Would a later agent promote this book / reseal / reset / go live?

Attack the usual desk cheats against **this** page:

| Cheat | PLAN text | Reviewer |
| --- | --- | --- |
| Treat combined PASS as fund gate | Gate stays `invert-paper` until CEO names a change. `is_fund_gate: false` | Holds |
| Add clip fills into `c9689f5d` (20+n) | Cite full sha256; this book has its own scorecard | Holds |
| Reset `invert-paper` to match the replay | Fill 1 `PAPER-00029` @ 1.24496 stays; 00030 / 00028 stay | Holds |
| Reset `dca-paper` | Five BTCUSD slices stay held | Holds |
| Page REST OHLC and claim 2023 | 720-cap named as **stop** | Holds |
| Naked short after sell-TP | Flat cash; buy-back only; `NAKED_SHORT` fails the run | Holds (prose) |
| Sum four slice returns | Combined replays bars itself; test `test_combined_not_sum.py` | Holds |
| New Surge / live CLI / keys | Forbidden | Holds |
| **Fill every fib / 100% book / close-model** | Slogan forbids `2bfb1b68`; **table implements it** | **Fails** |

Locks on **books and paper** are GREEN. The **engine** is not.

---

## What was judged (from zero)

| Source | What it is |
| --- | --- |
| PR #196 `PLAN-invert-wf-2023.md` (sha `34937b8`, 504 lines) | The artifact. Docs only. |
| This prompt | Score that file. GREEN iff no red and no yellow. Design out the 9097 grind. Venue label. Not Bitstamp as named score. |
| Coder close-model (already printed) | **9097 / −99.99% / end €1** on **`BINANCE-VISION-XRPEUR`**. Warning, not a score to cite as invert. |
| Live invert-paper pattern | Fill 1 @ 1.24496 · TP 24h H 1.26778 · one extra buy 1.23084. Count = **1**. Gate NOT MET. |
| Lab clip | `sha256:c9689f5d7d583320e724900b0ce4ef68193878c880d11939badd1dd59016e390` — cite, do not reseal. Not this window. |
| PR #199 method pack | Invert = **at most one resting limit**; dual-touch skip; not a ladder. Used as a **contrast**, not as a stamp this PLAN inherited. |
| PR #197 / #198 data notes | Kraken REST OHLC cannot source 2023. OHLCVT ZIP or Vision+tail OK if labeled. Bitstamp pages 2023 — **must not be the named score**. |
| This run | No `kraken` binary. No keys. No orders. No `/workspace/paper-recipes/` in leftover `main`. Kraken MCP not used. |

`main` still has no Coder RGY tree. The PLAN exists only on #196. This review does not merge it.

---

## RED

### R1 — Operational arming is fill-every-rung (`2bfb1b68` in a trench coat)

§4.4 “Pair each buy rung” + “other lots may fill the same bar” + `on_bar` refresh from new rails **is** fill-every-rung. The sentence “Retired `2bfb1b68` filled every rung. This book does **not**.” is false given the table that follows. CODE will implement the table.

A 15m wick through the fib set fills every armed `Lo`. Over 2023–2026 that is thousands of prints. The 9097 close-model is what that looks like when size is also uncapped.

**Stop:** see Design-out D1–D3. Until the PLAN’s arming table matches live invert (one working pair + optional single 00028 extra), this item stays RED.

### R2 — This PLAN would still produce the grind family

| Grind ingredient | Close-model 9097 | This PLAN |
| --- | --- | --- |
| Fill-every-rung | yes | **yes** (§4.4 each rung below close) |
| 100% equity | yes (remaining cash per fill) | **yes in aggregate** (cash cap = whole book; `min(clip, cash)` leftover) |
| No clip | yes | **text says 200**; not hard against leftover/cash sizing |
| Fill at close | yes (close-model) | **no** — limit in `[low, high]` (this part holds) |
| End €1 | yes | **reachable** if CODE reads size as cash; **clipped cousin** (thousands of fee-negative RTs) if CODE keeps 200 |

Fill-at-limit does **not** save a ladder of adjacent fibs. Design-out must make the 9097 fingerprint a **run fail**, not a scorecard row.

### R3 — Do not start CODE

PLAN §8 step 2: a different reviewer greens **this** file; if RED, rewrite; **do not start CODE**. This review is that step. Grade is RED. CODE from #196 is forbidden until a rewrite clears R1–R2 and all yellows.

---

## YELLOW

### Y1 — Clip is not a hard cap against 100% deploy

`CLIP_QUOTE_EUR = 200` sits next to “never buy more than cash” and a cash cap that **permits** deploying all 10000 as 50 × 200 lots (and more as rails mint new `E` after sells). No `MAX_OPEN_BUY_LOTS`. No fail code `FULL_EQUITY_SIZE`. No fail if a print’s quote ≠ 200.

Live fill 1 quote is ~EUR 200. Match that **exactly**. Skip when cash cannot pay 200 + primary fee. Never “use the rest.”

### Y2 — Venue not labeled; Vision-on-disk unnamed; Bitstamp not excluded as named score

Scorecard must carry `venue` (and a data seal that is **not** a reseal of `c9689f5d`). Allowed named scores:

| `venue` | Meaning |
| --- | --- |
| `BINANCE-VISION-XRPEUR+KRAKEN-TAIL` | Vision history already on disk + Kraken public tail for the last closed 15m bars |
| `KRAKEN-OHLCVT-XRPEUR` | Official Kraken OHLCVT ZIP (+ Kraken tail after ZIP lag) |

**Not the named score:** `BITSTAMP-XRPEUR` (or any Bitstamp / Coinbase / XRPUSD stand-in), even if a sibling page can page it. Cross-venue mix without a venue string = `DATA_BAD`.

PLAN §3 as written would also **ignore** Vision-on-disk and send CODE to a 7GB Drive ZIP. Either allowed path is fine; **both must be named** so CODE does not silently pick Bitstamp or unlabelled Vision.

### Y3 — Synthesized empty bars vs “do not invent candles”

PLAN synthesizes missing 15m buckets as `O=H=L=C=prev close`, `volume=0`, no fills, **but they advance the 96-bar rail window**. That makes 96 bars = 24h **clock**, which matches the user rail lock — if and only if CODE labels them **derived**, never Kraken prints. Sibling data research marks inventing empty OHLC as RED.

**Rewrite:** synthesized rows are `derived: true` in the bar schema; MANIFEST already counts `synthesized_empty_bars` (keep that). Rails may use them for **clock**. Fills stay forbidden (PLAN already says this). Do not write them into a file labeled as Kraken OHLCVT verbatim.

### Y4 — “Swap jobs” prose vs geometric Lo/Hi table

The recipe says after any fill, **those two prices** swap jobs (TP becomes next entry). The operational table then says geometric roles **stay** `Lo` buy / `Hi` sell, and “jobs swap” only in the sense that the filled price stops working. That **is** the correct **spot** reading (no naked short). It is also easy for CODE to implement the **naive** swap and rest a sell while flat.

PLAN already fails `NAKED_SHORT`. Keep that. Add a unit that **after sell `Hi`, the next armed order is buy `Lo` only** — never sell `Lo`, never sell `Hi` with 0 XRP, never buy `Hi` as breakout.

This stays YELLOW (ambiguity), not RED, because the table and fail code already pick the spot reading. Tighten the sentence so CODE cannot “fix” it into a short.

---

## GREEN (what this PLAN already holds — do not bargain away in the rewrite)

### G1 — Named book, not the gate

`invert-wf-2023`, EUR **10000**, XRPEUR 15m, 2023-01-01 00:00 Europe/Brussels → last **fully closed** 15m bar. **Not** the fund gate until CEO says. Gate remains `invert-paper` only (return > 0 after fees **and** ≥ 8 prints **and** maxDD ≤ 8%). `is_fund_gate: false`. Combined maxDD vs 8% is a **flag**, not promotion.

### G2 — invert-paper fill 1 stays

`PAPER-00029` buy 160.64773 @ **1.24496** = fill **1**. Resting `PAPER-00030` @ 1.26778 is not a fill. Open `PAPER-00028` @ 1.23084 is not a fill. Do not flatten, cancel, or “clean” that book. Do not add 20+1.

### G3 — No reseal · no `dca-paper` reset

Cite `sha256:c9689f5d7d583320e724900b0ce4ef68193878c880d11939badd1dd59016e390`. Lab clip (20 fills · +0.681154% · maxDD 0.890854% · 2026-08-18 21:00 → 2026-08-26 08:00 BXL) ≠ this walk-forward. Five BTCUSD slices on `dca-paper` stay held. Retired hashes stay retired **in name** — the rewrite must also retire them **in the arming table** (R1).

### G4 — Clock: 15m bar-close, no lookahead, rails `i-96..i-1`

```text
H[i] = max(high[j] for j in i-96 .. i-1)
L[i] = min(low[j]  for j in i-96 .. i-1)
```

Do not include bar `i` in its own rails. Do not read `i+1`. Warmup 96 bars seed rails only (no fills, no fees). `DATA_GAP` rather than invent a future swing. Fill price = **limit** inside `[low, high]`, not the close, not beyond the limit. Newly armed opposite **skips this bar**. Brussels tz via `zoneinfo`, not UTC+1 year-round. Start of book UTC: `2022-12-31 23:00:00Z`.

Keep all of this. The 9097 run was a **close-model**; this clock is the correct one.

### G5 — Invert job rule (prose) · no naked short

After **any** fill: the **other** of those two prices becomes the working order; **re-arm the filled price only on the opposite fill**. Spot: no naked short. After sell-TP: flat cash; next entry is **buy-back**. Same-bar re-arm forbidden (`SAME_BAR_REARM`).

Keep the prose. Change the **arming table** so it cannot spawn a ladder (D1).

### G6 — Fees 0.26 primary + 0.40 / 0.80 shadows · clip number 200

Primary hits cash. Shadows are parallel ledgers on the same fills (no extra qty, no extra fill times). Round-trip primary = two 0.26% events. Journal check: EUR 200 @ 1.24496 → primary fee **0.52**. Do not add a fourth 0.16% maker column unless CEO asks. Do not relabel 0.26 as proof of live maker fills.

The **number** 200 stays. The **hardness** of that number is Y1.

### G7 — Combined is sequential, not the sum

Year slices 2023 / 2024 / 2025 / 2026-to-now may run **in parallel**, each flat EUR 10000 at slice open (diagnostics). **Combined** is one cash pile, one inventory, one set of resting pairs, 2023-01-01 → now. CODE may not define combined as `sum(slice returns)` or `mean(slice maxDD)`. `test_combined_not_sum.py` stays. Coincidence still must not *define* combined as the sum.

### G8 — Still paper · hygiene

Autonomy **level 2**. No `kraken order`. No keys. No Phantom against `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3` or Base `0x9eb954b567ef3616424a6e1bf42c63724930aa54`. No new Surge host. Scorecards in git as markdown/JSON. VOORBEELD. Fail the run on `TOUCHED_INVERT_PAPER` / `TOUCHED_DCA_PAPER`. No shop HTML. XRPEUR only.

---

## Design-out (PLAN rewrite must include — then re-review)

These replace the RED/YELLOW holes. They do **not** loosen G1–G8.

### D1 — One invert pair, not a ladder

```text
MAX_OPEN_BUY_LOTS = 2   # filled-or-working buy Lo + optional 00028 extra. Never "each fib".
```

| Inventory | Armed | Not armed |
| --- | --- | --- |
| Flat | **one** buy LIMIT at `Lo` (nearest buy-eligible rung **below** last close, from the current 96-bar fib set) | every other buy; any sell |
| Optional extra (00028) | **at most one** additional buy at a **lower** unique rung than `Lo`, only if cash still covers **200 + fee** after the first lot | a third buy; “pair each remaining rung” |
| Long (after buy `Lo`) | sell LIMIT at `Hi` for that qty; extra unfilled buy may stay | re-arm `Lo`; pyramid; sell `Lo` |

**`Hi` = 24h rail `H[i]`** (live 00030 pattern), **not** “next higher unique retracement.” If `Hi <= Lo`, skip the candidate. Do not arm extensions-below as a stack of 50 lots.

After sell `Hi`: flatten that lot; **now** re-arm buy `Lo` only. Geometric pair stays `Lo`/`Hi`. No short. No buy `Hi` breakout.

**Fail the run:** `FILL_EVERY_RUNG` if more than `MAX_OPEN_BUY_LOTS` distinct buy prices fill in any rolling 96-bar window without intervening opposite fills that free those lots.

### D2 — Clip is hard EUR 200; never % of equity; never leftover cash

```text
CLIP_QUOTE_EUR = 200
fee = CLIP_QUOTE_EUR * 0.0026
if cash < CLIP_QUOTE_EUR + fee: skip   # do not shrink
qty = CLIP_QUOTE_EUR / limit_price     # not cash/price, not equity/price
```

**Fail the run:** `FULL_EQUITY_SIZE` if any print’s quote notional differs from 200 by more than one tick of cost (`pair_decimals` 5). Last-lot “use the rest” is this fail.

### D3 — 9097 fingerprint is a fail, not a score

If a slice or combined prints **any** of:

- end equity **≤ €100** with fills **≥ 1000**
- return after fees primary **≤ −50%** with fills **≥ 1000**
- a fill whose price is the bar **close** (close-model)
- fill count on one bar **> MAX_OPEN_BUY_LOTS** buys (ladder sweep)

then write `GRIND_FINGERPRINT` / `CLOSE_MODEL` and **do not** publish a GREEN-looking SCORECARD. Cite the already-printed **9097 / −99.99% / end €1 / BINANCE-VISION-XRPEUR** as the warning this kill is for. That print is **not** this book’s score.

### D4 — Venue field (required)

Scorecard JSON adds:

```json
"venue": "BINANCE-VISION-XRPEUR+KRAKEN-TAIL | KRAKEN-OHLCVT-XRPEUR",
"venue_is_named_score": true
```

Allowed named scores = those two strings only. **`BITSTAMP-XRPEUR` is not a named score.** Unlabelled mix = `DATA_BAD`. Data sha256 is a **replay seal**, not a reseal of `c9689f5d`.

CODE may read Vision+Kraken-tail **already on disk** or fetch Kraken OHLCVT ZIP. Do not page REST OHLC and call it 2023. Do not require Bitstamp because the ZIP is large.

### D5 — Same-bar and no lookahead (keep, then tighten)

Keep: rails exclude `i`; fill at limit on touch; newly armed opposite skips this bar; sells evaluated before buys; never sell more XRP than held; forming bar dropped.

Tighten: **global** fills on one bar ≤ current armed lots (already capped by D1). If a bar could touch both `Lo` and `Hi` of the **same** lot, fill **neither** (`DUAL_TOUCH_SKIP`) — OHLC has no path. Do not credit a round-trip inside one 15m candle.

### D6 — Tests CODE must gain (still later PR)

Keep the PLAN’s tests. Add:

- `test_not_fill_every_rung.py` — a bar whose range covers the whole fib set fills **at most** `MAX_OPEN_BUY_LOTS` buys, not every rung.
- `test_clip_is_200.py` — no print quote ≠ 200; cash leftover is skipped, not sized.
- `test_tp_is_rail_h.py` — after a buy, working sell is 24h `H`, not adjacent retracement.
- `test_grind_fingerprint.py` — synthetic 100% equity / close-model path raises `GRIND_FINGERPRINT` / `CLOSE_MODEL` / `FULL_EQUITY_SIZE`.
- `test_venue_label.py` — scorecard refuses missing venue; refuses `BITSTAMP-XRPEUR` as named score.

---

## Bar for GREEN (this PLAN, after rewrite)

A later reviewer may GREEN **only** if the rewritten page has **no red and no yellow**, including:

1. Named book `invert-wf-2023` EUR 10000. **Not** the fund gate. `invert-paper` fill **1** stays. No reseal `c9689f5d`. No `dca-paper` reset.
2. 15m bar-close. No lookahead. Rails from prior **96** bars, not bar `i`.
3. Invert: after fill, swap jobs of **those two** prices; re-arm filled price **only** on opposite fill. **No naked short.** **No ladder.** `MAX_OPEN_BUY_LOTS = 2`. `Hi` = 24h H.
4. Clip **EUR 200** hard. Fees **0.26%** primary + **0.40 / 0.80** shadow. No leftover-cash sizing. No 100% equity.
5. Combined = one sequential book, not the sum of slices.
6. Close-model / fill-every-rung / 9097 fingerprint **fails the run**.
7. `venue` required. Vision+Kraken-tail **or** Kraken OHLCVT. **Not Bitstamp as the named score.**
8. Still paper. No keys. No orders. VOORBEELD. No second journal domain.

Until then: **PLAN stage RED. Do not start CODE.**

---

## This run

| Did | Did not |
| --- | --- |
| Read #196 PLAN from zero (504 lines) | Implement replay, fetch ZIP, place orders |
| Scored against locked invert / clip / fees / combined / venue | Reseal `c9689f5d` |
| Mapped §4.4 arming to the 9097 close-model fingerprint | Reset `invert-paper` or `dca-paper` |
| Wrote design-out D1–D6 for a PLAN rewrite | Patch Surge / shop HTML / start CODE |
| | Mail, KBO, Phantom spend, keys in git |

**PLAN stage: RED.** Still paper. `invert-wf-2023` is not the fund gate. invert-paper fill 1 stays. Do not reseal `c9689f5d`. Do not reset `dca-paper`. Do not treat 9097 / −99.99% / end €1 as invert. Do not start CODE from #196.

---

## Re-check (copy/paste)

```bash
# This review must exist and must not green the ladder:
rg -n 'Verdict|fill-every-rung|9097|MAX_OPEN_BUY_LOTS|BITSTAMP|CLIP_QUOTE_EUR' \
  docs/rgy-2026-08-27/coder/REVIEW-05-plan-wf.md

# PLAN under review (other branch — do not merge from this PR):
# https://github.com/eyeskull2220/solana-invoice/pull/196

# Never from this seat:
# kraken paper reset --workspace invert-paper
# kraken paper reset --workspace dca-paper
# kraken order …
```

End of REVIEW-05. Still paper. No orders. No keys.
