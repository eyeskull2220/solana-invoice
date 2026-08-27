# RESEARCH — Which trading-style clocks survive posted crypto spot fees?

**Seat:** RESEARCHER · Inform **Coder**  
**Lens:** start **simple** (15m bar vs 0.26 / 0.40 / 0.80), then **broaden** to clocks and styles. Docs + public GETs + public fee tables only. **General language.** Not an invert rewrite. Not a new invert score.  
**Date:** 2026-08-27  
**Stamp:** VOORBEELD · paper / simulated · not FACTUUR · not INVOICE · not live-trade advice  
**HEAD (leftover `main` at write):** `2170952`  
**Still paper.** `is_fund_gate: false`. invert-paper fill **1** stays. Do not reseal `c9689f5d`. Do not reset `invert-paper` or `dca-paper`. **No orders. No keys. No CODE.**

This file answers one question: **which trading-style CLOCKS actually survive posted crypto spot fees**, in public literature and public fee tables — not a new invert score.

Sibling [#211](https://github.com/eyeskull2220/solana-invoice/pull/211) already did the 15m inequality. This page **steals that inequality** and broadens. It does **not** reprint invert as a prettier curve.

**PLAN [#207](https://github.com/eyeskull2220/solana-invoice/pull/207) GREEN** ([#214](https://github.com/eyeskull2220/solana-invoice/pull/214)) is a **PLAN-stage pass**. It is **not a CODE licence**. Do not start CODE from #207, from #214, from #196, or from this research.

---

## Locks (this sitting)

| Lock | Status |
|---|---|
| Still paper / no keys / no orders / no CODE | **GREEN** |
| `is_fund_gate` | **false** |
| `invert-paper` is the **fund gate** (fill **1**) | **GREEN** — not this file |
| `invert-wf-2023` is a 15m walk-forward, **not** the gate | **GREEN** |
| PLAN #207 GREEN is **not** a CODE licence | **GREEN** |
| Do not replace **INVERT-V2-1LIMIT −15.21% / 15.49% DD** | **GREEN** — cited, not restated as prettier |
| Do not invent a 2023 equity curve | **GREEN** |
| Do not reseal `c9689f5d` / reset `dca-paper` | **GREEN** |
| Do not change invert | **GREEN** — **H- labeled, not applied** |
| VOORBEELD | **GREEN** |

Live gate book (untouched): fill **1** `PAPER-00029` buy XRPEUR @ **1.24496**. Resting TP `PAPER-00030` sell LIMIT @ **1.26778** is **not** a fill. Open `PAPER-00028` @ **1.23084** is **not** a fill. Gate (return > 0 after fees **and** ≥ 8 prints **and** maxDD ≤ 8%) is **NOT MET**.

Named research-book prints (**STEAL — do not replace**):

| Book | Print | What it is |
|---|---|---|
| Grind / fill-every-rung | **9097** fills · **−99.989999%** · maxDD **99.990007%** · end **€1** | **Not invert.** Close-model ladder. [#201](https://github.com/eyeskull2220/solana-invoice/pull/201) |
| invert-v2 day0 TWO-CLIP | **7923** fills · **−40.84%** · maxDD **41.08%** · fees **4120** · `price_pnl` **+36** | **Not invert.** Two concurrent buys. |
| **INVERT-V2-1LIMIT** | **−15.21%** · maxDD **15.49%** · **2779** fills · max concurrent **1** | **FAIL vs 8% DD.** **Not** the fund gate. **Not** this page’s score. **Do not replace.** |
| Sealed lab clip | 20 fills · +0.681154% · maxDD 0.890854% · 8 days vs `sha256:c9689f5d…` | **Cite. Do not reseal. Not 2023→now.** |

Kraken MCP this VM: **not used**. Public REST only. Server clock this sitting: `GET /0/public/Time` → `unixtime` **1787863758** (`Thu, 27 Aug 26 20:49:18 +0000`). `GET /0/public/SystemStatus` → `online`.

---

## Method of this paper

1. **Simple first:** round-trip fee vs typical **15m** XRPEUR range. Steal [#211](https://github.com/eyeskull2220/solana-invoice/pull/211). If the tax is larger than the bar, a 15m harvest is dead before style is discussed.
2. **Then clocks:** same inequality at **1h / 4h / 1d**, from public REST + √time from 2023+ weekly / 2024-09+ daily. General. Not an invert rewrite.
3. **Then styles on those clocks:** maker vs taker (queue, missed fills); hold length vs fee (churn vs one swing); grid density vs one pair; trend-following vs fade on the **same** tape.
4. **Public literature + public fee tables.** No invented 2023 curve. No new invert cells.
5. **Hypotheses labeled `H-`.** Slower clock / wider / maker. **Not applied.** Invert stays invert.

---

## Verdict (for Coder)

| Claim | Color |
|---|---|
| Round-trip **0.52%** vs typical 15m range **~0.45–0.47%** | **RED** as a 15m-bar harvest ([#211](https://github.com/eyeskull2220/solana-invoice/pull/211)) |
| 0.40 / 0.80 shadows as “stress only” | **YELLOW** — Kraken Pro **Tier 1 since 2026-07-09** is **0.40% maker / 0.80% taker** |
| **1h** clock at 0.26% taker (scaled range ~0.91–0.93%) | **YELLOW** geometry · **RED** if you must capture ~100% of the bar |
| **4h** clock at 0.26% taker | **YELLOW** — public Kraken 0.26% **trend** study **dies on 4h** (−6.01%) |
| **1d** (or slower) clock at ~26 bps, **low turnover** | **YELLOW/GREEN cluster in literature** — the only posted-fee survival that repeats |
| Maker as a free tax cut | **RED** as a slogan. Queue + missed fills + adverse selection. After 2026-07-09, Tier 1 **maker RT is 0.80%** |
| Tight grid / high density at posted spot fees | **RED** in practitioner backtests (fees 40–55% of gross) |
| One pair / wide spacing / low churn | **YELLOW** — the *shape* that can live; **not** a new invert PnL |
| Fade (15m sign-reversion) pays 26 bps | **RED** — arXiv gross ~**1.3 bp** vs 5–20 bp costs; **0 of 183** pairs clear 5 bp |
| Trend-follow on the **same** tape, **daily** clock, few trades | **YELLOW** — one honest Kraken 0.26% walk-forward: **+4.33%** vs buy-and-hold **+127%** |
| This file as fund gate / live / keys / CODE from #207 | **RED** |
| Replacing INVERT-V2-1LIMIT **−15.21% / 15.49% DD** | **RED** — not done |

**Overall:** posted crypto **spot** fees (paper **0.26%** taker; live Kraken Tier 1 **0.40 / 0.80**; Binance VIP 0 **0.10 / 0.10**) kill **fast clocks** and **tight grids**. What **repeats** in the public record is a **slower clock**, and/or **wider spacing**, and/or **low turnover**, and/or **maker only when the posted maker rate is actually cheaper and the queue is honest**. That cluster is **`H-` labeled, not applied.** It is **not** permission to rewrite invert, not a 1LIMIT restatement, and **not** a CODE licence from PLAN 207 GREEN. Still paper.

---

## 1. Simple first — 15m bar vs 0.26% / 0.40% / 0.80%

Steal from [#211](https://github.com/eyeskull2220/solana-invoice/pull/211). Rechecked this sitting. Not a new invert score.

### 1.1 The tax (posted tables, not a hoped-for rebate)

| Column | Per fill | Round-trip (buy+sell) | What it is |
|---|---|---|---|
| **Paper primary** (“Starter taker”, locked on invert-paper) | **0.26%** | **0.52%** | Engine default. **Not** live Tier 1. |
| Shadow | **0.40%** | **0.80%** | Matches **live Tier 1 maker** after 2026-07-09 |
| Shadow taker stress | **0.80%** | **1.60%** | Matches **live Tier 1 taker** after 2026-07-09 |
| Binance VIP 0 (public comparison) | **0.10%** | **0.20%** | Cheaper band many blogs assume |

Official Kraken Pro **Spot Crypto**, cross-platform tiers from **9 July 2026**:

| Tier | 30d spot vol / AoP | Maker | Taker |
|---|---|---|---|
| **Tier 1** | $0+ | **0.40%** | **0.80%** |
| Tier 2 | $2.5k+ | 0.30% | 0.60% |
| Tier 3 | $10k+ or $20k AoP | 0.22% | 0.38% |

Sources: [Kraken fee schedule](https://www.kraken.com/features/fee-schedule) · [cross-platform fee tier changes](https://support.kraken.com/articles/cross-platform-fee-tier-changes) · [Kraken blog 2026-07-09](https://blog.kraken.com/product/pro/new-kraken-pro-fee-tiers).

Binance VIP 0 spot: **0.10% / 0.10%** ([Binance Academy on fees](https://academy.binance.com/en/articles/how-to-calculate-transaction-fees-on-binance); [VIP structure](https://www.binance.com/en/square/post/14541038221378)). Coinquant’s 15m death (below) is on **this cheaper band**. Kraken 26 bps is **stricter**.

XRPEUR is **spot crypto**, not the cheaper stablecoin/FX table. Kraken+ Instant Buy waiver is **not** Pro/API spot.

### 1.2 Typical 15m range (do not use the 7.5-day now-tape as 2023)

REST `OHLC interval=15` returns **~720 bars ≈ 7.5 days**. Using that window as 2023 is **RED** ([#197](https://github.com/eyeskull2220/solana-invoice/pull/197), [#211](https://github.com/eyeskull2220/solana-invoice/pull/211)).

This sitting’s 15m now-tape (2026-08-20 08:45Z → 2026-08-27 20:45Z, n=721): median `(H−L)/mid` **0.79%**. Noisy. Includes spike weeks. **Not** “typical 2023→now.” Do not promote it.

**2023→now proxy (public, no invented 15m file):**

| Series (this sitting) | Window | Median `(H−L)/mid` | Implied 15m if range ~ √time |
|---|---|---|---|
| Weekly REST `interval=10080` | **2022-12-29 → 2026-08-27** (n=192 weeks) | **12.05%** | 12.05 / √(7×96) ≈ **0.47%** |
| Daily REST `interval=1440` | **2024-09-06 → 2026-08-27** (n=721; REST cap, **not** full 2023) | **4.46%** | 4.46 / √96 ≈ **0.45%** |

[#211](https://github.com/eyeskull2220/solana-invoice/pull/211): **typical 15m range ≈ 0.45–0.47%.** This sitting agrees. Daily p25 (3.10%) implies a quiet 15m ≈ **0.32%**.

### 1.3 The inequality (unchanged)

```text
round-trip tax          typical 15m range
0.52%  (primary 0.26) vs   ~0.45–0.47%
0.80%  (0.40 shadow)  vs   ~0.45–0.47%
1.60%  (0.80 shadow)  vs   ~0.45–0.47%
0.20%  (Binance 0.10) vs   ~0.45–0.47%   ← only this cheaper band even *fits* a typical bar
```

**A style that harvests one 15m bar as its whole round-trip is underwater at 0.26% taker** even if it captured **100%** of a typical bar’s high–low. Quiet bars are worse. Open-to-close on the now-tape (median **0.36%**) is smaller still. Wick range is the optimistic “room.”

**Simple answer:** 26 bps × 2 is a **15m-range-sized tax** on XRPEUR. Crypto volatility lives on **days and weeks** (daily median ~4.5%, weekly ~12%). It is **not** 0.52% sitting inside a typical 15-minute candle.

EUR 200 clip does not change the **percent**. It only caps **euros** per fill. [#211](https://github.com/eyeskull2220/solana-invoice/pull/211) §1.4. Not restated as a pardon.

---

## 2. Broaden — 1h / 4h / 1d clocks (general, not an invert rewrite)

Same tax. Bigger bars. **Not** “change invert’s 15m lock.” That change is **H-C1**, labeled below, **not applied**.

### 2.1 √time from the 2023+ / 2024-09+ proxies

| Clock | Bars vs 15m | Scaled typical range | vs 0.52% RT | vs 0.80% RT | vs 1.60% RT |
|---|---|---|---|---|---|
| **15m** | 1 | **0.45–0.47%** | **under** | under | under |
| **1h** | 4 | **0.91–0.93%** | over **if** ~full capture | **under / knife** | under |
| **4h** | 16 | **1.82–1.86%** | over | over | knife at 100% capture |
| **1d** | 96 | **4.45–4.55%** | over | over | over **if** a large fraction is captured |

This is **geometry**, not a style PnL. Capture is never 100%. Close-to-close is smaller than high–low.

### 2.2 REST windows this sitting (labeled; 720-cap)

Do **not** splice these into a 2023 invert curve. 1h/4h are **short now-tapes**. Daily is the longest honest REST window.

| Clock | REST window | n | Median `(H−L)/mid` | Median `|C−O|/mid` | Frac ≥ 0.52% |
|---|---|---:|---:|---:|---:|
| 15m | 2026-08-20 → 2026-08-27 | 721 | **0.79%** (now-tape) | 0.36% | 0.75 |
| 1h | 2026-07-28 → 2026-08-27 | 721 | **0.53%** (now-tape) | 0.24% | 0.51 |
| 4h | 2026-04-29 → 2026-08-27 | 721 | **1.20%** | 0.49% | 0.93 |
| 1d | 2024-09-06 → 2026-08-27 | 721 | **4.46%** | 1.69% | 1.00 |
| 1w | 2017-05-18 → 2026-08-27 (full listing) | 485 | 15.82% | 5.92% | 1.00 |

**Read the 1h now-tape slowly.** Median 1h range **0.53%** ≈ the **0.52%** tax. A 1h harvest on the last 30 days is still a **knife-edge**, not a licence. The **scaled 2023+ 1h (~0.92%)** is the longer-run proxy. Neither is an invert score.

### 2.3 What the public literature actually prints at these clocks

**Mean-reversion, fees on, 78 backtests** — [Coinquant, 2026-08-03](https://www.coinquant.ai/blog/building-a-mean-reversion-strategy-in-cryptocurrency-markets-evidence-from-78-backtests). BTC/ETH, 15m/1h/4h/1d, **Binance-class costs** (cheaper than Kraken 0.26%), naked MR, no trend filter:

| Timeframe | Average return (their grid) |
|---|---|
| **15m** | **−14.4%** |
| **1h** | **−8.1%** |
| **4h** | **−9.5%** |
| **1d** | **−4.0%** |

One 15m Bollinger run: **693 trades**, **> $2,300 fees** on $10,000. They scaled a 5% daily MA-distance threshold down to **~0.6% on 15m** — a **thin** margin vs our **0.52%** RT; at 0.80 / 1.60 shadows it is negative **by construction**. Faster clocks **systematically erode**. 4h is not a rescue of 15m on that grid (it dipped below 1h). **1d is the least-bad clock**, still **negative on average** because **regime** (bear −40.6%) dominates the indicator.

**Trend-follow, Kraken taker 0.26% per side, walk-forward** — [nar1-frames, DEV, 2026-08-21](https://dev.to/nar1frames/i-built-a-crypto-trading-bot-it-lost-to-doing-nothing-355a). Donchian 20-day breakout. **Same rule, different clock.** Honest fees. **Not invert** — cited for **fee × timeframe**:

| Timeframe | Trades | Fees | Net |
|---|---|---|---|
| **1 day** | 14 | 1.3%/yr | **+4.33%** |
| **4 hours** | 61 | 11.4%/yr | **−6.01%** |
| **1 minute** | 52 in 45 days | 23.5% in 45 days | **−25.18%, zero wins** |

Quote: on 1-minute bars “the fee is roughly six times the average move you’re trying to catch.” **4h already dies at 26 bps** in that study. 15m sits between 4h and 1m. Buy-and-hold on their window: **+127.77%**. Survival here means **“lost less than a fee factory,”** not “beat holding.”

**15m sign exists; size does not pay the fee** — [Neklyudov, 2026, arXiv:2608.21888](https://arxiv.org/html/2608.21888). 183 Binance pairs, walk-forward:

- Directional 15m reversal is **real** (AUC small; 90% of crypto pairs vs 2.7% of US stocks).
- Gross edge per trade peaks near **1.3 bp**. Cheapest spot round-trip band cited **5 bp**; taker band **10–20 bp**.
- **Not one of 183 pairs** clears even the **5 bp maker** band. Median pair **0.46 bp**. 5-minute is worse (**0.15 bp**).

26 bps **per side** (52 bp RT) is **~40×** that 1.3 bp peak. 15m *sign* fade is a microstructure leftover. It is **not** a 26 bps taker business.

**Hourly ML / 24h momentum, costs on** — [arXiv:2606.00060](https://arxiv.org/html/2606.00060). Same hourly BTC tape, walk-forward: zero-cost XGBoost long-only **+73.5%** annualised → **−64%** after costs; 24-hour momentum “loses heavily after transaction costs because it trades too often.” Turnover, not the label of the model, is the death.

**Clock cluster that repeats:** **daily-or-slower**, **few round-trips per year**, posted spot fee **≤ ~26 bps/side**. **4h is already a maybe-not** at Kraken 0.26%. **1h / 15m are fee factories** unless the **posted** rate is a **few bp** (maker rebate / VIP), which **this desk’s Tier 1 table is not**.

---

## 3. Maker vs taker as a style choice (queue, missed fills)

Not “switch the engine to maker and reprint invert GREEN.” That is **H-C3 / PR 200 H6**. **Not applied.**

### 3.1 Posted maker is not automatically cheaper on this venue

After **2026-07-09**, Kraken Pro **Tier 1 maker is 0.40%**. Round-trip **0.80%**. That is **worse** than paper’s 0.26% taker RT **0.52%**. “Go maker” **raises** the tax at live entry unless you have **volume or AoP** into Tier 3+ (maker 0.22% / taker 0.38%). Binance VIP 0 maker **0.10%** is a **different table**. Do not launder Binance maker into a Kraken paper PASS.

### 3.2 Fill probability is the hidden fee

A resting limit is a **lottery ticket for a trade**, not a trade. Public microstructure:

- [marketmaker.cc — maker-taker decision](https://marketmaker.cc/en/blog/post/maker-taker-fees-rebates-execution/): non-fill risk + **adverse selection** (conditional on fill, price more often moves against you). Back-of-queue fills when the level is **swept**.
- [arXiv:2502.18625](https://arxiv.org/html/2502.18625v2) — *The Market Maker’s Dilemma*: maker fill probability **< 1**; **negative correlation** between fill probability and post-fill return (“negative drift of maker orders”). If the next move is against you, you fill with probability 1 (stale quote / toxic arb). If the next move is with you, you often **miss**.
- [DEV — maker-taker economics for grid bots](https://dev.to/jacktrader/maker-taker-economics-for-grid-bots-when-post-only-actually-pays-4ihm): post-only EV = `p × (gap − 2m)` vs taker EV = `gap − 2t`. With a 5 bp step and 2/5 maker-taker split, post-only **stops paying** once fill probability drops below **~0.72**. Missed fills are the cost.

Paper engines that fill every resting limit on a wick **understate** live queue. [#194](https://github.com/eyeskull2220/solana-invoice/pull/194) already named Uphold “high demand” on 13 Jul 2023. Instant full-size at `P` is optimistic.

### 3.3 Style reading (not a recipe)

| Choice | Pays | Risks |
|---|---|---|
| **Taker** | Immediacy. Fill ≈ 1 (slip aside). | Full posted taker. At Tier 1 that is **0.80%/side**. At paper 0.26%, still 15m-range-sized. |
| **Maker / post-only** | Lower *posted* rate **if** the table says so (Binance 10 bp; **not** Kraken Tier 1 40 bp). | Queue. Missed rungs. Adverse selection. Backtests that assume 100% maker fills **cheat**. |

**What survives in literature:** maker **plus** a **wide enough gap** that `p × (gap − 2m)` stays positive **and** a venue where `m` is actually small. Tight grids that “make” on every tick still die when `gap < 2m` or when `p` collapses in a trend. **H-C3 not applied.**

---

## 4. Hold length vs fee (churn vs one swing)

Two different deaths. Do not conflate. Do not invent a hold-time PnL.

### 4.1 Identity

```text
fee_drag ≈ n_fills × clip × rate
```

Primary: `n × 200 × 0.0026`. TWO-CLIP STEAL: **7923 × 0.52 = 4119.96 ≈ 4120**. That hole is **count**, not concurrent size (2 × 200 = 4% of 10k cannot make a 4120 hole without turnover).

| Death | Mechanism | STEAL exhibit |
|---|---|---|
| **Churn** | Many short round-trips whose gross `<` RT fee | TWO-CLIP: `price_pnl +36`, fees **4120**, median hold **13 bars (~3.25 h)** |
| **Size** | Notional per fill / 100% equity | Grind: **100% remaining equity** → end **€1** ([#201](https://github.com/eyeskull2220/solana-invoice/pull/201)) |
| **Stuck inventory** | One swing that does not come back | TWO-CLIP **mean** hold **47.6 bars (~12 h)** — tail, not the mill |

Median 13 = **how** the count happens (fast completes in chop). Mean 47.6 = **inventory time** on the tail (Torres hang, trend leftover). **Do not use median as occupancy** ([#212](https://github.com/eyeskull2220/solana-invoice/pull/212) S9).

INVERT-V2-1LIMIT **−15.21% / 15.49% DD / 2779 fills** is the **one-slot** cousin: concurrent size cut, **churn not gone**. **Do not replace that print.** Do not scale 7923 → 2779 into a prettier curve here.

### 4.2 Public churn math (general)

[StratBase — transaction cost erosion](https://stratbase.ai/en/blog/transaction-cost-erosion): 4 round-trips/day × 0.15% friction ≈ **219%/year** required gross. Swing ~weekly (~52 RT) ≈ **7.8%/year**. The **clock of the hold** is the **clock of the tax**.

[Coin Bureau bot mistakes](https://coinbureau.com/guides/crypto-trading-bot-mistakes-to-avoid): minimum target must exceed **round-trip + spread + slip + buffer**. A 0.4% bounce can vanish after two fees.

**Style that can live:** **one swing** whose captured move **>>** RT fee, held until the opposite prints, **low n**. **Style that dies:** re-arm every quiet bar so median hold is hours and **n** is thousands. Hold **time** is not edge ([#211](https://github.com/eyeskull2220/solana-invoice/pull/211) 47-bar geometry vs invert-v2 capture ≈ 0).

**H-C2** (wider spacing so each completed pair clears 2× fee) and **H-C1** (slower decision clock) are the labeled ways to cut **n**. **Not applied.**

---

## 5. Grid density vs one pair

Fill **count** scales with **how many levels are working**, not with Fibonacci labels.

### 5.1 Public grid rule (STEAL spacing identity, not a WFO of ratios)

- Net per completed cycle ≈ `capital_per_grid × (grid_rate − 2 × fee)`. If `grid_rate < 2 × fee`, every cycle **loses**. ([VoiceOfChain](https://voiceofchain.com/academy/grid-bot-profit-calculation); [NovaCalculator](https://www.novacalculator.com/crypto-web3/trading/crypto-grid-bot-calculator/); [Dexly](https://dexly.trade/learn/grid-trading-crypto).)
- Practitioner floor: spacing **at least 2×** RT; thumb often **3–5×**. At 0.26% that is **0.52%** floor, “comfortable” **~1.5–2.6%**. Using that to **retune invert rungs** is **HYPOTHESIS** (PR 200 **H4** / [#212](https://github.com/eyeskull2220/solana-invoice/pull/212) **H-FR3**). The **floor** (do not complete a pair inside 0.52%) is fee **identity**.
- [cryptogates.io](https://cryptogates.io/common-grid-trading-mistakes-in-crypto-backtests/): tight grids, high trade count, fees **40–55%** of gross; “small range movements often can’t cover transaction costs.”
- [Echo Zero](https://blog.echozero.app/article/grid-trading-bot-performance-in-sideways-markets): BTC daily vol ~3.2% → 0.5% spacing = overtrade; 5% spacing misses swings. Fee cut 0.10% → 0.05% can **double** net on high-frequency grids — which is an argument for **VIP/maker tables**, not for denser rungs.
- [Hummingbot GridExecutor](https://hummingbot.org/strategies/v2-strategies/executors/gridexecutor/): **one level at a time per executor**. N executors ⇒ N concurrent opens. **One pair is N = 1.**
- Fib bounce ≠ extra fill edge vs random levels: Tsinaslanidis, Guijarro & Voukelatos, ESWA 2022 ([ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0957417421012495); [open PDF](https://riunet.upv.es/server/api/core/bitstreams/07add8c4-4239-44e7-bf1f-93d66108918d/content)).

### 5.2 Desk exhibits (cite, do not blend)

| Density | Fills (2023→now order of magnitude) | End / return | Lesson |
|---|---|---|---|
| Fill-every-rung (many levels) | **9097** | **€1 / −99.99%** | Ladder + size death. **Not invert.** |
| Two concurrent clips | **7923** | **5916 / −40.84%** | Clip 200 killed size death; **churn** remained. **Not invert.** |
| **One** resting limit | **2779** | **INVERT-V2-1LIMIT −15.21% / 15.49% DD** | Density cut **helped vs 7923**; **did not** clear 8% DD. **Do not replace.** |

Going many-rungs → 2-rungs cut fills only **~13%** (9097 → 7923). Going 2 → 1 cut more (**7923 → 2779**) because the **parallel stream** died. **Neither cut is a PASS.** One pair is **necessary** to stop the ladder; it is **not sufficient** if the remaining pair still **churns inside the fee**.

**Style that can live:** **one** (or few) **wide** levels, gap **> 2× posted RT**, skip quiet days. **Style that dies:** density for “more fills.” More fills **are** the tax.

---

## 6. Trend-following vs fade on the **same** tape

Opposite bets. Same fees. Same OHLC. They cannot both harvest the same 15m bar.

### 6.1 What each needs

| | Fade / mean-reversion | Trend-follow |
|---|---|---|
| Belief | Extremes correct | Extremes persist |
| Good tape | Chop, range | One-way weeks/months |
| Bad tape | Real trend (band-walk, catching knives) | Whipsaw around the mean |
| Fee shape | **Many** small bounces | **Few** swings; long holds; **missed** chop |

Coinquant §1.1 / §4: **regime**, not the indicator family, dominates. Naked MR **+16.3%** average in their bull window, **−40.6%** in bear — **identical logic**. A high win rate still lost (68% WR, **−12.5%**). Fade **without** a trend filter **buys downtrends**.

Liu & Tsyvinski, *Risks and Returns of Cryptocurrency*, RFS 2021 ([DOI](https://doi.org/10.1093/rfs/hhaa113)): **time-series momentum** at **one-to-four week** horizons — a **daily/weekly** clock, not 15m. Liu, Tsyvinski & Wu, JF 2022: crypto momentum formation **~two weeks**, not 12-1 months equity-style. [Han, Kang & Ryu, SSRN 4675565](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4675565): under **transaction costs and daily price fluctuations**, many momentum portfolios **liquidate**; statistically significant **returns** ≠ significant **profits**.

Moskowitz, Ooi & Pedersen, JFE 2012, *Time series momentum* ([ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0304405X11002613)): TSMOM is a **slow** cross-asset effect. It is not a 15m fade.

### 6.2 Same tape, different clock — public prints

On **one** venue tape, public work that **survives posted fees** is almost always:

1. **Trend, daily (or slower), low n** — nar1-frames Donchian on **1d**, Kraken **0.26%**, **14** trades, **+4.33%**. Same rule on **4h** **dies**. Same rule on **1m** is **zero wins**.
2. **Fade, 15m, high n** — arXiv 2608.21888: **sign** is real, **1.3 bp** is not a business at 5–20 bp costs. Coinquant 15m average **−14.4%**.
3. **Fade, 1d, still regime-fragile** — Coinquant 1d average **−4.0%**; bull cells can look pretty on **3 trades**; bear cells **−45%** class.

**You do not get to pick both at 15m.** A 15m fade **fights** the 1d trend. A 1d trend **ignores** 15m noise — which is also how it **avoids** paying 0.52% ninety-six times a day.

Torres 13 Jul 2023 is the named **same-tape exam** ([#194](https://github.com/eyeskull2220/solana-invoice/pull/194)): fade wants to sell the spike; trend wants to buy the breakout; a **grid** wants to fill **every** rung in the wick. Invert’s job that day is **boring** (0 or 1 print, skipped-rung log) — that is **recipe honesty**, not a style PASS. **No invented July curve here.**

### 6.3 Honest reading

| Style × clock at posted ~26 bps spot | Public cluster |
|---|---|
| Fade × 15m / 1h | **Dies** (sign leftover; fee > edge) |
| Fade × 4h / 1d, naked | **Regime-fragile**; average still negative in Coinquant |
| Trend × 1m / 4h at 0.26% | **Dies** (nar1-frames) |
| Trend × **1d**, few trades, 0.26% | **Can print a small plus** vs a fee factory; **loses to hold** |
| Grid × dense rungs, any fast clock | **Dies** (spacing inside fee) |
| Maker × wide gap × cheap maker table | **Can live**; **not** Kraken Tier 1 0.40/0.80 |

**H- not applied.** A later PLAN that picked “1d trend” or “wide one-pair fade” would be a **new recipe**, new hash, still paper, still `is_fund_gate: false`. Not invert. Not this page.

---

## 7. STEAL vs HYPOTHESIS

### STEAL (use around a style discussion — do not rewrite invert)

| ID | Steal | Source |
|---|---|---|
| **S-C0** | Typical 15m XRPEUR range **~0.45–0.47%** vs RT **0.52 / 0.80 / 1.60**. 15m harvest is underwater at 0.26% taker. | [#211](https://github.com/eyeskull2220/solana-invoice/pull/211) + this sitting’s weekly/daily REST |
| **S-C1** | Scaled 1h ~**0.91–0.93%**, 4h ~**1.82–1.86%**, 1d ~**4.45–4.55%**. Geometry, not a score. | √time from 2023+ weekly / 2024-09+ daily |
| **S-C2** | REST 720-cap: 15m/1h are **now-tapes**. Daily starts **2024-09-06**. Do not call them 2023. | Kraken [OHLC 720](https://docs.kraken.com/api-reference/market-data/get-ohlc-data) |
| **S-C3** | Paper **0.26** + shadows **0.40 / 0.80**. Live Tier 1 **0.40 maker / 0.80 taker** since 2026-07-09. | Kraken fee page |
| **S-C4** | Coinquant: 15m **−14.4%**, 1h **−8.1%**, 4h **−9.5%**, 1d **−4.0%**. Faster erodes. | Coinquant 2026-08-03 |
| **S-C5** | nar1-frames: Kraken 0.26% Donchian **1d +4.33% / 4h −6.01% / 1m −25%**. Same signal, fees write the story. | DEV 2026-08-21 |
| **S-C6** | 15m fade gross **~1.3 bp**; **0/183** pairs clear **5 bp**. | arXiv:2608.21888 |
| **S-C7** | Maker fill **p < 1**; missed fills + adverse selection. Post-only EV needs **p** and **gap > 2m**. | arXiv:2502.18625 · jacktrader DEV · marketmaker.cc |
| **S-C8** | Grid net = gap − 2×fee. Density raises **n**. Fib bounce ≠ extra edge. | Grid literature + ESWA 2022 |
| **S-C9** | Churn death = **n × fee**. Size death = 100% equity. Median hold ≠ occupancy. | TWO-CLIP / grind STEAL · [#212](https://github.com/eyeskull2220/solana-invoice/pull/212) |
| **S-C10** | INVERT-V2-1LIMIT **−15.21% / 15.49% DD / 2779 fills / max concurrent 1** stays. TWO-CLIP **7923 / −40.84% / 4120 / +36** stays. Grind **9097 / −99.989999%** stays. | Operator / [#201](https://github.com/eyeskull2220/solana-invoice/pull/201) / [#214](https://github.com/eyeskull2220/solana-invoice/pull/214) |
| **S-C11** | `is_fund_gate: false`. invert-paper fill **1**. No reseal. No `dca-paper` reset. PLAN #207 GREEN ≠ CODE. | Locks |
| **S-C12** | Crypto TSMOM in academia is **weeks**, not 15m. Costs can liquidate “significant” momentum. | Liu & Tsyvinski RFS 2021 · SSRN 4675565 |

### HYPOTHESIS (would change invert or invent a score — **not applied**)

| ID | Hypothesis | Why it is not this page |
|---|---|---|
| **H-C1** | Decision clock **1h / 4h / 1d**; 15m only for touch fills | **Slower clock.** Changes the 15m invert lock. PR 211 **H-3**. |
| **H-C2** | Min gap ≥ `k ×` round-trip (wider rungs / skip tight pairs) | **Wider.** Changes full-fib density. PR 211 **H-2**. |
| **H-C3** | Score **maker / post-only** as primary | **Maker.** Changes 0.26% taker default. After 2026-07-09, Tier 1 maker is **0.40%** anyway. Queue not modeled. PR 200 **H6**. |
| **H-C4** | Switch the book to **1d Donchian / TSMOM** | New style. nar1-frames is **not** invert. New hash if ever shipped. |
| **H-C5** | Blend trend filter onto 15m fade so Coinquant bear −40% disappears | New recipe. Coinquant’s own next paper. Do not WFO on 2023–2026. |
| **H-C6** | Treat 1LIMIT **−15.21%** as “almost 8%” and promote | Gate is **≤ 8% DD and ≥ 8 prints and return > 0**. **15.49% DD** is **over**. Not the gate. |
| **H-C7** | Invent a 2023 daily-clock equity curve in this markdown | Forbidden. Missing archive ≠ PASS. |
| **H-C8** | Start CODE from PLAN #207 because reviewer stamped GREEN | **GREEN is not a CODE licence.** [#214](https://github.com/eyeskull2220/solana-invoice/pull/214) A7. |
| **H-C9** | Revive `2bfb1b68` / fill-every-rung / 14 pairs | Retired. Density is the mill. |

Any H\* that ships belongs on a **new** workspace or a **new** seal. Not on `c9689f5d`. Not on a `dca-paper` reset. Not on `invert-paper` fill 1.

---

## 8. Inform Coder

Coder may **read** this pack. Coder may **not** treat it as an engine change.

**Do**

- Keep paper. Keep `is_fund_gate: false`. Keep fill **1**.
- Cite 15m vs 0.52% as **[#211](https://github.com/eyeskull2220/solana-invoice/pull/211)** + this sitting’s recheck.
- When talking clocks, use the **cluster**: 15m/1h **die** at posted ~26 bps; 4h is **already dying** in the one honest Kraken 0.26% study; **1d + low n** is the repeating survival shape **in public literature**.
- Keep **three fee columns**. Live Tier 1 **0.40 / 0.80** is the shadow that matches the public table.
- Leave INVERT-V2-1LIMIT **−15.21% / 15.49% DD** ugly.

**Do not**

- Apply **H-C1 / H-C2 / H-C3** (slower / wider / maker) as invert.
- CODE from PLAN [#207](https://github.com/eyeskull2220/solana-invoice/pull/207) or REVIEW [#214](https://github.com/eyeskull2220/solana-invoice/pull/214). GREEN ≠ licence.
- CODE from PLAN [#196](https://github.com/eyeskull2220/solana-invoice/pull/196) (retired ladder).
- Invent a 2023 daily or 4h invert (or Donchian) equity curve.
- Replace 1LIMIT / TWO-CLIP / grind cells.
- Reseal `c9689f5d`. Reset `invert-paper` or `dca-paper`. Place orders. Paste keys.
- Call maker “free” without a queue model and without the **posted** maker rate.

---

## 9. RED / YELLOW / GREEN

### RED

- Treating typical 15m range as plenty vs 26 bps.
- Using 7.5-day REST 15m (median 0.79%) as 2023→now.
- Calling Kraken Tier 1 maker a tax cut vs paper 0.26% (0.40% maker **raises** RT to 0.80% at Tier 1).
- Assuming 100% maker fills / no missed queue.
- Tight grid as a fee-survival strategy.
- Fade × 15m as a 26 bps business (1.3 bp vs 52 bp).
- Replacing INVERT-V2-1LIMIT **−15.21% / 15.49% DD**.
- Inventing a 2023 equity curve.
- Funding / live / keys / reseal / `dca-paper` reset.
- Applying H-C\* inside this PR.
- Starting CODE because PLAN 207 is GREEN.

### YELLOW

- 1h scaled ~0.92% vs 0.52% (geometry only; now-tape median 0.53% is a knife).
- 4h: room vs 0.52% on √time; **dies** in nar1-frames at 0.26% trend.
- 1d literature survival is **small vs hold**, regime-fragile for fade, **not** a gate.
- Daily REST starts 2024-09-06. Implied 15m/1h/4h are a **√time model**, not a downloaded `XRPEUR_15.csv`.
- 0.26% primary vs live Tier 1 **0.80% taker**.
- Kraken MCP unused; public REST was enough for range math.

### GREEN

- Simple 15m inequality stated before broadening.
- Clocks 1h / 4h / 1d compared in **general** language, not as a silent invert rewrite.
- Maker vs taker includes **queue / missed fills / adverse selection**, not just the fee cell.
- Hold vs fee splits **churn / size / stuck inventory**.
- Grid density vs one pair uses public spacing identity + desk exhibits **without** blending them into a new curve.
- Trend vs fade on the **same** tape: opposite bets, opposite fee shapes; academic TSMOM is **weeks**.
- STEAL vs H- labeled. **H-C1/2/3 not applied.**
- Still paper. Gate stays `invert-paper` fill **1**. PLAN 207 GREEN ≠ CODE.

---

## 10. What this file is not

1. **Not the fund gate.** `invert-paper` fill **1**. Stay paper.  
2. **Not a new invert-wf-2023 score.** No PASS/FAIL for a fair invert.  
3. **Not a replacement** of INVERT-V2-1LIMIT **−15.21% / 15.49% DD**.  
4. **Not** the 8-day lab clip. Do not reseal `c9689f5d`.  
5. **Not** permission to flatten 00030/00028 or reset `dca-paper`.  
6. **Not** a CODE licence from PLAN #207 GREEN.  
7. **Not** a SEPA instruction. 10k / 200 / 4120 are paper JSON.  
8. **Not** tax advice. Paper is geen belastingfeit.  
9. **Not** a shop / secretaris page / FACTUUR.

---

## Sources (public URLs)

Fee tables

- https://www.kraken.com/features/fee-schedule
- https://support.kraken.com/articles/cross-platform-fee-tier-changes
- https://blog.kraken.com/product/pro/new-kraken-pro-fee-tiers
- https://support.kraken.com/articles/201893638-how-trading-fees-work-on-kraken
- https://academy.binance.com/en/articles/how-to-calculate-transaction-fees-on-binance
- https://www.binance.com/en/square/post/14541038221378

Clocks / costs / styles

- https://arxiv.org/html/2608.21888 — 15m sign-reversion; 1.3 bp vs 5–20 bp
- https://www.coinquant.ai/blog/building-a-mean-reversion-strategy-in-cryptocurrency-markets-evidence-from-78-backtests
- https://dev.to/nar1frames/i-built-a-crypto-trading-bot-it-lost-to-doing-nothing-355a
- https://arxiv.org/html/2606.00060 — hourly ML / 24h momentum after costs
- https://doi.org/10.1093/rfs/hhaa113 — Liu & Tsyvinski, RFS 2021
- https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4675565 — momentum under realistic costs
- https://www.sciencedirect.com/science/article/pii/S0304405X11002613 — Moskowitz, Ooi, Pedersen, JFE 2012
- https://stratbase.ai/en/blog/transaction-cost-erosion
- https://coinbureau.com/guides/crypto-trading-bot-mistakes-to-avoid
- https://changelly.com/blog/mean-revision-trading-crypto/

Maker / queue

- https://arxiv.org/html/2502.18625v2
- https://marketmaker.cc/en/blog/post/maker-taker-fees-rebates-execution/
- https://dev.to/jacktrader/maker-taker-economics-for-grid-bots-when-post-only-actually-pays-4ihm
- https://www.freqtrade.io/en/stable/backtesting/
- https://cutemarkets.com/blog/same-bar-fills-lookahead-intraday-strategies

Grid density

- https://cryptogates.io/common-grid-trading-mistakes-in-crypto-backtests/
- https://blog.echozero.app/article/grid-trading-bot-performance-in-sideways-markets
- https://voiceofchain.com/academy/grid-bot-profit-calculation
- https://www.novacalculator.com/crypto-web3/trading/crypto-grid-bot-calculator/
- https://dexly.trade/learn/grid-trading-crypto
- https://hummingbot.org/strategies/v2-strategies/executors/gridexecutor/
- https://www.sciencedirect.com/science/article/abs/pii/S0957417421012495
- https://riunet.upv.es/server/api/core/bitstreams/07add8c4-4239-44e7-bf1f-93d66108918d/content

Kraken public REST (this sitting)

- https://docs.kraken.com/api-reference/market-data/get-ohlc-data
- https://docs.kraken.com/api-reference/market-data/get-ticker-information
- https://docs.kraken.com/api-reference/market-data/get-server-time

Desk (cite, do not reseal / reset / CODE)

- https://dca-paper-journal.surge.sh/
- https://github.com/eyeskull2220/solana-invoice/pull/211 — 15m vs 26 bps
- https://github.com/eyeskull2220/solana-invoice/pull/212 — 1-limit fill rate (not a score)
- https://github.com/eyeskull2220/solana-invoice/pull/207 — PLAN lock (**not a CODE licence**)
- https://github.com/eyeskull2220/solana-invoice/pull/214 — REVIEW PLAN GREEN (**not a CODE licence**)
- https://github.com/eyeskull2220/solana-invoice/pull/196 — retired ladder PLAN (**do not CODE**)
- https://github.com/eyeskull2220/solana-invoice/pull/203 — REVIEW-05 PLAN RED
- https://github.com/eyeskull2220/solana-invoice/pull/201 — grind score RED
- https://github.com/eyeskull2220/solana-invoice/pull/200 — STEAL vs H1–H10
- https://github.com/eyeskull2220/solana-invoice/pull/199 — invert method pack
- https://github.com/eyeskull2220/solana-invoice/pull/194 — 2023 slice / Torres
- https://github.com/eyeskull2220/solana-invoice/pull/132 — Coder 01 live fill 1
- https://github.com/eyeskull2220/solana-invoice/pull/144 — Coder 02 invert-only gate

---

## Re-check (copy/paste — public / git only)

```bash
curl -sS 'https://api.kraken.com/0/public/Time'
curl -sS 'https://api.kraken.com/0/public/SystemStatus'
curl -sS 'https://api.kraken.com/0/public/Ticker?pair=XRPEUR'
curl -sS 'https://api.kraken.com/0/public/OHLC?pair=XRPEUR&interval=15'   >/tmp/xrp_15.json
curl -sS 'https://api.kraken.com/0/public/OHLC?pair=XRPEUR&interval=60'   >/tmp/xrp_1h.json
curl -sS 'https://api.kraken.com/0/public/OHLC?pair=XRPEUR&interval=240'  >/tmp/xrp_4h.json
curl -sS 'https://api.kraken.com/0/public/OHLC?pair=XRPEUR&interval=1440' >/tmp/xrp_1d.json
curl -sS 'https://api.kraken.com/0/public/OHLC?pair=XRPEUR&interval=10080' >/tmp/xrp_1w.json
# 15m first bar must be days, not years, behind now (720 ceiling)
# daily first bar ~2024-09 (720 cap). weekly 2023+ must exist.

rg -n 'is_fund_gate|H-C1|H-C2|H-C3|−15.21|15.49|not a CODE licence|0.45' \
  docs/rgy-2026-08-27/coder/RESEARCH-style-clocks-and-costs.md

curl -sS https://dca-paper-journal.surge.sh/ | rg -n 'fills|PAPER-00029|NOT MET|c9689f5d|invert-paper' || true

# Never:
# kraken paper reset --workspace invert-paper
# kraken paper reset --workspace dca-paper
# kraken order …
```

Fee table: https://www.kraken.com/features/fee-schedule (Spot Crypto Tier 1 = 0.40 / 0.80).  
July 2026 change: https://support.kraken.com/articles/cross-platform-fee-tier-changes

Count fund-gate fills only from `PAPER-*` **prints** on **`invert-paper`**. Resting 00030 and open 00028 do not count. 9097 / 7923 / 2779 are **research-book** counts, not a ping.

**`invert-wf-2023` may measure 2023→now. It may not fund. Posted spot fees kill fast clocks and tight grids. What repeats in public literature is slower / wider / low-n, and maker only when the posted maker rate is actually cheap and the queue is honest. H-C1/H-C2/H-C3 not applied. PLAN 207 GREEN is not a CODE licence. INVERT-V2-1LIMIT −15.21% / 15.49% DD stays. invert-paper fill 1 stays. Still paper.**

End. RESEARCHER. Inform Coder. Docs only. `is_fund_gate: false`. VOORBEELD.
