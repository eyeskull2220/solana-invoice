# SCORECARD — Donchian 20/10 sized clips (XRPEUR)

**Seat:** CODER  
**Stamp:** VOORBEELD · paper / simulated · not FACTUUR · not INVOICE · not live  
**Book:** paper score only. `is_fund_gate` = **false**. Do **not** reset `donch-d20-xrpeur-paper`.  
**Named window:** **2023-01-01 → 2026-08-27** (last complete UTC day).  
**Not live. No keys. No invert. No KO/BTC/ETH books.**

Clip **A 200** is **income-FAIL**. Do not defend it as income. Timid-gate can PASS.

## Named score (2023-01-01 → last complete UTC day)

| Path | fills | return | CAGR | maxDD | timid-gate | income |
|---|---:|---:|---:|---:|---|---|
| A clip **200** | 37 | 5.759519% | 1.545033% | 3.162919% | **PASS** | **FAIL** |
| B clip **584.87** (maxDD→8% book) | 37 | 16.842849% | 4.354097% | 7.991311% | **PASS** | **UNVERIFIED (3.5y HICP incomplete)** |
| C clip **800** (ruin=8% book) | 37 | 23.038075% | 5.840742% | 10.158336% | **FAIL** | **UNVERIFIED (3.5y HICP incomplete)** |

**Named clip B = 584.87 EUR.** Scaled so this recipe’s historical maxDD on the named tape is 8% of the 10k book.

## Clip A detail

| Cell | Number |
|---|---:|
| fills | 37 |
| return after fees | 5.759519% |
| CAGR | 1.545033% |
| maxDD | 3.162919% |
| ending equity | 10575.95 EUR |
| fees | 20.71 EUR |
| open_long | True |
| timid-gate | **PASS** |
| income | **FAIL** |

Shadows (same fills clock, parallel fee):

| fee | fills | return | maxDD | gate |
|---|---:|---:|---:|---|
| 0.26% named | 37 | 5.759519% | 3.162919% | PASS |
| 0.0040 shadow | 37 | 5.647984% | 3.211311% | PASS |
| 0.0080 shadow | 37 | 5.329313% | 3.349857% | PASS |

## Clip B / C (same fills clock as A)

| Clip | EUR | equity | fees | timid-gate | income |
|---|---:|---:|---:|---|---|
| B | 584.87 | 11684.28 | 60.57 | **PASS** | **UNVERIFIED** (beats 9.06% floor; 3.5y HICP incomplete) |
| C | 800 | 12303.81 | 82.85 | **FAIL** (DD 10.158336% > 8%) | **UNVERIFIED** (beats 9.06% floor; 3.5y HICP incomplete) |

JSON keeps full Decimal. Still paper. `is_fund_gate: false`.

## REST-720 check (not the named 2023 print)

