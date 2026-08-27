# PLAN — invert-wf-2023 paper walk-forward

> **Seat:** PLANNER (Coder paper lane). **This PR is docs only.** Do not implement from this file. Do not place paper or live orders. Do not reseal. Do not reset `invert-paper` or `dca-paper`.
>
> **For a later CODE seat:** after a **different** reviewer greens **this** page, implement the backtester described here. Split year slices so they can run in parallel. Combined is a separate sequential job. This book is **not** the fund gate until CEO says.

**Date:** 2026-08-27  
**Stamp:** VOORBEELD · paper / simulated · not FACTUUR · not INVOICE · not live-trade advice  
**Operator:** natural person, Geel. **KBO/BTW: nog niet toegekend.**  
**HEAD (leftover `main` at write):** `2170952`

**Goal:** A paper walk-forward **replay** of invert on **XRPEUR 15m** from **2023-01-01 00:00 Europe/Brussels** through the last **fully closed** 15m bar at CODE run time. Named book: **`invert-wf-2023`** (EUR **10000**).

**Architecture:** Clock is each closed 15m bar. No lookahead. Full fib set from rolling 24h rails. After **any** fill, swap TP/entry jobs of **those two** prices. Re-arm only on the opposite fill. Spot: no naked short. Fees on. Four independent year slices may run in parallel; combined is one sequential EUR 10000 book.

**Tech stack (later CODE):** Python 3 stdlib (csv, json, zoneinfo, hashlib, unittest). No Kraken private API. No keys. No Phantom. No new Surge host.

---

## 0. Hard locks (do not bargain)

These override every later CODE choice, every sibling RESEARCH note, and every “just this once.”

| Lock | Meaning |
| --- | --- |
| **Still paper** | Autonomy **level 2**. No `kraken order`. No `kraken futures order`. No `--validate` then live. No API keys in git, HTML, JSON, screenshots, or chat. |
| **No Phantom** | No send, swap, rebalance, perps, or bot against `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3` or Base `0x9eb954b567ef3616424a6e1bf42c63724930aa54`. Sales-USDC is not trading float. |
| **No live Kraken** | Public historical OHLCVT / public ticker only. Kraken MCP may be down; that is not permission to go live or to CLI live. |
| **No reseal** | Cite `sha256:c9689f5d7d583320e724900b0ce4ef68193878c880d11939badd1dd59016e390`. Do not rotate, rewrite, or restamp it as this walk-forward. Lab clip ≠ this book. |
| **No reset `invert-paper`** | Fill **1** `PAPER-00029` buy XRPEUR **160.64773 @ 1.24496** stays. Resting TP `PAPER-00030` sell LIMIT @ **1.26778** stays. Open `PAPER-00028` buy LIMIT @ **1.23084** stays. Do not flatten, cancel, or “clean” that book. |
| **No reset `dca-paper`** | Five BTCUSD slices stay held. Not this book. Not the gate. |
| **Not the fund gate until CEO says** | Fund gate remains **`invert-paper` only** (return > 0 after fees **and** ≥ 8 prints **and** maxDD ≤ 8%). `invert-wf-2023` is a **named research book**. A pretty 2023–2026 curve does **not** promote live. A later CEO page must name it as the gate, or it never is. |
| **No second journal domain** | Do **not** publish `invert-wf-2023.surge.sh` or any new Surge host. Scorecards live as markdown/JSON in this git tree. Existing journal stays `https://dca-paper-journal.surge.sh/` — this PLAN does not patch it. |
| **VOORBEELD if any page** | Any HTML or markdown report stamps **VOORBEELD**. Never FACTUUR / INVOICE. Identity: natural person, Geel. **KBO/BTW: nog niet toegekend.** |
| **XRPEUR only** | This book does not add pairs. Allowlist expansion is WAIT. No memecoins. No sleeve mix. |

**Retired hashes stay retired:** `2bfb1b68` fill-every-rung · `9056f296` entry-waits-TP · `094513` arming-only (99 fills PASS on that old hash is not live, not this book).

---

## 1. What this book is / is not

