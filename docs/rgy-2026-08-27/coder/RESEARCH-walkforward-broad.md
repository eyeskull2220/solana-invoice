# RESEARCH — Walk-forward a 15m grid/fib invert from 2023 without lookahead

**Seat:** RESEARCHER · Coder  
**Lens:** start **simple**, then **broaden** because the simple trail is thin for this job. Docs only.  
**Date:** 2026-08-27  
**Stamp:** VOORBEELD · paper / simulated · not FACTUUR · not INVOICE · not live-trade advice  
**HEAD (this repo):** `2170952`  
**Still paper.** `invert-paper` stays. `dca-paper` stays. Do not reseal `c9689f5d`.

This file answers: **how people actually walk-forward a 15-minute grid / Fibonacci invert from 2023 without lookahead** — not only our recipe. It does not place orders, paste keys, reseal the lab clip, reset `dca-paper`, or rewrite invert.

---

## Locks (this sitting)

| Lock | Status |
|---|---|
| Still paper | **GREEN** — no orders, no keys |
| `invert-paper` stay | **GREEN** — named gate book, not rewritten |
| `dca-paper` stay | **GREEN** — five BTCUSD slices held |
| Do not reseal `c9689f5d` | **GREEN** — cited, not rotated |
| 8-day lab clip as 2023 walk-forward | **RED** — that clip is 2026-08-18 → 2026-08-26, not 2023 |
| Promotion / live / 10k as deposit | **RED** |

