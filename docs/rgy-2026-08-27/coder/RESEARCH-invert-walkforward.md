# RESEARCH — Invert 15m walk-forward method (from 2023)

**Seat:** RESEARCHER (Coder pack)  
**Lens:** adversarial **first**, then RED / YELLOW / GREEN. Method only. Not a score. Not a fill.  
**Date:** 2026-08-27  
**Stamp:** VOORBEELD · paper / simulated · not FACTUUR · not INVOICE · not live-trade advice  
**HEAD (this repo):** `2170952`  
**Still paper.** Do not reseal `c9689f5d`. Do not reset `invert-paper`. Do not reset `dca-paper`.

This file is the **adversarial method pack** for a **15m XRPEUR invert walk-forward starting 2023**. It does not place orders, does not paste keys, does not spend Phantom, does not rewrite shop HTML, and does not republish the journal.

It does **not** print a 2023 equity curve. Inventing one here is cheating. Sibling slice pages may *apply* this recipe; they do not rewrite it.

---

## What this score is (and is not)

| Thing | This pack |
|---|---|
| Recipe | Spot invert, XRPEUR, 15m, full fib set, swap jobs after any fill, re-arm only on the opposite fill, **no naked short** |
| Window | Causal walk-forward **from 2023-01-01 00:00 Europe/Brussels** (first closed 15m bar of 2023) through the slice’s last **closed** 15m bar |
| Book | A **simulated** historical book. Not `invert-paper`. Not `dca-paper`. Not the 8-day lab clip |
| Gate language (same three conjuncts, **this** simulated book only) | return > 0 **after fees** · fills **≥ 8** · maxDD **≤ 8%** |
| 8-day lab clip `sha256:c9689f5d…` | **Cite. Do not score as this. Do not reseal.** |
| Live paper `PAPER-00029` / `00030` / `00028` | **A different book.** Do not add 20+1. Do not splice into 2023 |

**Lab clip (NOT this walk-forward):** name `fib-grid-invert-xrpeur-15m` · XRPEUR 15m · 2026-08-18 21:00 → 2026-08-26 08:00 Europe/Brussels · 20 fills · +0.681154% · maxDD 0.890854% · PASS vs

`sha256:c9689f5d7d583320e724900b0ce4ef68193878c880d11939badd1dd59016e390`

Do not treat +0.68% as this method’s result. Do not restamp it as “2023+ walk-forward.” Do not rotate the hash.

**Live `invert-paper` (NOT this walk-forward):** fill 1 = `PAPER-00029` buy XRPEUR @ 1.24496. Resting TP `PAPER-00030` sell LIMIT @ 1.26778 is **not** a fill. Open `PAPER-00028` @ 1.23084 is **not** a fill. Gate on that book: **NOT MET**. Leave it. This pack does not ping it, flatten it, or reset it.

---

## Adversarial first

Attacks that would fake a 2023 invert walk-forward. Each is a **stop**, not a note to bargain.

1. **Treat the 8-day `c9689f5d` clip as this score.** The public Kraken OHLC 15m feed returns ~720 bars (~7.5 days). Pulling `/0/public/OHLC?pair=XRPEUR&interval=15` (even with `since=2023-01-01`) still returns **late-August 2026**. Scoring that window and labelling it “from 2023” is the clip in a trench coat. Cite `c9689f5d`. Do not reseal. Do not add 20+1.

2. **Reset `invert-paper` or `dca-paper` to “run the backtest.”** Historical replay is a **separate simulated ledger**. `invert-paper` keeps fill 1 + resting 00030 + open 00028. `dca-paper` keeps five BTCUSD slices. Official `paper init` / `paper reset` on those workspaces is banned from this pack.

3. **Repainting swings.** A zigzag / fractal whose last pivot **moves** as new 15m bars arrive. Rails that jump when the next bar prints are lookahead. Confirmation must be **closed-bar and lagged** (see lock S1). Until confirmation, the candidate does not exist.