Must rhyme [PR #227](https://github.com/eyeskull2220/solana-invoice/pull/227): 19 / +6.271917% / 3.148108%.

| Cell | This run | #227 |
|---|---:|---:|
| fills | 19 | 19 |
| return | 6.271917% | 6.271917% |
| maxDD | 3.148108% | 3.148108% |

REST-720 first complete bar **2024-09-07**. It is **not** a 2023-start tape. PASS is one spike clip; skip it → FAIL. **income-FAIL.**

Named clip A **rhymes** 37 / +5.759519% / 3.162919% / equity **10575.95** / fees **20.71**. Still **income-FAIL** vs HICP floor 9.056183%.

## Recipe

- Kraken **XRPEUR**. Close signal, **next open**. Prior 20-high in / 10-low out. Long-only. Cap 1.
- Channel excludes today. `close >` / `close <`.
- Fee 0.26% taker per fill. Shadows 0.40 / 0.80.
- Start 10000 EUR. MTM at complete-day close.
- Warmup bars before 2023-01-01 seed the channel only (no fills).

## Tape

- REST-720 source of record `2024-09-07 → 2026-08-27`.
- Pre-REST head: OHLCVT-format `XRPEUR_1440` copy, overlap **0-diff numeric OHLC** (n=206).
- Official Drive OHLCVT ZIP: **quota exceeded this sitting**.
- No Binance splice. Forming 2026-08-28 dropped.

## Income bar

- Eurostat I15 BE CP00: 2023-01 = 125.66, 2025-12 = 137.04 → floor **9.056183%** (35 months). API updated 2026-02-06T23:00:00+0100.
- 3.5y cumulative through Aug 2026: **UNVERIFIED** (2026 months missing on I15 dump).
- Agent cost: **UNVERIFIED**.
- Clip A must beat that floor to even be discussed as income. It does not.

## Fills (named clip A)

| # | side | signal | fill | px |
|---:|---|---|---|---:|
| 1 | buy | 2023-01-13 | 2023-01-14 | 0.35573 |
| 2 | sell | 2023-02-09 | 2023-02-10 | 0.35563 |
| 3 | buy | 2023-03-21 | 2023-03-22 | 0.43656 |
| 4 | sell | 2023-04-19 | 2023-04-20 | 0.44903 |
| 5 | buy | 2023-05-28 | 2023-05-29 | 0.44951 |
| 6 | sell | 2023-06-28 | 2023-06-29 | 0.42587 |
| 7 | buy | 2023-07-13 | 2023-07-14 | 0.72679 |
| 8 | sell | 2023-08-03 | 2023-08-04 | 0.60465 |
| 9 | buy | 2023-09-20 | 2023-09-21 | 0.48912 |
| 10 | sell | 2023-10-09 | 2023-10-10 | 0.47555 |
| 11 | buy | 2023-10-24 | 2023-10-25 | 0.52668 |
| 12 | sell | 2023-11-21 | 2023-11-22 | 0.53 |
| 13 | buy | 2023-12-08 | 2023-12-09 | 0.62526 |
| 14 | sell | 2024-01-03 | 2024-01-04 | 0.53347 |
| 15 | buy | 2024-02-14 | 2024-02-15 | 0.50162 |
| 16 | sell | 2024-04-02 | 2024-04-03 | 0.54493 |
| 17 | buy | 2024-07-13 | 2024-07-14 | 0.48197 |
| 18 | sell | 2024-08-02 | 2024-08-03 | 0.51297 |
| 19 | buy | 2024-09-28 | 2024-09-29 | 0.55042 |
| 20 | sell | 2024-10-02 | 2024-10-03 | 0.48713 |
| 21 | buy | 2024-11-10 | 2024-11-11 | 0.54805 |
| 22 | sell | 2025-02-02 | 2025-02-03 | 2.52050 |
| 23 | buy | 2025-03-02 | 2025-03-03 | 2.82294 |
| 24 | sell | 2025-03-10 | 2025-03-11 | 1.86437 |
| 25 | buy | 2025-05-09 | 2025-05-10 | 2.08200 |
| 26 | sell | 2025-05-23 | 2025-05-24 | 2.02224 |
| 27 | buy | 2025-07-09 | 2025-07-10 | 2.04942 |
| 28 | sell | 2025-08-02 | 2025-08-03 | 2.39203 |
| 29 | buy | 2026-01-04 | 2026-01-05 | 1.78616 |
| 30 | sell | 2026-01-18 | 2026-01-19 | 1.71307 |
| 31 | buy | 2026-03-15 | 2026-03-16 | 1.26729 |
| 32 | sell | 2026-03-26 | 2026-03-27 | 1.17964 |
| 33 | buy | 2026-04-16 | 2026-04-17 | 1.23450 |
| 34 | sell | 2026-04-28 | 2026-04-29 | 1.17758 |
| 35 | buy | 2026-05-10 | 2026-05-11 | 1.25363 |
| 36 | sell | 2026-05-22 | 2026-05-23 | 1.14968 |
| 37 | buy | 2026-08-20 | 2026-08-21 | 1.08547 |

## Re-run

```bash
python3 docs/rgy-2026-08-28/coder/score_income_paths.py
```

Public GETs only. Still paper. `is_fund_gate: false`.