| Object | Role |
| --- | --- |
| **`invert-wf-2023`** | New **paper replay** book. EUR 10000. XRPEUR 15m invert. Window 2023-01-01 00:00 Europe/Brussels → last closed 15m bar. |
| **`invert-paper`** | **Fund-gate book.** Fill 1. Still NOT MET. Untouched by this PLAN and by later CODE. |
| **Lab clip `c9689f5d`** | Sealed 8-day lab (2026-08-18 21:00 → 2026-08-26 08:00 BXL). 20 fills · +0.681154% · maxDD 0.890854% · PASS. **Cite. Do not reseal.** Not this window. Not funding proof. |
| **`dca-paper`** | USD hold. Five slices. Leave running. |
| **3x sleeve** | Separate FAIL book. Never mix PnL. |
| **Slice scorecards 2023 / 2024 / 2025 / 2026-to-now** | Parallel **diagnostics**. Each starts flat EUR 10000 at slice open. **Do not sum them** and call it the book. |
| **Combined scorecard** | The named-book curve: **one** sequential EUR 10000 from 2023-01-01 through now. |

`invert-paper` gate (unchanged, still NOT MET):

1. Return > 0 after fees  
2. Fills ≥ 8 (`PAPER-*` **prints**; resting is not a fill)  
3. maxDD ≤ 8%

Live operator book (do not touch):

| Id | Role | Price | Gate fill? |
| --- | --- | --- | --- |
| **PAPER-00029** | FILL 1 · buy 160.64773 XRPEUR | **1.24496** | **Yes. Count = 1.** |
| **PAPER-00030** | Resting TP · sell LIMIT 160.64773 | **1.26778** | No |
| **PAPER-00028** | Open buy LIMIT 162.49066 | **1.23084** | No |

This PLAN does not ping the journal. This PLAN does not count 00030/00028. This PLAN does not add 20+1.

---

## 2. Window and slices (Europe/Brussels)

All civil datetimes are **Europe/Brussels** (CET/CEST). Convert with `zoneinfo.ZoneInfo("Europe/Brussels")`. Do not assume UTC+1 year-round.

| Slice id | Start (inclusive) | End (exclusive) | Parallel? |
| --- | --- | --- | --- |
| `2023` | 2023-01-01 00:00 | 2024-01-01 00:00 | Yes |
| `2024` | 2024-01-01 00:00 | 2025-01-01 00:00 | Yes |
| `2025` | 2025-01-01 00:00 | 2026-01-01 00:00 | Yes |
| `2026` | 2026-01-01 00:00 | last **fully closed** 15m bar at CODE run | Yes |
| `combined` | 2023-01-01 00:00 | last **fully closed** 15m bar at CODE run | **No** — one sequential process |

Start of book in UTC: `2022-12-31 23:00:00 UTC` (Brussels is CET that night).

**Warmup (lookback, not lookahead):** each slice (and combined) may read **96 closed 15m bars** immediately **before** slice start to seed 24h rails. Warmup bars **must not** fill, must not accrue fees, must not count toward fills. If bars are missing, fail the slice with `DATA_GAP` rather than inventing a swing from the future.

**Independent slices:** each starts **flat**, cash **EUR 10000**, no inherited XRP, no inherited resting orders, no inherited invert pair. That is what makes them parallel.

**Combined:** one cash pile, one inventory, one set of resting pairs, carried across year boundaries. CODE may implement combined as one process over the full CSV. CODE may **not** implement combined as `sum(slice returns)` or `mean(slice maxDD)`.

---

## 3. Data (public, no keys)

Kraken REST `GET /0/public/OHLC` returns **at most ~720** candles. For 15m that is ~7.5 days. **It cannot source 2023–2026.** Using `since` does not lift that cap. CODE that pages OHLC and claims a 2023 book is a **stop**.

**Source of record:** Kraken **downloadable historical OHLCVT** (public ZIP, no account):

- Docs: https://support.kraken.com/ch/articles/360047124832-downloadable-historical-ohlcvt-open-high-low-close-volume-trades-data  
- Interval file: **15-minute** CSV for pair **XRPEUR** (Kraken filename as shipped in the ZIP; do not invent a second pair).

**CODE data job:**

1. Download the public ZIP (or the XRPEUR 15m member if shipped separately).  
2. Extract **only** XRPEUR 15m. Do not commit the all-pairs ZIP.  
3. Filter rows to warmup-start → last closed bar.  
4. Write `paper/invert-wf-2023/data/XRPEUR_15m.csv` **or** a fetch script plus `SHA256SUMS`. Prefer a fetch script + checksums if the CSV is large; if committed, keep it XRPEUR-only.  
5. Record `source_sha256`, row count, first ts, last ts in `data/MANIFEST.json`. That checksum is a **data seal for this replay**. It is **not** a reseal of `c9689f5d`.