4. **Using a future high (or future low) for fib.** Computing `swing_high = max(high)` over the whole year / whole slice / whole 2023–2026 file, then placing 2023-Jan rungs from that high. Same crime: 24h high that includes bars not yet closed; “highest close of the bull”; mixing XRPUSD / BTC rails onto XRPEUR.

5. **Filling both sides the same bar.** A 15m candle with `low <= P_buy` and `high >= P_sell` does **not** prove the path went buy-then-sell (or sell-then-buy). OHLC has no path. Crediting a round-trip inside one bar is lookahead. **At most one fill per bar**, and only the side that is actually armed given inventory.

6. **Intra-bar fill without a touch.** Filling a buy LIMIT at close / mid / next open when `low` never `<=` the resting price. Filling a sell LIMIT when `high` never `>=` the resting price. Filling on the **arm bar** (decision at close of bar `t`, fill on bar `t`’s already-known wick).

7. **Naked short on spot.** After sell-TP you are **flat EUR**. Next entry is **buy-back**. Resting a sell with zero XRP, borrowing, or copying the 3x sleeve’s long↔short flip into this spot replay is a different movie. Sleeve FAIL (6 fills, −2.729078%, maxDD 5.326685%) is **not** this score.

8. **Fee vanity.** Reporting gross rung-to-rung without 0.26% per fill, or setting shadow extra to 0 because the engine did. Gate 1 is shadowed round-trip. Default **0.26%** taker; **also** print **0.40** and **0.80** taker. Two fills = two fees (0.52 / 0.80 / 1.60 round-trip).

9. **Go live / paste keys / treat 10k as a SEPA deposit.** This is a method page. Autonomy stays **level 2**. Kraken MCP may be down; that is not permission to CLI a live order. No keys in git.

10. **Invent a 2023 result in this file.** No qty, no fill count, no maxDD, no PASS/FAIL for 2023 lives here. Data path for full-year 15m is **not** the public OHLC cap. Missing archive ≠ “assume PASS.”

11. **Use a retired invert hash.** Live lock name `fib-grid-invert-xrpeur-15m` vs `c9689f5d`. Retired: `2bfb1b68` fill-every-rung · `9056f296` entry-waits-TP · `094513` arming-only (99 fills PASS on that old hash is not this walk-forward). This pack is invert-swap, not those.

12. **Tune on the test years.** Picking swing lag `N`, first rung pair, or size on 2023–2026 then scoring the same bars. If a parameter is not locked below, it is **not** free to grid-search on the walk-forward window.

13. **Collapse books.** Do not mix sleeve PnL, `dca-paper` BTC, leftover `fib-paper` BTCUSD, or live `PAPER-00029` into the 2023 simulated fills. One scoreboard row per book.

14. **Broaden the pair list to rush 8 fills.** This method is **XRPEUR only**. Extra EUR pairs are WAIT (journal allowlist vs CODER.md fork is not a shopping list).

---

## Locked recipe (must hold)

Copy these as implementation invariants. A later slice page that violates one is not this method.

### L1 — Pair, clock, bars

- **Pair:** XRPEUR only (Kraken `XXRPZEUR` / `XRP/EUR`). Rails from **that pair’s** OHLC. No XRPUSD, no BTC, no index.
- **Timeframe:** 15m. Bar time = interval **start** (Kraken OHLC convention). Score on **closed** bars only. The forming bar is invisible.
- **Timezone for calendar slices:** Europe/Brussels dates. Convert with the offset that actually applied that day (CET/CEST). Do not shift 15m closes by a guessed hour.
- **Walk-forward start:** 2023-01-01 00:00 Europe/Brussels. Warmup bars **before** that instant may exist only to confirm a swing; they are **not** fills, not return, not maxDD.
- **Decision time:** close of bar `t`. New rest orders become eligible to fill from bar `t+1` onward. Never from bar `t`.

