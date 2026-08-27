# RESEARCH — invert-wf-2023 year slice (2023)

**Seat:** RESEARCHER (Coder pack)  
**Lens:** regimes and Coder checklist. **Not a plan. Not a fill. Not a score.**  
**Date:** 2026-08-27  
**Stamp:** VOORBEELD · paper / simulated · not FACTUUR · not INVOICE · not live-trade advice  
**HEAD (this leftover repo):** `2170952`  
**Still paper.** Do not reseal `c9689f5d`. Do not reset `dca-paper`. No orders. No keys.

This file is the **year-slice pack** for `invert-wf-2023`. It only scopes the **2023** window of one **continuous** invert book. It does not place paper or live orders, does not paste keys, does not spend Phantom, does not rewrite shop HTML, and does not republish the journal.

**Replay status: NOT RUN.** This sitting did not replay XRPEUR 15m invert. Do not invent fills, return-after-fees, maxDD, first/last fill, or a PASS/FAIL for this window.

---

## What this file is

| Item | Lock |
| --- | --- |
| Named walk-forward | `invert-wf-2023` |
| Named book | `invert-paper` (spot EUR, XRPEUR 15m invert) |
| Window this pack scopes | **2023-01-01 00:00:00 → 2023-12-31 23:59:59.999 Europe/Brussels** |
| Pair / TF | **XRPEUR** · **15m** · invert recipe (full fib rungs; after any fill swap those two prices; re-arm only on the opposite fill; **spot no naked short**) |
| Capital | **EUR 10000** is the start of the **continuous book**, stamped at window open (see below). Not a SEPA deposit. Not a live size. |
| Isolation vs fund | Isolated 2023 gate numbers (fills / return after fees / maxDD) are a **diagnostic**. **They do not fund.** |

Sibling year packs (2024–2026) are **later windows of the same book**. They do not re-init EUR 10000.

---

## Continuous book (prefer this)

**Prefer one continuous `invert-paper` book.** This file only scopes the 2023 window. Do not start a fresh 10k book on 2024-01-01, 2025-01-01, or 2026-01-01.

| Stamp | Value |
| --- | --- |
| Book start (continuous) | **2023-01-01 00:00:00 Europe/Brussels** |
| Start equity | **EUR 10000** paper (JSON number). Not a deposit instruction. |
| This slice | 2023-01-01 00:00:00 → 2023-12-31 23:59:59.999 Europe/Brussels |
| Next slice inherits | Ending **shadowed** equity of this window (open inventory, resting limits, cash). **Do not flatten at year-end to “clean” the book.** |
| UTC equivalent (open) | 2022-12-31 23:00:00 UTC (CET, UTC+1) |
| UTC equivalent (close) | 2023-12-31 22:59:59 UTC (CET, UTC+1) |

**DST (Coder must stamp fills in Europe/Brussels, not UTC-as-Brussels):**

- CET (UTC+1) until **2023-03-26 02:00** Brussels.
- CEST (UTC+2) **2023-03-26 02:00 → 2023-10-29 03:00** Brussels.
- CET after **2023-10-29 03:00** Brussels.

If Coder reports first/last fill in UTC without a Brussels conversion, the checklist row is incomplete — not a reason to invent a local time.

**Why continuous, not a reset-per-year book:** invert after a fill **swaps the jobs of those two prices**. Year-boundary `paper init` would drop resting rungs, wipe maxDD memory, and turn a multi-year walk-forward into four lab clips. The 8-day sealed lab clip `c9689f5d` already showed that a short window can look clean. A year slice that resets capital is the same cheat at larger scale.

---

## What this file is not

1. **Not a score.** No invented fill count, return, maxDD, or gate color for 2023.
2. **Not the 8-day lab clip.** `fib-grid-invert-xrpeur-15m` vs `sha256:c9689f5d7d583320e724900b0ce4ef68193878c880d11939badd1dd59016e390` is 2026-08-18 21:00 → 2026-08-26 08:00 Europe/Brussels. Cite. Do not reseal. Do not paste its 20 fills / +0.681154% / maxDD 0.890854% into this year.
3. **Not the live `invert-paper` journal (2026).** Operator book fill 1 `PAPER-00029` @ 1.24496 is **this decade's** walk-forward, not 2023. Do not 20+1. Do not backfill 2023 ids from 00029.
4. **Not `dca-paper`.** Five BTCUSD slices stay held. Not this book.
5. **Not the 3x sleeve.** FAIL stays on the sleeve. Never mix into `invert-paper`.
6. **Not live.** Autonomy **level 2**. No `kraken order`. No API keys. Kraken MCP this run: **error / undiscoverable**. Public `Ticker`/`OHLC` are **now**, not 2023 15m history.
7. **Not a 15m candle dump.** Kraken public OHLC only returns a short recent window. This pack maps **regimes** from cited daily EUR tables + USD monthly heatmaps. Coder's replay must use **venue Kraken XRPEUR 15m**, not this daily FX table as fills.

