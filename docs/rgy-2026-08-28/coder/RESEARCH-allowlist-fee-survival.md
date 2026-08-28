# RESEARCH — Which EUR-allowlist PAPER path can survive posted fees and sit in the gate numbers?

**Seat:** RESEARCHER · Coder  
**Lens:** start **simple** (round-trip tax vs range), then one pair at a time. Docs + public GETs only.  
**Date:** 2026-08-28  
**Stamp:** VOORBEELD · paper / simulated · not FACTUUR · not INVOICE · not live-trade advice  
**HEAD (leftover `main` at write):** `2170952`  
**Still paper.** No orders. No keys. No CODE. Invert STOP. Do not reset `invert-paper` or `dca-paper`.  
**`is_fund_gate`:** **false** — this file does not stamp a PASS.

**Question (CEO 2026-08-28 21:48 Europe/Brussels):** what Kraken PAPER path on the EUR allowlist can actually survive posted fees **and** sit inside the funding-gate numbers?

Gate (all three, on a **named book later** — **not** `invert-paper`, **not** `dca-paper`):

1. return > 0 after fees  
2. fills ≥ 8  
3. max DD ≤ 8%

No path in this file **PASSES** that gate. There is **no** named scorecard here. Geometry + public ranges only. Inventing fills / return / DD would be cheating.

---

## Locks (this sitting — do not bargain)

