# RESEARCH — D6 Kraken-native 15m path (not the 1-limit score)

**Seat:** RESEARCHER · Coder  
**Lens:** public Kraken market data only. Then STEAL / HYPOTHESIS. Then RED / YELLOW / GREEN.  
**Date:** 2026-08-27  
**Stamp:** VOORBEELD · paper / simulated · not FACTUUR · not INVOICE · not live-trade advice  
**HEAD (this leftover repo):** `2170952`  
**Still paper.** No orders. No keys. No live. `is_fund_gate: false`.

This file prepares **D6**: a **Kraken-native XRPEUR 15m** tape from **2023-01-01 00:00 Europe/Brussels → now**, for a **later** 1-limit invert score labeled **`KRAKEN-XRPEUR-15m`**.

It does **not** run that score. It does **not** CODE a scorer. It does **not** invent a 2023 equity curve, fill count, return, or maxDD.

**Named live score right now (elsewhere, not this memo):** **`INVERT-V2-1LIMIT`** on **`BINANCE-VISION-XRPEUR`**. That book stays the named 1-limit book until a later seat labels a Kraken run. This page is the **Kraken path only**.

---

## Locks (this sitting)

| Lock | Status |
|---|---|
| Still paper · no orders · no keys | **GREEN** |
| Not the fund gate · `is_fund_gate: false` | **GREEN** |
| Do not reseal `c9689f5d` | **GREEN** — cited, not rotated |
| Do not reset `invert-paper` | **GREEN** — fill 1 `PAPER-00029` stays |
| Do not reset `dca-paper` | **GREEN** — five BTCUSD slices stay held |
| Do not CODE a scorer in this PR | **GREEN** — docs only |
| Do not invent a 2023 equity curve | **GREEN** — none printed |
| Do not implement PLAN #196 every-fib-below-close arming | **GREEN** — PLAN is **RED** (#203). D6 is tape, not engine |
| Do not recommend Bitstamp as Kraken | **GREEN** — Bitstamp is already a **third dump** |
| Named 1-limit book stays Vision until a later labeled Kraken run | **GREEN** — this file does not steal the name `INVERT-V2-1LIMIT` |

**Lab clip (cite only):** `fib-grid-invert-xrpeur-15m` · 2026-08-18 21:00 → 2026-08-26 08:00 Europe/Brussels · 20 fills · +0.681154% · maxDD 0.890854% · vs `sha256:c9689f5d7d583320e724900b0ce4ef68193878c880d11939badd1dd59016e390`. Not this path. Not this window.

**Live `invert-paper` (do not touch):** fill 1 = `PAPER-00029` buy XRPEUR 160.64773 @ **1.24496**. Resting TP `PAPER-00030` @ 1.26778 is **not** a fill. Open `PAPER-00028` @ 1.23084 is **not** a fill. Gate (return > 0 after fees **and** ≥ 8 prints **and** maxDD ≤ 8%) is **NOT MET**.

**PLAN #196 (`PLAN-invert-wf-2023.md`) is RED** ([PR #203](https://github.com/eyeskull2220/solana-invoice/pull/203)). Do **not** implement its **every-fib-below-close** arming table. A later 1-limit score (at most one resting limit; live 00029/00030 + optional 00028 extra) is a **different** engine. D6 only says how to **get Kraken 15m bars**.

**Read first (present on sibling PRs, not leftover `main`):**