---

## Gate (reminder — not a 2023 result)

**All three, same book, `invert-paper` only:**

1. Return **> 0 after fees** (Starter **0.26% taker** per print + fee-shadow extra + round-trip). Not mark-to-market. Not buy-and-hold spot.
2. **≥ 8 fills** (`PAPER-*` **prints**. Resting limits are not fills).
3. **maxDD ≤ 8%** from peak equity on **that** book.

Fail any one → stay paper. Isolated 2023 may be scored **after** replay as a diagnostic. **Isolated PASS does not fund. Isolated FAIL does not authorize a reseal or a `dca-paper` reset.**

---

## Data quality (read before the regime map)

Daily EUR prints below are **regime context**, not Kraken 15m invert fills.

**Source A — Pound Sterling Live, XRP/EUR daily OHLC 2023**  
https://www.poundsterlinglive.com/crypto-currency/ripple-to-euro-history-2023  
Fetched 2026-08-27. Table header: High **0.7329** on **20/07/2023**; Low **0.3163** on **01/01/2023**.

**Conflict in the same table (Coder must not launder this into a fill):** the **13 July 2023** row prints high **0.8308**, which is **above** that header's annual high. Traders Union's annual XRP/EUR row lists 2023 high **0.8378** / low **0.285** / close **0.5592** (https://tradersunion.com/currencies/price-history/xrp-eur/). Those are **different aggregators**. **Replay truth is Kraken `XRPEUR` 15m.** If venue high/low disagree with Source A, keep the venue and footnote the aggregator.

**Source B — Kraken XRP/USD monthly (ChartsCheck heatmap)**  
https://www.chartscheck.com/monthly-returns-heatmap/kraken/XRP/USD  
USD monthly % is **not** invert EUR return. Use it only to name trend vs range months. EUR/USD moved in 2023; do not convert USD OHLC with a single FX print and call it XRPEUR.

**Source C — event chronology (why the tape moved)**  
Reuters / CoinDesk / CNBC 2023-07-13 Torres ruling; Fortune 2023-08-23 fade; Forbes/CoinGecko June 5–6 SEC vs Binance/Coinbase; SVB weekend 2023-03-10.

**Expected 15m bar count (calendar, not venue):** 365 × 96 = **35 040** bars in 2023. Coder reports **holes** (missing 15m, halted minutes, Sunday thin books) as data quality. Interpolating a hole into a `PAPER-*` print is journal fraud.

---

## Month-end EUR closes (Source A — regime only)

Daily close, XRP per EUR, Pound Sterling Live table. **Not invert equity.**

| Date (calendar) | Open | High | Low | Close |
| --- | ---: | ---: | ---: | ---: |
| 2023-01-01 | 0.3220 | 0.3223 | 0.3161 | **0.3163** |
| 2023-01-31 | 0.3803 | 0.3878 | 0.3558 | **0.3629** |
| 2023-02-28 | 0.3581 | 0.3587 | 0.3515 | **0.3570** |
| 2023-03-31 | 0.5001 | 0.5123 | 0.4815 | **0.4883** |
| 2023-04-30 | 0.4353 | 0.4418 | 0.4280 | **0.4341** |
| 2023-05-31 | 0.4616 | 0.4928 | 0.4564 | **0.4850** |
| 2023-06-30 | 0.4367 | 0.4436 | 0.4130 | **0.4333** |
| 2023-07-31 | 0.6396 | 0.6547 | 0.6224 | **0.6345** |
| 2023-08-31 | 0.4834 | 0.4861 | 0.4574 | **0.4709** |
| 2023-09-30 | 0.4934 | 0.4934 | 0.4861 | **0.4871** |
| 2023-10-31 | 0.5459 | 0.5816 | 0.5310 | **0.5673** |
| 2023-11-30 | 0.5556 | 0.5586 | 0.5475 | **0.5567** |
| 2023-12-31 | 0.5642 | 0.5702 | 0.5499 | **0.5591** |

Spot path 0.3163 → 0.5591 is about **+77% buy-and-hold**. **That is not invert return.** Invert is rung fills after 0.26% + shadow on each print. Do not write +77% into the post-replay scoreboard.

USD monthly % (Source B, Kraken XRPUSD, for **shape** only): Jan +19.8 · Feb −7.2 · Mar +43.0 · Apr −12.2 · May +9.9 · Jun −8.4 · Jul +47.5 · Aug −26.8 · Sep +0.8 · Oct +16.6 · Nov +1.1 · Dec +1.4.

---

## Notable XRPEUR regimes in 2023 (stress invert)

Invert (full fib set on 15m, swap the two filled prices, re-arm only on the opposite fill, spot flat-cash after a sell-TP) is stressed by **one-way trends** (rungs get run; opposite never prints), **tight ranges** (fee grind: two takers = **0.52%** before shadow), and **gaps/spikes** (15m bar skips rungs; paper instant-fills what live would queue or miss).

### R1 — Post-FTX grind up (Jan 2023) — trend

Jan 1 close **0.3163** → Jan 31 close **0.3629**. USD month ~+20%. Slow recovery from the 2022 FTX low. Invert stress: a **persistent up-tape** with few deep retraces. Buy rungs may fill once; sell-TP rungs may lag; maxDD may look tiny while **fill count stays thin**. Do not call a quiet month a PASS because maxDD is small.

### R2 — February chop — range

Feb 28 close **0.3570** vs Jan 31 **0.3629**. USD month ~−7%. Invert's "home" tape **and** the fee-grind tape. Many 15m mean-reversion prints can still lose gate 1 after 0.26%×2 + shadow. Coder: count prints, then **shadowed** round-trips, not "it ranged so invert should win."

### R3 — SVB weekend + March melt-up — gap then trend

- **2023-03-10** (SVB Friday): Source A open **0.3684** / high **0.3754** / low **0.3441** / close **0.3501**.
- **2023-03-11–13** (weekend + Monday): closes **0.3481 → 0.3394 → 0.3448**. Thin weekend book; USDC de-peg adjacent (Circle/SVB). Crypto trades 24/7; "weekend gap" here means **thin liquidity + news**, not an FX Saturday close.
- March close **0.4883**. USD month ~+43%. Banking-crisis bounce into month-end.

Invert stress: Friday dump can fill a stack of buy rungs in one session; the March trend can then **leave those buys without opposite prints** until much higher — or stop-run them if Coder flattens (do not flatten to clean). Spot invert **must not naked-short** the melt-up.

### R4 — April give-back / May bounce — range-trend mix

Apr close **0.4341** (USD ~−12%). May close **0.4850** (USD ~+10%). Classic two-way month pair. Stress: April fade after March highs (trend against leftover longs); May bounce that looks like "invert working" on a **tiny n**. Do not promote a May clip.

### R5 — June SEC week — gap / range-break

SEC sued Binance **2023-06-05** and Coinbase **2023-06-06**. Forbes: XRP ~−5% with the complex. Source A:

- **2023-06-05:** open 0.4846 / high 0.5100 / low 0.4815 / close **0.5014**
- **2023-06-06:** open 0.5007 / high 0.5073 / low **0.4541** / close **0.4753** (~10% low-to-high on the 6th)

Month close **0.4333**. USD month ~−8%. Hinman-docs bounce mid-June (CoinDesk 2023-06-13, XRP +7.4% USD) is a **news spike inside a down month** — invert can get **whipsawed both ways** in the same June window. XRP was **not** named in the Binance securities list; the tape still sold with the complex. Do not skip June because "XRP wasn't listed."

### R6 — 13–14 July Torres ruling — **primary gap + trend + fade** (hardest invert test)

U.S. District Judge Analisa Torres, **2023-07-13**: programmatic exchange sales of XRP **not** investment contracts; institutional sales **were**. Reuters: XRP +75% that afternoon. CoinDesk: high ~**$0.93**, ~+96% in a day.

Source A daily (EUR) — **the bar invert cannot pretend is a normal 15m**:

| Date | Open | High | Low | Close | Why invert cares |
| --- | ---: | ---: | ---: | ---: | --- |
| **2023-07-12** | 0.4319 | 0.4328 | 0.4179 | **0.4232** | Last quiet close before the ruling |
| **2023-07-13** | 0.4232 | **0.8308** | 0.4211 | **0.7266** | Open-to-high **~+96%**. Rungs skipped. Paper instant-fill ≠ live queue. |
| **2023-07-14** | 0.7266 | 0.7355 | **0.5966** | **0.6412** | Fade day. Opposite rungs can print in a dump that still leaves you offside vs the 13th high. |
| **2023-07-20** | 0.7086 | **0.7329** | 0.7220 | 0.7329 | Source A *header* annual high (conflicts with 13 Jul 0.8308 — **use Kraken 15m**) |
| **2023-07-31** | 0.6396 | 0.6547 | 0.6224 | **0.6345** | Still elevated vs 12 Jul |

USD July ~+47.5% (open 0.47 → close 0.70, high 0.95 on Kraken XRPUSD monthly). Invert stress, in order:

1. **Gap/spike:** one 15m (or a handful) can traverse **every** fib extension the recipe arms (1.272 / 1.618 / 2.0 / 2.618 both sides). Coder must log **skipped rungs**, not invent a fill at each level the wick tagged.
2. **Trend:** 12 Jul close 0.42 → 31 Jul close 0.63 is still a **one-way** month after the spike.
3. **Paper lie:** engine fills whole size at the quote; live XRPEUR on 13 Jul had exchange outages (Uphold "high demand" that day). Slippage unmodeled.
4. **Do not mark the spike as return > 0.** An open long that is +70% mark-to-market is **not** gate 1 until opposite prints **and** both fees + shadow are subtracted.

Relists (Coinbase and others announcing XRP back) are **liquidity regime change** in the days after 13 Jul — spread/queue change. Paper 0.26% taker does not prove that book.

### R7 — August give-back — trend down

Jul 31 close **0.6345** → Aug 31 close **0.4709**. USD month **~−27%**. Fortune (2023-08-23): XRP had erased almost all of the ruling gains, ~$0.53 vs ~$0.48 pre-ruling.

Invert stress: leftover **longs from the July spike** vs a month-long fade. This is how invert **maxDD** is likely to print if July filled buys and August never paid the swapped sells. Do not flatten August to hide DD. Do not mix sleeve shorts into this spot book.

### R8 — September dead range — fee grind

Sep 30 close **0.4871** vs Aug 31 **0.4709**. USD month **~+0.8%**. Tightest monthly USD print of the year. Invert can **overtrade**: many 15m touches, ≥8 fills looking "easy," return after fees **still ≤ 0**. Gate 2 without gate 1 is still FAIL. Isolation checklist must not celebrate fill count alone.

### R9 — October grind up — trend

Oct 31 close **0.5673**. USD month ~+16.5%. Broader-crypto bid (BTC ETF-anticipation tape). Invert stress: similar to January — **slow trend**, fewer opposite prints. Thin fill count is not a data bug.

### R10 — 13–14 November spike/fade — gap inside a flat month

USD November ~**+1%** close-to-close **hides** a wick: Kraken XRPUSD monthly high **0.7499**. Source A:

- **2023-11-13:** open 0.6196 / high **0.7004** / low 0.6006 / close **0.6275**
- **2023-11-14:** open 0.6275 / high 0.6282 / low **0.5505** / close **0.5792**

Invert stress: **same shape as July, smaller**. A 15m invert that armed into 13 Nov can fill extensions on the high then get **faded through the 14 Nov low**. Month-end close **0.5567** looks like a range. **Do not skip this week because November % is ~1.**

### R11 — December year-end range — quiet close

Dec 31 close **0.5591**. USD month ~+1.4%, high 0.70 USD. Year-end tape. Invert stress: holiday thin books (24–26 Dec, 31 Dec). Holes and wide 15m spreads. Continuous book: **do not flatten 31 Dec** so 2024 starts at 10k.

---

## How each class attacks invert (Coder, not a prediction)

| Class | 2023 homes | Attack on invert | What Coder logs (after replay — do not invent now) |
| --- | --- | --- | --- |
| **Trend** | Jan, Mar, Jul (after 13th), Aug, Oct | One side prints; opposite sits; maxDD from leftover inventory | Side of net inventory at month-end; whether sell-TP ever printed |
| **Range** | Feb, May mix, Sep, Dec | Fee grind; ≥8 fills can still fail gate 1 | Shadowed round-trip vs raw fill count |
| **Gap / spike** | 10 Mar, 5–6 Jun, **13–14 Jul**, 13–14 Nov | 15m skips rungs; wick ≠ fill; paper instant-fill | Skipped rungs; first 15m that opened **through** a level vs printed |
| **Thin book** | SVB weekend, 13 Jul relist chaos, late Dec | Spread + queue unmodeled | Venue volume holes; do not interpolate |

**Naked short:** after a sell-TP, spot invert is **flat cash**. Next entry is buy-back. July and November fades do **not** authorize a short on `invert-paper`. Sleeve 3x is a different book and stays FAIL/closed.

---

## Coder checklist — fill **after** the 2023 replay finishes

Replay is **paper**, workspace **`invert-paper`**, pair **XRPEUR**, TF **15m**, invert recipe as locked (full fib; swap the two prices after any fill; re-arm only on the opposite fill; no naked short). Fee column: engine **0.26%** + **shadow extra** + round-trip. Timezone: **Europe/Brussels**.

**Do not fill this table from daily FX, from USD heatmaps, from the 8-day lab clip, or from 2026 `PAPER-00029`.** Empty until the engine prints.

### A — Window hygiene

- [ ] First 15m bar used: timestamp **Europe/Brussels** (and UTC) · venue Kraken XRPEUR
- [ ] Last 15m bar used: timestamp **Europe/Brussels** (and UTC)
- [ ] Bar count vs 35 040 · holes listed (date, length). No interpolated fills
- [ ] DST crossings 2023-03-26 and 2023-10-29: no duplicated/missing hour in the series
- [ ] Continuous book: start equity **EUR 10000** at 2023-01-01 00:00 Brussels · **no** year-end flatten
- [ ] Recipe hash **cited, not resealed**. `c9689f5d` is the 2026 lab clip — **not** this slice's lock to rotate

### B — Fills (prints only)

- [ ] **Fill count** ( `PAPER-*` prints on `invert-paper` inside the window )
- [ ] Resting limits at window end: **not** counted
- [ ] **First fill:** id · side · price · fee · shadow · timestamp Europe/Brussels
- [ ] **Last fill:** id · side · price · fee · shadow · timestamp Europe/Brussels
- [ ] Skipped-rung log on **2023-07-13**, **2023-07-14**, **2023-11-13**, **2023-11-14**, **2023-06-06**, **2023-03-10** (venue 15m, not Source A)

### C — Return after fees (shadow)

- [ ] Realized round-trips after engine 0.26% **and** shadow extra
- [ ] Open inventory marked **separately** (mark-to-market is **not** gate 1)
- [ ] **Return after fees (shadowed), this window, continuous book:** _______ %  *(blank until replay)*
- [ ] Buy-and-hold +77% (0.3163→0.5591) **not** copied here

### D — maxDD

- [ ] Peak equity timestamp (Brussels) and value
- [ ] Trough equity timestamp (Brussels) and value
- [ ] **maxDD from peak, this window:** _______ %  *(blank until replay)*
- [ ] Likely stress months to *inspect* (not a prediction): **July spike, August fade, November 13–14**. Inspect ≠ invent.

### E — Isolation gate (diagnostic only — **does not fund**)

Score the **2023 window in isolation** on the three conjuncts. This is a lab read of one year of the continuous book. **It is not a fund memo. It is not paper-to-live. It is not a reason to go live, reseal, or reset `dca-paper`.**

| Conjunct | Isolated 2023 (after replay) | Fund? |
| --- | --- | --- |
| Return > 0 after fees (shadow) | YES / NO / UNKNOWN — *not filled* | **No. Isolation does not fund.** |
| Fills ≥ 8 (prints) | YES / NO / UNKNOWN — *not filled* | **No.** |
| maxDD ≤ 8% | YES / NO / UNKNOWN — *not filled* | **No.** |
| **All three** | PASS / FAIL / NOT RUN | **Does not fund either way.** |

Today: **NOT RUN.**

If isolated 2023 is PASS: still paper. Still autonomy 2. Still wait for the **full continuous** walk-forward **and** CEO yes **and** a healthy connector. The 8-day clip already PASSed and still does not fund.

If isolated 2023 is FAIL: record it. Do not reseal. Do not add pairs to rush 8. Do not mix sleeve. Do not skip July.

### F — Locks that survive a pretty 2023

- [ ] Still paper. No keys in git. No Phantom spend from `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3` or Base `0x9eb954b567ef3616424a6e1bf42c63724930aa54`
- [ ] No extra pairs / extra clips to chase 8 fills in a quiet September
- [ ] No USD conversion of XRPUSD as if it were XRPEUR
- [ ] No naked short on the August or 14 Nov fade
- [ ] Journal stamp VOORBEELD. Not FACTUUR
- [ ] `dca-paper` untouched. Sleeve PnL not mixed

---

## Adversarial (stop, not a note)

1. **Invent a 2023 score from this markdown.** Daily EUR and USD monthly % are not invert fills.
2. **Use +77% spot as gate 1.** Buy-and-hold is a different strategy.
3. **Treat isolated 2023 PASS as funding.** It does not fund.
4. **Reset the book at 2024-01-01 to EUR 10000.** Continuous book inherits equity.
5. **Reseal `c9689f5d`** or stamp a new hash because 2023 "needs its own lock."
6. **Skip 13 July** as an outlier so maxDD looks ≤ 8%. The point of this slice is that day.
7. **Count wick tags as fills.** 13 Jul high 0.8308 (Source A) is not 20 fib prints.
8. **Go live, or treat 10k as a SEPA instruction.**
9. **Backfill from 2026 `PAPER-00029` / Surge journal.** Wrong decade.
10. **Interpolate Kraken holes** so bar count equals 35 040.

---

## This sitting (research only)

| Probe | Result |
| --- | --- |
| Kraken MCP | **error** — tools undiscoverable. No orders attempted. |
| `kraken` CLI | not on this VM |
| Public ticker XRPEUR (2026-08-27) | last **1.24595** — **not** 2023 data |
| 2023 15m venue dump | **not available** from public OHLC (short recent window only) |
| Replay | **NOT RUN** |
| Score | **not invented** |

---

## Sources (retrieval 2026-08-27)

- Pound Sterling Live, XRP/EUR 2023 daily OHLC: https://www.poundsterlinglive.com/crypto-currency/ripple-to-euro-history-2023
- Traders Union, XRP/EUR annual row (high/low conflict): https://tradersunion.com/currencies/price-history/xrp-eur/
- ChartsCheck, Kraken XRPUSD monthly heatmap: https://www.chartscheck.com/monthly-returns-heatmap/kraken/XRP/USD
- Reuters, Torres ruling 2023-07-13: https://www.reuters.com/legal/us-judge-says-sec-lawsuit-vs-ripple-labs-can-proceed-trial-some-claims-2023-07-13/
- CoinDesk, XRP spike 2023-07-13: https://www.coindesk.com/markets/2023/07/13/ripples-xrp-token-surges-28-after-court-rules-xrp-sales-arent-investment-contracts
- CNBC, same day: https://www.cnbc.com/2023/07/13/xrp-surges-after-judge-delivers-a-huge-win-to-ripple-in-its-case-against-the-sec.html
- Fortune, gains erased 2023-08-23: https://fortune.com/crypto/2023/08/23/xrp-pricing-gains-erased-ripple-ruling-sec/
- Forbes, SEC vs Binance tape 2023-06-06: https://www.forbes.com/sites/roberthart/2023/06/06/crypto-prices-plunge-as-sector-grapples-with-fallout-from-secs-binance-lawsuit/
- CoinGecko research, named-token drawdowns 5–12 Jun 2023: https://www.coingecko.com/research/publications/sec-cryptocurrency-lawsuit
- CoinDesk, Hinman docs 2023-06-13: https://www.coindesk.com/markets/2023/06/13/xrp-prices-jump-as-hinman-speech-released-in-ripple-labs-filing
- Desk locks: Coder `01-adv-research.md` (#132), `02-adv-plan.md` (#144), `CODER.md` (#118), CEO invert gate (#113)

---

## Re-check (copy/paste — public only)

```bash
# Do not order. Public now-tape is not 2023.
curl -sS 'https://api.kraken.com/0/public/Ticker?pair=XRPEUR'
# Venue 15m for *this* decade only (will not return 2023):
curl -sS 'https://api.kraken.com/0/public/OHLC?pair=XRPEUR&interval=15' | head -c 200
```

When Coder has a 2023 XRPEUR 15m series **offline / archived** (not this git tree): replay paper on `invert-paper`, then fill section **B–E**. Still paper. Isolation does not fund.

---

End. RESEARCHER. Docs only. No orders. No keys. No invented score. Continuous book, 2023 window only. Still paper.
