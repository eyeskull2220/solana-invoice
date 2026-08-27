# RESEARCH: 15m XRP/EUR OHLC for paper invert-wf-2023

**Job:** find a usable 15-minute XRP/EUR OHLC path from `2023-01-01 00:00 Europe/Brussels` to now, for paper `invert-wf-2023`.

**Rules followed:** docs + public GETs only. No orders. No keys. No invented candles. Prices from probes are not copied here — only timestamps, counts, and shapes.

**Status:** still paper. Not the fund gate. No score.

**Probed:** 2026-08-27.

---

## Window and pair

| Item | Value |
|---|---|
| Window start | `2023-01-01 00:00:00 Europe/Brussels` (CET, UTC+1) = unix `1672527600` = `2022-12-31 23:00:00 UTC` |
| Window end | probe time 2026-08-27 (Europe/Brussels) |
| Calendar 15m bars if dense | ~1334 days × 96 = ~128,064 bars. Do not treat this as a downloaded row count. |
| Pair (Kraken) | request `XRPEUR`; wire key `XXRPZEUR`; `wsname` `XRP/EUR`; `status` `online` (`GET /0/public/AssetPairs?pair=XRPEUR`) |
| First Kraken XRPEUR trade ever | `since=0` returned trades at `2017-05-18T15:51:07Z` — market exists well before 2023 |

Candle timestamps in the sources below are unix seconds (or ms) in UTC. Align the **window start** to Brussels; do not relabel every bar into local time unless the paper job asks.

---

## Simple first: Kraken public OHLC `interval=15`

**Verdict: UNSATISFIABLE for this window.** Last-720-only. `since` does not walk back to 2023.

### URLs opened

- REST spec: https://docs.kraken.com/api-reference/market-data/get-ohlc-data
- Historical-data guide (misleading on depth): https://docs.kraken.com/exchange/guides/general/historical-data
- Live: `GET https://api.kraken.com/0/public/OHLC?pair=XRPEUR&interval=15`
- Live: `GET https://api.kraken.com/0/public/OHLC?pair=XRPEUR&interval=15&since=1672527600`

### What the spec says

> Returns up to 720 of the most recent entries (**older data cannot be retrieved, regardless of the value of `since`**).

`since` is documented as incremental updates of the **current** 720-wide window, not a historical cursor.

The historical-data guide shows a `since`/`last` loop and says default `since` is “Oldest available.” That loop only pages **forward** from the oldest candle still in the 720-wide cache. It cannot backfill 2023. Live probe matches the REST spec, not the guide’s implication of deep history.

### What the live calls actually returned (2026-08-27)

Both with and without `since=1672527600`:

| Field | Value |
|---|---|
| HTTP | 200, `error: []` |
| Pair key | `XXRPZEUR` |
| Count | **721** (720 committed + current uncommitted bar, as the spec warns) |
| First bar | `1787211900` = `2026-08-20T07:45:00Z` |
| Last bar | `1787859900` = `2026-08-27T19:45:00Z` |
| Span | **7.5 days** = 720 × 15 minutes |
| Shape | `[time, open, high, low, close, vwap, volume, count]` |
| Covers 2023-01-01? | **No** |

Auth: none. Cost: none. Coder can fetch without keys: **yes**, but the payload is last ~7.5 days of 15m XRPEUR only.

**Do not use this endpoint as the invert-wf-2023 history store.**

---

## Ring 1 — Kraken-native: pagination, trades, support CSVs

Prefer this ring if any path is real. Two Kraken-native paths exist. REST OHLC pagination is not one of them.

### 1a. REST OHLC `since` / `last` increment — not a backfill

Already covered. `last` is “ID to be used as since when polling for **new, committed** OHLC data.” Forward-only inside the last 720.

Covers 2023-01-01? **No.** License/cost: public, free. Coder without keys: yes, useless for this window.

### 1b. REST Trades — real `since` pagination, entire market history

**This is a real Kraken-native paginated path.** Docs and live agree.

#### URLs opened

