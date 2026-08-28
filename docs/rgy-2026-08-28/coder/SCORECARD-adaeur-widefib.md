# SCORECARD — `adaeur-widefib-paper`

**Seat:** CODER  
**Stamp:** VOORBEELD · paper / simulated · not FACTUUR · not INVOICE · not live  
**Book:** `adaeur-widefib-paper` (new paper book). `is_fund_gate` = **false** on **this book only** — not `invert-paper`.  
**Fetched:** 2026-08-28T20:08:52Z

## Gate: **FAIL**

All three conjuncts (named 4h tape, after 0.26% taker, no invented fills):

| Conjunct | Value | Need | Hit |
|---|---:|---|---|
| return after fees | **-0.371729%** | > 0 | NO |
| fills | **5** | ≥ 8 | NO |
| max DD (MTM last close) | **0.945972%** | ≤ 8% | YES |
| **result** | | | **FAIL** |

## Named score (4h wick-touch)

| Cell | Number |
|---|---:|
| fills | 5 |
| buy fills | 3 |
| sell fills | 2 |
| n closed pairs | 2 |
| dual-skips (`DUAL_TOUCH_SKIP`) | 0 |
| immediate-cross skips (buy rest) | 0 |
| days armed (`(H−L)/L ≥ 1.04%`) | 121 |
| days skipped (range < 1.04%) | 0 |
| days in window | 121 |
| return after fees % | -0.371729 |
| max DD % | 0.945972 |
| start equity EUR | 10000.00 |
| ending equity EUR (MTM) | 9962.82708526 |
| ending cash EUR | 9813.16156211 |
| ending qty ADA | 857.6329331046 |
| ending state | LONG |
| fees EUR | 2.64108689 |

Named fills (limit price, 4h wick-touch, Kraken ADAEUR):

| # | side | price | bar UTC | pair L / H |
|---:|---|---:|---|---|
| 1 | buy | 0.22192700 | `2026-05-07T16:00:00Z` | 0.22192700 / 0.23243700 |
| 2 | sell | 0.23243700 | `2026-05-08T20:00:00Z` | 0.22192700 / 0.23243700 |
| 3 | buy | 0.22890300 | `2026-05-10T00:00:00Z` | 0.22890300 / 0.23614900 |
| 4 | sell | 0.23614900 | `2026-05-10T12:00:00Z` | 0.22890300 / 0.23614900 |
| 5 | buy | 0.23320000 | `2026-05-12T08:00:00Z` | 0.23320000 / 0.24049900 |

Open clip: LONG from `2026-05-12T08:00:00Z` sell resting at **0.24049900**. Max later 4h high **0.23999900** (never tagged; 650 bars). No invented fill.

## Tape (named)

| | |
|---|---|
| venue | **Kraken ADAEUR** (no Binance splice) |
| pair | `ADAEUR` |
| interval | 240 (4h) |
| fetched rows | 721 |
| scored closed bars | 720 (forming bar dropped) |
| window | `2026-04-30T20:00:00Z` → `2026-08-28T16:00:00Z` UTC |
| daily rails | interval=1440 complete bars `2024-09-07T00:00:00Z` → `2026-08-27T00:00:00Z` |
| OHLC sha256 (4h fetched) | `b1b170f978b953c2b9939e200c8747d37c3c37885145aecf7b52467e8040a8cf` |

## Recipe (what was scored)

- Two prices only: prior **complete UTC day** H and L. No lookahead (today’s 1d bar is invisible).
- Arm only if `(H−L)/L ≥ 1.04%`. Else skip the day.
- If flat: rest **buy at L**. Skip the rest if last/open would immediately cross (`open ≤ L` or `prev_close ≤ L`).
- If long: rest **sell at H only**, volume = inventory. Cap **1** long. No third clip.
- After a fill, only the opposite is working. Newly armed opposite does **not** fill the fill bar.
- Fill = 4h wick-touch at the limit (`low ≤ L` buy, `high ≥ H` sell). Fill price = the limit, not the wick.
- Same 4h bar both-sides: **`DUAL_TOUCH_SKIP`** — no fill either side.
- Fee **0.26% taker per fill**. Clip **EUR 200**. Start **10000 EUR**.
- Max DD: mark-to-market on each scored bar’s **close**.
- **Not** invert. **Not** 14 rungs. **Not** 15m. **Not** `invert-paper`. **Not** `dca-paper`.

## SHADOW — 1d wick-touch (not the named score)

Same recipe, fill clock = Kraken `interval=1440` last ~720 **days**. Do not mix into the named cells.

| Cell | SHADOW |
|---|---:|
| window | `2024-09-07T00:00:00Z` → `2026-08-27T00:00:00Z` |
| scored closed days | 720 |
| fills | 11 |
| n closed pairs | 5 |
| dual-skips | 5 |
| cross-skips | 0 |
| days armed / skipped | 719 / 1 |
| return after fees % | -0.630411 |
| max DD % | 1.888308 |
| ending equity EUR | 9936.95894263 |
| shadow gate (informational) | FAIL |

## Operator box (cite, do not ping)

- `adaeur-widefib-paper` created **2026-08-28 21:59 Europe/Brussels**, EUR 10000, fee 0.26%, allow ADAEUR only.
- Empty: **0 fills, 0 orders**. This VM did **not** run Kraken paper CLI against that box.
- Live resters were **SKIPPED** because last **0.17451** is already below prior-day L **0.178212** (a buy at L would cross). This score uses the same cross-skip rule.
- `invert-paper` and `dca-paper` were **not** touched. No reset. No invert CODE. No IOTA. No memecoins. No live. No API keys.

## Re-run

```bash
python3 docs/rgy-2026-08-28/coder/score_adaeur_widefib.py
```

Public GETs only. Writes this markdown and `scorecard.adaeur-widefib.json`.

**FAIL.** Still paper.
