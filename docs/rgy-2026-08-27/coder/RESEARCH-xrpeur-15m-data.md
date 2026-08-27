# RESEARCH — XRPEUR 15m data for `invert-wf-2023`

**Seat:** RESEARCHER · Coder  
**Lens:** public Kraken market data only. Then RED / YELLOW / GREEN.  
**Date:** 2026-08-27  
**Stamp:** VOORBEELD · paper / simulated · not FACTUUR · not INVOICE · not live-trade advice  
**HEAD (this repo):** `2170952`  
**Still paper. No orders. No keys. No live.**

This file answers one question: **how to obtain Kraken XRPEUR 15-minute OHLC from 2023-01-01 00:00 Europe/Brussels through now**, for a **paper** walk-forward named **`invert-wf-2023`**.

It does **not** feed the funding gate. It does **not** feed `invert-paper`. It does not reseal `c9689f5d`. It does not reset `dca-paper`. It does not place paper or live orders.

Probed this sitting from public REST only (no API key, no `x-api-key`, no Kraken MCP — that namespace was error / undiscoverable). Server clock: `GET /0/public/Time` → `unixtime` 1787860741 (`Thu, 27 Aug 26 19:59:01 +0000`). `GET /0/public/SystemStatus` → `online`.

---

## Verdict

| Claim | Color |
|---|---|
| Pair `XRPEUR` is listed and online | **GREEN** |
| 2023-01-01 Europe/Brussels is **after** first print — do **not** truncate the window for listing | **GREEN** |
| REST `OHLC` `interval=15` can supply 2023→now | **RED** (720-bar ceiling ≈ 7.5 days) |
| REST `Trades` can supply 2023→now if paginated and aggregated locally | **GREEN** as a method, **YELLOW** as wall-clock (1 req/s, 1000 trades/page) |
| Official OHLCVT ZIP (`XRPEUR_15.csv`) + quarterly folder + Trades tail | **GREEN** preferred bulk path |
| Invent / forward-fill empty 15m bars as if Kraken printed them | **RED** |
| Use this series as the `invert-paper` fund gate | **RED** (wrong book) |
| Use this series as live / keys / orders | **RED** |

**Window start is not listing-limited.** First XRPEUR print is **2017-05-18**, not 2023-01-01. Write the real first date; do not pretend the pair starts in 2023.

---

## What this is / is not

| Name | Role here |
|---|---|
| **`invert-wf-2023`** | Paper walk-forward that **this data feeds**. XRPEUR 15m, window 2023-01-01 00:00 Europe/Brussels → now. |
| **`invert-paper`** | Named **funding-gate** book (fill 1 `PAPER-00029` as of sibling Coder 01). **Not this file.** |
| Lab clip `c9689f5d` | 8-day sealed lab (`fib-grid-invert-xrpeur-15m`, 2026-08-18 → 2026-08-26 BXL). **Not this file. Do not reseal.** |
| Fund gate | return > 0 after fees **and** ≥ 8 prints **and** maxDD ≤ 8% on `invert-paper`. **Not this file.** |

Loading 2023 candles into a later engine does **not** mint `PAPER-*` fills and does **not** green the gate.

---

## Pair string (do not guess)

`GET https://api.kraken.com/0/public/AssetPairs?pair=XRPEUR`

| Field | Wire value this sitting |
|---|---|
| Query `pair` | **`XRPEUR`** (altname; use this on OHLC / Trades) |
| Result key (default) | **`XXRPZEUR`** |
| `altname` | `XRPEUR` |
| `wsname` | `XRP/EUR` |
| `base` / `quote` | `XXRP` / `ZEUR` |
| `status` | `online` |
| `pair_decimals` | 5 |
| `tick_size` | `0.00001` |
| `ordermin` / `costmin` | `1.65` / `0.45` |

Optional `assetVersion=1` switches result keys to display names (`XRP/EUR`). Default (omit) keeps `XXRPZEUR`. **Do not normalize away the wire key.** Parse whichever key is not `last` / `error`.

Kraken blog (2017): new fiat pairs included XRP/EUR. That is listing copy, not a candle. First **print** is below.

---

## Window (Europe/Brussels → UTC)

Kraken REST timestamps are **UTC unix**. The walk-forward clock is **Europe/Brussels**. Convert once at the boundary; keep bars on the UTC 15m grid.

