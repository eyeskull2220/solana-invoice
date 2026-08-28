# REVIEWER — donch-d20 XRPEUR (reconstruct, then compare)

**Seat:** REVIEWER (adversarial). Different seat from the one that scored. Did not read Coder fills before reconstructing.  
**Stage:** paper score vs published recipe. Docs only. No live bot. No trading CODE in this PR.  
**Date:** 2026-08-28  
**Stamp:** VOORBEELD · paper / simulated · not FACTUUR · not INVOICE · not live-trade advice  
**HEAD (leftover `main` at write):** `2170952`  
**This file is judgment only.** No orders. No keys. No reseal of `c9689f5d`. No reset of `invert-paper` or `dca-paper`. No shop HTML.

Score **starts at 0**. Coder claims are not truth. Reconstruct from Kraken public data, then compare.

---

## Verdict: **YELLOW** — REST-720 rhymes and **PASSES** the numeric gate; named 2023+ is **not scored**

| Tape | This seat | Gate | Color vs Coder |
| --- | --- | --- | --- |
| **REST-720** (must) | Independent reconstruct. 19 fills / **+6.271917%** / maxDD **3.148108%** / equity **10627.191690** / fees **11.462799** / open_long **true** | **PASS** (return>0, fills≥8, maxDD≤8%) | **RHYME** — Coder 19 / +6.271917% / 3.148108%. Delta ~1e-7 (their 6-decimal rounding). Do not kill this print. |
| **2023-01-01 → 2026-08-27** (OHLCVT + 0-diff REST tail) | **NOT SCORED.** Official Drive OHLCVT ZIP is quota-blocked this sitting. Did not invent a 2023 tape from REST. | n/a | **KILL as a stamp.** Do not inherit Coder’s 37 / +5.759519% / 3.162919% / 10575.95 / 20.71. Unverified. |

**Overall: YELLOW.** REST-720 is a real Kraken-native 1d Donchian D20 print and it clears the published numeric gate. It is **not** a 2023-start tape, **not** the fund gate, **not** invert-paper, and **not** an income machine — eight of nine closed clips lost; the PASS is one EUR-200 ride through the 2024-11 → 2025-02 XRP spike. The named 2023+ book stays unstamped until OHLCVT actually lands.

Still paper. No live. No keys. No orders.

---

## Recipe this sitting used (published, no WFO)

Reconstructed from the prompt, not from Coder’s engine.

| Lock | Value |
| --- | --- |
| Pair / venue | Kraken **XRPEUR** public data only. Result key `XXRPZEUR`. No Binance splice. |
| Clock | Signal on **complete UTC day CLOSE**. Fill **NEXT day OPEN**. |
| IN | `close > max(high of prior 20 complete days)` while **flat**. Ignore extra entries while long. |
| OUT | `close < min(low of prior 10 complete days)` while **long**. Ignore exits while flat. |
| Book | Start **EUR 10000**. Clip **EUR 200**. One long only. Rest cash. Long only. |
| Fee named | **0.26% taker** per fill. Buy fee = `200 * 0.0026`. Sell fee = `qty * open * 0.0026`. |
| Shadows | **0.40%** and **0.80%** on the **same** fill prices / dates / sides. |
| MTM / DD | Mark `cash + qty * close` on each complete-day close. maxDD = peak-to-trough / peak. |
| Window | Through last complete UTC day **2026-08-27**. Drop forming **2026-08-28**. Signals from 2023-01-01 **if the tape reaches it**. |
| Gate | return after fees **> 0** AND fills **≥ 8** AND maxDD **≤ 8%**. |

Fill convention matches this repo’s paper clip (see adaeur-widefib SCORECARD): buy spends `CLIP + CLIP*fee`; sell credits `notional - notional*fee`; qty = `CLIP / fill_px`.

---

## 1) REST-720 (must) — this seat’s numbers

`GET https://api.kraken.com/0/public/OHLC?pair=XRPEUR&interval=1440`

| Cell | This reconstruct |
| --- | ---: |
| Label | **REST-720** — this is **not** a 2023-start tape |
| Raw rows | 721 (Kraken `last` = completed `2026-08-27T00:00:00Z`) |
| Complete bars | **720**, `2024-09-07` → `2026-08-27`, **0 gaps** |
| Forming dropped | `2026-08-28` (open 1.24739 / close 1.18982 unused for H/L/C/MTM) |
| Warmup | First IN needs 20 prior complete days → first possible signal **2024-09-27**; first actual IN **2024-09-28** |
| Fills | **19** (10 buy + 9 sell) |
| return_after_fees_pct | **6.2719169036** → **+6.271917%** at 6 dp |
| maxDD_pct | **3.1481077395** → **3.148108%** at 6 dp |
| Ending equity | **10627.19169036 EUR** |
| Fees | **11.46279893 EUR** |
| open_long | **true** (last fill buy 2026-08-21 @ 1.08547; MTM last close 1.24767) |
| Cash / qty | 10397.306019 / 184.251983 XRP |
| Peak / trough | 10942.301458 on **2025-01-17** → 10597.826019 on **2026-05-23** (the last sell, from that peak) |
| Ignored IN while long | 25 |
| Ignored OUT while flat | 36 |
| Pending after 2026-08-27 close | none (no 08-28 open fill) |
| **GATE** | **PASS** |

