# RESEARCH — Can a 15m XRPEUR invert survive 26 bps (EUR 200 clips, 2023→now)?

**Seat:** RESEARCHER · Coder  
**Lens:** start **simple** (round-trip fee vs typical 15m range), then **broaden**. Docs + public GETs only.  
**Date:** 2026-08-27  
**Stamp:** VOORBEELD · paper / simulated · not FACTUUR · not INVOICE · not live-trade advice  
**HEAD (this leftover repo):** `2170952`  
**Still paper. No keys. No orders.** Do not reseal `c9689f5d`. Do not reset `invert-paper` or `dca-paper`. Do not rewrite invert.

This file answers one question: **can a 15-minute XRPEUR invert, charged 0.26% per fill (with 0.40 / 0.80 shadows) on EUR 200 clips, survive 2023-01-01 00:00 Europe/Brussels → now?**

It does **not** print a new invert equity curve. Inventing one here is cheating. Operator-stated prints below are **cited and checked for arithmetic**, not restated as a prettier number.

---

## Locks (this sitting)

| Lock | Status |
|---|---|
| Still paper / no keys / no orders | **GREEN** |
| `invert-paper` is the **fund gate** (fill **1**) | **GREEN** — not this file |
| `invert-wf-2023` is a 15m walk-forward, **not** the gate | **GREEN** |
| 9097-fill was **fill-every-rung** (retired `2bfb1b68` family) | **GREEN** — cited, not revived |
| invert-v2 day0 TWO-CLIP is **operator-stated**; 1-limit rescore **in flight** | **GREEN** — not replaced |
| Do not invent our PnL | **GREEN** |
| Do not change invert | **GREEN** — H- labels only |
| Do not reseal `c9689f5d` / reset `dca-paper` | **GREEN** |

Live gate book (untouched): fill **1** `PAPER-00029` buy XRPEUR @ **1.24496**. Resting TP `PAPER-00030` sell LIMIT @ **1.26778** is **not** a fill. Open `PAPER-00028` @ **1.23084** is **not** a fill. Gate (return > 0 after fees **and** ≥ 8 prints **and** maxDD ≤ 8%) is **NOT MET**.

Sealed lab clip (cite only): `fib-grid-invert-xrpeur-15m`, 2026-08-18 21:00 → 2026-08-26 08:00 Europe/Brussels, 20 fills, +0.681154%, maxDD 0.890854%, vs `sha256:c9689f5d7d583320e724900b0ce4ef68193878c880d11939badd1dd59016e390`. **Not** 2023→now.

Kraken MCP this VM: **error / undiscoverable**. Public REST only. Server clock this sitting: `GET /0/public/Time` → `unixtime` **1787862017** (`Thu, 27 Aug 26 20:20:17 +0000`). `GET /0/public/SystemStatus` → `online`.

---

## Method of this paper

1. **Simple first:** one inequality. Round-trip fee vs typical 15m XRPEUR range. If the tax is larger than the bar, a 15m harvest is dead before invert state is discussed.
2. **Then clip euros:** EUR 200 does not change the percent. It only caps euros per fill.
3. **Then hold time:** 47-bar mean hold (11.75 h) vs the same inequality scaled by √time.
4. **Then broaden:** which 15m mean-reversion / grid systems actually publish a survival at ~26 bps, and which die.
5. **Hypotheses labeled `H-`.** Not applied. Invert stays invert.

Probed this sitting from public REST (no key): `OHLC` `interval=15/60/240/1440/10080` pair `XRPEUR`, `Ticker`, `Time`, `SystemStatus`. Daily REST is last ~720 days (from **2024-09-06**). Weekly REST covers **2023+**. 15m REST is last **7.5 days** only — a noisy now-tape, not the 2023 series.

---

## Verdict