| Civil time | Offset | Unix |
|---|---|---|
| **2023-01-01 00:00:00 Europe/Brussels** | CET (UTC+1) winter | **`1672527600`** |
| Same instant UTC | 2022-12-31 23:00:00 UTC | `1672527600` |

DST later in the window (CEST, UTC+2) does **not** change the UTC bar grid. Do not re-bucket bars into “Brussels candles.” Filter `time >= 1672527600` and interpret session labels in Brussels.

Interval: **`15`** (minutes). Allowed OHLC enums: `1, 5, 15, 30, 60, 240, 1440, 10080, 21600`.

Rough UTC-aligned slot count 1672527600 → 2026-08-27 19:59 UTC ≈ **128147** fifteen-minute slots. Many may have **no trade**. That is not a listing gap.

---

## First available XRPEUR candle (real date — not 2023)

**2023-01-01 is not before listing.** Do not slide the walk-forward start.

### First print (REST `Trades`, `since=0`)

`GET https://api.kraken.com/0/public/Trades?pair=XRPEUR&since=0&count=5`

First row (`XXRPZEUR[0]`):

| | |
|---|---|
| price / volume | `0.35000000` / `0.10000000` |
| time | **`1495122667.744094`** |
| UTC | **2017-05-18 15:51:07.744094Z** |
| Europe/Brussels | **2017-05-18 17:51:07.744094+02:00** |
| side / type / `trade_id` | `b` / `l` / `1` |

### First 15m **bucket** that can hold a candle

UTC 15m floor: `1495122667 // 900 * 900` = **`1495122300`**

| | |
|---|---|
| Bar open UTC | **2017-05-18 15:45:00Z** |
| Bar open Europe/Brussels | **2017-05-18 17:45:00+02:00** |

REST `OHLC?interval=15` **cannot return this bar** (720-bar ceiling). The following 15m OHLC is **aggregated from public Trades in that bucket this sitting**, not copied from `/public/OHLC`:

`GET https://api.kraken.com/0/public/Trades?pair=XRPEUR&since=0&count=1000` → 24 prints with `1495122300 <= t < 1495123200`:

| field | value |
|---|---|
| time (bar open) | `1495122300` |
| open / high / low / close | `0.35` / `0.35` / `0.3` / `0.34` |
| volume / count | `29928.93471693` / `24` |
| last print in bucket | `1495123196.91213` (`trade_id` 24) |

That is a **trades-built** bar. Do not paste it into a file labeled “REST OHLC history.”

### REST weekly OHLC (listing-length, still not 15m)

`GET https://api.kraken.com/0/public/OHLC?pair=XRPEUR&interval=10080` → **485** weeks, first `1495065600` (2017-05-18 00:00:00Z) open `0.35000`, last 2026-08-27. **No adjacent weekly gap > 8 days** in that array. Nearest week to the walk-forward start: `1672272000` (2022-12-29 00:00:00Z), volume `34814464.53997786`, count `22765`. Evidence the **market was live** at the 2023 boundary. **Not** a 15m candle.

### 2023-01-01 boundary prints (REST `Trades`)

`since=1672527600000000000` (and the same first row with `since=1672527600` seconds — Kraken accepted both magnitudes this sitting):

| | UTC | Europe/Brussels | price |
|---|---|---|---|
| Last print **before** window | 2022-12-31 22:58:20.215530Z | 2022-12-31 23:58:20+01:00 | `0.31779` |
| First print **in** window | **2022-12-31 23:01:42.596888Z** | **2023-01-01 00:01:42.596888+01:00** | **`0.31759`** |

~102 seconds after midnight Brussels with no print is a quiet open, not a delist. Do **not** invent a 00:00:00 candle. The first **real** print in-window is 00:01:42 Brussels. The UTC 15m bar `1672527600` (2022-12-31 23:00Z) **does** contain trades (this first print is inside it). This sitting did **not** download every trade in that bar, so this file does **not** publish that bar’s OHLC.

---

## Public endpoints (exact)

Base: **`https://api.kraken.com/0`**. All of these are **public**. No key. No `API-Sign`. Do not send `x-api-key` / `x-user-key`.

Docs:

