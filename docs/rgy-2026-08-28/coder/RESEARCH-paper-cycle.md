# RESEARCH — What is one complete paper cycle?

**Seat:** RESEARCHER · Coder  
**Lens:** simple **first**, then broaden. Adversarial before GREEN. Method only. Not a score. Not a fill.  
**Date:** 2026-08-28  
**Stamp:** VOORBEELD · paper / simulated · not FACTUUR · not INVOICE · not live-trade advice  
**HEAD (leftover `main` at write):** `2170952`  
**Still paper.** No orders. No keys. No CODE. No live. No Phantom spend. No memecoins.  
**`is_fund_gate`:** **false**

This file answers the operator correction: **do not oneshot a 3-year historical dump and call it a paper print.** Research how a **PAPER CYCLE** works first.

Named next book (CEO must name it before it is a gate): a **1d XRPEUR blueprint** journal that can be written **going forward**. Not a 2023→2026 blob. Not CODE this sitting.

---

## Locks (do not bargain)

| Lock | Status |
|---|---|
| Still paper / no keys / no orders / no CODE / no live | **held** |
| `is_fund_gate` | **false** — this pack does not fund |
| Do not reset `invert-paper` | **held** — live cycle stays. Cite it. Do not flatten TPs |
| Do not reset `dca-paper` | **held** — five BTCUSD slices @ 78900.6 stay held |
| Do not reset `donch-d20-xrpeur-paper` | **held** — candidate book. Different recipe. Not this page’s score |
| Do not reseal `c9689f5d` | **held** — 8-day lab clip 20 fills / +0.681154% / maxDD 0.890854% is **not** a cycle dump and **not** funding proof |
| Invert after any fill | TP becomes next entry; entry becomes next TP. **Symmetric re-arm.** Re-arm the filled price **only** on the opposite fill |
| Spot | **Never naked-short.** Sell inventory, then buy back. After sell-TP you are **flat EUR** |
| All fib extensions and reversals | **rungs**. Full set is the catalog, not a spray of working orders |
| Cap on live invert-paper | **2 long. No third buy.** |

**Oneshot dumps already judged (cite, do not restamp):**

