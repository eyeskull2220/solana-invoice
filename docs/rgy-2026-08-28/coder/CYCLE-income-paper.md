# CYCLE — paper Donchian-sized + blueprint XRPEUR

**Seat:** CODER  
**Stamp:** VOORBEELD · paper / simulated · not FACTUUR · not INVOICE · not live  
**Date:** 2026-08-28  
**CEO lock:** 22:31 Europe/Brussels — write the paper **CYCLE** first. **No new 3-year dump.** This file is **not** the living score.  
**`is_fund_gate`:** **false**

This PR did **not** open a SCORECARD. If a later seat prints 2023→now fills, that print is **not** this cycle and is **not** the living score until CEO names it.

Still paper. No live. No keys. No invert. Do **not** reset `donch-d20-xrpeur-paper`. Do **not** create KO/BTC/ETH books.

---

## What a cycle is

One **round-trip** on **Kraken XRPEUR**, EUR book **10000**, **next-bar fills**, fee **0.26%** per fill, shadows **0.40 / 0.80** on the same fills. Signal on a **complete UTC day**. Fill at the **next** complete day’s **open**. Same-bar fill is lookahead.

| Path | One cycle | Flat after |
|---|---|---|
| **Donchian 20/10** | IN: close **>** prior-20 **high** → buy next open. OUT: close **<** prior-10 **low** → sell next open. Long-only. Ignore extra IN while long. Ignore OUT while flat. | cash until a **new** 20-high |
| **Blueprint** | IN: complete-day **low** tags a marked **support** (USD rung → EUR that day) → buy next open. OUT: complete-day **high** tags the **next higher** marked rung → sell next open. | cash; next IN is a marked support. **Do not skip** to a “major yellow.” |

Cap **1** long. Rest of the book stays cash. Clip is quote EUR (below). Book is **EUR**, not USD.

---

## Locks (do not bargain)

| Lock | Meaning |
|---|---|
| **Not the living score** | This page has **no** named fills / return / CAGR / maxDD dump. |
| **No 2023→now blob** | Do not ship a 3-year equity curve as the named print in this PR. |
| Named window (**method**, later SCORE) | **2023-01-01 → last complete UTC day** (this sitting: **2026-08-27**). Drop forming 2026-08-28. |
| **DRAWDATE slice** (not named) | **2025-10-01 → last complete UTC day.** Sept/Oct 2025 redraw. Robustness only. Do not print it as the named number. |
| Operator map | Operator knew the blueprint in **2023**. 2025 charts are a **redraw**, not the first knowledge date. |
| Clip-200 Donchian | **income-FAIL.** Timid-gate can PASS. Do not defend as income. |
| `donch-d20-xrpeur-paper` | **Do not reset.** |
| Invert / `invert-paper` / `dca-paper` | Untouched. No invert CODE. |
| Pair | **XRPEUR Kraken only.** No Binance splice. No USD book. |
| Extra levels | **Do not invent.** The 18 USD rungs below are the whole map. |

**Timid-gate** (three conjuncts, after 0.26%): return **> 0** AND fills **≥ 8** AND maxDD **≤ 8%**.  
**Income-bar:** 3.5y after-fee return must **beat Belgian HICP** over the same window (cite below). Agent-cost cover: **UNVERIFIED**.

---

## 1) Donchian 20/10 — same recipe, three clips

Close signal, next open. Channel = **prior** complete days only (today excluded). `close >` / `close <` (not `>=`).

| Clip | EUR | Role |
|---|---:|---|
| **A** | **200** | Size artifact. **income-FAIL.** |
| **B** | **TBD** | Scale **this** recipe until historical maxDD **= 8% of the 10k book**. Name the EUR clip on a later SCORE, not here. |
| **C** | **800** | Ruin-to-zero on one clip = **8% of book**. |

Clip B identity (later SCORE, after a real tape): if maxDD scales with clip on one long,

```text
clip_B_EUR = 200 * (8 / maxDD_pct_at_clip_200)
```

Do **not** stamp a EUR number from REST-720 and call it the 2023 named clip B.

### Clip A — already measured, still income-FAIL