### L2 — Bar-close only. No lookahead. Touch-fill rule

**Signals, swing confirmation, fib recompute, and arm/cancel happen at bar close.**

**Fill rule (state it; do not “improve” it):**

A limit is **resting** at the open of bar `b` only if it was armed at the close of some bar `u` with `u < b`.

| Side | Touch | Fill price | Not a fill |
|---|---|---|---|
| Buy LIMIT at `P` | `low[b] <= P` | **`P`** (not the low, not the close) | `low[b] > P`; arm bar; market-at-close |
| Sell LIMIT at `P` | `high[b] >= P` | **`P`** (not the high, not the close) | `high[b] < P`; arm bar; market-at-close |

No intra-bar fill **unless** that bar’s high/low **actually touches** the resting limit.

**Gap-through:** if `open[b]` is already through `P` (buy: `open[b] < P`; sell: `open[b] > P`) **and** the touch inequality still holds, count a fill at **`P`** on the default column, and **also** record a gap shadow at `open[b]`. Do not skip the default column. Do not invent ticks between open and the wick.

**Same-bar both-sides: forbidden.** If a bar’s range could touch two prices, fill **at most one** order: the single limit that is armed given inventory (L4). Never buy and sell in the same 15m bar. Never assume OHLC path (OHLC vs OLHC). If an implementation had both limits working (a recipe bug), **fill neither** that bar and flag `DUAL_TOUCH_SKIP`.

**Close-only alternative is not this pack.** Do not require `close` to cross `P`. Wick touch is allowed; dual-fill is not.

### L3 — Fib rails from the swing on this pair only

**Full set (every level is a rung):**

- Retracements: **0.236 / 0.382 / 0.5 / 0.618 / 0.786**
- Extensions: **1.272 / 1.618 / 2.0 / 2.618** **both sides**

**Formula (lock the convention; mixing 0-at-start vs 0-at-end is a silent shift):**

Let `H` = confirmed swing high, `L` = confirmed swing low, `H > L`, `range = H - L`.

```
retracements (inside [L, H]):
  for r in {0.236, 0.382, 0.5, 0.618, 0.786}:
      L + r * range

extensions both sides (beyond the rails):
  for e in {1.272, 1.618, 2.0, 2.618}:
      above = L + e * range          # = H + (e - 1) * range
      below = H - e * range          # = L - (e - 1) * range
```

Do not add 0/1 rails as extra “always-on” rungs unless they coincide with `L`/`H` already in the working pair. Do not drop 0.5 or 2.0. Do not compute this set from any other pair.

**Swing confirmation (causal — lock S1):**

A bar `i` is a **candidate** swing high if `high[i]` is the max of `high[i-N : i]` (left window only, `N` fixed). It is **confirmed** at the close of bar `i+N` iff `high[i]` remains strictly greater than `high[i+1] … high[i+N]`. Symmetric for swing lows vs `low`.  

- **`N = 8`** (eight 15m bars = 2 hours). Locked here. Not grid-searched on 2023+.
- Rails at time `t` use only swings whose **confirmation close ≤ t**.
- Unconfirmed last pivot: **does not exist**. That is the anti-repaint rule.
- One working swing at a time: last **confirmed** high + last **confirmed** low that belong to the same completed move (the later confirmation of the two is the earliest you may arm from those rails).
- Recompute rungs only at confirmation events (bar close). Do not rebuild every bar from a sliding “highest high so far this year.”

### L4 — After ANY fill, swap TP/entry jobs. Re-arm only on the opposite fill

Working pair = two prices `(P_entry, P_tp)` chosen from the current rung set, `P_entry ≠ P_tp`.

**Inventory (spot):** `{FLAT_EUR, LONG_XRP}`. Never `SHORT_XRP`.

**Arming (at most one resting limit):**

