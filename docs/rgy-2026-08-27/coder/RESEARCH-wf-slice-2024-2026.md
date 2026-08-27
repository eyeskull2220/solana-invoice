# RESEARCH — invert-wf-2023 year-slice packs (2024 · 2025 · 2026-YTD)

**Seat:** RESEARCHER · Coder lane  
**Lens:** adversarial **first**, then RED / YELLOW / GREEN. Research only. Not a plan. Not a fill. Not a scoreboard.  
**Date:** 2026-08-27  
**As-of:** 2026-08-27, Europe/Brussels (CEST, UTC+2)  
**Stamp:** VOORBEELD · paper / simulated · not FACTUUR · not INVOICE · not live-trade advice  
**HEAD (this repo):** `2170952`  
**Still paper.** Docs only. No orders. No keys.

This file packs **three diagnostic year slices** onto the named walk-forward `invert-wf-2023`:

| Pack | Window (Europe/Brussels, inclusive start, exclusive end except “now”) |
|---|---|
| **2024** | 2024-01-01 00:00 → 2025-01-01 00:00 |
| **2025** | 2025-01-01 00:00 → 2026-01-01 00:00 |
| **2026-YTD** | 2026-01-01 00:00 → **now** 2026-08-27 (this sitting) |

Pair / recipe: **XRPEUR 15m invert** (full fib set; after any fill swap those two prices; re-arm only on the opposite fill; spot no naked short).

**One continuous book with the 2023 slice. Not three reset books.** Combined score is the book. Slices are diagnostics.

This file does **not** place orders, does **not** paste keys, does **not** spend Phantom, does **not** rewrite shop HTML, does **not** reseal `c9689f5d`, and does **not** reset `invert-paper` or `dca-paper`.

---

## What this file is allowed to claim

| Claim | Status in this file |
|---|---|
| Slice **windows** in Europe/Brussels | Defined below |
| Why each year **stresses invert** (range / trend / crash / ETF-flow) | Researched from public XRPEUR path + cited events |
| **Checklist** each slice must report when a run exists | fills · return after fees · maxDD |
| Combined gate / score | **The continuous book**, not a year winner |
| Invert scores for 2024 / 2025 / 2026-YTD | **Not run. Not invented.** |
| 8-day lab clip as this walk-forward | **Forbidden.** Cite only. |
| Reset `invert-paper` to host a year replay | **Forbidden.** |

---

## Live operator book (not these slices)

https://dca-paper-journal.surge.sh/ fetched this sitting (republish **2026-08-27 21:10 Europe/Brussels**):

| Field | Value | Counts as invert-wf-2023 year-slice score? |
|---|---|---|
| Named live book | `invert-paper` · EUR 10000 | **No.** Different layer from historical WF packs. |
| **PAPER-00029** | FILL 1 · buy XRPEUR **160.64773 @ 1.24496** · 20:56:53 Europe/Brussels · cost 199.99999794 · fee 0.26% = 0.52 | **No.** Live paper print, not a 2024/2025/2026-YTD WF fill. |
| **PAPER-00030** | Resting TP sell LIMIT 160.64773 @ **1.26778** | **No.** Resting is not a fill. |
| **PAPER-00028** | Open buy LIMIT @ **1.23084** vol 162.49066 | **No.** Open is not a fill. |
| Journal fills | **1** (need ≥ 8) | Live gate only. |
| Journal return after fees | **−0.003979%** (or current mark) | Live n=1 mark. Not a year-slice return. |
| Journal maxDD | **0.003979%** | Live n=1. Not a year-slice maxDD. |
| Gate | **NOT MET** | Live book. |

Do not copy those three numbers into the 2026-YTD pack. Do not add 00029 as fill 21 of the 8-day clip. Do not reset this book to “start 2024 clean.”

---

## Adversarial first

Attacks that would fake a green multi-year invert. Each is a **stop**.

1. **Invent slice scores.** No invert-wf-2023 engine dump for 2024, 2025, or 2026-YTD exists in this git tree, on Surge, or from Kraken MCP (namespace **error** this sitting). Filling fills / return-after-fees / maxDD from “typical invert” or from daily OHLC path-through is cheating. **Leave the score cells blank / NOT RUN.**