Live book (operator / journal, not this file's job to ping): fill **1** `PAPER-00029` buy XRPEUR @ 1.24496. Resting TP `PAPER-00030` @ 1.26778 is **not** a fill. Open `PAPER-00028` @ 1.23084 is **not** a fill. Gate (return > 0 after fees **and** ≥ 8 prints **and** maxDD ≤ 8%) is **NOT MET**.

Sealed lab clip (cite only): name `fib-grid-invert-xrpeur-15m`, window 2026-08-18 21:00 → 2026-08-26 08:00 Europe/Brussels, 20 fills, +0.681154%, maxDD 0.890854%, vs `sha256:c9689f5d7d583320e724900b0ce4ef68193878c880d11939badd1dd59016e390`. That is **not** a walk-forward from 2023.

Invert recipe (journal, unchanged here): 15m; full fib set — retracements 0.236 / 0.382 / 0.5 / 0.618 / 0.786 + extensions 1.272 / 1.618 / 2.0 / 2.618 both sides; every level a rung; after **any** fill swap jobs of those two prices; re-arm only on the opposite fill; spot no naked short.

---

## Method of this paper

1. **Simple first:** bar-close replay + resting limits. That is the industry default for 15m OHLC grids.
2. **Broaden when thin:** the simple trail tells you *how to step bars*. It does **not** tell you how to pick fib rails without seeing the future, how to score 2023–2026, how a wick fill differs from a close fill, or what XRPEUR actually costs. Those are the sections people actually argue about.
3. **Steal vs invert:** each public trick is tagged **STEAL** (use around invert, do not rewrite the recipe) or **HYPOTHESIS** (would change invert — flagged, not applied).

---

## 1. Simple first — bar-close replay + resting limits

### 1.1 What people actually run

Retail and open-source 15m bots almost never replay the L3 book for a fib/grid. They replay **OHLC bars in time order**, keep a book of **resting limits**, and fill a resting order when the bar's range tags the price.

That split — **decision at close, fill of already-working limits inside the bar** — is the honest simple engine:

| Event | Knowable when? | Allowed? |
|---|---|---|
| Completed bar `t-1` O/H/L/C | At open of bar `t` | Yes |
| Resting limit placed **before** bar `t` | Working at open of `t` | Fill during `t` if the range tags it |
| Signal computed from bar `t` close | After `t` closes | Place / cancel for bar `t+1` only |
| Using bar `t` high **and** low to both *create* a new order and *fill* it | Same bar | Lookahead. Stop. |

CuteMarkets states the regression test in one sentence: a touch or breakout on bar `t` enters no earlier than bar `t+1` **unless** the strategy explicitly modeled a standing order before the touch. ([Same-bar fill lookahead](https://cutemarkets.com/blog/same-bar-fills-lookahead-intraday-strategies))

Backtrader's default is the same idea: a market order created on a closed bar matches the **next** bar. Cheat-on-open is an opt-in, named cheat. ([Order creation/execution](https://www.backtrader.com/docu/order-creation-execution/order-creation-execution/); [Cheat-On-Open](https://www.backtrader.com/docu/cerebro/cheat-on-open/cheat-on-open/))

Freqtrade backtesting fills a limit **at the requested price with no slippage if that price is inside the candle high/low**. Entries otherwise happen at open unless custom pricing is set. Intra-candle path (high before low or the reverse) is unknown; `--timeframe-detail` is the documented patch. ([Freqtrade backtesting](https://www.freqtrade.io/en/stable/backtesting/))

vectorbt's `Portfolio.from_signals` defaults to filling on the **same bar's close**. The cheap honesty test is `entries.shift(1)` (or next-bar open). If the shift kills the strategy, there was no strategy. ([vectorbt tutorial notes](https://www.quantt.co.uk/resources/vectorbt-tutorial); [Coriva vectorbt tutorial](https://coriva.eu.org/en/vectorbt-tutorial/))

QuantConnect's research guide: look-ahead is using information from the future; the event-driven engine helps but does not save you from adjusted prices, restated fundamentals, or a universe picked after the fact. ([QuantConnect research guide](https://www.quantconnect.com/docs/v2/writing-algorithms/key-concepts/research-guide))

### 1.2 Resting limits are the grid/fib case, not the SMA case

An SMA crossover **reacts**. A grid or fib invert **posts**. That is why the CuteMarkets "unless standing order" clause matters more here than in a close-to-close momentum test.

People who actually backtest grids on OHLC do this:

1. At close of `t`, compute (or keep) the rung prices.
2. Post limits that will be working at the open of `t+1`.
3. During `t+1`, if `low <= rung <= high`, mark the resting limit filled at the rung (sometimes with a slip haircut).
4. After a fill, arm the paired TP / invert swap. That new order is eligible from the **next** bar (or from the remainder of this bar only if you have a path model — 15m OHLC does not).

A public fib-grid write-up on OKX states the candle check as `low <= level <= high`, then later reframes it as a **tick-crossing** check (did the level fall between previous and current trade?). They call touch=fill a first-pass that ignores depth. ([OKX multi-symbol grid/fib architecture](https://medium.com/@jsgastoniriartecabrera/i-built-a-multi-symbol-grid-fibonacci-trading-bot-for-okx-heres-the-full-architecture-379adb67af3c))

Hummingbot's GridExecutor is the production-shaped version of the same idea: levels between start and end price, each with an amount and a take-profit, states `NOT_ACTIVE → OPEN_ORDER_PLACED → OPEN_ORDER_FILLED → CLOSE_ORDER_PLACED → COMPLETE`. Their backtest engine has a `GridExecutorSimulator` that replays OHLCV and estimates fills; it is not an L3 queue. ([GridExecutor](https://hummingbot.org/strategies/v2-strategies/executors/gridexecutor/); [Hummingbot backtesting engine](https://deepwiki.com/hummingbot/hummingbot/8.1-backtesting-engine))

HFT / market-replay tools (hftbacktest, ordersim) exist and are **stricter**: fill only after volume trades through your queue. They are the honest model for passive making. They are **not** what 15m fib invert desks actually run from 2023, because years of MBO tape for XRPEUR is not the public default. ([hftbacktest fill docs](https://hftbacktest.readthedocs.io/en/latest/order_fill.html); [hftradingbook backtesting](https://hftradingbook.com/systems/backtesting-and-simulation))

### 1.3 Data for "from 2023" — the simple path is already blocked by the public REST

Kraken public `GET /0/public/OHLC` returns **up to 720** of the most recent candles. Interval `15` is valid. The **last** row is the **current, not-yet-committed** timeframe and is always present. Older history **cannot** be retrieved from this endpoint regardless of `since`. ([Get OHLC Data](https://docs.kraken.com/api-reference/market-data/get-ohlc-data); [historical-data guide](https://docs.kraken.com/exchange/guides/general/historical-data))

720 × 15m ≈ **7.5 days**. That is why the sealed clip fits in one REST pull and a 2023 walk-forward does not.

What people actually use for multi-year 15m:

- Kraken's **downloadable OHLCVT ZIP** (1 / 5 / 15 / 30 / 60 / 240 / 720 / 1440 minute CSVs from market start). Missing candles mean **no trades in that interval**, not a flat market. ([Downloadable historical OHLCVT](https://support.kraken.com/articles/360047124832-downloadable-historical-ohlcvt-open-high-low-close-volume-trades-data))
- Optional: time-and-sales ZIP if you want tick crossing instead of bar touch. ([Downloadable historical market data](https://support.kraken.com/articles/360047543791-downloadable-historical-market-data-time-and-sales-))

**STEAL:** drop the uncommitted last REST candle; use the OHLCVT ZIP for 2023→now; do not treat 720 REST bars as "from 2023."  
**Does not change invert.** It is the tape, not the recipe.

### 1.4 Why the simple trail is thin for *this* job

Bar-close + resting limits answers the **clock**. It does not answer:

- Which swing high/low are the fib **rails**, and when those rails become knowable.
- Whether a wick tag is a fill (grid-bot default) or a tease (conservative close-through).
- How to **score** 2023–2026 without fitting the 8-day clip and calling it walk-forward.
- What fee/slippage to subtract on XRPEUR so "return > 0 after fees" is not a vanity mark.

So we broaden. Invert stays frozen while we look.

---

## 2. Broaden — walk-forward optimization vs anchored walk-forward

Pardo (1992, 2008) is the named source for walk-forward **analysis**: optimize on an in-sample window, test the **next** out-of-sample slice, roll, stitch **only** the OOS equity. ([Wikipedia: Walk-forward optimization](https://en.wikipedia.org/wiki/Walk_forward_optimization))

Two window shapes dominate practice:

| Shape | Train window | What it matches in production | Cost |
|---|---|---|---|
| **Rolling** (classic Pardo / WFO) | Fixed length; drop old bars as you add new | You will re-fit every N months on recent data | Higher variance; old regimes leave |
| **Anchored** (expanding) | Fixed start (e.g. 2023-01-01); train grows | You never throw away early history | Old regimes poison the fit |

sklearn `TimeSeriesSplit` is **anchored by default**: successive train sets are supersets of earlier ones. `max_train_size` turns it rolling. `gap` drops samples between train and test (a cheap embargo, not a full purge). ([TimeSeriesSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html))

Kiploks: pick the shape that matches how you will **refit live**. If you cannot write that sentence, you copied a forum default. Rolling windows also reset indicator warm-up every fold — exclude warm-up from the objective. ([Anchored vs rolling](https://kiploks.com/research/anchored-vs-rolling-walk-forward-windows-which-should-you-use))

LuxAlgo / Backtrex: neither shape is uniformly better; window length and step are themselves tunables, so a walk-forward can be overfit. Typical published IS:OOS ratios are 3:1 to 5:1, chosen **before** seeing results. ([LuxAlgo walk-forward analysis](https://www.luxalgo.com/library/concept/walk-forward-analysis/); [Backtrex WFO guide](https://backtrex.com/en/blog/walk-forward-optimization-backtesting-guide))

PapersWithBacktest places WFO next to purged CV and CPCV in the AFML stack. Typical ranges they quote (equity-day scale): train 252–756 bars, test 21–63, embargo ≥ max label span, step = test length so OOS slices do not overlap. Scale those to **15m crypto** and you need a **time** budget (months), not a bar count copied from daily equities. ([Walk-forward optimization course](https://paperswithbacktest.com/course/walk-forward-optimization))

### Steal vs invert

- **STEAL (scoring, not recipe):** freeze invert. Replay 15m XRPEUR from 2023 with **one** locked rule set. Report **calendar slices** (e.g. 2023 / 2024 / 2025 / 2026 YTD) as OOS of that frozen rule. That **is** a walk-forward of a fixed system. It is not Pardo WFO.
- **STEAL (if anyone later retunes):** rolling windows, because 15m XRPEUR regimes (2022 leftover bear → 2024 ETF/flow years → 2025–26) are not one stationary process. Embargo ≥ longest invert round-trip.
- **HYPOTHESIS — would change invert:** re-optimize which fib ratios, grid spacing, or "rails" lookback on each IS window (true WFO of the invert). That is a **different recipe**. Do not do it and then keep the name `c9689f5d`. If someone does it, they need a **new** hash on a **new** book, not a reseal.

Bailey, Borwein, López de Prado & Zhu: if you search many parameter sets, compute **PBO** via combinatorially symmetric CV. PBO ≈ 0.5 means the IS winner is a coin flip OOS. ([The Probability of Backtest Overfitting, SSRN 2326253](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2326253))

Our 8-day clip already **selected** a live lock among retired hashes (`2bfb1b68`, `9056f296`, `094513`). Treating that selection as a 2023 walk-forward is the PBO failure mode. **Do not reseal.**

---

## 3. Broaden — purged k-fold for time series

Shuffled k-fold trains on the future and tests on the past. López de Prado, *Advances in Financial Machine Learning* (Wiley, 2018):

- **Ch. 7** — why k-fold fails in finance; **purge** training rows whose **label horizon** overlaps the test window; **embargo** a gap after the test fold because features are still serially correlated.
- **Ch. 12** — **Combinatorial Purged CV (CPCV):** leave *k>1* folds out so you can reconstruct **multiple** OOS paths, not one Pardo path.

Public implementations: [purged-cross-validation](https://github.com/eslazarev/purged-cross-validation) (`PurgedKFold`, `CombinatorialPurgedCV`, `reconstruct_paths`); [skfolio CombinatorialPurgedCV](https://skfolio.org/generated/skfolio.model_selection.CombinatorialPurgedCV.html). sklearn `TimeSeriesSplit(gap=…)` is the footnote version: one gap, no label-aware purge, no combinatorial paths.

Stats.SE walkthrough of CPCV: with *N* blocks and *k* test blocks you get multiple full paths; purge is a **different** idea from the combination grid. ([What is CPCV?](https://stats.stackexchange.com/questions/443159/what-is-combinatorial-purged-cross-validation-for-time-series-data))

### Why invert labels overlap

An invert fill at 15m bar `t` may not round-trip for hours or days (resting TP). The **label** of bar `t` is "what happened to that rung's pair until the opposite fill." Training on bars whose round-trips leak into the test window is the AFML overlap.

**STEAL:** when scoring frozen invert across folds, embargo at least the **max observed holding time** (or a conservative cap, e.g. 2–5 days of 15m bars). Do not shuffle. Do not use random k-fold.

**HYPOTHESIS — would change invert:** use CPCV / PBO to **drop** fib ratios that only win on one path. That is a recipe search. New book, new hash, still paper. Not a reseal of `c9689f5d`.

**HYPOTHESIS — would change invert:** triple-barrier labels (de Prado) instead of invert swap-on-fill. Different strategy.

Purged k-fold is **thin as a replacement** for walk-forward on a **path-dependent grid**. CPCV assumes you can score a row. Invert's next order depends on which rung filled. Event-driven replay of the frozen recipe on expanding/rolling **time** windows is the match; purged k-fold is a **diagnostic** on top, not the engine.

---

## 4. Broaden — fib swing selection (the real lookahead)

Invert needs **rails** (a swing high and swing low) before 0.236…2.618 mean anything. Discretionary rail picking on a finished chart is the standard fib cheat.

Investopedia: accuracy depends on which swing points you pick; two traders draw different levels; levels are not predictive by themselves. ([Fibonacci retracement strategies](https://www.investopedia.com/articles/active-trading/091114/strategies-trading-fibonacci-retracements.asp))

YWO's backtest recipe: define the swing **mechanically** (e.g. 3-candle low), then advance **bar by bar** and do not look ahead. They also note basic fib vs coin-flip studies. ([How to backtest Fibonacci](https://ywo.com/blog/backtest-fibonacci-strategy/))

Mechanical swing families people actually code:

| Detector | Confirmation | Repaint? | Delay |
|---|---|---|---|
| **Williams fractal** (5-bar: middle high > 2 on each side) | 2 bars to the right must close | No, once confirmed | **2 bars** (30m on a 15m chart) |
| **N-bar pivot** (`n` left, `n` right) | `n` future bars | No, once confirmed | **n bars** |
| **ZigZag** (percent / ATR threshold) | Last leg extends until reverse | **Yes, last leg** | Unknown until reverse |

Williams fractal: confirmation lags by two bars; a marker on the live bar is provisional. Once the two right-hand bars close, an honest fractal is fixed. Lag is the price of no-repaint. ([LuxAlgo: Williams Fractal](https://www.luxalgo.com/library/concept/williams-fractal/))

ta4j: `RecentZigZagSwingHigh/Low` confirm after a threshold move — no fixed lookahead window, but the last leg still moves until the threshold hits. Fractal swings need the `following*` window. ([Trendlines & swing points](https://ta4j.github.io/ta4j-wiki/Trendlines-and-Swing-Points.html))

Market Fragments pivot-engine paper: lookback length is a **responsiveness** knob, not a predictive parameter; in-sample "success × swing" proxies inflate with longer lookbacks while directional accuracy stays flat. Optimizing lookback on that proxy ships the longest L. Walk-forward on a proper metric did not. ([Main Pivot Engine paper](https://www.marketfragments.com/post/mf-strategy-factory-main-pivot-engine-paper))

TradingView / Pine: `request.security(..., lookahead=barmerge.lookahead_on)` without a `[1]` offset leaks the **finished** HTF high/low onto earlier bars — the exact "I already knew today's high" fib cheat. The documented non-repaint pattern is `expression[1]` **and** `lookahead_on`. ([Pine other timeframes](https://www.tradingview.com/pine-script-docs/concepts/other-timeframes-and-data/); [Repainting](https://www.tradingview.com/pine-script-docs/concepts/repainting/); [TV support: peeking into the future](https://www.tradingview.com/support/solutions/43000614705-strategy-produces-unrealistically-good-results-by-peeking-into-the-future/))

### Steal vs invert

- **STEAL:** never draw rails from the **sample-wide** 2023–2026 high/low. Rails at time `t` may use only swings **already confirmed** by `t`.
- **STEAL:** if rails come from a higher timeframe (4h / 1d), use the Pine `[1]`+`lookahead_on` rule: last **closed** HTF bar only.
- **STEAL:** do not use unconfirmed ZigZag as live rails. Last-leg ZigZag is a chart decoration, not a fill engine.
- **HYPOTHESIS — would change invert:** lock rails to Williams 5-bar fractals (2-bar delay) or a named N-bar pivot. The journal says "full fib set from that pair's rails" but does not name the detector. Naming it would **specify** invert, not just score it. Flag, do not apply. If the current engine already uses a detector, **cite it** on a later recipe page; do not invent one here.
- **HYPOTHESIS — would change invert:** rebuild rails every N bars from the last confirmed impulse (rolling fib) vs once-per-leg. Different invert.

---

## 5. Broaden — grid fill-on-touch vs fill-on-close

This is the second-largest honesty gap after swing selection.

| Model | Fill when | Typical user | Bias vs live resting limit |
|---|---|---|---|
| **Fill-on-touch** (wick) | `low <= limit <= high` | Freqtrade default; most grid blogs | **Optimistic**: tags a wick with no size, no queue |
| **Fill-on-close** | Close crosses or closes through the level | Conservative bar engines | **Pessimistic**: misses honest intra-bar fills of a standing order |
| **Timeframe-detail** | 15m decisions, 1m (or tick) path | Freqtrade `--timeframe-detail` | Better path; still no queue |
| **Tick crossing** | Last trade crossed the level | OKX fib-grid live loop; Kraken trades ZIP | Closer to tape; still no queue |
| **Queue / MBO** | Size traded through ahead of you | hftbacktest, ordersim | Honest maker; rarely available 2023→ for this desk |

Freqtrade (quoted): *"All orders are filled at the requested price (no slippage) as long as the price is within the candle's high/low range."* Also: the engine cannot know whether high happened before low. `--timeframe-detail` is the documented intra-candle patch. ([Backtesting](https://www.freqtrade.io/en/stable/backtesting/))

Coin Bureau's 2026 crypto backtest guide: a grid bot backtest should assume **maker or taker depending on behaviour**, plus spread, inventory, and **missed fills**. Do not assume every touch filled the full size. ([How to backtest a crypto strategy](https://coinbureau.com/guides/how-to-backtest-your-crypto-trading-strategy))

tbot.team: close-only backtests miss intra-candle stops and TPs; they claim large win-rate gaps when you add intra-candle data. Treat the magnitudes as marketing; treat the **direction** as real. ([How backtesting really works](https://tbot.team/learn/how-backtesting-works))

Our paper engine (Kraken paper skill): **instant full fills, slippage 0, no partials.** That is strictly more optimistic than fill-on-touch OHLC. CODER "ten ways" already lists this. Live TP `PAPER-00030` can sit while the public ticker **tags** 1.26778 — that is the touch-vs-print gap in one sitting (see Coder 01).

**STEAL:** for a 2023 OHLC walk-forward of **frozen** invert, publish **two** fill columns: touch and close-through. Gate language stays **prints**, not tags. Do not backfill `PAPER-00030` from a live high.

**STEAL:** if 1m OHLCVT is in the Kraken ZIP, use it as path-inside-15m (Freqtrade detail analogue). Still paper. Still not a reseal.

**HYPOTHESIS — would change invert:** require close-through before swapping jobs (more conservative invert). That changes fill count vs the lab clip. New book if you ship it.

**HYPOTHESIS — would change invert:** fill-every-rung on a touch (`2bfb1b68`, retired). Do not revive.

---

## 6. Broaden — fee / slippage models for XRPEUR

### 6.1 Posted fees (public, this sitting)

Kraken Pro **spot** cross-platform table on the public fee page (fetched 2026-08-27):

| Tier | 30d spot vol | Maker | Taker |
|---|---|---|---|
| Tier 1 | $0+ | **0.40%** | **0.80%** |
| … | … | … | … |

([Kraken fee schedule](https://www.kraken.com/features/fee-schedule); [How trading fees work](https://support.kraken.com/articles/201893638-how-trading-fees-work-on-kraken))

The **paper engine** still deducts **0.26% taker** per fill (Starter-era default in `kraken-paper-strategy`). Live journal already prints a **shadow ladder**: `0.26=0.52; 0.40=0.80; 0.80 taker=1.60` on the round-trip. That shadow is the right instinct: **do not silently switch the engine to maker 0.16% because a grid "should" make.**

Instant Buy/Sell on kraken.com is a **different product** (1% / 1.5% + spread). Not the Pro book. Do not mix.

2023-era Kraken blog: volume-trial taker as low as 4–8 bps at $100M+ — irrelevant to a EUR 10k paper book. ([$100M+ fee tier trial, Aug 2023](https://blog.kraken.com/product/promotions/announcing-krakens-100m-250m-and-500m-volume-fee-tier-trial))

### 6.2 Spread / slippage (public, not XRPEUR-specific)

Bridgeport's Kraken **venue** snapshot (not pair-tagged XRPEUR): spread ~0.94 bps @ $5k, ~3.43 bps @ $100k; slippage ~0.47 / 1.71 bps. They note **strong EUR liquidity** vs thinner alts. ([Bridgeport: Kraken execution](https://analytics.bridgeportmq.com/exchange/kraken))

Brokerate's fee/spread survey: posted fee ≠ all-in; alts (incl. XRP) usually wider than BTC/ETH; Kraken retail posted fees historically higher than Binance-class books. ([Crypto exchange fees PDF](https://brokerate.io/library/crypto-exchange-fees-costs-a-deep-dive-into-spreads-slippage-and-hidden-charges.pdf))

There is **no** public, citable, pair-level XRPEUR 2023–2026 slippage surface in these sources. Anyone inventing "XRPEUR slip = 2 bps" is guessing. Honest models in the literature:

1. **Posted taker** on every fill (paper engine).
2. **Shadow extra** for spread + slip (CODER STARTABLE). Journal already shows 0.40 and 0.80 ladders.
3. **Maker** only if you model queue and missed fills (hftbacktest). We do not.
4. **Half-spread** haircut on touch fills as a poor-man's adverse-selection tax.

Round-trip at invert prices 1.24496 → 1.26778 is about **+1.833% gross**. Two 0.26% takers ≈ 0.52% → ~+1.31% **if** the TP prints and there is zero slip. Two 0.80% takers ≈ 1.60% → still green vs 1.83% **on that one hypothetical**. That hypothetical is **not** a fill and would still be **2 < 8**. Do not write it into the scoreboard (Coder 01 / 02).

**STEAL:** keep engine 0.26% **and** the 0.40 / 0.80 shadow. Gate 1 uses the **worst honest** shadow you are willing to defend, not the prettiest.

**STEAL:** do not use Instant 1% as the Pro paper fee.

**HYPOTHESIS — would change invert scoring:** switch paper fills to maker 0.40% or 0.16% because "grids make." That **changes** the return conjunct without changing rungs. Flag as a scoring cheat unless queue is modeled. Do not reseal a PASS that assumed 0.26% into a maker story.

**HYPOTHESIS — would change invert:** size rungs from XRPEUR depth so each clip is < X% of visible bid/ask. No public 2023 depth tape in this research; would be a new recipe constraint.

---

## 7. Broaden — look-ahead bugs (mapped to invert)

Freqtrade `lookahead-analysis` is the practical checker people run: full-dataframe indicator pass vs sliced pass; flags `.mean()` over the whole frame, `shift(-n)`, `iloc` into the future, `rolling`-less aggregations, MACD `signalperiod=1`. Limit orders are **forced to market** during that command to avoid false positives, unless `--lookahead-allow-limit-orders`. ([Lookahead analysis](https://www.freqtrade.io/en/stable/lookahead-analysis/))

Marketmaker.cc controlled audit: same-bar fill of a signal that already contains `r[t]` turns a noise strategy from Sharpe **−0.74 → +14.8**. Diagnostic: shift every fill one bar later; if it collapses, you were trading the past. ([Look-ahead taxonomy](https://marketmaker.cc/en/blog/post/look-ahead-bias-taxonomy/))

QuanterLab / Pomegra: using a bar's high/low in the **signal** is lookahead unless the order was already standing; close-of-bar indicators cannot fill at that bar's open. ([Look-ahead bias](https://quanterlab.com/articles/foundations-look-ahead-bias); [Data quality and look-ahead](https://pomegra.io/learn/library/track-e-trading-risk/active-trading/chapter-10-backtesting/data-quality-and-look-ahead-bias))

Kraken-specific: the **uncommitted** last OHLC row is live lookahead if you treat it as a closed 15m bar. ([OHLC docs](https://docs.kraken.com/api-reference/market-data/get-ohlc-data))

### Invert-shaped bug list (do not "fix" invert from this page)

| # | Bug | Invert shape | Steal or hypothesis |
|---|---|---|---|
| L1 | Same-bar signal **and** fill | Compute invert swap from bar `t` close and fill the new TP on bar `t` wick | **STEAL** next-bar for **new** orders |
| L2 | Path unknown (high and low both used) | Buy rung and sell rung both tagged in one 15m candle; engine takes the favourable order | **STEAL** conservative: if both would fill, take **adverse** order or skip; or 1m detail |
| L3 | Sample-wide rails | Fib from 2023–2026 high/low, then "replay" 2023 | **STEAL** confirmed swings only |
| L4 | ZigZag last leg | Rails move after the fill that "used" them | **STEAL** confirmed fractals / closed ZigZag only |
| L5 | HTF `lookahead_on` without `[1]` | Daily high as today's TP at the daily open | **STEAL** Pine offset rule |
| L6 | Whole-frame `.mean()` / `.max()` | Volatility or range from the future | **STEAL** `rolling` only |
| L7 | Uncommitted REST candle | Last 15m bar still forming | **STEAL** drop it |
| L8 | Touch counted as a **print** | Live high 1.26778 ⇒ journal fill 00030 | **STEAL** prints only (already locked) |
| L9 | 20+1 / reseal | Lab clip + `PAPER-00029` = 21 fills | **STEAL** new book after seal; **do not reseal** |
| L10 | WFO window shopping | Try IS/OOS ratios until OOS looks green | **STEAL** freeze windows before results (Pardo / PBO) |
| L11 | Fee lookahead | Score with maker after seeing taker would fail | **STEAL** declare fee model first |
| L12 | Retired hash revival | `094513` 99 fills PASS | **STEAL** retired stays retired |

L2 is the grid-specific cousin of same-bar fill. 15m invert with many rungs **will** see bars that tag two levels. OHLC cannot order them. **STEAL** a written tie-break. **HYPOTHESIS** if today's invert already assumes a path — cite the engine, do not invent one here.

---

## 8. What we should steal vs what would change invert

Invert stays. `dca-paper` stays. `c9689f5d` stays sealed. This table is the whole point of the broaden.

### STEAL (around invert — do not rewrite rungs)

1. **Bar-close decisions, next-bar eligibility for new orders.** Standing limits may fill on a later bar's range. (Backtrader, CuteMarkets, Freqtrade.)
2. **2023 tape from Kraken OHLCVT ZIP**, not public REST 720. Drop the uncommitted last candle.
3. **Frozen-recipe walk-forward:** one invert, calendar OOS slices from 2023. Stitch OOS only. Do not call the 8-day clip this.
4. **Rolling vs anchored as a scoring choice**, documented in one sentence tied to "we will not retune live." For frozen invert, **anchored from 2023-01-01** (or first XRPEUR 15m bar in the ZIP) is the honest default. Rolling is for a later retune study.
5. **Embargo ≥ max invert holding time** if anyone splits folds.
6. **Confirmed swings only** for rails (fractal / N-bar). No sample-wide high/low. No live ZigZag leg.
7. **Two fill columns:** touch vs close-through. Optional 1m detail from the same ZIP.
8. **Fee shadow ladder** already on the journal (0.26 / 0.40 / 0.80). Gate 1 uses shadowed return.
9. **One-bar shift diagnostic** on the whole replay. If it dies, it was lookahead.
10. **Freqtrade-style lookahead pass** (or equivalent sliced-vs-full indicator check) before anyone trusts a 2023 equity curve.
11. **Count `PAPER-*` prints only.** Resting 00030 / open 00028 stay non-fills.
12. **Do not reseal.** A 2023 walk-forward, if ever run, is a **new** artifact with a **new** hash on `invert-paper` **history**, not a rewrite of `c9689f5d`.

### HYPOTHESIS (would change invert — not applied)

| ID | Change | Why it is a recipe change |
|---|---|---|
| H1 | Name Williams-5 or N-bar as **the** rail detector | Journal says "rails" without a detector |
| H2 | Rolling fib (rebuild rails each impulse) vs static leg | Different rungs |
| H3 | Fill-on-close-through required before swap-jobs | Fewer fills than wick-touch; would disagree with a touch-based clip |
| H4 | True Pardo WFO of which fib ratios / spacing survive each year | New parameter path; PBO applies; new hash |
| H5 | CPCV to drop ratios | Search, not the locked full set |
| H6 | Maker-fee engine without a queue model | Changes gate 1 without changing rungs |
| H7 | Depth-capped size / partial fills | New constraints |
| H8 | Revive fill-every-rung or entry-waits-TP | Retired hashes |
| H9 | Mix sleeve 3x into the 2023 spot path | Journal fraud; sleeve FAIL is not the gate |
| H10 | Use `dca-paper` or leftover `fib-paper` BTCUSD as the 2023 walk-forward book | Wrong book |

Any H* that ships belongs on a **new** workspace or a **new** seal. Not on `c9689f5d`. Not on a `dca-paper` reset.

---

## 9. Recommended 2023 walk-forward (frozen invert, still paper)

This is a **research recipe for a later Coder page**, not an order ticket and not a reseal.

1. **Data.** Kraken OHLCVT ZIP, pair XRPEUR, interval 15 (and 1m if using detail). Fill missing 15m bars as **no trade** (Kraken's documented meaning), not as a zero-range candle that cannot tag a limit. Start at 2023-01-01 00:00 **or** the first 15m print on/after that date. End = last **committed** bar. Public REST is only for a live sanity check of the tail.
2. **Engine.** Event loop on 15m bars. At open of `t`, resting orders from `t-1` may fill on `t` high/low (touch column) and/or on close-through (close column). New invert swap after a fill is eligible from `t+1` unless 1m detail gives a remaining path **and** that rule is written down.
3. **Rails.** Only swings confirmed by the detector you name **before** the run. If you cannot name it, **stop** — that is H1, not this run.
4. **Fees.** Deduct 0.26% per fill in the engine copy of paper; also print 0.40% maker / 0.80% taker shadows (public Tier 1 this sitting). Slippage: do not invent an XRPEUR bps; use a declared extra (CODER shadow) or 0 with the "ten ways" disclaimer.
5. **Walk-forward.** Frozen invert. Report yearly OOS (2023, 2024, 2025, 2026 YTD) plus the stitched OOS curve. Warm-up: enough bars for the named swing detector. **Do not** optimize rungs on 2023 and test 2024 under the same seal.
6. **Gate.** Still the three conjuncts on **`invert-paper` prints**, not on the 2023 simulator. A 2023 replay is **lab**, like `c9689f5d`, until it is a **new** named artifact. It does not promote. It does not add to fill 1.
7. **Tie-break.** If one 15m bar would fill two invert prices, write the rule (adverse, first-in-time via 1m, or skip). Silent "both filled at the good prices" is L2.

Still paper. Still n=1 on the live invert book. Still do not reseal.

---

## 10. Verdict

**Simple path:** bar-close replay + resting limits **is** how people walk-forward 15m grids. Steal it.

**Thin for this job:** "from 2023 without lookahead" dies on **rails**, **touch vs close**, **REST 720 vs ZIP**, **fee shadow vs maker fantasy**, and **clip-as-walk-forward**. Broaden was required.

**Not our recipe only:** Pardo WFO, sklearn anchored splits, AFML purge/embargo/CPCV, Williams fractals, Freqtrade touch fills, Hummingbot grid state machines, Pine lookahead, Kraken OHLCVT, and PBO are the public stack. We steal the **clock, tape, confirmation, and scoring**. We do **not** change invert in this file.

**Promotion:** **RED**. Gate NOT MET. 8-day PASS ≠ 2023 walk-forward. Sleeve FAIL is not the gate.

---

## Sources (public URLs)

Walk-forward / CV

- https://en.wikipedia.org/wiki/Walk_forward_optimization
- https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html
- https://kiploks.com/research/anchored-vs-rolling-walk-forward-windows-which-should-you-use
- https://www.luxalgo.com/library/concept/walk-forward-analysis/
- https://backtrex.com/en/blog/walk-forward-optimization-backtesting-guide
- https://paperswithbacktest.com/course/walk-forward-optimization
- https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2326253
- https://github.com/eslazarev/purged-cross-validation
- https://skfolio.org/generated/skfolio.model_selection.CombinatorialPurgedCV.html
- https://stats.stackexchange.com/questions/443159/what-is-combinatorial-purged-cross-validation-for-time-series-data

Replay / fills / lookahead

- https://www.freqtrade.io/en/stable/backtesting/
- https://www.freqtrade.io/en/stable/lookahead-analysis/
- https://www.backtrader.com/docu/order-creation-execution/order-creation-execution/
- https://www.backtrader.com/docu/cerebro/cheat-on-open/cheat-on-open/
- https://cutemarkets.com/blog/same-bar-fills-lookahead-intraday-strategies
- https://www.quantconnect.com/docs/v2/writing-algorithms/key-concepts/research-guide
- https://www.quantt.co.uk/resources/vectorbt-tutorial
- https://coriva.eu.org/en/vectorbt-tutorial/
- https://marketmaker.cc/en/blog/post/look-ahead-bias-taxonomy/
- https://quanterlab.com/articles/foundations-look-ahead-bias
- https://hftbacktest.readthedocs.io/en/latest/order_fill.html
- https://hftradingbook.com/systems/backtesting-and-simulation
- https://hummingbot.org/strategies/v2-strategies/executors/gridexecutor/
- https://coinbureau.com/guides/how-to-backtest-your-crypto-trading-strategy
- https://medium.com/@jsgastoniriartecabrera/i-built-a-multi-symbol-grid-fibonacci-trading-bot-for-okx-heres-the-full-architecture-379adb67af3c

Fib / swings / Pine

- https://www.investopedia.com/articles/active-trading/091114/strategies-trading-fibonacci-retracements.asp
- https://ywo.com/blog/backtest-fibonacci-strategy/
- https://www.luxalgo.com/library/concept/williams-fractal/
- https://ta4j.github.io/ta4j-wiki/Trendlines-and-Swing-Points.html
- https://www.marketfragments.com/post/mf-strategy-factory-main-pivot-engine-paper
- https://www.tradingview.com/pine-script-docs/concepts/other-timeframes-and-data/
- https://www.tradingview.com/pine-script-docs/concepts/repainting/
- https://www.tradingview.com/support/solutions/43000614705-strategy-produces-unrealistically-good-results-by-peeking-into-the-future/

Kraken tape / fees (public)

- https://docs.kraken.com/api-reference/market-data/get-ohlc-data
- https://docs.kraken.com/exchange/guides/general/historical-data
- https://support.kraken.com/articles/360047124832-downloadable-historical-ohlcvt-open-high-low-close-volume-trades-data
- https://support.kraken.com/articles/360047543791-downloadable-historical-market-data-time-and-sales-
- https://www.kraken.com/features/fee-schedule
- https://support.kraken.com/articles/201893638-how-trading-fees-work-on-kraken
- https://analytics.bridgeportmq.com/exchange/kraken

Desk (cite, do not reseal / reset)

- https://dca-paper-journal.surge.sh/
- https://github.com/eyeskull2220/solana-invoice/pull/132 — Coder 01 research
- https://github.com/eyeskull2220/solana-invoice/pull/144 — Coder 02 plan locks
- https://github.com/eyeskull2220/solana-invoice/pull/118 — CODER seat

AFML book (paywalled; chapter map is public): López de Prado, *Advances in Financial Machine Learning*, Wiley 2018, ch. 7 (purge/embargo), ch. 12 (CPCV).

---

## Out of scope (honoured)

- No paper or live Kraken orders  
- No API keys  
- No reseal of `c9689f5d`  
- No `dca-paper` reset / convert  
- No invert rung rewrite (hypotheses named, not applied)  
- No journal HTML patch, no shop HTML  
- No Phantom spend, no FACTUUR title, no invented KBO  

**Promotion: no.** Stay paper. Gate NOT MET. A 2023 walk-forward, if a later Coder runs it, is a new lab artifact — not this seal, not fill 1, not a reason to fund.