| Inventory | Armed | Not armed |
|---|---|---|
| `FLAT_EUR` | buy LIMIT at `P_entry` | any sell |
| `LONG_XRP` | sell LIMIT at `P_tp` | buy (do not pyramid; do not re-arm entry) |

**On a fill:**

1. Record the print (id, side, `P`, bar close time, fee at 0.26 / 0.40 / 0.80).
2. **Swap jobs of those two prices:** the price that was TP becomes next entry; the price that was entry becomes next TP.
3. **Do not re-arm the filled price** until the **opposite** price fills.
4. Inventory: buy fill → `LONG_XRP`. Sell-TP fill → `FLAT_EUR`.

**Spot no naked short (overrides a swap that would sell from flat):**

- After sell-TP you are **flat EUR**.
- Next entry is **buy-back** (a buy LIMIT).
- If the swap would make the next job a **sell while flat**, **discard the short**. Stay `FLAT_EUR`. Next armed order is buy-back at the new `P_entry` **only if** that job is a buy; otherwise buy-back at the nearest **buy-eligible** rung **below** last from the current fib set (still this pair, still confirmed rails). Never rest a sell with zero XRP.

This is the spot reading of the same invert pairing. The 3x sleeve’s real long↔short flip is a **different book** and not this walk-forward.

Not this pack: fill-every-rung (`2bfb1b68`); entry-waits-TP as the only arm (`9056f296`); arming-only (`094513`).

### L5 — Fees

| Column | Taker per fill | Round-trip (buy+sell) |
|---|---|---|
| Default (Kraken Starter, paper engine) | **0.26%** | **0.52%** |
| Shadow | **0.40%** | **0.80%** |
| Shadow taker stress | **0.80%** | **1.60%** |

- Deduct the fee on **every** print. Gate 1 uses **shadowed** return, not mark-to-market.
- Report all three columns. A slice that is green at 0.26 and red at 0.80 is **not** a silent pass.
- Size: paper EUR 10000 **simulated** starting capital for this historical book (not a deposit; not the live `invert-paper` JSON). Do not reuse live qty `160.64773` from 00029 unless a slice is explicitly scoring that live book (it must not).

### L6 — Books you must not touch

- Do not reseal `c9689f5d`. Cite the full sha256 if you mention the clip.
- Do not reset / init / flatten `invert-paper`.
- Do not reset / sell / convert `dca-paper`.
- Do not mix sleeve PnL into this score.
- Do not place paper or live Kraken orders from this page.

---

## Look-ahead bugs this recipe can hit

Named so a later implementer can grep for them. Hitting one invalidates the slice.

### B1 — Repainting swings

**How it shows up:** zigzag last-pivot, `argrelextrema` without right-lag, “swing = highest high of last 200 bars” updated every bar so the origin of the fib **moves**. Retracement 0.618 from a pivot that later disappears.

**Tell:** rails at bar `t` change when you recompute at `t+1` **without** a new **confirmed** swing. Replay from a stored `rails[t]` must match a causal pass.

**Stop:** S1 (`N=8` confirm). Unconfirmed candidates are not rails.

### B2 — Using a future high for fib

**How it shows up:** `H = max(high[2023-01-01 : 2023-12-31])` then arm January. Same: max of the **slice file**; 24h high that includes the still-open day; using the 2026-08-27 public 24h high **1.26778** as a 2023 TP; XRPUSD high mapped onto XRPEUR.

**Tell:** a rung at time `t` needs a bar `u > t` to exist. `H` and `L` must be confirmed swings with confirmation time `≤ t`.

**Stop:** rails from the swing on **this pair only**, confirmed, lagged.

### B3 — Filling both sides the same bar

**How it shows up:** `low <= P_entry` and `high >= P_tp` on one 15m candle → book buy **and** sell, +1.83% gross before fees, 2 fills toward the gate. OHLC path unknown. Wide XRP wicks make this common.

