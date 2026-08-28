# RESEARCH — What style on the EUR allowlist survives posted fees?

**Seat:** RESEARCHER · Coder  
**Lens:** one **simple** search, then **broaden** until a workable **paper** path is named (or each class dies with numbers).  
**Date:** 2026-08-28  
**Stamp:** VOORBEELD · paper / simulated · not FACTUUR · not INVOICE · not live-trade advice  
**HEAD (leftover `main` at write):** `2170952`  
**Still paper.** No orders. No keys. No CODE. No live. No Phantom spend. No memecoins.  
**`is_fund_gate`:** **false**

This file answers: **which style, on the CEO EUR allowlist, can historically survive 0.26% taker (and the 0.40 / 0.80 shadows) with return > 0 after fees, fills ≥ 8, and maxDD ≤ 8% on 2023+ data.**

It does **not** restamp invert. Invert is cited as a **dead class** and left ugly. Fail-and-stop on invert is **not** this job.

Operator lock 2026-08-28: paper lane exists so the operator can later fund Kraken when a **named book is proven**. Fund gate (unchanged): return > 0 after fees **AND** ≥ 8 fills **AND** maxDD ≤ 8% on `invert-paper` **OR a later CEO-named book**. `invert-paper` fill **2** is live (`PAPER-00029` + `PAPER-00031`). Gate **2/8 NOT MET**. Still paper. Operator is not the freelancer.

---

## Locks (do not bargain)