- REST spec: https://docs.kraken.com/api-reference/market-data/get-recent-trades  
  Title says “Get Recent Trades”; `since` still walks history.
- Support FAQ (entire history → rebuild any OHLC): https://support.kraken.com/articles/advanced-api-faq
- Support Python client (CSV time-and-sales): https://support.kraken.com/articles/360029077772-python-code-to-retrieve-historical-time-and-sales-trading-history-
- Historical-data guide (1000/call, ns `since`): https://docs.kraken.com/exchange/guides/general/historical-data
- Rate limits (private counter; public is IP): https://docs.kraken.com/exchange/guides/rest/ratelimits
- Live: `GET https://api.kraken.com/0/public/Trades?pair=XRPEUR&since=0&count=3`
- Live: `GET https://api.kraken.com/0/public/Trades?pair=XRPEUR&since=1672527600000000000&count=5`
- Live: `GET https://api.kraken.com/0/public/Trades?pair=XRPEUR&since=1672527708487498662&count=1000`
- Live: `GET https://api.kraken.com/0/public/Trades?pair=XRPEUR&count=5` (recent, no since)

#### What docs say

- Entire trading history is available, first trade to latest.
- `since=0` starts at market birth.
- `since` is unix **nanoseconds** (seconds + 9 digits). Response `last` is the next `since`.
- Rebuild OHLC for any interval from those ticks (Kraken’s own FAQ wording).
- Default / max `count` = 1000.

Support Python uses the **result key** (e.g. `XXBTZUSD`). For this pair the result key is `XXRPZEUR`, not the request altname `XRPEUR`. Using `result["XRPEUR"]` will KeyError.

#### What live calls actually returned

| Call | First trade time (UTC) | Notes |
|---|---|---|
| `since=0`, count=3 | `2017-05-18T15:51:07Z` | Market start, not 2023 |
| `since=1672527600` + 9 zeros, count=5 | `2022-12-31T23:01:42Z` | **On the Brussels window start** |
| Next page, count=1000 | `2022-12-31T23:01:48Z` → `2023-01-01T08:28:38Z` | 1000 trades ≈ 9.4 hours at that snapshot |
| No `since`, count=5 | `2026-08-27T19:56:22Z` | Recent-only if you omit `since` |

Covers 2023-01-01? **Yes**, as ticks. Not as 15m bars until Coder aggregates. Empty 15m slots (no prints) are missing unless Coder inserts them — same rule as Kraken’s OHLCVT CSVs. Do not invent those bars.

#### Rate limits (name them; do not guess a secret counter)

Public Trades/OHLC are **not** the keyed REST call-counter (Starter 15 / Intermediate 20). They are **IP-throttled**.

| Source | Stated delay |
|---|---|
| Historical-data “safe intervals” table | **Trades 1–2 seconds**; OHLC 1 second |
| Same page, earlier note | 100–200 ms “to avoid throttling” (looser, conflicts with the table) |
| Support Python example | `time.sleep(3)` on error / exception |
| Freqtrade Kraken notes | `rateLimit: 3100` ms between calls if using CCXT |

Errors to expect: `EAPI:Rate limit exceeded`, `EService: Throttled: [unix]`. Back off; do not retry as an order.

One measured page (1000 trades / ~9.4 h near 2023-01-01) is **not** a lifetime rate. Do not project a total request count from that single page. Walk until `last` / trade time passes “now.”

Auth: none. Cost: none. Coder without keys: **yes.**

### 1c. Downloadable historical OHLCVT CSV (first-party 15m)

**This is the Kraken-native candle file, not the REST 720 window.**

#### URLs opened

