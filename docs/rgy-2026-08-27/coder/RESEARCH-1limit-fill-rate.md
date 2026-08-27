# RESEARCH — 1-limit fill rate vs fees (XRPEUR 15m)

**Seat:** RESEARCHER (Coder pack)  
**Lens:** fee math + public grid/fib literature. **Not a score. Not a fill. Not CODE.**  
**Date:** 2026-08-27  
**Stamp:** VOORBEELD · paper / simulated · not FACTUUR · not INVOICE · not live-trade advice  
**HEAD (leftover `main` at write):** `2170952`  
**Still paper.** `is_fund_gate: false`. invert-paper fill **1** stays. Do not reseal `c9689f5d`. Do not reset `invert-paper` or `dca-paper`. Do not CODE from [PLAN PR 196](https://github.com/eyeskull2220/solana-invoice/pull/196).

This file answers **expected fill rate** for **ONE nearest-below-close buy + next-higher TP** on 15m XRPEUR, versus two measured exhibits. It does not place orders, paste keys, spend Phantom, rewrite shop HTML, republish the journal, or invent a prettier PnL.

Named next score running **elsewhere:** `INVERT-V2-1LIMIT`. This page does **not** contain that score. Do not wait for it. Do not paste it here. Do not invent it.

---

## 0. Hard locks

| Lock | Meaning |
| --- | --- |
| **Still paper** | Autonomy **level 2**. No `kraken order`. No keys. |
| **Not the fund gate** | `is_fund_gate: false`. Gate stays `invert-paper` only (return > 0 after fees **and** ≥ 8 prints **and** maxDD ≤ 8%). **NOT MET.** |
| **No reseal** | Cite `sha256:c9689f5d7d583320e724900b0ce4ef68193878c880d11939badd1dd59016e390`. Lab clip ≠ this note. |
| **No reset `invert-paper`** | Fill **1** `PAPER-00029` buy XRPEUR **160.64773 @ 1.24496** stays. Resting TP `PAPER-00030` @ **1.26778** is **not** a fill. Open `PAPER-00028` @ **1.23084** is **not** a fill. |
| **No reset `dca-paper`** | Five BTCUSD slices stay held. |
| **Do not CODE from PLAN #196** | Reviewer [#203](https://github.com/eyeskull2220/solana-invoice/pull/203): **RED**. Pairing **every** fib below close is fill-every-rung (`2bfb1b68`). |
| **Do not invent a prettier PnL** | Grind −99.989999% and two-clip −40.84% stay as printed. |
| **Do not apply H\* as invert** | Hypotheses named below are **not** the recipe. **Do not WFO ratios.** |
| **XRPEUR 15m only** | No extra pairs to fatten fills. |
| **VOORBEELD** | Operator: natural person, Geel. **KBO/BTW: nog niet toegekend.** |

**INVERT-V2-1LIMIT (named, not scored here):** invert = **one resting limit**. After fill: **long + one TP**, **not two buys**. Clip **EUR 200**. Fee **0.26%** primary. That is the object of the fill-rate question. Live `00028` extra buy is a **different** posture (two-clip family).

Retired hashes stay retired: `2bfb1b68` fill-every-rung · `9056f296` entry-waits-TP · `094513` arming-only.

---

## 1. Measured exhibits (STEAL — do not replace)

These cells are **already printed**. This file does not restamp them, blend them, or turn them into a 1-limit equity curve.

### 1.1 Rejected grind (not invert)

| Cell | Value |
| --- | --- |
| Model | **close-model · fill-every-rung** |
| Fills | **9097** |
| Return after fees | **−99.989999%** |
| End | **1 EUR** |
| Fees | **4278** |
| Fingerprint | 100% equity / dust floor / not invert |

Review: [PR #201](https://github.com/eyeskull2220/solana-invoice/pull/201). Window cited there: **BINANCE-VISION-XRPEUR + Kraken tail**, **n = 128142** bars, 2023-01-01 → now, one 5-bar gap 2023-03-24. Venue is **not** the 1-limit question; the fill **count** is the ladder ceiling on that tape.

`(1 - 0.0026)^n × 10000 = 1` ⇒ **n ≈ 3538** fills to dust on 100% remaining equity. 9097 > 3538: the book **hit the floor and kept spraying**. Ending **exactly 1.00** is a min-equity halt, not invert PnL. Reviewer arithmetic: 9097 × 0.26% × EUR 200 ≈ **4730 EUR** fees — a **clipped** book cannot reach 1.00 from fees alone. Dust requires all-in.

### 1.2 Day-0 TWO-CLIP exhibit (not invert)

| Cell | Value |
| --- | --- |
| Model | **not invert** (two concurrent buys) |
| Fills | **7923** |
| Return after fees | **−40.84%** |
| maxDD | **41.08%** |
| End | **5916** |
| Fees | **4120** |
| `price_pnl` | **+36** |
| Max concurrent limits | **2** |
| First bar | **2 buys** |
| Fills/year | **2260 / 2338 / 1983 / 1342** (2023 / 2024 / 2025 / 2026-to-now) |
| Mean hold | **47.6 bars (~12 h)** |
| Median hold | **13 bars (~3.25 h)** |
| Clip | EUR 200 (fee identity below) |
| Fee | 0.26% per print |

**Fee identity (re-check, not a new score):**

```text
7923 × 200 × 0.0026 = 7923 × 0.52 = 4119.96 ≈ 4120
10000 + 36 − 4120 = 5916
(5916 − 10000) / 10000 = −0.4084 = −40.84%
2260 + 2338 + 1983 + 1342 = 7923
```

`price_pnl +36` with fees **4120** is the mill: the tape almost paid **zero** net of the clip; **churn** took the book. maxDD **41.08%** is the same crash with a slightly higher peak. Do not replace these cells with a 1-limit restatement.

**Year rate (STEAL counts / calendar, not a 1-limit forecast):**

| Slice | Fills | Calendar days (approx.) | Fills/day |
| --- | ---: | ---: | ---: |
| 2023 | 2260 | 365 | **6.19** |
| 2024 | 2338 | 366 | **6.39** |
| 2025 | 1983 | 365 | **5.43** |
| 2026-to-now | 1342 | ~239 (1 Jan → 27 Aug) | **5.61** |
| Combined | 7923 | ~1335 | **~5.9** |

Grind on the same sitting’s window: 9097 / ~1334 d ≈ **6.8 fills/day**. Two-clip vs grind cut **1174 fills (~13%)**, not an order of magnitude. Capping concurrent at **2** barely moved **count** vs the ladder. It moved **size** (clip 200 vs 100% equity): end **5916** vs end **1**.

### 1.3 Live invert-paper (different book — do not mix)

| Id | Role | Price | Gate fill? |
| --- | --- | --- | --- |
| **PAPER-00029** | FILL 1 · buy 160.64773 | **1.24496** | **Yes. Count = 1.** |
| **PAPER-00030** | Resting TP · sell LIMIT | **1.26778** (24h H) | No |
| **PAPER-00028** | Open buy LIMIT | **1.23084** | No |

Live after fill 1 is **long + TP + one extra lower buy**. That is the **two-clip shape**, not V2-1LIMIT. Gross 1.24496 → 1.26778 = **+1.833%**. Two 0.26% = **0.52%**. That **one hypothetical** still would be **2 < 8**. Do not write it into a scoreboard ([#132](https://github.com/eyeskull2220/solana-invoice/pull/132)).

### 1.4 Sealed lab clip (cite, do not reseal, do not scale)

`fib-grid-invert-xrpeur-15m` · 2026-08-18 21:00 → 2026-08-26 08:00 Europe/Brussels · **20 fills** · +0.681154% · maxDD 0.890854% · PASS vs `c9689f5d`.

20 / 8 d = **2.5 fills/day**. Applying 2.5 × ~1334 d ≈ **3335** fills to 2023–now is **HYPOTHESIS** (quiet 8-day window ≠ Torres July). Named in §7 as **H-FR2**. Do not apply as invert.

---

## 2. What “1-limit” is (so fill-rate has a meaning)

Method pack [#199](https://github.com/eyeskull2220/solana-invoice/pull/199) L4 and REVIEW-05 [#203](https://github.com/eyeskull2220/solana-invoice/pull/203) D1 already wrote the invert pair. This page uses the **stricter** V2-1LIMIT reading the operator named:

| Inventory | Armed | Not armed |
| --- | --- | --- |
| Flat EUR | **one** buy LIMIT at nearest buy-eligible rung **below** last close | every other buy; any sell |
| Long (after that buy) | **one** sell LIMIT at the paired TP | re-arm entry; pyramid; **second buy** |

**Not this object:**

- PLAN #196 §4.4 “pair **each** buy rung below close” — fill-every-rung. **Do not CODE.**
- Two-clip / live `00028` extra buy — first bar **2 buys**.
- Close-model grind — fill at close, 100% equity.

**Clock (STEAL from #199 / #196 prose, not the #196 arming table):** closed 15m bars; rails from prior 96 bars (exclude `i`); new order eligible from `t+1`; fill at **limit** if `[low, high]` tags it; same-bar both-sides → skip (`DUAL_TOUCH_SKIP` / `SAME_BAR_REARM`); spot no naked short; after sell-TP, flat cash, buy-back.

**TP in the question:** “next-higher” unique fib on the **24h range**. That is **adjacent-rung TP**, not live `00030` = 24h **H**. Fee section §4 is about **that** pairing. Live rail-H TP is a **different** gap (1.83% on fill 1) and is **not** this mill.

---

## 3. Q1 — Expected fill rate vs 7923 and 9097

**No fake curve.** Public grid literature plus the two exhibits. One number for “1-limit fills 2023–now” would be a score. This file has **none**.

### 3.1 What the literature actually says

Grid bots are **inventory market-making with N posted levels**. Fill **count** scales with **how many levels are working**, not with Fibonacci labels.

- More grids ⇒ tighter spacing ⇒ **more fills** ⇒ **more round-trip fees**. Per-cycle gross is the **grid rate** (gap / price). Net = `capital_per_grid × (grid_rate − 2 × fee)`. If `grid_rate < 2 × fee`, every completed cycle **loses**. ([VoiceOfChain grid profit](https://voiceofchain.com/academy/grid-bot-profit-calculation); [Dexly: grid trading](https://dexly.trade/learn/grid-trading-crypto); [Binance grid params](https://dp-binance.com/en/docs/grid-bot-optimal-params.html); [NovaCalculator spacing floor](https://www.novacalculator.com/crypto-web3/trading/crypto-grid-bot-calculator/))
- Practitioners’ rule of thumb (not a WFO target): spacing **3–5×** round-trip fee, or at least **clear 2× fee**. At primary **0.26%** that is **0.52%** RT, so a “comfortable” geometric step is **~1.5–2.6%** — **HYPOTHESIS** if used to retune invert rungs (**H-FR3**). The **floor** (do not arm below 0.52%) is fee **identity**, not a tuned ratio.
- Geometric vs arithmetic: geometric keeps **percent** gap constant (crypto-default). Fib retracements **are** a geometric-ish partition of a range. They are **not** a bounce oracle. Tsinaslanidis, Guijarro & Voukelatos (ESWA 2022): bounce probability on Fibonacci zones is **statistically indistinguishable** from non-Fibonacci zones; a Fibonacci trading rule does **not** beat random levels. ([ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0957417421012495); [open PDF](https://riunet.upv.es/server/api/core/bitstreams/07add8c4-4239-44e7-bf1f-93d66108918d/content))
- Hummingbot `GridExecutor` state machine is **one level at a time per executor**: `OPEN_ORDER_PLACED → OPEN_ORDER_FILLED → CLOSE_ORDER_PLACED → COMPLETE`. N executors ⇒ N concurrent opens. **1-limit is N = 1.** ([GridExecutor](https://hummingbot.org/strategies/v2-strategies/executors/gridexecutor/))
- Freqtrade / CuteMarkets / Backtrader: a **standing** limit may fill on a later bar’s range; a **newly armed** order does not fill the arm bar. ([Freqtrade backtesting](https://www.freqtrade.io/en/stable/backtesting/); [CuteMarkets same-bar](https://cutemarkets.com/blog/same-bar-fills-lookahead-intraday-strategies); sibling [#200](https://github.com/eyeskull2220/solana-invoice/pull/200))

**STEAL:** fill count ~ **active levels × oscillation crossings**. Fib ratios do not add extra fills beyond the **geometry of the gaps**.  
**Do not steal:** “fib 0.618 fills more than a random rung” as a rate model.

### 3.2 Structural bounds (identities, not a score)

Let `N_bar = 128142` (grind window, order of magnitude for 2023-01-01 → 2026-08-27 15m). 1-limit + same-bar lock ⇒ **at most one print per bar**.

| Bound | Fills | What it is |
| --- | ---: | --- |
| Hard cap (1 fill / bar) | **128142** | Clock ceiling. Not expected. |
| Grind (fill-every-rung close-model) | **9097** | STEAL ladder ceiling on that tape |
| Two-clip (max concurrent **2**, first bar 2 buys) | **7923** | STEAL 2-slot count. **Not invert.** |
| Half of two-clip if slots independent | **3962** | **H-FR1** — do not apply as invert |
| Always-long at STEAL **mean** hold 47.6 bars | `2 × 128142 / 47.6 ≈ 5384` | Occupancy identity **if** never flat-waiting. Not a score. Uses two-clip hold, not 1-limit hold. |
| Same identity at **median** 13 | `2 × 128142 / 13 ≈ 19714` | **Impossible** vs 7923. Median is the typical **completed** hold, not occupancy. **Do not use.** |
| Lab 2.5/day × ~1334 d | **~3335** | **H-FR2** — 8-day clip scaled. Do not apply. |

**What 1-limit is allowed to do to count:**

1. **Cannot exceed the grind ladder** (9097) on the same tape without filling rungs it does not arm. A wick through 18 fibs is **one** touch of the **resting** price, not 18 prints (§5).
2. **Cannot print first-bar 2 buys.** Two-clip’s day-0 tell is forbidden. That alone removes the **stack**, not necessarily half the multi-year count.
3. **Should sit at or below 7923.** Two-clip already had only 2 slots and still printed 7923. One slot has **less** capacity to harvest the same oscillations. Capital lock of 2×200 EUR on a 10k book is only 4% — 1-limit does **not** free a trapped book the way going 100% → clip 200 did. So 1-limit is **unlikely** to print *more* than 7923.
4. **Two-clip vs grind was only −13% fills.** The ladder’s extra 1174 prints were **deeper rungs**. Going 50 rungs → 2 rungs barely cut **count**. Going **2 → 1** cuts the **remaining parallel stream**. That cut is **real** (no double-buy bars) and **not** 13%. It is also **not proven to be 50%** (the two clips share one path; they are not two independent Poisson clocks).

**Honest statement (no invented n):** 1-limit fill count on this window is **expected below 7923 and far below 9097**, with a **plausible occupancy band** between “always-long at mean hold” (~5k prints **if** hold times transfer) and “half the two-clip stream” (~4k **if** slots were independent). **Neither band is a score.** `INVERT-V2-1LIMIT` running elsewhere prints the number. This page does not.

**Fills/year shape:** two-clip stayed **~5.4–6.4/day** every year. A 1-limit that still arms **next-fib TP** in chop will still print **every year**. It will not go quiet in 2025 just because concurrent size is 1. Year **shape** (2024 peak, 2025 dip, 2026 partial) is a **tape** fact (STEAL). Scaling those years by 1/2 is **H-FR1**.

---

## 4. Q2 — Can a completed 1-limit round trip beat 0.52% RT?

Primary fee **0.26%** per print. Round-trip = two prints. Paper engine lock (journal shadow): `0.26=0.52; 0.40=0.80; 0.80 taker=1.60`.

Public Kraken Pro **this sitting** (cross-platform, 9 Jul 2026): Tier 1 **0.40% maker / 0.80% taker**. ([Fee schedule](https://www.kraken.com/features/fee-schedule); [cross-platform tiers](https://support.kraken.com/gb/articles/cross-platform-fee-tier-changes)). Paper still scores **0.26** primary and **shadows** 0.40 / 0.80. Do **not** relabel 0.26 as proof of live maker fills. Do **not** switch the engine to maker because “grids make” (**H6** in [#200](https://github.com/eyeskull2220/solana-invoice/pull/200)).

### 4.1 Break-even identity (clip EUR 200, primary 0.26%)

Long round-trip: buy quote **200** at `Lo`, sell the same qty at `Hi`. Let `r = Hi / Lo`.

```text
buy_fee  = 0.0026 × 200
sell_fee = 0.0026 × 200 × r
gross    = 200 × (r − 1)
net      = 200(r − 1) − 0.52(1 + r)

net > 0  ⇔  r > 200.52 / 199.48  = 1.00521356
         ⇔  (Hi − Lo) / Lo > 0.521356%
```

**Arm gate (fee identity, not a WFO ratio):** if `(Hi − Lo) / Lo < 0.52%` (use **0.521356%** at 0.26%), **do not arm the pair**. A completed round trip **cannot** beat 0.52% RT. Completing it is the mill.

Shadows (same clip, same identity, not a retune):

| Column | Per fill | RT | Break-even `(Hi−Lo)/Lo` |
| --- | ---: | ---: | ---: |
| Primary 0.26% | 0.26% | **0.52%** | **0.5214%** |
| Shadow 0.40% | 0.40% | **0.80%** | **0.8032%** |
| Shadow 0.80% | 0.80% | **1.60%** | **1.6129%** |

Live fill-1 pair 1.24496 → 1.26778: `(Hi−Lo)/Lo = 1.833%` **clears** 0.52% and 0.80%; **clears** 1.61% only barely. That TP is **24h H**, not next fib. Do not cite it as proof next-fib works.

### 4.2 Next fib on a 24h range

Locked retracements on range `R = H − L`: gaps as a **fraction of R**:

| Adjacent pair (α) | α = Δ / R |
| --- | ---: |
| 0 ↔ 0.236 | 0.236 |
| 0.236 ↔ 0.382 | 0.146 |
| **0.382 ↔ 0.5** | **0.118** |
| **0.5 ↔ 0.618** | **0.118** |
| 0.618 ↔ 0.786 | 0.168 |
| 0.786 ↔ 1 (rail) | 0.214 |

Tightest next-fib step: **α = 0.118**.

```text
(Hi − Lo) / Lo = (α × R) / Lo = α × (R / Lo)
```

`Lo` is at or above `L`, so `R / Lo ≤ (H − L) / L` (24h range as % of the low). Next-fib **cannot** beat 0.52% when:

```text
α × (R / Lo) < 0.00521356
R / Lo      < 0.00521356 / α
```

| α (next fib) | 24h `R/Lo` below which **do not arm** (primary 0.26%) |
| ---: | ---: |
| 0.118 (tightest) | **< 4.42%** |
| 0.146 | **< 3.57%** |
| 0.168 | **< 3.10%** |
| 0.214 | **< 2.44%** |
| 0.236 | **< 2.21%** |

**When is `(Hi−Lo)/Lo < 0.52%` so the pair should not arm?**

1. **Always, as a price check**, before posting: compute `Hi` and `Lo` ticks, refuse if `Hi/Lo − 1 < 0.00521356`. This does **not** search α. It applies the locked fee to the locked pair.
2. **On a quiet 24h tape**, next-fib is **usually** under the floor. A 2% 24h range × α 0.118 = **0.236%** gross ≪ 0.52%. September 2023 (USD month ~+0.8%, [#194](https://github.com/eyeskull2220/solana-invoice/pull/194) R8) is the named fee-grind month. Two-clip still printed **~6 fills/day** through 2023 — including that chop. Next-fib 1-limit **will still arm and lose** unless the gate in (1) is on.
3. **On a wide 24h tape**, next-fib *can* clear 0.52% (24h range ≳ 4.4% at α 0.118). Clearing the **fee** does not clear **gate 1** (need the TP to **print**), **gate 2** (need ≥ 8), or **gate 3** (maxDD ≤ 8%). It only says that **one** completed RT is not automatically negative.

**Can a completed 1-limit RT beat 0.52% if TP is next fib on a 24h range?**  
**Yes, only when the adjacent gap itself is > 0.52% of `Lo`.** That is a **property of that day’s rails**, not of “invert.” On typical XRPEUR 24h ranges of a few percent, **tightest fibs fail the identity**. Public grid docs call that “spacing inside the fee.” Fibonacci labels do not rescue it (ESWA 2022: fib bounce = random bounce).

**Do not WFO** a minimum 24h range, a skipped-α list, or “use 0.618 only” on 2023–2026 so the mill disappears. That is **H-FR3** / **H4** (Pardo WFO of ratios). New book, new hash, still paper — not a reseal, not this page.

---

## 5. Q3 — Spike days: one limit vs a stack of prints

[#194](https://github.com/eyeskull2220/solana-invoice/pull/194) already named the days. Coder skipped-rung log (after a **later** replay — **not invented here**): **2023-07-13, 07-14, 11-13, 11-14, 06-06, 03-10**. This page states what **1-limit is allowed to do**. It does not fill the log.

### 5.1 2023-07-13 Torres

U.S. District Judge Analisa Torres, **2023-07-13**: programmatic exchange sales of XRP **not** investment contracts; institutional sales **were**. Reuters: XRP **+75%** that afternoon. ([Reuters](https://www.reuters.com/legal/us-judge-says-sec-lawsuit-vs-ripple-labs-can-proceed-trial-some-claims-2023-07-13/); [CNBC](https://www.cnbc.com/2023/07/13/xrp-surges-after-judge-delivers-a-huge-win-to-ripple-in-its-case-against-the-sec.html))

Pound Sterling Live daily EUR (regime only, **not** Kraken 15m fills — [#194](https://github.com/eyeskull2220/solana-invoice/pull/194)): 12 Jul close **0.4232** → 13 Jul high **0.8308** / close **0.7266** (open-to-high **~+96%**). 14 Jul fade low **0.5966**. Aggregators disagree on the annual high; **venue 15m is truth**. Do not launder Source A into a print.

### 5.2 2023-11-13 wick

Same shape, smaller. Source A: 13 Nov high **0.7004** / close **0.6275**; 14 Nov low **0.5505**. USD November ~+1% **hides** the wick. Do not skip the week because the month % is ~1.

### 5.3 What ONE limit may print

Assume a buy LIMIT was **already resting** from a **prior** bar (L2 / CuteMarkets standing-order rule).

| Event on the spike 15m | 1-limit (V2) | Ladder / two-clip / grind |
| --- | --- | --- |
| Wick tags the resting `Lo` | **At most one buy** at `Lo` | Every tagged `Lo` below the wick |
| Same bar also tags `Hi` / extensions | **`DUAL_TOUCH_SKIP` / same-bar lock:** newly armed TP **does not fill**. Do **not** credit a RT inside one candle. OHLC has no path. | Close-model grind **does** double-print (9097 tell) |
| Wick traverses 0.236 … 2.618 both sides | **Skipped-rung log.** Tags ≠ prints. | Fill-every-rung = **stack of prints** |
| Next bars | One TP working. **No second buy.** | Two-clip may still have the extra buy (`00028` / first-bar 2 buys) |
| Fade day (14 Jul / 14 Nov) | May fill the **one** TP if it was armed from `t+1` and tagged. Still one lot. **No naked short.** | Ladder sells / leftover longs from the stack |

**Skipped-rung honesty:** a 15m that opens or wicks **through** a level without a **resting** order at that level is **not** a fill. Paper instant-full-size is already optimistic vs live queue (Uphold “high demand” 13 Jul — [#194](https://github.com/eyeskull2220/solana-invoice/pull/194)). Counting wick tags as 18 fib prints is the grind. **1-limit’s job on Torres is to stay boring: 0 or 1 print that bar, then a list of skipped rungs.**

Do **not** skip 13 Jul to pretty maxDD. Do **not** invent the skipped-rung list from daily EUR. Do **not** mark +70% MTM as gate 1.

---

## 6. Q4 — Median 13 vs mean 12 h: churn vs size; does 1-limit cut fills?

Two-clip STEAL: **median hold 13 bars (~3.25 h)**, **mean 47.6 bars (~12 h)**. Right-skew: most completed RTs are **short**; a long tail of stuck inventory pulls the mean to half a day.

### 6.1 Two fee deaths (do not conflate)

| Death | Mechanism | Two-clip evidence | Grind evidence |
| --- | --- | --- | --- |
| **Churn** | Many short RTs whose gross `< 0.52%` | **4120** fees; `price_pnl +36`; median **13** bars; end **5916** | Extra prints from the ladder |
| **Size** | Notional per fill / concurrent lots / 100% equity | Max concurrent **2 × 200 = 400 EUR** (4% of 10k). **Not** the 41% DD. | **100% remaining equity** → end **1** |

**Identity:** 41% DD on two-clip ≈ fees **4120** / 10000. Concurrent size 400 EUR cannot produce a 4100 EUR hole without **turnover**. The hole is **count × 0.52 EUR**. Median 13 bars is **how** that count happens: next-fib (or adjacent) gaps in chop complete fast and **pay the fee twice**.

Mean 12 h is the **other** tape: trend / spike leftover (July 13 long, August fade — [#194](https://github.com/eyeskull2220/solana-invoice/pull/194) R6–R7). That is **inventory time**, not extra fills. 1-limit **does** cap how much inventory you hold (**200 not 400**, **not 100%**). It does **not** shorten the Torres hang.

### 6.2 Does 1-limit cut concurrent size? Yes.

V2-1LIMIT: one clip **200**. Never two buys. Never leftover-cash resize. REVIEW-05 Y1: skip if `cash < 200 × 1.0026`. That **kills the grind’s size death**. Two-clip already had clip 200 and still lost **40.84%** — because **churn** remained.

### 6.3 Does 1-limit cut fill count? Partially, not by magic.

| Cut | Why | How much |
| --- | --- | --- |
| No first-bar 2 buys | Structural | Removes **stacked** opens. Multi-year effect **unmeasured** (not a score). |
| No parallel clip | One stream vs two | **≤ 7923**. Not proven = 3962 (**H-FR1**). |
| No deep ladder | Already true of two-clip | Two-clip vs grind was only **−13%** fills. 1-limit does not re-win that 13%; it is already not the grind. |
| Next-fib still armed in chop | Median 13 remains available | **Count stays high** unless the **0.52% arm gate** is on. The gate cuts **bad** RTs, which **is** a fill cut, and is **fee identity**, not WFO. |
| Same-bar skip on spikes | One print, not a stack | Torres / 11-13: honesty, not a yearly 2×. |

**Bottom line:** 1-limit **cuts concurrent size**. It **cuts fill count** only where the second clip was actually printing (day-0 2 buys, parallel harvest) and where skipped-rung honesty refuses a stack. It **does not**, by itself, stop **churn death** if TP stays **next fib** inside a 24h range `< ~4.4%` at α 0.118. Two-clip already proved: clip 200 + two slots + 7923 fills = **−40.84%** with **+36** price PnL.

---

## 7. Q5 — STEAL vs HYPOTHESIS

Sibling method [#200](https://github.com/eyeskull2220/solana-invoice/pull/200): **STEAL** clock / tape / confirmation / scoring / fee shadow / print-not-tag. **H1–H10** would **change invert** — flagged, **not applied**. This page adds fill-rate IDs. **Do not apply H\* as invert. Do not WFO ratios.**

### STEAL (use around invert — do not rewrite rungs)

| ID | Steal | Source |
| --- | --- | --- |
| S1 | Grind cells **9097 / −99.989999% / end 1 / fees 4278** stay. Not invert. | This prompt / #201 |
| S2 | Two-clip cells **7923 / −40.84% / maxDD 41.08% / end 5916 / fees 4120 / price_pnl +36 / max concurrent 2 / first bar 2 buys / 2260·2338·1983·1342 / mean 47.6 / median 13** stay. Not invert. | This prompt |
| S3 | Fee identity `fills × 200 × 0.0026` on two-clip. Churn, not size. | Arithmetic |
| S4 | Fill count scales with **active levels**; spacing must clear **2× fee**. | Grid literature §3.1 |
| S5 | Fib bounce ≠ extra fill edge vs random levels. | ESWA 2022 |
| S6 | Standing limit may fill later bar; new order skips arm bar; dual-touch skip. | Freqtrade / CuteMarkets / #199 |
| S7 | `(Hi−Lo)/Lo < 0.521356%` ⇒ do not arm. Identity at 0.26% × 2, clip 200. | §4.1 |
| S8 | Spike days: 1-limit ≤ 1 print / bar; skipped-rung log; no stack. | #194 / §5 |
| S9 | Median 13 = churn clock; mean 47.6 = stuck-inventory clock. Do not use median as occupancy. | §6 |
| S10 | `is_fund_gate: false`. invert-paper fill **1**. No reseal. No `dca-paper` reset. No CODE from #196. | Locks |
| S11 | Engine 0.26 + shadows 0.40 / 0.80. Public Tier 1 is 0.40 / 0.80. | Kraken fee page / journal |
| S12 | Calendar OOS slices of a **frozen** recipe ≠ Pardo WFO of ratios. | #200 / Pardo |

### HYPOTHESIS (would change invert or invent a score — **not applied**)

| ID | Hypothesis | Why it is not this page |
| --- | --- | --- |
| **H-FR1** | 1-limit fills = 7923 / 2 = 3962 | Independent-slot assumption. Two clips share one path. |
| **H-FR2** | Lab 2.5 fills/day × 2023–now ≈ 3335 | 8-day clip is not walk-forward. Do not reseal. |
| **H-FR3** | WFO min 24h range / skip tight α / “only 0.618” so 2023 looks green | Pardo search of ratios. **H4** in #200. PBO. New hash if ever shipped. |
| **H-FR4** | Treat two-clip 7923 as invert | First bar **2 buys**. V2-1LIMIT forbids that. |
| **H-FR5** | Scale two-clip PnL to 1-limit (halve fees, keep +36, write −20%) | Invented prettier PnL. Forbidden. |
| **H-FR6** | CODE PLAN #196 “pair each fib below close” as 1-limit | Reviewer RED. Fill-every-rung. |
| **H-FR7** | Use median 13 as occupancy ⇒ ~20k fills | Contradicts 7923. |
| **H1** | Name Williams-5 / N-bar as **the** rail detector | #200. Specifies invert. Flag only. |
| **H3** | Require close-through before swap | Changes fill count vs wick-touch. |
| **H4** | True WFO of which fib ratios survive each year | New recipe. |
| **H6** | Maker-fee engine without a queue | Scoring cheat. |
| **H8** | Revive `2bfb1b68` / `9056f296` / `094513` | Retired. |

Any H\* that ships belongs on a **new** workspace or a **new** seal. Not on `c9689f5d`. Not on a `dca-paper` reset. Not on `invert-paper` fill 1.

---

## 8. What this means for `INVERT-V2-1LIMIT` (still not a score)

The named next score should, when it exists, be readable against this page **without** this page changing:

1. **`is_fund_gate: false`.** Live gate remains fill **1**.
2. **One resting limit.** After buy: long + one TP. **Fail** if first bar has 2 buys (two-clip tell).
3. **Clip 200 hard.** Fail `FULL_EQUITY_SIZE` / grind fingerprint (end ≤ €100 with fills ≥ 1000, or close-model). Do not replace −99.989999%.
4. **Arm gate:** skip pair if `(Hi−Lo)/Lo < 0.521356%` at primary 0.26%. Report how many candidates the gate refused. That is **not** a WFO of α.
5. **Skipped-rung log** on 2023-07-13 / 07-14 / 11-13 / 11-14 / 06-06 / 03-10. Wick tags are not prints.
6. **Three fee columns.** Do not switch to maker.
7. **Do not CODE from #196.** If a PLAN rewrite greens D1 (`MAX_OPEN_BUY_LOTS` / one pair), that is a **different** PLAN PR. This research does not start CODE.

If that score prints **~7923** fills with **two** buys on bar 1, it is **not** V2-1LIMIT. If it prints **~9097** and end **1**, it is the grind. If it prints a pretty curve without the arm-gate and without skipped rungs, it is a **prettier PnL**. Reject it.

---

## 9. Verdict

| Probe | Result | Color |
| --- | --- | --- |
| 1-limit expected fills vs 7923 / 9097 | **Below both**, not a single n. Ladder 9097 is the ceiling; two-clip 7923 is the 2-slot STEAL; 1-slot is **not proven = half**. | **YELLOW** (unscored) · **GREEN** (no fake curve) |
| Next-fib RT vs 0.52% | **Only if** `(Hi−Lo)/Lo > 0.5214%`. Tightest α=0.118 needs 24h `R/Lo ≳ 4.42%`. Else **do not arm**. | **GREEN** (identity) |
| Torres / 11-13 | One standing limit: **0 or 1 print**; skipped-rung log; no stack; no same-bar RT. | **GREEN** (rule) |
| Median 13 vs mean 12 h | Churn vs stuck inventory. 1-limit **cuts size**; **cuts count only** where the second clip / stack was printing. Next-fib still churns. | **GREEN** (split) |
| STEAL vs H\* | H-FR1–7 and #200 H1/H3/H4/H6/H8 **not applied**. No WFO. | **GREEN** |
| Promotion / fund gate | **RED** — fill 1, NOT MET | **RED** |
| CODE from PLAN #196 | **RED** — do not start | **RED** |
| Invented 1-limit PnL | **Not done** | **GREEN** |
| invert-paper / `c9689f5d` / `dca-paper` | Untouched | **GREEN** |

**Promotion: no.** Stay paper. `INVERT-V2-1LIMIT` is a named book **elsewhere**, not this markdown, not the fund gate.

---

## 10. This sitting

| Did | Did not |
| --- | --- |
| Wrote fill-rate research from public grid/fib literature + fee identities | Replay, fetch OHLCVT, place orders |
| Left grind −99.989999% and two-clip −40.84% unreplaced | Invent a 1-limit equity curve |
| Named H-FR\* / pointed at #200 H\* | Apply H\* as invert / WFO α |
| Stamped `is_fund_gate: false` | CODE from PLAN #196 |
| | Reseal `c9689f5d` / reset `invert-paper` / reset `dca-paper` |
| | Keys, Phantom, FACTUUR, shop HTML, journal ping |

Kraken MCP this VM: **error / undiscoverable**. No `kraken` CLI. Public fee page cited; no private API.

---

## Sources

Grid / fees / fib

- https://voiceofchain.com/academy/grid-bot-profit-calculation
- https://dexly.trade/learn/grid-trading-crypto
- https://dp-binance.com/en/docs/grid-bot-optimal-params.html
- https://www.novacalculator.com/crypto-web3/trading/crypto-grid-bot-calculator/
- https://hummingbot.org/strategies/v2-strategies/executors/gridexecutor/
- https://www.freqtrade.io/en/stable/backtesting/
- https://cutemarkets.com/blog/same-bar-fills-lookahead-intraday-strategies
- https://www.sciencedirect.com/science/article/abs/pii/S0957417421012495
- https://riunet.upv.es/server/api/core/bitstreams/07add8c4-4239-44e7-bf1f-93d66108918d/content
- https://www.kraken.com/features/fee-schedule
- https://support.kraken.com/gb/articles/cross-platform-fee-tier-changes
- https://support.kraken.com/articles/201893638-how-trading-fees-work-on-kraken

Spike day (public)

- https://www.reuters.com/legal/us-judge-says-sec-lawsuit-vs-ripple-labs-can-proceed-trial-some-claims-2023-07-13/
- https://www.cnbc.com/2023/07/13/xrp-surges-after-judge-delivers-a-huge-win-to-ripple-in-its-case-against-the-sec.html

Desk (cite, do not reseal / reset / CODE)

- https://dca-paper-journal.surge.sh/
- https://github.com/eyeskull2220/solana-invoice/pull/196 — PLAN invert-wf-2023 (**do not CODE**)
- https://github.com/eyeskull2220/solana-invoice/pull/203 — REVIEW-05 PLAN **RED**
- https://github.com/eyeskull2220/solana-invoice/pull/201 — grind score **RED** / not invert
- https://github.com/eyeskull2220/solana-invoice/pull/199 — invert method pack (1 resting limit)
- https://github.com/eyeskull2220/solana-invoice/pull/200 — STEAL vs H1–H10
- https://github.com/eyeskull2220/solana-invoice/pull/194 — 2023 slice / Torres / skipped-rung checklist
- https://github.com/eyeskull2220/solana-invoice/pull/132 — Coder 01 live fill 1
- https://github.com/eyeskull2220/solana-invoice/pull/144 — Coder 02 invert-only gate
- https://github.com/eyeskull2220/solana-invoice/pull/118 — CODER seat

---

## Re-check (copy/paste)

```bash
# This pack must exist and must not contain a fake 1-limit PASS:
rg -n 'is_fund_gate|7923|9097|0\.521|H-FR|INVERT-V2-1LIMIT|do not CODE' \
  docs/rgy-2026-08-27/coder/RESEARCH-1limit-fill-rate.md

# Fee identity on the two-clip STEAL:
python3 -c "print(7923*200*0.0026, 10000+36-4120, (5916-10000)/10000, 2260+2338+1983+1342)"

# Break-even r:
python3 -c "print(200.52/199.48-1)"

# Live gate book — expect fill 1, not 7923:
curl -sS https://dca-paper-journal.surge.sh/ | rg -n 'fills|PAPER-00029|NOT MET|c9689f5d|invert-paper'

# Never:
# kraken paper reset --workspace invert-paper
# kraken paper reset --workspace dca-paper
# kraken order …
```

**Promotion: no.** Stay paper. Do not reseal `c9689f5d`. Do not reset `invert-paper`. Do not CODE from PLAN PR 196. Do not invent a prettier PnL. `INVERT-V2-1LIMIT` prints elsewhere. This file is research only.

End. RESEARCHER. Docs only. `is_fund_gate: false`. invert-paper fill 1 stays. Still paper.
