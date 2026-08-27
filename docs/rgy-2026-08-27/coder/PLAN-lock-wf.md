# PLAN lock — invert-wf-2023 (designs out #203 red/yellow)

**Seat:** FIX (Coder PLAN). **This PR is docs only.** Do not implement from this file. Do not place paper or live orders. Do not reseal. Do not reset `invert-paper` or `dca-paper`. **Do not start CODE.**

**Date of this page:** 2026-08-27
**File:** `docs/rgy-2026-08-27/coder/PLAN-lock-wf.md`
**Stamp:** VOORBEELD · paper / simulated · not FACTUUR · not INVOICE · not live-trade advice
**Operator:** natural person, Geel. **KBO/BTW: nog niet toegekend.** **Operator is not the freelancer.**
**HEAD (leftover `main` at write):** `2170952`

**This file is the PLAN lock** for the paper walk-forward book **`invert-wf-2023`**. It is **not** a rewrite of [PR #196](https://github.com/eyeskull2220/solana-invoice/pull/196). Teammates read **this lock** for the engine. #196’s operational arming table is **retired**.

RED in [PR #203](https://github.com/eyeskull2220/solana-invoice/pull/203) (`REVIEW-05-plan-wf.md`) because #196 kept the GREEN book slogans, then told CODE to **pair each fib below close** and could deploy the **whole EUR 10000 book**. That is fill-every-rung (`2bfb1b68`) plus 100% equity in aggregate. Coder already printed the grind: **fills 9097 / −99.99% / end €1** on **`BINANCE-VISION-XRPEUR`**. invert-v2 day0 is still **FAIL (−41%, 7923 fills)**. Neither print is invert. This page designs those reds (and the yellows) out. It does not licence CODE.

SovereignForge is **one Belgian income machine**. Paper lane: **`invert-paper` is the fund gate** (fill **1** stays). **`invert-wf-2023` is a 15m walk-forward from 2023, not the gate.** Still paper.

**Goal (later CODE, after a different reviewer greens this page):** a paper walk-forward **replay** of invert on **XRPEUR 15m** from **2023-01-01 00:00 Europe/Brussels** through the last **fully closed** 15m bar. Named book: **`invert-wf-2023`** (EUR **10000**). **One invert pair only.** Hard clip **EUR 200**. Grind fingerprint **fails the run**.

**Tech stack (later CODE):** Python 3 stdlib (csv, json, zoneinfo, hashlib, unittest). No Kraken private API. No keys. No Phantom. No new Surge host.

---

## 0. The reds and yellows — designed out

|#203 hole | Design-out on this page |
| --- | --- |
| **R1** Operational arming is fill-every-rung (`2bfb1b68` in a trench coat): pair each buy rung below close; other lots may fill the same bar | **§4.** ONE invert pair. Do **not** pair every fib below close. At most **one** resting limit. Optional second is live-like **PAPER-00028 extra only if named**, not 14 pairs. |
| **R2** This PLAN would still produce the 9097 / −99.99% / end €1 grind family | **§7.** A run with grind fingerprint (thousands of fills, fees ≈ capital, end ~1) **FAILS**. Do not publish as invert. Cite 9097 and invert-v2 day0 7923 as **warnings**, not scores. |
| **R3** Do not start CODE from #196 | **§11.** Sequence is this lock → different reviewer → CODE. **This PR does not start CODE.** |
| **Y1** Clip is not hard against 100% deploy (`min(200, cash)`, 50 × 200 lots) | **§5.** Hard clip **EUR 200 per fill**. Not 100% equity. Not the whole book. Skip when cash cannot pay 200 + primary fee. Never shrink. Never leftover-cash size. |
| **Y2** Venue unlabeled; Vision-on-disk unnamed; Bitstamp not banned as named score | **§3.** Named score venue: **`BINANCE-VISION-XRPEUR`** or later **`KRAKEN-TRADES` / `KRAKEN-OHLCVT`**. **Not Bitstamp as the named score.** `venue` required. |
| **Y3** Synthesized empty bars unlabeled as derived | **§3.** Synthesized rows are `derived: true`. Rails may use them for **clock**. Fills forbidden. Do not write them into a file labeled as Kraken OHLCVT verbatim. |
| **Y4** “Swap jobs” vs geometric Lo/Hi (naive short) | **§4.** After fill, swap those **two** prices. Re-arm filled price **only** on opposite fill. Spot: after sell `Hi`, next armed order is **buy `Lo` only**. Never sell while flat. |

GREEN for this PLAN pack requires those holes closed **and** the keeps in §1. Scoring this page GREEN is not permission to start CODE, not a fund-gate conversion, and not a reseal.

---

## 1. GREENS kept (from PLAN-invert-wf-2023 #196)

PR #203 already listed these as GREEN slogans. **Do not bargain them away.** The rewrite changes the **arming table**, not these locks.

### G1 — Named book, not the gate

`invert-wf-2023`, EUR **10000**, XRPEUR 15m, 2023-01-01 00:00 Europe/Brussels → last **fully closed** 15m bar. **Not** the fund gate until CEO says. Gate remains **`invert-paper` only** (return > 0 after fees **and** ≥ 8 prints **and** maxDD ≤ 8%). `is_fund_gate: false`. Combined maxDD vs 8% is a **flag**, not promotion. A pretty 2023–2026 curve does **not** promote live.

### G2 — invert-paper fill 1 stays

| Id | Role | Price | Gate fill? |
| --- | --- | --- | --- |
| **PAPER-00029** | FILL 1 · buy 160.64773 XRPEUR | **1.24496** | **Yes. Count = 1.** |
| **PAPER-00030** | Resting TP · sell LIMIT 160.64773 | **1.26778** | No |
| **PAPER-00028** | Open buy LIMIT 162.49066 | **1.23084** | No |

Do not flatten, cancel, or “clean” that book. Do not add 20+1. Resting is not a fill. This PLAN does not ping the journal.

### G3 — No reseal · no `dca-paper` reset

Cite `sha256:c9689f5d7d583320e724900b0ce4ef68193878c880d11939badd1dd59016e390`. Lab clip (name `fib-grid-invert-xrpeur-15m`, 20 fills · +0.681154% · maxDD 0.890854% · 2026-08-18 21:00 → 2026-08-26 08:00 BXL · PASS) ≠ this walk-forward. Do not rotate, rewrite, or restamp it. Five BTCUSD slices on `dca-paper` stay held. Not this book. Not the gate.

**Retired hashes stay retired in name and in the arming table:** `2bfb1b68` fill-every-rung · `9056f296` entry-waits-TP · `094513` arming-only (99 fills PASS on that old hash is not live, not this book).

### G4 — Clock: 15m bar-close, no lookahead, rails `i-96..i-1`

```text
H[i] = max(high[j] for j in i-96 .. i-1)   # prior 96 closed bars = 24h
L[i] = min(low[j]  for j in i-96 .. i-1)
R[i] = H[i] - L[i]
```

Do **not** include bar `i` in its own rails. Do not read `i+1`. Warmup 96 bars seed rails only (no fills, no fees). `DATA_GAP` rather than invent a future swing. Fill price = **limit** inside `[low, high]`, not the close, not beyond the limit. Newly armed opposite **skips this bar**. Brussels tz via `zoneinfo`, not UTC+1 year-round. Start of book UTC: `2022-12-31 23:00:00Z`. If `R[i] <= 0`, skip fib refresh this bar (no new rungs). Existing frozen pair still evaluates.

The 9097 run was a **close-model**. This clock is the correct one. **Keep it.**

### G5 — Invert job rule (prose) · no naked short

After **any** fill: the **other** of those two prices becomes the working order; **re-arm the filled price only on the opposite fill**. Spot: **no naked short**. After sell-TP: flat cash; next entry is **buy-back**. Same-bar re-arm forbidden (`SAME_BAR_REARM`). Sleeve 3x FAIL (6 fills, −2.729078%, maxDD 5.326685%) is a **different book**. Never mix.

Keep the prose. The **arming table** in §4 is what #196 got wrong.

### G6 — Fees 0.26 primary + 0.40 / 0.80 shadows · clip **number** 200

Primary hits cash. Shadows are parallel ledgers on the same fills (no extra qty, no extra fill times). Round-trip primary = two 0.26% events. Journal check: EUR 200 @ 1.24496 → primary fee **0.52**. Do not add a fourth 0.16% maker column unless CEO asks. Do not relabel 0.26 as proof of live maker fills.

The **number** 200 stays. The **hardness** of that number is §5 (was Y1).

### G7 — Combined is sequential, not the sum

Year slices 2023 / 2024 / 2025 / 2026-to-now may run **in parallel**, each flat EUR 10000 at slice open (diagnostics). **Combined** is one cash pile, one inventory, one invert pair, 2023-01-01 → now. CODE may not define combined as `sum(slice returns)` or `mean(slice maxDD)`. `test_combined_not_sum.py` stays. Coincidence still must not *define* combined as the sum.

### G8 — Still paper · hygiene

Autonomy **level 2**. No `kraken order`. No `kraken futures order`. No `--validate` then live. No keys in git, HTML, JSON, screenshots, or chat. No Phantom send, swap, rebalance, perps, or bot against `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3` or Base `0x9eb954b567ef3616424a6e1bf42c63724930aa54`. Sales-USDC is not trading float. No new Surge host (`invert-wf-2023.surge.sh` forbidden). Scorecards in git as markdown/JSON. Existing journal stays `https://dca-paper-journal.surge.sh/` — this PLAN does not patch it. VOORBEELD. Fail the run on `TOUCHED_INVERT_PAPER` / `TOUCHED_DCA_PAPER`. No shop HTML. XRPEUR only. Allowlist expansion is WAIT. No memecoins. No sleeve mix.

**Operator is not the freelancer.** Team delivers. This paper book is not a hire-me desk and not a day-rate.

---

## 2. What this book is / is not

| Object | Role |
| --- | --- |
| **`invert-wf-2023`** | New **paper replay** book. EUR 10000. XRPEUR 15m invert. Window 2023-01-01 00:00 Europe/Brussels → last closed 15m bar. **Not the fund gate.** |
| **`invert-paper`** | **Fund-gate book.** Fill 1. Still NOT MET. Untouched by this PLAN and by later CODE. |
| Lab clip `c9689f5d` | Sealed 8-day lab. **Cite. Do not reseal.** Not this window. Not funding proof. |
| **`dca-paper`** | USD hold. Five slices. Leave running. |
| 3x sleeve | Separate FAIL book. Never mix PnL. |
| **9097-fill** (`BINANCE-VISION-XRPEUR`) | Fill-every-rung close-model. **Not invert.** Warning. |
| **invert-v2 day0** | **FAIL (−41%, 7923 fills).** Not invert. Not this book. Not the gate. |
| Slice scorecards 2023 / 2024 / 2025 / 2026-to-now | Parallel **diagnostics**. Each starts flat EUR 10000. **Do not sum them.** |
| Combined scorecard | The named-book curve: **one** sequential EUR 10000 from 2023-01-01 through now. |

`invert-paper` gate (unchanged, still NOT MET):

1. Return > 0 after fees
2. Fills ≥ 8 (`PAPER-*` **prints**; resting is not a fill)
3. maxDD ≤ 8%

---

## 3. Data and named score venue

Kraken REST `GET /0/public/OHLC` returns **at most ~720** candles. For 15m that is ~7.5 days. **It cannot source 2023–2026.** Using `since` does not lift that cap. CODE that pages OHLC and claims a 2023 book is a **stop**.

### Named score venues (required)

Scorecard JSON **must** carry `venue`. Allowed named scores **only**:

| `venue` | Meaning |
| --- | --- |
| **`BINANCE-VISION-XRPEUR`** | Binance Vision XRPEUR history (the tape already named on the 9097 warning). Kraken public tail may close the last 15m bars; the **named score string stays this**. |
| **`KRAKEN-TRADES`** | Later path: Kraken public trades, aggregated to 15m. |
| **`KRAKEN-OHLCVT`** | Later path: official Kraken downloadable historical OHLCVT ZIP (15-minute XRPEUR member) + Kraken tail after ZIP lag. |

**Not the named score:** `BITSTAMP-XRPEUR`, Bitstamp, Coinbase, XRPUSD, or any stand-in, even if a sibling page can page it from 2023. Cross-venue mix without a venue string = `DATA_BAD`. Unlabelled Vision pasted onto a Kraken scorecard = `DATA_BAD`.

Data sha256 is a **replay seal** for this book. It is **not** a reseal of `c9689f5d`.

CODE may read Vision already on disk **or** later fetch Kraken TRADES / OHLCVT. Do not page REST OHLC and call it 2023. Do not require Bitstamp because a ZIP is large.

### Bar schema (after parse)

```text
ts_utc       int     # unix seconds, bar OPEN
ts_bxl       str     # ISO-8601 with offset, Europe/Brussels
open, high, low, close  decimal strings as the venue sent (do not float-round on ingest)
volume       decimal
trades       int     # if present; else 0
closed       true    # drop the in-progress candle
derived      bool    # true iff synthesized empty bucket
venue        str     # one of the three named-score strings
```

**Empty intervals:** a source may omit buckets with no trades. CODE **synthesizes** missing 15m buckets so the clock is continuous: `open=high=low=close=previous close`, `volume=0`, `trades=0`, **`derived: true`**. Synthesized bars may **not** fill (no print in the bucket). They **do** advance the 24h rail window. Do not write derived rows into a file labeled as Kraken OHLCVT verbatim. MANIFEST counts `synthesized_empty_bars`.

**No lookahead on ingest:** sort by `ts_utc` ascending. Reject a row whose open is after a later row. Drop any bar with `high < max(open,close)` or `low > min(open,close)` as `DATA_BAD` (fail the run; do not “fix” OHLC).

**CODE data job (later PR, not this one):**

1. Bind **one** named venue. Write it into `data/MANIFEST.json` and every scorecard.
2. Filter rows to warmup-start → last closed bar.
3. Write `paper/invert-wf-2023/data/XRPEUR_15m.csv` **or** a fetch script plus `SHA256SUMS`. Prefer fetch + checksums if the CSV is large; if committed, keep it XRPEUR-only.
4. Record `source_sha256`, `venue`, row count, first ts, last ts. That checksum is a **data seal for this replay**, not a reseal of `c9689f5d`.
5. Do not commit an all-pairs ZIP.

---

## 4. Invert engine — ONE pair (not a ladder)

Copy the live lock language. Do not revive retired hashes.

> 15m. Full fib set: **rails** + retracements **0.236 / 0.382 / 0.5 / 0.618 / 0.786** + extensions **1.272 / 1.618 / 2.0 / 2.618** **both sides**. After **ANY** fill, swap jobs of **those two** prices. Re-arm only on the opposite fill. Spot: **no naked short**. After sell-TP you are **flat cash**; next entry is **buy-back**.

The full fib set is the **menu**. It is **not** a stack of lots. Retired `2bfb1b68` filled every rung. **This book does not.** Do not pair every fib below close.

### 4.1 Lot count (lock)

```text
MAX_RESTING_LIMITS     = 1    # default: at most one resting limit
PAPER_00028_EXTRA      = named only
MAX_OPEN_BUY_LOTS      = 1 + (1 if run names extra=true else 0)
                          # never 14, never "each fib", never "all rungs below close"
```

**Default:** ONE invert pair. At most **one** resting limit.

**Optional second:** live-like **PAPER-00028 extra** — **at most one** additional buy at a **lower** unique rung than `Lo` — **only if the run names** `paper_00028_extra: true` in the scorecard / CLI. If unnamed, extra is **off**. A third buy is forbidden. Fourteen pairs is forbidden.

**Fail the run:** `FILL_EVERY_RUNG` if more than `MAX_OPEN_BUY_LOTS` distinct buy prices fill in any rolling 96-bar window without intervening opposite fills that free those lots. `LADDER_ARM` if CODE arms more buy prices than `MAX_OPEN_BUY_LOTS`.

### 4.2 Working pair

A **lot** is two prices `(Lo, Hi)` plus side state. `Lo < Hi`. Tick = XRPEUR **1e-5**.

| Field | Meaning |
| --- | --- |
| `p_lo` / `p_hi` | geometric pair (do not flip into a short) |
| `qty` | XRP size of this lot |
| `state` | `flat_waiting_buy` \| `long_waiting_sell` |
| `frozen` | true once the two prices are latched for this lot |

**Pick (flat, at bar close of `t`, eligible from `t+1`):**

- `Lo` = nearest buy-eligible rung **strictly below** last **closed** close, from the current 96-bar fib set.
- `Hi` = **24h rail `H[i]`** (live `PAPER-00030` pattern), **not** “next higher unique retracement.” Adjacent-fib TP is a fee mill (gross often < 0.52% round-trip). Forbidden.
- If `Hi <= Lo`, skip. Wait. Do not drop to the next fib as a substitute TP.
- If no buy-eligible rung below close, wait.
- Only **buy** limits while flat. Never a sell while `xrp_held == 0`.

**Full fib set (menu, both sides)** — unique ticks from `H, L, R`:

- Rails: `L`, `H`
- Retracements from H (down): `H - r * R` for `r` in `{0.236, 0.382, 0.5, 0.618, 0.786}`
- Retracements from L (up): `L + r * R` for the same `r`
- Extensions above H: `H + (e - 1) * R` for `e` in `{1.272, 1.618, 2.0, 2.618}`
- Extensions below L: `L - (e - 1) * R` for the same `e`

Deduplicate at tick 1e-5. **Arm at most one `Lo` from that set** (plus optional named 00028 extra). Do not arm extensions-below as a stack.

### 4.3 Operational table (CODE implements this, not #196’s ladder)

| Inventory | Armed | Not armed |
| --- | --- | --- |
| Flat | **one** buy LIMIT at `Lo` | every other buy; any sell |
| Optional extra (00028), **only if named** | **at most one** additional buy at a **lower** unique rung than `Lo`, only if cash still covers **200 + fee** after the first lot | a third buy; “pair each remaining rung”; 14 pairs |
| Long (after buy `Lo`) | sell LIMIT at `Hi` for that qty; named extra unfilled buy may stay | re-arm `Lo`; pyramid; sell `Lo`; buy `Hi` breakout |

**After any fill — those two prices:**

| Event | Working order | Re-arm of the filled price |
| --- | --- | --- |
| Buy fills at `Lo` | cancel duplicate buys at `Lo`; arm **sell `Hi`** for that qty | **Forbidden until sell `Hi` fills** |
| Sell `Hi` fills | flatten that lot; cash increases; **now** re-arm **buy `Lo`** | Buy-back at `Lo`, TP still `Hi`. Geometric roles stay. **No short.** |

**“Swap TP/entry jobs” on spot, operationally:** the filled price **stops** being the working order; the **other** price **becomes** the working order. Re-arm the filled price **only** after that opposite fill. That is the whole invert.

Do not pyramid the same `Lo`. Do not sell `Lo` while long (scratch at entry). Do not sell `Hi` without inventory. Do not buy `Hi` as a breakout on this spot book.

**After sell `Hi`, the next armed order is buy `Lo` only** — never sell `Lo`, never sell `Hi` with 0 XRP, never buy `Hi`. If a naive swap would rest a sell while flat, **discard the short** (`NAKED_SHORT` fails the run if CODE does it anyway).

Live invert-paper after fill 1 is the pattern: long from **1.24496**, TP sell at **1.26778** (24h H), and a **different** lower buy still working at **1.23084** only as the optional named extra. Buy-back is not “buy the high you just sold.” Re-arm of **1.24496** waits on the opposite fill (the TP).

---

## 5. Hard clip EUR 200 — not 100% equity

Match invert-paper fill 1: **EUR 200 quote per fill** (live cost `199.99999794` @ 1.24496 → qty `160.64773`).

```text
CLIP_QUOTE_EUR = 200
fee = CLIP_QUOTE_EUR * 0.0026
if cash < CLIP_QUOTE_EUR + fee: skip   # do not shrink, do not "use the rest"
qty = CLIP_QUOTE_EUR / limit_price     # not cash/price, not equity/price
```

**Never:**

- 100% of equity
- the whole book deployed as `floor(cash/200)` lots
- last-lot leftover-cash sizing `min(200, cash)`
- a fill whose quote notional is not 200

Starting cash **10000**. Never buy more quote than `cash` after the **primary** fee haircut — **by skipping**, not by shrinking the clip. Never sell more XRP than `xrp_held`.

**Fail the run:** `FULL_EQUITY_SIZE` if any print’s quote notional differs from 200 by more than one tick of cost (pair decimals 5). Last-lot “use the rest” is this fail.

### Fees (kept from G6)

| Column | Rate per fill | Role |
| --- | --- | --- |
| **Primary (default)** | **0.26%** | Scorecard return, cash, maxDD, “after fees.” |
| **Shadow 0.40** | 0.40% | Report only. Does not change fills or inventory. |
| **Shadow 0.80 taker** | 0.80% | Report only. Worst-case taker haircut. |

Fee on a fill: `rate * (qty * fill_price)` in EUR. Primary fee **debits cash** (buy: extra EUR out; sell: less EUR in). Shadows are **parallel ledgers** on the same fills.

---

## 6. Touch at P · armed t eligible t+1 · causal swing · same-bar skip

### 6.1 Fill rule

A limit is **resting** at the open of bar `b` only if it was armed at the close of some bar `u` with `u < b`.

| Side | Touch | Fill price | Not a fill |
| --- | --- | --- | --- |
| Buy LIMIT at `P` | `low[b] <= P` | **`P`** (not the low, not the close) | `low[b] > P`; arm bar; market-at-close |
| Sell LIMIT at `P` | `high[b] >= P` | **`P`** (not the high, not the close) | `high[b] < P`; arm bar; market-at-close |

**Armed at close of `t` → eligible from `t+1`.** Never from bar `t`. Forming bar dropped.

**Gap-through:** if `open[b]` is already through `P` (buy: `open[b] < P`; sell: `open[b] > P`) **and** the touch inequality still holds, count a fill at **`P`** on the default column, and **also** record a gap shadow at `open[b]`. Do not skip the default column.

Close-model (fill at close / full remaining cash) is **not** this book. A fill whose price is the bar **close** is `CLOSE_MODEL` and **fails the run**.

### 6.2 Same-bar both-sides = skip, not a round-trip

A 15m candle with `low <= Lo` and `high >= Hi` does **not** prove the path. OHLC has no path.

**If a bar could touch both `Lo` and `Hi` of the same lot, fill neither.** Flag `DUAL_TOUCH_SKIP`. Do not credit a round-trip inside one 15m candle.

Global fills on one bar ≤ current armed lots (already capped by §4.1). Never sell more XRP than held. Newly swapped / newly latched orders skip this bar (`SAME_BAR_REARM`).

Evaluate in this order **only when dual-touch is not true for that lot**:

1. For the **long** lot, if `Hi` is in `[low, high]`, fill the sell at `Hi`.
2. Then, for the **flat** lot / named extra, if `Lo` is in `[low, high]` and cash allows **EUR 200 + fee**, fill the buy at `Lo`.
3. Newly swapped / newly latched orders skip this bar.

### 6.3 Causal swing — no future high

Illegal:

- Reading bar `i+1` while evaluating `i`
- Using bar `i` high/low to **build** rails that bar `i` then fills (rails use `i-96..i-1` only)
- `H = max(high)` over the whole year / whole slice / whole 2023–2026 file, then placing January rungs from that high
- 24h high that includes the still-open bar or a future day
- Mixing XRPUSD / BTC rails onto XRPEUR
- Filling the post-swap order on the same bar
- Backfilling fills from a live ticker tag
- Treating the in-progress candle as closed
- Repainting swings (zigzag last-pivot that moves as new bars arrive)

Legal:

- Using O/H/L/C of bar `i` **after it is closed** to test whether a **pre-existing** limit sits inside `[low, high]`
- Lookback warmup **before** the slice
- Rolling 24h rails from **prior** 96 closed bars

If a later CODE seat uses swing objects (not only the 96-bar window): confirmation is **`N = 8`** (eight 15m bars = 2 hours), closed-bar, right-lag. A candidate high at `i` confirms at close of `i+8` iff it remains strictly greater than `high[i+1]…high[i+8]`. Symmetric for lows. Unconfirmed last pivot **does not exist**. Rails at time `t` use only swings whose **confirmation close ≤ t**. `N` is locked. Not grid-searched on 2023+.

**`DATA_GAP` rather than invent a future swing.**

---

## 7. Grind fingerprint FAILS the run

**9097-fill was fill-every-rung, not invert.** invert-v2 day0 is still **FAIL (−41%, 7923 fills)**. Neither is this book. Neither is the fund gate. Do not publish either as invert.

Coder close-model already printed on **`BINANCE-VISION-XRPEUR`**:

| | |
| --- | --- |
| Fills | **9097** |
| Return | **−99.99%** |
| End | **€1** |
| Fingerprint | fill-every-rung · 100% equity · no clip · fill at close / full remaining cash |

`(1 - 0.0026)^9097` on full remaining notional is the €1 fingerprint. Missing positions are recoverable; **this curve is not a strategy.**

If a slice or combined prints **any** of:

- thousands of fills **and** fees ≈ capital **and** end equity ~ **€1**
- end equity **≤ €100** with fills **≥ 1000**
- return after fees primary **≤ −50%** with fills **≥ 1000**
- a fill whose price is the bar **close** (close-model)
- fill count on one bar **> MAX_OPEN_BUY_LOTS** buys (ladder sweep)
- fill count on a single calendar year **≥ 5000** without a documented, named extra that still respects §4.1 (9097 / 7923 class)

then write `GRIND_FINGERPRINT` / `CLOSE_MODEL` / `FILL_EVERY_RUNG` as appropriate and **do not** publish a GREEN-looking SCORECARD. Cite **9097 / −99.99% / end €1 / BINANCE-VISION-XRPEUR** and **invert-v2 day0 FAIL (−41%, 7923 fills)** as the warnings this kill is for. Those prints are **not** this book’s score.

A grind SCORECARD that still says `book: invert-wf-2023` without the fail code is a **stop**.

---

## 8. Window, slices, equity

All civil datetimes are **Europe/Brussels** (CET/CEST). Convert with `zoneinfo.ZoneInfo("Europe/Brussels")`.

| Slice id | Start (inclusive) | End (exclusive) | Parallel? |
| --- | --- | --- | --- |
| `2023` | 2023-01-01 00:00 | 2024-01-01 00:00 | Yes |
| `2024` | 2024-01-01 00:00 | 2025-01-01 00:00 | Yes |
| `2025` | 2025-01-01 00:00 | 2026-01-01 00:00 | Yes |
| `2026` | 2026-01-01 00:00 | last **fully closed** 15m bar at CODE run | Yes |
| `combined` | 2023-01-01 00:00 | last **fully closed** 15m bar at CODE run | **No** — one sequential process |

Start of book in UTC: `2022-12-31 23:00:00 UTC`.

**Independent slices:** each starts **flat**, cash **EUR 10000**, no inherited XRP, no inherited resting orders, no inherited invert pair.

**Combined:** one cash pile, one inventory, one invert pair, carried across year boundaries. CODE may implement combined as one process over the full CSV. CODE may **not** implement combined as `sum(slice returns)`.

At each bar close:

```text
equity = cash + xrp_held * close
peak   = max(peak, equity)
dd     = (peak - equity) / peak     # 0 if peak == 0
maxDD  = max(maxDD, dd)
```

Start: cash=10000, xrp=0, peak=10000, maxDD=0.

**Return after fees (primary):** `(final_equity / 10000) - 1`. Mark-to-market is allowed **inside** equity (XRP marked at close) **after** primary fees on fills. Do not report “return before fees.”

---

## 9. Scorecard (per slice + combined)

Each run writes JSON **and** a VOORBEELD markdown table. Same schema.

```json
{
  "book": "invert-wf-2023",
  "slice": "2023",
  "stamp": "VOORBEELD",
  "pair": "XRPEUR",
  "interval": "15m",
  "tz": "Europe/Brussels",
  "venue": "BINANCE-VISION-XRPEUR",
  "venue_is_named_score": true,
  "paper_00028_extra": false,
  "max_resting_limits": 1,
  "max_open_buy_lots": 1,
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
  "fail_codes": [],
  "notes": [
    "Not the fund gate until CEO says.",
    "invert-paper fill 1 stays. Do not reseal c9689f5d.",
    "9097-fill was fill-every-rung, not invert.",
    "invert-v2 day0 FAIL (−41%, 7923 fills) is not this book."
  ]
}
```

`venue` must be one of `BINANCE-VISION-XRPEUR` | `KRAKEN-TRADES` | `KRAKEN-OHLCVT`. Missing venue, or `BITSTAMP-XRPEUR`, refuses the scorecard (`DATA_BAD`).

**Required printed columns (markdown):**

| Slice | Venue | Fills | Return after fees (0.26) | Return shadow 0.40 | Return shadow 0.80 | maxDD | maxDD vs 8% | Fail codes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 2023 | | | | | | | | |
| 2024 | | | | | | | | |
| 2025 | | | | | | | | |
| 2026-to-now | | | | | | | | |
| **combined** | | | | | | | | |

Fills = count of **prints** (buys and sells). Resting at end-of-slice is not a fill. A round trip is **two** fills. `DUAL_TOUCH_SKIP` is not a fill.

`maxDD vs 8%` is a **comparison flag**, not a promotion. Combined maxDD **over** 8% does not reset invert-paper. Combined maxDD **under** 8% with return > 0 and fills ≥ 8 still does **not** become the fund gate until CEO says.

**Fail the run (no fake GREEN):** `DATA_GAP`, `DATA_BAD`, `LOOKAHEAD`, `NAKED_SHORT`, `SAME_BAR_REARM`, `DUAL_TOUCH_SKIP` (when CODE credited a round-trip anyway), `TOUCHED_INVERT_PAPER`, `TOUCHED_DCA_PAPER`, `FILL_EVERY_RUNG`, `LADDER_ARM`, `FULL_EQUITY_SIZE`, `GRIND_FINGERPRINT`, `CLOSE_MODEL`, `FUTURE_HIGH`.

---

## 10. Later CODE — files (not this PR)

This PLAN lock creates **only** this markdown file. CODE (later PR, after a **different** reviewer greens **this** page) lands the tree below. Do not put the engine in leftover `index.html` / `catalog.html`. Do not deploy to Surge. **Do not start CODE from this PR. Do not start CODE from #196.**

```text
paper/invert-wf-2023/
  README.md                 # VOORBEELD; points at this PLAN lock; not the gate
  SHA256SUMS                # data + scorecard hashes
  data/
    MANIFEST.json           # venue required
    fetch_xrpeur_15m.py     # public Vision or later Kraken TRADES/OHLCVT only
    XRPEUR_15m.csv          # optional if size allows; else fetch + checksum
  src/
    __init__.py
    bars.py                 # parse, synthesize empties (derived), tz
    fib.py                  # rails + full set (menu, not lots)
    lots.py                 # ONE pair / fill / swap / no naked short
    fees.py                 # 0.26 primary + 0.40/0.80 shadows
    replay.py               # bar-close loop, no lookahead
    scorecard.py            # JSON + markdown; grind fails the run
  tests/
    test_no_lookahead.py
    test_no_naked_short.py
    test_swap_rearm.py
    test_fees.py
    test_slice_isolation.py
    test_combined_not_sum.py
    test_not_fill_every_rung.py
    test_clip_is_200.py
    test_tp_is_rail_h.py
    test_grind_fingerprint.py
    test_venue_label.py
    test_dual_touch_skip.py
    test_armed_t_eligible_t1.py
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
python paper/invert-wf-2023/src/replay.py --slice 2023 \
  --venue BINANCE-VISION-XRPEUR \
  --data paper/invert-wf-2023/data/XRPEUR_15m.csv
# --paper-00028-extra is OFF unless named
python paper/invert-wf-2023/src/replay.py --slice combined \
  --venue BINANCE-VISION-XRPEUR \
  --data paper/invert-wf-2023/data/XRPEUR_15m.csv
python paper/invert-wf-2023/src/scorecard.py --out paper/invert-wf-2023/out/SCORECARD.md
```

The four year commands **may run in parallel**. `combined` waits for data only, **not** for slice JSON. Combined **replays the bars itself**.

**Interfaces CODE must keep stable:**

```python
def fib_rungs(h: str, l: str) -> list[str]:
    """Unique tick-rounded rungs: rails + retracements + extensions, both sides. Menu, not lots."""

def rails(bars: list[Bar], i: int) -> tuple[str, str]:
    """H, L from bars[i-96:i] (exclude i). No future high."""

def on_bar(state: BookState, bar: Bar) -> BookState:
    """Evaluate fills on this closed bar. Do not refresh a ladder of unfilled buys."""

def replay(bars: list[Bar], start_ts: int, end_ts_exclusive: int) -> Scorecard:
    """Slice window. Warmup bars before start_ts seed rails only."""
```

Use **decimal strings or `decimal.Decimal`**. Do not accumulate EUR in binary float.

### CODE tasks (later — not this PR)

Checkbox tracking for the CODE seat. This PLAN lock leaves them unchecked.

#### Task 1 — Data ingest (no keys)

- [ ] Bind one named venue (`BINANCE-VISION-XRPEUR` or later `KRAKEN-TRADES` / `KRAKEN-OHLCVT`). Write MANIFEST + sha256.
- [ ] Synthesize empty buckets as `derived: true`. Drop in-progress bar. Brussels tz.
- [ ] Test: sorted, continuous 15m, no future bars, `DATA_BAD` on inverted OHLC, refuse `BITSTAMP-XRPEUR` as named score.
- [ ] Commit fetch script + checksums. Do not commit an all-pairs ZIP.

#### Task 2 — Fib rungs (menu)

- [ ] Implement full set §4.2. Dedup to 1e-5.
- [ ] Test: `H=2, L=1` produces rails 1 and 2, retracement 1.5, both-side extensions, no duplicates.
- [ ] Test: rails for bar `i` ignore `bars[i].high` (no future high).

#### Task 3 — ONE pair / invert / spot

- [ ] Default `MAX_RESTING_LIMITS = 1`. Named 00028 extra only if flagged.
- [ ] Buy only when flat-or-named-extra with cash for **200 + fee**. Sell only when `xrp_held >= qty`.
- [ ] After buy: arm sell `Hi` = 24h `H`; do not re-arm that `Lo` until sell fills.
- [ ] After sell: flatten; re-arm buy `Lo` only.
- [ ] Same-bar: dual-touch → `DUAL_TOUCH_SKIP`; no fill of the newly armed opposite.
- [ ] Test: a bar whose range covers the whole fib set fills **at most** `MAX_OPEN_BUY_LOTS` buys, not every rung.
- [ ] Test: attempting a sell with 0 XRP raises `NAKED_SHORT` and does not change cash.
- [ ] Test: buy then same-bar hit of `Hi` does **not** fill the sell; dual-touch fills **neither**.

#### Task 4 — Fees, clip, grind

- [ ] Primary 0.26% hits cash. Shadows 0.40 / 0.80 are parallel returns.
- [ ] Test: EUR 200 buy @ 1.24496 → primary fee 0.52 (as journal).
- [ ] Test: no print quote ≠ 200; cash leftover is skipped, not sized.
- [ ] Test: synthetic 100% equity / close-model / 9097-class path raises `GRIND_FINGERPRINT` / `CLOSE_MODEL` / `FULL_EQUITY_SIZE`.
- [ ] Shadows do not change `fills` or `qty`.

#### Task 5 — Slice replay (parallel)

- [ ] `--slice 2023|2024|2025|2026` writes `out/{slice}.json` only.
- [ ] Warmup 96 bars, no warmup fills.
- [ ] Test: 2023 process does not open or write `out/2024.json`.

#### Task 6 — Combined + scorecard

- [ ] `--slice combined` one sequential EUR 10000.
- [ ] Test: `combined.return != 2023.return + 2024.return + …` as a rule.
- [ ] Write `out/SCORECARD.md` VOORBEELD with §9 table. `is_fund_gate: false`. `venue` required.
- [ ] Cite `c9689f5d` full hash in the scorecard footer. Do not reseal.
- [ ] Grind fail codes block a GREEN-looking table.

#### Task 7 — Hygiene (must stay green)

- [ ] `rg` the CODE PR for `kraken order`, `futures order`, API-key fields, Phantom send: **zero**.
- [ ] No new Surge host. No journal HTML patch unless a **different** Coder journal ticket says ping `PAPER-00029` — that ticket is **not** this backtester.
- [ ] No writes under operator workspaces `invert-paper` / `dca-paper` / `fib-paper` / `grid-paper`.
- [ ] No shop/catalog HTML. No FACTUUR title. No freelancer / hire-me / day-rate on this book.

---

## 11. Sequence

1. **This PR** — merge this markdown only. **Do not start CODE.**
2. **A different reviewer** — scores **this file**. GREEN only if no red and no yellow on the bar in §13. If RED, rewrite this page. **Do not start CODE.**
3. **CODE** — later PR, tree in §10. Still paper. Still not the gate. Still not a reseal. Still not a `dca-paper` reset.

Sibling RESEARCH agents (XRPEUR 15m data, invert walk-forward method, 2023 slice, 2024–26 slices) do **not** edit these locks. If research finds the OHLCVT ZIP layout differs, CODE follows the public ZIP, labels `venue: KRAKEN-OHLCVT`, and records it in `MANIFEST.json`. It does not change invert-paper. It does not take Bitstamp as the named score.

**Do not start CODE from #196.** That PLAN’s arming table is retired.

---

## 12. Attacks this PLAN already refuses

| Attack | Stop |
| --- | --- |
| Treat combined PASS as fund gate | Gate stays `invert-paper` until CEO names a change |
| Pair every fib below close | Retired `2bfb1b68`. ONE invert pair. `FILL_EVERY_RUNG` / `LADDER_ARM` |
| Deploy the whole 10000 as 50 × 200 lots | Hard clip 200; skip; `FULL_EQUITY_SIZE` |
| Adjacent-fib TP (fee mill) | `Hi` = 24h rail `H`, not next retracement |
| Same-bar round-trip | `DUAL_TOUCH_SKIP`. Fill neither. |
| Close-model fills | `CLOSE_MODEL`. Fail the run. |
| Publish 9097 / 7923 as invert | `GRIND_FINGERPRINT`. Do not publish. |
| Named score on Bitstamp | `DATA_BAD`. Venue lock §3. |
| Future high of the year as rails | `FUTURE_HIGH` / `LOOKAHEAD`. Rails `i-96..i-1` only. |
| Add clip fills into `c9689f5d` (20+n) | Cite seal; this book has its own scorecard |
| Reset invert-paper to match the replay | Fill 1 stays |
| Reset dca-paper for a clean EUR book | Stay held |
| Page REST OHLC and claim 2023 history | Use named venue archive |
| Naked short after sell-TP | Flat cash; buy-back only |
| Sum four slice returns | Combined is a sequential replay |
| Extra pairs to fatten fills | XRPEUR only |
| New Surge journal | Markdown in git only |
| Live CLI because MCP is dead | Still paper |
| Keys in MANIFEST / CSV headers | Public data only |
| Patch dca-paper-journal HTML from this ticket | Out of scope |
| Sleeve PnL blended in | Separate FAIL book |
| Operator-as-freelancer copy | Operator is not the freelancer |

---

## 13. Bar for GREEN (this PLAN lock)

A later reviewer may GREEN **only** if this page has **no red and no yellow**, including:

1. Named book `invert-wf-2023` EUR 10000. **Not** the fund gate. `invert-paper` fill **1** stays. No reseal `c9689f5d`. No `dca-paper` reset.
2. 15m bar-close. No lookahead. Rails from prior **96** bars, not bar `i`. Causal swing. No future high.
3. Invert: after fill, swap jobs of **those two** prices; re-arm filled price **only** on opposite fill. **No naked short.** **No ladder.** Default `MAX_RESTING_LIMITS = 1`. Optional PAPER-00028 extra **only if named**. `Hi` = 24h H.
4. Clip **EUR 200** hard. Fees **0.26%** primary + **0.40 / 0.80** shadow. No leftover-cash sizing. No 100% equity. Not the whole book deployed.
5. Same-bar both-sides = skip, not a round-trip. Touch at `P`. Armed `t` eligible `t+1`.
6. Combined = one sequential book, not the sum of slices.
7. Close-model / fill-every-rung / 9097 / 7923 grind fingerprint **fails the run**. Do not publish as invert.
8. `venue` required. Named score: **`BINANCE-VISION-XRPEUR`** or later **`KRAKEN-TRADES` / `KRAKEN-OHLCVT`**. **Not Bitstamp as the named score.**
9. Still paper. No keys. No orders. VOORBEELD. No second journal domain. Operator is not the freelancer.

Until then: **do not start CODE.**

This file does not rewrite PR #196. Teammates read **this lock** for the engine. Scoring this page GREEN is not permission to start CODE and not a fund-gate conversion.

---

## 14. This run

| Did | Did not |
| --- | --- |
| Wrote this PLAN lock to close #203 reds/yellows | Implement replay, fetch ZIP, place orders |
| Kept every #196 GREEN slogan (G1–G8) | Bargain away not-the-gate / fill 1 / no reseal / clock / fees / combined / paper |
| Locked ONE invert pair; retired pair-each-fib (`2bfb1b68`) | 14 pairs; fill-every-rung ladder |
| Locked hard EUR 200; skip leftover cash | 100% equity; whole-book deploy |
| Locked dual-touch skip, touch at P, armed t eligible t+1, causal swing | Close-model; same-bar round-trip; future high |
| Locked venue `BINANCE-VISION-XRPEUR` or later `KRAKEN-TRADES` / `KRAKEN-OHLCVT` | Bitstamp as named score |
| Locked grind fingerprint as a **fail** (9097 and invert-v2 day0 7923 cited as warnings) | Publish grind as invert; start CODE |
| | Reseal `c9689f5d`; reset `invert-paper` or `dca-paper`; shop HTML; mail; keys |

**PLAN stage after this file:** the #203 reds and yellows are designed out on paper. **Next seat: a different reviewer scores this file.** Not CODE. Not live. Not the fund gate.

---

**PII:** No personal mailbox, phone, IBAN, or invented KBO on this page. Treasury strings stay listed only as **do-not-touch** Phantom bans.

End. Still paper. `invert-wf-2023` is not the fund gate. invert-paper fill 1 stays. Do not reseal `c9689f5d`. Do not reset `dca-paper`. 9097-fill was fill-every-rung, not invert. invert-v2 day0 still FAIL (−41%, 7923 fills). Operator is not the freelancer. **Do not start CODE.**