**Bar schema (after parse):**

```text
ts_utc       int     # unix seconds, bar OPEN
ts_bxl       str     # ISO-8601 with offset, Europe/Brussels
open, high, low, close  decimal strings as Kraken sent (do not float-round on ingest)
volume       decimal
trades       int     # if present; else 0
closed       true    # drop the in-progress candle if a source includes it
```

**Empty intervals:** Kraken OHLCVT omits buckets with no trades. CODE **synthesizes** missing 15m buckets so the clock is continuous: `open=high=low=close=previous close`, `volume=0`, `trades=0`. Synthesized bars may **not** fill (no print in the bucket). They **do** advance the 24h rail window.

**No lookahead on ingest:** sort by `ts_utc` ascending. Reject a row whose open is after a later row. Drop any bar with `high < max(open,close)` or `low > min(open,close)` as `DATA_BAD` (fail the run; do not “fix” OHLC).

---

## 4. Invert engine (the recipe)

Copy the live lock language. Do not revive retired hashes.

> 15m. Full fib set: **rails** + retracements **0.236 / 0.382 / 0.5 / 0.618 / 0.786** + extensions **1.272 / 1.618 / 2.0 / 2.618** **both sides**. Every level is a rung. After **ANY** fill, swap jobs of **those two** prices: **TP becomes next entry, entry becomes next TP**. Re-arm only on the opposite fill. Spot: **no naked short**. After sell-TP you are **flat cash**; next entry is **buy-back**.

### 4.1 Rails (24h, closed bars only)

Live invert-paper latched TP `PAPER-00030` at **24h H** (1.26778). This replay uses the same rail idea on 15m bars.

For bar `i` (the bar **being evaluated**, already closed):

```text
H[i] = max(high[j] for j in i-96 .. i-1)   # prior 96 closed bars = 24h
L[i] = min(low[j]  for j in i-96 .. i-1)
R[i] = H[i] - L[i]
```

- If fewer than 96 closed bars exist (even with warmup), skip fills until rails exist.  
- **Do not** include bar `i` in its own rails. That would let this bar’s high invent the TP that this bar then fills.  
- If `R[i] <= 0`, skip fib refresh this bar (no new rungs). Existing frozen pairs still evaluate.

### 4.2 Full fib set (both sides)

Let `H, L, R` be the rails. Deduplicate rungs by rounding to **XRPEUR tick 1e-5** (five decimal places, matching 1.24496 / 1.26778 / 1.23084).

**Rails:** `L`, `H`

**Retracements from H (down):** `H - r * R` for `r` in `{0.236, 0.382, 0.5, 0.618, 0.786}`  
**Retracements from L (up):** `L + r * R` for the same `r`

**Extensions above H:** `H + (e - 1) * R` for `e` in `{1.272, 1.618, 2.0, 2.618}`  
**Extensions below L:** `L - (e - 1) * R` for the same `e`

That is the full set. Both sides. Every unique tick is a rung.

### 4.3 Lot size (quote)

Match invert-paper fill 1: **EUR 200 quote per rung** (live cost `199.99999794` @ 1.24496 → qty `160.64773`).

```text
CLIP_QUOTE_EUR = 200
qty = CLIP_QUOTE_EUR / limit_price
```

Starting cash **10000**. Never buy more quote than `cash` after the **primary** fee haircut. Never sell more XRP than `xrp_held`.

### 4.4 Pair invert (not fill-every-rung)

Retired `2bfb1b68` filled every rung. This book does **not**.

A **lot** is two prices `(entry, tp)` plus side state:

| Field | Meaning |
| --- | --- |
| `p_entry` | current entry job |
| `p_tp` | current TP job |
| `qty` | XRP size of this lot |
| `state` | `flat_waiting_buy` \| `long_waiting_sell` |
| `frozen` | true once the two prices are latched for this lot |

**Arming (flat, spot):**

