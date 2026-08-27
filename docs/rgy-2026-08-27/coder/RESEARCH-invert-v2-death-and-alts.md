# RESEARCH — invert-v2 death score and alts (not invert)

**Seat:** RESEARCHER · Coder  
**Lens:** start from Coder’s **named death print**, then broaden. Docs only.  
**Date:** 2026-08-27  
**Stamp:** VOORBEELD · paper / simulated · not FACTUUR · not INVOICE · not live-trade advice  
**HEAD (leftover `main` at write):** `2170952`  
**Still paper.** `invert-paper` stays. `dca-paper` stays. Do not reseal `c9689f5d`.  
**`is_fund_gate`:** **false**

This file answers Coder’s ten questions about **why a 2023→now 15m XRPEUR close-model died**, and which **alts** are hypotheses vs steal-around-invert. It does **not** rewrite sibling packs. It does **not** place orders, paste keys, reseal the lab clip, reset `dca-paper`, or invent a prettier curve.

Sibling packs this sitting (read, not copied):

| PR | File | Steal from it |
|---|---|---|
| [#200](https://github.com/eyeskull2220/solana-invoice/pull/200) | `RESEARCH-walkforward-broad.md` | Clock, tape, confirmation, scoring. **STEAL vs H1–H10.** Do **not** apply H* as invert. |
| [#196](https://github.com/eyeskull2220/solana-invoice/pull/196) | `PLAN-invert-wf-2023.md` | Clip **200**, opposite-fill re-arm, prior-**96** rails, sequential **10k**. |
| [#198](https://github.com/eyeskull2220/solana-invoice/pull/198) | `RESEARCH-xrpeur-15m-broad.md` | Kraken REST OHLC last-720 **UNSATISFIABLE**. Trades reconstruct = keyless Kraken-native path. Bitstamp = labeled fallback. Drive OHLCVT = official CSV if obtainable. |
| [#199](https://github.com/eyeskull2220/solana-invoice/pull/199) | `RESEARCH-invert-walkforward.md` | Bar-close, wick touch of standing limits, `DUAL_TOUCH_SKIP`, swap those two prices, re-arm only on opposite fill. |
| [#194](https://github.com/eyeskull2220/solana-invoice/pull/194) | `RESEARCH-wf-slice-2023.md` | 13–14 Jul Torres / 13–14 Nov wick as **regimes**, not scores. |
| [#201](https://github.com/eyeskull2220/solana-invoice/pull/201) | `REVIEW-wf-2023-score.md` | Same named cells judged **RED / not invert**. Reviewer also inferred 100% size from the 1.00 floor. **This file keeps Coder’s clip-200 lock** and does not flatten the two stories into a restated PnL. |

---

## Locks (this sitting)

| Lock | Status |
|---|---|
| Still paper | **held** — no orders, no keys |
| `invert-paper` stay | **held** — fill **1** `PAPER-00029` @ 1.24496; TP `PAPER-00030` @ 1.26778 not a fill; open `PAPER-00028` @ 1.23084 not a fill |
| `dca-paper` stay | **held** — five BTCUSD slices |
| Do not reseal `c9689f5d` | **held** — cited, not rotated |
| Named death score as invert | **RED** — it is fill-every-rung, not invert |
| Promotion / live / 10k as deposit | **RED** |
| `is_fund_gate` | **false** |

Gate on live `invert-paper` (unchanged, **NOT MET**): return > 0 after fees **and** ≥ 8 prints **and** maxDD ≤ 8%.

Sealed lab clip (cite only): name `fib-grid-invert-xrpeur-15m`, window 2026-08-18 21:00 → 2026-08-26 08:00 Europe/Brussels, 20 fills, +0.681154%, maxDD 0.890854%, vs `sha256:c9689f5d7d583320e724900b0ce4ef68193878c880d11939badd1dd59016e390`. That is **not** this death print and **not** a 2023 walk-forward.

Retired hashes stay retired: `2bfb1b68` fill-every-rung · `9056f296` entry-waits-TP · `094513` arming-only.

---

## Named score (Coder measured — do not pretty)

Close-model **BINANCE-VISION-XRPEUR**, window 2023-01-01 → now:

| Cell | Print |
|---|---|
| Fills | **9097** |
| Return after fees | **−99.989999%** |
| maxDD | **99.990007%** |
| End equity | **~1 EUR** (from 10000) |
| Fees | **~4278 EUR** |
| Clip | **WAS 200** |
| Rails | **WERE prior 96** (24h of 15m) |
| Miss | **fill-every-rung** — **14 adjacent pairs armed every bar** (retired `2bfb1b68`) |
| Twin | **Bitstamp 9069 / same death** (labeled `BITSTAMP-XRPEUR`, not mixed into the named row) |

**That score is NOT invert.** Invert is: after any fill, swap jobs of **those two** prices; re-arm the filled price **only** on the opposite fill; spot no naked short. Fill-every-rung arms the whole stack every bar.

Do not replace −99.989999%. Do not write a hypothetical EUR-200 pair-invert curve in this file. A later **new** score after a **new** engine is a different artifact. Not a reseal.

**Arithmetic on the printed cells (not a restatement):**

- Full-clip primary fees if every one of 9097 prints were EUR 200 × 0.26% = **4730.44 EUR**. Coder’s **~4278** is ~90% of that — consistent with clip 200 **shrinking** as cash dies, not with a silent 100% restatement.
- 14 × 200 = **2800 EUR** of working buys if all 14 pairs are armed from a 10000 book. That is cash-feasible without all-in. The miss is the **ladder**, not a missing clip number.
- 10000 − 4278 = 5722 if fees were the only drain. End **~1 EUR** therefore also needs **inventory / overlapping lots / same-bar both-sides**, not fees alone. Sibling reviewer [#201](https://github.com/eyeskull2220/solana-invoice/pull/201) inferred all-in from the 1.00 floor. Coder’s lock for **this** sitting remains clip **200**. This file does **not** invent which remainder-path produced dust.

9097 / ~1334 calendar days ≈ **6.8 fills/day**. Lab-rate invert on the sealed clip is **20 / 8 days = 2.5 fills/day**. Different machines.

---

## Method of this paper

1. **Do not apply PR 200 H1–H10 as invert.** Those are named recipe changes. Flag only.
2. **Steal** clock / tape / confirmation / scoring / two fill columns / fee shadow / `DUAL_TOUCH_SKIP` from the sibling packs.
3. **Public ranges** are labeled venue + resolution. They are **not** invert fills and **not** a 2023 equity curve.
4. **Alts A–D** are Coder’s questions. Each is **HYPOTHESIS** or **labeled experiment**. None is applied here.

---

## 1. Fee vs rung math — when can a completed invert even beat fees?

**STEAL (scoring, not recipe):** keep engine **0.26%** per print and the journal shadow ladder **0.40 / 0.80** taker (round-trip **0.52 / 0.80 / 1.60**). Gate-style “after fees” uses the worst honest shadow you will defend, not the prettiest. ([PR 200 §6](https://github.com/eyeskull2220/solana-invoice/pull/200); [PR 196 §4.6](https://github.com/eyeskull2220/solana-invoice/pull/196).)

**Public Kraken Pro Tier 1 this sitting (not the paper engine):** maker **0.40%** / taker **0.80%**. Instant Buy/Sell is a different product (1% / 1.5% + spread). Do not mix. ([Kraken fee schedule](https://www.kraken.com/features/fee-schedule); [How trading fees work](https://support.kraken.com/articles/201893638-how-trading-fees-work-on-kraken).)

Paper still deducts **0.26%** (Starter-era default). **HYPOTHESIS (H6 in PR 200, not applied):** switch the engine to maker 0.40% / 0.16% because “grids make.” That changes gate 1 without changing rungs.

### 1.1 What a completed invert must clear

Buy `Lo`, sell `Hi`, qty sized off quote:

```text
gross = (Hi - Lo) / Lo
fee_as_%_of_entry ≈ 0.26% + 0.26% × (Hi / Lo)    # two prints
net ≈ gross − that
```

When `Hi ≈ Lo`, two 0.26% prints ≈ **0.52%** of entry. A completed invert of a pair whose `(Hi−Lo)/Lo` is **under** ~0.52% is fee death **even if both sides print**. Shadows: **0.80%** and **1.60%**.

Live invert-paper latch (not a fill of 00030): **1.24496 → 1.26778**.

```text
gross = (1.26778 − 1.24496) / 1.24496 = 1.8330%
primary RT ≈ 0.26% + 0.26% × (1.26778/1.24496) = 0.5248%
net ≈ 1.308%  if  the TP prints and slip = 0
```

That hypothetical is **not** a print, still **2 < 8**, and is **not** written into the live scoreboard. It only shows a **wide** pair can beat 0.52%. Adjacent fibs often cannot.

### 1.2 Implied fib spacing (15 unique rungs → 14 adjacent pairs)

PLAN full set, one-origin retracements (dups from “both sides” collapsed), plus rails and both-side extensions — **15 unique ticks**, **14 adjacent pairs**, matching Coder’s death miss:

| Sorted as fraction of 24h range `R = H − L` | Adjacent gap as × `R` |
|---|---|
| extensions below (4) | 0.618, 0.382, 0.346, 0.272 |
| `L` → 0.236 → 0.382 → 0.5 → 0.618 → 0.786 → `H` | **0.236, 0.146, 0.118, 0.118, 0.168, 0.214** |
| extensions above (4) | 0.272, 0.346, 0.382, 0.618 |

**Tightest interior pair** is 0.382↔0.5 and 0.5↔0.618: gap = **0.118 × R**.

As a percent of price `P`:

```text
adjacent_% ≈ 0.118 × (R / P)
need adjacent_% ≳ 0.52%  ⇒  R/P ≳ 0.52% / 0.118 ≈ 4.41%
need adjacent_% ≳ 0.80%  ⇒  R/P ≳ 6.78%
need adjacent_% ≳ 1.60%  ⇒  R/P ≳ 13.56%
```

So on a day whose 24h range is **under ~4.4% of price**, a **completed** invert of the tightest adjacent fib pair **cannot** beat primary 0.52% even with perfect fills and zero slip. At the 0.80 shadow, you need ~p75 range. At 1.60, almost never.

### 1.3 Typical 24h XRPEUR range 2023–2026 (public, labeled)

**Not Kraken 15m. Not invert fills. Not a 2023 equity curve.** Calendar-day OHLC is a **proxy** for “24h high−low,” not the rolling prior-96 window PLAN uses.

**Bitstamp daily `step=86400`**, pair `xrpeur`, public, no key, window `2022-12-31 → 2026-08-27` (**n = 1336** days). Label: **`BITSTAMP-XRPEUR` daily**. ([Bitstamp OHLC](https://www.bitstamp.net/api/).)

| Slice | n | median `(H−L)/C` | mean | p25 | p75 | p90 |
|---|---:|---:|---:|---:|---:|---:|
| All | 1336 | **4.290%** | 5.634% | 2.954% | 6.780% | 9.823% |
| 2023 | 365 | 4.019% | 5.031% | 2.783% | 6.102% | — |
| 2024 | 366 | 4.412% | 6.283% | 2.874% | 7.663% | — |
| 2025 | 365 | 4.977% | 6.271% | 3.553% | 7.643% | — |
| 2026 YTD | 239 | 3.762% | 4.604% | 2.636% | 5.504% | — |

Median `(H−L)/L` = **4.399%**.

Fee test on **this daily proxy** (still not invert):

| Test | Days | Share |
|---|---:|---:|
| Tightest adjacent `0.118×(H−L)/C` < **0.52%** (cannot beat primary RT) | 685 / 1336 | **51.3%** |
| Full rails `(H−L)/L` < **0.52%** (even 24h H vs L cannot beat primary) | 0 / 1336 | **0.0%** |
| Full rails `(H−L)/L` < **1.04%** (alt A vs the two rails) | 8 / 1336 | **0.6%** |

**Read that slowly.** On about **half** of public Bitstamp days, the **tightest adjacent fib pair** is inside the primary fee. The **two rails** `L`/`H` almost always clear 0.52% **if** the book actually traverses the whole 24h range as one invert lot. Fill-every-rung does the first thing all day. Pair-invert / alt D is the second thing, rarely.

Annual EUR extremes (different aggregator; **year** range, not 24h): Traders Union XRP/EUR 2023 high **0.8378** / low **0.285** / close **0.5592** (~+77% buy-and-hold). 2024 high **2.76** / low **0.3**. 2025 high **3.3** / low **1.33**. 2026 YTD high **2.0619** / low **0.8527**. **Buy-and-hold is not invert.** ([Traders Union XRP/EUR history](https://tradersunion.com/currencies/price-history/xrp-eur/).)

Kraken public ticker **this sitting** (2026-08-27, not 2023): last **1.24541**, 24h high **1.26778** (= live TP 00030), 24h low **1.17108**. `(H−L)/last` ≈ **7.8%** today — a **wide** 24h, still not a print. Coder 01 cited low **1.19568** earlier the same day. ([Kraken Ticker](https://docs.kraken.com/api-reference/market-data/get-ticker-information).)

**When can a completed invert beat fees?**

- **Adjacent 0.118-rung pairs:** only when 24h `R/P` ≳ **4.4%** (primary), ≳ **6.8%** (0.80 shadow), ≳ **13.6%** (1.60). Public daily median sits **on the 4.4% knife-edge**.
- **Wide pairs** (live 1.83% latch; full-day rails ~4.4% median): yes **on paper geometry**, if the opposite actually prints, clip stays 200, and you do **not** spray 14 pairs.
- **Fill-every-rung of 14 pairs:** you mostly complete the **knife-edge** pairs, many times per week, two fees each. That is the death math. It is not a 2023 invert equity curve.

**HYPOTHESIS — would change invert (not applied):** size rungs from depth so each clip is < X% of visible bid/ask (PR 200 H7). No public 2023 XRPEUR depth tape in this research.

---

## 2. Why fill-every-rung dies on 15m

Three stacked machines, not one unlucky year.

### 2.1 Many rungs inside one bar

A 15m candle’s `(H−L)` is often **several** adjacent 0.118-rungs. Torres day (diagnostic, §10): Bitstamp 15m **2023-07-13 18:15 UTC** ran **0.70028 → 0.83783** (~**18%** of that close). One bar can tag the **entire** 14-pair stack. Fill-every-rung prints a **ladder**. PLAN invert logs **skipped rungs** and fills **at most one per lot per bar**.

### 2.2 Same-bar both-sides

OHLC has no path. If `low ≤ Lo` and `high ≥ Hi` on one close-model bar, a spray engine can credit **buy and sell on the same close**. Two 0.26% hits, **zero** geometric edge if both fill at the same close. That is PR 200 **L2** / PR 199 **B3**. Close-model does not even require a wick: the **close** can invent the cross.

### 2.3 Fee grind

9097 prints × ~0.47 EUR (Coder’s ~4278 / 9097) is a **fee factory**. Median-day adjacent pairs do not clear 0.52% (§1). Overtrade + sub-fee spacing + same-bar round-trips = **−99.989999%**. That number stays. It is **not** invert PnL.

### 2.4 Contrast: PLAN pair-invert vs invert-paper this week

| | Death print (this score) | PLAN `invert-wf-2023` ([#196](https://github.com/eyeskull2220/solana-invoice/pull/196)) | Live `invert-paper` this week |
|---|---|---|---|
| Recipe | Retired **fill-every-rung** `2bfb1b68` | Pair invert: lot = `(Lo, Hi)`; swap those two; re-arm **only** on opposite | Same invert lock. **Do not reset.** |
| Armed | **14 adjacent pairs every bar** | Buy rungs `< last close`, each paired with **next higher**; cash cap; skip extras | **Cap 2 long** (alt B, labeled experiment) · **nearest-2** 24h fibs (alt C, Day 0) |
| Clip | **WAS 200** | **EUR 200** | Fill 1 cost ~200 @ 1.24496 |
| Rails | **prior 96** | prior 96, **exclude bar i** | Live TP latched at **24h H 1.26778** |
| Book | 10000 simulated, Vision close-model | sequential **10k** combined; year slices parallel diagnostics | live paper 10000; fill **1**; gate **NOT MET** |
| Same-bar | close-model; newly armed opposite **can** print | newly armed opposite **skips this bar**; `SAME_BAR_REARM` fails the run | not this score |
| What it is | **NOT invert** | **paper replay contract**, still `is_fund_gate: false` | **fund gate book**, n=1 |

PLAN is **one lot’s opposite-fill**, plus the 00028 pattern (other *unfilled* buys at **different** prices may stay). It is **not** 14 live pairs printing every touch.

**STEAL:** opposite-fill re-arm, clip 200, prior-96, sequential 10k, same-bar skip of the newly armed opposite.  
**Do not steal:** fill-every-rung. **H8 in PR 200 — would change invert — not applied:** revive `2bfb1b68`.

---

## 3. Two fill columns (STEAL from PR 200) — 9097 vs a wick PLAN score

**STEAL:** for a frozen-invert walk-forward, publish **two** columns — **touch** (`low ≤ P ≤ high`, fill at `P`) vs **close-through** (close crosses / closes through `P`). Gate language stays **prints**, not tags. ([PR 200 §5](https://github.com/eyeskull2220/solana-invoice/pull/200); Freqtrade: fill at requested price if inside the candle high/low, path unknown. ([Freqtrade backtesting](https://www.freqtrade.io/en/stable/backtesting/).))

| Column | Fill when | Bias vs a live standing limit |
|---|---|---|
| **Touch / wick** (PR 199 L2, PLAN §4.4) | bar range tags the **already-resting** limit | Optimistic vs queue; honest vs “standing order” |
| **Close-through** | close crosses the level | Pessimistic: misses honest intra-bar fills |
| **Close-model (9097)** | Coder’s word: decisions **and** fills at close | **Different strategy.** Can same-bar re-arm. Not PLAN. |

**How this changes interpretation of 9097:**

- 9097 is a **close-only spray**, not a conservative lower bound of invert.
- A **wick PLAN** score of **pair-invert** (one lot, opposite-only, newly armed skips this bar) would almost certainly print **fewer** than 9097, because the 14-pair arm goes away. **Do not invent that number.**
- A **wick fill-every-rung** score would likely print **more tags** than close-model (wicks tag rungs the close never closed through). Also **not invert**. Also **not invented here**.
- Live TP 00030 sitting while the public high **equals** 1.26778 is the touch-vs-print gap in one sitting (Coder 01). Do not backfill 00030 from a tag.

**HYPOTHESIS (PR 200 H3, not applied):** require close-through before swap-jobs. New book if shipped.

---

## 4. L2 path-unknown — written tie-break for invert-v2 (no invented fills)

If one 15m bar tags both `Lo` and `Hi` of a lot, OHLC cannot order them. Silent “both filled at the good prices” is lookahead (PR 200 L2, PR 199 B3).

**Recommend this written rule for a later invert-v2 paper book** (new hash, still paper, **not** a reseal of `c9689f5d`, **not** applied in this file):

| Priority | Rule | Why |
|---|---|---|
| **0** | Fair invert only arms **one** side of a lot given inventory. If only `Lo` is working, a bar that also tags `Hi` fills **`Lo` only**. `Hi` is not armed. | Recipe. Dual-touch of both prices should be rare if L4 holds. |
| **1 (default)** | If **both** sides of the **same lot** would be eligible (recipe bug or same-bar re-arm): **`DUAL_TOUCH_SKIP`** — fill **neither**, flag the bar, **not** a round-trip. | STEAL PR 199. Does not invent a path. |
| **2 (diagnostic column, same venue)** | Optional **1m detail** (Freqtrade `--timeframe-detail` analogue) **from the same tape** as the 15m book. First 1m that tags the **armed** side fills at `P`. Newly armed opposite still skips the remainder of that 15m. | STEAL PR 200 optional 1m. **Do not** mix Vision 15m with Kraken 1m. |
| **3 (not default)** | **Adverse-first** (PLAN §4.4 operational order: sells of longs, then buys, then skip newly armed) as a **named** third column. | A path model. Write it. Do not silently take the favourable order. |

**Do not** use “fill both.” **Do not** invent 1m fills in this markdown. **Do not** treat `DUAL_TOUCH_SKIP` as a print toward 8.

If invert-v2 ever ships, the scorecard must show: same-bar dual-touch count, skip count, and which of {1,2,3} was locked **before** the run (PR 200 L10 / PBO: freeze the rule before seeing results).

---

## 5. Alt A — skip a pair whose `(Hi−Lo)/Lo` < 2 × primary RT (1.04%)

**HYPOTHESIS. Not applied.** Would change invert (spacing filter = new recipe). New book / new hash if anyone runs it. Not a reseal.

Geometry from §1: 2 × 0.52% = **1.04%**. On the Bitstamp daily proxy, **full rails** fail this on only **~0.6%** of days. **Tightest adjacent** pairs fail it on a **majority** of median-range days (adjacent ~0.51% at median 4.29% range).

So alt A, applied to **14 adjacent pairs**, would mostly **turn the stack off** and leave wide pairs (rails / far extensions). That is closer to alt D than to fill-every-rung. It is **not** a free “fix” of 9097: it is a **different invert**. Flag. Do not apply. Do not restamp `c9689f5d`.

---

## 6. Alt B — cap 2 long clips (live invert-paper this week)

**HYPOTHESIS / labeled experiment.** Not applied to the 2023 dump. **Do not reset** the live book to “match” a replay.

Live book this sitting already **looks** like a cap: **one** filled long (`PAPER-00029` @ 1.24496) + **one** resting lower buy (`PAPER-00028` @ 1.23084) + **one** TP (`PAPER-00030` @ 1.26778). Fill count stays **1**. Cap-2 is how you stop 14 × 200 from becoming implicit leverage. It does **not** by itself fix sub-fee adjacent spacing or same-bar close-model.

PLAN cash cap: skip extra rungs rather than lever. Alt B is a **hard count** on that skip. Recipe change if the locked invert allowed more unfilled buys than 2. **New book** if used as a 2023 engine. Live experiment stays on `invert-paper` and does **not** fund.

---

## 7. Alt C — nearest-2 rungs only (Day 0 invert-paper)

**HYPOTHESIS / labeled experiment.** Day-0 invert-paper picked the nearest buy-eligible rung below last close and the nearest rung above (PR 199 walk-forward protocol step 3). Full fib **set** still exists; only **two** prices work.

That is **not** fill-every-rung. It is also **not** proven by n=1. Do not grid-search “nearest-k” on 2023–2026 and call it OOS (PR 199 attack 12 / PR 200 H4). If a later paper run locks k=2 **before** the window, new hash, still paper, still `is_fund_gate: false`.

---

## 8. Alt D — only 24h `H` and `L` as the two prices

**HYPOTHESIS.** Like the live latch **TP 1.26778 / entry 1.24496**, not the full 14-rung set.

This is the pair that **can** beat 0.52% on ordinary days (§1: median rails ~4.4% vs adjacent ~0.51%). It is also **slow**: one-way months (Jan/Mar/Jul/Aug/Oct 2023 in [#194](https://github.com/eyeskull2220/solana-invoice/pull/194)) leave the opposite sitting. Fill count may stay thin. Do not celebrate thin maxDD with n≪8.

Naming “rails = prior-96 H and L, **only those two prices**” **specifies** invert. Journal today still says full fib set. **H1/H2-class change.** Flag. Do not apply. Do not treat 1.26778 as a 2023 TP (PR 199 B2).

---

## 9. Data honesty — named score stays Vision until CEO says

**STEAL:** the named death row stays **`BINANCE-VISION-XRPEUR`** (close-model, 9097, −99.989999%, …). Do not relabel it Kraken. Do not mix Bitstamp 9069 into that row. Twin stays **`BITSTAMP-XRPEUR` 9069 / same death**.

**A later labeled dump**, if CEO wants a Kraken-native 15m book, should be **PR 198 path #1: Kraken public Trades reconstruct** (`GET /0/public/Trades?pair=XRPEUR`, result key `XXRPZEUR`, nanosecond `since`/`last`, 1000/call, 1–2 s pause, bucket 900s). That is the keyless path that actually reaches 2023-01-01 **and** now. REST `/OHLC` interval 15 remains **UNSATISFIABLE** (last 720 ≈ 7.5 days). ([Kraken Get Recent Trades](https://docs.kraken.com/api-reference/market-data/get-recent-trades); [OHLC 720 cap](https://docs.kraken.com/api-reference/market-data/get-ohlc-data); [PR 198](https://github.com/eyeskull2220/solana-invoice/pull/198).)

**Path #2** if the ZIP is actually obtained: Kraken Drive **OHLCVT** (`XRPEUR_15.csv` after `namelist`) + Trades-fill of the post-last-quarterly tail. Missing CSV rows = **no trades**, not a flat candle that can fill. ([Downloadable OHLCVT](https://support.kraken.com/articles/360047124832-downloadable-historical-ohlcvt-open-high-low-close-volume-trades-data).)

**Bitstamp** remains the **labeled fallback**, not the Kraken book, not a baptism of Vision.

**Do not mix dumps.** Vision 15m + Kraken tail is already the splice [#201](https://github.com/eyeskull2220/solana-invoice/pull/201) called RED. A later Kraken reconstruct is a **new** `data_sha256`, new scorecard, `is_fund_gate: false`.

### Vision 5-bar gap (cite, because this file cites Vision)

Official Binance Vision spot 15m klines, pair **XRPEUR**, UTC:

| Day | Rows (expect 96) | Gap |
|---|---:|---|
| 2023-03-23 | **96** | none |
| **2023-03-24** | **91** | **5 bars / 75 min** |
| 2023-03-25 | **96** | none |

**Missing opens (UTC):** `2023-03-24 12:45`, `13:00`, `13:15`, `13:30`, `13:45`. Internal jump 12:30 → 14:00.

Fetched this sitting from:

- https://data.binance.vision/data/spot/daily/klines/XRPEUR/15m/XRPEUR-15m-2023-03-24.zip  
- Confirmed in the monthly file: https://data.binance.vision/data/spot/monthly/klines/XRPEUR/15m/XRPEUR-15m-2023-03.zip  

Schema: Binance public data klines. ([binance-public-data README](https://github.com/binance/binance-public-data).)

A Binance publish hole is **not** a Kraken hole. Do not interpolate those 75 minutes into prints. PLAN synthesizes empty clock buckets that **must not fill**. Kraken OHLCVT omits no-trade intervals. **Do not launder.**

---

## 10. 13–14 Jul 2023 (Torres) and 13–14 Nov 2023 (wick) — diagnostics only

**No invented scores.** What PLAN invert would even be **allowed** to do, vs grind.

### 10.1 Torres 13–14 Jul 2023

Public chronology (USD/news, not Kraken 15m fills): U.S. District Judge Analisa Torres, **2023-07-13** — programmatic exchange sales of XRP **not** investment contracts; institutional sales **were**. CNBC: XRP last **+71%** at about **80 cents** (Coin Metrics). Coinbase tweeted it would allow XRP trading again. ([CNBC 2023-07-13](https://www.cnbc.com/2023/07/13/xrp-surges-after-judge-delivers-a-huge-win-to-ripple-in-its-case-against-the-sec.html); [Reuters](https://www.reuters.com/legal/us-judge-says-sec-lawsuit-vs-ripple-labs-can-proceed-trial-some-claims-2023-07-13/); [CoinDesk](https://www.coindesk.com/markets/2023/07/13/ripples-xrp-token-surges-28-after-court-rules-xrp-sales-arent-investment-contracts).)

**Bitstamp daily** (labeled fallback, not the named Vision row):

| Date (UTC day) | O | H | L | C | `(H−L)/C` |
|---|---:|---:|---:|---:|---:|
| 2023-07-13 | 0.42304 | **0.83783** | 0.42101 | 0.72691 | **57.3%** |
| 2023-07-14 | 0.72649 | 0.73500 | 0.59588 | 0.64136 | **21.7%** |

**Bitstamp 15m (diagnostic path, still not a score):**

- Quiet morning 13 Jul: typical 15m range **<0.3%**.
- Widest 15m: **2023-07-13 18:15 UTC** O 0.71828 / H **0.83783** / L **0.70028** / C 0.75868 — **18.1%** of close in **one** bar. **16** bars that UTC day had 15m range **>5%**.
- 14 Jul widest 15m: **01:00 UTC**, range **7.9%**.

**What PLAN invert is allowed to do those days:**

1. Rails from **prior 96 closed bars only** — 13 Jul morning rails are still the **pre-ruling** 24h. This bar’s high must **not** invent the TP this bar then fills.
2. **At most one fill per lot per bar.** Newly armed opposite **skips** this bar.
3. If both `Lo` and `Hi` of a lot sit in the 18% wick **and** both would be eligible → **`DUAL_TOUCH_SKIP`**, not an 18% round-trip.
4. **Skipped-rung log** (PR 194 checklist): wick tags are not 14 fib prints. Fill-every-rung on this tape **is** the ladder that retired `2bfb1b68`.
5. After a sell-TP: **flat cash**, buy-back only. The 14 Jul fade does **not** authorize a naked short.
6. Paper instant full fill ≠ live queue / relist chaos. Do not mark a +70% open long as gate 1.

**Grind vs spike:** 13 Jul is **not** the fee-grind tape. It is the **skip / path-unknown / inventory** tape. 9097’s death is mostly the **other** 1333 days. Do not skip July to pretty maxDD. Do not invent a July invert return here.

### 10.2 13–14 Nov 2023 wick (same shape, smaller)

USD November close-to-close ~**+1%** hides a wick (PR 194 R10). **Bitstamp daily:** 13 Nov H **0.70082** / L 0.60024 / C 0.62770 (`(H−L)/C` **16.0%**). 14 Nov L **0.55000** / C 0.57917 (`(H−L)/C` **13.4%**).

Widest 15m: **2023-11-13 21:00 UTC** H 0.70082 / L 0.63286 / C 0.64864 — **10.5%** of close. 14 Nov widest **18:45 UTC**, **5.8%**.

Same PLAN allowances as July: one fill per lot, skip newly armed, `DUAL_TOUCH_SKIP` if both prices of a lot are eligible, skipped-rung log, no short on the fade, no invented score. Month-end looking “flat” is not permission to ignore the wick.

---

## Steal vs invert (this memo)

### STEAL (around invert — do not rewrite rungs)

1. Named death row stays **BINANCE-VISION-XRPEUR** close-model **9097 / −99.989999% / 99.990007% / ~1 EUR / fees ~4278**. Clip WAS 200. Rails WERE prior 96. Miss = fill-every-rung 14 pairs. **Not invert.**
2. Bitstamp twin **9069 / same death**, labeled, **not mixed**.
3. Vision **5-bar gap 2023-03-24 12:45–13:45 UTC**. No interpolated prints.
4. Later Kraken dump = **Trades reconstruct** (PR 198 #1) or Drive OHLCVT if obtained. REST 720 still unsatisfiable.
5. Two fill columns: touch vs close-through. 9097 is a third, different, machine.
6. `DUAL_TOUCH_SKIP` default if both sides of one lot would fill. Optional same-venue 1m diagnostic. Adverse-first only as a **named** column.
7. Fee shadow 0.26 / 0.40 / 0.80. Adjacent 0.118-rungs vs 0.52% on public daily ranges.
8. PLAN: clip 200, opposite-fill only, prior-96, sequential 10k, same-bar skip of newly armed.
9. Prints only. 00030 / 00028 are not fills. Do not 20+9097. Do not reseal.
10. Torres / Nov wick = **diagnostics + skipped-rung duty**, not scores.

### HYPOTHESIS (would change invert — **not applied**; not PR 200 H* shipped as invert)

| ID | Change | Class |
|---|---|---|
| **Alt A** | Skip pair if `(Hi−Lo)/Lo` < **1.04%** | Spacing filter. New recipe. |
| **Alt B** | Cap **2** long clips | Labeled live experiment. New 2023 book if used as engine. |
| **Alt C** | **Nearest-2** rungs only | Day-0 experiment. Lock k **before** a window; no search. |
| **Alt D** | Only 24h **H** and **L** | Two-price invert. Specifies rails. |
| PR 200 **H1–H10** | Detector name, rolling fib, close-through swap, WFO of ratios, CPCV drop, maker-fee cheat, depth cap, revive retired hashes, sleeve mix, wrong book | **Do not apply as invert.** |

Any H* / alt that ships belongs on a **new** workspace or a **new** seal. Not on `c9689f5d`. Not on a `dca-paper` reset. Not on live fill 1.

---

## Verdict

**Death print:** fill-every-rung on 15m, 14 pairs, close-model, Vision body. **RED as invert.** Numbers stay ugly. No fake GREEN.

**Fee math:** typical public daily XRPEUR range sits **on the 0.52% knife-edge** for adjacent fibs and **comfortably above** it for the two 24h rails — if you do not spray the stack.

**invert-v2 (still paper):** pair-invert, clip 200, prior-96, opposite-only, `DUAL_TOUCH_SKIP`, two fill columns, Kraken Trades (or OHLCVT) as a **later labeled** dump. Alts A–D stay hypotheses / labeled experiments.

**Promotion: no.** Gate on `invert-paper` remains **NOT MET** (fill 1). `is_fund_gate: false`. Stay paper.

---

## Sources (public URLs)

Sibling packs (this repo / GitHub)

- https://github.com/eyeskull2220/solana-invoice/pull/200 — walk-forward broaden (STEAL vs H1–H10)
- https://github.com/eyeskull2220/solana-invoice/pull/196 — PLAN invert-wf-2023
- https://github.com/eyeskull2220/solana-invoice/pull/198 — XRPEUR 15m paths
- https://github.com/eyeskull2220/solana-invoice/pull/199 — invert walk-forward method
- https://github.com/eyeskull2220/solana-invoice/pull/194 — 2023 slice regimes
- https://github.com/eyeskull2220/solana-invoice/pull/201 — reviewer: 9097 is not invert
- https://github.com/eyeskull2220/solana-invoice/pull/197 — XRPEUR 15m data
- https://github.com/eyeskull2220/solana-invoice/pull/132 — Coder 01 live book
- https://github.com/eyeskull2220/solana-invoice/pull/144 — Coder 02 locks

Fees / tape / fills

- https://www.kraken.com/features/fee-schedule
- https://support.kraken.com/articles/201893638-how-trading-fees-work-on-kraken
- https://docs.kraken.com/api-reference/market-data/get-ohlc-data
- https://docs.kraken.com/api-reference/market-data/get-recent-trades
- https://docs.kraken.com/api-reference/market-data/get-ticker-information
- https://support.kraken.com/articles/360047124832-downloadable-historical-ohlcvt-open-high-low-close-volume-trades-data
- https://www.freqtrade.io/en/stable/backtesting/
- https://cutemarkets.com/blog/same-bar-fills-lookahead-intraday-strategies

Ranges / events (not invert fills)

- https://www.bitstamp.net/api/ — daily + 15m `xrpeur` OHLC used as **labeled** proxy
- https://tradersunion.com/currencies/price-history/xrp-eur/
- https://www.cnbc.com/2023/07/13/xrp-surges-after-judge-delivers-a-huge-win-to-ripple-in-its-case-against-the-sec.html
- https://www.reuters.com/legal/us-judge-says-sec-lawsuit-vs-ripple-labs-can-proceed-trial-some-claims-2023-07-13/
- https://www.coindesk.com/markets/2023/07/13/ripples-xrp-token-surges-28-after-court-rules-xrp-sales-arent-investment-contracts
- https://www.chartscheck.com/monthly-returns-heatmap/kraken/XRP/USD — USD monthly **shape** only (PR 194)

Vision gap

- https://data.binance.vision/data/spot/daily/klines/XRPEUR/15m/XRPEUR-15m-2023-03-24.zip
- https://data.binance.vision/data/spot/monthly/klines/XRPEUR/15m/XRPEUR-15m-2023-03.zip
- https://github.com/binance/binance-public-data

Desk (cite, do not ping / reseal / reset)

- https://dca-paper-journal.surge.sh/

---

## Out of scope (honoured)

- No paper or live Kraken orders  
- No API keys  
- No reseal of `c9689f5d`  
- No `invert-paper` / `dca-paper` reset  
- No invert rung rewrite (alts named, not applied; PR 200 H* not applied)  
- No journal HTML patch, no shop HTML  
- No Phantom spend, no FACTUUR title, no invented KBO  
- No invented 2023 pair-invert equity curve  
- No mixing Vision / Bitstamp / Kraken into one dump  

**Promotion: no.** Stay paper. Gate NOT MET. `is_fund_gate: false`. 9097 is a rejected replay, not fill 8, not invert-v2.