### Shadows (same 19 fills)

| Fee | fills | return_after_fees_pct | maxDD_pct | ending equity | fees | open_long | gate |
| --- | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 0.26% named | 19 | +6.271917 | 3.148108 | 10627.191690 | 11.462799 | true | **PASS** |
| 0.40% shadow | 19 | +6.210194 | 3.194810 | 10621.019414 | 17.635075 | true | **PASS** |
| 0.80% shadow | 19 | +6.033843 | 3.328282 | 10603.384339 | 35.270151 | true | **PASS** |

Fee haircut does not flip the REST-720 gate. The spike clip is large enough that even 0.80% taker still prints positive.

### This seat’s fills (do not treat Coder’s list as source)

Clock check: every fill is the **next UTC day OPEN** after a close signal. Channel is **prior** 20/10 complete days (today excluded).

| # | side | signal close (UTC day) | fill open (UTC day) | fill px | channel | sig close | qty | fee EUR |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 1 | buy | 2024-09-28 | 2024-09-29 | 0.55042 | 0.54871 | 0.55042 | 363.358890 | 0.520000 |
| 2 | sell | 2024-10-02 | 2024-10-03 | 0.48713 | 0.51600 | 0.48767 | 363.358890 | 0.460208 |
| 3 | buy | 2024-11-10 | 2024-11-11 | 0.54805 | 0.53786 | 0.54795 | 364.930207 | 0.520000 |
| 4 | sell | 2025-02-02 | 2025-02-03 | 2.52050 | 2.53150 | 2.51883 | 364.930207 | 2.391497 |
| 5 | buy | 2025-03-02 | 2025-03-03 | 2.82294 | 2.69992 | 2.82294 | 70.848123 | 0.520000 |
| 6 | sell | 2025-03-10 | 2025-03-11 | 1.86437 | 1.87000 | 1.86239 | 70.848123 | 0.343426 |
| 7 | buy | 2025-05-09 | 2025-05-10 | 2.08200 | 2.08033 | 2.08185 | 96.061479 | 0.520000 |
| 8 | sell | 2025-05-23 | 2025-05-24 | 2.02224 | 2.03401 | 2.02190 | 96.061479 | 0.505074 |
| 9 | buy | 2025-07-09 | 2025-07-10 | 2.04942 | 2.00618 | 2.04942 | 97.588586 | 0.520000 |
| 10 | sell | 2025-08-02 | 2025-08-03 | 2.39203 | 2.50000 | 2.39010 | 97.588586 | 0.606931 |
| 11 | buy | 2026-01-04 | 2026-01-05 | 1.78616 | 1.75391 | 1.78632 | 111.972052 | 0.520000 |
| 12 | sell | 2026-01-18 | 2026-01-19 | 1.71307 | 1.73974 | 1.71200 | 111.972052 | 0.498722 |
| 13 | buy | 2026-03-15 | 2026-03-16 | 1.26729 | 1.26634 | 1.26706 | 157.817074 | 0.520000 |
| 14 | sell | 2026-03-26 | 2026-03-27 | 1.17964 | 1.18216 | 1.17960 | 157.817074 | 0.484035 |
| 15 | buy | 2026-04-16 | 2026-04-17 | 1.23450 | 1.19561 | 1.23332 | 162.008910 | 0.520000 |
| 16 | sell | 2026-04-28 | 2026-04-29 | 1.17758 | 1.18042 | 1.17874 | 162.008910 | 0.496024 |
| 17 | buy | 2026-05-10 | 2026-05-11 | 1.25363 | 1.24987 | 1.25124 | 159.536705 | 0.520000 |
| 18 | sell | 2026-05-22 | 2026-05-23 | 1.14968 | 1.16150 | 1.14908 | 159.536705 | 0.476882 |
| 19 | buy | 2026-08-20 | 2026-08-21 | 1.08547 | 0.97166 | 1.08467 | 184.251983 | 0.520000 |

Hand check, first IN: 2024-09-28 close **0.55042** > max high 2024-09-08→2024-09-27 **0.54871**. Next open 2024-09-29 **0.55042** (overnight flat — equal to prior close, not a same-bar fill).  
Hand check, spike OUT: 2025-02-02 close **2.51883** < min low of prior 10d **2.53150**. Fill next open **2.52050**.