- Support (OHLCVT): https://support.kraken.com/articles/360047124832-downloadable-historical-ohlcvt-open-high-low-close-volume-trades-data
- CSV section: https://support.kraken.com/sections/360009899492-csv-data
- Complete ZIP (Google Drive): https://drive.google.com/file/d/1ptNqWYidLkhb2VAKuLCxmp2OXEfGO-AP/view?usp=sharing
- Quarterly folder: https://drive.google.com/drive/folders/15RSlNuW_h0kVM8or8McOGOMfHeBFvFGI?usp=sharing
- Export URL (virus-scan interstitial): https://drive.google.com/uc?export=download&id=1ptNqWYidLkhb2VAKuLCxmp2OXEfGO-AP
- Third-party merge walkthrough (file naming only): https://concretumgroup.com/how-to-get-free-full-crypto-intraday-data-2013-2025-from-kraken/

#### What support says

- CSV OHLCVT for **each currency pair**, from market beginning to “the present.”
- Each ZIP contains intervals **1, 5, 15, 30, 60, 240, 720, 1440** minutes.
- Missing rows = no trades in that interval. Do not invent fills.
- REST OHLC is acknowledged as limited depth; these ZIPs are the bulk dump.
- Complete = one ZIP of all pairs; incrementals = quarterly ZIPs.

No Kraken account or API key is listed as required. Files are on a public Google Drive share.

#### What the pages/files actually returned (without unzipping 7.3G)

| Probe | Result |
|---|---|
| Drive file page title | `Kraken_OHLCVT.zip - Google Drive` |
| Virus-scan interstitial | “`Kraken_OHLCVT.zip` **(7.3G)** is too large for Google to scan” |
| Quarterly folder title | `OHLCVT Updates` |
| Zip names visible in folder HTML on 2026-08-27 | `Kraken_OHLCVT_Q{1–4}_{2023,2024,2025}.zip` and `Kraken_OHLCVT_Q1_2026.zip` |
| **Not** listed in that HTML | `Q2_2026`, `Q3_2026` |

Concretum (secondary): same complete file id; they treat the complete ZIP as **inception through Q3 2024**, then apply later quarterlies. Naming pattern they document: `{PAIR}_{INTERVAL}.csv` with no header, columns `timestamp,open,high,low,close,volume,trades` (example `XBTUSD_1.csv`, `ADAEUR_1440.csv`). **`XRPEUR_15.csv` was not unzipped in this research.** Support says 15m exists for each pair; XRPEUR is an online pair. Coder must `namelist` the ZIP before treating that filename as present.

Covers 2023-01-01? **Expected yes** if `XRPEUR_15.csv` is in the complete ZIP and/or `Q1_2023`. Not proven by opening the CSV.

Covers **now**? **Not from the ZIPs alone.** Last listed quarterly is Q1 2026 (through 2026-03-31). Q2 2026 (Apr–Jun) was not in the folder listing. Q3 2026 is in progress as of this probe. Tail after last quarterly must be filled from **Trades reconstruct** (ring 1b) or the last-7.5-day REST OHLC (not enough for a multi-month tail).

License/cost: Kraken-published, no purchase listed on the support article. Google Drive ToS apply to the host. Coder without **Kraken** keys: **yes**. Coder without friction: **no** — 7.3G + virus-scan confirm page; datacenter IPs often fail automated Drive downloads (Concretum says scripts get blocked; they download manually). No Google API key is required for the share link if a human (or a confirm-token GET) can complete the interstitial.

### 1d. Downloadable trades history CSV (time and sales)

#### URLs opened

- Support: https://support.kraken.com/articles/360047543791-downloadable-historical-market-data-time-and-sales-
- Complete ZIP: https://drive.google.com/file/d/10zh3tDpqANYvVtYVgczwVz3UZFRUb1el/view?usp=share_link
- Quarterly folder: https://drive.google.com/drive/folders/188O9xQjZTythjyLNes_5zfMEFaMbTT22?usp=sharing

#### What it actually returns

File page title: `Kraken_Trading_History.zip`. Folder title: `Trading History Updates`. Folder HTML on this probe listed `Kraken_Trading_History_Q3_2025.zip`, `Q4_2025`, `Q1_2026` — Drive folder pages lazy-load; **do not treat that as a complete quarterly inventory.**