**Tell:** two prints with the same bar timestamp. Fill count jumps by 2 on one close.

**Stop:** at most one resting limit (L4). At most one fill per bar. Dual touch → `DUAL_TOUCH_SKIP`, not a round-trip.

### B4 — Arm-bar / unclosed-bar fills (cousin of B3)

Decision at close(`t`) using `high[t]/low[t]` to fill the order you just armed. Or using the forming candle.

**Stop:** eligible from `t+1`. Forming bar dropped.

### B5 — Close-cross without touch (cousin of L2)

Filling because `close` is beyond `P` without checking `high`/`low`. On honest OHLC this should coincide with a touch; on corrupted rows (close outside H/L) it is a data bug — **drop the bar**, do not fill.

### B6 — Walk-forward contamination

Tuning `N`, which two rungs to start, size, or “skip chop” flags on 2023–2026 then reporting those years as OOS. Splicing `c9689f5d`’s 20 fills, or live 00029, into the historical count.

**Stop:** parameters locked in this file. Clip and live paper are other rows.

### B7 — Public OHLC cap labelled as 2023

Kraken `OHLC` interval 15 returns **721** recent bars (this sitting: first `2026-08-20 07:45 UTC` → last `2026-08-27 19:45 UTC`). `since=1672531200` (2023-01-01) **does not** rewind it. That window overlaps the sealed lab clip. Calling it 2023 is B7 + attack 1.

**Stop:** a disclosed 15m XRPEUR **archive** with first closed bar `≤ 2023-01-01` and no future bars. This repo does not contain that archive. This pack does not fetch one into git.

### B8 — Cross-convention fib (cousin of B2)

`above = H + 1.618 * range` vs locked `H + 0.618 * range`. Retracements measured from `H` downward with a 0-at-end tool mixed with 0-at-start extensions. Silent rung shift, looks “full set.”

**Stop:** the formula in L3.

---

## Walk-forward protocol (how to apply, still not a score)

1. **Load causal 15m XRPEUR** covering warmup + slice. Reject a feed whose first bar is after 2023-01-01 for a 2023 slice. Reject a feed that is the trailing ~720 public bars.
2. **Warmup** until the first dual confirmation (`H` and `L`) with confirmation time `< 2023-01-01` if possible; else the first confirmation **inside** 2023, with no fills before confirmation.
3. **Pick the first working pair** from the full rung set: nearest buy-eligible rung **below** last close as `P_entry`, nearest rung **above** last close as `P_tp`. If none above or none below, wait. Do not skip to extensions that require an unconfirmed move.
4. **Step bar by bar** from the first scored close: confirm swings → maybe recompute rungs → if working prices still exist, keep them until a fill; if a rail is invalidated because the confirmed swing **replaced** them, cancel the rest and re-pick at that close (cancel is **not** a fill). Then apply L2/L4.
5. **Count prints**, not rests. Cancel / skip / `DUAL_TOUCH_SKIP` are not fills.
6. **Equity** after each fill: start 10000 EUR simulated; subtract notional × taker% on each print; mark inventory at close **only for maxDD**, but **gate 1** is realized return after fees (closed round-trips), not an open mark.
7. **Report three fee columns.** Gate conjuncts on **this simulated book**. Do not write the result into `invert-paper`.
8. **Slices stay separate:** 2023 · 2024 · 2025 · 2026-YTD (excluding treating the 8-day clip as a slice). A later 2023 slice page owns the 2023 numbers. This file owns the method.

**Starting inventory:** `FLAT_EUR`. Do not start long from a fictional 2022 bag.

---

## Verdict: **GREEN** (locks) · **RED** (promotion / pretending this is a score)