| Print | Why it is not a paper cycle |
|---|---|
| Close-model 9097 fills / −99.989999% / 1.00 EUR ([PR #201](https://github.com/eyeskull2220/solana-invoice/pull/201)) | A **blob**. Fill-every-rung / same-bar / 100% size. Not invert |
| `INVERT-V2-1LIMIT` 2779 / −15.21% ([PR #222](https://github.com/eyeskull2220/solana-invoice/pull/222)) | Multi-year mill. Not journaled as cycles |
| D6 reconstruct 2665 / −16.03% | Same mill, Kraken-native. **STOP** on invert 15m |
| `donch-d20-xrpeur-paper` named 37 / +5.76% | **Different recipe** (20-high in / 10-low out). Candidate. **Do not reset.** Not a blueprint cycle |
| 8-day `c9689f5d` 20 fills | Sealed **lab clip**, not walk-forward, not this 1d book |

Journal this sitting (cite, do not ping / flatten / reset): https://dca-paper-journal.surge.sh/ — fills **2/8**, `PAPER-00029` + `PAPER-00031`, TPs `00030` @ 1.26778 and `00032` @ 1.24496 still open. Cap 2 long. No third buy.

Kraken public this sitting (`GET /0/public/Time` → `unixtime` **1787949256**, `Fri, 28 Aug 26 20:34:16 +0000`; `SystemStatus` → `online`): XRPEUR last **1.19151**, 24h H **1.26300**, 24h L **1.17715**. Kraken MCP: unavailable. No keys.

---

## What this page is (and is not)

| Thing | This pack |
|---|---|
| Question | What is **one complete paper cycle**, step by step, for a **1d XRPEUR blueprint** book that can be **journaled going forward**? |
| Operator method | Draw a **map** (fib + horizontal rungs + sometimes a channel). Print a vertical **DRAWDATE** on that day. Every level is actionable **after** the drawdate |
| Analog DRAWDATE stamps (not XRPEUR rails) | KO **2023-05-24** · BTC **2024-07-15** · ETH **2024-03-16**. XRP: operator **knew in 2023**; **2025 charts are a redraw** |
| Worked example | Live `invert-paper` fill 1 → fill 2, cap 2. **That is a cycle, not a dump** |
| Clock for the named next book | **1d** XRPEUR (days contain the 0.52% round-trip tax; 15m invert is a dead class — [PR #211](https://github.com/eyeskull2220/solana-invoice/pull/211) / [#222](https://github.com/eyeskull2220/solana-invoice/pull/222)) |
| Not this page | A 2023→2026 equity curve. A SCORECARD blob. CODE. Live. A Donchian trail. Fill-every-rung. Rolling `N=8` zigzag as a substitute for DRAWDATE |

**Do not invent a score.** No 2023 fill count. No 1d blueprint return. No PASS/FAIL for a book the CEO has not named. Missing DRAWDATE ≠ assume 2023-01-01.

---

## Simple (the whole cycle)

A paper cycle is **one clip** walking **two rungs**, journaled as events, not as a multi-year dump.

```text
DRAWDATE  →  ARM  →  TAG  →  FILL  →  NEXT-RUNG EXIT  →  RE-ARM
                 ↑                                         |
                 +---------- wait between rungs -----------+
```

1. **DRAWDATE.** Operator stamps a vertical on the **1d** XRPEUR chart. Map = fib + horizontals [+ channel]. Rungs **do not exist** for this book before that close.
2. **ARM.** Rest **at most one** working limit per clip, given inventory. Cap **2** clips (live invert-paper). Full fib set is the **catalog**, not the order list.
3. **TAG.** A **closed** 1d bar’s high/low **touches** a resting rung. Log the tag. **Tag ≠ fill.**
4. **FILL.** A `PAPER-*` **print** at the limit. Fee hits now. Inventory updates. Rest the **next-rung** exit.
5. **BETWEEN RUNGS.** Price in the gap. Book **WAIT**. Journal `IDLE`. Do not spray. Do not redraw.
6. **NEXT-RUNG EXIT.** Opposite `PAPER-*` print at the swapped price. Cycle **closes**. Two fees.
7. **RE-ARM.** Those two prices **swap jobs**. Symmetric. Filled price sleeps until the opposite prints. Spot: if flat, next rest is **buy-back**, never a naked sell.

**Walk-forward** = cycle 1, then cycle 2, then cycle 3, each a journal row, from DRAWDATE **forward to now**. Not one blob labelled “2023+”.

That is the unit. The 9097-fill dump is what you get when you skip this unit.

---

## Operator method — DRAWDATE is the confirmation

This is the operator’s method, **not a guess**, **not** PR #199’s agent-invented `N=8` zigzag.

| Analog | DRAWDATE (vertical) | Meaning |
|---|---|---|
| KO | **2023-05-24** | Map drawn that day. Levels live **after** |
| BTC | **2024-07-15** | Same |
| ETH | **2024-03-16** | Same |
| **XRP** | Operator **knew in 2023** | Exact 2023 stamp is **operator-supplied**. **Do not invent it here.** **2025 charts are a redraw** = a **new** DRAWDATE, not a silent rail move |

**After DRAWDATE, every level on that map is actionable.** Before DRAWDATE, a 1d wick that would have “touched” a future fib **does not count**. That is the anti-lookahead rule for a blueprint book. You do not need a rolling swing confirm to fake causality: the **stamp is the confirm**.

**Redraw ≠ rolling update.** A 2025 XRP redraw is a **new map** with a **new vertical**. Journal it as `DRAWDATE_2`. Cancel rests that belonged to `DRAWDATE_1` (cancel is **not** a fill). Do not splice 2023 rungs and 2025 rungs into one score.

**Do not copy KO/BTC/ETH rails onto XRPEUR.** Those dates teach **how to stamp**, not which prices XRP uses.

PR #199 L3 `N=8` (eight 15m bars) was a replay anti-repaint rule for agents **without** the operator’s chart. For a **blueprint** book, replacing DRAWDATE with a sliding zigzag is a **different recipe**. Do not mix them.

---

## Step by step — one complete cycle on a 1d XRPEUR blueprint

Clock: **closed 1d** bars, Kraken `XRPEUR` / `XXRPZEUR`. Decision at **bar close**. A rest armed at close of day `t` is eligible from day `t+1`. Never the arm bar. Fill at **limit** if `[low, high]` contains `P`. Not the close. Not the wick-beyond as extra size.

Clip: **EUR 200** (live `PAPER-00029` cost ~200). Book capital **EUR 10 000 simulated** if a new book is ever named. **Not** 100% equity. **Not** the live invert-paper JSON.

### 0. Name the book (CEO). Do not init it here

Proposed shape only: `xrpeur-1d-blueprint-paper` (CEO names it or it stays a memo). **Not** `invert-paper`. **Not** `dca-paper`. **Not** `donch-d20-xrpeur-paper`. **Not** a `paper init` in this PR.

### 1. DRAWDATE (not a fill)

Operator draws:

- Fibonacci **full set** on **this pair only** (retracements 0.236 / 0.382 / 0.5 / 0.618 / 0.786 + extensions 1.272 / 1.618 / 2.0 / 2.618 **both sides**). Same formula as [PR #199](https://github.com/eyeskull2220/solana-invoice/pull/199) L3, **from the swing that exists on the chart at DRAWDATE**, not from a future high.
- **Horizontal** rungs (prior highs/lows / round numbers the operator actually drew).
- **Sometimes a channel** (both rails are rungs).

Print a vertical: `DRAWDATE = YYYY-MM-DD` (Europe/Brussels calendar date of the stamp). Journal row:

```text
event=DRAWDATE  book=…  pair=XRPEUR  clock=1d  date=…  map_hash=…  n_rungs=…
```

Before this date: **no cycle**. Warmup bars may exist on disk; they **must not** fill.

**XRP 2023 stamp:** WAIT for the operator. “Knew in 2023” is not a date. Inventing `2023-01-01` as DRAWDATE is the oneshot dump in a trench coat.

### 2. ARM (not a fill)

From the map, pick **one working pair** `(P_entry, P_tp)` for clip 1:

```text
C = last CLOSED 1d close (after DRAWDATE)
P_entry = nearest rung strictly below C     # buy-eligible
P_tp    = nearest rung strictly above C     # next-rung exit
```

If either side is missing: **wait**. Do not skip to an unconfirmed extension. Do not latch 24h H as `P_tp` unless that high is **already a drawn rung** on the map (live invert-paper TP `1.26778` is journaled as **24h H** — that is the **15m invert book**, YELLOW as a fib lesson, not the 1d blueprint rule).

Inventory starts `FLAT_EUR`. Arm **buy LIMIT** at `P_entry`. Do not arm the sell. Do not rest the whole catalog.

Cap 2 (from live invert-paper): a **second** clip may arm a **different** buy rung **below**, only while longs < 2. **No third buy.** See § Broaden.

### 3. TAG (not a fill)

On a later **closed** 1d bar `b` (`b` after arm bar):

| Rest | Tag |
|---|---|
| Buy LIMIT at `P` | `low[b] <= P` |
| Sell LIMIT at `P` | `high[b] >= P` |

Journal `event=TAG` with bar date, `P`, side. **A tag without a `PAPER-*` print is not a fill.** A live ticker through `P` is not a fill ([PR #132](https://github.com/eyeskull2220/solana-invoice/pull/132) attack 9). Do not backfill from OHLC.

### 4. FILL (this counts)

**A fill is a `PAPER-*` print** on **this** book: closed or fully filled, with an id.

| Counts as a fill | Does not count |
|---|---|
| `PAPER-00029` buy XRPEUR @ 1.24496 | Resting TP `PAPER-00030` |
| `PAPER-00031` buy XRPEUR @ 1.23084 | Resting TP `PAPER-00032` |
| Future sell-TP print on those TPs | Open / cancelled / rejected |
| | DRAWDATE, TAG, ARM, IDLE, redraw cancel |
| | Donchian / DCA / sleeve prints |
| | Lab-clip `c9689f5d` fills (other book) |
| | Same-bar invented round-trip |

Fill price = **`P`** (the limit), not the low, not the close. Gap-through: still count default at `P`; shadow the `open`. Same-bar both-sides: **at most one fill per clip per bar**. Newly armed opposite **skips this bar**. If a bug had both sides working, fill **neither**, flag `DUAL_TOUCH_SKIP` / `SAME_BAR_REARM`.

On a buy fill: inventory `LONG_XRP`. Record fee. Rest **sell LIMIT** at `P_tp` (next-rung exit). **Do not re-arm a buy** on this clip (no pyramid). Live tell: after fill 1, a leftover second **buy** (`PAPER-00028` → later fill 2) is **clip 2 under cap 2**, not a re-arm of clip 1.

### 5. BETWEEN RUNGS (the book WAIT)

This is the part a dump skips.

Price is **not** on a working limit. Examples from **live invert-paper this sitting** (illustration, not a ping):

| Clip | Entry (filled) | Resting TP | Last 1.19151 |
|---|---|---|---|
| 1 | 1.24496 (`00029`) | 1.26778 (`00030`) | **below entry**, TP still above |
| 2 | 1.23084 (`00031`) | 1.24496 (`00032`, latch fill-1) | **below entry**, TP still above |

24h H **1.26300** did **not** tag `00030` (1.26778). 24h L **1.17715** is **below both entries**. Cap **2** → **no third buy** even though price went lower.

**What the book does:**

- Leave the resting TPs.
- Do not market-out because mark-to-market is red.
- Do not add clip 3.
- Do not redraw the map because the day was ugly.
- Journal `event=IDLE  between_rungs=true  last=…  working=[…]`.
- Mark-to-market may be written as **comment**. It is **not** gate-1 and **not** a fill.

Idle can last **many 1d bars**. That is healthy. 15m invert died on **n**. A 1d blueprint that idles is doing the job.

### 6. NEXT-RUNG EXIT (the other fill; cycle closes)

The sell LIMIT at `P_tp` prints (`PAPER-*`). Spot: you **sold inventory**, you did **not** open a short. Inventory `FLAT_EUR`.

**Cycle 1 is complete** only when **both** legs have prints:

```text
FILL_BUY  @ P_entry   +  FILL_SELL @ P_tp
```

Until the sell prints, you have an **open cycle** (live invert-paper right now: **two** open cycles, **zero** closed round-trips). Gate language “fills ≥ 8” counts **prints**, not closed round-trips — keep both numbers on the journal so nobody “almosts” 8 with two buys and two rests.

### 7. RE-ARM (symmetric; not a fill)

After **any** fill, swap jobs of **those two** prices:

```text
old:  entry = A,  TP = B
fill at A  →  next entry = B,  next TP = A
fill at B  →  next entry = A,  next TP = B
```

**Re-arm the filled price only on the opposite fill.** The price that just printed **sleeps**.

Spot override: after sell-TP you are **flat cash**. Next rest is **buy-back**. If the swap would sell with zero XRP, **discard the short**. Stay `FLAT_EUR`. Never rest a sell naked.

Arm at this close; eligible `t+1`. Then wait between rungs again. That wait **is** cycle 2 starting — it is not permission to dump 2024–2026 in one sitting.

---

## Fees (every print; cycle uses two)

| Column | Per fill | Round-trip (buy+sell) |
|---|---:|---:|
| Paper engine (Kraken Starter taker) | **0.26%** | **0.52%** |
| Shadow (Tier 1 maker since 2026-07-09) | **0.40%** | **0.80%** |
| Shadow taker stress (Tier 1 taker) | **0.80%** | **1.60%** |

Live invert-paper already prints this on fill 2: `0.26=0.52; 0.40=0.80; 0.80 taker=1.60` (euros on a **EUR 200** clip).

Rules:

- Deduct the engine fee on **every** `PAPER-*` print. Buy fill 1 already paid 0.52 EUR. TP `00030` is **not** profit until it prints **and** the sell fee is subtracted.
- Gate 1 (if this book is ever a gate) is **shadowed realized** return after **closed** cycles, not last-vs-entry.
- Report all three columns. Green at 0.26 and red at 0.80 is **not** a silent pass.
- **1d median HL on XRPEUR REST ~4.46%** (2024-09+ — [PR #222](https://github.com/eyeskull2220/solana-invoice/pull/222)) **contains** 0.52%. That is why this cycle is asked on **1d**, not 15m (~0.45% typical range, dead vs the tax). Geometry is not a PnL.
- Paper skill: **slippage 0, partials not modeled**, instant full fills. Say it on every journal. Paper is not proof ([PR #118](https://github.com/eyeskull2220/solana-invoice/pull/118) ten ways).

Do not reuse live qty `160.64773` / `162.49066` as 1d-blueprint size unless scoring **that** live book (this pack must not).

---

## Worked example — live `invert-paper` is a cycle (not a dump)

Source: operator + https://dca-paper-journal.surge.sh/ this sitting. **Leave the book.**

| Id | Event | Price | Qty | When (Europe/Brussels) | Fill? |
|---|---|---|---|---|---|
| `PAPER-00027` → **`PAPER-00029`** | **FILL 1** buy | **1.24496** | 160.64773 | 20:56:53 | **Yes. Print 1** |
| **`PAPER-00030`** | Clip-1 TP sell LIMIT | **1.26778** (24h H) | 160.64773 | still open | **No** |
| `PAPER-00028` → **`PAPER-00031`** | **FILL 2** buy | **1.23084** | 162.49066 | 08:15:34 | **Yes. Print 2** |
| **`PAPER-00032`** | Clip-2 TP sell LIMIT | **1.24496** (latch fill-1 px) | 162.49066 | rested 08:19:27 · still open | **No** |

**Invert swap, visible:** after fill 1 at **1.24496**, clip-2’s TP is **that same price**. Entry became next TP. Symmetric re-arm of **those two** prices, on a **second clip**, under **cap 2**.

**Cap 2:** two longs, two TPs, **no third buy**. Last **1.19151** is through both entries and **still** no clip 3. That is cycle discipline. Fill-every-rung would have sprayed the 1.177 low.

**What is complete vs open:**

| Cycle / clip | Entry print | Exit print | State |
|---|---|---|---|
| Clip 1 | `00029` @ 1.24496 | `00030` @ 1.26778 **not printed** | **Open cycle** |
| Clip 2 | `00031` @ 1.23084 | `00032` @ 1.24496 **not printed** | **Open cycle** |

Gate on this book: **2/8 NOT MET**. Return after fees **−0.0496% (mark)**. maxDD **~0.0496%**. Mark is not a closed cycle. **Do not flatten 00030/00032.** Ping only when **they** print.

**Why this is the teaching object:** n=2, cap=2, swap visible, idle between rungs, fees on the print, resting ≠ fill. The 9097 blob had none of that.

This example is **15m invert-paper**, not the 1d blueprint. The **cycle anatomy** transfers. The **clock** for the named next book is **1d**. Do not restamp invert 15m as 1d.

---

## Walk-forward is a sequence of cycles (not one blob)

A dump:

```text
for bar in 2023-01-01 .. 2026-08-28:
    fill whatever the wick touched
print fills=9097, return=−99.99%
call it "walk-forward"
```

A cycle walk-forward:

```text
DRAWDATE = operator stamp (XRP 2023 date WAIT; redraw 2025 = DRAWDATE_2)
cycle_id = 0
for each closed 1d bar after DRAWDATE, up to yesterday:
    if IDLE: journal idle (optional daily, or weekly heartbeat)
    if TAG: journal tag
    if FILL: journal print, fees, inventory, re-arm, cycle_id
    if EXIT: close cycle_id, journal net after two fees, cycle_id += 1
stop at now. do not continue into the forming bar.
```

| Dump (forbidden) | Sequence of cycles (this pack) |
|---|---|
| One SCORECARD for 3.6 years | One **row per event**, then a **row per closed cycle** |
| 9097 / 2779 / 2665 as “the print” | Live invert-paper: **2 prints**, 2 open cycles, 0 closed |
| Close-model both sides same bar | ≤1 fill per clip per **1d** bar; opposite skips arm bar |
| Rolling fib from future high | Rails frozen at DRAWDATE until a **redraw stamp** |
| Splice Binance Vision + Kraken tail | Kraken XRPEUR 1d only ([PR #210](https://github.com/eyeskull2220/solana-invoice/pull/210) OHLCVT `XRPEUR_1440.csv` when a slice exists) |
| Sum year slices to fake ≥ 8 | Expanding **count of closed cycles** from DRAWDATE. A year with 3 prints is **3**, not a reason to add 2024 in the same cell |
| Treat `c9689f5d` 20 fills as cycle 1…20 of 2023 | **Other book.** Cite. Do not 20+2 |

**Journal columns for one closed cycle** (going forward — fill these when they happen, not from a dump):

```text
cycle_id
drawdate
book
pair            XRPEUR
clock           1d
clip_eur        200
entry_id        PAPER-…
entry_px
entry_ts
entry_fee_0.26 / 0.40 / 0.80
exit_id         PAPER-…          # empty while open
exit_px
exit_ts
exit_fee_…
net_after_fees  # blank until exit prints
idle_days
tags            # dates that touched but did not print (honesty)
inventory_after FLAT_EUR | LONG_XRP
next_entry / next_tp    # post-swap
```

**Heartbeat while open:** `as_of`, `last`, `working_ids`, `between_rungs=true`. Live invert-paper today would heartbeat: last 1.19151, working `00030`+`00032`, between rungs, cap 2, no third buy.

**When to stop a sitting:** after the **current** cycle’s events for **today’s closed bar** are journaled. Starting a 3-year loop “to get to 8 fills” is gate-cheating ([PR #118](https://github.com/eyeskull2220/solana-invoice/pull/118) extra clips).

REST 1d OHLC is a **720-cap** (first bar ~2024-09-07). It cannot source a 2023 DRAWDATE tape. Official `XRPEUR_1440` is the later dump **if** CEO asks for a historical sequence **from a real DRAWDATE**. That sequence is still **row-by-row cycles**, not a blob. This PR does not fetch it.

---

## Broaden (only because the simple cycle is not thin — these are the live tells)

### B1 — Cap 2 is two clips, not fill-every-rung

Live invert-paper runs **two** open cycles. That is allowed **inventory policy**, not permission to rest the full fib set.

| Allowed | Forbidden |
|---|---|
| Clip 1 long + clip 2 long, **two** TPs, cap 2 | Clip 3 because price made a new low |
| Clip-2 TP latched at clip-1 fill (`00032` @ 1.24496) | Every extension as a live LIMIT (`2bfb1b68`) |
| Skip extra rungs rather than lever | 100% equity / overlapping full-book lots |

Cash cap: working buys + held cost + primary fees **≤ cash**. Skip rather than borrow. Spot cannot short the fade.

### B2 — Channel rungs

If the operator drew a channel, **both** rails are horizontals in the catalog. They do not get a special fill model. They are not a Donchian 20/10 ([`donch-d20-xrpeur-paper`](https://github.com/eyeskull2220/solana-invoice/pull/227) is that other movie — leave it).

### B3 — 15m invert vs 1d blueprint

| | Live `invert-paper` (gate, 2/8) | 1d XRPEUR blueprint (this pack) |
|---|---|---|
| Clock | 15m | **1d** |
| Confirm | Live book already running | **DRAWDATE** vertical |
| Cycle anatomy | **Same** (swap, re-arm opposite, no naked short, cap 2) | **Same** |
| Fee vs bar | Typical 15m HL ~0.45% **< 0.52% RT** — dead class | Typical 1d HL ~4.46% **contains** the tax |
| Do not | Reset it to “test 1d” | Init it in this PR |

Do **not** propose “15m invert that waits for a daily close.” That is still invert 15m ([PR #222](https://github.com/eyeskull2220/solana-invoice/pull/222) STOP).

### B4 — Donchian is not a blueprint cycle

`donch-d20-xrpeur-paper`: breakout in, 10-day trail out, **no** two-price swap, **no** DRAWDATE map. Named candidate PASS is **not** this method. **Do not reset. Do not mix fills into a blueprint journal.**

### B5 — Redraw

XRP 2025 charts = **DRAWDATE_2**. New catalog. Cancel `DRAWDATE_1` rests (not fills). Cycles in progress: operator choice, **journaled**, not silently repriced. Do not let a redraw rescue an open clip’s TP.

---

## Adversarial first (stops, not bargains)

1. **Oneshot 2023→2026 and call it a cycle print.** 9097 / 2779 / 2665 / even a 37-fill Donchian blob. Forbidden as **this** answer. Sequence of cycles or nothing.
2. **Invent the XRP 2023 DRAWDATE.** Operator said they knew in 2023; they did not stamp the day in this prompt. WAIT.
3. **Treat 2025 redraw as the 2023 map.** Different vertical. Do not splice.
4. **Count `00030` / `00032` as fills.** Resting is not a fill. Gate 2/8 stays **2**.
5. **Count a TAG or a live through as a fill.** Last 1.19151 through 1.23084 is **not** a third print.
6. **Third buy under cap 2** because 24h L is 1.177. Spray. Retired `2bfb1b68`.
7. **Replace DRAWDATE with PR #199 `N=8` zigzag** and call it the operator’s method. It is not.
8. **Same-bar buy+sell on a fat 1d candle** as a closed cycle. `DUAL_TOUCH_SKIP`. Opposite skips the arm bar.
9. **Naked short** after a sell-TP, or sleeve flip mixed into spot. Spot = flat then buy-back.
10. **Fee vanity.** Mark −0.0496% as gate-1. Gate-1 needs **closed** legs after fees.
11. **Reset `invert-paper` / `dca-paper` / `donch-d20-xrpeur-paper`** to run the 1d book. New book or memo.
12. **Reseal `c9689f5d`** as “the first 20 cycles.” Other book.
13. **CODE / live / keys / 10k as a SEPA deposit.** Autonomy **2**. This is a method page.
14. **Copy KO 2023-05-24 prices onto XRPEUR.** Analog stamp only.
15. **Fund from this markdown.** `is_fund_gate: false`. invert-paper remains the gate at **2/8 NOT MET**.

---

## Verdict: **GREEN** (cycle anatomy) · **RED** (promotion / oneshot / invented DRAWDATE)

| Probe | Result | Color |
|---|---|---|
| One cycle = DRAWDATE → arm → tag → fill → idle → next-rung exit → re-arm | Written | **GREEN** (pack) |
| Live invert-paper 00029/00031 as cycle-not-dump | Cited; TPs open; cap 2 | **GREEN** (example) · **RED** if flattened |
| Walk-forward = sequence of cycles, not a blob | Named; dump table | **GREEN** (named) |
| XRP 2023 DRAWDATE in this file | None (must not invent) | **YELLOW** (WAIT) |
| 1d blueprint fill/return/maxDD | None (must not invent) | **YELLOW** (unscored) |
| 9097 / 2779 / 2665 as this cycle | Forbidden | **RED** if used |
| Reset invert / dca / donch / reseal `c9689f5d` | Forbidden | **GREEN** (not touched) |
| Promotion / live / CODE | Out of scope | **GREEN** (not done) · **RED** if a later page funds from this |

**Promotion: no.** Stay paper. Gate on live `invert-paper` remains **NOT MET** (2/8). This pack has **no 1d blueprint prints**.

---

## RED

### R1 — Do not oneshot a dump

A 3-year loop that emits thousands of fills is **not** a paper cycle. Design-out already exists for that movie ([PR #201](https://github.com/eyeskull2220/solana-invoice/pull/201) D1–D9). This page does not restamp it.

### R2 — Do not invent DRAWDATE or a 1d score

XRP “knew in 2023” is not `2023-01-01`. Missing stamp ≠ PASS. REST 720 1d is not 2023.

### R3 — Do not promote

Live n=2 prints, 0 closed invert round-trips on the gate book. Paper omits slippage and partials. Method markdown is not a fund memo.

### R4 — Do not touch locked books

No `paper reset` on `invert-paper`, `dca-paper`, `donch-d20-xrpeur-paper`. No flatten of `00030`/`00032`. No reseal of `c9689f5d`.

---

## YELLOW

### Y1 — XRP 2023 stamp WAIT

Operator must print the 2023 vertical (and whether 2025 redraw replaces it). Until then the 1d blueprint book **cannot** start a historical sequence honestly. **Going forward from today** still needs a stamp: either “map already live from 2023 knowledge” (operator yes) or a **new** DRAWDATE on a closed 1d bar **now**. This file does not pick.

### Y2 — Live TP 24h H vs fib

`PAPER-00030` @ 1.26778 = journal 24h H. Teaching object is the **swap + cap 2**, not “use rolling 24h H as 1d `P_tp`.”

### Y3 — Connector / recipe file

Kraken MCP error. `/workspace/paper-recipes/` is not in `solana-invoice`. Do not place paper orders to “verify” a cycle.

### Y4 — Fills ≥ 8 counts prints; a complete cycle is two prints

Do not silently switch the gate to “8 closed round-trips” without CEO. Do not switch it to “8 tags.” Keep **prints** and **closed cycles** as two columns.

### Y5 — 1d REST 720 vs OHLCVT 1440

A going-forward journal from **today** does not need 2023 daily history. A going-forward journal from a **2023 DRAWDATE** does. Disclose source or do not score.

---

## GREEN

### G1 — Cycle unit is small enough to journal

DRAWDATE, tag, fill, idle, exit, re-arm. Live invert-paper already shows fill → TP, second fill → latched TP, cap 2, idle under both entries.

### G2 — Look-ahead stops named without a dump

Actionable **after** DRAWDATE. Arm `t`, fill from `t+1`. Touch-fill at limit. No same-bar round-trip. Redraw = new stamp.

### G3 — Locked books left alone; clip cited not resealed

`sha256:c9689f5d7d583320e724900b0ce4ef68193878c880d11939badd1dd59016e390`

No keys. No Phantom. No FACTUUR. No invented KBO. Operator: natural person, Geel. **KBO/BTW: nog niet toegekend.**

### G4 — Gate language not redefined

Still: return > 0 after fees **and** ≥ 8 prints **and** maxDD ≤ 8%, on the book you claim. Cycle anatomy ≠ “method exists so gate is green.”

### G5 — FACTUUR / keys / treasury

Out of this research. Treasury receive strings stay Wallet’s, never Kraken float:

- Solana USDC `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3`
- Base USDC `0x9eb954b567ef3616424a6e1bf42c63724930aa54`

---

## NOTES

- **Report-only.** No paper order, no live order, no journal HTML patch, no shop edit, no mail, no reseal, no reset, no `donch` init, no blueprint-book init.
- **Sources:** operator correction this sitting (DRAWDATE analogs KO 2023-05-24 / BTC 2024-07-15 / ETH 2024-03-16; XRP knew-2023 / 2025 redraw; invert swap; live cycle 00029/00031 cap 2); live journal https://dca-paper-journal.surge.sh/ ; [PR #118](https://github.com/eyeskull2220/solana-invoice/pull/118) Coder seat; [PR #132](https://github.com/eyeskull2220/solana-invoice/pull/132) / [#144](https://github.com/eyeskull2220/solana-invoice/pull/144) live invert gate; [PR #155](https://github.com/eyeskull2220/solana-invoice/pull/155) VOORBEELD journal; [PR #199](https://github.com/eyeskull2220/solana-invoice/pull/199) invert path rules (cited for fill/swap, **not** as a DRAWDATE substitute); [PR #201](https://github.com/eyeskull2220/solana-invoice/pull/201) dump RED; [PR #206](https://github.com/eyeskull2220/solana-invoice/pull/206) one-limit; [PR #210](https://github.com/eyeskull2220/solana-invoice/pull/210) OHLCVT how-to; [PR #222](https://github.com/eyeskull2220/solana-invoice/pull/222) 1d vs 15m fees; [PR #227](https://github.com/eyeskull2220/solana-invoice/pull/227) donch candidate (leave it); Kraken public Time/Status/Ticker XRPEUR 2026-08-28 20:34Z; `kraken-paper-strategy` (0.26% taker, no slippage/partials); `kraken-autonomy-levels` (level 2 = paper); `kraken-grid-trading` (fill at N → rest N±1 — cousin of invert swap, **not** this blueprint).
- **Retired hashes stay retired.** `2bfb1b68` fill-every-rung · `9056f296` entry-waits-TP · `094513` arming-only.
- **Tax (not advice):** paper is not a tax event. A cycle journal is not a CAP annex. Phantom sales-USDC = beroepsinkomen. Live Kraken later = apart handelsdossier. No invented FIFO.
- **PII:** no personal mailbox, no IBAN, no invented KBO.
- Concurrent dump/score agents must **not** treat this file as a licence to print 2023–2026 in one cell.

**Promotion: no.** Stay paper. Do not reseal `c9689f5d`. Do not reset `invert-paper`. Do not reset `dca-paper`. Do not reset `donch-d20-xrpeur-paper`. Do not oneshot 2023→2026. Journal **one cycle at a time** after DRAWDATE.

---

## Re-check (copy/paste — public / git only)

```bash
# This pack must exist, define DRAWDATE, and must not contain a fake 2023 PASS:
rg -n 'DRAWDATE|PAPER-00031|cap 2|between rungs|oneshot|is_fund_gate|2023-05-24' \
  docs/rgy-2026-08-28/coder/RESEARCH-paper-cycle.md

# Live cycle — expect fills 2/8, two TPs open, cap 2, not a dump:
curl -sS https://dca-paper-journal.surge.sh/ | rg -n \
  'PAPER-00029|PAPER-00031|PAPER-00030|PAPER-00032|fills 2|Cap 2|c9689f5d|donch-d20'

# Public now-tape is idle context, not a fill:
curl -sS -A 'rgy-research-paper-cycle-2026-08-28' 'https://api.kraken.com/0/public/Time'
curl -sS -A 'rgy-research-paper-cycle-2026-08-28' \
  'https://api.kraken.com/0/public/Ticker?pair=XRPEUR'

# Never:
# kraken paper reset --workspace invert-paper
# kraken paper reset --workspace dca-paper
# kraken paper reset --workspace donch-d20-xrpeur-paper
# kraken paper init --workspace xrpeur-1d-blueprint-paper
# kraken order …
```

Count fund-gate fills only from `PAPER-*` **prints** on **`invert-paper`**. Resting `00030` / `00032` do not count. A 1d blueprint cycle starts on a **stamped DRAWDATE** and is journaled **forward**, one event at a time. Still paper.

**A paper cycle is DRAWDATE → arm → tag → fill → idle between rungs → next-rung exit → symmetric re-arm. Live invert-paper already has that shape (00029 / 00031, cap 2). A 3-year dump is not a cycle. CEO stamps the XRP 2023 vertical (or a new one) before a 1d blueprint book exists. `is_fund_gate: false`.**

End. RESEARCHER. Docs only. `is_fund_gate: false`. VOORBEELD.