| Lock | Status |
|---|---|
| Invert STOP. D6 / 1-limit / 15m invert fee factory stay dead | **held** |
| Do not CODE from [PLAN #196](https://github.com/eyeskull2220/solana-invoice/pull/196) or [PLAN #207](https://github.com/eyeskull2220/solana-invoice/pull/207) | **held** |
| Do not open invert variants | **held** |
| `invert-paper` fill **2** stays. Cap **2**. No third buy | **held** — `PAPER-00031` buy XRPEUR @ **1.23084**; TP `PAPER-00032` @ **1.24496** + `PAPER-00030` @ **1.26778** still open. Cite [journal](https://dca-paper-journal.surge.sh/) 2026-08-28, do not ping / flatten / reset |
| Do not reset `dca-paper` | **held** — five BTCUSD slices @ 78900.6 |
| Still paper. No live. No API keys. No Phantom | **held** |
| EUR allowlist only | **held** — XRPEUR, XLMEUR, HBAREUR, ADAEUR, QNTEUR, XDCEUR, ALGOEUR |
| IOTA is **not** Kraken spot | **held** — do not invent a pair |
| No ISO-20022 basket. No memecoins | **held** |
| Sleeve 3x only XRP/XLM/HBAR/ADA/ALGO. QNT + XDC spot-only | **held** |
| Fee rails (do not invent others) | **primary 0.26% taker** (paper journal). Shadows: Kraken Pro **Tier 1 since 2026-07-09 = 0.40% maker / 0.80% taker** |
| Round-trip = **2×** one-way. Closed clip underwater unless price move **> RT** | **held** |

**Steal (already landed — do not re-litigate invert):**

- [PR #216](https://github.com/eyeskull2220/solana-invoice/pull/216) — seven style families (trend, mean-reversion, grid, fib, invert, DCA, leverage).
- [PR #217](https://github.com/eyeskull2220/solana-invoice/pull/217) — 15m fade does not pay 0.26% taker. Survival cluster is **slower clocks and low n**.
- [PR #211](https://github.com/eyeskull2220/solana-invoice/pull/211) — 15m XRPEUR invert needs **> 0.52%** banked per closed pair at 0.26% taker; typical 15m range **~0.45–0.47%**.
- Named invert prints stay **FAIL** (cite, do not rescore): Vision 1-limit **2779 / −15.21% / 15.49% DD**; Kraken D6 **2665 / −16.03% / 16.34% DD**.
- 8-day sealed invert lab clip `sha256:c9689f5d` was **+0.681154% / 20 fills / maxDD 0.890854%** — lab only, **not** the fund gate.
- `fib-grid-xrpeur-30d` sealed on `lab-fibgrid` (`sha256:b5976d5c7cdf16ea8b3966d46f9fe534547a79cda52b4810580ae6af8bdba517`) before scoring. Offline. **Not** the fund gate.

Kraken this sitting (public, no key): `GET /0/public/Time` → `unixtime` **1787946661** (`Fri, 28 Aug 26 19:51:01 +0000`). `SystemStatus` → `online`. Kraken MCP on this VM: **error / undiscoverable**. REST only.

---

## Simple first (30 seconds)

Paper charges **0.26% per fill**. A closed clip is two fills. Tax = **0.52%**. If the move you harvest is smaller than that, you lose even with a perfect fill.

15m on XRPEUR does not contain 0.52% on a typical bar ([#211](https://github.com/eyeskull2220/solana-invoice/pull/211)). That clock is dead for this fee. Do not revive it. Do not fade 15m on any allowlist pair.

Days and 4-hour bars **do** contain 0.52% on every allowlist pair this sitting (table below). That is **room**, not a score. Room does not print 8 fills. Grinding n to *force* 8 fills is how 2779 / 2665 died.

Clip **EUR 200** on a **10k** book makes the **8% DD** gate structurally easy on **spot** (two clips to zero ≈ 4% of book + fees). The hard parts are **return > 0 after fees** (must bank > RT per closed pair) and **fills ≥ 8 without grinding**.

---

## 1. Min favorable move per closed clip

Identity, not a backtest. CEO lock: round-trip = **2×** the one-way rate.

| One-way (per fill) | Round-trip | Min move to be net > 0 | On clip **EUR 200** | On clip **EUR 100** (1% of a 10k book) |
|---|---:|---:|---:|---:|
| **0.26%** taker (paper primary) | **0.52%** | **> 0.52%** | **> 1.04 EUR** | **> 0.52 EUR** |
| **0.40%** maker (Tier 1 shadow) | **0.80%** | **> 0.80%** | **> 1.60 EUR** | **> 0.80 EUR** |
| **0.80%** taker (Tier 1 shadow) | **1.60%** | **> 1.60%** | **> 3.20 EUR** | **> 1.60 EUR** |

Percent does not care about 200 vs 100. Euros do.

Eight fills at clip 200 × 0.26% = **4.16 EUR** = **0.0416%** of a 10k book. That is the **fee floor** if you stop at 8. Return > 0 still needs the **price** column to clear it. Four closed pairs must each bank **> 0.52%** (primary) / **> 0.80%** / **> 1.60%**.

Live Kraken Pro **Tier 1 since 2026-07-09** is **0.40% maker / 0.80% taker** — not a maker rebate. ([Fee schedule](https://www.kraken.com/features/fee-schedule); [cross-platform tiers, last updated 2026-07-09](https://support.kraken.com/articles/cross-platform-fee-tier-changes); [Kraken Blog 2026-07-09](https://blog.kraken.com/product/pro/new-kraken-pro-fee-tiers).) Paper **0.26%** is the **old** Starter-taker language still locked on the journal. Scoring a paper PASS at 0.26% **understates** a post-July-2026 live Starter.

---

## 2. Allowlist pairs — range / vol (public REST, 2026-08-28)

Ticker-confirmed **online** this sitting via `GET /0/public/AssetPairs` + `GET /0/public/Ticker`. IOTA / MIOTA: **zero** AssetPairs keys; Kraken Pro [markets list](https://support.kraken.com/articles/kraken-markets) has **no** IOTA row. **Do not invent `IOTAEUR`.**

Margin leverage from AssetPairs this sitting: XRP/ADA up to 10×; XLM/HBAR/ALGO **2–3×**; **QNT and XDC `leverage_buy`/`leverage_sell` empty → spot-only.** Matches the CEO sleeve lock.

OHLC is Kraken public REST, last-**720** bars (not a 2023 dump). **4h** window ≈ 2026-04-30 → 2026-08-28. **1d** window ≈ 2024-09-07 → 2026-08-28 except HBAR listed **2025-07-10** (n=415) and XDC listed **2025-09-02** (n=361). Range = `(high−low)/mid`. This is **bar room**, not captured edge, not fills.

Implied 15m ≈ daily median / √96 (Brownian scale, same method as [#211](https://github.com/eyeskull2220/solana-invoice/pull/211)). Labeled **proxy**. Not a downloaded 15m file.

| Pair | 24h last / range / base vol (Ticker 19:51Z) | 4h median range (n=721) | 4h frac ≥ 0.52% / ≥ 1.04% / ≥ 1.60% | 1d median range | 1d frac ≥ 0.52% / ≥ 1.04% | Implied 15m | Clears fee hurdle often enough for ≥8 fills **without** grinding n? |
|---|---|---:|---|---:|---|---:|---|
| **XRPEUR** | 1.1886 · 7.04% · 9.56M | **1.21%** | 0.932 / 0.598 / 0.340 | **4.46%** (n=721) | 1.00 / 0.997 | **~0.46%** | **1d yes / 4h maybe / 15m no.** Invert-paper already lives here — **do not mix.** |
| **XLMEUR** | 0.1536 · 6.91% · 2.31M | **1.80%** | 0.981 / 0.759 / 0.553 | **4.98%** | 1.00 / 0.997 | **~0.51%** | **1d yes / 4h often.** Liquid enough for clip 200. |
| **HBAREUR** | 0.0657 · 7.24% · 2.57M | **1.30%** | 0.939 / 0.656 / 0.337 | **4.70%** (n=415, from 2025-07-10) | 1.00 / 1.00 | **~0.48%** | **1d yes / 4h maybe.** Short listing. Not first path. |
| **ADAEUR** | 0.1747 · 8.34% · 8.59M | **1.77%** | **0.988 / 0.824 / 0.558** | **5.79%** | 1.00 / 1.00 | **~0.59%** | **1d yes / 4h best fee-clear among liquid names.** Implied 15m only *thinly* above 0.52% — still **do not** fade 15m (capture ≠ 100% of wick; 0.80 shadow kills it). |
| **QNTEUR** | 52.43 · 4.38% · 781 QNT (~41k EUR) | **1.25%** | 0.867 / 0.594 / 0.344 | **5.00%** | 1.00 / 1.00 | **~0.51%** | **1d yes / 4h maybe.** Thin EUR book. **Spot-only.** |
| **XDCEUR** | 0.0236 · 3.91% · 5.11M | **1.04%** | **0.756 / 0.498 / 0.311** | **3.75%** (n=361, from 2025-09-02) | 0.997 / 0.983 | **~0.38%** | **Weakest 4h.** Half of 4h bars fail 2× primary RT. **Spot-only.** Not first path. |
| **ALGOEUR** | 0.0746 · 6.91% · 1.70M | **1.82%** | 0.974 / 0.773 / 0.566 | **5.85%** | 1.00 / 1.00 | **~0.60%** | **1d yes / 4h often.** Widest daily; 28% of 1d bars have range **> 8%** (coin, not book). |

**Read the 15m column slowly.** XRPEUR ~0.46% vs 0.52% RT is the [#211](https://github.com/eyeskull2220/solana-invoice/pull/211) knife-edge, rechecked this sitting from the same daily REST. XDC is worse. ADA/ALGO implied 15m ~0.59% is **not** a 15m licence — typical capture of a bar is not the whole wick, and the 0.40/0.80 shadows are 0.80/1.60% RT.

**1d:** every allowlist pair’s median daily range is **~4–6%**, so a **wide** closed clip (rails, not adjacent ticks) **can** clear 0.52% on ordinary days. That is geometry. **UNVERIFIED** as fills.

**4h:** median **1.0–1.8%**. ADA/ALGO/XLM clear 1.04% (2× primary RT) on **~75–82%** of 4h bars. XDC only **~50%**. A 4h harvest with **spacing ≥ 1.04%** is the first clock that is not dead on arrival at 0.26% taker.

Sources: [Kraken OHLC](https://docs.kraken.com/api-reference/market-data/get-ohlc-data) · [Ticker](https://docs.kraken.com/api-reference/market-data/get-ticker-information) · [AssetPairs](https://docs.kraken.com/api-reference/market-data/get-tradable-asset-pairs) · fetched **2026-08-28 19:51–19:52 UTC**.

---

## 3. Rank PAPER PATHS (not invert)

None of these is a PASS. Rank = “could this *geometry* sit in the three numbers on a **new** book,” not a scorecard.

| Rank | Path | Fees | fills ≥ 8 | max DD ≤ 8% | Notes |
|---:|---|---|---|---|---|
| 1 | **Wide fib, 4h/1d rails, one pair, clip 200, N=1 ping-pong** | Spacing **≥ 1.04%** (2× primary) so a closed pair is not underwater by construction. 1d median 4–6% contains that. | **Possible** if the tape chops across two prices often enough. 4 closed pairs = 8 fills. Calendar: **weeks**, not 15m. Trend months leave the opposite sitting → n stays thin. **UNVERIFIED.** | **Easy on spot** at clip 200 / cap 1–2 (two clips to zero ≈ 4% of 10k). | Steal from [#217](https://github.com/eyeskull2220/solana-invoice/pull/217) survival cluster: slower clock, low n, wide gap. **Not** 14 rungs. **Not** invert-paper. |
| 2 | **Wide grid, one pair, spacing vs fee** | Same identity: adjacent gap **< 0.52%** ⇒ every cycle loses. Journal sketch of **3 buy / 3 sell around last** is a density trap unless spacing is locked **≥ 1.04%** (band then ~5%+). | 6 live levels print **fast** — that is how 9097 died. Cap working orders or you grind n into fee death. **UNVERIFIED.** | Clip 200 helps; a 6-level spray does **not** (inventory drift). | `grid-paper` already named on the journal as a **track**, not a score. Do not copy 3/3 tight around last. |
| 3 | **Slow DCA on one EUR pair** | 8 × 200 × 0.26% = **4.16 EUR**. Tiny vs 10k. Not a harvest problem. | **Calendar:** weekly clip 200 → n=8 in **8 weeks**. Daily → 8 days. Expected n = cadence × days. All **buys** unless you add sells (then it is not DCA). | Clip 200 × 8 = 1600 deployed. Coin must drop **~50%** to hit 8% **book** DD. Quiet-week DD likely ok. **UNVERIFIED** path. | Return > 0 is a **beta bet**, not fee-survival of closed clips. New book only — **do not** reset `dca-paper` (BTCUSD held). |
| 4 | **Long-term hold of a EUR stack** | One or two taker buys. Fee is dust. | **Tension:** a hold does **not** print 8 fills unless you slice it into DCA. Flag: fills ≥ 8 **vs** “set and forget” are opposite instructions. | Same clip-200 cushion if you don’t go all-in. All-in ADA/ALGO: 25–28% of 1d bars have range **> 8%** — 8% DD on a full book is a **common week**, not a tail. | [#216](https://github.com/eyeskull2220/solana-invoice/pull/216) family 6. Kraken’s own DCA primer is weekly/monthly, not 15m. ([Kraken Learn — DCA](https://www.kraken.com/learn/finance/dollar-cost-averaging).) |
| 5 | **Maker-only resters** | **Does not cut the paper primary.** Journal `invert-paper` this sitting: `fee_rate 0.0026` on **every** print ([journal](https://dca-paper-journal.surge.sh/)). Sibling packs already locked paper as **0.26% taker**, not maker ([#211](https://github.com/eyeskull2220/solana-invoice/pull/211) §3.5). Live Tier 1 **maker is 0.40%** (RT **0.80%**) — **worse** than paper 0.26% taker. | Resting limits can still print 8. Queue / missed fills **UNVERIFIED** on paper. | Unchanged vs spot clip 200. | **UNKNOWN** whether this paper engine can be maker as a **fee** column. Even if a post-only flag exists, the **journal rail stays 0.26% taker**. Not a first path. |
| 6 | **3x sleeve (XRP/XLM/HBAR/ADA/ALGO only)** | Futures fees + funding = a **third** tax column. Do not mix into spot. | Named sleeve already **FAIL fills < 8**: PF_XRPUSD **6 / −2.729078% / 5.326685% DD**. Cite, do not invent a pass. | **Likely fails 8% DD.** 3× means **~2.67%** adverse spot ≈ 8% sleeve DD. Allowlist **1d p25** ranges are **already 3–4%**. A quiet day can breach the gate. Kill switch at 10% peak DD is **wider** than the 8% gate — too late. | **Do not recommend as first path.** QNT/XDC never. No IOTA perp. No live. |

Public 4h **trend-follow** at the same 0.26% Kraken taker already died in one study (61 trades, **−6.01%** on 4h; 1d **+4.33%** with only **14** trades / years). ([nar1-frames, DEV, 2026-08-21](https://dev.to/nar1frames/i-built-a-crypto-trading-bot-it-lost-to-doing-nothing-355a).) Steal **fee × clock**, not that Donchian recipe. 14 trades **fails fills ≥ 8** in any short paper window. That is the gate’s built-in bind: **slow enough to beat fees ↔ maybe too slow for 8 prints.**

---

## 4. ONE recommended next paper path

**Not a PASS. No named scorecard. `is_fund_gate: false`.**

| | Try **next** |
|---|---|
| **Pair** | **ADAEUR** |
| **Clock** | **4h** decision / touch; **1d rails** (prior-day H and L as the two prices). Not 15m. |
| **Style** | **Wide fib / two-price ping-pong** (family 4 catalog, family 3 with **N = 1**). One resting buy below, one resting sell above. After a fill, only the **opposite** is working. **Not** 14 rungs. **Not** invert. **Not** 3/3 grid. |
| **Clip** | **EUR 200** |
| **Spacing lock** | Arm only if `(Hi−Lo)/Lo ≥ 1.04%` (2× primary RT). Skip the bar if the rails are inside the tax. Shadow-aware: a live-shaped column would need **≥ 1.60%** to clear Tier 1 taker. |
| **Cap** | **1 long clip** (2 working prices, 0 or 1 inventory). No third buy. |
| **Book name** | **`adaeur-widefib-paper`** — **not** `invert-paper`, **not** `dca-paper`, **not** `grid-paper` (3/3 recipe lives there). EUR 10000 paper. |
| **Fee rail** | Primary **0.26% taker** (paper engine). Shadow 0.40 / 0.80. Do not pretend maker. |

**Why this can clear fees:** ADAEUR 4h median range **1.77%** this sitting; **82.4%** of 4h bars have range **≥ 1.04%**; **every** daily bar in the 720-window cleared 0.52%. A closed pair on **prior-day H/L** is not the 15m knife-edge. [#211](https://github.com/eyeskull2220/solana-invoice/pull/211) / [#217](https://github.com/eyeskull2220/solana-invoice/pull/217) already showed the survival cluster is this clock + this width + low n.

**Why this can reach 8 fills:** 4 closed pairs = 8 prints. On a 4h chop that tags both rails a few times a week, n=8 is **weeks**, not years (1d Donchian’s 14 trades/3y would FAIL this gate). If ADA trends one way, the opposite sits and **n stays < 8** — that is an honest FAIL of *this* path, not a reason to tighten spacing.

**Why this can stay under 8% DD:** clip 200 + cap 1 on a 10k book. ADA to zero on that clip is **2%** of book + 0.52 EUR fee. The 8% DD gate is not the binding constraint **unless** someone sizes up or sleeves 3×.

**Why ADAEUR, not XRP / XDC / ALGO:** XRPEUR is `invert-paper` — do not mix. XDCEUR 4h is the weakest fee-clear (half the bars fail 1.04%) and spot-only. ALGOEUR is slightly wider but thinner EUR volume and more 1d bars with range > 8%. ADAEUR is the liquid name whose 4h most often contains 2× the paper tax.

**What this file will not claim:** fills, return, or DD for `adaeur-widefib-paper`. Those cells are **UNVERIFIED** until a **named scorecard** exists. Public 4h mean-reversion averages are **negative** ([Coinquant 2026-08-03](https://www.coinquant.ai/blog/building-a-mean-reversion-strategy-in-cryptocurrency-markets-evidence-from-78-backtests) 4h avg **−9.5%**) — that is **fade density**, not two-price rails. Do not launder Coinquant into a PASS.

If this path is not run, and no other new book is scored: **FAIL** the question as asked. Nothing on the allowlist currently **sits inside** the three numbers with a named scorecard except invert lab `c9689f5d` (not the gate) and invert-paper n=2 (gate **NOT MET**).

**What would have to change on an honest FAIL of the try:**

- **Clock** — do not go back to 15m. If 4h still fee-grinds, slow to **1d** and accept a longer wait for n=8 (or the gate’s fills≥8 is the thing that has to give).  
- **Spacing** — if adjacent gaps sneak under 0.52%, widen (k=2 already locked above) or skip. Tightening to get fills is fee death.  
- **Maker** — will **not** save paper (0.26% taker anyway) and **hurts** live Tier 1 (0.40% maker). Not the lever.  
- **n** — cap working orders at 1 lot. Raising n to hit 8 faster is the 2779/2665 machine.

---

## 5. Will-not-do (honoured)

- No invert **CODE**. No invert variants. No D6 / 1-limit / 15m invert fee factory.  
- No CODE from PLAN [#196](https://github.com/eyeskull2220/solana-invoice/pull/196) or [#207](https://github.com/eyeskull2220/solana-invoice/pull/207). Do not edit `PLAN-lock-wf.md`.  
- No 15m fade on any allowlist pair.  
- No IOTA / MIOTA pair. No ISO-20022 basket. No memecoins.  
- No live. No API keys. No Phantom spend.  
- No reset of `invert-paper` (fill **2** stays, cap **2**, no third buy) or `dca-paper`.  
- No reseal of `c9689f5d` or `b5976d5c…`. No prettier 2779 / 2665.  
- No 3x as first path. No QNT/XDC sleeve.  
- No invented fills, return, or DD. No PASS without a named scorecard.

**Promotion: no.** Stay paper. Gate on `invert-paper` remains **NOT MET** (fills 2/8). This file’s candidate book is **not opened here**.

---

## Verdict

| Probe | Color |
|---|---|
| 0.52 / 0.80 / 1.60 RT math on clip 200 and clip 100 | **GREEN** (identity) |
| 15m fade on the allowlist | **RED** — XRPEUR typical ~0.46%; others not a licence |
| 1d rails vs 0.52% | **YELLOW** geometry (room exists) · **UNVERIFIED** fills |
| 4h ADAEUR vs 1.04% | **YELLOW** — 82% of bars have the room · not a score |
| XDCEUR 4h | **RED** as first path (weakest fee-clear) |
| Maker-only on this paper engine | **RED** as a fee cut (still 0.26% taker) |
| 3x sleeve vs 8% DD | **RED** as first path |
| Long hold vs fills ≥ 8 | **RED** tension |
| Named invert prints 2779 / 2665 | **FAIL** · cited, not rescored |
| This file as fund gate | **RED** — `is_fund_gate: false` |
| Recommended try `adaeur-widefib-paper` | **YELLOW** — next experiment, **not a PASS** |

**Overall:** the only honest next paper path that can *clear the tax by construction*, *reach 8 fills on a weeks-scale chop*, and *stay under 8% DD at clip 200* is **ADAEUR / 4h / two-price wide fib / clip 200 / `adaeur-widefib-paper`**. It does **not** PASS until someone prints a named scorecard. If the desk needs a PASS today: **FAIL** — clock, spacing, or the fills≥8 rule would have to change; maker will not save it; invert stays dead.

---

## Sources

Sibling packs

- https://github.com/eyeskull2220/solana-invoice/pull/216 — seven families  
- https://github.com/eyeskull2220/solana-invoice/pull/217 — clocks vs posted fees  
- https://github.com/eyeskull2220/solana-invoice/pull/211 — 15m XRPEUR vs 26 bps  

Fees

- https://www.kraken.com/features/fee-schedule — Spot Crypto Tier 1 **0.40 / 0.80** (fetched 2026-08-28)  
- https://support.kraken.com/articles/cross-platform-fee-tier-changes — last updated **2026-07-09**  
- https://blog.kraken.com/product/pro/new-kraken-pro-fee-tiers — 2026-07-09  

Tape (this sitting)

- https://api.kraken.com/0/public/Time  
- https://api.kraken.com/0/public/SystemStatus  
- https://api.kraken.com/0/public/AssetPairs  
- https://api.kraken.com/0/public/Ticker?pair=XRPEUR,XLMEUR,HBAREUR,ADAEUR,QNTEUR,XDCEUR,ALGOEUR  
- https://api.kraken.com/0/public/OHLC?pair={PAIR}&interval=240|1440  
- https://docs.kraken.com/api-reference/market-data/get-ohlc-data  
- https://support.kraken.com/articles/kraken-markets — no IOTA row  

Literature (fee × clock, not our score)

- https://dev.to/nar1frames/i-built-a-crypto-trading-bot-it-lost-to-doing-nothing-355a  
- https://www.coinquant.ai/blog/building-a-mean-reversion-strategy-in-cryptocurrency-markets-evidence-from-78-backtests  
- https://www.kraken.com/learn/finance/dollar-cost-averaging  

Desk (cite, do not ping / reset)

- https://dca-paper-journal.surge.sh/ — invert-paper fills **2/8**, cap 2, no third buy, fee_rate 0.0026  

---

## Re-check (copy/paste — public / git only)

```bash
curl -sS 'https://api.kraken.com/0/public/Time'
curl -sS 'https://api.kraken.com/0/public/SystemStatus'
curl -sS 'https://api.kraken.com/0/public/Ticker?pair=XRPEUR,XLMEUR,HBAREUR,ADAEUR,QNTEUR,XDCEUR,ALGOEUR'
# IOTA must be absent:
curl -sS 'https://api.kraken.com/0/public/AssetPairs' | python3 -c "import sys,json; r=json.load(sys.stdin)['result']; print([k for k in r if 'IOTA' in k.upper() or 'MIOTA' in k.upper()])"

curl -sS https://dca-paper-journal.surge.sh/ | rg -n 'fills 2|PAPER-00031|1.23084|PAPER-00032|cap 2|NOT MET|dca-paper' || true

rg -n 'is_fund_gate|adaeur-widefib-paper|IOTAEUR|invert STOP|0\\.52|1.04' \
  docs/rgy-2026-08-28/coder/RESEARCH-allowlist-fee-survival.md

# Never:
# kraken paper reset --workspace invert-paper
# kraken paper reset --workspace dca-paper
# kraken order …
```

**Still paper. Invert stays dead. Recommended next (not a PASS): ADAEUR 4h two-price wide fib, clip 200, book `adaeur-widefib-paper`.**