| Claim | Color |
|---|---|
| Round-trip **0.52%** vs typical 15m range **~0.45–0.47%** (2023+ weekly / 2024-09+ daily, Brownian scaled) | **RED** as a 15m-bar harvest |
| EUR 200 clip makes 0.26% “cheap enough” | **RED** — percent is the tax; clip only caps euros |
| 47-bar mean hold (~11.75 h) is *structurally able* to cover 0.52% **if** a large fraction of the scaled range is captured | **YELLOW** as geometry · **RED** as invert-v2’s captured edge |
| invert-v2 day0 TWO-CLIP (operator): 7923 fills, −41%, fees 4120, price_pnl +36 | **RED** survival · arithmetic **checks** · **not** a new score |
| 9097-fill as invert survival | **RED** — fill-every-rung / close-model / 100% equity (PR #201) |
| 15m mean-reversion / tight grids at 26 bps taker in public literature | **RED** (arxiv 1.3 bp gross vs 5–20 bp costs; Coinquant 15m avg −14.4%) |
| Daily-or-slower systems at 26 bps | **YELLOW** — one public Kraken 0.26% study survives on **1d**, dies on **4h** |
| 0.40 / 0.80 shadows as “stress only” | **YELLOW** — Kraken Pro **Tier 1 since 2026-07-09** is **0.40% maker / 0.80% taker** |
| This file as fund gate / live / keys | **RED** |
| 1-limit rescore | **in flight** — no invented cells |

**Overall:** a 15m XRPEUR invert **charged as a taker at 26 bps on every fill**, trading often enough to print thousands of clips, **does not survive 2023→now** on the operator TWO-CLIP print, and **should not be expected to** from the range math. Survival at 26 bps in the public record is a **slower clock** and/or **wider spacing** and/or **maker** problem — not “run the same 15m invert harder.” **H- not applied.** Still paper.

---

## 1. Simple first — round-trip 0.52% vs typical 15m range

### 1.1 The tax (locked on this desk)

From invert-paper / PLAN-invert-wf-2023 / Coder 01 (unchanged here):

| Column | Per fill | Round-trip (buy+sell) | EUR 200 clip, euros |
|---|---|---|---|
| **Primary** (paper engine “Starter taker”) | **0.26%** | **0.52%** | **0.52 / 1.04** |
| Shadow | **0.40%** | **0.80%** | **0.80 / 1.60** |
| Shadow taker stress | **0.80%** | **1.60%** | **1.60 / 3.20** |

Two fills = two fees. Gate-1 is shadowed return, not mark-to-market. EUR 200 is the live fill-1 quote (`PAPER-00029` cost ~199.99999794 @ 1.24496). Percent does not care about 200 vs 10000. Euros do: `fee_eur = clip × rate × n_fills`.

### 1.2 Typical 15m range (do not use the 7.5-day now-tape as 2023)

REST `OHLC interval=15` returns **720 committed bars ≈ 7.5 days**. Sibling `#197` already called using that window as 2023 **RED**. This sitting’s 15m tape (2026-08-20 08:15Z → 2026-08-27 20:00Z):

| Stat on `(high−low)/mid` | Last 7.5d 15m (n=720) |
|---|---|
| median | **0.79%** |
| p25 / p75 | 0.52% / 1.17% |
| mean | 1.00% (pulled by spikes) |
| frac ≥ 0.52% / 0.80% / 1.60% | 0.76 / 0.49 / 0.13 |
| max | **22.72%** at `2026-08-22 05:00Z` (high 1.45274 / low 1.1563) |

That median is a **noisy now-tape**, including a 22% 15m bar. It is **not** “typical 2023→now.” Do not promote it.

**2023→now proxy (public, no invented 15m file):**

| Series (this sitting) | Window | Median `(H−L)/mid` | Implied 15m if range ~ √time |
|---|---|---|---|
| Weekly REST `interval=10080` | **2022-12-29 → 2026-08-20** (n=191 weeks) | **12.07%** | 12.07 / √(7×96) ≈ **0.47%** |
| Daily REST `interval=1440` | **2024-09-06 → 2026-08-26** (n=720; REST cap, **not** full 2023) | **4.45%** (p25 3.10, p75 7.09, p90 11.13) | 4.45 / √96 ≈ **0.45%** |

Weekly 2023+ and daily 2024-09+ agree. **Typical 15m range ≈ 0.45–0.47%.** Daily p25 implies a quiet 15m ≈ **0.32%**.

REST 1h (last 720 hours from 2026-07-28): median range **0.53%**, frac ≥ 0.52% = **0.51**. REST 4h (from 2026-04-29): median **1.20%**. Order of magnitude matches √time. Not a 2023 15m dump.

### 1.3 The inequality

```text
round-trip tax          typical 15m range
0.52%  (primary)     vs   ~0.45–0.47%
0.80%  (0.40 shadow) vs   ~0.45–0.47%
1.60%  (0.80 shadow) vs   ~0.45–0.47%
```

**A system that harvests one 15m bar as its whole round-trip is underwater at 0.26% taker** even if it captured **100%** of a typical bar’s high–low. Quiet bars (daily p25 scaling ~0.32%) are worse. The 7.5-day median 0.79% is a spike week, not a license.

Open-to-close on that same 7.5-day tape (median **0.36%**, mean 0.51%) is smaller still. Wick range is the optimistic “room”; close-to-close is what a close-model actually banks.

**Simple answer:** 26 bps × 2 is a **15m-range-sized tax** on XRPEUR. 15m invert does not get a free lunch from “crypto is volatile.” Volatility is there on **days and weeks** (daily median range 4.45%, weekly 12%). It is **not** 0.52% sitting inside a typical 15-minute candle.

### 1.4 EUR 200 clip — euros, not a pardon

| n fills | Primary fees at EUR 200 × 0.26% | vs paper 10k |
|---|---|---|
| 1 (live `PAPER-00029`) | **0.52 EUR** | 0.0052% of book |
| 20 (lab clip rate, 8 days) | 10.40 EUR | 0.10% |
| 7923 (operator TWO-CLIP) | **4119.96 EUR** | **41.2%** of 10k if price_pnl ≈ 0 |
| 9097 at EUR 200 (not the 9097 print’s sizing) | 4730 EUR | 47% — ugly, **not** dust to 1.00 |

EUR 200 **prevents** the 100%-equity dust path (PR #201: 10000 → 1.00 needs all-in). It **does not** prevent a 41% fee hole if you still print ~8k taker fills with no price edge.

Live TP spacing (not a fill): `1.26778 / 1.24496 − 1` = **+1.833%** gross. Two 0.26% hits leave ~**+1.31%** **if** 00030 prints. That hypothetical is **2 < 8** and is **not** 2023→now. It only shows a **wide** Lo/Hi *can* beat 0.52%. Adjacent fib ticks often cannot.

---

## 2. Operator prints (cite, arithmetic only — not a new score)

### 2.1 9097-fill — fill-every-rung, not invert

PR [#201](https://github.com/eyeskull2220/solana-invoice/pull/201) `REVIEW-wf-2023-score.md`: named 15m print **BINANCE-VISION-XRPEUR + Kraken tail**, n=128142, close-model, fills **9097**, return after fees **−99.989999%**, maxDD **99.990007%**, EUR 10000 → **1.00**. Reviewer: **RED**, not a fair invert. Retired fill-every-rung `2bfb1b68`. 100% equity. Same-bar both sides not designed out.

Do **not** reuse −99.99% as “invert vs 26 bps.” That number is a **floor + spray**. Reviewer already wrote: 9097 × 0.26% × 200 ≈ 4730 EUR of fees on the **locked clip** — ugly, not 1.00. Dust requires all-in.

### 2.2 invert-v2 day0 TWO-CLIP — operator-stated this sitting

| Cell | Operator | Arithmetic this file |
|---|---|---|
| Fills | **7923** | — |
| Return | **−41%** | (36 − 4120) / 10000 = **−40.84%** |
| Fees | **4120** | 7923 × 200 × 0.0026 = **4119.96** |
| price_pnl | **+36** | +36 / (7923/2) / 200 = **+0.0045%** gross **per round-trip** |

Fees match **primary 0.26% on EUR 200 × 7923 fills** to the euro. price_pnl +36 says the **market almost did not pay**. Net is the fee column. **This file does not invent a different PnL.** 1-limit rescore is **in flight** — no cells for it.

If TWO-CLIP = two concurrent EUR 200 lots on ~128k bars (~1334 days): 7923 fills ≈ **5.9 fills/day** ≈ **3.0 round-trips/day** if paired. Lab clip rate was **2.5 fills/day** over 8 days. Not the same book, not a splice.

### 2.3 47-bar mean hold — is it enough?

47 × 15 m = **705 min = 11.75 h**.

Brownian scale from daily median 4.45%:

```text
range_47 ≈ 4.45% × √(47/96) ≈ 3.11%
```

Break-even **if** the strategy captures fraction `f` of that scaled range:

| Capture `f` of scaled range | 0.26% RT 0.52% | 0.40% RT 0.80% | 0.80% RT 1.60% |
|---|---|---|---|
| 100% | ~1.3 bars (0.3 h) | ~3 bars | ~12 bars |
| 50% | ~5 bars (1.3 h) | ~12 bars | **~50 bars ≈ 47** |
| 25% | ~21 bars (5.2 h) | **~50 bars ≈ 47** | ~198 bars (2.1 d) |
| 10% | ~131 bars (33 h) | ~310 bars (3.2 d) | ~1241 bars (13 d) |

**Geometry:** 47 bars **can** cover 0.52% if invert actually banks ~**17%+** of a ~3% hold-range (or a **fixed Lo/Hi** ≥ ~0.52% plus slippage). Live 00029→00030 spacing **1.83%** would be enough **per closed pair**. Tight next-fib rungs would not.

**invert-v2 captured edge:** +0.0045% gross per RT vs 0.52% tax ≈ **capture ≈ 0**. 47 bars of clock time did **not** produce 47 bars of *paid* mean reversion on that print. Hold time is not edge. **Do not upgrade +36 into a 3% capture.**

---

## 3. Broaden — what 15m mean-reversion / grid systems survive 26 bps?

Public record, not our engine. None of these rewrite invert.

### 3.1 Sign exists; size does not pay the fee

[Neklyudov, 2026, arXiv:2608.21888](https://arxiv.org/html/2608.21888) — *Short-horizon mean reversion in cryptocurrency markets* (15m, 183 Binance pairs, walk-forward):

- Directional 15m reversal is **real** (AUC small, 90% of crypto pairs vs 2.7% of US stocks).
- Gross edge per trade peaks near **1.3 bp**. Cheapest spot round-trip band cited **5 bp**; taker band **10–20 bp**.
- **Not one of 183 pairs** clears even the **5 bp maker** band at any confidence threshold. Median pair **0.46 bp**. 5-minute is worse (0.15 bp).

26 bps **per side** (52 bp RT) is **~40×** that 1.3 bp peak. 15m *sign* mean reversion is a microstructure leftover. It is **not** a 26 bps taker business.

### 3.2 Naked 15m mean reversion, averaged, loses

[Coinquant, 2026-08-03](https://www.coinquant.ai/blog/building-a-mean-reversion-strategy-in-cryptocurrency-markets-evidence-from-78-backtests) — 78 backtests, BTC/ETH, 15m/1h/4h/1d, fees on:

| Timeframe | Average return (their grid) |
|---|---|
| **15m** | **−14.4%** |
| 1h | −8.1% |
| 4h | −9.5% |
| 1d | −4.0% |

One 15m Bollinger run: **693 trades**, **> $2,300 fees** on $10,000 — same shape as a fee column eating the book. They also scaled a 5% daily MA-distance threshold down to **~0.6% on 15m**. 0.6% vs our 0.52% RT is a **thin** margin before slippage; at 0.80/1.60 shadows it is negative **by construction**.

### 3.3 Same 0.26% Kraken taker, slower clock

[nar1-frames, DEV, 2026-08-21](https://dev.to/nar1frames/i-built-a-crypto-trading-bot-it-lost-to-doing-nothing-355a) — Kraken taker **0.26% per side**, honest fees, walk-forward (trend-follow, not invert — cited for **fee×timeframe**, not for our recipe):

| Timeframe | Trades | Fees | Net |
|---|---|---|---|
| **1 day** | 14 | 1.3%/yr | **+4.33%** |
| **4 hours** | 61 | 11.4%/yr | **−6.01%** |
| **1 minute** | 52 in 45 days | 23.5% in 45 days | **−25.18%, zero wins** |

Quote: on 1-minute bars “the fee is roughly six times the average move you’re trying to catch.” That is the same inequality as §1, one octave faster. **4h already dies at 26 bps** in that study. 15m is between 4h and 1m.

### 3.4 Grids: spacing must exceed round-trip, or “grid profit” is a lie

Practitioner consensus (not XRPEUR invert scores):

- [cryptogates.io — grid backtest mistakes](https://cryptogates.io/common-grid-trading-mistakes-in-crypto-backtests/): tight grids, high trade count, fees 40–55% of gross; “small range movements often can’t cover transaction costs.”
- [vantixs — slippage/fees](https://vantixs.com/blog/slippage-fees-funding-crypto-backtests): altcoin grid with 0.3% spread + taker ≈ **0.5%+ RT**; “a grid with 0.5% spacing barely breaks even.”
- [trademarkets.pro — perp grids](https://trademarkets.pro/grid-trading-on-perpetuals.html): subtract RT fees from level spacing **before** arming; if residual is tiny, widen, maker-only, or skip.

**What actually survives ~26 bps in that literature:**

| Pattern | Why it can live | Why 15m invert-as-taker may not |
|---|---|---|
| **Daily** (or slower) MR / breakout | Move per trade >> 0.52% | 15m bar is not |
| **Wide grid** (spacing ≥ 2× RT, often ≥ 1–2% on alts) | Each closed pair pays the tax | Full-fib adjacent rungs can be ticks |
| **Maker / post-only** (old Kraken maker 0.16–0.25% RT; **new** Tier 1 maker RT is **0.80%**) | Cuts the tax if you **rest** | Paper engine **defaults 0.26% taker**; live Tier 1 maker is **not** cheap after 2026-07-09 |
| **Low turnover** | Fewer × 0.52% | 5–7 fills/day × years is a fee factory |
| **EUR 200 (or smaller) clip + skip extra rungs** | Caps euros, not percent | TWO-CLIP still paid 4120 EUR |

Fill-every-rung is the anti-pattern: every wick is a fill; spacing collapses to the fib mesh; fees ≈ capital (9097 path) or fees ≈ 41% with flat price (7923 path).

### 3.5 Kraken schedule this sitting (shadows are not imaginary)

Official [Kraken fee schedule](https://www.kraken.com/features/fee-schedule) **Spot Crypto**, cross-platform tiers from [9 July 2026](https://support.kraken.com/articles/cross-platform-fee-tier-changes):

| Tier | 30d spot vol / AoP | Maker | Taker |
|---|---|---|---|
| **Tier 1** | $0+ | **0.40%** | **0.80%** |
| Tier 2 | $2.5k+ | 0.30% | 0.60% |
| Tier 3 | $10k+ or $20k AoP | 0.22% | 0.38% |

Paper **0.26%** is the **old** Starter-taker language still locked on invert-paper. **Live entry without volume/AoP is 0.80% taker / 0.40% maker** — exactly the desk’s **0.40 / 0.80 shadows**. A 2023→now replay at 0.26% **understates** a post-July-2026 live Starter. XRPEUR is **spot crypto**, not the cheaper stablecoin/FX table.

Kraken+ fee waiver is **app Instant Buy**, not Pro/API spot. Irrelevant to invert limits.

---

## 4. Hypotheses (labeled `H-` — **not applied**)

Would change invert or the fee column. Written so a later PLAN can pick them. **This file applies none.**

| Id | Hypothesis | Why it is not “just research” |
|---|---|---|
| **H-1** | Score **maker** (post-only) as primary, taker as shadow | Changes the locked 0.26% taker default. After 2026-07-09, Tier 1 **maker** is 0.40% anyway (RT 0.80%). |
| **H-2** | Min rung gap ≥ `k × round-trip` (e.g. k=2 → 1.04% at 0.26%) before a pair may arm | Changes full-fib “every level is a rung” density. |
| **H-3** | Decision clock **1h / 4h / 1d**; 15m only for touch fills | Changes the 15m invert lock. |
| **H-4** | **One** invert pair (00029/00030 pattern), not TWO-CLIP, not fill-every-rung | 1-limit rescore is **already in flight**. Do not steal its PnL here. |
| **H-5** | Promote 0.40/0.80 from shadow to **primary** for any live-shaped column | Honest vs July 2026 Tier 1; would recolor every paper PASS at 0.26%. |
| **H-6** | Hold-to-target **≥ N bars or ≥ X%**, else do not re-arm | Changes swap/re-arm. 47 bars was clock, not a gate. |

**Not hypotheses — already locked, do not bargain:** no naked short; re-arm only on opposite; EUR 200 clip; `invert-paper` stays fill 1; `invert-wf-2023` is not the fund gate; no keys; no orders.

---

## 5. RED / YELLOW / GREEN

### RED

- Treating typical 15m range as “plenty vs 26 bps.” Scaled 2023+ weekly / 2024-09+ daily says **~0.45–0.47%** vs **0.52%** RT.
- Treating EUR 200 as a survival proof. It caps euros; 7923 × 0.52 EUR = **4120**.
- Calling 9097 / −99.99% “invert vs fees.” Fill-every-rung + 100% + close-model (PR #201).
- Replacing invert-v2 −41% / +36 price_pnl with a hypothetical 47-bar 3% capture.
- Using 7.5-day REST 15m (median 0.79%, max 22.7%) as the 2023→now range.
- Funding / live / keys / reseal / `dca-paper` reset / 20+1 with the lab clip.
- Applying H-1…H-6 inside this PR.

### YELLOW

- 47-bar hold **geometry** vs 0.52% (possible at high capture; invert-v2 capture was ~0).
- Daily REST starts 2024-09-06 (720 cap). Weekly covers 2023; implied 15m is a **√time model**, not a downloaded `XRPEUR_15.csv`.
- 2026-08-22 05:00Z 15m range 22.7% — print quality unknown; excluded from “typical.”
- 0.26% primary vs live Tier 1 **0.80% taker** after 2026-07-09.
- 1-limit rescore in flight.
- Kraken MCP down; public REST was enough for this math.

### GREEN

- Simple inequality stated before broadening.
- Operator TWO-CLIP arithmetic checks (4120 = 7923 × 200 × 0.0026).
- 9097 named as fill-every-rung, not invert.
- Literature: 15m MR/grid at ~26 bps taker dies; slower / wider / (old) maker is the surviving cluster.
- Still paper. Gate stays `invert-paper` fill **1**. `invert-wf-2023` is not the gate. Invert recipe not edited.

---

## 6. What this file is not

1. **Not the fund gate.** `invert-paper` fill **1**. Stay paper.  
2. **Not a new invert-wf-2023 score.** No PASS/FAIL for a fair invert on Kraken OHLCVT.  
3. **Not** the 8-day lab clip. Do not reseal `c9689f5d`.  
4. **Not** permission to flatten 00030/00028 or reset `dca-paper`.  
5. **Not** a SEPA instruction. 10k / 200 / 4120 are paper JSON.  
6. **Not** tax advice. Paper is geen belastingfeit.  
7. **Not** a shop / secretaris page / FACTUUR.

---

## Re-check (copy/paste — public / git only)

```bash
curl -sS 'https://api.kraken.com/0/public/Time'
curl -sS 'https://api.kraken.com/0/public/SystemStatus'
curl -sS 'https://api.kraken.com/0/public/Ticker?pair=XRPEUR'
curl -sS 'https://api.kraken.com/0/public/OHLC?pair=XRPEUR&interval=15'  >/tmp/xrp_15.json
curl -sS 'https://api.kraken.com/0/public/OHLC?pair=XRPEUR&interval=1440' >/tmp/xrp_1d.json
curl -sS 'https://api.kraken.com/0/public/OHLC?pair=XRPEUR&interval=10080' >/tmp/xrp_1w.json
# 15m first bar must be days, not years, behind now (720 ceiling)
# weekly first bar 2023+ must exist (pair listed 2017-05-18)

curl -sS https://dca-paper-journal.surge.sh/ | rg -n 'fills|PAPER-00029|NOT MET|c9689f5d|invert-paper' || true
```

Fee table: https://www.kraken.com/features/fee-schedule (Spot Crypto Tier 1 = 0.40 / 0.80).  
July 2026 change: https://support.kraken.com/articles/cross-platform-fee-tier-changes  

Count fund-gate fills only from `PAPER-*` **prints** on **`invert-paper`**. Resting 00030 and open 00028 do not count. 7923 and 9097 are **research-book / rejected-replay** counts, not a ping.

**`invert-wf-2023` may measure 2023→now. It may not fund. A 15m invert at 26 bps taker with thousands of EUR 200 clips is a fee factory unless each closed pair’s spacing (and captured move) clears 0.52% — typical 15m range does not. H- not applied. Still paper.**
