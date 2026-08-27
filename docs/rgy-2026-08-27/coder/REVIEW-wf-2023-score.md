# REVIEWER — invert-wf-2023 named 15m score

**Seat:** REVIEWER (adversarial).  
**Stage:** score vs recipe. Docs only.  
**Date:** 2026-08-27  
**Stamp:** VOORBEELD · paper / simulated · not FACTUUR · not INVOICE · not live-trade advice  
**HEAD (leftover `main` at write):** `2170952`  
**This file is judgment only.** No orders. No keys. No reseal of `c9689f5d`. No reset of `invert-paper` or `dca-paper`. No shop HTML. No new Surge host.

Score **starts at 0**. GREEN only if the reported run is a **fair invert**: after any fill, swap jobs of **those two** prices; re-arm the filled price **only** on the opposite fill; spot no naked short; not retired fill-every-rung.

It is not. **RED.** Do not invent a prettier PnL. The numbers below stay as *this replay's print*. They are not replaced.

---

## Verdict: **RED** — not a fair invert

This sitting's named 15m print is **not** the fund gate. Live `invert-paper` stays **fill 1**. Promotion stays **RED**. The walk-forward score itself is also **RED** as invert.

| Probe | Result | Color |
| --- | --- | --- |
| Fair invert (swap those two prices; re-arm only on opposite) | Not evidenced. 9097 prints + close-model + 100% size + 1.00 EUR floor read as retired **fill-every-rung** and/or **same-bar both sides** | **RED** |
| Fee death (fees ≈ capital) | 10000 → **1.00** EUR; return after fees **−99.989999%**; maxDD **99.990007%** | **RED** |
| Same-bar both sides | Close-model. No `SAME_BAR_REARM` fail. Newly armed opposite can print on the same 15m close | **RED** |
| 100% equity sizing | Terminal dust. Locked clip is **EUR 200** (live `PAPER-00029` cost ~200). All-in is not invert-paper | **RED** |
| Venue | **BINANCE-VISION-XRPEUR + Kraken tail**, not Kraken XRPEUR 15m | **RED** |
| Fill model | **close-model**, not limit-at-rung inside `[low, high]` | **RED** |
| This score as fund gate | Forbidden. Gate stays `invert-paper` only | **GREEN** (not used as gate) |
| invert-paper fill count | Still **1** (`PAPER-00029`). TP 00030 / open 00028 are not fills | **GREEN** (lock held) |
| Invent a better PnL | Not done | **GREEN** |
| Reseal `c9689f5d` / reset `dca-paper` / live / keys | Not done | **GREEN** |

**Overall: RED.** Design-out the replay. Then a **new** score. Do not restamp this curve.

---

## What was scored (from zero)

Coder reported a named 15m print on window **2023-01-01 → now**:

| Cell | Reported |
| --- | --- |
| Series | **BINANCE-VISION-XRPEUR + Kraken tail** |
| Bars | **n = 128142** |
| Gap | **one 5-bar hole 2023-03-24** |
| Model | **close-model** |
| Fills | **9097** |
| Return after fees | **−99.989999%** |
| maxDD | **99.990007%** |
| Start / end | **EUR 10000 → 1.00** |

Locks this review uses (not bargained):