- Only **buy** limits. Never a sell while `xrp_held == 0`.  
- Candidate buy rungs = fib set strictly **below** bar `i-1` close (last known close before this bar).  
- Pair each buy rung `E` with a TP `T` = the **next higher** unique rung in the same fib set (`T > E`). If no higher rung, skip that candidate.  
- Do **not** arm a second lot at the same `E` while one lot already waits there.  
- Cash cap: sum of working buy notionals + held cost basis + primary fees must stay ≤ cash. Skip extra rungs rather than lever.

**Swap jobs (spot, locked — do not invent a short):**

The recipe says: after **any** fill, **those two prices** swap jobs (TP becomes next entry, entry becomes next TP), and **re-arm only on the opposite fill**. Sleeve 3x may flip long↔short. **This spot book may not.** After sell-TP you are **flat cash**; next entry is **buy-back**.

A naive swap that sells `Lo` while long, or that shorts `Hi` after the TP, is a **naked short / scratch**. Forbidden.

Live invert-paper after fill 1: long from **1.24496**, TP sell at **1.26778** (24h H), and a **different** lower buy still working at **1.23084**. Buy-back is not “buy the high you just sold.” Re-arm of **1.24496** waits on the opposite fill (the TP).

**Locked pairing:**

- A lot is always a **lower** price `Lo` and a **higher** price `Hi` (`Lo < Hi`).  
- **Flat:** entry job = **buy `Lo`**, TP job = **sell `Hi`**. Only the buy is armed.  
- **Long (after buy `Lo`):** working order = **sell `Hi`**. Do **not** re-arm buy `Lo` until that sell fills. Other unfilled buy rungs at **different** prices may stay (00028 pattern).  
- **After sell `Hi`:** flatten to cash. **Now** re-arm **buy `Lo`** (opposite fill happened). Geometric pair stays `Lo`/`Hi`. Do not open a short. Do not buy `Hi` as a breakout on this spot book.

**Operational table CODE implements:**

| Event | Working orders | Re-arm of the filled price |
| --- | --- | --- |
| Flat | buy limits at fib rungs `< last close`, each paired with next-higher rung as future TP | n/a |
| Buy fills at `Lo` | cancel duplicate buys at `Lo`; arm **sell `Hi`** for that qty; **leave other unfilled buy rungs** (00028 pattern) | **Forbidden until sell `Hi` fills** |
| Sell `Hi` fills | flatten that lot; cash increases; **now** re-arm **buy `Lo`** (the opposite price). Do **not** open a short. | Buy-back at `Lo`, TP still `Hi` — the two prices keep their **geometric** roles; **jobs** swap in the sense that the just-filled TP (`Hi`) is no longer working, and the old entry (`Lo`) becomes the next entry again after the opposite fill |

**“Swap TP/entry jobs” on spot, operationally:** the filled price **stops** being the working order; the **other** price **becomes** the working order. Re-arm the filled price **only** after that opposite fill. That is the whole invert. Do not pyramid the same `Lo`. Do not sell `Lo` while long (that would be a scratch at entry). Do not sell `Hi` without inventory.

**Same-bar rule:** at most **one** fill **per lot** per bar. The newly armed opposite order **does not fill on the same bar**. Other lots may fill the same bar if cash/inventory allow. **Global:** never sell more XRP than held. Apply fills in this order:

1. For each **long** lot, if `Hi` is in `[low, high]`, fill the sell at `Hi`.  
2. Then, for each **flat** lot / candidate, if `Lo` is in `[low, high]` and cash allows, fill the buy at `Lo`.  
3. Newly swapped / newly latched orders skip this bar.

Fill price = **limit** (maker). Not the close. Not the high/low extreme beyond the limit.

### 4.5 No lookahead

Illegal:

- Reading bar `i+1` while evaluating `i`  
- Using bar `i` high/low to **build** rails that bar `i` then fills (rails use `i-96..i-1` only)  
- Filling the post-swap order on the same bar  
- Backfilling fills from a live ticker tag  
- Treating the in-progress candle as closed

Legal:

- Using O/H/L/C of bar `i` **after it is closed** to test whether a **pre-existing** limit sits inside `[low, high]`  
- Lookback warmup **before** the slice

### 4.6 Fees

User lock for **this** book (matches invert-paper journal shadow columns on a EUR 200 clip: `0.26=0.52; 0.40=0.80; 0.80 taker=1.60`):