Same 7.3G-class Drive caveats. This is ticks, not 15m. Useful as a Kraken-native bulk alternative to REST Trades if the ZIP can be fetched. REST Trades already paginates without Drive.

Covers 2023-01-01? Support says from market beginning. Not unzipped. Coder without Kraken keys: yes, with the same Google interstitial.

### 1e. Futures “public execution events” — wrong market

URL opened: https://docs.kraken.com/api-reference/market-history/get-public-execution-events

Host: `https://futures.kraken.com/api/history/v3` — **Kraken Futures**, `GET /market/{tradeable}/executions`. Paginated `since`/`before`/`continuation_token`. Not spot `XRP/EUR`. Do not use as XRPEUR spot OHLC.

### Ring 1 summary for Coder

| Path | 15m candles? | 2023-01-01 | Through now | Coder, no keys |
|---|---|---|---|---|
| REST OHLC 15 | yes, last 720 | no | last 7.5d only | yes, unsatisfiable |
| REST Trades + aggregate | after reconstruct | **yes** (ticks live-proven) | **yes** (walk `last`) | **yes** |
| Drive OHLCVT `XRPEUR_15.csv` | yes, if file present | expected, unzip to confirm | **no** (ZIP tail stops at last quarterly; Q1 2026 listed, Q2 2026 not) | no Kraken key; Drive 7.3G is the blocker |
| Drive trades ZIP | after reconstruct | expected | same quarterly tail issue | same Drive blocker |

**Prefer Kraken-native:** REST Trades reconstruct is the path that is live-proven, keyless, and reaches both 2023-01-01 and now. Drive OHLCVT is the official candle dump if Coder can actually obtain the ZIP and then Trades-fill the post-Q1-2026 tail.

---

## Ring 2 — other EUR venues (Bitstamp already labeled)

Keep looking for Kraken-native (ring 1). These are venue substitutes, not Kraken prints.

### 2a. Bitstamp XRP/EUR — fallback label `BITSTAMP-XRPEUR`

#### URLs opened

- Docs: https://www.bitstamp.net/api/ (OHLC data)
- Live: `GET https://www.bitstamp.net/api/v2/ohlc/xrpeur/?step=900&limit=5&start=1672527600`
- Live: `GET https://www.bitstamp.net/api/v2/ohlc/xrpeur/?step=900&limit=1000&start=1672527600`
- Live: `GET https://www.bitstamp.net/api/v2/ohlc/xrpeur/?step=900&limit=3` (recent)
- Live trades (not used for 15m): `GET https://www.bitstamp.net/api/v2/transactions/xrpeur/?time=day`

#### What docs say

- `step=900` is 15 minutes (enum includes 900).
- `limit` 1–1000, required.
- `start` / `end` unix. If both set, **end wins**. If neither, data up to now.
- No auth on this market-data GET.

#### What live calls actually returned

| Call | Count | First timestamp | Last timestamp |
|---|---|---|---|
| `start=1672527600`, limit=5 | 5 | `2022-12-31T23:00:00Z` (**Brussels window start**) | `2023-01-01T00:00:00Z` |
| `start=1672527600`, limit=1000 | 1000 | same start | `2023-01-11T08:45:00Z` (~10.4 days) |
| no start, limit=3 | 3 | `2026-08-27T19:15:00Z` | `2026-08-27T19:45:00Z` |

Shape: `timestamp, open, high, low, close, volume` (no vwap, no trade count).

Covers 2023-01-01? **Yes.** Through now? **Yes**, by paging `start` forward ~1000 × 15m per call (~128 calls for the full window). That is a **Bitstamp** book, not Kraken.

Rate limits (docs): **400 requests/second** standard; **10,000 per 10 minutes** default threshold; `400.002` on exceed. No key for public OHLC.

License/cost: public Bitstamp market data, no key. Coder without keys: **yes.**

This is the already-labeled fallback `BITSTAMP-XRPEUR`. Do not promote it over Kraken-native Trades/OHLCVT.

### 2b. Coinbase Advanced Trade public candles `XRP-EUR`