| Source | Lock |
| --- | --- |
| This prompt | Attack invert vs fill-every-rung; fee death; same-bar both sides; 100% equity. GREEN only if fair invert. No invented better PnL. Not the fund gate. invert-paper still fill 1. |
| [PR #196](https://github.com/eyeskull2220/solana-invoice/pull/196) `PLAN-invert-wf-2023.md` | Closed-bar clock. Full fib both sides. Swap those two prices. Re-arm only on opposite. **EUR 200 clip.** Primary fee **0.26%**. Same-bar: newly armed opposite **does not fill this bar**. Fill at **limit**, not close. Data: **Kraken** OHLCVT. Retired `2bfb1b68` fill-every-rung stays retired. `is_fund_gate: false`. |
| [PR #197](https://github.com/eyeskull2220/solana-invoice/pull/197) `RESEARCH-xrpeur-15m-data.md` | Query pair **XRPEUR**. REST OHLC 15m cannot source 2023 (720-bar ceiling). **Do not** label Binance / Bitstamp as Kraken. **Do not** invent empty-bar OHLC. |
| [PR #132](https://github.com/eyeskull2220/solana-invoice/pull/132) / [#144](https://github.com/eyeskull2220/solana-invoice/pull/144) / [#118](https://github.com/eyeskull2220/solana-invoice/pull/118) | Gate = `invert-paper` only. Fill **1**. Do not reseal `c9689f5d`. Do not reset `dca-paper`. Still paper. |
| [PR #194](https://github.com/eyeskull2220/solana-invoice/pull/194) | 2023 slice checklist: skipped-rung log on **2023-07-13** (and 07-14, 11-13, 11-14, 06-06, 03-10). Interpolating a hole into a print is journal fraud. |
| Live recipe (spot) | After sell-TP: **flat cash**; next entry is **buy-back**. No naked short. |

This leftover tree has **no** `paper/invert-wf-2023/` engine dump. Kraken MCP this VM: not used for orders. No `kraken order`. Arithmetic below is on **the reported cells only**.

---

## ADVERSARIAL (first)

A score that can ship is a page a later agent could follow **without** turning dust, a Binance splice, or a close-model spray into “invert is proven.” Attack this print as if it were a bad layout.

### A1 — Can 9097 fills be invert, or is this retired fill-every-rung?

**Locked invert:** a lot is two prices `(Lo, Hi)`. After **any** fill, those two **swap jobs**. The filled price **stops** working. The other price **becomes** the working order. Re-arm the filled price **only** after that opposite prints. Spot: no naked short. Other *unfilled* buy rungs at **different** prices may stay (live `PAPER-00028` pattern). That is **not** “every fib touch is a fill.”

**Retired `2bfb1b68` fill-every-rung:** every level is live. A wick through the stack prints a **ladder**. July 13 2023 (open-to-high ~+96% on EUR aggregators) would mint a **stack** of prints in one session if every extension were a fill. The sealed lab clip `c9689f5d` (8 days, **20** fills, +0.681154%, maxDD 0.890854%) is the invert **rate** the desk already sealed: **2.5 fills/day**, not a spray.

**This print:** 9097 fills / ~1334 calendar days ≈ **6.8 fills/day**. ~**7.1%** of 128142 bars print. Lab-rate over the same window would be ~**3335** fills, not 9097.

9097 *can* happen on a tight two-price ping-pong. It is **not proven** invert, because the report does not show:

1. After each print, **only** the swapped opposite was armed.  
2. Skipped-rung log on **2023-07-13** (and the other spike days in #194). Wick tags are not 18 fib prints.  
3. Cash cap: sum of working buy notionals + held cost + primary fees **≤ cash**. Skip extra rungs rather than lever (#196 §4.4).  
4. Fail codes `NAKED_SHORT` / `SAME_BAR_REARM` never fired — because they were **implemented**, not because they were omitted.

**Close-model + 100% size + 1.00 EUR floor** is the tell. Fill-every-rung and same-bar both-sides both produce **fee death**. Fair invert at EUR 200 does not end at 1.00 EUR from fees alone (9097 × 0.26% × 200 ≈ **4730 EUR** of fees — ugly, not dust). Dust is **all-in** and/or **double prints**.

**Stop:** do not call 9097 “invert working.” Do not revive `2bfb1b68`. Do not treat ≥8 as a gate win on this book. This book is **not** the fund gate.

### A2 — Fee death (fees ≈ capital)

Reported: **10000 → 1.00 EUR**. Return after fees **−99.989999%**. maxDD **99.990007%**.

That pair is a **floor**, not an invert terminal. 1.00 / 10000 − 1 = **−99.99%**. maxDD **99.990007%** is the same crash with a peak a few euro above start (a tiny mark, then dust). Reviewer does **not** invent a peak timestamp or a prettier trough.

**Primary Starter taker 0.26% on 100% of remaining equity, zero gross edge:**

```text
10000 × (0.9974)^n = 1  →  n ≈ 3538 fills
```

9097 > 3538. Either the book **hit ~1 EUR around fill 3500 and kept counting prints on dust**, or same-bar **two** fees per bar (round-trip at the close) halves the bars-to-floor:

```text
10000 × (0.9948)^k = 1  →  k ≈ 1767 round-trips  →  ~3534 fills
```

`(0.9974)^9097 × 10000` without a floor is **~5×10⁻⁷ EUR**, not 1.00. **Ending exactly 1.00 is a min-equity halt.** Scoring −99.989999% after a halt is “when did we hit dust,” not “what did invert earn.”

**EUR 200 clip (locked, live 00029):** 9097 × 0.52 EUR ≈ **4730 EUR** fees. That path **cannot** print 1.00 EUR from fees alone. 100% equity (or many overlapping full-book lots — the same cheat) is required for this terminal.

Lab-rate invert at 100% size, still zero edge: `(0.9974)^3335 × 10000 ≈ 1.70 EUR`. So **even a fair invert state machine, all-in, multi-year, 0.26% taker, wipes.** The −99.99% is a **sizing artifact**. It is not a measurement of invert edge. Reviewer will not replace it with a hypothetical 200-EUR curve.

**Stop:** do not read −99.99% as “invert failed the market.” Do not reseal to hide it. Do not mix sleeve shorts into the fade. Record **this** print as **invalid invert**, then design-out.

### A3 — Same-bar both sides

Locked (#196 §4.4–4.5): at most **one** fill **per lot** per bar. The newly armed opposite **does not fill on the same bar**. Fill price = **limit** if the pre-existing order sits in `[low, high]`. Not the close. Not the extreme beyond the limit. Fail the run on `SAME_BAR_REARM`.

**Close-model** (Coder’s word): a 15m bar whose range spans **both** `Lo` and `Hi` can print **buy and sell on the same close**. Path-within-bar is invisible. Invert’s opposite has not happened as a later event; the engine invented a round-trip. Two 0.26% hits on 100% equity = **0.52% of the book per such bar**, with **zero** geometric edge if both fill at the same close.

That is how you get **fees ≈ capital** without a three-year trend against you.

The report does not give: same-bar two-sided count, `SAME_BAR_REARM` trips, or a proof it is 0. Close-model without that lock **defaults to guilty**.

**Stop:** close-model is a **different strategy** from invert limits. Do not score it as invert.

### A4 — 100% equity sizing

Live invert-paper fill 1 ([PR #193](https://github.com/eyeskull2220/solana-invoice/pull/193) journal cite / #196 lock): **160.64773 XRPEUR @ 1.24496**, cost **199.99999794**, fee 0.26% = **0.52**. That is **EUR 200 quote**, **2%** of the 10k paper book, not 100%.

#196 §4.3: `CLIP_QUOTE_EUR = 200`. Never buy more quote than cash after primary fee. Never sell more XRP than held. Cash cap: skip extra rungs rather than lever.

100% of 10000 per rung is **50×** the live clip. Combined with many armed rungs it is **implicit leverage** (same cash promised to several lots) — fill-every-rung’s twin.

**Stop:** a 100% replay is not invert-paper. Do not promote a dust curve. Do not “fix” it by inventing a 200-EUR PnL in this file.

### A5 — Wrong venue, wrong gap rule, not the gate

**BINANCE-VISION-XRPEUR + Kraken tail** is a **cross-venue splice**. #197 forbids labeling Binance as Kraken. Named book is **Kraken XRPEUR**. Different prints, different 24h rails, different 2023-07-13 book.

REST Kraken 15m OHLC is **~7.5 days** (720-bar ceiling). A “Kraken tail” is the last week. **Almost the entire 128142-bar sample is Binance** if Vision is the body.

**One 5-bar gap 2023-03-24:** 75 minutes. #197: missing row = no trades; **do not invent** the candle. #196 synthesizes empty buckets for the **clock** but they **may not fill**. Either way: interpolating a hole into a `PAPER-*` print is fraud (#194). A Binance publish hole is **not** a Kraken hole. Do not launder it.

**n = 128142** is in the right order of magnitude for 2023-01-01 → 2026-08-27 15m slots (~128147 in #197). Bar-count hygiene is not the fail. **Venue + model + size + invert state** are.

**Not the fund gate.** invert-paper still:

| Id | Role | Price | Gate fill? |
| --- | --- | --- | --- |
| PAPER-00029 | FILL 1 · buy XRPEUR | 1.24496 | **Yes. Count = 1** |
| PAPER-00030 | Resting TP sell LIMIT | 1.26778 | No |
| PAPER-00028 | Open | 1.23084 | No |

Gate (all three, **`invert-paper` only**): return > 0 after fees **and** ≥ 8 prints **and** maxDD ≤ 8%. **NOT MET.** 9097 on a Binance close-model dust book does not move that count to 8. Do not 20+1 with the lab clip. Do not reseal `sha256:c9689f5d7d583320e724900b0ce4ef68193878c880d11939badd1dd59016e390`.

---

## RED

### R1 — Not a fair invert (fill-every-rung / swap-and-wait unproven)

9097 prints without an opposite-only re-arm log, without a skipped-rung log on 13 Jul, with close-model, with 100% size, is **not** the locked recipe. Retired `2bfb1b68` stays retired. `9056f296` entry-waits-TP and `094513` arming-only (99 fills PASS, not live) stay retired.

### R2 — Fee death / 1.00 EUR floor

Return **−99.989999%**, maxDD **99.990007%**, end **1.00 EUR**. Fees consumed the book (and/or a halt froze residual). This is not gate-1. Reviewer does **not** write a substitute return.

### R3 — Same-bar both sides not designed out

Close-model. No reported `SAME_BAR_REARM` fail. Newly armed TP can print on the same close as the entry. That round-trip is **not** invert.

### R4 — 100% equity

Violates EUR 200 clip and cash cap. Makes maxDD 99.99% uninformative about invert. Live 00029 is a 200 EUR clip.

### R5 — Binance Vision body, Kraken tail

Wrong venue for the named pair. Splice boundary is a silent regime change. #197 RED if labeled Kraken.

### R6 — Close-model ≠ limit invert

Locked fill: limit in `[low, high]`. Close-model fills at close (and misses/overfills vs a through). Lab clip and live 00030/00028 are **limits**.

### R7 — Do not promote, reseal, or reset

Still paper. Autonomy 2. No keys. No Phantom. Gate stays `invert-paper` fill **1**. Do not reseal `c9689f5d`. Do not reset `dca-paper`. Do not flatten 00030/00028. Sleeve FAIL is not this score.

---

## YELLOW

**None remaining on invert-fairness.** Adjacent notes that are **not** a pass:

### Designed out — bar count looks plausible

128142 vs ~128147 UTC 15m slots (#197) plus one 5-bar hole is **not** proof of Kraken continuity. It is a count. Venue still RED.

### Designed out — fills ≥ 8

9097 ≥ 8 is the **wrong conjunct to celebrate**. Gate-2 without invert state, without gate-1, with 99.99% DD, on the **wrong book**, is still FAIL. Isolation diagnostic does not fund (#194).

### Designed out — “Kraken tail”

A 7.5-day REST tail does not baptize 3.6 years of Binance as Kraken XRPEUR.

---

## GREEN (locks around the score — not the score)

### G1 — Not used as the fund gate

This review does not promote `invert-wf-2023`. Live book remains `invert-paper`, fill **1**, **NOT MET**.

### G2 — No invented better PnL

−99.989999% / maxDD 99.990007% / end 1.00 EUR stay as **this replay’s print**. Next number requires a new run after design-out.

### G3 — No reseal, no `dca-paper` reset, no live, no keys

Cite `c9689f5d` only. Five BTCUSD slices stay held. No `kraken order`. Treasury strings stay Wallet receive-only (`96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3`, Base `0x9eb954b567ef3616424a6e1bf42c63724930aa54`).

### G4 — Sleeve / lab clip / 00029 not mixed into this scoreboard

Lab 20 / +0.681154% / 0.890854% is **not** this window. 00029 is **not** fill 21. Sleeve FAIL stays on the sleeve.

---

## Design-out — what must change in the replay **before** a new score

Do **not** patch this curve. Do **not** invent a 200-EUR restatement in markdown. Implement the locked engine, then print a **new** scorecard. Until then the named 15m score is **RED / not invert**.

| # | Change | Why this print failed |
| --- | --- | --- |
| **D1** | **Invert state machine.** Lot = `(Lo, Hi)`. After fill, those two swap jobs. Re-arm the filled price **only** on the opposite print. Spot: sell only with inventory; after sell-TP **flat cash**, buy-back at `Lo`. Other unfilled *different* buy rungs may stay (00028). **Not** fill-every-rung `2bfb1b68`. | 9097 unproven as opposite-only |
| **D2** | **Same-bar lock.** ≤1 fill per lot per bar. Newly armed opposite **skips this bar**. Fail the run on `SAME_BAR_REARM`. Report same-bar two-sided count; it must be **0** for re-arm. | Close-model both sides |
| **D3** | **Fill at limit**, if pre-existing order in `[low, high]`. Not close-model. Not wick-beyond as extra size. Rails from bars `i-96..i-1` only (no lookahead). | Coder scored close-model |
| **D4** | **EUR 200 clip** per rung. Cash cap: working buys + held + primary fees ≤ cash. Skip rungs rather than lever. **Never 100% equity.** | 10000 → 1.00 is all-in / levered spray |
| **D5** | **Fees.** Primary **0.26%** hits cash. Shadows **0.40 / 0.80** parallel, do not change fills. If equity hits a documented min (do not silently floor at 1.00 and keep spraying), **stop and flag** `MIN_EQUITY`. Report cumulative primary fees vs start cash **separate** from return. | 1.00 is a halt, not a score |
| **D6** | **Venue = Kraken XRPEUR 15m.** OHLCVT ZIP + official tail (#197). **Not** Binance Vision labeled as the book. Do not invent empty-bar OHLC. Synthesized clock bars (#196) **must not fill**. Log the 2023-03-24 hole on **Kraken**, not Vision; 0 interpolated prints. | Cross-venue splice |
| **D7** | **Spike honesty.** Skipped-rung log on 2023-07-13, 07-14, 11-13, 11-14, 06-06, 03-10 (venue 15m). Do not skip July to pretty maxDD. | Fill-every-rung tell |
| **D8** | **Scorecard.** Combined = one sequential EUR 10000. Do not sum year slices. `is_fund_gate: false`. Cite `c9689f5d`; do not reseal. invert-paper fill 1 stays. | Wrong-book promotion |
| **D9** | **Do not replace −99.989999%.** That number is this replay. The next run prints new cells. | No invented better PnL |

**Fail the next run (no fake GREEN):** `DATA_GAP` (if fills invented in holes) · `DATA_BAD` · `LOOKAHEAD` · `NAKED_SHORT` · `SAME_BAR_REARM` · `TOUCHED_INVERT_PAPER` · `TOUCHED_DCA_PAPER` · `CROSS_VENUE` · `CLOSE_MODEL` · `FULL_EQUITY` · `MIN_EQUITY` (halt then continued prints).

---

## What this score is not

1. **Not the fund gate.** `invert-paper` fill **1**. Stay paper.  
2. **Not** the 8-day lab clip. Do not 20+9097. Do not reseal.  
3. **Not** a reason to reset `dca-paper` or flatten 00030/00028.  
4. **Not** a SEPA instruction. 10k is paper. 1.00 is dust in a JSON.  
5. **Not** a tax fact. Paper is geen belastingfeit.  
6. **Not** permission to go live because “we sampled 3.6 years.” Autonomy **2**. Connector / keys: still no.

---

## This run

| Did | Did not |
| --- | --- |
| Judged the reported 15m cells against invert recipe, #196, #197, #194, live fill-1 locks | Place paper or live Kraken orders |
| Arithmetic on 0.26% × 100% vs EUR 200 clip vs 1.00 floor | Invent a better return / maxDD / fill count |
| Named Binance Vision + close-model + 100% size as design-out | Reseal `c9689f5d` |
| Left invert-paper at fill 1 | Reset `dca-paper` / `invert-paper` |
| | Patch Surge, shop HTML, keys, Phantom, FACTUUR |

**Score: RED.** Not a fair invert. Design-out D1–D9, then a **new** score. Still paper. No reseal. No `dca-paper` reset. Gate on `invert-paper` only — **NOT MET**. No live.

---

## Re-check (copy/paste — public / git only)

```bash
# live gate book — expect fill 1, not 9097
curl -sS https://dca-paper-journal.surge.sh/ | rg -n 'fills|PAPER-00029|NOT MET|c9689f5d|invert-paper'

# public now-tape is not 2023 and is not Binance Vision
curl -sS 'https://api.kraken.com/0/public/Ticker?pair=XRPEUR'
curl -sS 'https://api.kraken.com/0/public/OHLC?pair=XRPEUR&interval=15' >/dev/null

# this leftover tree: no engine dump to “fix” the PnL
ls paper/invert-wf-2023 2>/dev/null || echo 'no invert-wf-2023 tree on this checkout'
```

Count fund-gate fills only from `PAPER-*` **prints** on **`invert-paper`**. Resting 00030 and open 00028 do not count. The 9097 print is a **rejected replay**, not a ping.

End of invert-wf-2023 score review.
