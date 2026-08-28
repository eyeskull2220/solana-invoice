# SCORECARD — blueprint XRPEUR (all rungs)

**Seat:** CODER  
**Stamp:** VOORBEELD · paper / simulated · not FACTUUR · not INVOICE · not live  
**NAMED window:** **2023-01-01 → last complete UTC day** (2026-08-27).  
**DRAWDATE slice:** 2025-10-01 → 2026-08-27 (Sept/Oct 2025 redraw). **Not named.**  
Operator knew the blueprint in **2023**. 2025 charts are a redraw.  
**Every marked rung is actionable.** Do not skip. Do not only trade major yellows.  
USD labels, score **XRPEUR** (EUR book). No USD book. No KO/BTC/ETH. Still paper.

## NAMED (2023-01-01 → 2026-08-27)

| Path | fills | return | CAGR | maxDD | timid-gate | income |
|---|---:|---:|---:|---:|---|---|
| blueprint all-rungs clip 200 | 31 | 3.181486% | 0.861210% | 1.051533% | **PASS** | **FAIL** |

| Cell | Number |
|---|---:|
| fills | 31 |
| return after fees | 3.181486% |
| CAGR | 0.861210% |
| maxDD | 1.051533% |
| ending equity | 10318.15 EUR |
| fees | 17.08 EUR |
| open_long | True |
| timid-gate | **PASS** |
| income | **FAIL** |

Shadows:

| fee | fills | return | maxDD | gate |
|---|---:|---:|---:|---|
| 0.26% named | 31 | 3.181486% | 1.051533% | PASS |
| 0.0040 shadow | 31 | 3.089508% | 1.051879% | PASS |
| 0.0080 shadow | 31 | 2.826714% | 1.052869% | PASS |

## DRAWDATE slice (not named)

| Path | fills | return | CAGR | maxDD | timid-gate | income |
|---|---:|---:|---:|---:|---|---|
| slice 2025-10-01 → 2026-08-27 | 5 | -0.170919% | -0.189159% | 0.872591% | **FAIL** | **FAIL** |

Do **not** ship the DRAWDATE row as the named number.

## Recipe

- 18 USD rungs (no extras). Convert USD→EUR **per UTC day**: `XRPEUR/XRPUSD` when both Kraken daily closes exist, else `1 / ECB USD per EUR` (business-day FF).
- Flat: buy **nearest** support (highest rung ≤ prior close that still has a next higher rung) if that day’s **low** tags it.
- Long: sell **next higher** rung if that day’s **high** tags it. Do not skip rungs.
- Fill = **next complete day’s open**. Cap 1. Clip EUR 200. Fee 0.26% + shadows 0.40/0.80.
- Book is EUR 10000. Not a USD book.

## Rungs (USD)