| File | PR | Use here |
|---|---|---|
| `RESEARCH-xrpeur-15m-data.md` | [#197](https://github.com/eyeskull2220/solana-invoice/pull/197) | REST vs ZIP, `XXRPZEUR`, empty-bar rule |
| `RESEARCH-xrpeur-15m-broad.md` | [#198](https://github.com/eyeskull2220/solana-invoice/pull/198) | Drive 7.3G interstitial, Bitstamp as labeled fallback, rings |
| `PLAN-invert-wf-2023.md` | [#196](https://github.com/eyeskull2220/solana-invoice/pull/196) | **RED** — clock/fees/locks may be cited; **arming table is not D6** |

Probed this sitting from public REST only (no API key, no Kraken MCP — that namespace was error / undiscoverable). Server clock: `GET /0/public/Time` → `unixtime` **1787862002** (`Thu, 27 Aug 26 20:20:02 +0000`). `GET /0/public/SystemStatus` → `online`.

---

## What D6 is / is not

| Name | Role |
|---|---|
| **D6** | Kraken-native 15m **data path** for a later 1-limit invert **score**. This file. |
| **`KRAKEN-XRPEUR-15m`** | Venue label a later scorer **must** write if it uses this tape. Not minted here. |
| **`INVERT-V2-1LIMIT` on `BINANCE-VISION-XRPEUR`** | Named 1-limit book **now**, running elsewhere. Keep it. Do not rename it Kraken. |
| **`invert-wf-2023`** | Paper walk-forward name from PLAN #196. **Not started from this PR.** Not the fund gate. |
| **`BITSTAMP-XRPEUR`** | Already-labeled **third dump** (#198). Pages 15m from 2023. **Not Kraken. Not D6.** |
| **Fund gate / `invert-paper`** | Untouched. |

Loading 2023 Kraken candles into a later engine does **not** mint `PAPER-*` fills and does **not** green the gate.

---

## 1. Exact public steps (no keys) — 2023-01-01 → now

Two Kraken-native methods. REST `OHLC interval=15` is **not** one of them.

Window start: **2023-01-01 00:00:00 Europe/Brussels** = CET UTC+1 = unix **`1672527600`** = `2022-12-31 23:00:00 UTC`. Keep bars on the **UTC 15m grid**. Do not re-bucket into “Brussels candles.”

Pair (this sitting, `GET /0/public/AssetPairs?pair=XRPEUR`):

| Field | Wire |
|---|---|
| Query `pair` | **`XRPEUR`** (altname) |
| **Result key** | **`XXRPZEUR`** |
| `wsname` | `XRP/EUR` |
| `status` | `online` |
| `pair_decimals` | 5 |
| `base` / `quote` | `XXRP` / `ZEUR` |

**Parse `result.XXRPZEUR` (or the non-`last` pair key). `result["XRPEUR"]` KeyErrors.** Optional `assetVersion=1` switches keys to display names. Default (omit) keeps `XXRPZEUR`. Do not normalize the wire key away.

First XRPEUR print (`Trades?since=0&count=1` this sitting): **2017-05-18 15:51:07.744094Z**, `trade_id` **1**, `result.last` `1495122667744093843`. 2023-01-01 is **after** listing. Do not truncate the window.

Base: **`https://api.kraken.com/0`**. Public. No `API-Sign`. No `x-api-key` / `x-user-key`.

### 1.A Forbidden simple path — REST `OHLC` (720-bar ceiling)

```
GET https://api.kraken.com/0/public/OHLC?pair=XRPEUR&interval=15
GET https://api.kraken.com/0/public/OHLC?pair=XRPEUR&interval=15&since=1672527600
```

Docs: up to **720** most recent entries. **Older data cannot be retrieved, regardless of `since`.** Last array row is the **current uncommitted** bar.

This sitting, **both** calls (with and the 2023 `since` is the same trap):

| | |
|---|---|
| Result key | **`XXRPZEUR`** |
| `n` | **721** (720 committed-scale + current bar) |
| First bar | `1787213700` = **2026-08-20 08:15:00Z** |
| Last bar | `1787861700` = **2026-08-27 20:15:00Z** |
| `result.last` | `1787860800` |
| Covers 2023? | **No** |

720 × 15 min = **7.5 days**. Using REST OHLC as D6 history is a silent last-week clip. **RED.** Use it only as a **tail poll** after a real history file exists; **drop the uncommitted last row**.

Docs: https://docs.kraken.com/api-reference/market-data/get-ohlc-data

### 1.B Path A — REST `Trades` reconstruct (keyless, live-proven, Cursor-VM native)

Official FAQ method: page **entire** time-and-sales, then **create OHLC for any interval**.

```
GET https://api.kraken.com/0/public/Trades?pair=XRPEUR&since=1672527600000000000&count=1000
```

| Rule | Wire / this sitting |
|---|---|
| `pair` | `XRPEUR` |
| Result key | **`XXRPZEUR`** |
| `since` | Unix **nanoseconds**. `result.last` is always ns. **Paginate with `last` as returned. Do not add 1.** Seconds `1672527600` also returned the 2023 boundary in sibling #197; still persist **`last`**. |
| `since=0` | First trade of the market (2017-05-18) |
| `count` | 1–**1000**. Silent cap: `count=1001` still returns 1000. |
| Row | `[price, volume, time, buy/sell, market/limit, miscellaneous, trade_id]` |
| `time` | unix **seconds** (float) |
| Without `since` | Last ~1000 **recent** trades — not 2023 |

**Loop (public, no key):**

1. `since = 1672527600000000000` (window start) or `0` (listing).
2. `GET /0/public/Trades?pair=XRPEUR&since={since}&count=1000`
3. Read trades from **`result.XXRPZEUR`**.
4. Next `since = result.last` (string ns).
5. Stop when a trade `time` is past “now”, or `last` stops advancing.
6. Sleep **1–2 seconds** between calls (see §1.D). Do not retry-spam.

**Aggregate 15m (UTC):** bucket `floor(time / 900) * 900`.

| Field | From prints in `[open, open+900)` |
|---|---|
| `open` | first trade price |
| `high` / `low` | max / min price |
| `close` | last trade price |
| `volume` | sum size |
| `trades` | count |
| `vwap` | optional size-weighted (REST OHLC has it; ZIP CSV does **not**) |

**Empty-bar rule (no invent fills):**

- Interval with **zero** trades → **omit the row** (Kraken OHLCVT’s own note: missing candlestick = no trades). That is a **gap of prints**, not a license to synthesize OHLC.
- Do **not** forward-fill `O=H=L=C=previous close` into a file labeled Kraken.
- If a later 1-limit **engine** needs a continuous 96-bar **clock** for rails, synthesized slots are **`derived: true`**, `volume=0`, `trades=0`, and **must not fill**. They are not Kraken prints. See §3.

This sitting did **not** walk the full 2023→now tape. Method is confirmed (boundary + 2023-03-24 pages). A complete 15m series is **not** in this repo and is **not** attached.

Docs:

- Trades: https://docs.kraken.com/api-reference/market-data/get-recent-trades
- FAQ (history via Trades): https://support.kraken.com/articles/advanced-api-faq
- Historical-data guide (ns `since`, 1000/call, **Trades 1–2 s**): https://docs.kraken.com/exchange/guides/general/historical-data

### 1.C Path B — official OHLCVT ZIP + quarterly folder + Trades tail

Kraken support (first-party), files on a **public Google Drive**. No Kraken account. No API key.

| What | Support | Drive this sitting |
|---|---|---|
| **OHLCVT complete ZIP** | https://support.kraken.com/articles/360047124832-downloadable-historical-ohlcvt-open-high-low-close-volume-trades-data | https://drive.google.com/file/d/1ptNqWYidLkhb2VAKuLCxmp2OXEfGO-AP/view?usp=sharing |
| **OHLCVT quarterly folder** | same article | https://drive.google.com/drive/folders/15RSlNuW_h0kVM8or8McOGOMfHeBFvFGI?usp=sharing |
| **Trades complete ZIP** (ticks, not 15m) | https://support.kraken.com/articles/360047543791-downloadable-historical-market-data-time-and-sales- | https://drive.google.com/file/d/10zh3tDpqANYvVtYVgczwVz3UZFRUb1el/view?usp=sharing |
| **Trades quarterly folder** | same | https://drive.google.com/drive/folders/188O9xQjZTythjyLNes_5zfMEFaMbTT22?usp=sharing |

Export URL (hits the virus-scan interstitial):  
`https://drive.google.com/uc?export=download&id=1ptNqWYidLkhb2VAKuLCxmp2OXEfGO-AP`

**This sitting, without unzipping 7.3G:**

| Probe | Result |
|---|---|
| Drive file title | `Kraken_OHLCVT.zip` |
| Interstitial | **“Google Drive - Virus scan warning”** · **`Kraken_OHLCVT.zip` (7.3G) is too large for Google to scan for viruses. Would you still like to download this file?** |
| Confirm | HTML confirm-token page (not a raw ZIP body) |
| Quarterly names in folder HTML | `Kraken_OHLCVT_Q{1–4}_{2023,2024,2025}.zip` **and** `Kraken_OHLCVT_Q1_2026.zip` (**13** files) |
| **Not** listed | `Q2_2026`, `Q3_2026` |

ZIP layout (support + community extractors; **`namelist` before trusting the filename**):

- Intervals in each ZIP: **1, 5, 15, 30, 60, 240, 720, 1440** minutes.
- Expected 15m member: **`XRPEUR_15.csv`**.
- Typical rows: **no header**, `timestamp,open,high,low,close,volume,trades`.
- **No `vwap`** in the CSV (REST OHLC **has** `vwap`). Do not mix schemas.
- **Missing row = no trades.** Do not invent fills.

**Steps (when a human or a later CODE seat can actually obtain the ZIP):**

1. Download complete `Kraken_OHLCVT.zip` **after** the interstitial confirm (not a silent `curl` of the 7.3G file into this leftover repo).
2. Download every quarterly ZIP listed in the official folder (`Q1_2023` … `Q1_2026` as of this probe).
3. `namelist` → extract **`XRPEUR_15.csv`** from each; concat; sort; drop duplicate `timestamp`.
4. Keep `timestamp >= 1672527600`. Drop any in-progress bar if a source includes one.
5. **Do not** insert synthetic OHLC for missing timestamps in the **Kraken-labeled** file.
6. **Tail:** last listed quarterly is **Q1 2026** (through 2026-03-31). From last kept CSV timestamp → now, page REST **Trades** (`since=<last_csv_ts_ns>`) and aggregate 15m from **real prints only**. REST `OHLC interval=15` covers only the last 7.5 days — not a multi-month tail.
7. Record `source_sha256`, first/last ts, row count, `venue: KRAKEN-XRPEUR-15m` in a MANIFEST. That checksum is a **data seal for this tape**. It is **not** a reseal of `c9689f5d`.

Drive file IDs can rotate when Kraken re-uploads. Durable pointer = **support article**, not a memorized ID.

**Do not commit the all-pairs 7.3G ZIP to git.**

### 1.D Rate limits (public, no key)

https://support.kraken.com/articles/206548367-what-are-the-api-rate-limits-  
https://docs.kraken.com/exchange/guides/general/historical-data

| Fact | Source |
|---|---|
| Public REST limited by **IP** | Support “Public (REST Market Data)” |
| **`Trades` and `OHLC` also by currency pair** | Same |
| Stay at **≤ 1 request/second** to remain inside limits | Support: “1 per second (or less)” |
| Historical-data **safe delay table** | **OHLC 1 s** · **Trades 1–2 s** · Depth 1 s |
| Same page, looser note | 100–200 ms “to avoid throttling” — **stricter table wins** |
| Support Python example | `time.sleep(3)` on error |
| Errors | `EAPI:Rate limit exceeded` · `EService: Throttled: [unix]` |

Private-key counters (Starter 15 / decay 0.33/s, Standard 20 / −0.5/s) are **not** this path. D6 sends **no key**. Trading-engine limits are **not** this path. **No orders.**

On 429 / throttle: back off (seconds, then longer). Do not retry as if it were an order. Public Trades has **no** trade-execution idempotency problem — it is a GET. Still do not hammer.

### 1.E Preferred order for D6 (Kraken only)

| Rank | Path | 2023-01-01 | Through now | Empty bars | Coder, no Kraken keys |
|---|---|---|---|---|---|
| **1** | REST `Trades` reconstruct, `XXRPZEUR`, 1–2 s | **Yes** (ticks live-proven) | **Yes** (walk `last`) | omit / `derived` clock only | **Yes from this VM** |
| **2** | Drive OHLCVT `XRPEUR_15.csv` + quarterlies + Trades tail | Expected (unzip to confirm) | **No** from ZIPs alone (tail after Q1 2026) | omit (Kraken rule) | No Kraken key; **7.3G interstitial is the blocker** |
| **Stop** | REST `OHLC interval=15` as history | No (~7.5 d) | last week only | n/a | yes, **unsatisfiable** |
| **Not D6** | `BITSTAMP-XRPEUR` `step=900` | Yes | Yes | Bitstamp’s clock | yes — **third dump, already labeled** |
| **Not D6** | Coinbase / Bitfinex / CDD Kraken URLs / Kaiko / CoinAPI / Tardis-full | see #198 | — | — | not Kraken-native |

---

## 2. What would `CROSS_VENUE` if Vision stays the named 1-limit book

**Named now:** `INVERT-V2-1LIMIT` on **`BINANCE-VISION-XRPEUR`** (running elsewhere).  
**Later labeled tape:** **`KRAKEN-XRPEUR-15m`** (this D6 path).

Those are **two books**. A later 1-limit Kraken score is a **new named artifact**. It does not inherit Vision fills, Vision holes, or the Vision seal. It does not reseal `c9689f5d`. It does not write into `invert-paper`.

`CROSS_VENUE` = treating them as one tape, or filling one book from the other, without a venue string that makes the mix **fail**.

| # | Action | Why it is `CROSS_VENUE` |
|---|---|---|
| C1 | Score 1-limit invert on Vision bars and **report `venue: KRAKEN-XRPEUR-15m`** | Wrong matching engine, wrong halt calendar, wrong fee/queue |
| C2 | Stitch Vision history + Kraken tail (or Kraken history + Vision tail) **without** a venue field | Unlabeled mix. REVIEW-05 already names this `DATA_BAD` |
| C3 | Copy Vision’s **2023-03-24** missing/halt klines onto a Kraken book as `DATA_GAP` | Binance matching-engine halt ≠ Kraken. Kraken **printed** that window (§3) |
| C4 | Fill a Kraken-labeled limit because a **Vision wick** tagged the price | Different book. Touch on A is not a print on B |
| C5 | Compare Vision `INVERT-V2-1LIMIT` fills / return / maxDD to a Kraken run **as if same book** | Cross-venue unmarked. Print two rows, two `venue` strings |
| C6 | Fill Kraken holes from **Bitstamp** (or Coinbase, XRPUSD, FX-converted USD) and keep the Kraken name | Bitstamp is the **third dump**. Hole-fill from another venue is `CROSS_VENUE` |
| C7 | Use Vision bars as **96-bar warmup rails** for a Kraken replay | Rails from the wrong pair-venue |
| C8 | Paste the already-printed close-model **9097 / −99.99% / end €1 / `BINANCE-VISION-XRPEUR`** onto a Kraken scorecard | Wrong venue; that fingerprint is a **warning**, not invert, not D6 |

**STEAL:** keep `INVERT-V2-1LIMIT` on Vision as the named 1-limit score. When a later seat runs 1-limit on D6 tape, **new** scorecard JSON:

```json
{
  "book": "invert-wf-2023",
  "score_name": "INVERT-V2-1LIMIT-KRAKEN",
  "venue": "KRAKEN-XRPEUR-15m",
  "venue_is_named_score": true,
  "is_fund_gate": false,
  "stamp": "VOORBEELD"
}
```

Do **not** reuse the Vision score name without a venue suffix. Allowed named scores for a later engine (REVIEW-05 D4, tightened here):

| `venue` | Meaning | This memo |
|---|---|---|
| `BINANCE-VISION-XRPEUR` | Vision 15m (named 1-limit **now**) | Out of scope except as the book **not** to overwrite |
| `KRAKEN-XRPEUR-15m` | D6 path (Trades reconstruct and/or OHLCVT+tail) | **This file** |
| `BINANCE-VISION-XRPEUR+KRAKEN-TAIL` | Explicit mix, only if a later PLAN names it | Not D6. Still not Bitstamp |

**Not a named score:** `BITSTAMP-XRPEUR`, Coinbase `XRP-EUR`, `XRPUSD`, unlabeled mix.

Unlabeled mix = `DATA_BAD` / `CROSS_VENUE`. Do not start CODE that “just needs 2023 bars” from #198’s Bitstamp fallback.

---

## 3. How to write the 2023-03-24 hole **on Kraken** (not Vision)

### 3.1 What 2023-03-24 is on **Vision / Binance** (context only)

Binance spot matching-engine bug (trailing-stop). Spot trading, deposits, withdrawals **temporarily suspended**.

| Clock | Event (public CZ / Binance posts) |
|---|---|
| ~**18:27 WIB** = **11:27 UTC** 2023-03-24 | Spot trading disabled |
| Engines snapshot hourly; bug at minute 57 → longer reconcile | — |
| ~**21:00 WIB** = **14:00 UTC** | Platform to function as usual (trailing stops still off) |

Vision klines for XRPEUR (and other spot symbols) may show **missing / halt / zero-trade** 15m slots across that window. That is a **Binance** hole. It is the hole the Vision-named 1-limit book must disclose **on Vision**.

**Do not copy it onto Kraken.**

### 3.2 What 2023-03-24 is on **Kraken** (this sitting — public Trades, no keys)

Kraken ACH/Silvergate funding changes around **2023-03-27** are **not** an XRPEUR spot halt. Crypto spot continued.

Public `GET /0/public/Trades?pair=XRPEUR` during the Binance halt window (result key **`XXRPZEUR`**):

| Probe (`since` unix s → first print) | UTC | price | `trade_id` |
|---|---|---|---|
| 11:20Z (pre) | 2023-03-24 **11:20:05Z** | 0.39967 | 18681440 |
| 11:27Z (halt start) | 2023-03-24 **11:28:07Z** | 0.39941 | 18681471 |
| 12:00–12:15Z **bucket** | **82 prints** in one 15m | first 0.39413 / last 0.39681 | 18681793 → 18681874 |
| 12:30Z (mid halt) | 2023-03-24 **12:30:13Z** | 0.39879 | 18681961 |
| 13:50Z (near Binance resume) | 2023-03-24 **13:50:04Z** | 0.39457 | 18682283 |
| 14:11Z (after) | 2023-03-24 **14:11:15Z** | 0.39364 | 18682371 |

**Kraken XRPEUR was printing while Binance spot was down.** A missing Vision kline at 12:00Z is **not** a Kraken `DATA_GAP`.

This sitting did **not** enumerate every 15m slot on 2023-03-24. It proved the halt window is **not empty** on Kraken. A later D6 ingest logs **Kraken** holes only: timestamps where **Kraken** OHLCVT omits a row **and** REST Trades has **zero** prints in that UTC bucket.

### 3.3 How a later Kraken ingest must write that day

| Rule | Kraken-native (`KRAKEN-XRPEUR-15m`) |
|---|---|
| Source of truth | Kraken Trades / OHLCVT for **that** bucket |
| If prints exist | Write the aggregated 15m bar. **Eligible to fill** a **pre-resting** limit (later 1-limit engine — not this PR) |
| If **no** Kraken prints | **Omit** the row in the Kraken file. Log `HOLE kraken utc=<bar_open> reason=no_trades`. Not `HOLE vision_copied` |
| Synthesized **clock** bar (only if the engine needs 96-bar rails) | `derived: true`, `open=high=low=close=previous_kraken_close`, `volume=0`, `trades=0` |
| **Synthesized clock bars must not fill** | Touch-fill against a derived flat bar is journal fraud. Skip. `SYNTH_FILL` fails the later run |
| Do not | Forward-fill and call it Kraken. Do not insert Vision halt bars. Do not insert Bitstamp bars |

PLAN #196 §3 synthesizes missing buckets so the 24h rail **clock** is continuous, and already says synthesized bars may **not** fill. Sibling #197/#198 mark inventing empty OHLC as **RED** if unlabeled. D6 lock: **Kraken file omits; derived clock is a separate series; fills never on derived.**

**HYPOTHESIS (do not apply):** treat 2023-03-24 as a global crypto halt and skip the day on Kraken so Vision and Kraken calendars match. That would **delete real Kraken prints** (82 in one 15m this sitting).

---

## 4. Bitstamp is not Kraken (already a third dump)

#198 already labeled **`BITSTAMP-XRPEUR`**: `GET https://www.bitstamp.net/api/v2/ohlc/xrpeur/?step=900&limit=1000&start=1672527600` pages 15m from the Brussels window start. Public, no key, ~1000 bars/call.

**D6 does not promote it.** It is dump **three** (Vision = 1, Kraken = 2, Bitstamp = 3). Using it as a Kraken stand-in is `CROSS_VENUE` (C6). A later CODE seat that “just needs 2023 bars” because Drive is 7.3G must use **REST Trades** (§1.B), not Bitstamp.

Do not: fill Kraken holes from Bitstamp; name a score `KRAKEN-XRPEUR-15m` on Bitstamp OHLC; average Kraken+Bitstamp closes.

---

## 5. Coder-without-keys feasibility (this Cursor VM)

Kraken MCP: **error / undiscoverable**. `kraken` CLI: not required for public GET. **No keys used.**

| Path | This VM (2026-08-27) | Verdict |
|---|---|---|
| `GET /0/public/Time`, `SystemStatus`, `AssetPairs?pair=XRPEUR` | 200, `XXRPZEUR`, `online` | **GREEN** |
| `GET /0/public/OHLC?interval=15&since=1672527600` | 721 bars, first **2026-08-20** | **GREEN** as a trap proof · **RED** as D6 history |
| `GET /0/public/Trades` pages (`since=0`, 2023-03-24 halt window, 12:00Z bucket) | 200, key `XXRPZEUR`, real prints | **GREEN** method · **YELLOW** wall-clock for a full 2023→now walk |
| Drive `uc?export=download` complete OHLCVT | **Virus-scan interstitial**, file **7.3G**, confirm token — **not** a ZIP body | **YELLOW/RED as automation** from a datacenter VM |
| Unzip `XRPEUR_15.csv` | **Not done** (would be a 7.3G download into leftover `solana-invoice`) | Not proven this sitting |
| Bitstamp OHLC | Not fetched this sitting on purpose | Already dumped in #198 |

**STEAL for a Cursor coder without keys:**

1. **Do the 2023→now history with REST Trades** at **1–2 s/page**, 1000 trades/page, persist `last`, parse `XXRPZEUR`. This VM can. Do not burst. Do not invent a page-count or a finish time here (one 2023-01-01 page in #198 was ~9.4 h of trades — **not** a lifetime rate).
2. **Do not** `curl` the 7.3G Drive file as the default from this environment. Interstitial + size + datacenter IP blocks (Concretum: scripts get blocked; they download **manually**) make it a **human/local** step, not a VM one-shot.
3. If a later CODE seat **does** obtain the ZIP on a laptop, use it as bulk 15m through last quarterly, then Trades-fill the tail. Still no Kraken keys. Still do not commit the all-pairs ZIP.
4. REST OHLC 15m remains the **incremental** feed for new **committed** bars after backfill — last 7.5 days, drop the forming candle.

**Do not download 7.3G into this PR.** Do not attach a reconstructed 15m CSV here. D6 is the **path**, not the blob.

---

## STEAL vs HYPOTHESIS

Invert recipe stays frozen. `INVERT-V2-1LIMIT` stays on Vision until a later labeled Kraken run. This table is the point of D6.

### STEAL (tape / labels — do not rewrite 1-limit rungs)

1. **D6 history = Kraken `Trades` reconstruct and/or official OHLCVT + quarterlies + Trades tail.** Not REST OHLC 720.
2. **Result key `XXRPZEUR`.** Query `pair=XRPEUR`. Paginate with `result.last` (ns). Sleep **1–2 s**.
3. **Empty Kraken interval = omit.** Missing OHLCVT row = no trades. No invent fills.
4. **Derived clock bars** (if 96-bar rails need a continuous clock) are **`derived: true`**, volume 0, **must not fill**.
5. **Venue string required.** Named 1-limit **now** = Vision. Later Kraken run = `KRAKEN-XRPEUR-15m`. Unlabeled mix = `CROSS_VENUE` / `DATA_BAD`.
6. **Write 2023-03-24 from Kraken prints.** Binance halt is Vision’s hole. Kraken printed (82 trades in 12:00–12:15Z this sitting).
7. **Bitstamp stays dump three.** Do not recommend it as Kraken.
8. **Cursor VM without keys:** Trades path is feasible; Drive 7.3G interstitial is not the default.
9. **PLAN #196 every-fib-below-close is RED.** D6 does not implement it. Later 1-limit = at most one resting limit (live 00029/00030 pattern), **later PR**.
10. **`is_fund_gate: false`.** Do not reseal `c9689f5d`. Do not reset `invert-paper` / `dca-paper`. No 2023 equity curve in this file.
11. Drop REST OHLC’s **uncommitted** last bar. Drop forming candles.

### HYPOTHESIS (would change invert / venue / gate — **not applied**)

| ID | Change | Why it is not D6 |
|---|---|---|
| H1 | Implement PLAN #196 “pair **each** buy rung below close” | **RED** fill-every-rung. 9097 fingerprint family. Not 1-limit |
| H2 | Name this memo’s tape `INVERT-V2-1LIMIT` without a venue suffix | Steals the Vision-named score |
| H3 | Fill Kraken holes from Bitstamp / Vision / XRPUSD | `CROSS_VENUE` |
| H4 | Copy Binance 2023-03-24 halt onto Kraken as `DATA_GAP` | Deletes real Kraken prints |
| H5 | Forward-fill empty 15m as Kraken OHLC and allow fills | Invented candles |
| H6 | CODE a scorer / print a 2023 return in this PR | Forbidden by the job |
| H7 | Page REST OHLC and label it 2023 | 720 cap |
| H8 | Reseal `c9689f5d` or reset `invert-paper` / `dca-paper` | Wrong books |
| H9 | Treat a later Kraken 1-limit PASS as the fund gate | Gate stays `invert-paper` until CEO says |
| H10 | Download 7.3G into leftover `solana-invoice` as “the path” | Blob ≠ path; interstitial |

Any H* that ships belongs on a **new** book / **new** hash. Not on `c9689f5d`. Not on Vision’s named score without a new venue.

---

## RED / YELLOW / GREEN

### RED

- REST `OHLC interval=15` as the 2023→now series.
- Invented candles (empty-bar OHLCV labeled Kraken, other venues as Kraken, XRPUSD, lab-clip bars).
- Bitstamp (or Vision) as `KRAKEN-XRPEUR-15m`.
- Copying the Vision/Binance 2023-03-24 hole onto Kraken.
- Filling synthesized clock bars.
- Feeding this into the **fund gate** or **`invert-paper`** scoreboard.
- Implementing PLAN #196 every-fib arming from this path memo.
- Inventing a 2023 equity curve / fill count / PASS in this file.
- Live, keys, orders, Phantom, shop HTML, reseal, `paper reset`.

### YELLOW

- REST `Trades` full walk: correct, **slow**, easy to throttle if burst. Wall-clock not estimated here.
- Drive 7.3G interstitial: official, keyless, **awkward from a Cursor VM**. IDs can move; support articles are durable.
- Complete ZIP ≠ “through this minute”; last quarterly this sitting = **Q1 2026**; need Trades tail.
- `since` seconds vs nanoseconds: both worked at the 2023 boundary in #197; **`last` is ns**.
- Kraken MCP down this VM; public REST was enough.
- PLAN synthesizes empties for clock vs “do not invent” — resolved only if `derived: true` and **no fills**.

### GREEN

- Query pair **`XRPEUR`**, result **`XXRPZEUR`**, interval **15**, public hosts above.
- Window start **`1672527600`** is inside a live XRPEUR market (first print 2017-05-18).
- D6 methods: **`/0/public/Trades` reconstruct** and/or **OHLCVT `XRPEUR_15.csv` + quarterlies + tail**.
- 2023-03-24 Kraken prints **during** the Binance halt (probed).
- Named 1-limit book **left on Vision**. This memo is Kraken path only.
- Still paper. No keys in this file. `is_fund_gate: false`.

---

## Out of scope (honoured)

- No `kraken order` / paper order / futures order  
- No API keys, no private REST  
- No scorer CODE, no 15m CSV blob, no 7.3G download into git  
- No `invert-paper` fill ping, no fund-gate score, no invented 2023 curve  
- No reseal of `c9689f5d`, no `dca-paper` / `invert-paper` reset  
- No PLAN #196 arming table  
- No shop / catalog HTML, no journal republish, no live, no FACTUUR  

**Promotion: no.** Stay paper. Gate on live `invert-paper` remains **NOT MET**. D6 is a tape path for a **later** 1-limit Kraken score — not that score.

---

## Re-check (copy/paste — public only)

```bash
# Pair key must be XXRPZEUR
curl -sS 'https://api.kraken.com/0/public/AssetPairs?pair=XRPEUR'

# Ceiling check: since=2023 must NOT walk to 2023
curl -sS 'https://api.kraken.com/0/public/OHLC?pair=XRPEUR&interval=15&since=1672527600'

# First print 2017-05-18; result key XXRPZEUR
curl -sS 'https://api.kraken.com/0/public/Trades?pair=XRPEUR&since=0&count=1'

# 2023-03-24 11:27Z — expect prints (Binance was halted; Kraken was not)
curl -sS 'https://api.kraken.com/0/public/Trades?pair=XRPEUR&since=1679657220000000000&count=3'

curl -sS 'https://api.kraken.com/0/public/Time'
curl -sS 'https://api.kraken.com/0/public/SystemStatus'

# Drive interstitial (do NOT download 7.3G):
# curl -sS -L 'https://drive.google.com/uc?export=download&id=1ptNqWYidLkhb2VAKuLCxmp2OXEfGO-AP' | rg -n '7.3G|Virus scan|Kraken_OHLCVT'

# Never:
# kraken paper reset --workspace invert-paper
# kraken paper reset --workspace dca-paper
# kraken order …
```

Parse `result.XXRPZEUR`. First trade time must stay **2017-05-18**. First REST 15m bar must stay **days**, not years, behind “now.” A 2023-03-24 11:27Z Trades page must **not** be empty if Kraken history is unchanged.

**D6 may start 2023-01-01 Europe/Brussels. It may not start from REST OHLC. It may not invent bars. It may not fill derived clock bars. It is not the fund gate. It is not `INVERT-V2-1LIMIT` on Vision. Bitstamp is not Kraken.**

---

**PII:** No personal mailbox, phone, IBAN, or invented KBO on this page. Treasury strings stay **do-not-touch** Phantom bans (`96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3`).

End. RESEARCHER. Docs only. Still paper. `is_fund_gate: false`. VOORBEELD.