#### URLs opened

- Docs: https://docs.cdp.coinbase.com/api-reference/advanced-trade-api/rest-api/public/get-public-product-candles
- Product: `GET https://api.coinbase.com/api/v3/brokerage/market/products/XRP-EUR`
- Candles: `GET .../products/XRP-EUR/candles?start=&end=&granularity=FIFTEEN_MINUTE&limit=`

#### What docs say

Public `GET /api/v3/brokerage/market/products/{product_id}/candles`. `granularity=FIFTEEN_MINUTE`. `start`/`end` required. Default/max **350** candles. No key on the public route.

#### What live calls actually returned

| Window probed | Candles returned |
|---|---|
| Product metadata | `product_id=XRP-EUR`, `status=online`, `trading_disabled=false` |
| start=`1672527600` (2023-01-01 Brussels), 350 bars | **`candles: []`** |
| 2023-07-01 | **0** |
| 2024-01-01 | 97 (data exists) |
| 2024-07-01, 2024-10-01, 2024-11-01, 2025-01-01, recent 2026-08 | non-empty |

Covers 2023-01-01? **No** (empty). Pair is live now; history does not start at the paper window. Coder without keys: yes, but unusable for this start date. Not Kraken-native.

### 2c. Bitfinex `tXRPEUR`

#### URLs opened

- `GET https://api-pub.bitfinex.com/v2/candles/trade:15m:tXRPEUR/hist?limit=5&sort=1&start=1672527600000` → `[]`
- `GET https://api-pub.bitfinex.com/v2/tickers?symbols=tXRPEUR` → `[]`
- Also empty: `tXRP/EUR`, `tXRP:EUR`

Covers 2023-01-01? **No pair on this public ticker/candle path.** Coder without keys: the GETs work; they return empty. Not a venue.

### 2d. Kraken downloadable history

Same as ring 1c / 1d (Drive OHLCVT + trades ZIPs). First-party. Listed again here only because the job named it in ring 2.

---

## Ring 3 — aggregators and wrappers

### 3a. Cryptowatch / Kraken Pro charts

#### URLs opened

- Sunset post: https://blog.kraken.com/product/cryptowatch-to-sunset-kraken-pro-to-integrate-cryptowatch-features (31 Jul 2023)
- Landing: https://www.kraken.com/cryptowatch
- Live: `https://api.cryptowat.ch/markets/kraken/xrpeur/ohlc?periods=900` → **DNS NXDOMAIN** (`No address associated with hostname`)

Cryptowatch Web/Desktop/Mobile **and Cryptowatch API** were sunsetting; blog says the API is included. Kraken Pro is a trading UI, not a documented historical OHLC dump. No usable public Cryptowatch path.

Covers 2023-01-01? N/A (dead). Coder without keys: cannot resolve the host.

### 3b. CryptoDataDownload

#### URLs opened

- Kraken page: https://www.cryptodatadownload.com/data/kraken/ — marketing copy; on this fetch the Kraken OHLC block rendered as **“Currently unavailable.”**
- `https://www.cryptodatadownload.com/cdd/Kraken_XRPEUR_d.csv` → **404**
- `.../Kraken_XRPEUR_1h.csv` → **404**
- `.../Kraken_XRPEUR_15m.csv` → **404**
- `.../Bitstamp_XRPEUR_1h.csv` → **200** `text/csv`
- `.../Bitstamp_XRPEUR_d.csv` → **200**
- `.../Bitstamp_XRPEUR_15m.csv` → not a 15m file (no usable 15m URL found)

Bitstamp 1h CSV (not 15m): header `unix,date,symbol,open,high,low,close,Volume XRP,Volume EUR`; first data line is dated **2026-08-27** (file is newest-first); last line **2018-05-15**. Calendar 2023 is inside that 1h file. **Wrong resolution for this job.** First line of file is an attribution URL to cryptodatadownload.com.

License/cost: free CSV with their attribution; Plus/API token products exist on the site. Coder without keys: Bitstamp 1h/d yes; Kraken files 404; no 15m.