| Column | Rate per fill | Role |
| --- | --- | --- |
| **Primary (default)** | **0.26%** | Scorecard return, cash, maxDD, “after fees.” This PLAN’s default. Journal calls the 0.26 column out even when labelled maker on this page. |
| **Shadow 0.40** | 0.40% | Report only. Does not change fills or inventory. |
| **Shadow 0.80 taker** | 0.80% | Report only. Worst-case taker haircut. |

Fee on a fill: `rate * (qty * fill_price)` in EUR. Primary fee **debits cash** (buy: extra EUR out; sell: less EUR in). Shadows are **parallel ledgers** on the same fills: recompute cash path at 0.40 and 0.80 without changing qty or fill times.

Do **not** also apply Kraken live maker 0.16% as a fourth column unless a later CEO page asks. Do **not** relabel 0.26% as “proof of maker fills.” Paper limits here fill at the limit; live books can still take.

Round-trip primary = two 0.26% events. Gate-style “return after fees” on **this** book uses **primary**. Shadows print beside it.

### 4.7 Equity and maxDD

At each bar close:

```text
equity = cash + xrp_held * close
peak   = max(peak, equity)
dd     = (peak - equity) / peak     # 0 if peak == 0
maxDD  = max(maxDD, dd)
```

Start: cash=10000, xrp=0, peak=10000, maxDD=0.

**Return after fees (primary):** `(final_equity / 10000) - 1`.  
Mark-to-market is allowed **inside** equity (XRP marked at close) **after** primary fees on fills. Do not report “return before fees.” Do not drop fees because the engine is simulated.

---

## 5. Scorecard (per slice + combined)

Each run writes JSON **and** a VOORBEELD markdown table. Same schema.

```json
{
  "book": "invert-wf-2023",
  "slice": "2023",
  "stamp": "VOORBEELD",
  "pair": "XRPEUR",
  "interval": "15m",
  "tz": "Europe/Brussels",
  "start": "2023-01-01T00:00:00+01:00",
  "end_exclusive": "2024-01-01T00:00:00+01:00",
  "start_cash_eur": 10000,
  "clip_quote_eur": 200,
  "fee_primary": 0.0026,
  "fills": 0,
  "return_after_fees_primary": 0.0,
  "max_dd": 0.0,
  "max_dd_vs_8pct": "at_or_under|over",
  "shadow_return_0_40": 0.0,
  "shadow_return_0_80": 0.0,
  "end_cash_eur": 0.0,
  "end_xrp": 0.0,
  "end_equity_eur": 0.0,
  "bars_replayed": 0,
  "synthesized_empty_bars": 0,
  "data_sha256": "",
  "is_fund_gate": false,
  "notes": [
    "Not the fund gate until CEO says.",
    "invert-paper fill 1 stays. Do not reseal c9689f5d."
  ]
}
```

**Required printed columns (markdown):**

| Slice | Fills | Return after fees (0.26) | Return shadow 0.40 | Return shadow 0.80 | maxDD | maxDD vs 8% |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| 2023 | | | | | | |
| 2024 | | | | | | |
| 2025 | | | | | | |
| 2026-to-now | | | | | | |
| **combined** | | | | | | |

Fills = count of **prints** (buys and sells). Resting at end-of-slice is not a fill. A round trip is **two** fills.

`maxDD vs 8%` is a **comparison flag**, not a promotion. Combined maxDD **over** 8% does not reset invert-paper. Combined maxDD **under** 8% with return > 0 and fills ≥ 8 still does **not** become the fund gate until CEO says.

**Fail the run (no fake GREEN):** `DATA_GAP`, `DATA_BAD`, `LOOKAHEAD`, `NAKED_SHORT`, `SAME_BAR_REARM`, `TOUCHED_INVERT_PAPER`, `TOUCHED_DCA_PAPER`.

---

## 6. Later CODE — files and parallel jobs

This PLAN PR creates **only** this markdown file. CODE (later PR) lands the tree below. Do not put the engine in leftover `index.html` / `catalog.html`. Do not deploy to Surge.