| Probe | Result | Color |
|---|---|---|
| Method locks L1–L6 written, adversarial first | This file | **GREEN** (pack) |
| 8-day `c9689f5d` as this walk-forward | Forbidden | **RED** if used; **GREEN** if cited-not-scored |
| Reset `invert-paper` / `dca-paper` | Forbidden | **GREEN** (not touched) |
| 2023 fill count / return / maxDD in this file | None (must not invent) | **YELLOW** (unscored) |
| Public OHLC as 2023 history | ~721 bars of **2026-08-20…27**, not 2023 | **RED** as data; **GREEN** as disclosed trap |
| Look-ahead B1/B2/B3 named with stops | Repaint / future high / same-bar dual fill | **GREEN** (named) |
| Spot naked short | Banned; buy-back after sell-TP | **GREEN** |
| Fees 0.26 default + shadow 0.40 and 0.80 | Locked | **GREEN** |
| Live / keys / 10k as deposit | Out of scope | **GREEN** (not done) |
| Promotion of invert as proven | n=method only; live invert-paper still 1 fill | **RED** |

**Promotion: no.** Stay paper. Gate on live `invert-paper` remains **NOT MET**. This pack does not greenlight 2023 either — it has **no 2023 prints**.

---

## RED

### R1 — Do not score the lab clip as 2023+

`c9689f5d` is a sealed 8-day PASS. Walk-forward-from-2023 is a **new** simulated book. Adding 20 clip fills, restamping PASS, or rotating the hash to match a journal republish is promotion fraud. Cite only.

### R2 — Do not use the public OHLC cap

This sitting: Kraken 15m XRPEUR OHLC `n=721`, first **2026-08-20 07:45 UTC**, last **2026-08-27 19:45 UTC**, last ~**1.25018**, 24h high **1.26778**. That is **not** 2023. A slice that “just curls OHLC” is scoring last week.

### R3 — Do not promote

No 2023 archive in this git tree. No invented PASS. Live invert-paper: **1** fill. Paper engine still omits slippage and partials even when a historical replay is honest. First live size is a **later** page after a **real** walk-forward gate on `invert-paper`, not after a method markdown.

---

## YELLOW

### Y1 — 2023 archive missing here

`/workspace/paper-recipes/` is not in `solana-invoice`. This pack cannot see `invert-paper.md` text except as the Surge summary. Full 2023 15m XRPEUR is not in git. Slice researchers must **disclose source** (CSV hash, first/last bar, gap list). Unknown source = do not stamp GREEN on the slice.

### Y2 — Live TP equals 24h high; not a fib lesson for 2023

Public 24h high **1.26778** = live TP `PAPER-00030`. That is the **live paper** book, possibly a 24h-H latch, **not** permission to use rolling 24h high as 2023 rails (that is B2). Do not backfill 00030 from this method.

### Y3 — Connector / CLI

Kraken MCP may error. `which kraken` may be empty. This method does not require a live engine dump. It also must not be “implemented” by placing paper orders.

### Y4 — Allowlist fork

Journal (2026-08-26): XRPEUR, XLMEUR, HBAREUR, ADAEUR, QNTEUR, XDCEUR, ALGOEUR. CODER.md lists a wider EUR set. **This walk-forward is XRPEUR only** (on both lists). Expanding to the union is WAIT, not a 2023 diversification study.

### Y5 — Gap-through and wick-touch vs live queue

Touch-fill at `P` is already optimistic vs live LIMIT queue (paper skill: instant full fills, slippage 0). Gap shadow at `open` is the honesty column, not a reason to skip default 0.26.

---

## GREEN

### G1 — Clip cited, not resealed

Full sha256 quoted above. Name `fib-grid-invert-xrpeur-15m`. Sleeve FAIL on that lock stays FAIL and stays out of this spot replay.

### G2 — Live books left alone

No `paper reset` on `invert-paper` or `dca-paper`. No flatten of 00030/00028. No sixth DCA slice. No Phantom send. No API keys.

### G3 — Recipe matches the invert lock, with path rules the 8-day clip did not have to spell