- OHLC: https://docs.kraken.com/api/docs/rest-api/get-ohlc-data
- Trades: https://docs.kraken.com/api/docs/rest-api/get-recent-trades
- FAQ (history via Trades; OHLC 720 cap): https://support.kraken.com/articles/advanced-api-faq
- Public rate limits: https://support.kraken.com/articles/206548367-what-are-the-api-rate-limits-

### 1. `GET /0/public/OHLC` — last ~7.5 days at 15m, not 2023

```
https://api.kraken.com/0/public/OHLC?pair=XRPEUR&interval=15
https://api.kraken.com/0/public/OHLC?pair=XRPEUR&interval=15&since=<unix_seconds>
```

| Rule | Wire / this sitting |
|---|---|
| `pair` | `XRPEUR` |
| `interval` | **`15`** |
| `since` | Unix **seconds**. Docs: incremental updates of **new committed** bars. **Not** a history pager. |
| Ceiling | Docs: **up to 720** most recent entries. **Older data cannot be retrieved, regardless of `since`.** |
| Last array row | Current **not-yet-committed** timeframe; always present |
| Row shape | `[time, open, high, low, close, vwap, volume, count]` |
| `result.last` | id to pass as next `since` when **polling new committed** bars |

This sitting, `interval=15` (with and without `since=1672527600` — **same window**):

| | unix | UTC | Europe/Brussels |
|---|---|---|---|
| First returned bar | `1787211900` | 2026-08-20 07:45:00Z | 2026-08-20 09:45:00+02:00 |
| Last returned bar | `1787859900` | 2026-08-27 19:45:00Z | 2026-08-27 21:45:00+02:00 |
| `n` | **721** (720 committed-scale history + current bar) | | |
| `result.last` | `1787859000` | | |

720 × 15 min = **7.5 days**. That matches the returned first bar. **`since=2023` does not walk back to 2023.** Using REST OHLC as `invert-wf-2023` history is a silent 7.5-day clip. **RED.**

Coverage at other intervals (same 720 ceiling, still public, still not 2023 15m):

| `interval` | ≈ span | First bar this sitting |
|---|---|---|
| 15 | 7.5 d | 2026-08-20 07:45Z |
| 240 | 120 d | 2026-04-29 16:00Z |
| 1440 | 720 d | 2024-09-06 00:00Z |
| 10080 | ~13.8 y | 2017-05-18 00:00Z (pair-length) |

Use `interval=15` REST OHLC only as a **tail poll** after a real history file exists.

### 2. `GET /0/public/Trades` — full history, then **you** build 15m

```
https://api.kraken.com/0/public/Trades?pair=XRPEUR&since=0
https://api.kraken.com/0/public/Trades?pair=XRPEUR&since=1672527600000000000&count=1000
```

| Rule | Wire / this sitting |
|---|---|
| `pair` | `XRPEUR` |
| `since=0` | First trade of the market (2017-05-18, above) |
| `since` | Docs/FAQ: unix **nanoseconds** (seconds + 9 digits). `result.last` is always ns. **Paginate with `last`, do not add 1.** Seconds `1672527600` returned the **same** first in-window print this sitting; still persist **`last` as returned**. |
| `count` | `1`–`1000`. Default this sitting with `since=0`: **1000**. `count=1001` → still **1000**, `error: []` (silent cap). |
| Row shape | `[price, volume, time, buy/sell, market/limit, miscellaneous, trade_id]` |
| `time` | unix **seconds** (float) |
| Without `since` | Docs: last 1000 trades (recent), **not** 2023 |

FAQ method (official): page `Trades`, then **create OHLC for any interval from time and sales**. That is the REST path for `invert-wf-2023`.

Pagination loop (public, no key):

1. `since = 1672527600000000000` (window start) or `0` (listing).
2. `GET /0/public/Trades?pair=XRPEUR&since={since}&count=1000`
3. Next `since = result.last` (string ns).
4. Stop when a trade `time` is past “now”, or `last` stops advancing.
5. Sleep **≥ 1 s** between calls (public Trades/OHLC limited **per IP and pair**).

Do not retry-spam. Support: ~1 public call/second stays inside limits; faster may throttle for seconds or longer. Errors: `EAPI:Rate limit exceeded`, `EService: Throttled: [unix]`.