```text
paper/invert-wf-2023/
  README.md                 # VOORBEELD; points at this PLAN; not the gate
  SHA256SUMS                # data + scorecard hashes
  data/
    MANIFEST.json
    fetch_xrpeur_15m.py     # public OHLCVT only
    XRPEUR_15m.csv          # optional if size allows; else fetch + checksum
  src/
    __init__.py
    bars.py                 # parse, synthesize empties, tz
    fib.py                  # rails + full set
    lots.py                 # arm / fill / swap / no naked short
    fees.py                 # 0.26 primary + 0.40/0.80 shadows
    replay.py               # bar-close loop, no lookahead
    scorecard.py            # JSON + markdown
  tests/
    test_no_lookahead.py
    test_no_naked_short.py
    test_swap_rearm.py
    test_fees.py
    test_slice_isolation.py
    test_combined_not_sum.py
  out/
    2023.json
    2024.json
    2025.json
    2026.json
    combined.json
    SCORECARD.md            # VOORBEELD table
```

**CLI (CODE):** run as scripts from repo root (hyphenated book folder is **not** a Python package name):

```bash
python paper/invert-wf-2023/src/replay.py --slice 2023 --data paper/invert-wf-2023/data/XRPEUR_15m.csv
python paper/invert-wf-2023/src/replay.py --slice 2024 --data paper/invert-wf-2023/data/XRPEUR_15m.csv
python paper/invert-wf-2023/src/replay.py --slice 2025 --data paper/invert-wf-2023/data/XRPEUR_15m.csv
python paper/invert-wf-2023/src/replay.py --slice 2026 --data paper/invert-wf-2023/data/XRPEUR_15m.csv
python paper/invert-wf-2023/src/replay.py --slice combined --data paper/invert-wf-2023/data/XRPEUR_15m.csv
python paper/invert-wf-2023/src/scorecard.py --out paper/invert-wf-2023/out/SCORECARD.md
```

The four year commands **may run in parallel** (separate processes, separate `out/{year}.json`). `combined` waits for data only, **not** for slice JSON. Combined **replays the bars itself**.

**Interfaces CODE must keep stable:**

```python
def fib_rungs(h: str, l: str) -> list[str]:
    """Unique tick-rounded rungs: rails + retracements + extensions, both sides."""

def rails(bars: list[Bar], i: int) -> tuple[str, str]:
    """H, L from bars[i-96:i] (exclude i)."""

def on_bar(state: BookState, bar: Bar) -> BookState:
    """Evaluate fills on this closed bar, then refresh unfilled buys from new rails."""

def replay(bars: list[Bar], start_ts: int, end_ts_exclusive: int) -> Scorecard:
    """Slice window. Warmup bars before start_ts seed rails only."""
```

Use **decimal strings or `decimal.Decimal`**. Do not accumulate EUR in binary float.

---

## 7. CODE tasks (later — not this PR)

Checkbox tracking for the CODE seat. This PLAN PR leaves them unchecked.

### Task 1 — Data ingest (no keys)

- [ ] Fetch public XRPEUR 15m OHLCVT. Write MANIFEST + sha256.  
- [ ] Synthesize empty buckets. Drop in-progress bar. Brussels tz.  
- [ ] Test: sorted, continuous 15m, no future bars, `DATA_BAD` on inverted OHLC.  
- [ ] Commit fetch script + checksums. Do not commit the all-pairs ZIP.

### Task 2 — Fib rungs

- [ ] Implement full set §4.2. Dedup to 1e-5.  
- [ ] Test: `H=2, L=1` produces rails 1 and 2, retracement 1.5, both-side extensions, no duplicates.  
- [ ] Test: rails for bar `i` ignore `bars[i].high`.

### Task 3 — Lots / invert / spot

- [ ] Buy only when flat-or-adding with cash. Sell only when `xrp_held >= qty`.  
- [ ] After buy: arm sell `Hi`; do not re-arm that `Lo` until sell fills.  
- [ ] After sell: flatten; re-arm buy `Lo` only.  
- [ ] Same-bar: no fill of the newly armed opposite.  
- [ ] Test: attempting a sell with 0 XRP raises `NAKED_SHORT` and does not change cash.  
- [ ] Test: buy then same-bar hit of `Hi` does **not** fill the sell.

### Task 4 — Fees and shadows

- [ ] Primary 0.26% hits cash. Shadows 0.40 / 0.80 are parallel returns.  
- [ ] Test: EUR 200 buy @ 1.24496 → primary fee 0.52 (as journal).  
- [ ] Test: shadows do not change `fills` or `qty`.