| Lock | Status |
|---|---|
| Still paper / no keys / no orders / no CODE / no live | **held** |
| `is_fund_gate` | **false** — this pack does not fund |
| Do not reseal `c9689f5d` | **held** — 8-day lab clip 20 fills / +0.681154% / maxDD 0.890854% is **not** funding proof |
| Do not reset `dca-paper` | **held** — five BTCUSD slices @ 78900.6 stay held. Do not convert to EUR |
| Do not mix 3x sleeve | **held** — FAIL book (6 fills, −2.729078%, maxDD 5.326685%, fills&lt;8). Sleeve only XRP/XLM/HBAR/ADA/ALGO. Never QNT/XDC |
| Allowlist EUR spot only | XRPEUR, XLMEUR, HBAREUR, ADAEUR, QNTEUR, XDCEUR, ALGOEUR. **IOTA is not on Kraken.** Do not invent a pair |
| Invert variants / slower invert clock / maker-invert / CODE from [#207](https://github.com/eyeskull2220/solana-invoice/pull/207) | **STOP.** Not applied. 15m invert with a longer hold is **not** a new recipe |
| New activity | new paper book if CEO names it. **Not** `invert-paper`. **Not** a `dca-paper` reset |

Proven dead (cite, do **not** revive):

| Print | Fills | Return after fees | maxDD | Verdict |
|---|---:|---:|---:|---|
| 15m XRPEUR invert @ 0.26% taker / EUR 200 | — | fee factory unless a **closed pair** banks **> 0.52%**. Typical 15m range **~0.45%** | — | **DEAD** ([PR #211](https://github.com/eyeskull2220/solana-invoice/pull/211)) |
| **`INVERT-V2-1LIMIT` `BINANCE-VISION-XRPEUR`** | **2779** | **−15.21%** | **15.49%** | **FAIL** |
| D6 Kraken reconstruct (operator lock) | **2665** | **−16.03%** | **16.34%** | **rhymes=True. STOP** |
| invert-v2 day0 TWO-CLIP | 7923 | −40.84% | 41.08% | **FAIL** · not invert · fees **4120** |
| Close-model grind `2bfb1b68` | 9097 | −99.989999% | 99.990007% | **RED** · not invert ([#201](https://github.com/eyeskull2220/solana-invoice/pull/201)) |
| Live `invert-paper` | **2** | mark **−0.0496%** | **~0.0496%** | **NOT MET** (need 8) |
| Sleeve 3x `PF_XRPUSD` | 6 | −2.729078% | 5.326685% | **FAIL fills&lt;8** · not the gate |

Journal this sitting (cite, do not ping / flatten / reset): https://dca-paper-journal.surge.sh/ — fills **2/8**, `PAPER-00029` + `PAPER-00031`, TPs `00030` @ 1.26778 and `00032` @ 1.24496 still open. Cap 2 long. No third buy.

---

## Method (simple first, then broaden)

1. **Simple:** round-trip tax vs typical bar on the **allowlist**, 2023+ where REST can see it. If the tax is larger than the bar, that clock is dead before style is discussed.
2. **Broaden** only after that inequality is numbered: daily/weekly swing, long-term hold of the existing DCA stack, DCA-only, wider grids, maker-only if Kraken Pro Tier 1 0.40% maker is real, other allowlist pairs, 4h/1d clocks.
3. **Public REST only** this sitting. `GET /0/public/Time` → `unixtime` **1787946900** (`Fri, 28 Aug 26 19:55:00 +0000`). `SystemStatus` → `online`. Kraken MCP: unavailable. No keys.
4. **No lookahead in the probe:** Donchian / TSMOM decide on bar `t` using **prior** bars only; fill at bar `t+1` **open**. Paper fee **0.26%** per fill. Book **EUR 10 000**. Clip **EUR 200** (same clip as invert — not a new size cheat).
5. Daily REST is a **720-cap**: first bar **2024-09-07**. It is **not** full 2023. Weekly REST **is** full 2023+ (`n=191` weeks, 2023-01-05 → 2026-08-27) for XRPEUR / XLMEUR / ADAEUR / QNTEUR / ALGOEUR. HBAR lists **2025-07-10**. XDC lists **2025-08-28**. Do not call those two “2023+”.

Engine identity (not a WFO of α):

```text
fee_drag ≈ n_fills × clip × rate
paper 0.26% taker RT = 0.52%
Tier 1 maker RT (since 2026-07-09) = 0.80%
Tier 1 taker RT                    = 1.60%
```

EUR 200 does not change the **percent**. It caps **euros** per fill. Invert died on **count**. A survivor has to cut **n**, or capture a move **>> 0.52%**, or both.

---

## 1. Simple first — which clocks on the allowlist even contain 0.52%?

Kraken public `OHLC` this sitting. Median `(H−L)/mid`. Shadows included so Coder does not treat 0.26% as the live entry rate.

| Pair | Clock | Window | n | Median HL | Median \|C−O\| | Frac HL ≥ 0.52% | ≥ 0.80% | ≥ 1.60% |
|---|---|---|---:|---:|---:|---:|---:|---:|
| **XRPEUR** | 1w | 2023-01-05 → 2026-08-27 | 191 | **12.031%** | 4.358% | 100% | 100% | 100% |
| **XRPEUR** | 1d | 2024-09-07 → 2026-08-28 | 721 | **4.456%** | 1.691% | 100% | 100% | 96.8% |
| **XRPEUR** | 4h | 2026-04-30 → 2026-08-28 **now-tape** | 721 | **1.210%** | 0.491% | 93.2% | — | — |
| XLMEUR | 1w | 2023-01-05 → 2026-08-27 | 191 | 12.635% | 5.025% | 100% | 100% | 100% |
| XLMEUR | 1d | 2024-09-07 → 2026-08-28 | 721 | 4.981% | 2.102% | 100% | 100% | 98.2% |
| ADAEUR | 1w | 2023-01-05 → 2026-08-27 | 191 | 14.560% | 5.355% | 100% | 100% | 100% |
| ADAEUR | 1d | 2024-09-07 → 2026-08-28 | 721 | 5.785% | 2.391% | 100% | 100% | 99.4% |
| ALGOEUR | 1w | 2023-01-05 → 2026-08-27 | 191 | 16.074% | 6.079% | 100% | 100% | 100% |
| QNTEUR | 1w | 2023-01-05 → 2026-08-27 | 191 | 14.477% | 4.087% | 100% | 100% | 100% |
| HBAREUR | 1w | listing 2025-07-10 → 2026-08-27 | 60 | 12.416% | 4.733% | 100% | 100% | 100% |
| XDCEUR | 1w | listing 2025-08-28 → 2026-08-27 | 53 | 9.962% | 3.193% | 100% | 100% | 100% |

√time steal from [#211](https://github.com/eyeskull2220/solana-invoice/pull/211) / [#217](https://github.com/eyeskull2220/solana-invoice/pull/217), rechecked: typical **15m** XRPEUR range **~0.45–0.47%** vs RT **0.52%**. A one-bar 15m harvest is underwater at taker 26 bps. **Do not propose 15m invert with a longer hold as “new.”**

**Simple answer:** on this allowlist, **days and weeks contain the tax**. Fifteen minutes does not. Four-hour **open-to-close** on the now-tape (median **0.49%**) is still a knife vs 0.52%. Geometry is not a PnL. It only tells you which clocks are *allowed to be asked*.

---

## 2. Broaden — classes opened, with the number that killed each

Probe book = EUR 10 000, fee **0.26%** per fill, no lookahead. **Full** = all cash when in. **Clip** = EUR 200, one long, rest cash (invert’s clip, not a new lever).

### Class A — 15m invert / fade / 1-limit swap (cite only)

**Killed.** 2779 / −15.21% / 15.49% DD. D6 reconstruct 2665 / −16.03% / 16.34% / rhymes. Fee identity: `2779 × 200 × 0.0026 = 1445.08 EUR` (~14.45% of 10k). Typical 15m range ~0.45% does not bank 0.52%. arXiv:2608.21888: 15m sign-reversion peaks **~1.3 bp** gross; **0 of 183** Binance pairs clear **5 bp**. Desk tax is **52 bp** RT. **Not revived. Not slower-clock invert. Not maker-invert.**

### Class B — 4h trend (same Donchian rule, faster clock)

**Killed as a 2023+ recipe.** Public Kraken 0.26% Donchian ([nar1-frames, DEV 2026-08-21](https://dev.to/nar1frames/i-built-a-crypto-trading-bot-it-lost-to-doing-nothing-355a)): **4h −6.01%** / 61 trades / 11.4%/yr fees; **1m −25.18%, zero wins**. This sitting’s XRPEUR 4h now-tape (2026-04-30 → 2026-08-28 only): full-book Donchian 20/10 **+18.206% / maxDD 14.870% / 18 fills** — return can print on a short tape; **DD fails 8%**. Clip-sized 4h “PASS” on four months is a **size artifact**, not a 2023+ proof. **Do not pick 4h.**

### Class C — Full-book daily/weekly trend on the allowlist

**Killed by maxDD.** Same Donchian, 100% cash when in:

| Pair | Clock | Fills | Return | maxDD | Time-in |
|---|---|---:|---:|---:|---:|
| XRPEUR | weekly 4/2 (≈20d/10d) 2023+ | 17 | **+181.970%** | **55.531%** | 42% |
| XRPEUR | daily 20/10 REST 2024-09+ | 19 | **+148.409%** | **55.670%** | 26% |
| XLMEUR | daily 20/10 REST | 21 | +128.495% | 58.875% | 22% |
| ADAEUR | daily 20/10 REST | 19 | −22.738% | 74.864% | 26% |
| ALGOEUR | daily 20/10 REST | 19 | +43.120% | 62.473% | 29% |
| QNTEUR | daily 20/10 REST | 13 | +47.689% | 48.327% | 24% |

Return can be large. **maxDD is turtle-on-alts: 48–75%.** Gate is **≤ 8%**. Full-book trend is not the path. (nar1-frames’ **4% DD vs BTC −53%** was BTC + 80% flat. XRP trends are larger; a 10-bar exit still leaves a 50%+ peak-to-trough while you are in.)

### Class D — Long-term hold of the existing DCA stack

**Killed by fills.** `dca-paper` is five BTCUSD slices @ 78900.6, **held**. Journal this sitting: equity **9996.66**, uPnL **−3.34 (−0.033%)**, **5 fills**. Gate needs **≥ 8**. Hold-only cannot mint fills. BTC is **not** on the EUR new-activity allowlist. **Do not sell it. Do not convert. Do not reset.**

### Class E — New DCA-only on the EUR allowlist (calendar buy, never sell)

**Killed by maxDD** (and often by return on the 2024-09+ daily window). Weekly 2023+, clip 200, buy every 4 weeks (≈ monthly) or every week until cash is gone:

| Pair | Recipe | Fills | Return | maxDD |
|---|---|---:|---:|---:|
| XRPEUR | dca_4w | 48 | +60.790% | **67.778%** |
| XRPEUR | dca_1w | 50 | +161.859% | **71.468%** |
| XLMEUR | dca_4w | 48 | +15.985% | **67.762%** |
| ADAEUR | dca_4w | 48 | −47.486% | **81.085%** |
| ALGOEUR | dca_4w | 48 | −42.754% | **75.839%** |
| QNTEUR | dca_4w | 48 | −34.092% | **51.312%** |
| XRPEUR | daily dca_7d REST | 50 | **−6.381%** | **71.633%** |

Fills clear 8. **DD does not.** DCA never exits the dump. XRP hold 2023+ itself: **+262.528% / maxDD 71.468% / fills=1**. The bull is real. The 8% DD gate is not a hold gate.

### Class F — Maker-only as a tax cut

**Killed as a rescue, kept as a shadow.** Kraken Pro **Tier 1 since 2026-07-09** is **0.40% maker / 0.80% taker** ([fee schedule](https://www.kraken.com/features/fee-schedule); [cross-platform tiers](https://support.kraken.com/articles/cross-platform-fee-tier-changes); [Kraken blog](https://blog.kraken.com/product/pro/new-kraken-pro-fee-tiers)). Paper 0.26% taker RT **0.52%**. Live Tier 1 **maker** RT **0.80%** — **worse**, not better. AoP **$20k** unlocks Tier 3 (0.22 / 0.38). Paper 10k EUR is **not** that. Queue / missed fills / adverse selection remain ([arXiv:2502.18625](https://arxiv.org/html/2502.18625v2)). **Do not score invert as maker. Do not pretend post-only is a rebate at Tier 1.**

### Class G — Wider grid (3 buy / 3 sell, spacing ≥ 2× fee)

**Not the candidate.** Spacing identity is real: net per cycle ≈ `gap − 2×fee`. At 0.26%, a **2%** gap is ~3.8× the tax; weekly XRP median HL **12%** can complete it. Death is **inventory in a trend** (Neutralis / Hummingbot): downtrend bags the coin; uptrend sells the inventory and **misses** the 2024 XRP hold (+262%). Desk already has an empty `grid-paper` track. A 3×200 clip dump of 20% is only **1.2%** of 10k — DD can look green **by size** while the style is still the wrong movie. **Do not mix onto `dca-paper`. Do not copy invert rungs into a grid.**

### Class H — Other allowlist pairs as the first book

| Pair | Why not first |
|---|---|
| XLMEUR | Clip Donchian **does** PASS (below). Slightly worse expanding DD (4.21% vs XRP 2.78%). Backup, not the named recipe |
| ADAEUR | Clip daily PASS is thin (**+1.022%**). Full-book **−22.7%**. Hold **−31% / 88% DD** |
| ALGOEUR | Clip daily PASS **+2.156%**. Hold **−58% / 85% DD** |
| QNTEUR | Weekly clip Donchian **−1.467%** (return fail). Daily clip PASS **+1.332%** only on REST 2024-09+ |
| HBAREUR | Lists **2025-07-10**. Weekly Donchian 4/2: **3 fills, −10.2% full**. Not 2023+ |
| XDCEUR | Lists **2025-08-28**. Weekly Donchian 4/2: **0 fills**. Not 2023+ |
| IOTA | **Unknown asset pair** on Kraken. Do not invent |

### Class I — 3x sleeve

**Killed and forbidden to mix.** 6 fills / −2.73% / 5.33% DD / FAIL fills&lt;8. Funding + liquidation are extra deaths spot does not have.

---

## 3. The class that did not die — clip-sized daily Donchian (low n)

Same published Turtle rule as nar1-frames (**20-bar high in, 10-bar low out**, long-only spot, cash when flat), **EUR 200 clip**, one position. Fees are a rounding error because **n is tens, not thousands**.

```text
19 fills × 200 EUR × 0.0026 = 9.88 EUR   (0.099% of 10k)
2779 fills × 200 EUR × 0.0026 = 1445.08 EUR  (invert 1-limit)
```

Daily median HL **4.46%** vs RT **0.52%** ≈ **8.6×** the tax sitting in a typical day. Capture is not 100%. It does not need to be: one held trend that banks tens of percent pays for many scratches. Closed-trade median gross this sitting was **negative** (−4.6% daily / −4.1% weekly) with a **fat right tail** (best closed weekly RT **+300%**). That is trend-follow, not a fade with a high win rate.

### Probe (paper 0.26%, clip 200, one long)

| Pair | Clock | Window | Fills | Return | maxDD | Time-in | vs gate |
|---|---|---|---:|---:|---:|---:|---|
| **XRPEUR** | weekly 4/2 | **2023-01-05 → 2026-08-27** | **17** | **+5.395%** | **2.780%** | 42% | **PASS** |
| **XRPEUR** | daily 20/10 | 2024-09-07 → 2026-08-28 | **19** | **+6.150%** | **3.141%** | 26% | **PASS** |
| XLMEUR | weekly 4/2 | 2023-01-05 → 2026-08-27 | 16 | +3.743% | 4.214% | 37% | PASS (backup) |
| XLMEUR | daily 20/10 | 2024-09-07 → 2026-08-28 | 21 | +5.626% | 3.654% | 22% | PASS (backup) |
| ADAEUR | daily 20/10 | 2024-09-07 → 2026-08-28 | 19 | +1.022% | 3.001% | 26% | thin PASS |
| ALGOEUR | daily 20/10 | 2024-09-07 → 2026-08-28 | 19 | +2.156% | 3.473% | 29% | PASS (weaker) |

Shadows on **XRPEUR daily 20/10 clip** (same fills, posted tables):

| Fee column | Per fill | Return | maxDD | vs gate |
|---|---:|---:|---:|---|
| Paper taker (engine) | 0.26% | **+6.150%** | **3.141%** | **PASS** |
| Tier 1 maker | 0.40% | **+6.080%** | **3.183%** | **PASS** |
| Tier 1 taker | 0.80% | **+5.880%** | **3.305%** | **PASS** |

Maker is **not** why this lives. **Low n** is why the 0.80% shadow still clears. At invert’s 2779 fills the same shadow is a mill.

### Expanding walk-forward (published 20/10 — **not** a searched lookback)

Calendar **years** often have **&lt; 8 fills** (Turtle is low-n). Do not use a single year as a gate. **Expand from 2023** (weekly native) / from REST start (daily):

**XRPEUR weekly 4/2 clip 0.26%** (Kraken-native 2023+):

| Window | n weeks | Fills | Return | maxDD | Gate |
|---|---:|---:|---:|---:|---|
| 2023 only | 52 | 7 | +0.383% | 0.795% | fail fills&lt;8 |
| **2023 → 2024** | 104 | **11** | **+5.619%** | **1.672%** | **PASS** |
| **2023 → 2025** | 156 | **16** | **+5.448%** | **2.780%** | **PASS** |
| **2023 → 2026-08-27** | 191 | **17** | **+5.397%** | **2.780%** | **PASS** |

**XRPEUR daily 20/10 clip 0.26%** (REST 720-cap; first bar 2024-09-07):

| Window | n days | Fills | Return | maxDD | Gate |
|---|---:|---:|---:|---:|---|
| REST → 2024 | 116 | 3 | +5.070% | 2.111% | fail fills&lt;8 |
| **REST → 2025** | 481 | **10** | **+6.480%** | **2.962%** | **PASS** |
| **REST → 2026-08-28** | 721 | **19** | **+6.153%** | **3.141%** | **PASS** |

Isolated 2025 / 2026 daily slices were **slightly negative** on the clip (−0.44% / −0.33%). That is a **chop year**, not a hidden invert. The expanding window still PASSES because the 2024 XRP trend is **not fully given back** — the 10-bar exit got out. That is the whole point of the style. A later PLAN that WFO’d lookbacks on 2025 to erase the scratch would be **Pardo**. **Do not.**

Public cousin (BTC, Kraken 0.26%, honest walk-forward, **not** this allowlist): nar1-frames Donchian **1d +4.33% / 14 trades / 3 years / ~80% flat / 4% DD vs BTC −53%**. Same clock family. Different coin. This sitting’s XRP **clip** replica is the allowlist number; the BTC study is the **fee × timeframe** steal, not a paste.

---

## 4. ONE candidate recipe (paper, not the fund gate)

Name: **`DONCH-D20-XRPEUR-CLIP200`**  
Proposed paper book (CEO must name it before it is a gate): **`donch-paper`**. Create later. **Do not** init it in this PR. **Do not** touch `invert-paper` or `dca-paper`.

| Field | Value |
|---|---|
| **Pair** | **XRPEUR** (allowlist; deepest 2023+ Kraken tape; listing 2017-05-18). XLMEUR is the **backup**, not the named recipe |
| **Clock** | **1d**. Entry: close **above prior 20-day high**. Exit: close **below prior 10-day low**. Long-only spot. Cash when flat. **Weekly 4/2** is the Kraken-native **2023+ proxy** until `XRPEUR_1440.csv` from the official OHLCVT ZIP exists ([PR #210](https://github.com/eyeskull2220/solana-invoice/pull/210)) |
| **Clip** | **EUR 200**, **one** long at a time, rest of the 10k stays **cash**. Same clip as invert. Full-book is **Class C FAIL** (maxDD ~56%) — clip is **load-bearing** for the 8% DD gate |
| **Fee assumption** | **Primary: 0.26% taker** (paper engine). **Shadows: 0.40% maker / 0.80% taker** (Kraken Pro Tier 1 since 2026-07-09). Do not score a maker rebate. Kraken+ Instant Buy **1%** is a **different product** — do not use it |
| **Why it can clear 0.52%** | Daily median HL **4.46%** (2024-09+) and weekly **12.03%** (2023+) **contain** the tax. Hold is **days to weeks**, not 13 bars of 15m. Fee drag at 19 fills is **EUR 9.88**, not EUR 1445. Shadows still PASS on the clip because **n is small**, not because maker is cheaper |
| **How we walk-forward it** | See §5. Published 20/10. No WFO of lookback. Expanding windows from 2023. Next-bar open fill. Three fee columns. New book. Still `is_fund_gate: false` until CEO says |
| **Why it is not invert-in-a-trench-coat** | See §6 |

This is **not** “15m invert that waits longer.” Decision clock is **daily**. Trigger is a **breakout**, not a fib pair. After a fill there is **no swap of two prices**. The exit is a **trailing 10-day low**, not the other rung.

---

## 5. Walk-forward (how Coder would measure — not CODE this sitting)

PLAN-stage only if CEO asks. **PLAN #207 GREEN is not a CODE licence** and is **invert**. This recipe is a **new hash** if it ever ships.

1. **Dump.** Prefer official OHLCVT `XRPEUR_1440.csv` 2023-01-01 → now ([PR #210](https://github.com/eyeskull2220/solana-invoice/pull/210) Drive IDs rotate — scrape the support article). Until that file exists, **weekly 4/2 on REST** is the 2023+ Kraken-native score; daily 20/10 REST is the 2024-09+ replica. Do **not** relabel Vision as Kraken. Do **not** forward-fill empty days.
2. **Engine lie-detector.** Signal on **closed** bar `t` from bars `t-N … t-1` only. Fill at `t+1` **open**. Same-bar fill is lookahead ([Freqtrade](https://www.freqtrade.io/en/stable/backtesting/); [CuteMarkets](https://cutemarkets.com/blog/same-bar-fills-lookahead-intraday-strategies)).
3. **Params are published, not searched.** Donchian **20 / 10**. Clip **200**. One long. No RSI. No fib. No second pair. No 15m touch layer “just for fills.”
4. **Windows.** Expanding: 2023→2024, 2023→2025, 2023→now. A window without **≥ 8 fills** is **not scored as a gate** (it is a **warmup / low-n** note). Do not promote a single chop year.
5. **Fee columns.** 0.26 / 0.40 / 0.80 per fill. PASS only if **paper 0.26%** meets return > 0 **and** fills ≥ 8 **and** maxDD ≤ 8%, **and** 0.80% shadow still has return > 0 (DD may rise; it must stay ≤ 8% on the clip).
6. **Paper book.** New workspace `donch-paper`, EUR 10 000, **after** CEO names it. Live paper: at most **one** rest (buy-stop / sell-stop), not a fib catalog. **Do not** ping `invert-paper`. **Do not** reset `dca-paper`.
7. **Promotion.** **No** until CEO names this book as a gate candidate. `invert-paper` stays the current fund gate at **2/8**.

---

## 6. Why this is not invert-in-a-trench-coat

| Invert (dead on 15m) | This recipe |
|---|---|
| Two prices swap jobs after a fill | **No pair.** Breakout in, trail out |
| Fib catalog / 24h H latch | **No fib.** Prior 20-day high / 10-day low |
| 15m bar-close | **1d** bar-close (weekly 4/2 only as 2023 REST proxy) |
| Re-arm the filled price on the opposite print | **Stay flat** after exit until a **new** 20-day high |
| Fade between two rails | **Follow** the move; chop is skipped (low n) |
| ~2 fills/day for years (2779) | **~10 fills/year** (17–19 on the probe) |
| Closed pair must bank > 0.52% **inside a tight gap** | Captured move is a **trend**, typically **>> 0.52%** or the trade is a scratch and you are **out** |
| Spot cannot short the fade → stuck inventory | Spot long-only **and** a trail that **exits**. Stuck inventory is a **skipped year**, not a sitting TP |

Putting Donchian **onto invert** (H-C4 / H-TS5 in [#217](https://github.com/eyeskull2220/solana-invoice/pull/217) / [#216](https://github.com/eyeskull2220/solana-invoice/pull/216)) is still **forbidden**. This page names a **different book**.

---

## 7. What this file is not claiming

- **Not the fund gate.** `invert-paper` is still **2/8 NOT MET**. `is_fund_gate: false`.
- **Not** a full-book Turtle. Full-book maxDD **~56%** on XRPEUR. Clip is required for the 8% line.
- **Not** “beat buy-and-hold.” XRP hold 2023+ was **+262% / 71% DD**. This recipe is a **stay-under-8%-DD** harvest of part of that trend. nar1-frames already said the quiet part: +4.33% vs BTC hold +127%.
- **Not** a 2023 daily native dump. Daily REST starts **2024-09-07**. Weekly 4/2 is the 2023+ stand-in. OHLCVT 1440 is the later D6-class dump for **this** recipe (a new score, not a restamp of 2665).
- **Not** permission to WFO 20/10 on 2025 so chop disappears.
- **Not** CODE, orders, keys, reseal, `dca-paper` reset, sleeve mix, memecoins, Phantom spend, IOTA, or a 15m rewrite.

---

## Verdict

| Probe | Color |
|---|---|
| 15m invert / D6 reconstruct / 1-limit 2779 | **DEAD** · cited · not this page’s score |
| 4h Donchian as 2023+ recipe | **RED** (nar1-frames −6.01%; now-tape full DD 14.87%) |
| Full-book 1d/1w trend on allowlist | **RED** vs 8% DD (XRP ~56%) |
| Hold / new DCA on allowlist | **RED** vs 8% DD (XRP hold 71%; DCA 67–88%) |
| Existing `dca-paper` hold | **RED** vs fills ≥ 8 (5 fills). **Do not reset** |
| Maker as a Tier 1 tax cut | **RED** (0.40% maker **raises** RT to 0.80%) |
| Wide grid as the named path | **YELLOW** geometry · **RED** as the one recipe (trend inventory) |
| HBAR / XDC / IOTA as 2023+ first book | **RED** (listing / unknown pair) |
| 3x sleeve mixed in | **RED** |
| **`DONCH-D20-XRPEUR-CLIP200`** weekly 4/2 2023+ expanding | **GREEN as a paper candidate** · 17 fills · **+5.40%** · **2.78% DD** · shadows on daily clip still PASS |
| This file as fund gate / live / CODE | **RED** |

**Overall:** the allowlist **can** historically survive 0.26% taker (and the 0.40/0.80 shadows) if you take **XRPEUR**, a **daily Donchian 20/10**, **EUR 200**, **one long**, and you **do not** invert. Expanding 2023→now on Kraken weekly PASSES the three-part gate **as a research probe**. It is **not** funded. CEO names the book or it stays a memo.

**Promotion: no.** Stay paper. Gate on `invert-paper` remains **NOT MET** (fill 2/8).

---

## Sources (public URLs)

This sitting (Kraken REST, 2026-08-28 ~19:55Z)

- `GET https://api.kraken.com/0/public/Time` → `1787946900`
- `GET https://api.kraken.com/0/public/SystemStatus` → `online`
- `GET https://api.kraken.com/0/public/Ticker?pair=XRPEUR,XLMEUR,HBAREUR,ADAEUR,QNTEUR,XDCEUR,ALGOEUR`
- `GET https://api.kraken.com/0/public/OHLC?pair=…&interval=10080|1440|240`
- Result keys: `XXRPZEUR`, `XXLMZEUR`, `HBAREUR`, `ADAEUR`, `QNTEUR`, `XDCEUR`, `ALGOEUR`

Fee tables

- https://www.kraken.com/features/fee-schedule
- https://support.kraken.com/articles/cross-platform-fee-tier-changes
- https://blog.kraken.com/product/pro/new-kraken-pro-fee-tiers
- https://support.kraken.com/articles/201893638-how-trading-fees-work-on-kraken

Clocks / costs / styles

- https://dev.to/nar1frames/i-built-a-crypto-trading-bot-it-lost-to-doing-nothing-355a — Kraken 0.26% Donchian 1d +4.33% / 4h −6.01% / 1m −25%
- https://arxiv.org/html/2608.21888 — 15m sign-reversion 1.3 bp vs 5–20 bp
- https://www.coinquant.ai/blog/building-a-mean-reversion-strategy-in-cryptocurrency-markets-evidence-from-78-backtests — 15m avg −14.4%
- https://doi.org/10.1093/rfs/hhaa113 — Liu & Tsyvinski, crypto TSMOM is **weeks**
- https://www.aqr.com/Insights/Research/Journal-Article/A-Century-of-Evidence-on-Trend-Following-Investing
- https://arxiv.org/html/2502.18625v2 — maker fill p&lt;1, adverse selection
- https://hummingbot.org/strategies/v2-strategies/executors/gridexecutor/
- https://www.kraken.com/learn/finance/dollar-cost-averaging
- https://docs.kraken.com/api-reference/market-data/get-ohlc-data — 720-cap
- https://docs.kraken.com/exchange/guides/general/historical-data
- https://support.kraken.com/articles/360047124832-downloadable-historical-ohlcvt-open-high-low-close-volume-trades-data

Desk (cite, do not reseal / reset / CODE / ping)

- https://dca-paper-journal.surge.sh/ — fill **2/8**, `00029`+`00031`, TPs open, `dca-paper` held
- https://github.com/eyeskull2220/solana-invoice/pull/211 — 15m vs 26 bps
- https://github.com/eyeskull2220/solana-invoice/pull/216 — styles broad (H- not applied)
- https://github.com/eyeskull2220/solana-invoice/pull/217 — clocks vs fees (1d cluster; **not** a named recipe)
- https://github.com/eyeskull2220/solana-invoice/pull/210 — OHLCVT / Trades how-to
- https://github.com/eyeskull2220/solana-invoice/pull/209 — D6 path (do not hunt a prettier invert)
- https://github.com/eyeskull2220/solana-invoice/pull/207 — invert PLAN lock (**not CODE**, **not this recipe**)
- https://github.com/eyeskull2220/solana-invoice/pull/201 — 9097 is not invert

---

## Out of scope (honoured)

- No paper or live Kraken orders  
- No API keys  
- No reseal of `c9689f5d`  
- No `invert-paper` / `dca-paper` reset  
- No flatten of `PAPER-00030` / `PAPER-00032`  
- No invert rewrite, no slower-clock invert, no maker-invert, no CODE from #207  
- No `donch-paper` init in this PR  
- No memecoins, no IOTA, no extra coins, no live, no Phantom spend  
- No journal HTML patch, no shop HTML, no FACTUUR, no invented KBO  

**Promotion: no.** Stay paper. Gate NOT MET. `is_fund_gate: false`.

---

## Re-check (copy/paste — public / git only)

```bash
curl -sS -A 'rgy-research-what-survives-fees-2026-08-28' 'https://api.kraken.com/0/public/Time'
curl -sS -A 'rgy-research-what-survives-fees-2026-08-28' 'https://api.kraken.com/0/public/SystemStatus'
curl -sS -A 'rgy-research-what-survives-fees-2026-08-28' \
  'https://api.kraken.com/0/public/Ticker?pair=XRPEUR,XLMEUR,HBAREUR,ADAEUR,QNTEUR,XDCEUR,ALGOEUR'
# IOTA must stay unknown:
curl -sS -A 'rgy-research-what-survives-fees-2026-08-28' \
  'https://api.kraken.com/0/public/Ticker?pair=IOTAEUR'
curl -sS -A 'rgy-research-what-survives-fees-2026-08-28' \
  'https://api.kraken.com/0/public/OHLC?pair=XRPEUR&interval=10080' | python3 -c \
  "import json,sys,datetime as dt; d=json.load(sys.stdin); k=next(x for x in d['result'] if x!='last'); r=d['result'][k]; print(k,len(r),dt.datetime.utcfromtimestamp(r[0][0]).date(),dt.datetime.utcfromtimestamp(r[-1][0]).date())"
# weekly first bar must be 2017-era; 2023+ n ~191

rg -n 'DONCH-D20-XRPEUR-CLIP200|is_fund_gate|2779|2665|do not CODE|2/8' \
  docs/rgy-2026-08-28/coder/RESEARCH-what-survives-fees.md

curl -sS https://dca-paper-journal.surge.sh/ | rg -n 'fills|PAPER-00029|PAPER-00031|NOT MET|c9689f5d|invert-paper|dca-paper' || true

# Never:
# kraken paper reset --workspace invert-paper
# kraken paper reset --workspace dca-paper
# kraken paper init --workspace donch-paper
# kraken order …
```

Count fund-gate fills only from `PAPER-*` **prints** on **`invert-paper`**. Resting `00030` / `00032` do not count. 17 / 19 are **research-book** counts, not a ping.

**Posted spot fees kill 15m invert and 4h churn. Hold/DCA on this allowlist clears return and fills and dies on 8% DD. Full-book Donchian dies on 8% DD. Clip-sized XRPEUR daily Donchian 20/10 is the one paper candidate that historically clears 0.52% (and the 0.40/0.80 shadows) with fills ≥ 8 and maxDD ≤ 8% on 2023+ weekly / 2024-09+ daily REST. It is not invert. CEO names the book or it is not the gate. Still paper.**

End. RESEARCHER. Docs only. `is_fund_gate: false`. VOORBEELD.