15m. Full fib set. After **any** fill, swap jobs of **those two** prices. Re-arm only on the opposite fill. Spot: no naked short; after sell-TP, flat EUR; next entry buy-back. **Plus** closed-bar decisions, touch-only intra-bar, no dual fill, causal `N=8` swings, fees 0.26/0.40/0.80.

### G4 — Gate language not redefined

Still: return > 0 after fees **and** ≥ 8 prints **and** maxDD ≤ 8%, on the book you claim. This method does not replace that gate with “method exists.”

### G5 — FACTUUR / keys / treasury

Out of this research. Treasury receive strings stay Wallet’s, never Kraken float:

- Solana USDC `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3`
- Base USDC `0x9eb954b567ef3616424a6e1bf42c63724930aa54`

---

## NOTES

- **Report-only.** No paper order, no live order, no journal HTML patch, no shop edit, no mail, no reseal, no reset. Sibling Coder 01/02 (#132 / #144) own the **live** invert-paper gate. This file owns **how** a 2023+ 15m replay must not look ahead.
- **Sources:** operator/Coder invert lock (Surge journal https://dca-paper-journal.surge.sh/ this sitting: fills **1**, clip cited, recipe summary); PR #132 `01-adv-research.md`; PR #144 `02-adv-plan.md`; PR #118 `docs/ultra-seats/CODER.md`; Kraken public `AssetPairs`+`Ticker`+`OHLC` interval 15 XRPEUR at 2026-08-27 ~19:45 UTC (721 bars, **not** 2023); `kraken-paper-strategy` (0.26% taker, no slippage/partials); `kraken-paper-to-live`; `kraken-autonomy-levels` (level 2 = paper).
- **Retired hashes stay retired.** `2bfb1b68` / `9056f296` / `094513` are not this walk-forward.
- **Tax (not advice):** a simulated 2023 replay is not a tax event. Paper is not a tax event. Phantom sales-USDC = beroepsinkomen. Live Kraken later = apart handelsdossier. No invented FIFO. No CAP from this markdown.
- **PII:** no personal mailbox, no IBAN, no invented KBO. Operator: natural person, Geel. **KBO/BTW: nog niet toegekend.**
- Concurrent slice agents (2023 numbers, 2024–26 numbers, data-archive research) must **follow** this pack. They must not **reseal** it with a PASS line.

**Promotion: no.** Stay paper. Do not reseal `c9689f5d`. Do not reset `invert-paper`. Do not reset `dca-paper`. Do not treat last week’s OHLC as 2023. Name B1/B2/B3 before any slice claims GREEN.

---

## Re-check (copy/paste)

```bash
# This pack must exist and must not contain a fake 2023 PASS:
rg -n 'c9689f5d|DUAL_TOUCH_SKIP|0\.236|naked short|0\.80' docs/rgy-2026-08-27/coder/RESEARCH-invert-walkforward.md

# Public OHLC is NOT 2023 (expect ~720 bars, first ts in 2026 if run near this sitting):
curl -sS 'https://api.kraken.com/0/public/OHLC?pair=XRPEUR&interval=15' \
  | python3 -c "import json,sys,datetime; d=json.load(sys.stdin); k=[x for x in d['result'] if x!='last'][0]; r=d['result'][k]; print(len(r), datetime.datetime.fromtimestamp(r[0][0], datetime.UTC), datetime.datetime.fromtimestamp(r[-1][0], datetime.UTC))"

# Live journal is a different book — do not write 2023 into it:
curl -sS https://dca-paper-journal.surge.sh/ | rg -n '0 fills|fills 1|PAPER-00029|NOT MET|c9689f5d|naked short'

# Never:
# kraken paper reset --workspace invert-paper
# kraken paper reset --workspace dca-paper
# kraken order …
```

Count historical prints only from a **causal** 15m XRPEUR archive under L1–L6. If a slice cannot name its first bar and its swing-confirm lag, it is not this method. Still paper.