2. **Treat the 8-day lab clip as this run.** Sealed window XRPEUR 15m **2026-08-18 21:00 → 2026-08-26 08:00 Europe/Brussels**. Spot: **20 fills · +0.681154% · maxDD 0.890854% · PASS** vs  
   `sha256:c9689f5d7d583320e724900b0ce4ef68193878c880d11939badd1dd59016e390`  
   That clip sits **inside** 2026-YTD on the calendar and is still **not** the 2026 pack, not fill 21, not funding proof. Do not reseal. Do not paste +0.68% into 2026-YTD.

3. **Three reset books.** `invert-wf-2024` init 10k, `invert-wf-2025` init 10k, `invert-wf-2026` init 10k, then pick the pretty year. That **hides** path dependence (size after 2023, DD that crosses 31 Dec, rung state at year-end). Packs are **slices of one book**.

4. **Reset live `invert-paper` to host a year replay.** Live book already has PAPER-00029. `paper reset` / `paper init` on that workspace destroys the operator ledger. Historical packs, if they ever run, do **not** cannibalize `invert-paper`. `dca-paper` stay. `c9689f5d` stay sealed.

5. **Score a year as if it were the gate.** Gate language (Coder #118 / #132 / journal): return > 0 **after fees** **and** ≥ 8 **prints** **and** maxDD ≤ 8% on the **named book you want to promote**. A 2024 diagnostic that “looks green” while the continuous book is red is not a fund memo. Combined score = **the book**.

6. **Call max(year maxDD) the book maxDD.** A drawdown can **open in December and close in February**. Book maxDD is one continuous equity peak-to-trough. Slice maxDD is “how ugly was this window,” including unfinished DD at the cut.

7. **Backfill fills from Kraken public OHLC.** Public **15m** OHLC this sitting: **721** candles, **2026-08-20 09:45 → 2026-08-27 21:45 Europe/Brussels** (~**7.5 days**). `since=0` does **not** extend it. Year packs need a **historical 15m pack** (sibling data research). Daily/weekly path is **regime context**, not invert prints.

8. **Count 2024 “ETF” as XRP spot ETFs.** US **Bitcoin** spot ETFs began trading **2024-01-11**. US **XRP** spot ETFs are a **2025-Q4** event (Canary XRPC **2025-11-13**, Bitwise **2025-11-20**, Grayscale GXRP **2025-11-24**; REX-Osprey XRPR earlier **2025-09-18**). 2024 stress = **BTC-ETF-era + XRP range, then Nov–Dec 2024 breakout**. Do not write “XRP ETF 2024” into the pack name.

9. **Use USD ATH as XRPEUR invert score.** Public USD ATH cites **~$3.66 on 2025-07-18**. Kraken **XRPEUR daily** 2025 high this dump: **3.2989 on the 2025-01-16 UTC daily candle**. Invert is **XRPEUR**. Quote EUR candles for the pair; cite USD ATH only as a **regime marker**.

10. **Promote because 2026-YTD includes today’s live ticker.** Kraken public XRPEUR this sitting: last **~1.246**, 24h high **1.26778** (exact live TP), 24h low **1.19568**. A live tag is not a WF fill. Paper does not model partials or queue.

11. **Mix sleeve / DCA / leftover fib into a year pack.** 3x sleeve FAIL (6 fills, −2.729078%, maxDD 5.326685%) is **not** the gate. `dca-paper` five BTCUSD slices stay held. `fib-paper` leftover BTCUSD is not XRPEUR invert.

12. **Rush 8 fills by slicing until a slice has 8.** Extra clips, extra pairs, or “only count the trending months” is gate-cheating. Re-arm only on the opposite fill of XRPEUR.

13. **Treat journal n=1 maxDD 0.003979% as 2026-YTD maxDD.** Sample of one live print. Walk-forward 2026-YTD is **NOT RUN**.

14. **Collapse timezone.** Cuts are **Europe/Brussels**. Kraken OHLC timestamps are **UTC**. DST: CEST (UTC+2) in summer; CET (UTC+1) after last-Sunday-October. Do not shift a 31 Dec 23:00 UTC bar into the wrong year silently.

15. **Call this file a run.** Packs + checklist + regime map. **No engine JSON. No invented equity curve.**

---

## Verdict: **RED** (scores / promotion) · **GREEN** (pack shape / locks)

| Probe | Result | Color |
|---|---|---|
| 2024 / 2025 / 2026-YTD invert fills, return after fees, maxDD | **NOT RUN** — not invented | **GREEN** as honesty; **RED** as proof |
| Combined score is the continuous `invert-wf-2023` book | Locked below | **GREEN** (lock) · **RED** (no book score yet) |
| Three reset books / yearly `paper init` | Forbidden | **GREEN** if not done; **RED** if a later page does it |
| 8-day `c9689f5d` as 2026-YTD or as this WF | Forbidden | **GREEN** (cited, not used as score) |
| Reset live `invert-paper` | Forbidden | **GREEN** this file |
| Public 15m depth vs year packs | ~7.5 days only | **YELLOW** (data blocker for a **run**, not a fake score) |
| Kraken MCP / `kraken` CLI this VM | Error / missing | **YELLOW** |
| Still paper / no keys / no orders | This PR | **GREEN** |

**Promotion / funding: no.** Stay paper. Gate on live `invert-paper` is **NOT MET** (fills 1). Historical year packs are **not** a workaround.

---

## Book vs packs (continuous)

```
invert-wf-2023  (ONE book, ONE equity, ONE fill counter, ONE peak)
├── 2023 slice     (sibling RESEARCH — not scored here)
├── 2024 pack      diagnostic window
├── 2025 pack      diagnostic window
└── 2026-YTD pack  diagnostic window → 2026-08-27 BXL
```

**Carry across 31 Dec (do not reset):**

- Cash / inventory / open working orders (entry vs TP jobs on the two live prices)
- Running fill count (book-level)
- Peak equity used for **book** maxDD
- Fee shadow ledger
- Fib-rail state implied by the last print (do not rebuild rails from a fresh mid on 1 Jan)

**What a slice may report (diagnostics only):**

- Prints whose **fill timestamp** falls in the Brussels window
- Slice **contribution** to shadowed PnL (sum of round-trips **closed** in-window; open MTM at the cut is labeled **mark, not gate-1**)
- Slice maxDD = peak-to-trough **inside the window**, plus whether book DD was **open at the cut**

**What a slice may not do:**

- Restart capital at 10k
- Drop working limits
- Zero the fill counter
- Claim gate-green because that year alone printed ≥ 8

If a later Coder **run** page exists, it names **one** workspace for the whole WF (suggested: `invert-wf-2023`). It does **not** `init`/`reset` live `invert-paper`.

---

## Time cuts (Europe/Brussels)

| Pack | Start | End | Notes |
|---|---|---|---|
| 2024 | 2024-01-01 00:00 CET (UTC+1) | 2025-01-01 00:00 CET | Leap year. 366 calendar days → **35 136** 15m bars **if** the 15m pack is complete. |
| 2025 | 2025-01-01 00:00 CET | 2026-01-01 00:00 CET | 365 days → **35 040** 15m bars if complete. DST end 2025-10-26. |
| 2026-YTD | 2026-01-01 00:00 CET | **now** 2026-08-27 CEST | Incomplete year. Do not pad to 31 Dec. This sitting ~21:56 BXL. Daily Kraken last close **1.24672** (2026-08-27 UTC daily candle). |

Align engine bars to **Europe/Brussels** for slice membership. If the 15m pack is stored in UTC, convert then cut — do not cut UTC midnights and call them Brussels years.

**2023 continuity:** the 2024 pack **opens with whatever the 2023 slice closed** (position, cash, peak). This file does not invent that close.

---

## Data that exists vs data that does not

Fetched **2026-08-27 ~19:56 UTC** from `https://api.kraken.com/0/public/OHLC` and `Ticker` (no keys).

| Series | What Kraken public returned this sitting | Enough to **run** XRPEUR 15m invert year packs? |
|---|---|---|
| Ticker XRPEUR | last ~1.246; 24h H **1.26778**; 24h L **1.19568**; 24h VWAP ~1.24475 | No (spot check only) |
| OHLC 15m | n=721 · ~7.5 days · 2026-08-20 09:45 BXL → 2026-08-27 21:45 BXL | **No** |
| OHLC 60m | n=721 · from 2026-07-28 | **No** |
| OHLC 240m | n=721 · from 2026-04-29 | **No** |
| OHLC 1440m (daily) | n=721 · **2024-09-06 → 2026-08-27** UTC | Regime **from Sep 2024**; **not** Jan–Aug 2024 15m |
| OHLC 10080m (weekly) | n=485 · 2017-05-18 → 2026-08-27 | Regime **including 2023–2024**; **not** invert prints |

**YELLOW — run blocker:** year-slice **execution** waits on a historical XRPEUR **15m** pack covering 2024-01-01 BXL through now (sibling: XRPEUR 15m data 2023+). This RESEARCH still **defines** the packs. It does not pretend daily bars are 15m fills.

Gaps to log when a 15m pack arrives (do not invent them): missing bars, duplicate timestamps, weekend holes, DST duplicates/skips. Incomplete pack → slice **NOT RUN**, not “assume flat.”

---

## Regime map — why these years stress invert

Invert (15m, full fib both sides, swap jobs after a print, no spot naked short) dies in different ways:

| Stress | What it does to invert | Where it shows in these packs |
|---|---|---|
| **Long range / chop** | Many rung touches → fee grind; false opposite-fills | 2024 Jan–Oct |
| **One-sided breakout** | The “wrong” side never prints; inventory / missed re-arm | 2024 Nov–Dec; 2025-01; 2025-07 |
| **Air-pocket crash** | Working buys through; maxDD; TP never reached | 2025-10; 2026-02; 2026-06–08 |
| **ETF-flow vs price** | Narrative “institutionally bid” while spot still trends down — mark-to-market trap | 2025-11+ and 2026 YTD |

Public **price path** below is **XRPEUR on Kraken**, not invert PnL.

### 2024 — ETF-era range, then breakout

**Macro (not XRP ETFs):** US spot **Bitcoin** ETFs launched **2024-01-11**. XRP spent most of the year **range-bound** under SEC-overhang, then **broke** in Nov–Dec.

**Kraken XRPEUR weekly (Brussels membership, this dump):**

- **2024 full:** n=52 weeks · open **0.53347** · close **2.24566** · **low 0.35311** (week of 2024-07-04 CEST) · **high 2.75902** (week stamped 2024-11-28 CET — daily pin below)
- **2024 Jan–Oct only:** n=44 · close **0.50483** · **high 0.68103** (week of 2024-03-07) · **low 0.35311**

**Kraken XRPEUR daily (only from 2024-09-06):**

- Sep–Oct still ~**0.45–0.59**
- Nov daily high **1.85** · close **1.8439**
- Dec daily high **2.75902** on **2024-12-03** UTC daily · YE close **2.00824**

**Invert stress:**

1. **Jan–Oct range** (~0.35–0.68 weekly): classic mean-reversion **and** death-by-0.26%-taker if the engine over-trades every 15m wick. Gate-1 after fees can fail while “price went nowhere.”
2. **Nov–Dec vertical:** range rails go stale in days. Spot invert **cannot** flip to a naked short after a sell-TP — it goes **flat cash** and must buy-back. A year diagnostic that only keeps the range months is cheating.

**Not in this pack’s name:** US spot XRP ETFs (those are 2025).

**Scores (fills / return after fees / maxDD):** **NOT RUN.**

### 2025 — two spikes, a crash, then XRP ETFs into a down-close

**Kraken XRPEUR daily (full year in the 721-day window):**

| Marker | XRPEUR daily (UTC candle date) |
|---|---|
| Open 2025-01-01 | 2.00823 |
| **Year high** | **3.2989** on **2025-01-16** |
| Jul swing high | 3.14748 (July daily high; USD ATH ~**3.66 on 2025-07-18** is a **USD** marker, not this EUR high) |
| **Year low** | **1.24** on **2025-10-10** |
| Close 2025-12-31 | 1.56607 |

Monthly daily highs/lows (UTC months, same dump): Jan 3.2989 / 2.00666 · Feb 2.96382 / 1.7123 · Mar 2.90 / 1.752 · Apr 2.08033 / 1.46352 · May 2.38428 / 1.83197 · Jun 2.03849 / 1.65911 · Jul 3.14748 / 1.8222 · Aug 2.89951 / 2.357 · Sep 2.71368 / 2.29961 · Oct 2.645 / **1.24** · Nov 2.23178 / 1.58071 · Dec 1.90584 / 1.5112.

**Cited 2025 event layer (not invert scores):**

- Mid-2025: Ripple/SEC path resolved enough for ETF plumbing (appeals dropped **2025-08-07** in public reporting).
- Regulated XRP futures seasoning through 2025 (Bitnomial Mar; CME May — Ripple insights **2026-04-17**).
- US spot XRP ETF **wave in Nov 2025**: Canary XRPC **2025-11-13**; Bitwise **2025-11-20**; Grayscale GXRP **2025-11-24**; Franklin XRPZ / 21Shares TOXR shortly after; REX-Osprey XRPR **2025-09-18**. First-month no net outflow days; **~$1B** cumulative inflows by **2025-12-16** (Ripple).

**Invert stress:**

1. **January extension** (2.00 → 3.30): trend run; leftover range inventory from 2024 YE is the **continuity** test.
2. **Feb–Jun chop under 3:** fee grind after a spike — not the same as 2024’s 0.50 range.
3. **July second spike** then fade: two “ATH-ish” regimes in one year. A slice that reports only July is cherry-picking.
4. **October air pocket to 1.24:** maxDD candidate. Book DD may **start** before 1 Oct and **end** after.
5. **Nov–Dec ETFs while price closes 1.57, down from 3.30:** “ETF launched” ≠ invert green. Do not mark-to-market the narrative.

**Scores:** **NOT RUN.**

### 2026-YTD — lower-high, grind, August flush, bounce to ~1.25 (through 2026-08-27)

**Kraken XRPEUR daily 2026-01-01 → 2026-08-27:**

| Marker | XRPEUR daily |
|---|---|
| Open 2026-01-01 | 1.56611 |
| **YTD high** | **2.06198** on **2026-01-06** |
| **YTD low** | **0.852** on **2026-08-14** |
| 2026-08-27 daily | O 1.22009 · H **1.26778** · L **1.19568** · C **1.24672** |

Monthlies: Jan 2.06198 / 1.26816 · Feb 1.41903 / 0.951 · Mar 1.39748 / 1.12791 · Apr 1.27761 / 1.11027 · May 1.32715 / 1.09225 · Jun 1.14964 / 0.8855 · Jul 1.03499 / 0.89545 · Aug (through 27) 1.45274 / **0.852**.

**Cited 2026 event layer:**

- ETF **inflows continued** while spot was **not** making new highs: Ripple (Apr 2026) ~**$1.50B** by early March; later public flow prints ~**$1.5–1.6B** into Aug 2026. Bitwise 10-Q path: XRP **$1.82 → $1.04** in H1 2026 on the USD principal-market series they report — **USD**, not a substitute XRPEUR invert score.
- **Do not** treat the sealed 8-day window **2026-08-18 21:00 → 2026-08-26 08:00 BXL** as the 2026-YTD pack. That window is **after** the 2026-08-14 daily low and is a **lab clip**, not walk-forward.

**Invert stress:**

1. **Jan fade from 2.06:** failed retest of 2025 highs.
2. **Feb break of 1.00 (0.951 low):** crash-through of working bids.
3. **Jun–Jul grind 0.89–1.03:** range again, but **after** a halved book in EUR terms from 2025 — continuity of size matters.
4. **Aug 14 low 0.852 then bounce to ~1.25 / tag 1.26778:** exactly the kind of wick that fools a 15m invert **and** fools a researcher who pastes the 8-day PASS.

**Scores:** **NOT RUN.** Live `invert-paper` fill 1 is **not** this cell.

---

## Checklist (every slice, when a run exists)

Copy this table into a later **run** page. Until then, cells stay **NOT RUN**.

### Per-slice diagnostic (not the gate)

| Cell | Rule |
|---|---|
| **fills** | Count `PAPER-*` **prints** whose fill time is inside the Brussels window. Resting limits = 0. Cancels = 0. Do not import live 00029 into 2024/2025. Do not import `c9689f5d`’s 20. |
| **return after fees** | Shadowed, round-trip: engine **0.26% taker per print** + conservative extra (spread/slippage **not** zero because the engine said 0). Closed round-trips in-window. Open MTM at the cut = **mark**, labeled, **not** gate-1. |
| **maxDD** | Peak-to-trough **in-window** on the **same continuous equity**. Also flag: “book DD open at start/end of slice? yes/no.” Unknown ≠ ≤ 8%. |
| **bars** | 15m bars present / expected; gap list. Incomplete → NOT RUN. |
| **carry-in / carry-out** | Cash, inventory, working two-price jobs, running book fills, book peak. |

**Fail any honesty check → do not color the slice green.**

### Combined score = the book

Gate (all three, **one** book — `invert-wf-2023` when that run exists; live promotion still names **`invert-paper`** per Coder lock):

1. Return > 0 **after fees** (shadowed) on the **full** continuous path (2023 slice + these packs, no yearly restart).
2. Fills ≥ 8 **prints** on that book (not 8 per year, not 20 from the lab clip, not 1 from live 00029 added to a replay).
3. maxDD ≤ 8% from **book** peak equity.

| Combined cell | 2026-08-27 |
|---|---|
| invert-wf-2023 fills | **NOT RUN** |
| invert-wf-2023 return after fees | **NOT RUN** |
| invert-wf-2023 maxDD | **NOT RUN** |
| Live `invert-paper` (operator, not WF) | fills **1** · return after fees **−0.003979%** (journal) · maxDD **0.003979%** (journal) · **NOT MET** |
| Lab clip `c9689f5d` | 20 / +0.681154% / 0.890854% · **not this book** |

A later agent who writes “2024 GREEN, 2025 GREEN, 2026 GREEN therefore fund” without a **book** row has failed this file.

### Empty scoreboard (intentionally blank)

| Pack | fills | return after fees | maxDD | Notes |
|---|---|---|---|---|
| 2023 (sibling) | — | — | — | Not this file |
| **2024** | **NOT RUN** | **NOT RUN** | **NOT RUN** | Range then Nov–Dec breakout |
| **2025** | **NOT RUN** | **NOT RUN** | **NOT RUN** | Jan/Jul spikes · Oct 1.24 · Nov ETFs |
| **2026-YTD** | **NOT RUN** | **NOT RUN** | **NOT RUN** | Through 2026-08-27 BXL · **not** the 8-day clip · **not** live 00029 |
| **Book `invert-wf-2023`** | **NOT RUN** | **NOT RUN** | **NOT RUN** | Combined score lives here |

---

## RED

### R1 — No invented invert numbers

This sitting has **no** invert-wf-2023 history JSON. Daily/weekly XRPEUR **is** a path. Path ≠ fills. Do not simulate “would have filled every 0.382” from OHLC in this research.

### R2 — 8-day clip is not 2026-YTD and not this WF

Lab: 2026-08-18 21:00 → 2026-08-26 08:00 BXL · 20 fills · +0.681154% · maxDD 0.890854% · `c9689f5d…`. Cite. Do not reseal. Do not 20+1 with PAPER-00029.

### R3 — Do not reset `invert-paper`

Live fill 1 is the operator gate book. Year packs are **not** permission to `paper reset invert-paper`. Also do not reset `dca-paper`.

### R4 — Do not promote

Paper-to-live still wants multi-session paper, human yes, healthy connector. Live `invert-paper` **NOT MET**. Historical packs **NOT RUN**. Kraken MCP **error**. Autonomy **2**.

---

## YELLOW

### Y1 — 15m history is not in the public 720-candle window

Year packs are specified; **execution** needs a stored 15m pack. Public OHLC 15m ≈ last **7.5 days** only. Sibling data research owns how to fetch/store it. This file does not invent a vendor.

### Y2 — Daily coverage of 2024 is incomplete until Sep 6

Jan–Aug 2024 XRPEUR **daily** is **not** in the 721-day daily dump. Weekly covers it. When 15m arrives, **verify** Jan–Aug 2024 rather than splicing weekly closes into 15m.

### Y3 — USD vs EUR extrema

2025 USD ATH (~3.66 on 2025-07-18) ≠ Kraken XRPEUR daily high **3.2989** on **2025-01-16**. Always label currency.

### Y4 — Journal vs older Coder 01

PR #132 recorded Surge at **0 fills**. Live journal this sitting prints **fills 1** (republish 21:10 BXL). Trust **current** operator/journal for live `invert-paper`. Still do not treat that as WF-2026.

### Y5 — Connector

Kraken MCP: error. `which kraken`: empty here. `/workspace/paper-recipes/` not in this git tree. Do not invent engine qty for a WF that has not run. (Live 00029 qty **160.64773** is a **journal** fact for invert-paper only.)

---

## GREEN

### G1 — Pack shape

Three **windows**, one **book**, checklist without numbers. Combined score named as the book.

### G2 — Locks held on this run

No orders. No keys. No Phantom. No reseal. No `invert-paper` reset. No `dca-paper` reset. No shop HTML. No FACTUUR.

### G3 — 8-day clip excluded from scores

Quoted in full as the journal prints it. Not copied into the empty scoreboard.

### G4 — Sleeve / DCA / fib leftover excluded

Not mixed into year packs.

### G5 — XRPEUR is the invert pair

Allowlisted on journal (seven EUR pairs, ticker-confirmed 2026-08-26) and on Coder seat. These packs do not add SOLEUR/ETHEUR to “get fills.”

---

## NOTES

- **Report-only.** Sibling PLAN invert-wf-2023 / 2023-slice RESEARCH may exist in parallel. This file does not implement a runner.
- **Sources:** Kraken public `Ticker` + `OHLC` (15 / 60 / 240 / 1440 / 10080) 2026-08-27 ~19:56 UTC; live journal https://dca-paper-journal.surge.sh/ (21:10 BXL republish); Coder `01-adv-research.md` PR #132; Coder `02-adv-plan.md` PR #144; `docs/ultra-seats/CODER.md` PR #118; Ripple “XRP ETFs: The Institutional Era Has Begun” (2026-04-17); public USD ATH / ETF date reporting as **regime markers**. Kraken MCP: **error**.
- **Tax (not advice):** paper is not a tax event. No invented FIFO. No CAP from a WF that has not run.
- **PII:** no mailbox, no IBAN, no invented KBO. Operator: natural person, Geel. **KBO/BTW: nog niet toegekend.**

**Promotion: no.** Stay paper. Do not invent scores. Do not treat the 8-day clip as this run. Do not reset `invert-paper`. Combined score is the book. Slices are diagnostics.

---

## Re-check (copy/paste)

```bash
# live operator book — do not reset
curl -sS https://dca-paper-journal.surge.sh/ | rg -n 'fills 1|PAPER-00029|c9689f5d|8-day|NOT MET|invert-paper'

# public path (regime only — not invert fills)
curl -sS 'https://api.kraken.com/0/public/Ticker?pair=XRPEUR'
curl -sS 'https://api.kraken.com/0/public/OHLC?pair=XRPEUR&interval=15'  | python3 -c "import sys,json,datetime; d=json.load(sys.stdin); k=[x for x in d['result'] if x!='last'][0]; r=d['result'][k]; print(len(r), datetime.datetime.utcfromtimestamp(r[0][0]), datetime.datetime.utcfromtimestamp(r[-1][0]))"

# engine (when it exists — not this VM; NEVER reset invert-paper for a year pack)
# kraken paper status  --workspace invert-paper -o json
# kraken paper history --workspace invert-paper -o json
# kraken paper status  --workspace invert-wf-2023 -o json   # if a WF workspace is created later
```

If a later run fills the scoreboard, it still prints **book** row first. Year rows stay diagnostics.
