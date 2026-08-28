# RESEARCH — Blueprint ladder vs clip-200 Donchian (XRPEUR, still paper)

**Seat:** RESEARCHER · Coder  
**Lens:** simple first (resize Donchian 20/10), then broaden to the operator’s **level-to-level** ladder. Docs + public REST this sitting.  
**Date:** 2026-08-28  
**Stamp:** VOORBEELD · paper / simulated · not FACTUUR · not INVOICE · not live-trade advice  
**HEAD (leftover `main` at write):** `2170952`  
**Still paper.** No orders. No keys. **No CODE.** No live. No Phantom spend.  
**`is_fund_gate`:** **false**

This file answers: which **paper** recipe on **XRPEUR 2023+** can (a) survive **0.26%** fees, (b) keep **maxDD ≤ 8%** on a 10k book **or name why that DD cap is the thing killing income**, and (c) print an **annualized** return that beats **~2% inflation by a real margin**, not **1.6%/yr**.

It does **not** restamp invert. It does **not** reset `donch-d20-xrpeur-paper`, `invert-paper`, or `dca-paper`. It does **not** reseal `c9689f5d`.

---

## Operator locks (this sitting — do not bargain)

| Lock | Status |
|---|---|
| Still paper / no keys / no orders / **no CODE** / no live | **held** |
| `is_fund_gate` | **false** — this pack does not fund |
| Do not reset `invert-paper` | **held** — fill **2/8** (`PAPER-00029` + `PAPER-00031`). TPs `00030` @ 1.26778 and `00032` @ 1.24496 still open. Cap 2. No third buy |
| Do not reset `dca-paper` | **held** — five BTCUSD slices @ 78900.6 |
| Do not reset `donch-d20-xrpeur-paper` | **held** — candidate book. Cite the named clip-200 print. **Do not init, flatten, or catch-up** from this PR |
| Do not reseal `c9689f5d` | **held** — 8-day lab clip 20 / +0.681154% / 0.890854% is **not** this score |
| Invert / slower invert / maker-invert / CODE from [#207](https://github.com/eyeskull2220/solana-invoice/pull/207) | **STOP** |
| **USD labels, XRPEUR book** | Score on **Kraken XRPEUR**. Map USD rungs via **Kraken `ZEURZUSD`**. **Do not** invent a USD venue book. Do not splice Binance/Bitstamp |
| **Every marked price is actionable** | **held** — do **not** skip rungs. Do **not** only trade “majors.” Each marked price is an **entry or an exit**. NAMED score uses **all 18** |
| **NAMED blueprint window** | **2023-01-01 → last complete UTC day on XRPEUR.** They **knew** the blueprint in **2023**. Scoring that window on these rungs is the **named** print, **not** lookahead |
| **Sept/Oct 2025 charts** | A **redraw** of the same ladder. **Not** the birth of the map. **Not** the named start date |
| **2025-10-01 → last complete UTC day** | **Robustness slice.** Keep it. **Do not** make it the only print. **Do not** replace the 2023+ named score with it |
| Resized Donchian 20/10 | **2023+ is legal** — Donchian has **no drawn map**. Named Donchian remains 2023+ (journal OHLCVT 1d / weekly REST this sitting) |
| Next-bar | Signal on a **closed** bar from **prior** information. Fill at the **next** bar **open**. Same-bar fill is lookahead |

Journal this sitting (cite, do not ping / flatten / reset): https://dca-paper-journal.surge.sh/ — invert-paper **2/8 NOT MET**. `donch-d20-xrpeur-paper` named WF **37 fills / +5.76% / maxDD 3.16%** on OHLCVT 1d 2023-01-01 → 2026-08-27, clip EUR 200, ending **10575.95**. Live that book: **CASH / 0 resters**. **Not the fund gate.**

**Operator correction (this sitting):** they **knew the blueprint in 2023**. The Sept/Oct 2025 charts are a **redraw**, not the first time the rungs existed. **NAMED score = 2023-01-01 → last complete UTC day on XRPEUR, every marked rung actionable.** Keep **2025-10-01 → last complete day** as a **robustness slice**, not the only print. Still paper. **No CODE.**

---

## The job clip-200 already failed

Operator correction (plain language): **37 fills / +5.76% over 2023-01-01 → 2026-08-27 on clip EUR 200 is not income.**

| | Number |
|---|---:|
| Named print (journal, Kraken OHLCVT XRPEUR **1d**, clip 200, 0.26%) | **37 fills · +5.76% · maxDD 3.16%** |
| Calendar | 2023-01-01 → 2026-08-27 = **1334 days · 3.652 years** |
| Annualized | **(1.0576)^(365.25/1334) − 1 = 1.545%/yr ≈ 1.55%/yr** |
| vs operator ~2% inflation | **FAIL** (short ~0.45 pp, and **not** a real margin) |
| vs Belgian HICP Jul 2026 **3.6%** ([Trading Economics / Eurostat](https://tradingeconomics.com/belgium/harmonised-inflation-rate-yoy)) | **FAIL harder** |
| Fees at 0.26% | `37 × 200 × 0.0026 = 19.24 EUR` (**0.192% of 10k**) — **fees are not the death** |
| Agent cost on 10k | **+576 EUR / 3.652 y ≈ 158 EUR/year**. Cursor Pro-class **~€220/year** is **not** covered. A cloud-agent swarm at **~€1000/year** is not covered. |

**Clip-200 Donchian PASS is the wrong job.** It was built to clear **return > 0 ∧ fills ≥ 8 ∧ maxDD ≤ 8%**. It does that by **not deploying the book**. 2% of 10k in the market cannot print Belgian income even when the **percent** on the clip is fine.

This sitting does **not** restamp the 37-fill OHLCVT cell. Official OHLCVT ZIP was **Drive quota / virus-scan blocked** (see tape). Weekly REST **rhymes**: 16 fills / **+5.498% / 2.771% DD / 1.48%/yr**. Same movie, coarser clock.

---

## Tape (this sitting)

Kraken public REST, **no key**. `GET /0/public/Time` → `unixtime` **1787948780** (`Fri, 28 Aug 26 20:26:20 +0000`). `SystemStatus` → `online`. Last XRPEUR **1.19120**. Last `ZEURZUSD` **1.15835**. Check: XRPUSD **1.37910 / 1.15835 ≈ 1.1906** ≈ XRPEUR. **FX is Kraken. The trading book is XRPEUR.**

| Series | Interval | Fetched | Scored (forming bar dropped) | First scored | Last scored |
|---|---|---:|---:|---|---|
| XRPEUR weekly | 10080 | 485 | **190 weeks in 2023+** (484 closed total) | 2023-01-05 | **2026-08-20** (week of 2026-08-27 still forming) |
| XRPEUR daily | 1440 | 721 | **720 days** | **2024-09-07** | **2026-08-27** |
| EURUSD weekly | 10080 | 338 | 2020-03-12 → 2026-08-20 | — | median **1.09509** on 2023+ |
| EURUSD daily | 1440 | 721 | REST-720 | 2024-09-07 | 2026-08-27 |

**OHLCVT:** support article [360047124832](https://support.kraken.com/articles/360047124832-downloadable-historical-ohlcvt-open-high-low-close-volume-trades-data) Drive IDs scraped this sitting (`1ptNqWYidLkhb2VAKuLCxmp2OXEfGO-AP` complete; quarterly folder `15RSlNuW_h0kVM8or8McOGOMfHeBFvFGI`). **GET returned “Too many users have viewed or downloaded this file recently.”** Not unzipped. **Named Donchian 2023+ daily native stays the journal’s 37-fill cell.** This file’s **own 2023+ numbers are Kraken REST weekly** (full 2023+) plus **REST-720 daily** (from 2024-09-07). That cap is [documented](https://docs.kraken.com/api-reference/market-data/get-ohlc-data).

**Last complete UTC day** for daily REST: **2026-08-27**. Weekly last **committed** bar: **2026-08-20**.

Engine (same lie-detector as [#222](https://github.com/eyeskull2220/solana-invoice/pull/222) / Freqtrade):

```text
signal on closed bar t (prior bars only)
fill at bar t+1 OPEN
paper fee 0.26% taker per fill
book EUR 10 000 · one long · rest cash
same-bar both-sides / multi-rung span on weekly = SKIP (unknown path)
```

---

## USD rungs (operator; every one is live)

USD labels as marked. EUR column = USD / **median Kraken EURUSD 1.09509** (illustration only). The engine maps **bar-by-bar** with contemporaneous `ZEURZUSD` so a horizontal **USD** line is scored on XRPEUR without opening an XRPUSD book.

| # | USD (actionable) | EUR @ 1.09509 (illustration) |
|---:|---:|---:|
| 1 | 2.08746 | 1.906 |
| 2 | 1.77853 | 1.624 |
| 3 | 1.54756 | 1.413 |
| 4 | 1.50000 | 1.370 |
| 5 | 1.46459 | 1.337 |
| 6 | 1.36057 | 1.242 |
| 7 | 1.27520 | 1.164 |
| 8 | 1.14021 | 1.041 |
| 9 | 1.04798 | 0.957 |
| 10 | 0.87806 | 0.802 |
| 11 | 0.856 | 0.782 |
| 12 | 0.737 | 0.673 |
| 13 | 0.635 | 0.580 |
| 14 | 0.522 | 0.477 |
| 15 | 0.444 | 0.405 |
| 16 | 0.377 | 0.344 |
| 17 | 0.343 | 0.313 |
| 18 | 0.312 | 0.285 |

**No extra invented rungs.** Adjacent gap is the next **marked** price, not a 1.00→1.70 skip. “Majors only” (`1.77853 / 1.50000 / 1.04798 / 0.87806`) is a **killed comparison** below, not the named recipe.

---

## 1. Simple first — resize Donchian 20/10 (no drawn map, 2023+ legal)

Same published Turtle as the candidate book: **20-bar high in / 10-bar low out**, long-only spot, cash when flat, **next-open** fill. Weekly **4/2** is the Kraken-native **2023+** proxy (≈20d/10d). Daily **20/10** is REST-720 (**not** full 2023).

Fee identity at low n is not the death:

```text
16 fills × 200 EUR × 0.0026 =  8.32 EUR   (weekly this sitting; actual 9.77 with notional)
37 fills × 200 EUR × 0.0026 = 19.24 EUR   (journal OHLCVT)
16 fills × 688 EUR × 0.0026 = 28.62 EUR   (max clip under 8% DD)
```

### Weekly 4/2 · XRPEUR · 2023-01-05 → 2026-08-20 · Kraken REST (this sitting)

| Clip | Fills | Return after 0.26% | Ann. | maxDD | Fees EUR | € / year on 10k | vs 8% DD | vs ~2% infl. | Agent Pro ~€220/yr | Swarm ~€1000/yr |
|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|
| **200** (wrong job) | **16** | **+5.498%** | **+1.48%** | **2.771%** | 9.77 | **150** | PASS | **FAIL** | **NO** | **NO** |
| **1000** | 16 | +27.492% | **+6.87%** | **10.550%** | 48.87 | 752 | **FAIL DD** | YES | YES | **NO** |
| **2000** | 16 | +54.983% | **+12.74%** | **16.254%** | 97.75 | 1504 | **FAIL DD** | YES | YES | YES |
| **Full book** | 16 | **+194.860%** | **+34.43%** | **55.622%** | 726 | 5331 | **FAIL DD** | YES | YES | YES |
| **Max clip ≤ 8% DD** | 16 | **+18.91%** | **+4.85%** | **8.00%** | 33.6 | **517** | **PASS (on the line)** | thin YES | **YES** | **NO** |

**Max clip that still respects 8% DD (weekly, 0.26%, close-MTM): EUR 688.**

That is the whole Donchian story on this tape:

- Clip **200** keeps DD cute and **fails income** (1.48%/yr; journal OHLCVT **1.55%/yr**).
- Clip **1000 / 2000** print **real** annualized numbers and **break 8%**.
- Full book is an **income machine** (**+34%/yr**) with **turtle-on-alts DD (~56%)**.
- The **largest clip that still clears 8%** is **~7% of the 10k book** and only **+4.85%/yr**. That beats **2%** by **~2.8 pp**. It does **not** beat July 2026 Belgian HICP **3.6%** by a fat margin. It covers a **Pro-class** agent bill and **does not** cover a **€1000/yr** swarm.

**The 8% DD cap is the thing killing Donchian income** if the gate keeps all three conjuncts. Return and fills were never the bind on clip-200. **Size** is the bind. Size is what 8% forbids.

### Daily 20/10 · REST-720 · 2024-09-07 → 2026-08-27 (not full 2023)

| Clip | Fills | Return | Ann. | maxDD | Fees | €/yr | 8% DD |
|---|---:|---:|---:|---:|---:|---:|---|
| 200 | 19 | +6.272% | +3.13% | 3.148% | 11.46 | 318 | PASS |
| 1000 | 19 | +31.360% | +14.84% | **11.708%** | 57.31 | 1591 | FAIL |
| 2000 | 19 | +62.719% | +28.02% | 17.735% | 115 | 3182 | FAIL |
| Full book | 19 | +160.427% | +62.51% | **55.754%** | 1241 | 8138 | FAIL |
| **Max clip EUR 595** | 19 | +18.646% | **+9.33%** | **8.00%** | 34 | 973 | PASS |

Shorter REST window **inflates annualized** (2024–26 XRP trend is a bigger **fraction** of the tape). **Do not** treat +9.33%/yr as the 2023+ Donchian income number. The **2023+** Donchian number that matches the journal’s job is **weekly 1.48%/yr at clip 200** / **1.55%/yr OHLCVT**. Max-clip 2023+ is the **688 / 4.85%/yr** row.

Fee shadows (weekly clip 200 — n is small, shadows still return > 0):

| Per fill | Return | maxDD |
|---:|---:|---:|
| 0.26% paper | +5.498% | 2.771% |
| 0.40% Tier 1 maker | +5.446% | 2.786% |
| 0.80% Tier 1 taker | +5.295% | 2.842% |

Weekly **max-clip 688** at 0.40% / 0.80% nudges maxDD to **8.05% / 8.22%** — over the line. The 8% clip is **calibrated to paper 0.26%**. Live Tier 1 shadows need a **slightly smaller** clip or they fail the cap they were sized for.

---

## 2. Broaden — level-to-level blueprint (every rung, no extras)

**Recipe (named):** long **near** a tagged support rung, **exit the next higher marked resistance**. One clip. Next-bar open. **Do not skip.** If a **weekly** bar’s range spans **two or more** EUR-mapped rungs, **skip** (OHLC has no path — same honesty as `DUAL_TOUCH_SKIP`). Target locked in EUR at **signal-time** FX.

This is **not** invert. No pair-swap. No 15m. No fib catalog beyond the **18 marked** prices.

**Why 2023+ is the named window:** they had this ladder in 2023. Scoring XRPEUR from **2023-01-01** is the job, not a hindsight overlay of a 2025 drawing. The Sept/Oct 2025 charts are a **redraw** of the same rungs. **2025-10-01** is scored below as robustness only.

### NAMED — 2023-01-01 → last complete day · weekly REST · **every rung**

| Clip | Fills | Return | Ann. | maxDD | Fees | €/yr | fills≥8 | 8% DD | vs 2% infl. | Pro €220 | Swarm €1000 |
|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|
| 200 | **11** | **+2.762%** | **+0.75%** | 0.747% | 6.41 | 76 | YES | PASS | **FAIL** | NO | NO |
| 1000 | 11 | +13.812% | +3.60% | 3.546% | 32 | 378 | YES | PASS | YES (thin) | YES | NO |
| **2000** | 11 | **+27.624%** | **+6.90%** | **6.670%** | 64 | 756 | YES | **PASS** | **YES, real margin vs 2%** | YES | **NO** |
| **Max clip EUR 2465** | 11 | +34.05% | **+8.35%** | **8.00%** | 79 | 932 | YES | PASS @ 0.26% | YES | YES | **shy** |

**11 path-skips** (weeks that touched ≥2 rungs) and **23** “tagged the top rung, no next.” Weekly **under-counts** adjacent climbs. That is conservative, not a gift.

Named weekly fills (clip 200, for the log — size does not change **when**, only **how much**):

| # | side | next-open EUR | week | USD rung |
|---:|---|---:|---|---:|
| 1 | buy | 0.35132 | 2023-01-19 | 0.377 |
| 2 | sell | 0.38846 | 2023-03-23 | 0.377 |
| 3 | buy | 0.46366 | 2023-04-06 | 0.522 |
| 4 | sell | 0.73205 | 2023-07-20 | 0.522 |
| 5 | buy | 0.64622 | 2023-07-27 | 0.737 |
| 6 | sell | 1.04469 | 2024-11-21 | 0.737 |
| 7 | buy | 1.19962 | 2026-03-12 | 1.36057 |
| 8 | sell | 1.27844 | 2026-03-19 | 1.36057 |
| 9 | buy | 1.22342 | 2026-03-26 | 1.46459 |
| 10 | sell | 1.17460 | 2026-05-21 | 1.46459 |
| 11 | buy | 1.12381 | 2026-05-28 | 1.36057 (still LONG at window end) |

The **2024–25 blow-off** (Donchian weekly bought ~0.57 and sold **2.29**) is **mostly a next-bar gap** on one adjacent rung here (0.737 → next), not a skip to 1.70. After that sell, the engine waited for a **single-rung** touch. **That is the no-skip rule plus weekly path-skip**, not a majors filter.

Fee shadows on **clip 2000** (stays ≤ 8% DD on all three columns):

| Per fill | Return | maxDD | Fees EUR |
|---:|---:|---:|---:|
| 0.26% | +27.624% | **6.670%** | 64 |
| 0.40% | +27.279% | 6.739% | 99 |
| 0.80% | +26.293% | **6.936%** | 197 |

Max-clip **2465** at 0.40%/0.80% goes **8.08% / 8.32%** DD. **Prefer clip 2000** if the 8% line must survive Tier 1 shadows.

**Annualized +6.90%/yr (clip 2000) or +8.35%/yr (clip 2465 @ 0.26%)** is the first recipe on this sitting that is **not 1.6%/yr**, still **≤ 8% DD** (at paper 0.26%), **survives 0.26%** (11 fills, fees tens of EUR, not thousands), and **covers Pro-class agent cost**. It does **not** cover a **€1000/yr** swarm. It does **not** match full-book Donchian **+34%/yr**.

### Robustness — 2025-10-01 → 2026-08-27 (keep this slice; **not** the named print)

Redraw window after the Sept/Oct 2025 charts. **330 days.** Daily REST **can** see it (inside the 720-cap). Weekly too. **Kept** so a later reader can see the redraw slice. **Not** a second named PASS. **Not** a replacement for 2023+.

| Tape | Clip | Fills | Return | Ann. | maxDD | fills≥8 |
|---|---:|---:|---:|---:|---:|---|
| **Daily REST** | 200 | **3** | **−0.170%** | −0.19% | 0.873% | **FAIL** |
| Daily REST | 1000 | 3 | −0.848% | −0.94% | 4.330% | FAIL |
| Daily REST | 2000 | 3 | −1.697% | −1.87% | 8.581% | FAIL |
| Weekly REST | 200 | **5** | +0.198% | +0.22% | 0.548% | **FAIL** |

Daily robustness fills: buy **1.77853** 2025-12-20 @ 1.629 → sell 2026-01-05 @ 1.786 → buy **1.77853** again 2026-01-30 @ 1.509, **still long**. The USD “~1.00 → ~1.70” Aug 2026 blast is **~0.86 → ~1.47 EUR** at ~1.16 FX. A long from **1.51 EUR** targeting the **1.778 USD** rung (~1.74 EUR) **does not get a next-bar sell** on a **1.70 USD** high, and there is **no stop** at 1.05. **Visual ladder ≠ this engine completing the blast as adjacent fills in the redraw window.**

**Do not promote the robustness slice.** Named remains **2023-01-01 → last complete day, every rung.** The redraw **did not** by itself print income, 8 fills, and a blast harvest under these rules. Keep the slice in the file anyway — it is the honest check on the redraw, not the only print.

### Killed — majors only (not the recipe)

Same engine, **only** 1.77853 / 1.50000 / 1.04798 / 0.87806. Weekly 2023+:

| Clip | Fills | Return | Ann. | maxDD |
|---|---:|---:|---:|---:|
| 200 | **5** | +2.156% | +0.59% | 0.898% |
| 1000 | 5 | +10.782% | +2.84% | 4.491% |

Fewer fills (gate tension), **not** a blast ATM. **Not named.** Operator: every level is actionable.

### REST-720 daily blueprint (2024-09-07 → 2026-08-27) — not full 2023

| Clip | Fills | Return | Ann. | maxDD |
|---|---:|---:|---:|---:|
| 200 | 17 | +2.476% | +1.25% | 0.850% |
| 1000 | 17 | +12.379% | +6.10% | 3.829% |

Useful as a **daily** check that adjacent rungs **can** print ≥ 8 fills on a 2-year REST tape. **Not** the named 2023+ cell.

---

## 3. Does it cover agent cost on 10k?

Paper profit is **not** a Cursor invoice. Yardsticks, fiat, not this book:

| | |
|---|---|
| Pro-class subscription | **~€220 / year** (~$20/mo) |
| Heavy cloud-agent swarm | **~€1000 / year** (this desk’s actual swarm is a **multiple**; do not pretend 10k paper pays the whole Ultra bill) |

| Recipe (2023+ unless noted) | € / year | Covers ~€220 | Covers ~€1000 |
|---|---:|---|---|
| Journal Donchian clip **200** (OHLCVT 1d) | **158** | **NO** | **NO** |
| Donchian weekly clip **200** (this sitting) | 150 | **NO** | **NO** |
| Donchian weekly **max clip 688** (8% DD) | **517** | **YES** | **NO** |
| Donchian weekly clip **1000** | 752 | YES | NO — **FAIL 8% DD** |
| Blueprint weekly clip **2000** (every rung) | **756** | **YES** | **NO** |
| Blueprint weekly **max clip 2465** @ 0.26% | **932** | **YES** | **shy** |
| Donchian weekly **full book** | **5331** | YES | **YES** — **FAIL 8% DD (56%)** |

**Clip-200 does not pay agents.** That is the operator correction, numbered.

---

## 4. Why the 8% DD cap is the income kill (Donchian)

On **one** long clip, book DD ≈ **clip-fraction × position MAE**, **plus** giveback of **already-banked** gains (the journal’s 3.16% DD on clip 200 is mostly **giveback of a tiny equity peak**, not “XRP went to zero”).

Scale the clip and **both** return and DD scale. This sitting’s weekly Donchian:

```text
clip  200 → +1.48%/yr · DD  2.77%   FAIL income
clip  688 → +4.85%/yr · DD  8.00%   max legal under the cap
clip 1000 → +6.87%/yr · DD 10.55%  illegal under the cap
full book → +34.4%/yr · DD 55.6%   income exists; gate forbids it
```

**If the desk wants Donchian income, the 8% line has to move, or the book has to be larger than 10k so that a 688-class clip is a smaller percent.** A 50k book with clip 688 is the same **percent** DD and the same **percent** return — euros scale, the **annualized percent** does not. **Percent income vs inflation is a clip-fraction problem, not a 10k-vs-50k trick**, unless you are willing to run **more of the book**.

Blueprint **can** run a **bigger clip under 8%** (2000–2465) because it is **out** more and the adjacent-rung MAE is **not** a 50% XRP dump while 100% invested. That is **why** it prints **~7–8%/yr** without a 56% DD. It also **skips** the 2024–25 moon that full-book Donchian ate.

---

## Verdict

| Probe | Color |
|---|---|
| Journal `donch-d20-xrpeur-paper` clip 200 · 37 / +5.76% / 3.16% | **PASS the old gate · FAIL income** · **1.55%/yr** · **do not reset** |
| Donchian weekly clip 200 (this sitting) | **FAIL income** · 16 / +5.50% / 1.48%/yr / 2.77% DD · rhymes |
| Donchian clip 1000 / 2000 / full book | **RED vs 8% DD** · that is the income, and the cap kills it |
| Donchian **max clip 688** weekly | **YELLOW income** · +4.85%/yr · on the 8% line · covers Pro, not swarm · 0.40/0.80 shadows **nick** 8% |
| Blueprint **every rung** weekly NAMED 2023+ clip **200** | **FAIL income** · 11 / +0.75%/yr |
| Blueprint clip **2000** NAMED 2023+ | **GREEN as a paper income candidate vs 2%** · 11 / **+6.90%/yr** / **6.67% DD** / fees 64 · shadows still ≤ 8% DD · covers Pro, not swarm |
| Blueprint max clip 2465 @ 0.26% | **YELLOW** · +8.35%/yr on the 8% line · shadows go over 8% |
| Robustness 2025-10-01 daily | **RED as a standalone / named print** · 3 fills / negative · **kept** as robustness, not the only print |
| Majors-only | **RED as named** (operator: every rung) · 5 fills |
| 15m invert / 2779 / 2665 / `c9689f5d` reseal | **DEAD / held** · not this page |
| This file as fund gate / live / CODE | **RED** |

**Overall:** the clip-200 Donchian PASS is **not** a Belgian income machine. **Fees are survived** (n is tens). **Inflation is not.** The **8% DD cap is the Donchian income kill**: the max legal clip on 2023+ weekly REST is **EUR 688 → +4.85%/yr**. A **level-to-level blueprint on all 18 marked rungs**, named **2023-01-01 → last complete day** because they **knew the map in 2023**, **clip 2000**, is the first recipe this sitting that **beats ~2% by a real margin** while **staying under 8% DD** and **surviving 0.26%** (and the 0.40/0.80 shadows). **2025-10-01 is a kept robustness FAIL on fills**, not the named window, not a second named PASS. Sept/Oct 2025 is a **redraw**. **OHLCVT was blocked**; weekly is the 2023+ native tape here. **Still paper. Not the fund gate.** `invert-paper` remains **2/8 NOT MET**.

**Promotion: no.** Stay paper. Do not reset `donch-d20-xrpeur-paper`. Do not catch-up the Aug 21 Donchian long. CEO names a **new** hash if clip-2000 blueprint ever becomes a book — **not** a resize of the live Donchian workspace from this PR.

---

## What this file is not claiming

- **Not** that 2023+ on these rungs is lookahead. They **knew** the blueprint in 2023. The named print **is** that window.
- **Not** that Sept/Oct 2025 is when the map was born. Those charts are a **redraw**.
- **Not** that 2025-10-01 is the named score. It is a **kept robustness slice**, and on this engine it **FAIL**s fills.
- **Not** that weekly path-skip is how a human reads the chart. A daily OHLCVT dump would likely **raise n** (more adjacent fills, more fees). That dump **does not exist on this VM this sitting**.
- **Not** that the Aug 2026 USD blast was harvested as 1.05→1.78 in the **redraw** window. Robustness **3 fills, still long from 1.51 EUR**.
- **Not** “beat buy-and-hold.” Full-book Donchian +195% / 56% DD; XRP hold 2023+ was the bigger DD movie ([#222](https://github.com/eyeskull2220/solana-invoice/pull/222) Class E).
- **Not** CODE, orders, keys, a live bot, a new `kraken paper init`, or a resize of `donch-d20-xrpeur-paper`.

---

## Sources (public URLs)

This sitting (Kraken REST, 2026-08-28 ~20:26Z)

- `GET https://api.kraken.com/0/public/Time` → `1787948780`
- `GET https://api.kraken.com/0/public/SystemStatus` → `online`
- `GET https://api.kraken.com/0/public/Ticker?pair=XRPEUR,EURUSD,XRPUSD`
- `GET https://api.kraken.com/0/public/OHLC?pair=XRPEUR&interval=10080|1440`
- `GET https://api.kraken.com/0/public/OHLC?pair=EURUSD&interval=10080|1440`
- Result keys: `XXRPZEUR`, `ZEURZUSD` (XRPUSD ticker only as FX check: `XXRPZUSD`)

OHLCVT (blocked this sitting)

- https://support.kraken.com/articles/360047124832-downloadable-historical-ohlcvt-open-high-low-close-volume-trades-data
- https://docs.kraken.com/api-reference/market-data/get-ohlc-data — 720-cap
- https://docs.kraken.com/exchange/guides/general/historical-data

Fees / inflation / clocks

- https://www.kraken.com/features/fee-schedule
- https://support.kraken.com/articles/cross-platform-fee-tier-changes
- https://tradingeconomics.com/belgium/harmonised-inflation-rate-yoy — BE HICP Jul 2026 **3.6%**
- https://www.ecb.europa.eu/stats/macroeconomic-and-sectoral/hicp/html/index.en.html — ECB **~2%** medium-term
- https://dev.to/nar1frames/i-built-a-crypto-trading-bot-it-lost-to-doing-nothing-355a
- https://www.freqtrade.io/en/stable/backtesting/

Desk (cite, do not reseal / reset / CODE / ping)

- https://dca-paper-journal.surge.sh/ — invert **2/8**; donch clip-200 **37 / +5.76% / 3.16%**; adaeur-widefib FAIL
- https://github.com/eyeskull2220/solana-invoice/pull/222 — clip-200 Donchian as fee-survivor (wrong **income** job)
- https://github.com/eyeskull2220/solana-invoice/pull/225 — adaeur-widefib named FAIL
- https://github.com/eyeskull2220/solana-invoice/pull/210 — OHLCVT / Trades how-to
- https://github.com/eyeskull2220/solana-invoice/pull/211 — 15m vs 26 bps
- https://github.com/eyeskull2220/solana-invoice/pull/207 — invert PLAN (**not CODE**, **not this recipe**)

---

## Out of scope (honoured)

- No paper or live Kraken orders  
- No API keys  
- No reseal of `c9689f5d`  
- No `invert-paper` / `dca-paper` / `donch-d20-xrpeur-paper` reset  
- No flatten of `PAPER-00030` / `PAPER-00032`  
- No invert rewrite, no slower-clock invert, no maker-invert, no CODE from #207  
- No live bot CODE, no `kraken paper init` of a blueprint book in this PR  
- No invented rungs, no majors-only as named, no USD venue book  
- No treating 2025-10-01 as the only / named print  
- No treating 2023+ blueprint as lookahead (they knew the map)  
- No memecoins, no IOTA, no Phantom spend, no FACTUUR, no invented KBO  

**Promotion: no.** Stay paper. Gate on `invert-paper` remains **NOT MET** (fill 2/8). `is_fund_gate: false`.

---

## Re-check (copy/paste — public / git only)

```bash
curl -sS -A 'rgy-research-blueprint-vs-clip200-2026-08-28' 'https://api.kraken.com/0/public/Time'
curl -sS -A 'rgy-research-blueprint-vs-clip200-2026-08-28' 'https://api.kraken.com/0/public/SystemStatus'
curl -sS -A 'rgy-research-blueprint-vs-clip200-2026-08-28' \
  'https://api.kraken.com/0/public/Ticker?pair=XRPEUR,EURUSD,XRPUSD'
curl -sS -A 'rgy-research-blueprint-vs-clip200-2026-08-28' \
  'https://api.kraken.com/0/public/OHLC?pair=XRPEUR&interval=10080' | python3 -c \
  "import json,sys,datetime as dt; d=json.load(sys.stdin); k=next(x for x in d['result'] if x!='last'); r=d['result'][k]; print(k,len(r),dt.datetime.fromtimestamp(r[0][0],dt.UTC).date(),dt.datetime.fromtimestamp(r[-1][0],dt.UTC).date())"
# weekly first bar must be 2017-era; 2023+ n ~190 after dropping the forming week

# OHLCVT may 403/quota — do not relabel REST as OHLCVT
curl -sS -L -A 'rgy-research-blueprint-vs-clip200-2026-08-28' \
  'https://support.kraken.com/articles/360047124832-downloadable-historical-ohlcvt-open-high-low-close-volume-trades-data' \
  | grep -oE 'https://drive.google.com[^\"[:space:]<>]+' | head

rg -n 'is_fund_gate|37 fills|1.55|688|clip 2000|every rung|knew the blueprint|redraw|2025-10-01|robustness|do not CODE|donch-d20' \
  docs/rgy-2026-08-28/coder/RESEARCH-blueprint-vs-clip200.md

curl -sS https://dca-paper-journal.surge.sh/ | rg -n 'donch-d20|37 fills|5.76|invert-paper|PAPER-00031|c9689f5d' || true

# Never:
# kraken paper reset --workspace invert-paper
# kraken paper reset --workspace dca-paper
# kraken paper reset --workspace donch-d20-xrpeur-paper
# kraken order …
```

Count fund-gate fills only from `PAPER-*` **prints** on **`invert-paper`**. 16 / 11 / 37 are **research-book** counts, not a ping.

**Clip-200 Donchian historically survives 0.26% and 8% DD and fails inflation (~1.55%/yr). The 8% cap is the Donchian income kill (max legal weekly clip ~688 → ~4.85%/yr). They knew the blueprint in 2023; Sept/Oct 2025 is a redraw. Named score is 2023-01-01 → last complete day on XRPEUR, every rung actionable, clip 2000 weekly REST (~6.90%/yr, 6.67% DD). Keep 2025-10-01 as robustness only (FAIL fills). Still paper. No CODE.**

End. RESEARCHER. Docs only. `is_fund_gate: false`. VOORBEELD.