This sitting did **not** walk the full 2023→now trade tape (would be many thousands of pages). Method is confirmed; a complete 15m series from Trades is **not** in this repo.

### 3. Official bulk CSVs (public Drive, no key) — preferred for 2023 bulk

Kraken support, not a third-party scrape:

| What | Support page | Drive this sitting (from that page’s HTML) |
|---|---|---|
| **OHLCVT** complete ZIP | https://support.kraken.com/articles/360047124832-downloadable-historical-ohlcvt-open-high-low-close-volume-trades-data | File https://drive.google.com/file/d/1ptNqWYidLkhb2VAKuLCxmp2OXEfGO-AP/view?usp=sharing |
| **OHLCVT** quarterly folder | same article | Folder https://drive.google.com/drive/folders/15RSlNuW_h0kVM8or8McOGOMfHeBFvFGI?usp=sharing |
| **Trades** (time & sales) complete ZIP | https://support.kraken.com/articles/360047543791-downloadable-historical-market-data-time-and-sales- | File https://drive.google.com/file/d/10zh3tDpqANYvVtYVgczwVz3UZFRUb1el/view?usp=sharing |
| **Trades** quarterly folder | same article | Folder https://drive.google.com/drive/folders/188O9xQjZTythjyLNes_5zfMEFaMbTT22?usp=sharing |

OHLCVT ZIP layout (Kraken + observed community extractors; confirm names **inside the ZIP**, do not invent a missing file):

- Intervals in the ZIP: **1, 5, 15, 30, 60, 240, 720, 1440** minutes (no 10080 in the ZIP list).
- Expected 15m filename: **`XRPEUR_15.csv`**.
- Typical rows: **no header**, columns `timestamp,open,high,low,close,volume,trades`.
- **No `vwap`** in the CSV (REST OHLC **has** `vwap`). Do not mix schemas.
- **Missing row = no trades in that interval** (Kraken’s own note). That is a **gap of prints**, not a license to synthesize OHLC.

Complete ZIP lags “now” (quarterly updates). After the last CSV timestamp, page REST `Trades` with `since=<last_csv_ts_ns>` and aggregate 15m, **or** poll REST `OHLC interval=15` only for the last 7.5 days.

Drive file IDs can rotate when Kraken re-uploads. If a link 404s, use the **support article**, not a memorized ID.

---

## How to build `invert-wf-2023` without inventing candles

**Preferred**

1. Download Kraken OHLCVT complete ZIP + every quarterly ZIP in the official folder.
2. Extract **`XRPEUR_15.csv`** from each; concat; sort; drop duplicate `timestamp`.
3. Keep rows with `timestamp >= 1672527600`.
4. **Do not** insert synthetic bars for missing timestamps.
5. Tail: REST `Trades` from last kept timestamp → now, bucket `time // 900 * 900` in UTC, OHLC from real prints only (`open` = first price, `high`/`low` = max/min, `close` = last, `volume` = sum, `count` = n). Skip empty buckets.
6. Optional freshness: REST `OHLC?pair=XRPEUR&interval=15` for the last 7.5 days; **drop the uncommitted last row** until that bar closes; do not use it to backfill 2023.

**REST-only (no ZIP)**

Page `Trades` from `since=1672527600000000000`, same aggregation. Same rule: **no empty-bar invention**.

**Forbidden**

- Treating the 721 REST 15m bars as 2023–2026 history.
- Forward-filling close into no-trade slots and calling it Kraken OHLC.
- Cross-venue XRP/EUR (Bitstamp, Binance, …) labeled as Kraken.
- USD `XRPUSD` as a EUR walk-forward.
- Backfilling `invert-paper` / fund-gate fills from these candles.
- Any private endpoint, order, or key.

---

## Known gaps (only what is evidenced)