| Source | Window | fills | return | maxDD | timid-gate | income |
|---|---|---:|---:|---:|---|---|
| REST-720 reconstruct [PR #227](https://github.com/eyeskull2220/solana-invoice/pull/227) | 2024-09-07 → 2026-08-27 (**not** 2023-start) | **19** | **+6.271917%** | **3.148108%** | **PASS** | **FAIL** |
| Coder stamp 37 / +5.759519% / 3.5y | claimed 2023-01-01 → 2026-08-27 | 37 | +5.76% | ~3.16% | timid-gate **PASS** (if true) | **FAIL** |
| That 37-fill stamp | — | — | — | — | **KILL as verified** (#227: OHLCVT quota; unverified) | still **FAIL** even if later rhymed |

REST-720 PASS is **one** EUR-200 ride (2024-11-11 → 2025-02-03). Skip that clip → **FAIL** (−0.90%). Not a salary. CAGR is not printed here.

Shadows 0.40 / 0.80 still PASS the **timid** gate on REST-720 because **n is small**. That does not flip income.

---

## 2) Blueprint XRPEUR — every rung live

USD labels (high → low). Convert **USD → EUR per UTC day** via that day’s **XRPEUR/XRPUSD** (preferred, same venue) or **EURUSD**. Score **EUR**. Do not keep a USD book.

```text
2.08746
1.77853
1.54756
1.50000
1.46459
1.36057
1.27520
1.14021
1.04798
0.87806
0.856
0.737
0.635
0.522
0.444
0.377
0.343
0.312
```

**18 rungs. 17 adjacent pairs.** Every pair is a legal cycle: buy the **lower**, sell the **next higher**. Do **not** skip rungs. Do **not** only trade “major yellows.”

Map sanity (USD XRP, not PnL): Aug 2026 **~1.00 → ~1.70** sits on 1.04798 / 1.14021 / 1.54756 / 1.77853. Jun 2026 **1.05–1.14** after May **1.54** cut. Jan 2026 **0.34–0.44** sits on 0.343 / 0.377 / 0.444. If a later SCORE cannot see those tags on Kraken, stop — do not invent levels.

Clip for this path: **same three sizes as Donchian (200 / B / 800)** unless a later SCORE names a different quote. Cap 1. Next-bar. 0.26% + shadows.

---

## Windows (later SCORE — not this PR)

| Label | Start | End | Role |
|---|---|---|---|
| **NAMED** | 2023-01-01 | last complete UTC day | Method lock. **Do not print it in this PR.** Needs official OHLCVT `XRPEUR_1440` + 0-diff REST tail ([PR #210](https://github.com/eyeskull2220/solana-invoice/pull/210)). REST `since=` does not rewind. |
| **DRAWDATE slice** | 2025-10-01 | last complete UTC day | Robustness only. Not named. |
| REST-720 | 2024-09-07 | 2026-08-27 | Donchian clip-A timid-gate only. **Wrong tape** if labelled 2023-start. |

Donchian has **no drawn map** — resized 20/10 stays **2023+** when scored. Blueprint uses the 18 rungs on **both** named and slice; slice is not a different ladder.

---

## Income bar (definition, not a dump)

A later 3.5y after-fee return must **exceed** Belgian **HICP** over the same window.

| Cite | What this sitting actually got | Date |
|---|---|---|
| Eurostat `prc_hicp_midx` BE `CP00` unit **I15** (2015=100) | **2023-01 = 125.66** · **2025-12 = 137.04** → **+9.06%** in 35 months | API `updated` **2026-02-06**; **2026 months missing on this dump** |
| FRED `CP0000BEM086NEST` (2025=100) | Jul 2026 **102.64** | FRED updated **2026-08-19** |
| STATBEL HICP | https://statbel.fgov.be/en/themes/consumer-prices/harmonised-index-consumer-prices-hicp · be.STAT last-13-month cube changed **2026-08-17** | — |
| **3.5y cumulative % Jan 2023 → Aug 2026** | **UNVERIFIED** (I15 dump ends Dec 2025; 2025=100 is another base) | — |
| Agent cost cover | **UNVERIFIED** | — |

Floor already enough to fail clip-200 as income: **+9.06%** HICP by Dec 2025 vs clip-A **+5.76%** (unverified 3.5y) or REST-720 **+6.27%** (~2y, one spike). Beat-HICP on a later named 2023 tape is still required. Do not splice I15 onto 2025=100 and call it STATBEL.

---

## Later SCORE must print (not here)

Two tables, **named window 2023-01-01 → last complete UTC day**, annualized **CAGR**, three fee columns:

| Path | fills | return | CAGR | maxDD | timid-gate | income |
|---|---|---|---|---|---|---|
| Donchian clip A 200 | — | — | — | — | expect PASS / FAIL from tape, **income FAIL** unless HICP is beaten | **FAIL** until proven |
| Donchian clip B (name EUR) | — | — | — | **= 8%** by construction | — | — |
| Donchian clip C 800 | — | — | — | — | — | — |
| Blueprint all-rungs named | — | — | — | — | — | vs HICP |
| Blueprint DRAWDATE slice | slice only | slice only | slice only | slice only | **not named** | **not named** |

No live. No invert. No `donch-d20-xrpeur-paper` reset.

---

## Out of scope (honoured)

- No 2023→now fill dump, no SCORECARD markdown/JSON/py in this PR  
- No paper or live Kraken orders, no API keys, no Phantom spend  
- No invert CODE, no reseal of `c9689f5d`, no `invert-paper` / `dca-paper` reset  
- No KO / BTC / ETH books, no IOTA, no memecoins, no shop HTML  

**Promotion: no.** Stay paper. This cycle is not the fund gate and not the living score.

End. CODER. Docs only. `is_fund_gate: false`. VOORBEELD.