### 3c. Tardis.dev (Kraken spot trades, not native 15m OHLC)

#### URLs opened

- https://docs.tardis.dev/historical-data-details/kraken
- https://docs.tardis.dev/downloadable-csv-files/api
- https://api.tardis.dev/v1/exchanges/kraken
- `GET https://datasets.tardis.dev/v1/kraken/trades/2023/01/01/XRP-EUR.csv.gz` (no key)
- `GET https://datasets.tardis.dev/v1/kraken/trades/2023/01/02/XRP-EUR.csv.gz` (no key)
- `.../XRPEUR.csv.gz` → 400 invalid symbol (must be `XRP-EUR`)

#### What docs / live returned

- Kraken data from **2019-06-04**. Dataset symbol `XRP-EUR`: `availableSince=2019-06-04`, `availableTo=2026-08-27`, types include `trades` (no native 15m OHLC type).
- Unauthorized: **first day of each month only.**
- 2023-01-01 file: HTTP 200 gzip CSV, **2458 lines** including header `exchange,symbol,timestamp,local_timestamp,id,side,price,amount`. That is **UTC day 2023-01-01**, not Brussels midnight (window start is still 2022-12-31 23:00Z).
- 2023-01-02 file: **401** — “only historical CSV … first day of each month.”

Full 2023→now needs a Tardis API key. First-of-month samples are not a 15m series. Reconstruct would still be required.

License/cost: commercial except monthly-first-day samples. Coder without keys: samples only. Not preferable to Kraken REST Trades.

### 3d. Kaiko

#### URLs opened

- https://docs.kaiko.com/rest-api/data-feeds/level-1-and-level-2-data/level-1-aggregations/trade-count-ohlcv-and-vwap
- Live (no key): `GET https://us.market-api.kaiko.io/v2/data/trades.v1/exchanges/krkn/spot/xrp-eur/aggregations/count_ohlcv_vwap?interval=15m&start_time=2023-01-01T00:00:00.000Z` → **403** `Please provide authentication details`

Docs: `X-Api-Key` required; `interval` can be `15m`. Paid institutional feed. Coder without keys: **no.** Coverage of 2023 not verified (auth wall).

### 3e. CoinAPI

#### URLs opened

- https://docs.coinapi.io/market-data/rest-api/ohlcv
- Live (no key): `GET https://rest.coinapi.io/v1/ohlcv/KRAKEN_SPOT_XRP_EUR/history?period_id=15MIN&time_start=2023-01-01T00:00:00&limit=5` → **401** missing `X-CoinAPI-Key`

Docs: sign up for a key; Startup plan 10 req/s and 1,000/day. Historical OHLCV exists as a product; **this research did not retrieve any KRAKEN XRP/EUR 15m rows.** Coder without keys: **no.**

### 3f. CCXT examples

#### URLs opened

- https://docs.ccxt.com/docs/exchanges/kraken (`fetchOHLCV`, `fetchTrades`)
- https://github.com/ccxt/ccxt/issues/4449 (Kraken OHLC ignores `since` for deep history)
- Freqtrade Kraken notes: https://www.freqtrade.io/en/stable/exchanges/ and https://www.freqtrade.io/en/stable/data-download/

CCXT `kraken.fetchOHLCV('XRP/EUR', '15m')` is the REST OHLC wrapper. Docs advertise `params.paginate`. That cannot expand the server’s 720-candle cache — live REST already proved `since=2023` still returns August 2026. Freqtrade: “The Kraken API does only provide 720 historic candles… `--dl-trades` is mandatory” for backtest.

`fetchTrades` is the CCXT spelling of ring 1b. RateLimit guidance from Freqtrade: 3100 ms. Coder without keys: yes for public methods. Do not use `fetchOHLCV` as the invert-wf-2023 loader.

### 3g. First-party CSV

Same as ring 1c (Kraken OHLCVT) and 1d (Kraken trades ZIP). That is the first-party CSV. CDD is third-party and lacked Kraken XRPEUR files on this probe.

