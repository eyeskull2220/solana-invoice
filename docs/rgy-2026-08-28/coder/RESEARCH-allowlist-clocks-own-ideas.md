# RESEARCH — Allowlist clocks + own ideas (non-invert paper path)

**Seat:** RESEARCHER · Inform **Coder**  
**Lens:** OWN-IDEAS pass. Steal clock / tape / fees. Invent style **only** as labeled **`H-`**. **No invert variants. No invert autopsy.**  
**Date:** 2026-08-28  
**Stamp:** VOORBEELD · paper / simulated · not FACTUUR · not INVOICE · not live-trade advice  
**HEAD (leftover `main` at write):** `2170952`  
**Still paper.** `is_fund_gate: false`. invert-paper fill **2** stays. Do not reset `dca-paper`. **No IOTA. No memecoins. No live. No keys. No CODE.** Do not CODE from PLAN [#196](https://github.com/eyeskull2220/solana-invoice/pull/196) or PLAN [#207](https://github.com/eyeskull2220/solana-invoice/pull/207).

**CEO question:** which **non-invert** paper path on **XRPEUR XLMEUR HBAREUR ADAEUR QNTEUR XDCEUR ALGOEUR** can survive fees **and** live inside the gate (return > 0 after fees, **≥ 8 fills**, maxDD ≤ 8%).

Vision 1-limit (`INVERT-V2-1LIMIT` on `BINANCE-VISION-XRPEUR`: **−15.21% / 15.49% DD / 2779 fills**) and D6 (Kraken-native 15m path, [#209](https://github.com/eyeskull2220/solana-invoice/pull/209)) both **FAIL** the gate; this page does not re-autopsy invert.

Sibling clocks/fees (STEAL inequality, do not reprint invert): [#211](https://github.com/eyeskull2220/solana-invoice/pull/211) 15m vs 26 bps · [#217](https://github.com/eyeskull2220/solana-invoice/pull/217) style clocks · [#216](https://github.com/eyeskull2220/solana-invoice/pull/216) styles broad. This file **broadens to the seven-pair allowlist** and asks which **clock × style** can print **n high enough for ≥ 8** without becoming a fee mill.

---

## Locks (this sitting)

| Lock | Status |
|---|---|
| Still paper / no keys / no orders / no CODE | **GREEN** |
| `is_fund_gate` | **false** |
| invert-paper fill **2** stays (`PAPER-00029`, `PAPER-00031`) | **GREEN** — not this file |
| `dca-paper` not reset (five BTCUSD slices held) | **GREEN** |
| No invert variants / no invert rewrite | **GREEN** |
| No PLAN #196 / #207 CODE | **GREEN** |
| No IOTA / no memecoins / no live | **GREEN** |
| Do not reseal `c9689f5d` | **GREEN** — cited, not rotated |
| Sleeve 3x is **negative control**, not a survival path | **GREEN** |
| Own ideas labeled **`H-`**, not applied | **GREEN** |
| VOORBEELD | **GREEN** |

Live gate book (untouched): fills **2/8**. `PAPER-00029` buy XRPEUR @ **1.24496**. `PAPER-00031` buy XRPEUR @ **1.23084**. Resting TPs `PAPER-00030` @ **1.26778** and `PAPER-00032` @ **1.24496** are **not** fills. Gate **NOT MET**.

Kraken MCP this VM: **error / undiscoverable**. Public REST only. Server clock: `GET /0/public/Time` → `unixtime` **1787946731** (`Fri, 28 Aug 26 19:52:11 +0000`). `GET /0/public/SystemStatus` → `online`.

---

## Method of this paper

1. **Steal** the fee identity and the 15m death from [#211](https://github.com/eyeskull2220/solana-invoice/pull/211) / [#217](https://github.com/eyeskull2220/solana-invoice/pull/217). Do not re-score invert.
2. **Fetch** public Kraken OHLC last-720 (committed bars; drop the uncommitted last row) for the seven allowlist pairs at **1h / 4h / 1d / 1w**. REST has **no 12h** (`interval=720` → `EGeneral:Invalid arguments`). 12h is **aggregated from 4h** (three consecutive 4h bars, UTC 12h buckets). Venue + range labeled. Not a 2023 dump.
3. **Count how often a 0.52% / 0.80% / 1.60% move prints** as bar **range** `(H−L)/mid` and as bar **body** `|C−O|/mid`. Range is the optimistic room. Body is the honest capture proxy. Neither is a fill.
4. **Styles** on those clocks: mean-reversion, trend-follow, DCA drip, wide grid, hold+trim. Ask which naturally keep **n** in the gate band: **≥ 8 prints** and **≥ 8 CLOSED clips in ~90d**, without 15m grinding, and without thousands of fills/year.
5. **Pair personality** from the same sitting’s ticker + depth + zero-volume 1h bars.
6. **Maker rest** vs posted tables. 0.16% maker is **not** on the current crypto-spot schedule.
7. **Hypotheses `H-`.** Not applied. Not invert. Not a score.

**Not a score.** No invented equity curve. No dump started.

---

## Verdict (for Coder / CEO)

| Claim | Color |
|---|---|
| 15m / 1h harvest of a typical bar at paper **0.26%** taker (RT **0.52%**) | **DEAD** on jumpy and thin names alike. 1h median **range** on this 30d now-tape is **0.17–0.87%**; median **body** is **0.09–0.42%**. |
| 4h as a taker harvest at 0.26% | **DEAD / knife.** Median 4h body **0.45–0.79%** vs RT 0.52%. Public Kraken 0.26% Donchian **dies on 4h** ([nar1-frames](https://dev.to/nar1frames/i-built-a-crypto-trading-bot-it-lost-to-doing-nothing-355a)). |
| **12h** (4h-agg, ~120d) at 0.26% | **MAYBE geometry.** Median 12h **range** **1.99–3.41%**, median **body** **0.86–1.29%**. Clears 0.52% often; **does not** clear live Tier 1 taker RT **1.60%** on a typical body. |
| **1d** at 0.26%, **low n**, one lot | **MAYBE / try-next cluster.** Daily median range **3.75–5.84%**, median body **1.45–2.54%**. Room vs 0.52% and vs 0.80% RT. Literature: daily trend can print a small plus; daily fade is still regime-fragile. |
| **1w** at 0.26% | **MAYBE on 1y, knife on 90d n-gate.** Weekly body usually ≫ fee. **~13 weeks in 90d** — 8 closed clips needs you to complete most weeks. Easy on 1y (52 weeks). |
| Same clocks at **0.80%** per side (live Tier 1 taker; RT **1.60%**) | **1h/4h DEAD. 12h DEAD-on-body. 1d MAYBE if you capture a large fraction of the day. 1w MAYBE.** |
| Tight MR / dense grid / 1h fade | **DEAD** at both 0.26 and 0.80. n is the mill. |
| DCA drip without trim | **DEAD vs closed-clip count.** Buys print; clips do not close. `dca-paper` stays held — not this path. |
| Wide grid (gap ≥ 2× RT, few levels) | **MAYBE** on 12h/1d jumpy names. **DEAD** if 3×3 around last on a 1h clock. |
| Hold+trim on 1d / 12h, jumpy EUR, clip 200 | **TRY NEXT (`H-A1`).** n can be *designed* into 8–16 closed clips / 90d. |
| Thin+slow (QNT, XDC) as a fee gift | **HURTS the 8-fill gate more than it helps.** Fewer fake 1h prints, worse slip, listing too young for a 1y Kraken-EUR walk-forward on **HBAR** and **XDC**. |
| Paper LIMIT below last = maker 0.16% | **RED as a slogan.** Posted Tier 1 maker is **0.40%** (fetched 2026-08-28). 0.16% is legacy Starter / stale marketing / stablecoin table — **not** these pairs. |
| Kill-switch sleeve 3x as a survival sleeve | **RED.** Negative control only. Lab clip: **6 fills / −2.73% / maxDD 5.33% / FAIL fills&lt;8**. |
| This file as fund gate / live / keys / CODE | **RED** |

**Overall:** the only non-invert cluster that can **both** clear a 0.52% (and maybe 0.80%) round-trip **and** print **8+ closed clips in 90 days without 15m grinding** is a **12h-or-1d decision clock**, **one lot**, **wide gap**, **hold+trim or slow trend-follow**, on **jumpy** EUR names first (**XRPEUR / ADAEUR / XLMEUR**; ALGO/HBAR as backups). That cluster is **`H-` labeled, not applied, not a score.** QNT/XDC are spot-only personality tests, not the first walk-forward. Still paper.

---

## 1. Fees this sitting (posted tables, not a hoped-for rebate)

Paper primary stays **0.26% per print** (Starter-era taker locked on invert-paper). Shadows **0.40 / 0.80**. Round-trips:

| Column | Per fill | Round-trip | What it is |
|---|---|---|---|
| **Paper primary** | **0.26%** | **0.52%** | Engine default. **Not** live Tier 1. |
| Shadow | **0.40%** | **0.80%** | Matches **live Tier 1 maker** after 2026-07-09 |
| Shadow taker stress | **0.80%** | **1.60%** | Matches **live Tier 1 taker** after 2026-07-09 |
| **Hoped-for maker 0.16%** | 0.16% | 0.32% | **Not on the current crypto-spot table** |

**Kraken Pro Spot Crypto, fetched 2026-08-28** from [fee schedule](https://www.kraken.com/features/fee-schedule) (same numbers as [cross-platform tiers, 9 Jul 2026](https://support.kraken.com/articles/cross-platform-fee-tier-changes) and [Kraken blog 2026-07-09](https://blog.kraken.com/product/pro/new-kraken-pro-fee-tiers)):

| Tier | 30d spot vol / AoP | Maker | Taker |
|---|---|---|---|
| **Tier 1** | $0+ | **0.40%** | **0.80%** |
| Tier 2 | $2.5k+ | 0.30% | 0.60% |
| Tier 3 | $10k+ or $20k AoP | 0.22% | 0.38% |

**0.16% maker is not published for these EUR crypto pairs today.** Where 0.16% *does* appear:

- **Legacy Starter** (pre-2026-07-09) maker 0.16% / taker 0.26% — the paper engine’s memory, not the live table.
- **Stablecoin / FX** schedule at **$50k+** 30d vol: 0.16% / 0.16% ([fee schedule](https://www.kraken.com/features/fee-schedule) “Stablecoin, Pegged Token & FX Pairs”). XRPEUR is **spot crypto**, not that table.
- Stale comparison copy (e.g. [Kraken vs Bitstamp](https://www.kraken.com/learn/kraken-vs-bitstamp)) still says “as low as 0.16% / 0.26%”. **Do not launder marketing into a paper PASS.**

Spot Maker Rebate table (select low-liquidity pairs): Tier 1 **0.38% maker / 0.80% taker**. Still **worse** than paper 0.26%. This sitting did **not** confirm whether QNT/XDC sit on that rebate list. **UNVERIFIED.** Even if they do, rebate does not make 1h bodies pay.

Allowlist pairs are **spot crypto**. Instant Buy waiver / Kraken+ app waiver is **not** Pro/API.

Break-even identity (clip EUR 200, buy+sell): net > 0 iff `(Hi−Lo)/Lo > ~0.521%` at 0.26%, `> ~0.803%` at 0.40%, `> ~1.613%` at 0.80%. **STEAL from [#212](https://github.com/eyeskull2220/solana-invoice/pull/212).** Completing a pair inside the fee is the mill.

---

## 2. Clock ladder — how often 0.52 / 0.80 / 1.60 prints

### 2.1 Venue + range (this sitting)

| Clock | How obtained | Window (typical; pair-dependent) | Label |
|---|---|---|---|
| **1h** | Kraken REST `OHLC interval=60`, last **720 committed** | **2026-07-29 → 2026-08-28** (~30d) | **Kraken last-720 now-tape.** Not 2023. |
| **4h** | `interval=240`, last 720 committed | **2026-04-30 → 2026-08-28** (~120d) | Kraken last-720 |
| **12h** | REST has **no** `interval=720`. **Aggregated** from committed 4h (UTC 12h buckets) | same ~120d, **n ≈ 241** | **Derived from Kraken 4h.** Not a native 12h file. |
| **1d** | `interval=1440`, last 720 committed | **2024-09-07 → 2026-08-27** for XRP/XLM/ADA/QNT/ALGO (**n=720**). **HBAR n=414 from 2025-07-10. XDC n=360 from 2025-09-02.** | Longest honest REST daily. Not full 2023. |
| **1w** | `interval=10080` (listing → now, under 720) | XRP from **2017-05-18** (n=484). HBAR from **2025-07-10** (n=59). XDC from **2025-08-28** (n=52). | Native Kraken weekly. |

Binance Vision *EUR 1h for **2026-07** (probe, not used as the matrix): **XRPEUR / XLMEUR / ADAEUR HTTP 200**. **HBAREUR / QNTEUR / XDCEUR / ALGOEUR HTTP 404**. Vision cannot backfill the thin names. Do not mix Vision 1h into a Kraken-labeled row.

Uncommitted last REST row **dropped**. Empty/zero-volume 1h bars **counted**, not filled.

### 2.2 How to read the tables

- **Range ≥ hurdle** = the bar’s high–low *could* have paid that tax if you captured the whole wick. Optimistic.
- **Body ≥ hurdle** = open-to-close *could* have paid it. Closer to what a hold-through-the-bar captures.
- **Hits / 90d** = scale the REST window to 90 calendar days. A 30d 1h tape scaled to 90d is a **now-tape extrapolation**, not 2023.
- A hit is **not** a fill. Style, queue, and one-lot lock decide how many hits become prints.

### 2.3 1h now-tape (~30d, n=720 committed) — Kraken REST

| Pair | med range | med body | med trades/bar | zero-vol 1h | range ≥0.52% | body ≥0.52% | body ≥0.80% | body ≥1.60% |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| XRPEUR | 0.531% | 0.237% | 238.5 | 0 | 51.5% | 22.2% | 14.3% | 5.3% |
| XLMEUR | 0.562% | 0.316% | 53 | 0 | 54.6% | 28.6% | 14.2% | 4.3% |
| HBAREUR | 0.411% | 0.230% | 21 | 4 | 39.9% | 21.0% | 10.6% | 2.6% |
| ADAEUR | **0.869%** | **0.422%** | 129 | 0 | **80.6%** | **40.7%** | 23.6% | 7.6% |
| QNTEUR | 0.321% | 0.179% | **8** | **38** | 31.5% | 17.5% | 8.9% | 1.4% |
| XDCEUR | **0.173%** | **0.086%** | **9** | **99** | 19.9% | 11.2% | 5.4% | 1.2% |
| ALGOEUR | 0.614% | 0.306% | 27 | 4 | 57.4% | 32.9% | 17.6% | 4.2% |

**1h vs 0.52% RT:** median **body** is **under** the tax on **every** allowlist pair. ADA is the least-bad (median range 0.87% barely over; median body 0.42% still under). XDC median range **0.17%** is a third of the tax. **A 1h harvest is dead at 0.26% taker before style is discussed.**

Scaled 1h **body ≥ 0.52%** hits / 90d (now-tape ×3): XRP ~480, ADA ~879, XDC ~243, QNT ~378. That is **hundreds of candidate bars**. A style that takes them is a fee factory. A style that takes **1–2%** of them can hit 8 closed clips — that is a **filter**, which is a new recipe (`H-`).

### 2.4 4h now-tape (~120d, n=720)

| Pair | med range | med body | med trades | range ≥0.52% /90d | body ≥0.52% /90d | body ≥0.80% /90d | body ≥1.60% /90d |
|---|---:|---:|---:|---:|---:|---:|---:|
| XRPEUR | 1.21% | 0.49% | 988 | 503 | 258 | 174 | 63 |
| XLMEUR | 1.79% | 0.76% | 319 | 530 | 333 | 257 | 134 |
| HBAREUR | 1.30% | 0.57% | 122 | 507 | 297 | 208 | 70 |
| ADAEUR | 1.77% | 0.73% | 442 | 533 | 342 | 246 | 116 |
| QNTEUR | 1.25% | 0.55% | **32** | 468 | 284 | 201 | 80 |
| XDCEUR | 1.03% | 0.45% | 114 | 408 | 250 | 175 | 74 |
| ALGOEUR | 1.82% | 0.79% | 124 | 526 | 358 | 266 | 124 |

Median 4h **body** sits **on** the 0.52% knife (XRP 0.49%, XDC 0.45%) or just over (ALGO 0.79%). **4h is not a rescue of 1h** at paper 0.26%. At live 0.80% taker (need ~1.60% body) you get **~63–134 candidate bodies / 90d** — still too many if you take them all, usable if you take **~10%**.

### 2.5 12h derived from 4h (~120d, n≈241)

| Pair | med range | med body | range ≥0.52% | range ≥0.80% | range ≥1.60% |
|---|---:|---:|---:|---:|---:|
| XRPEUR | 2.29% | 0.86% | 100% | 96.3% | 71.0% |
| XLMEUR | 3.24% | 1.21% | 100% | 100% | 85.5% |
| HBAREUR | 2.37% | 0.97% | 100% | 98.3% | 77.2% |
| ADAEUR | 3.08% | 1.05% | 100% | 98.8% | 90.5% |
| QNTEUR | 2.44% | 1.06% | 100% | 98.8% | 77.6% |
| XDCEUR | 1.99% | 0.90% | 96.3% | 89.2% | 58.9% |
| ALGOEUR | 3.41% | 1.29% | 100% | 100% | 89.2% |

**12h is the first clock where median body ≥ 0.52% on every allowlist pair.** Median body is **still under 1.60%** (live taker RT). Geometry: paper 0.26% **fits**; live Tier 1 taker **does not**, unless you capture **range** not body, or you skip to the fat tail.

~180 twelve-hour bars / 90d. Almost every bar’s **range** clears 0.52%. You **must skip**. Cadence below.

### 2.6 1d REST (longest honest daily; 720-cap)

| Pair | n | window | med range | med body | p25 range | body ≥0.52% /90d | body ≥0.80% /90d | body ≥1.60% /90d |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| XRPEUR | 720 | 2024-09-07→2026-08-27 | 4.45% | 1.69% | 3.10% | 74 | 66 | 48 |
| XLMEUR | 720 | same | 4.98% | 2.10% | 3.43% | 78 | 71 | 56 |
| HBAREUR | **414** | **2025-07-10→** | 4.70% | 1.93% | 3.25% | 77 | 71 | 51 |
| ADAEUR | 720 | 2024-09-07→ | **5.79%** | **2.38%** | 4.07% | 78 | 72 | 58 |
| QNTEUR | 720 | 2024-09-07→ | 5.00% | 2.16% | 3.58% | 77 | 71 | 56 |
| XDCEUR | **360** | **2025-09-02→** | **3.75%** | **1.45%** | 2.37% | 76 | 66 | 41 |
| ALGOEUR | 720 | 2024-09-07→ | **5.84%** | **2.54%** | 4.07% | 80 | 75 | 59 |

Daily **range** almost always clears 0.52% and 0.80% (XDC 1.60% range still 90%). Daily **body** clears 1.60% on **~46–66%** of days. **Room exists** at 0.26% and at 0.80% RT **if** the style captures a large fraction of a selected day and **does not trade most days**.

**HBAR and XDC cannot do an honest 1y Kraken-EUR walk-forward** (listed Jul/Aug–Sep 2025). Do not invent a 2023 HBAREUR / XDCEUR daily file.

### 2.7 1w native

Weekly median range **10–19%**, median body **3.2–7.8%**. Body ≥ 1.60% on **~67–87%** of weeks. Scaled: **~9–12 bodies ≥ 1.60% per 90d**, **~35–50 per 1y**.

**90d n-gate:** 13 weeks. 8 closed clips ⇒ complete **8/13 weeks**. Feasible only if the style is “trade almost every week.” A true hold that trims once a month **fails fills≥8 in 90d**.

**1y n-gate:** 52 weeks. Easy if you complete even a quarter of them.

---

## 3. Pair personality — jumpy vs thin+slow

**This sitting’s 24h ticker** (Kraken public, 2026-08-28 ~19:52Z):

| Pair | last | 24h notional € | 24h trades | 24h range | top-10 book € (bid+ask) | spread |
|---|---:|---:|---:|---:|---:|---:|
| XRPEUR | 1.189 | **11.4M** | **9599** | 7.22% | **126k** | 0.030% |
| ADAEUR | 0.175 | **1.50M** | **4164** | **8.57%** | 15k | 0.038% |
| XLMEUR | 0.153 | 354k | 1598 | 7.08% | 8.6k | 0.044% |
| HBAREUR | 0.066 | 169k | 1335 | 7.27% | 13k | 0.015% |
| ALGOEUR | 0.075 | 127k | 647 | 7.09% | 8.1k | 0.013% |
| XDCEUR | 0.024 | 120k | 1040 | **3.99%** | 38k | **0.170%** |
| QNTEUR | 52.43 | **41k** | 478 | 4.46% | 13k | 0.076% |

CEO split holds on this tape: **XRP / XLM / HBAR / ADA / ALGO** printed **7–8.6%** 24h ranges; **QNT / XDC** printed **4.0–4.5%**. Jumpy ≠ always more 1h range (HBAR 1h median 0.41% < XRP 0.53%); it shows up as **fatter 4h/12h/1d bodies** (ADA/ALGO/XLM lead).

**Does thin + slow help fees?**

| Effect | Helps? | This sitting |
|---|---|---|
| Fewer 1h bars that look like a 0.52% “fill” | Yes, mechanically | XDC: only 20% of 1h ranges ≥ 0.52%; 99/720 **zero-trade** hours. QNT: 38/720 empty hours, median 8 trades. |
| Fewer **fake** wick fills vs a deep book | Maybe | Empty hours cannot fill a resting limit honestly. Wick-touch engines that fill XDC on a 1-trade spike **overstate**. |
| Get **8 fills in 90d** | **Hurts** | If you refuse empty hours and refuse sub-fee gaps, QNT/XDC 1h **candidates** collapse. You then need a **slower** clock — which is the same conclusion as the jumpy names, with **less** history. |
| Slippage / spread | **Hurts** | XDC spread **0.17%** is **~2/3 of paper 0.26%** in one shot. QNT 0.076%. XRP 0.030%. Spread is a silent extra fee on taker and a wider “must rest” on maker. |
| 1y walk-forward | **Hurts XDC (and HBAR)** | Kraken EUR listing 2025. No 2023–2024 Kraken-EUR year to fail on. |

**Personality rule (STEAL, not a pair-WFO):** jumpy names (ADA, ALGO, XLM, XRP) supply **more honest bodies above fee** at 12h/1d. Thin+slow (QNT, XDC) supply **fewer fake 1h prints** and **worse** slip; they do **not** unlock a 1h maker business. Use QNT/XDC as **spot-only stress**, not as the first book. Journal already: never sleeve QNT/XDC.

Depth this sitting is a **snapshot**, not 2023. XRP top-10 is an order of magnitude deeper. A EUR 200 clip is **inside** every pair’s top-10 notional **today**. That does **not** prove 2023 XDC depth.

---

## 4. Styles — who keeps n in the gate band?

Gate language: **fills ≥ 8** (each print counts; live book is **2 buys**, TPs open). CEO extra: **8+ CLOSED clips in ~90d** and still healthy on ~1y. Tension: invert-family death was **too many** fills; sleeve death was **too few**.

**Target cadence (identity, not a score):**

```text
8 closed clips / 90d  =  1 completed RT every ~11 days
                     ≈  16 fills / 90d   (buy+sell)
                     ≈  0.18 fills/day
1y at the same rate   ≈  32 closed clips ≈ 64 fills/year
```

Fee drag at clip EUR 200, paper 0.26%: **64 × 0.52 € ≈ 33 €/year ≈ 0.33%** of 10k. Survivable **if** gross > that and maxDD ≤ 8%.  
At 0.80% taker: **64 × 1.60 € ≈ 102 €/year ≈ 1.0%**. Still a maybe.  
At invert-like 2779 fills: **2779 × 0.52 € ≈ 1445 € ≈ 14.5%** — DD gate is already dead from fees. **Do not go there.**

| Style | Natural n | vs 8 closed / 90d | vs fee mill | Fit |
|---|---|---|---|---|
| **Mean-reversion / fade** | High. Wants every bounce. | Overshoots badly on 1h/4h. On 1d, Coinquant average still **−4.0%** with cheaper-than-Kraken costs. | **Eats the book** unless heavily filtered (`H-`). | **DEAD** as naked 1h/4h. 1d fade = regime-fragile **MAYBE**. |
| **Trend-follow** | Low. Few swings. | Daily Donchian in the one honest Kraken **0.26%** study: **14 trades, +4.33%** — n can clear 8 on a **year**, may miss 8 **closed in 90d** if the window is quiet. 4h same rule **−6.01%**. | Natural ally of fees **if** clock is 1d+. | **MAYBE / try-next** on **1d**. **DEAD** on 1h/4h at 0.26%. |
| **DCA drip** | You choose the calendar. Weekly drip = 13 **buys** / 90d. | **Fills** can clear 8. **Closed clips** stay **0** until you sell. `dca-paper` is this machine and is **held, not reset**. | Fees only on the drip; DD is inventory. BTC already showed mark holes. | **DEAD as a closed-clip path.** Allowed only if paired with **trim** (= hold+trim). |
| **Wide grid** | n ≈ levels × crossings. 3×3 around last on 1h = mill. 1–2 levels, gap ≥ 2× RT, 12h/1d = controllable. | Can print 8 if the pair **oscillates** through a **wide** gap ~8 times in 90d. | Identity: `gap < 2× fee` ⇒ every cycle loses. | **MAYBE** on 12h/1d jumpy names, **few** levels. **DEAD** tight / 1h. |
| **Hold+trim** | n = number of trims + entries you **choose**. | **Best n-control.** Schedule 8–16 trims / 90d on days whose body ≥ 1.60% (plenty of candidate days — §2.6). | One lot, clip 200, skip quiet days. | **TRY NEXT.** Still has to survive 8% DD on a trend against the hold. |

Public cluster (STEAL [#217](https://github.com/eyeskull2220/solana-invoice/pull/217), not invert): **daily-or-slower, few round-trips, posted spot ≤ ~26 bps/side.** 4h already dies in the Kraken 0.26% trend study. 15m fade gross **~1.3 bp** vs 52 bp RT ([arXiv:2608.21888](https://arxiv.org/html/2608.21888)).

---

## 5. Maker rest — can a paper LIMIT below last be treated as maker?

**Geometry:** a buy LIMIT **below last** that does **not** cross the ask **rests**. On Kraken Pro that is a **maker** if it later trades. `oflags=post` rejects a cross so you never pay taker by accident ([Kraken order flags](https://docs.kraken.com/api-reference/trading/add-order); fee-optimization skill: post-only). A paper engine that fills when `low ≤ P` **without** a queue is **optimistic maker**: it assumes fill probability **1** at the maker price.

**What you may assume in paper (honest columns):**

| Assumption | Per fill | RT | Use as |
|---|---|---|---|
| Paper taker (locked) | 0.26% | 0.52% | Primary. Matches invert-paper journal. |
| **Posted** Tier 1 maker (2026-08-28) | **0.40%** | **0.80%** | Live-entry shadow. **Worse than paper 0.26%.** “Go maker” **raises** tax at Tier 1. |
| Posted Tier 1 taker | 0.80% | 1.60% | Stress. |
| **0.16% maker** | 0.16% | 0.32% | **Do not.** Not on current crypto-spot table (cite §1). |
| Maker + `p < 1` fill | 0.40% × p, plus missed-fill opportunity | — | Required for any maker claim. Adverse selection: you fill when the move is against you ([arXiv:2502.18625](https://arxiv.org/html/2502.18625v2)). |

**Thin books:** QNT median **8** trades/hour, XDC **9**, **99** empty XDC hours. A resting bid may sit through empty hours and then fill on a one-lot sweep — **toxic**. Jumpy-deep XRP (238 trades/hour, 0.03% spread) is the only allowlist name where “maker rest below last” is even a **serious** microstructure claim.

**H-A3 (not applied):** score a non-invert 1d hold+trim with **post-only** fills at **0.40%** maker and a **missed-fill** column. Do not score it at 0.16%. Do not call wick-touch 100% maker.

---

## 6. Kill-switch sleeve 3x — negative control for the DD gate

Journal (cite, do not mix into the gate): PF_XRPUSD paper **3x**, same invert pairing, real flip, **8-day lab clip**: **6 fills, −2.729078%, maxDD 5.326685%, FAIL fills&lt;8**. Not the seal verdict. Not this allowlist path.

**Why it is a negative control, not a try-next:**

- **3x multiplies DD.** Spot maxDD 8% cap becomes a 3x path that **should** fail `maxDD ≤ 8%` on any real walk-forward that actually moves. The 8-day clip **did not** break 8% (5.33%) — it failed **n** instead. That is **not** permission to 3x “until DD looks interesting.”
- **n-gate is independent of leverage.** 6 prints stay 6 prints. Leverage does not mint fills.
- Journal already: QNT/XDC **never** sleeved. Kill switch = futures-paper cancel-all. **No live.**

Do **not** put 3x in the survive matrix. **DEAD as a survival path.** Keep the printed sleeve FAIL as a warning that **leverage + short window** fails the **same gate** from the **n** side, and a **long** 3x window is how you expect to fail the **DD** side.

---

## 7. The fills≥8 vs low-n tension — proposed cadence

**Do not 15m grind.** 15m typical XRPEUR range **~0.45–0.47%** vs RT **0.52%** ([#211](https://github.com/eyeskull2220/solana-invoice/pull/211)). Same inequality is **worse** on QNT/XDC 1h bodies.

**Cadence that can print 8+ CLOSED clips in 90d without 15m grinding (`H-A1` / `H-A2` — not applied):**

1. **Decision clock: closed 1d bars** (or 12h if you need more candidates in a quiet 90d). 15m/1h are **touch/fill resolution only if a standing limit already rests** — not the decision clock.
2. **One lot.** Clip EUR 200. No pyramid. No 3×3 around last.
3. **Arm only if the planned gap ≥ 1.60%** (clears paper 0.52% with buffer; equals live taker RT; ~3× paper RT). Daily bodies ≥ 1.60% already occur **~41–59 times / 90d** on this allowlist — **too many**. Take **~15–25%** of them (a trend filter or a “trim into strength” rule) → **~8–16 closed clips**.
4. **Skip quiet days.** A day whose body &lt; 0.52% cannot pay paper RT if that body *is* the trade.
5. **Jumpy names first:** ADAEUR / ALGOEUR / XLMEUR / XRPEUR. HBAR as a 2025- listing **90d** probe only. QNT/XDC as **thin** probes on the **same 1d clock**, not a faster clock.
6. **90d:** 8–16 closed clips. **1y:** same rule frozen (no WFO of the gap). Expect ~32–64 closed clips if the 90d rate holds — still **two orders of magnitude** below 2779.
7. **Fills≥8:** 8 closed clips = 16 prints if every clip completes. Even **8 prints** (4 closed + opens) clears the **letter** of the gate; CEO asked for **closed** clips — design for **closed**.

**1w variant:** 13 shots / 90d. Works only if completion ≥ ~8/13. Safer as a **1y** clock than as the 90d n-engine.

**Anti-cadence (do not):** take every 4h body ≥ 0.52% (~250–360 / 90d) — that is 500–720 fills, fee mill. Take every 1h range ≥ 0.52% on ADA (~1740 / 90d) — dust.

---

## 8. Clock × style matrix

Legend: **survive** = geometry + public literature + n-band can all be true on this allowlist (still not a score). **maybe** = one of those three is yellow. **dead** = fee > typical capture, or n mill, or n cannot hit 8 closed / 90d.

### 8.1 At paper **0.26%** taker (RT **0.52%**)

| Clock ↓ / style → | Mean-reversion | Trend-follow | DCA drip (no trim) | Wide grid (gap ≥ 2× RT, ≤2 levels) | Hold+trim |
|---|---|---|---|---|---|
| **1h** | **dead** | **dead** | **dead** | **dead** | **dead** |
| **4h** | **dead** | **dead** (nar1-frames −6%) | **dead** | **dead / maybe** if gap ≥ 1.6% and skip most bars | **maybe** (filter hard) |
| **12h** | **maybe** (must skip ~90% of bars) | **maybe** | **dead** (closed clips) | **maybe** | **maybe / survive-cluster** |
| **1d** | **maybe** (Coinquant 1d avg −4%; regime) | **maybe / survive-cluster** | **dead** (closed clips) | **maybe** | **survive-cluster (try next)** |
| **1w** | **maybe** (90d n knife) | **maybe** (90d n knife; 1y easier) | **dead** unless weekly drip **plus** sells | **dead** (too few crossings for a grid) | **maybe** (8/13 weeks) |

### 8.2 At **0.80%** per side (live Tier 1 taker; RT **1.60%**) — also the 0.40/0.80 shadow pair if you round-trip taker/maker mixed, taker is the worse column

| Clock ↓ / style → | Mean-reversion | Trend-follow | DCA drip (no trim) | Wide grid | Hold+trim |
|---|---|---|---|---|---|
| **1h** | **dead** | **dead** | **dead** | **dead** | **dead** |
| **4h** | **dead** | **dead** | **dead** | **dead** | **dead** (median body 0.45–0.79% ≪ 1.60%) |
| **12h** | **dead** | **dead / maybe** (need range, not body) | **dead** | **dead** unless gap ≫ 1.60% | **maybe** on jumpy names, fat-tail days only |
| **1d** | **maybe** (body ≥1.60% ~half of days; fade still regime-fragile) | **maybe** | **dead** | **maybe** if spacing ≥ ~3% | **maybe / survive-cluster** |
| **1w** | **maybe** | **maybe** | **dead** | **dead** | **maybe** (n knife on 90d) |

**Maker 0.40% RT 0.80%** sits between the two tables: 12h median body **0.86–1.29%** **clears 0.80%** on jumpy names **if** you actually make and **if** `p` is high. XDC 12h range ≥0.80% is 89%, body median 0.90% — knife plus **0.17% spread**. Do not promote maker-12h-XDC.

---

## 9. One try next / one do not try

### Try next — `H-A1` (not applied, not invert, not a score)

**1d hold+trim**, one lot, clip EUR 200, allowlist **jumpy** first (**ADAEUR or XRPEUR**; XLM/ALGO backups). Arm a trim/entry only when planned gap **≥ 1.60%**. Target **8–16 closed clips / 90d**. Score three fee columns **0.26 / 0.40 / 0.80**. Standing limits may rest below last; **do not** credit them as 0.16% maker. `is_fund_gate: false`. New book name. **Do not touch invert-paper fill 2. Do not reset dca-paper.**

Optional twin on the same freeze: **1d trend-follow** (`H-A2`) — Donchian-or-similar **daily**, low n, same clip, same fee columns. Literature already printed **+4.33% vs hold +127%** at 0.26% on a different tape — steal the **clock**, not the PnL.

### Do not try

**1h mean-reversion or tight grid** on any of the seven pairs, including “but QNT is slow so fees won’t eat it.” 1h median bodies are **under** 0.52% everywhere; ADA’s extra jumpiness **increases** n, it does not pay the tax. Same ban on 15m, on invert variants, on 3x sleeve, on IOTA, on memecoins, on live, on PLAN 196/207 CODE.

---

## 10. What data dump would be needed before a real score (**do not start**)

A later score of `H-A1` / `H-A2` needs a **named tape**, not REST last-720 as “2023.” Do **not** start it in this PR.

| Need | Why | How (path only) | Blocker this VM |
|---|---|---|---|
| Kraken **1d** (and 4h/12h if used) **from listing → now** for XRPEUR, XLMEUR, ADAEUR, ALGOEUR, QNTEUR | 1y walk-forward. REST daily starts **2024-09-07** (720-cap). | Official OHLCVT `PAIR_1440.csv` / `PAIR_240.csv` + Trades tail ([OHLCVT](https://support.kraken.com/articles/360047124832-downloadable-historical-ohlcvt-open-high-low-close-volume-trades-data)) **or** REST `Trades` reconstruct, 1–2 s/page, result keys `XXRPZEUR` / `XXLMZEUR` / display names for the others. | Drive **7.3G interstitial**. Full Trades walk is slow. **Do not download 7.3G into this leftover repo.** |
| Honest listing windows | HBAR EUR **2025-07-10**, XDC EUR **2025-08-28**. | Score **90d** on those two; do **not** claim 1y Kraken-EUR. | None — already visible on REST weekly. |
| Native 12h | REST has no 720-minute interval. | Aggregate 4h **from the dump**, UTC buckets, label `derived_from=4h`. | Don’t use last-720 4h as 2023. |
| Spread / depth **time series** | Snapshot 2026-08-28 ≠ 2023 XDC slip. | Public `Depth` polls are not history. OHLCVT has no spread. **UNVERIFIED** without a paid tape or a self-logged poll. | Do not start a poller. |
| Maker fill probability | Wick-touch ≠ maker. | Needs live/paper post-only rejects + time-to-fill. invert-paper is **not** that log. | No keys. |
| Vision *EUR | Optional **labeled** twin for XRP/XLM/ADA 1h/1d. | `data.binance.vision` monthly klines. **404** this sitting for HBAR/QNT/XDC/ALGO EUR 1h. | Do not mix into a Kraken row. |
| Bitstamp | Third dump only. | Already labeled in [#198](https://github.com/eyeskull2220/solana-invoice/pull/198). | Not Kraken. |

**Do not:** REST `OHLC interval=15` as 2023 (720 = 7.5d). Invent HBAR/XDC 2023 EUR. Stitch Vision+Kraken unlabeled. Commit ZIPs. Start CODE from #196/#207.

---

## STEAL vs HYPOTHESIS

### STEAL (clock / tape / fees — do not rewrite invert)

| ID | Steal |
|---|---|
| **S-A0** | Vision 1-limit FAIL and D6 FAIL. Cite once. Do not autopsy. |
| **S-A1** | Paper 0.26 + shadows 0.40/0.80. Live Tier 1 **0.40 / 0.80** as of **2026-08-28** fee page. 0.16% maker **not** on crypto-spot. |
| **S-A2** | REST OHLC last-720: 1h≈30d, 4h≈120d, 1d from 2024-09-07 (HBAR/XDC shorter). 12h = 4h agg. Weekly from listing. Venue **Kraken public REST**, this sitting. |
| **S-A3** | 1h median **body &lt; 0.52%** on all seven. 12h first clock with median body ≥ 0.52%. 1d bodies often ≥ 1.60%. |
| **S-A4** | Jumpy: ADA/ALGO/XLM/XRP (and HBAR 24h). Thin+slow: QNT/XDC (empty 1h bars, higher spread, younger EUR listing for XDC). |
| **S-A5** | n-band: 8 closed / 90d ≈ 16 fills / 90d ≈ 0.18 fills/day. 2779 fills/year is a mill. 6 fills is a FAIL. |
| **S-A6** | Sleeve 3x lab: 6 / −2.73% / 5.33% DD / FAIL n. Negative control. Not the gate. |
| **S-A7** | invert-paper fill **2**. dca-paper held. `c9689f5d` unresealed. `is_fund_gate: false`. |
| **S-A8** | Public literature clock cluster: daily-or-slower, low n ([#217](https://github.com/eyeskull2220/solana-invoice/pull/217), Coinquant, nar1-frames, arXiv 2608.21888). |
| **S-A9** | Maker fill `p < 1` + adverse selection. Post-only is a flag, not a 0.16% coupon. |

### HYPOTHESIS (new non-invert recipe — **not applied**)

| ID | Hypothesis | Why not this page |
|---|---|---|
| **H-A1** | 1d hold+trim, gap ≥ 1.60%, 8–16 closed / 90d, jumpy EUR first | New book. No equity curve here. |
| **H-A2** | 1d trend-follow, same clip/fees | Steals nar1-frames **clock**, not PnL. New hash. |
| **H-A3** | Post-only scored at **0.40%** maker + missed-fill column | Queue not in REST OHLC. |
| **H-A4** | 12h as the decision clock instead of 1d | Derived bars. Dump 4h first. |
| **H-A5** | Wide 2-level grid on ADA/XLM 1d | New recipe. Gap identity only. |
| **H-A6** | Use QNT/XDC empty hours as “maker edge” | Empty ≠ edge. Spread hurts. |
| **H-A7** | 1w hold to dodge the mill | 90d n-gate knife (8/13). |
| **H-A8** | 3x sleeve to “help” DD or n | Negative control. Journal FAIL. |
| **H-A9** | Invert variant / slower invert clock | **Forbidden this sitting.** |
| **H-A10** | CODE from PLAN #196 / #207 because a reviewer stamped GREEN | GREEN ≠ CODE licence. |
| **H-A11** | Treat 0.16% maker as current Kraken crypto-spot | False on 2026-08-28 table. |
| **H-A12** | Start the OHLCVT / Trades dump in this PR | Job says do not start. |

Any H\* that ships: **new** workspace or **new** seal. Not `c9689f5d`. Not invert-paper. Not a `dca-paper` reset.

---

## Inform Coder

**Do**

- Keep paper. Keep fill **2**. Keep `dca-paper` held.
- When asked “what besides invert?”, point at **`H-A1` 1d hold+trim** (and `H-A2` 1d trend) on jumpy EUR, wide gap, 8–16 closed / 90d.
- Keep three fee columns. Live Tier 1 is **0.40 / 0.80**.
- Label REST windows. Do not call last-720 1h “2023.”
- Leave Vision 1-limit and D6 as **FAIL**. Leave sleeve 3x as **FAIL fills&lt;8**.

**Do not**

- Apply H-A\* inside invert-paper.
- CODE from #196 / #207.
- Invent a 1d equity curve in markdown.
- Credit 0.16% maker on XRPEUR.
- Sleeve QNT/XDC. Invent IOTA. Live. Keys. Memecoins.
- Start a 7.3G dump or a Trades backfill from this leftover repo.

---

## RED / YELLOW / GREEN

### RED

- 1h / 15m harvest at 0.26% or 0.80%.
- 0.16% maker as current Kraken crypto-spot.
- Tight grid / naked 1h fade / 3x survival sleeve / invert variants.
- Using 30d 1h REST as 2023→now.
- Claiming 1y Kraken-EUR WF for HBAR or XDC.
- Mixing Vision klines into a Kraken score row.
- Promotion, live, keys, reseal, `dca-paper` reset, PLAN CODE.

### YELLOW

- 12h derived from 4h (not native).
- 4h body vs 0.52% knife.
- 1w vs 90d n-gate (8/13).
- Maker rest below last **without** a `p` model.
- QNT/XDC: fewer fake 1h prints **and** worse slip; depth is a snapshot.
- Maker rebate pair list unverified.
- Daily REST starts 2024-09-07 for the long names.

### GREEN

- Own-ideas pass. Invert cited as FAIL once. No autopsy.
- Clocks 1h / 4h / 12h / 1d / 1w with venue + range.
- Styles compared on **n**, not vibes.
- Try next / do not try named.
- Dump listed, **not started**.
- Fill 2 stays. Still paper. `is_fund_gate: false`.

---

## What this file is not

1. **Not the fund gate.** invert-paper fills **2/8**. Stay paper.  
2. **Not an invert variant** and not a new invert score.  
3. **Not** PLAN #196 / #207 CODE.  
4. **Not** a dump, not a scorer, not a 2023 equity curve.  
5. **Not** a reseal of `c9689f5d`. Not a `dca-paper` reset.  
6. **Not** live, not keys, not IOTA, not memecoins.  
7. **Not** tax / SEPA / FACTUUR / shop HTML.

---

## Sources (public URLs)

Fee tables (fetched / cited **2026-08-28**)

- https://www.kraken.com/features/fee-schedule — Spot Crypto Tier 1 **0.40% / 0.80%**
- https://support.kraken.com/articles/cross-platform-fee-tier-changes — effective **2026-07-09**
- https://blog.kraken.com/product/pro/new-kraken-pro-fee-tiers
- https://support.kraken.com/articles/201893638-how-trading-fees-work-on-kraken

Kraken public REST (this sitting)

- https://docs.kraken.com/api-reference/market-data/get-ohlc-data — intervals **1,5,15,30,60,240,1440,10080,21600** (no 720)
- https://docs.kraken.com/api-reference/market-data/get-ticker-information
- https://docs.kraken.com/api-reference/market-data/get-order-book
- https://docs.kraken.com/api-reference/market-data/get-server-time
- https://support.kraken.com/articles/360047124832-downloadable-historical-ohlcvt-open-high-low-close-volume-trades-data — dump **not started**

Clocks / costs / styles (STEAL)

- https://arxiv.org/html/2608.21888 — 15m sign ~1.3 bp vs 5–20 bp costs
- https://www.coinquant.ai/blog/building-a-mean-reversion-strategy-in-cryptocurrency-markets-evidence-from-78-backtests — 15m −14.4% … 1d −4.0%
- https://dev.to/nar1frames/i-built-a-crypto-trading-bot-it-lost-to-doing-nothing-355a — Kraken 0.26% Donchian 1d +4.33% / 4h −6.01%
- https://arxiv.org/html/2502.18625v2 — maker `p < 1`, adverse selection
- https://data.binance.vision/ — XRPEUR/XLMEUR/ADAEUR 1h 2026-07 present; HBAR/QNT/XDC/ALGO EUR 1h **404** this sitting

Desk (cite, do not reseal / reset / CODE)

- https://dca-paper-journal.surge.sh/ — fill **2/8**, sleeve 3x FAIL, allowlist
- https://github.com/eyeskull2220/solana-invoice/pull/217 — style clocks / costs
- https://github.com/eyeskull2220/solana-invoice/pull/216 — styles broad
- https://github.com/eyeskull2220/solana-invoice/pull/211 — 15m vs 26 bps
- https://github.com/eyeskull2220/solana-invoice/pull/212 — 1-limit fill rate (not a score)
- https://github.com/eyeskull2220/solana-invoice/pull/209 — D6 Kraken-native 15m path (FAIL as a surviving 15m path)
- https://github.com/eyeskull2220/solana-invoice/pull/207 — PLAN lock (**not a CODE licence**)
- https://github.com/eyeskull2220/solana-invoice/pull/196 — retired ladder PLAN (**do not CODE**)

---

## Re-check (copy/paste — public / git only)

```bash
curl -sS 'https://api.kraken.com/0/public/Time'
curl -sS 'https://api.kraken.com/0/public/SystemStatus'
curl -sS 'https://api.kraken.com/0/public/Ticker?pair=XRPEUR,XLMEUR,HBAREUR,ADAEUR,QNTEUR,XDCEUR,ALGOEUR'
curl -sS 'https://api.kraken.com/0/public/OHLC?pair=XDCEUR&interval=60'  >/tmp/xdc_1h.json
curl -sS 'https://api.kraken.com/0/public/OHLC?pair=XRPEUR&interval=720'  # expect EGeneral:Invalid arguments
curl -sS 'https://api.kraken.com/0/public/OHLC?pair=HBAREUR&interval=1440' # first bar ~2025-07, not 2023
curl -sS -o /dev/null -w '%{http_code}\n' \
  'https://data.binance.vision/data/spot/monthly/klines/HBAREUR/1h/HBAREUR-1h-2026-07.zip'  # 404

rg -n 'is_fund_gate|H-A1|do not try|fill \*\*2\*\*|0\.40%|12h|UNVERIFIED|not a CODE licence' \
  docs/rgy-2026-08-28/coder/RESEARCH-allowlist-clocks-own-ideas.md

curl -sS https://dca-paper-journal.surge.sh/ | rg -n 'fills 2/8|PAPER-00031|NOT MET|c9689f5d|invert-paper' || true

# Never:
# kraken paper reset --workspace invert-paper
# kraken paper reset --workspace dca-paper
# kraken order …
# download 7.3G Kraken_OHLCVT.zip into this leftover repo
```

Fee table: https://www.kraken.com/features/fee-schedule (Spot Crypto Tier 1 = **0.40 / 0.80** on 2026-08-28).  
July 2026 change: https://support.kraken.com/articles/cross-platform-fee-tier-changes

Count fund-gate fills only from `PAPER-*` **prints** on **`invert-paper`**. Resting 00030 / 00032 do not count. Fill **2** stays.

**Vision 1-limit FAIL and D6 FAIL stay FAIL. The non-invert cluster that can both pay 0.52% (maybe 0.80%) and print 8+ closed clips in 90d without 15m grinding is 1d (or 12h) hold+trim / slow trend, one lot, wide gap, jumpy EUR first. H-A1/H-A2 not applied. No invert variants. PLAN 196/207 are not a CODE licence. invert-paper fill 2 stays. dca-paper stays held. Still paper.**

End. RESEARCHER. Inform Coder. Docs only. `is_fund_gate: false`. VOORBEELD.