### vs Coder REST-720 claim

Coder claimed: 19 fills / +6.271917% / maxDD 3.148108%.

| Cell | Coder claim | This reconstruct | Delta |
| --- | ---: | ---: | ---: |
| fills | 19 | 19 | 0 |
| return_after_fees_pct | 6.271917 | 6.2719169036 | −9.6e-8 |
| maxDD_pct | 3.148108 | 3.1481077395 | −2.6e-7 |

**Rhyme.** Arithmetic matches. This seat did not copy a fill list; the 19 rows above are the reconstruct. If Coder later posts a different fill table on REST-720, the table above is the one that produced their rounded headline.

---

## 2) 2023-01-01 → 2026-08-27 — Drive / OHLCVT blocked

Recipe allows a second score only on **official Kraken OHLCVT** XRPEUR 1440 ([support article](https://support.kraken.com/articles/360047124832-downloadable-historical-ohlcvt-open-high-low-close-volume-trades-data)) plus REST tail after the last official bar with **0-diff overlap**. REST `since=` does not walk back. Do not splice Binance. Do not invent empty days.

This sitting:

| Probe | Result |
| --- | --- |
| Support HTML Drive IDs | Complete `1ptNqWYidLkhb2VAKuLCxmp2OXEfGO-AP` (`Kraken_OHLCVT.zip`). Quarterlies folder `15RSlNuW_h0kVM8or8McOGOMfHeBFvFGI` through **Q1_2026** (no Q2_2026 / Q3_2026 listed). Same IDs as [PR #210](https://github.com/eyeskull2220/solana-invoice/pull/210). |
| Confirm-token GET | Virus-scan interstitial, then **`Google Drive - Quota exceeded`**: “Too many users have viewed or downloaded this file recently.” Hit on complete zip, Q1_2023, Q4_2025, and Q1_2026. |
| REST-720 as fake 2023 tape | **Forbidden.** REST first complete bar is **2024-09-07**. |

**2023+ is not scored here.** Coder’s named claim (37 fills / +5.759519% / maxDD 3.162919% / equity 10575.95 / fees 20.71 / open_long true) is **left as a claim**. This seat does not rhyme it and does not bless it.

---

## ADVERSARIAL (first)

A later agent must not turn a 720-day REST window plus one XRP melt-up into “Belgian income machine is proven.”

### A1 — REST-720 PASS is one clip

Nine closed round-trips on this tape. Raw clip move (sell notional vs EUR 200, before allocating buy fee):

| Pair (sell #) | raw clip move | after both taker fees |
| --- | ---: | --- |
| 2 | −11.50% | loss |
| **4 (buy 0.54805 → sell 2.52050)** | **+359.90%** | **the book** |
| 6 | −33.96% | loss |
| 8 | −2.87% | loss |
| 10 | +16.72% | win |
| 12 | −4.09% | loss |
| 14 | −6.92% | loss |
| 16 | −4.61% | loss |
| 18 | −8.29% | loss |

Replay of the **same** later fills with fills 3–4 skipped: **17 fills / −0.897034% / maxDD 1.271296% / equity 9910.30 → GATE FAIL** (return ≤ 0). Replay of **only** fills 3–4: **+7.168951%**.

So: REST-720 **PASSES** the published gate, and **fails** the same gate if that one 2024-11-11 → 2025-02-03 clip is absent. Eight of nine closed pairs lost. This is trend-follow doing what it says — it is not 19 independent edges and not a salary.

One-clip buy-and-hold from fill 1 (0.55042) to last close (1.24767), entry fee only: **+2.5283%**. Full-tape XRP from 2024-09-07 open 0.47059 to last close is **+165%**, but that is 100% equity, not the locked EUR 200 clip. Apples-to-apples: Donchian D20 clip **beat** one-clip BH on this window **because it sold the spike**. That is the recipe, not a hidden all-in.

### A2 — Include-today channel is a different (empty) rule

If the 20-day high **includes today**, `close > max(high)` is impossible (`close ≤ high`). Attack reconstruct: **0 fills / 0%**. Coder’s 19 fills cannot be that bug. This seat used **prior** 20/10 days, as the prompt wrote.

### A3 — Close-fill vs next-open

Same signals filled at **that day’s close** instead of next open: 19 fills / +6.272843% / maxDD 3.157180%. Headline would still PASS and still rhyme at 2 dp. The named clock is next-open; this seat used next-open. Coder REST headline matches next-open, not close-fill.

`close >=` instead of `>`: same 19 fills on this tape (no exact-touch extra). Not a fork.

### A4 — Forming 2026-08-28

Last complete close 1.24767 (08-27). Forming close 1.18982. Open long. Marking the incomplete close would print **+6.165327%** — still PASS, **not** Coder’s 6.271917%. Coder REST headline matches **complete-day MTM**, which is the recipe. No 08-28 open fill: 08-27 close did not signal; pending was none.

### A5 — Named 2023+ without OHLCVT is a stamp, not a tape

37 fills from 2023-01-01 is **possible** on this recipe (REST-720 already prints 19 from 2024-09-07). Possibility is not a reconstruct. Fees 20.71 on 37 fills is in the right ballpark for 0.26% of mixed notionals (37 × 200 × 0.0026 = 19.24, plus winner sell notionals). Ballpark is not a rhyme. **Kill the 2023+ print as verified.** Re-score when Drive returns `XRPEUR_1440.csv` and REST overlap is 0-diff.

### A6 — Not invert, not the fund gate, not live

This is long-only Donchian D20, clip EUR 200, 1d close/next-open. It does not swap two prices. It does not arm invert-paper. Live `invert-paper` / `dca-paper` were not touched. `c9689f5d` was not resealed. `is_fund_gate` for this book stays **false**.

---

## Color card

| Probe | Result | Color |
| --- | --- | --- |
| REST-720 reconstruct vs recipe | Next-open, prior-20/10, clip 200, 0.26% taker, complete-day MTM, Kraken XRPEUR, through 2026-08-27 | **GREEN** |
| REST-720 vs Coder headline | 19 / 6.271917 / 3.148108 rhyme | **GREEN** (rhyme, do not kill) |
| REST-720 numeric gate | PASS | **GREEN** |
| REST-720 as 2023-start / income machine | Tape starts 2024-09-07. PASS is one spike clip. Skip it → FAIL | **YELLOW** |
| 0.40% / 0.80% shadows same fills | Both still PASS on REST-720 | **GREEN** (informational) |
| 2023+ OHLCVT score | Drive quota exceeded. Not scored. No invented REST 2023 tape | **YELLOW** (blocked) |
| Inherit Coder 37 / +5.759519% / 10575.95 | Unverified | **RED** (kill stamp) |
| Used as fund gate / live / invert-paper reset / reseal `c9689f5d` | Not done | **GREEN** (lock held) |
| Trading CODE / orders / keys this PR | None | **GREEN** |

**Overall: YELLOW.**

---

## What would flip it

| Flip | From | To |
| --- | --- | --- |
| Official `XRPEUR_1440.csv` (complete or 2023Q1–2026Q1 zips) + REST tail, **0-diff** overlap on overlapping days, independent reconstruct **matches** Coder 37 / 5.759519 / 3.162919 (or a new honest print that still PASSes) | YELLOW (2023+ unscored) | GREEN on 2023+ **only if** gate holds **and** concentration is disclosed. Still not the fund gate. |
| Same OHLCVT reconstruct **disagrees** with 37 / 5.759519 (lookahead, Binance splice, include-today, 100% size, close-model) | YELLOW | **RED** — kill Coder 2023+ numbers, keep REST-720 if it still rhymes |
| REST-720 clock changed to include-today channel | PASS 19 fills | 0 fills, FAIL |
| REST-720 MTM on forming 08-28 close | still PASS, but headline would **stop rhyming** Coder 6.271917 | YELLOW vs Coder |
| Count REST-720 as the named 2023 book | — | **RED** (wrong tape label) |
| Promote to live / invert-paper / spend keys | — | **RED** (forbidden this sitting) |
| Operator wants “income machine” = many independent clips, not one 360% ride | REST-720 PASS | **FAIL that test** (skip spike → −0.90%) |

---

## Locks held

| Lock | Held |
| --- | --- |
| Docs-only review PR. One file. No live-bot CODE | yes |
| No invert CODE. No invert-paper / dca-paper reset | yes |
| No reseal of `c9689f5d` | yes |
| No orders. No API keys. Still paper | yes |
| Did not copy Coder fills then back-solve | yes — REST-720 fills reconstructed from public OHLC, then compared to the **headline** only |
| Did not invent a 2023 tape from REST | yes |
| Did not download the 7.3G complete zip into the leftover repo ([PR #221](https://github.com/eyeskull2220/solana-invoice/pull/221) note) | yes — Drive returned quota HTML, not a ZIP |

Parents: allowlist clocks [PR #221](https://github.com/eyeskull2220/solana-invoice/pull/221), OHLCVT how-to [PR #210](https://github.com/eyeskull2220/solana-invoice/pull/210), paper clip convention in adaeur-widefib [PR #225](https://github.com/eyeskull2220/solana-invoice/pull/225). Gate books `invert-paper` / `dca-paper` stay as they were.