| Gap | What it is | What it is not |
|---|---|---|
| REST OHLC 720 cap | Retrieval ceiling. `since` does not help. 15m ≈ 7.5 days. | A 2023 market halt. |
| Uncommitted last OHLC bar | Current 15m still forming. | A closed walk-forward print. |
| CSV / official OHLCVT omits empty intervals | No trades in that 15m. | A deleted listing. Do not invent the row. |
| Quiet open 2023-01-01 00:00–00:01:42 BXL | No print for ~102 s after midnight. | Pair unlisted. First in-window print is 00:01:42 BXL. |
| US XRP trading halt (Kraken blog: no later than 2021-01-29 17:00 PT) | **US residents** only. Quote: markets continue for clients **outside the United States**. | An XRPEUR delist for this EUR walk-forward. Halt is **before** 2023. |
| ZIP lag | Complete file is “history to last published quarter”; rest is quarterly + REST tail. | Live websocket history. |
| This sitting did not enumerate every empty 15m bar 2023→now | Would need the ZIP or a full Trades walk. | Permission to assume a continuous 128k-bar file. |
| Weekly REST OHLC: 485 consecutive weeks 2017-05-18 → 2026-08-27 | No **week-scale** hole in that public array. | Proof every 15m slot traded. |

**Do not invent 15m OHLC for gaps.** If a later coder needs a continuous indicator series, mark any fill-forward as **derived**, never as Kraken.

---

## Rate limits (public, no key)

https://support.kraken.com/articles/206548367-what-are-the-api-rate-limits-

- Public REST: by **IP**.
- **`Trades` and `OHLC` also by currency pair.**
- Stay at **≤ 1 request/second**.
- Private-key counter tables (Starter 15 / decay 0.33/s) are **not** this path. This research sends **no key**.

---

## RED / YELLOW / GREEN

### RED

- REST `OHLC interval=15` as the 2023→now series.
- Calling 2023-01-01 “before listing.” First print is **2017-05-18 15:51:07Z**.
- Invented candles (empty-bar OHLCV, other venues, XRPUSD, lab-clip bars).
- Feeding this into the **fund gate** or **`invert-paper`** scoreboard.
- Live, keys, orders, Phantom, shop HTML.

### YELLOW

- REST `Trades` pagination to now: correct, slow, easy to rate-limit if burst.
- `since` seconds vs nanoseconds: both worked for the 2023 boundary this sitting; **`last` is ns** — always page with `last`.
- Drive IDs can move; support articles are the durable pointer.
- Complete ZIP ≠ “through this minute”; need quarterlies + tail.
- Kraken MCP down this VM; public REST was enough and is the intended path.

### GREEN

- Query pair **`XRPEUR`**, interval **`15`**, public hosts above.
- Window start **`1672527600`** is inside a live XRPEUR market.
- First 15m bucket **2017-05-18 15:45:00Z**; walk-forward does **not** start there.
- Official method for deep history: **`/0/public/Trades`** and/or **OHLCVT `XRPEUR_15.csv`**.
- Still paper. No keys in this file.

---

## Out of scope (honoured)

- No `kraken order` / paper order / futures order
- No API keys, no private REST
- No `invert-paper` fill ping, no fund-gate score
- No reseal of `c9689f5d`, no `dca-paper` reset
- No shop / catalog HTML, no journal republish, no live

---

## Re-check (copy/paste)

```bash
curl -sS 'https://api.kraken.com/0/public/AssetPairs?pair=XRPEUR'
curl -sS 'https://api.kraken.com/0/public/OHLC?pair=XRPEUR&interval=15'
# ceiling check: since=2023 must NOT walk to 2023
curl -sS 'https://api.kraken.com/0/public/OHLC?pair=XRPEUR&interval=15&since=1672527600'
curl -sS 'https://api.kraken.com/0/public/Trades?pair=XRPEUR&since=0&count=1'
curl -sS 'https://api.kraken.com/0/public/Trades?pair=XRPEUR&since=1672527600000000000&count=1'
curl -sS 'https://api.kraken.com/0/public/OHLC?pair=XRPEUR&interval=10080'
curl -sS 'https://api.kraken.com/0/public/Time'
curl -sS 'https://api.kraken.com/0/public/SystemStatus'
```

Parse `result.XXRPZEUR` (default) or the non-`last` pair key. First trade time must stay **2017-05-18**. First REST 15m bar must stay **days**, not years, behind “now.” First in-window trade must stay **2023-01-01 00:01:42+01:00** (or a **later real** print if Kraken rewrites history — do not invent an earlier midnight candle).

**`invert-wf-2023` may start 2023-01-01 Europe/Brussels. It may not start from REST OHLC. It may not invent bars. It is not the fund gate.**
