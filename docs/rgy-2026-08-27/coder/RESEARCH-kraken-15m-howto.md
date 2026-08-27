# RESEARCH — Kraken 15m how-to (Coder runbook)

**Seat:** RESEARCHER · Coder  
**Date:** 2026-08-27  
**Stamp:** VOORBEELD · paper / simulated · not FACTUUR · not INVOICE · not live-trade advice  
**HEAD (this repo):** `2170952`  
**Still paper. No orders. No keys. No live.**

This file is the **runbook** for building a **Kraken-native** XRPEUR 15-minute series from `2023-01-01 00:00 Europe/Brussels` to now, for paper book **`invert-wf-2023`**.

It is **not** a score. It does **not** replace the named Vision print. It does **not** feed the fund gate.

Probed this sitting from **docs + public REST + public Drive HTML** (no API key, no `API-Sign`, no Kraken MCP). Server clock: `GET /0/public/Time` → `unixtime` **1787862001** (`Thu, 27 Aug 26 20:20:01 +0000`). `GET /0/public/SystemStatus` → `online`.

Parents: [PR #197](https://github.com/eyeskull2220/solana-invoice/pull/197) (wire facts), [PR #198](https://github.com/eyeskull2220/solana-invoice/pull/198) (broaden). This file is the **how**, not a second verdict.

---

## Locks (read before fetching)

| Lock | Meaning |
|---|---|
| Named score is **Vision** | `BINANCE-VISION-XRPEUR` (+ Kraken tail) stays the named 15m print until a **Kraken-native dump exists**. Do not relabel Vision as Kraken. |
| **D6 is after the 1-limit write-up** | Venue dump is design-out **D6** ([PR #201](https://github.com/eyeskull2220/solana-invoice/pull/201)). Do **not** mint a new `invert-wf-2023` score from this dump until the **1-limit** pack exists ([PR #206](https://github.com/eyeskull2220/solana-invoice/pull/206) `RESEARCH-one-limit-arming.md`). Fetch is allowed. Rescore is not this file. |
| Still paper | No keys. No private REST. No `kraken order`. Not the fund gate. Gate stays **`invert-paper` fill 1**. Do not reseal `c9689f5d`. |
| No invented candles | Missing 15m row = no trades. Skip the bucket. Do not forward-fill. Do not splice Binance/Bitstamp into a file labeled Kraken. |

---

## Simple first (do this, then stop if it already answers)

**`GET /0/public/OHLC?pair=XRPEUR&interval=15` cannot source 2023.**

Docs: https://docs.kraken.com/api/docs/rest-api/get-ohlc-data — *“Returns up to 720 of the most recent entries (older data cannot be retrieved, regardless of the value of `since`).”*

This sitting (same window with and without `since=1672527600`):

| | |
|---|---|
| `n` | **721** (720 committed-scale + current uncommitted bar) |
| First bar | `1787213700` = **2026-08-20 08:15:00Z** |
| Last bar | `1787861700` = **2026-08-27 20:15:00Z** |
| Span | **7.5 days** |

`since=2023` still returns August 2026. **UNSATISFIABLE as the history store.** Use it only as a **tail poll** after a real dump exists. Drop the last row until that bar closes.

Two Kraken-native paths that **do** work: **public Trades pagination** (below), or **official OHLCVT ZIP `XRPEUR_15.csv`**.

---

## Window and pair (do not guess)

| Item | Value |
|---|---|
| Query `pair` | **`XRPEUR`** |
| Result key (default, omit `assetVersion`) | **`XXRPZEUR`** — parse the key that is not `last` / `error`. `result["XRPEUR"]` KeyErrors. |
| `wsname` / status this sitting | `XRP/EUR` / `online` |
| Window start | **2023-01-01 00:00:00 Europe/Brussels** = CET = unix **`1672527600`** = `2022-12-31 23:00:00 UTC` |
| Bar grid | UTC 15m (`time // 900 * 900`). Do not re-bucket into “Brussels candles.” |
| First XRPEUR print ever | `since=0` → `1495122667.744094` = **2017-05-18 15:51:07Z**, `trade_id` **1**. 2023 is **after** listing. |

First **in-window** print this sitting:

```
GET https://api.kraken.com/0/public/Trades?pair=XRPEUR&since=1672527600000000000&count=1
```

→ `XXRPZEUR[0].time` **1672527702.5968883** = **2023-01-01 00:01:42+01:00**, `trade_id` **18373896**. Quiet ~102 s after midnight Brussels is not a delist. **Do not invent a 00:00:00 candle.**

Send a `User-Agent`. Kraken FAQ: Cloudflare Browser Integrity Check can **403** requests with missing / odd UA. Public GETs need **no** `API-Key` / `API-Sign`. Do not send both families.

---

## Path A — public Trades paginate (always works, no Drive, no keys)

Official method: page time-and-sales, then **create OHLC for any interval** (Kraken FAQ).

### Docs

| What | URL |
|---|---|
| REST Trades | https://docs.kraken.com/api/docs/rest-api/get-recent-trades |
| Same OpenAPI | https://docs.kraken.com/api-reference/market-data/get-recent-trades |
| Historical-data guide (`since` **nanoseconds**, `last`, 1000/call) | https://docs.kraken.com/exchange/guides/general/historical-data |
| FAQ (entire history; OHLC 720 cap; page with `last`) | https://support.kraken.com/articles/advanced-api-faq |
| Support Python (CSV ticks; `since = (start-1)+"999999999"`) | https://support.kraken.com/articles/360029077772-python-code-to-retrieve-historical-time-and-sales-trading-history- |
| Public rate limits (IP; Trades/OHLC also **per pair**) | https://support.kraken.com/articles/206548367-what-are-the-api-rate-limits- |

Title says “Get Recent Trades.” **`since` still walks history.** Omit `since` → last 1000 only (this sitting: August 2026). That is not 2023.

Docs conflict: the historical-data guide says *“Kraken does not provide a bulk historical data dump.”* The **support OHLCVT article does** (Path B). For REST ticks, ignore that sentence. For bulk candles, follow the support article.

### Exact URL

```
GET https://api.kraken.com/0/public/Trades?pair=XRPEUR&since=<ns>&count=1000
```

Smoke (copy/paste):

```bash
curl -sS -A 'invert-wf-2023-research' \
  'https://api.kraken.com/0/public/Trades?pair=XRPEUR&since=1672527600000000000&count=1000'
```

### `since` / `last`

| Rule | Do this |
|---|---|
| First call for this window | **`since=1672527600000000000`** (unix seconds + nine zeros). FAQ: nanosecond UNIX. |
| Support Python spelling | `str(start_unix - 1) + "999999999"` → `1672527599999999999`. Either is fine at the boundary; this sitting the 9-zero form returned the first in-window print. |
| Next call | **`since = result.last`** (string, nanoseconds). **Do not add 1.** FAQ: replace `since` with **`last` from the previous result.** |
| Trade `time` field | Unix **seconds** (float). Not ns. |
| Row shape | `[price, volume, time, buy/sell, market/limit, miscellaneous, trade_id]` |
| `count` | **1000** max. Default 1000. `count=1001` is silently capped (PR 197). |
| Stop | Last trade `time >= now`, or `last` stops advancing, or you hit a chosen end unix. |
| Persist | Save **`last` as returned** (string). Do not round. |

`since=1672527600` (seconds, no 9 zeros) also returned the same first in-window print this sitting. **Always page with `last`**, which is ns.

### 1 req/s

Public Trades/OHLC are **IP + pair** throttled. Private-key counters (Starter 15 / decay) are **not** this path — this runbook sends **no key**.

| Source | Delay |
|---|---|
| **This job** | **1 request / second** (`sleep 1` after every successful call) |
| Support public article | **≤ 1 per second** stays inside; faster may throttle for seconds or longer |
| Historical-data “safe intervals” table | Trades **1–2 seconds** (stricter than the same page’s 100–200 ms note — **do not use 100 ms**) |
| Support Python | `time.sleep(3)` **on error / exception only** (not a license to burst on success) |

Errors: `EAPI:Rate limit exceeded`, `EService: Throttled: [unix]`. Sleep **3 s**, retry the **same** `since` (the server did not advance). Do not treat this as an order retry. Do not spray.

### Reconstruct 15m (from real prints only)

Kraken FAQ: rebuild any interval from time and sales. Kraken OHLCVT note: **missing interval = no trades**.

For each trade with `time >= 1672527600`:

```text
bucket = floor(time / 900) * 900     # UTC bar open, unix seconds
open   = first price in bucket
high   = max price
low    = min price
close  = last price
volume = sum(volume)
trades = count of prints
vwap   = sum(price*volume)/sum(volume)   # optional; REST OHLC has vwap, OHLCVT CSV does not
```

| Do | Do not |
|---|---|
| Emit a row only if `trades >= 1` | Insert synthetic OHLC for empty buckets |
| Label the file **`KRAKEN-XRPEUR-TRADES-15m`** (reconstructed) | Label it REST `/OHLC` or Vision or Bitstamp |
| Skip buckets with zero prints | Forward-fill close |
| Drop an uncommitted last REST OHLC bar if you later tail-poll | Use REST OHLC to backfill 2023 |

Synthesized **clock** bars for the walk-forward engine (PLAN #196) **must not fill**. That is engine policy, not a candle you write into this dump.

### Expected pages 2023 → now (this sitting)

Not guessed from one 1000-trade page. Taken from public weekly OHLC **`count`** (Kraken’s own trade counts), which covers the whole listing (720-week ceiling still reaches 2017 for this pair):

```
GET https://api.kraken.com/0/public/OHLC?pair=XRPEUR&interval=10080
```

This sitting: **485** weekly bars, first `1495065600` (2017-05-18), last `1787788800` (2026-08-27). Sum of `count` on weeks that overlap the window (`week_open + 604800 > 1672527600`):

| | |
|---|---|
| Weeks overlapping window | **192** |
| Sum of weekly `count` | **9,787,839** trades |
| Pages at 1000/call | **ceil = 9788** |
| Wall-clock at **1 req/s** | **≈ 2.72 hours** (9788 s) |
| Wall-clock at 2 s/call (docs table) | **≈ 5.44 hours** |
| Weekly `count` range in window | min **9740** / max **303466** per week |
| First selected week | `1672272000` = 2022-12-29 00:00Z, `count` 22765 (overlaps **~3 days before** the Brussels midnight start → slight **overestimate**) |
| Last selected week | current/uncommitted weekly bar |

**9788 is a budget, not a stop code.** Walk until `last` / trade time passes now. Density is not constant (max week is ~30× min week). Do not project the rest of the tape from a single 9-hour page.

One-line re-check of the budget:

```bash
python3 - <<'PY'
import json, math, urllib.request
req = urllib.request.Request(
    'https://api.kraken.com/0/public/OHLC?pair=XRPEUR&interval=10080',
    headers={'User-Agent': 'invert-wf-2023-research'})
d = json.load(urllib.request.urlopen(req, timeout=60))
bars = d['result']['XXRPZEUR']
start = 1672527600
n = sum(int(r[7]) for r in bars if int(r[0]) + 604800 > start)
print('trades', n, 'pages', math.ceil(n / 1000))
PY
```

### Copy/paste pager (public, no keys, 1 req/s)

Writes **ticks** then you aggregate. Resume by reading the last saved `last` ns. This sitting did **not** walk 9788 pages.

```python
#!/usr/bin/env python3
"""Public Kraken Trades pager. No keys. 1 req/s. Still paper."""
import json, time, urllib.error, urllib.request

PAIR = "XRPEUR"
SINCE = "1672527600000000000"  # replace with saved last when resuming
UA = "invert-wf-2023-research"
OUT = "xrpeur-trades-2023.ndjson"

since = SINCE
with open(OUT, "a", encoding="utf-8") as fh:
    while True:
        url = (
            "https://api.kraken.com/0/public/Trades"
            f"?pair={PAIR}&since={since}&count=1000"
        )
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        try:
            raw = urllib.request.urlopen(req, timeout=60).read()
        except (urllib.error.URLError, TimeoutError):
            time.sleep(3)
            continue
        data = json.loads(raw)
        if data.get("error"):
            time.sleep(3)
            continue
        result = data["result"]
        last = result["last"]
        trades = next(v for k, v in result.items() if k != "last")
        if not trades:
            break
        fh.write(json.dumps({"last": last, "n": len(trades), "trades": trades}) + "\n")
        fh.flush()
        if last == since:
            break
        since = last
        t_last = float(trades[-1][2])
        if t_last >= time.time():
            break
        time.sleep(1.0)
print("resume since=", since)
```

Then bucket as above. **Do not** emit empty 15m rows.

---

## Path B — official OHLCVT ZIP `XRPEUR_15.csv` (Kraken-native candles)

Preferred **bulk** path if Coder can actually obtain the files. No Kraken account. No API key. Google Drive hosts the ZIP.

### How to get the links **this sitting** (durable first)

Drive file IDs rotate when Kraken re-uploads. **The support article is the pointer.** If a memorized ID 404s, re-scrape the article — do not invent a mirror.

```bash
# 1. OHLCVT article (candles)
curl -sS -L -A 'invert-wf-2023-research' \
  'https://support.kraken.com/articles/360047124832-downloadable-historical-ohlcvt-open-high-low-close-volume-trades-data' \
  | grep -oE 'https://drive.google.com[^"[:space:]<>]+'

# 2. Time-and-sales article (ticks ZIP, optional)
curl -sS -L -A 'invert-wf-2023-research' \
  'https://support.kraken.com/articles/360047543791-downloadable-historical-market-data-time-and-sales-' \
  | grep -oE 'https://drive.google.com[^"[:space:]<>]+'
```

CSV section index (no Drive IDs of its own): https://support.kraken.com/sections/360009899492-csv-data

### Links live this sitting (2026-08-27 20:20 UTC)

Scraped from those two articles’ HTML, then **GET** the Drive pages (HTTP 200, titles match):

| What | Support | Drive this sitting | Probe |
|---|---|---|---|
| Complete OHLCVT ZIP | article 360047124832 | https://drive.google.com/file/d/1ptNqWYidLkhb2VAKuLCxmp2OXEfGO-AP/view?usp=sharing | title **`Kraken_OHLCVT.zip`** |
| OHLCVT quarterlies | same article | https://drive.google.com/drive/folders/15RSlNuW_h0kVM8or8McOGOMfHeBFvFGI?usp=sharing | title **`OHLCVT Updates`** |
| Complete trades ZIP | article 360047543791 | https://drive.google.com/file/d/10zh3tDpqANYvVtYVgczwVz3UZFRUb1el/view?usp=share_link | title **`Kraken_Trading_History.zip`** |
| Trades quarterlies | same article | https://drive.google.com/drive/folders/188O9xQjZTythjyLNes_5zfMEFaMbTT22?usp=sharing | title **`Trading History Updates`** |

Direct export (virus-scan interstitial; 7.3G-class; datacenter IPs often fail):

```
https://drive.google.com/uc?export=download&id=1ptNqWYidLkhb2VAKuLCxmp2OXEfGO-AP
```

**Do not assume automated Drive download works from this VM.** A human confirm-token GET is the documented friction (PR 198). No Google API key is required for the public share if the interstitial completes.

### Quarterlies visible in folder HTML this sitting

**Present:** `Kraken_OHLCVT_Q{1–4}_{2023,2024,2025}.zip` and **`Kraken_OHLCVT_Q1_2026.zip`**.

**Not listed:** `Q2_2026`, `Q3_2026`.

Complete ZIP lags “now.” After the last CSV timestamp (expect through **2026-03-31** if only Q1 2026 is published), **Path A tail** from that unix as ns `since`. REST OHLC 15m only covers the last 7.5 days — not a multi-month tail.

Trades-folder HTML this sitting listed only `Q3_2025`, `Q4_2025`, `Q1_2026` — Drive folder pages lazy-load; **do not treat that as a complete inventory.** Prefer OHLCVT for 15m candles; use trades ZIP only if you want ticks without REST.

### Inside the ZIP (confirm; do not invent a missing file)

Support: each ZIP has intervals **1, 5, 15, 30, 60, 240, 720, 1440** minutes, **each pair**, from market start.

```bash
unzip -l Kraken_OHLCVT.zip | grep -E 'XRPEUR_15\.csv'
# also namelist every quarterly ZIP the same way
```

**`XRPEUR_15.csv` was not unzipped this sitting** (7.3G). Support says 15m exists per pair; XRPEUR is online. **`namelist` before treating the filename as present.**

Typical layout (Kraken + community extractors; verify on disk):

- No header
- Columns: `timestamp,open,high,low,close,volume,trades`
- **No `vwap`** (REST OHLC has `vwap` — do not mix schemas)
- **Missing row = no trades** (Kraken’s own note)

Keep `timestamp >= 1672527600`. Concat complete + quarterlies; sort; drop duplicate timestamps. **Do not insert empty-bar OHLC.**

Label: **`KRAKEN-OHLCVT-XRPEUR-15`**. That is the dump that can **retire the Vision name** — after the 1-limit write-up, on a **new** score, not by restamping −99.989999%.

---

## If a link is dead, broaden (in order)

Still Kraken-native until it is not. Still no keys. Still no invented candles.

1. **Re-scrape the support article HTML** for `drive.google.com` (IDs rotate).  
2. **Quarterly folder** if the complete ZIP 404s.  
3. **Trades ZIP** (article 360047543791) + reconstruct 15m (same as Path A).  
4. **Path A REST Trades** — live-proven this sitting; no Drive.  
5. Only if Kraken-native is blocked: fallback already labeled **`BITSTAMP-XRPEUR`** (`GET https://www.bitstamp.net/api/v2/ohlc/xrpeur/?step=900&limit=1000&start=1672527600`). **Different venue.** Keep looking at 1–4 first.  
6. **Do not use:** REST `/OHLC` interval=15 as 2023 history · CCXT `fetchOHLCV` on Kraken · Cryptowatch (`api.cryptowat.ch` NXDOMAIN) · Coinbase `XRP-EUR` from 2023-01-01 (empty) · Bitfinex `tXRPEUR` (no pair) · CDD `Kraken_XRPEUR_*.csv` (404) · Kaiko/CoinAPI/Tardis-full (need keys) · Kraken **Futures** history host · Vision relabeled as Kraken.

---

## What Coder writes vs what stays Vision

| Artifact | Status |
|---|---|
| Named 15m score | **Vision** (`BINANCE-VISION-XRPEUR` + Kraken tail). RED as invert ([PR #201](https://github.com/eyeskull2220/solana-invoice/pull/201)). Do not replace −99.989999%. |
| This runbook | How to **get** Kraken 15m. Not a score. |
| Dump file (later) | `KRAKEN-XRPEUR-TRADES-15m` and/or `KRAKEN-OHLCVT-XRPEUR-15` |
| New score | **After** 1-limit write-up **and** a Kraken-native dump. D6 then. Still `is_fund_gate: false`. |

---

## Out of scope (honoured)

- No paper or live Kraken orders, no Phantom, no keys  
- No `invert-paper` fill ping, no fund-gate score, no reseal of `c9689f5d`, no `dca-paper` reset  
- No shop/catalog HTML, no invented candles, no 9788-page walk in this sitting  
- Kraken MCP was error / undiscoverable; public REST was enough  

---

## Re-check (copy/paste — public only)

```bash
curl -sS -A 'invert-wf-2023-research' 'https://api.kraken.com/0/public/Time'
curl -sS -A 'invert-wf-2023-research' 'https://api.kraken.com/0/public/SystemStatus'
curl -sS -A 'invert-wf-2023-research' 'https://api.kraken.com/0/public/AssetPairs?pair=XRPEUR'
# 720-cap: first bar must stay days, not years, behind now
curl -sS -A 'invert-wf-2023-research' 'https://api.kraken.com/0/public/OHLC?pair=XRPEUR&interval=15'
# first in-window print must stay 2023-01-01 00:01:42+01:00 (or a later REAL print)
curl -sS -A 'invert-wf-2023-research' \
  'https://api.kraken.com/0/public/Trades?pair=XRPEUR&since=1672527600000000000&count=1'
# Drive IDs: scrape support, do not hard-fail a memorized hash
curl -sS -L -A 'invert-wf-2023-research' \
  'https://support.kraken.com/articles/360047124832-downloadable-historical-ohlcvt-open-high-low-close-volume-trades-data' \
  | grep -oE 'https://drive.google.com[^"[:space:]<>]+'
```

Parse `result.XXRPZEUR`. Sleep 1 s between Trades calls. **No keys.**

**`invert-wf-2023` may start 2023-01-01 Europe/Brussels. It may not start from REST OHLC. It may not invent bars. Named score stays Vision until a Kraken-native dump exists. D6 is after the 1-limit write-up. Still paper.**
