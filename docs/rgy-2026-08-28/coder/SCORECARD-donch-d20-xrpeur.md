# SCORECARD donch-d20-xrpeur

37 / 5.759519 / 3.162919 / PASS / 2023-01-01→2026-08-27 / Kraken

| field | value |
|---|---|
| verdict (0.26%) | **PASS** |
| fills | 37 |
| return_after_fees_pct | 5.759519 |
| maxDD_pct | 3.162919 |
| tape | 2023-01-01 → 2026-08-27 |
| bars (window) | 1335 |
| warmup | 2022-12-01 (31 bars before window) |
| coverage | 2023+ |
| venue | Kraken |
| pair | XRPEUR |
| clock | 1d Donchian 20-day high IN / 10-day low OUT |
| window | 2023-01-01 → 2026-08-27 (last complete UTC day) |
| capital | 10000.0 EUR, clip 200.0 EUR, one long, rest cash |
| decide / fill | close / next open |
| invert / fib / 15m / re-arm | no / no / no / no |
| parameter search | no (20/10) |
| unlock | CEO UNLOCK 2026-08-28 22:05 Europe/Brussels |
| still paper | yes — not the fund gate |

## Gate (named column 0.26% taker)

| test | value | pass |
|---|---|---|
| return > 0 after fees | 5.759519 | True |
| fills >= 8 | 37 | True |
| maxDD <= 8% | 3.162919 | True |

Shadows do not change the named verdict.

## Fee columns (same fills, different tax)

| fee | fills | return_after_fees_pct | maxDD_pct | final_equity_eur | still_long |
|---|---|---|---|---|---|
| 0.26% | 37 | 5.759519 | 3.162919 | 10575.95188 | True |
| 0.40% | 37 | 5.647984 | 3.211311 | 10564.798388 | True |
| 0.80% | 37 | 5.329313 | 3.349857 | 10532.931269 | True |

## Fills (0.26% book; prices shared)

| day (UTC) | side | price | units | notional_eur |
|---|---|---|---|---|
| 2023-01-14 | buy | 0.35573 | 562.22415877 | 200.0 |
| 2023-02-10 | sell | 0.35563 | 562.22415877 | 199.943778 |
| 2023-03-22 | buy | 0.43656 | 458.1271761 | 200.0 |
| 2023-04-20 | sell | 0.44903 | 458.1271761 | 205.712846 |
| 2023-05-29 | buy | 0.44951 | 444.9289226 | 200.0 |
| 2023-06-29 | sell | 0.42587 | 444.9289226 | 189.48188 |
| 2023-07-14 | buy | 0.72679 | 275.18265249 | 200.0 |
| 2023-08-04 | sell | 0.60465 | 275.18265249 | 166.389191 |
| 2023-09-21 | buy | 0.48912 | 408.89761204 | 200.0 |
| 2023-10-10 | sell | 0.47555 | 408.89761204 | 194.451259 |
| 2023-10-25 | buy | 0.52668 | 379.73722184 | 200.0 |
| 2023-11-22 | sell | 0.53 | 379.73722184 | 201.260728 |
| 2023-12-09 | buy | 0.62526 | 319.86693535 | 200.0 |
| 2024-01-04 | sell | 0.53347 | 319.86693535 | 170.639414 |
| 2024-02-15 | buy | 0.50162 | 398.70818548 | 200.0 |
| 2024-04-03 | sell | 0.54493 | 398.70818548 | 217.268052 |
| 2024-07-14 | buy | 0.48197 | 414.96358695 | 200.0 |
| 2024-08-03 | sell | 0.51297 | 414.96358695 | 212.863871 |
| 2024-09-29 | buy | 0.55042 | 363.35888958 | 200.0 |
| 2024-10-03 | sell | 0.48713 | 363.35888958 | 177.003016 |
| 2024-11-11 | buy | 0.54805 | 364.9302071 | 200.0 |
| 2025-02-03 | sell | 2.5205 | 364.9302071 | 919.806587 |
| 2025-03-03 | buy | 2.82294 | 70.84812288 | 200.0 |
| 2025-03-11 | sell | 1.86437 | 70.84812288 | 132.087115 |
| 2025-05-10 | buy | 2.082 | 96.06147935 | 200.0 |
| 2025-05-24 | sell | 2.02224 | 96.06147935 | 194.259366 |
| 2025-07-10 | buy | 2.04942 | 97.58858604 | 200.0 |
| 2025-08-03 | sell | 2.39203 | 97.58858604 | 233.434825 |
| 2026-01-05 | buy | 1.78616 | 111.97205178 | 200.0 |
| 2026-01-19 | sell | 1.71307 | 111.97205178 | 191.815963 |
| 2026-03-16 | buy | 1.26729 | 157.81707423 | 200.0 |
| 2026-03-27 | sell | 1.17964 | 157.81707423 | 186.167333 |
| 2026-04-17 | buy | 1.2345 | 162.00891049 | 200.0 |
| 2026-04-29 | sell | 1.17758 | 162.00891049 | 190.778453 |
| 2026-05-11 | buy | 1.25363 | 159.53670541 | 200.0 |
| 2026-05-23 | sell | 1.14968 | 159.53670541 | 183.416159 |
| 2026-08-21 | buy | 1.08547 | 184.25198301 | 200.0 |