### Task 5 — Slice replay (parallel)

- [ ] `--slice 2023|2024|2025|2026` writes `out/{slice}.json` only.  
- [ ] Warmup 96 bars, no warmup fills.  
- [ ] Test: 2023 process does not open or write `out/2024.json`.  
- [ ] Test: two slices can run as two processes without a shared mutable book.

### Task 6 — Combined + scorecard

- [ ] `--slice combined` one sequential EUR 10000.  
- [ ] Test: `combined.return != 2023.return + 2024.return + …` unless a documented coincidence (assert **not equal as a rule**; if equal, print `COINCIDENCE` and still refuse to *define* combined as the sum).  
- [ ] Write `out/SCORECARD.md` VOORBEELD with §5 table. `is_fund_gate: false`.  
- [ ] Cite `c9689f5d` full hash in the scorecard footer. Do not reseal.

### Task 7 — Hygiene (must stay green)

- [ ] `rg` the CODE PR for `kraken order`, `futures order`, API-key fields, Phantom send: **zero**.  
- [ ] No new Surge host. No journal HTML patch unless a **different** Coder journal ticket says ping `PAPER-00029` — that ticket is **not** this backtester.  
- [ ] No writes under operator workspaces `invert-paper` / `dca-paper` / `fib-paper` / `grid-paper`.  
- [ ] No shop/catalog HTML. No FACTUUR title.

---

## 8. Sequence

1. **This PR** — merge this markdown only.  
2. **A different reviewer** — scores **this file**. GREEN only if no red/yellow on: still paper · not the gate until CEO · invert-paper fill 1 stays · no reseal · no `dca-paper` reset · parallel slices + honest combined · no second journal domain · VOORBEELD · no Phantom / no live Kraken / no keys. If RED, rewrite this page. Do not start CODE.  
3. **CODE** — later PR, tree in §6, tasks in §7. Still paper. Still not the gate.

Sibling RESEARCH agents (XRPEUR 15m data, invert walk-forward method, 2023 slice, 2024–26 slices) do **not** edit these locks. If research finds the OHLCVT ZIP layout differs, CODE follows the public ZIP and records it in `MANIFEST.json`. It does not change invert-paper.

---

## 9. Attacks this PLAN already refuses

| Attack | Stop |
| --- | --- |
| Treat combined PASS as fund gate | Gate stays `invert-paper` until CEO names a change |
| Add clip fills into `c9689f5d` (20+n) | Cite seal; this book has its own scorecard |
| Reset invert-paper to match the replay | Fill 1 stays |
| Reset dca-paper for a clean EUR book | Stay held |
| Page REST OHLC and claim 2023 history | Use OHLCVT ZIP |
| Same-bar TP after buy | Forbidden |
| Naked short after sell-TP | Flat cash; buy-back only |
| Sum four slice returns | Combined is a sequential replay |
| Extra pairs to fatten fills | XRPEUR only |
| New Surge journal | Markdown in git only |
| Live CLI because MCP is dead | Still paper |
| Keys in MANIFEST / CSV headers | Public data only |
| Patch dca-paper-journal HTML from this ticket | Out of scope |
| Sleeve PnL blended in | Separate FAIL book |

---

## 10. This PR (PLAN only)

| Did | Did not |
| --- | --- |
| Wrote the CODE contract for `invert-wf-2023` | Implement replay, fetch data, place orders |
| Locked slice parallelism vs sequential combined | Name this book the fund gate |
| Locked invert recipe, 24h rails, EUR 200 clip, fee 0.26 + shadows 0.40/0.80 | Reseal `c9689f5d` |
| Locked invert-paper fill 1 and dca-paper hold | Reset either book |
| Locked VOORBEELD, no second journal domain, no Phantom, no live Kraken, no keys | Shop HTML, mail, KBO, Surge publish |

**Next seat:** a **different** reviewer scores this file. Then CODE. Not this run.

---

**PII:** No personal mailbox, phone, IBAN, or invented KBO on this page. Treasury strings stay listed only as **do-not-touch** Phantom bans.

End. Still paper. `invert-wf-2023` is not the fund gate until CEO says. invert-paper fill 1 stays. Do not reseal `c9689f5d`. Do not reset `dca-paper`.