---

## Ring 4 — reconstruct 15m from public trades (if still thin)

Ring 1 is not thin for ticks. Reconstruct is the Kraken-native way to **make** 15m bars when REST OHLC is last-720-only and Drive ZIPs are awkward.

### Method (from Kraken support, not invented)

1. `GET /0/public/Trades?pair=XRPEUR&since=<ns>&count=1000`
2. Start `since = 1672527600` + `999999999` (support Python: `(start_unix - 1) + "999999999"`) or `1672527600000000000`.
3. Append trades; set next `since = result.last`.
4. Stop when trade time ≥ now (or a chosen end).
5. Result key is `XXRPZEUR`.
6. Bucket by `floor(time / 900) * 900` (unix seconds). OHLC = first/max/min/last price; volume = sum size; trades = count. VWAP = size-weighted if the paper wants it (REST OHLC includes vwap; Bitstamp OHLC does not).
7. Intervals with zero trades: **omit** (Kraken OHLCVT rule) or mark missing. Do not forward-fill prices in this research and do not invent candles.

### Rate limits to name

| Endpoint | Source | Delay / cap |
|---|---|---|
| Kraken `OHLC` | docs historical-data table | 1 s between calls |
| Kraken `Trades` | same table | **1–2 s** between calls |
| Kraken `Trades` | same page note | 100–200 ms (stricter table wins for safety) |
| Kraken `Trades` | support Python | 3 s on error |
| Kraken public | REST ratelimits guide | IP throttle; `EAPI:Rate limit exceeded`; `EService: Throttled: [unix]` |
| Kraken via CCXT/Freqtrade | Freqtrade Kraken page | 3100 ms `rateLimit` |
| Bitstamp public | Bitstamp API docs | 400 req/s; 10k / 10 min |
| CoinAPI (if keyed later) | CoinAPI docs | plan table, Startup 10 rps / 1k per day |
| Tardis datasets | Tardis docs | monthly-first-day free; else Bearer key |
| Kaiko | Kaiko docs | `X-Api-Key`; 403 without |

Do not place or retry orders. This reconstruct is market-data GET only.

### What was not reconstructed here

No 15m series was built. No candle CSV is attached. Coder owns the fetch + aggregate if the paper job proceeds.

---

## Coder path (preference order, not a score)

Still paper. Not the fund gate.

1. **Kraken-native ticks (usable, keyless, live-proven for 2023-01-01 and paging):** `GET /0/public/Trades` with nanosecond `since` / `last`, 1000/call, 1–2 s pause, aggregate 15m. Pair key `XXRPZEUR`. Label the series as Kraken XRPEUR reconstructed 15m, not as REST `/OHLC`.
2. **Kraken-native official 15m CSV (usable if the ZIP is actually obtained):** Drive `Kraken_OHLCVT.zip` (7.3G) + quarterlies through `Kraken_OHLCVT_Q1_2026.zip`, extract `XRPEUR_15.csv` after `namelist` confirms it, then **Trades-fill from 2026-04-01 to now** (Q2 2026 not listed). Do not assume Google Drive automation works from this environment.
3. **Fallback already labeled `BITSTAMP-XRPEUR`:** `GET /api/v2/ohlc/xrpeur/?step=900&limit=1000&start=` — real 15m from the Brussels window start to now, no keys, ~1000 bars/call. Different venue. Keep looking at (1)/(2) first.
4. **Do not use:** Kraken REST `/OHLC` interval=15 (last 720 / 7.5 days). CCXT `fetchOHLCV` on Kraken. Cryptowatch. Coinbase XRP-EUR from 2023-01-01 (empty). Bitfinex `tXRPEUR` (no pair). CDD Kraken XRPEUR URLs (404). Kaiko/CoinAPI/Tardis-full without keys. Kraken Futures history host.

REST `/OHLC?pair=XRPEUR&interval=15` remains the right **incremental** feed for new bars after a backfill, not the backfill itself.