## Last complete day sanity

| field | value |
|---|---|
| day | 2026-08-27 |
| close | 1.24767 |
| Donch20 (prior 20 highs) | 1.45274 |
| Donch10 (prior 10 lows) | 0.85315 |
| enter? close > Donch20 | False |
| note | live book: no enter on 2026-08-27 close 1.24767 vs Donch20 1.45274 |

## Data

| field | value |
|---|---|
| intended | official Kraken OHLCVT PAIR 1440 XRPEUR/XXRPZEUR + REST 1440 tail |
| used | kraken_trades_agg_1d + rest_ohlc_1440_tail |
| ohlcvt_status | FAIL Drive quota (anonymous download of official zips blocked) |
| coverage_label | 2023+ |
| support article | https://support.kraken.com/articles/360047124832-downloadable-historical-ohlcvt-open-high-low-close-volume-trades-data |
| complete zip (quota-blocked here) | https://drive.google.com/file/d/1ptNqWYidLkhb2VAKuLCxmp2OXEfGO-AP/view |
| quarterly folder | https://drive.google.com/drive/folders/15RSlNuW_h0kVM8or8McOGOMfHeBFvFGI |
| rest ohlc | https://api.kraken.com/0/public/OHLC?pair=XRPEUR&interval=1440 |

URLs actually downloaded:

- `https://api.kraken.com/0/public/OHLC?pair=XRPEUR&interval=1440`
- `https://api.kraken.com/0/public/Trades?pair=XRPEUR&since=1669852800000000000&count=1000`
- `https://drive.usercontent.google.com/download?id=17ghRNMQGK0Is7_by784qGzP1eCUokI2V&export=download&confirm=t`

OHLCVT zip download failed (Google Drive quota exceeded on the official complete file https://drive.google.com/file/d/1ptNqWYidLkhb2VAKuLCxmp2OXEfGO-AP/view and quarterly folder https://drive.google.com/drive/folders/15RSlNuW_h0kVM8or8McOGOMfHeBFvFGI linked from https://support.kraken.com/articles/360047124832-downloadable-historical-ohlcvt-open-high-low-close-volume-trades-data). Tape is Kraken-native anyway: public Trades REST aggregated to UTC 1d from 2022-12-01 through the day before REST OHLC 1440 begins (2024-09-07), then REST OHLC 1440 through 2026-08-27. Not Binance. No invented OHLC: daily bars are first/max/min/last Kraken prints. Overlap vs REST 1440 on the splice day is recorded below. coverage=2023+.

Overlap (2024-09-07 trades-agg vs REST 1440): match=True O/H/L/C trades=[0.47059, 0.48159, 0.46952, 0.47426] rest=[0.47059, 0.48159, 0.46952, 0.47426]


## Locks

Do not touch invert-paper, dca-paper, adaeur-widefib-paper. Do not reseal c9689f5d.
Still paper. No keys. No live. This book is NOT the fund gate.