```
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

## Map sanity (Kraken XRPUSD REST, not PnL)

- **Aug 2026 ~1.00→~1.70:** XRPUSD low 0.98471 high 1.70000 (n=27 2026-08-01→2026-08-27). High 1.7 tags 1.77853/1.54756/1.14021/1.04798. MATCH on ~1.00→~1.70.
- **Jun 2026 1.05–1.14 after May 1.54 cut:** May low 1.26584 high 1.54960 (n=31 2026-05-01→2026-05-31); Jun low 1.00798 high 1.33911 (n=30 2026-06-01→2026-06-30). May high ~1.55 tags 1.54756. Jun traded through 1.04798 and 1.14021 (range wider than 1.05–1.14).
- **Jan 2026 0.34–0.44:** XRPUSD low 1.50041 high 2.41622 (n=31 2026-01-01→2026-01-31). **Not 0.34–0.44** on this tape (price ~1.50–2.42). Rungs 1.50000/1.54756/1.77853 were in play. 0.34–0.44 rungs sit on the map for earlier/lower prints (e.g. 2023) — do not invent a 2026 visit.
- **Jan 2023 (not requested as named 2026):** see XRPEUR named tape (USD REST starts 2024-09-07)

## Tape

- Same XRPEUR stitch as Donchian: REST from 2024-09-07, OHLCVT-copy head, overlap 0-diff numeric OHLC.
- Drive OHLCVT ZIP quota-blocked. No Binance. No invented levels.

## Income bar

- Eurostat I15 floor **9.056183%** (2023-01 → 2025-12). 3.5y through Aug 2026 **UNVERIFIED**. Agent cost **UNVERIFIED**.

## Named fills

| # | side | signal | fill | px | rung |
|---:|---|---|---|---:|---|
| 1 | buy | 2023-01-02 | 2023-01-03 | 0.3257 | support_usd=0.312 |
| 2 | sell | 2023-01-03 | 2023-01-04 | 0.32549 | resist_usd=0.343 |
| 3 | buy | 2023-01-04 | 2023-01-05 | 0.32751 | support_usd=0.343 |
| 4 | sell | 2023-01-11 | 2023-01-12 | 0.34625 | resist_usd=0.377 |
| 5 | buy | 2023-01-14 | 2023-01-15 | 0.36508 | support_usd=0.377 |
| 6 | sell | 2023-03-21 | 2023-03-22 | 0.43656 | resist_usd=0.444 |
| 7 | buy | 2023-03-22 | 2023-03-23 | 0.38846 | support_usd=0.444 |
| 8 | sell | 2023-03-28 | 2023-03-29 | 0.475 | resist_usd=0.522 |
| 9 | buy | 2023-04-01 | 2023-04-02 | 0.47047 | support_usd=0.522 |
| 10 | sell | 2023-07-13 | 2023-07-14 | 0.72679 | resist_usd=0.635 |
| 11 | buy | 2023-07-14 | 2023-07-15 | 0.63993 | support_usd=0.737 |
| 12 | sell | 2024-11-15 | 2024-11-16 | 0.84599 | resist_usd=0.856 |
| 13 | buy | 2024-11-17 | 2024-11-18 | 0.99906 | support_usd=1.04798 |
| 14 | sell | 2024-11-18 | 2024-11-19 | 1.05254 | resist_usd=1.14021 |
| 15 | buy | 2024-11-23 | 2024-11-24 | 1.40317 | support_usd=1.46459 |
| 16 | sell | 2024-11-24 | 2024-11-25 | 1.36656 | resist_usd=1.50000 |
| 17 | buy | 2024-11-25 | 2024-11-26 | 1.35270 | support_usd=1.36057 |
| 18 | sell | 2024-11-27 | 2024-11-28 | 1.39293 | resist_usd=1.46459 |
| 19 | buy | 2024-11-28 | 2024-11-29 | 1.46058 | support_usd=1.46459 |
| 20 | sell | 2024-11-29 | 2024-11-30 | 1.70381 | resist_usd=1.50000 |
| 21 | buy | 2024-11-30 | 2024-12-01 | 1.84499 | support_usd=1.77853 |
| 22 | sell | 2024-12-01 | 2024-12-02 | 2.17003 | resist_usd=2.08746 |
| 23 | buy | 2025-02-03 | 2025-02-04 | 2.61903 | support_usd=1.77853 |
| 24 | sell | 2025-02-04 | 2025-02-05 | 2.43194 | resist_usd=2.08746 |
| 25 | buy | 2025-04-07 | 2025-04-08 | 1.73956 | support_usd=1.77853 |
| 26 | sell | 2025-04-09 | 2025-04-10 | 1.87513 | resist_usd=2.08746 |
| 27 | buy | 2025-10-10 | 2025-10-11 | 2.07149 | support_usd=1.77853 |
| 28 | sell | 2025-10-11 | 2025-10-12 | 2.08100 | resist_usd=2.08746 |
| 29 | buy | 2025-12-19 | 2025-12-20 | 1.62932 | support_usd=1.77853 |
| 30 | sell | 2026-01-04 | 2026-01-05 | 1.78616 | resist_usd=2.08746 |
| 31 | buy | 2026-01-29 | 2026-01-30 | 1.50876 | support_usd=1.77853 |

## Re-run

```bash
python3 docs/rgy-2026-08-28/coder/score_income_paths.py
```

Still paper. Named = 2023-01-01. DRAWDATE is slice only. `is_fund_gate: false`.

