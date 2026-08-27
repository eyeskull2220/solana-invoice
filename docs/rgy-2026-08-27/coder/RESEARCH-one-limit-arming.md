# RESEARCH — One invert pair, one resting limit (arming)

**Seat:** RESEARCHER (Coder pack)  
**Lens:** simple **first**, then broaden. Adversarial before GREEN. Method only. Not a score. Not a fill.  
**Date:** 2026-08-27  
**Stamp:** VOORBEELD · paper / simulated · not FACTUUR · not INVOICE · not live-trade advice  
**HEAD (this repo):** `2170952`  
**Still paper.** Do not reseal `c9689f5d`. Do not reset `invert-paper`. Do not reset `dca-paper`.

This file answers **one** question: how to pick the **ONE** invert pair from a full fib set **without** fill-every-rung and **without** two entry limits.

It sits on the walk-forward method pack: [PR #199](https://github.com/eyeskull2220/solana-invoice/pull/199) `docs/rgy-2026-08-27/coder/RESEARCH-invert-walkforward.md`. This page does not replace that pack. It names the arming rule the pack already locked (L3/L4, protocol step 3) so a later `invert-wf-2023 1-limit rescore` cannot “improve” it by resting two buys.

It does **not** print a 2023 equity curve. Inventing one here is cheating.

Machine this sits in (CEO [PR #142](https://github.com/eyeskull2220/solana-invoice/pull/142)): **one Belgian income machine**, four lanes. This file is **Paper**, still RED on the live gate. It is not Sell. It is not Rails. Locks held is not income.

---

## What this page is (and is not)

| Thing | This pack |
|---|---|
| Question | Pick **one** working pair `(P_entry, P_tp)` from the **full** fib set. Rest **at most one** limit. |
| Named next score | `invert-wf-2023 1-limit rescore` — **named, not scored**. Still paper. Still simulated. |
| Live book | `invert-paper` fill **1** = `PAPER-00029`. Resting TP `PAPER-00030`. Extra buy `PAPER-00028` still open. **A different book.** |
| Lab clip | `sha256:c9689f5d…` — **cite. Do not score as this. Do not reseal.** |
| Not this page | Fill-every-rung (`2bfb1b68`). Entry-waits-TP (`9056f296`). Arming-only (`094513`). Sleeve 3x. `dca-paper`. |

**Do not invent a score.** No 2023 fill count. No 2023 return. No 2023 maxDD. No PASS/FAIL for `invert-wf-2023 1-limit rescore` lives here. The name is the next **row**. The numbers are a later slice with a causal 15m archive under PR #199 L1–L6.

---

## Simple (the whole rule)

Full fib set **exists**. Full set is **not** a stack of working orders.

1. Confirm a swing (**causal `N=8`**). Until both a high and a low are confirmed, **wait**. No pair. No rest.
2. From that confirmed set, pick **exactly two prices**: nearest buy-eligible rung **below** last **closed** 15m as `P_entry`, nearest rung **above** that close as `P_tp`. If none below or none above, **wait**.
3. Arm **one** side given inventory. Never both. Never a second buy.
4. Armed at close of bar `t` → eligible from bar `t+1`. Never the arm bar.
5. Same-bar dual touch → `DUAL_TOUCH_SKIP`. Not a round-trip. Not two fills.
6. After **any** fill, swap jobs of **those two** prices. Re-arm **only** on the opposite fill.

That is invert. Fill-every-rung is the other movie.

---

## Two books (do not collapse)

### Live paper — `invert-paper` (fill 1). Leave it.

Source this sitting: operator/Coder + live journal https://dca-paper-journal.surge.sh/

| Id | Role | Price | Qty (journal) | Gate fill? |
|---|---|---|---|---|
| **PAPER-00029** | **FILL 1** · buy XRPEUR (journal: order `PAPER-00027` filled) | **1.24496** | 160.64773 | **Yes. This is fill 1.** |
| **PAPER-00030** | Resting TP · sell LIMIT (journal: **24h H**) | **1.26778** | 160.64773 | **No.** Resting is not a fill. |
| **PAPER-00028** | **Still open · buy LIMIT** | **1.23084** | 162.49066 | **No.** Open is not a fill. |

Fill count toward the gate: **1**. Gate (return > 0 after fees **and** ≥ 8 prints **and** maxDD ≤ 8%) is **NOT MET**.

Do not flatten 00030/00028. Do not reset the workspace. Do not splice these ids into 2023.

### Named next score — `invert-wf-2023 1-limit rescore`. Still paper. Unscored.

A **simulated** historical book. Constraint that distinguishes it from a naive full-set replay:

- **At most one resting limit.**
- **Not two buys on bar one.**

It is **not** `invert-paper`. It is **not** the 8-day clip. It does **not** get numbers in this file.

---

## Adversarial first

Attacks that would fake “one pair” while still filling every rung.

1. **Rest the full fib set as live limits.** Retracements 0.236 / 0.382 / 0.5 / 0.618 / 0.786 plus extensions 1.272 / 1.618 / 2.0 / 2.618 both sides are the **rail catalog**. Putting a LIMIT on every rung is retired `2bfb1b68` fill-every-rung. A 15m bar that trades through two buys prints two entries. That is the bug this rescore is named to forbid.

2. **Two entry limits while flat.** `P_entry` plus a “backup” buy one rung lower. Bar one can fill the nearer buy, or both if the wick is wide. Invert while `FLAT_EUR` arms **one** buy. The extra rest is a second recipe.

3. **Re-arm a buy after the entry already filled.** Inventory is `LONG_XRP`. Armed side is **sell** at `P_tp`. A second buy is a pyramid. Journal: after fill 1, `PAPER-00028` is still a **buy** LIMIT. That is the live tell (flag below). Do not copy it into the 2023 rescore.

4. **Count 00028 or 00030 as the one-limit proof.** 00030 is a rest. 00028 is a rest. Neither proves the arming rule. The live book currently shows **two** working orders (sell TP **and** extra buy) plus one fill. That is **not** L4.

5. **Arm on bar `t` and fill on bar `t`.** Decision uses that bar’s already-known wick. Eligible from `t+1` only ([PR #199](https://github.com/eyeskull2220/solana-invoice/pull/199) L2 / B4).

6. **Same-bar buy and sell as a round-trip.** OHLC has no path. `DUAL_TOUCH_SKIP`. At most one fill per bar. At most one armed limit, so dual-touch should be rare; if an implementation had both sides working, fill **neither**.

7. **Repainting swing / future high for the pair.** Rails from a pivot that later moves, or `H = max(high)` over the whole year, then pick “nearest below close” from that future set. Causal `N=8` confirm. Confirmation close ≤ decision time. ([PR #199](https://github.com/eyeskull2220/solana-invoice/pull/199) S1 / B1 / B2).

8. **Treat 24h high as `P_tp`.** Live TP `1.26778` = public 24h H (journal labels it). That is the **live** book, possibly a latch, **not** the 2023 pair rule. Using rolling 24h high as the fib TP is B2.

9. **Invent `invert-wf-2023 1-limit rescore` numbers.** Public Kraken 15m OHLC is ~720 recent bars (late August 2026), not 2023. Missing archive ≠ assume PASS. Do not add 20 clip fills. Do not add live 00029 as fill 1 of 2023.

10. **Reset `invert-paper` to “run the one-limit test.”** Historical replay is a separate simulated ledger. Live fill 1 + 00030 + 00028 stay. Official `paper reset` on that workspace is banned from this pack.

11. **Naked short / two sells.** Spot: after sell-TP you are `FLAT_EUR`. Next rest is buy-back. Never a sell with zero XRP. Sleeve long↔short is a different book.

12. **Tune which two rungs on 2023–2026.** The pick rule is locked below. Grid-searching “best pair” on the walk-forward window is contamination ([PR #199](https://github.com/eyeskull2220/solana-invoice/pull/199) B6).

---

## Locked pick (must hold)

Copy as implementation invariants. A later slice that rests two buys is not this method. Cite [PR #199](https://github.com/eyeskull2220/solana-invoice/pull/199) L1–L4; this file only **tightens the pick**.

### P1 — Full set is the catalog, not the order list

Same formula as PR #199 L3. `H` / `L` confirmed, `range = H - L`.

```
retracements (inside [L, H]):
  for r in {0.236, 0.382, 0.5, 0.618, 0.786}:
      L + r * range

extensions both sides:
  for e in {1.272, 1.618, 2.0, 2.618}:
      above = L + e * range
      below = H - e * range
```

Every level is a **rung**. At most **two** rungs are the **working pair**. All other rungs are idle until a confirmation event **replaces** the swing (cancel the rest — cancel is not a fill — then re-pick).

Not this pack: LIMIT on every rung (`2bfb1b68`). “Arming-only” 99 fills (`094513`). Entry that waits forever for TP as the only rest (`9056f296`).

### P2 — Causal swing `N=8` before any pair exists

A bar `i` is a **candidate** swing high if `high[i]` is the max of `high[i-N : i]` (left window only). It is **confirmed** at the close of bar `i+N` iff `high[i]` remains strictly greater than `high[i+1] … high[i+N]`. Symmetric for lows.

- **`N = 8`** (eight 15m bars = 2 hours). Locked. Not searched on 2023+.
- Rails at `t` use only swings whose **confirmation close ≤ t**.
- Unconfirmed last pivot: **does not exist**.
- One working swing: last confirmed high + last confirmed low of the **same completed move**. Earliest arm = later of those two confirmation closes.
- Warmup bars before 2023-01-01 00:00 Europe/Brussels may confirm; they are not fills.

No confirmed `H` and `L` → **no pair** → **no rest**. Do not fall back to 24h H/L.

### P3 — Pick exactly two prices (the invert pair)

At the close that first allows a pair (and again only when a **new confirmation** invalidates the old pair):

Let `C` = `close` of that decision bar (closed 15m, this pair only: XRPEUR).

```
candidates = all rungs from P1 using the confirmed (H, L)
P_entry = max { p in candidates | p < C }     # nearest buy-eligible below last close
P_tp    = min { p in candidates | p > C }     # nearest rung above last close
```

- If `P_entry` missing or `P_tp` missing or `P_entry == P_tp`: **wait**. Do not skip to an unconfirmed extension. Do not invent a 24h-H TP.
- Do not pick two rungs **both below** `C` (that is two buys). Do not pick two rungs **both above** `C` (that is two sells / a TP with no entry).
- Do not pick a third “runner” or “backup.”
- Keep `(P_entry, P_tp)` until a **fill** (then P4 swap) or until a **new confirmed swing** cancels them.

This is PR #199 protocol step 3, stated so it cannot be read as “step all rungs.”

### P4 — At most one resting limit (inventory)

Spot inventory: `{FLAT_EUR, LONG_XRP}`. Never `SHORT_XRP`.

| Inventory | Armed (exactly one) | Forbidden |
|---|---|---|
| `FLAT_EUR` | buy LIMIT at `P_entry` | any sell; any second buy |
| `LONG_XRP` | sell LIMIT at `P_tp` | any buy (no pyramid, no re-arm entry); any second sell |

**On a fill:** record the print → **swap jobs of those two prices** → do **not** re-arm the filled price until the opposite fills → buy fill → `LONG_XRP`; sell-TP → `FLAT_EUR`.

**Spot no naked short:** after sell-TP, next rest is buy-back. If the swap would sell while flat, discard the short; stay `FLAT_EUR`; next armed order is a buy (PR #199 L4).

**Two buys on bar one — forbidden.** While `FLAT_EUR`, the book may contain **zero or one** buy LIMIT. A bar that would have touched two buy rungs fills **only** the single armed `P_entry` (if eligible and touched). The other rung was never working.

### P5 — Armed `t`, eligible `t+1`. Touch-fill. `DUAL_TOUCH_SKIP`

Cite [PR #199](https://github.com/eyeskull2220/solana-invoice/pull/199) L2. Repeat so arming cannot “clarify” it away:

- Signals, swing confirm, fib recompute, arm/cancel: **bar close** of `t`.
- A limit is resting at the open of bar `b` only if armed at close of some `u` with `u < b`.
- Buy LIMIT at `P`: fill at **`P`** iff `low[b] <= P`. Sell LIMIT at `P`: fill at **`P`** iff `high[b] >= P`.
- Gap-through: still count default fill at `P`; shadow the `open`. Do not skip the default column.
- **Same-bar both-sides:** if a bar’s range could touch two prices, fill **at most one** — the single limit that is armed. If a bug had both working, **fill neither** that bar and flag **`DUAL_TOUCH_SKIP`**. Not a round-trip. Not two fills toward the gate.
- Forming bar is invisible. Close-cross without a wick touch on a corrupt row: **drop the bar**, do not fill.

One-limit arming makes `DUAL_TOUCH_SKIP` a **bug flag**, not a normal outcome. Honest L4 has only one price that can print. Dual-touch with two rests means the pick rule was already broken (live 00028 class, or fill-every-rung).

---

## Broaden

### Flag: live `PAPER-00028` extra buy is a **second recipe**

Not a fill. Not a TP. A **second entry limit**.

| Fact (journal this sitting) | Invert one-limit (this pack / PR #199 L4) |
|---|---|
| Fill 1 is a **buy** @ 1.24496 → inventory should be `LONG_XRP` | Armed rest = **sell** at `P_tp` only |
| `PAPER-00030` sell LIMIT @ 1.26778 (24h H) | Allowed **shape** (one sell rest) — price source is YELLOW (24h H, not proven fib) |
| `PAPER-00028` **buy** LIMIT @ 1.23084 **still open**, qty **162.49066** (≠ fill qty 160.64773) | **Forbidden.** Second buy. Pyramid / fill-every-rung / leftover rest from a two-limit start |

**Verdict on 00028:** **second recipe.** Retired name that matches the *shape*: `2bfb1b68` fill-every-rung (or a two-buy arm while flat that survived the first fill). It is **not** the invert swap (re-arm only on the opposite fill). It is **not** proof that live invert-paper is one-limit.

Do **not** cancel it from this page. Do **not** backfill it from OHLC (live traded through 1.23084; paper still open — Coder 01 Y2). Do **not** count it as fill 2. Do **not** copy two-buy arming into `invert-wf-2023 1-limit rescore`.

If a later Coder ping sees 00028 print: that print is still a **live invert-paper** event, journaled as a fill on **that** book, and it is evidence the live book was **not** running this pack. It does not become a 2023 number.

### Why “not two buys on bar one” is the named constraint

Fill-every-rung and two-entry-limit both fail on the **first** 15m bar that spans more than one buy rung. Wide XRP wicks make that common. The 8-day clip PASS (`c9689f5d`, 20 fills) did not have to spell this; the 2023 rescore must. One armed buy ⇒ at most one buy print per bar ⇒ bar one cannot mint two entries.

`DUAL_TOUCH_SKIP` is the **other** same-bar crime (buy **and** sell). Do not conflate:

| Same-bar crime | What prints if you cheat | Stop |
|---|---|---|
| Two **buys** (two entry limits / every rung) | 2 buy fills, pyramid, fill count +2 | P4: one rest while flat |
| Buy **and** sell (both sides armed, or assumed OHLC path) | Fake round-trip | `DUAL_TOUCH_SKIP`; one rest while long is only the sell |

### Machine / Paper lane (do not promote)

CEO machine ([PR #142](https://github.com/eyeskull2220/solana-invoice/pull/142)): Paper is a **brake** until the invert gate is met. Gate is still **NOT MET** (live n=1). This arming pack does not greenlight 2023, live size, or funding. Autonomy stays **level 2**. No keys. No `kraken order`.

Sibling Coder 01/02 ([PR #132](https://github.com/eyeskull2220/solana-invoice/pull/132) / [PR #144](https://github.com/eyeskull2220/solana-invoice/pull/144)) own the **live** invert-paper gate. [PR #199](https://github.com/eyeskull2220/solana-invoice/pull/199) owns **how** a 2023+ 15m replay must not look ahead. This file owns **which one pair** that replay may rest.

### Fees / size (replay only, not a result)

If/when a slice scores `invert-wf-2023 1-limit rescore`: start **10000 EUR simulated**; taker **0.26%** default; also print **0.40** and **0.80**; two fills = two fees. Do not reuse live qty `160.64773` / `162.49066` as 2023 size.

---

## Verdict: **GREEN** (one-limit pick locks) · **RED** (00028 as invert; promotion; pretending this is a score)

| Probe | Result | Color |
|---|---|---|
| One pair from full set; at most one rest | P1–P5 written | **GREEN** (pack) |
| Causal `N=8`; armed `t` eligible `t+1`; `DUAL_TOUCH_SKIP` | Cited from PR #199, not rewritten | **GREEN** (named) |
| Live `PAPER-00028` extra buy | Second recipe vs L4 | **RED** as invert-compliance; **GREEN** as flagged, not flattened |
| `invert-wf-2023 1-limit rescore` fill/return/maxDD in this file | None (must not invent) | **YELLOW** (unscored) |
| 8-day `c9689f5d` as this rescore | Forbidden | **RED** if used |
| Reset `invert-paper` / `dca-paper` | Forbidden | **GREEN** (not touched) |
| Two buys on bar one | Named stop | **GREEN** (named) |
| Promotion / live / keys | Out of scope | **GREEN** (not done); **RED** if a later page funds from this |

**Promotion: no.** Stay paper. Gate on live `invert-paper` remains **NOT MET**. The named 2023 rescore has **no prints in this file**.

---

## RED

### R1 — Do not run fill-every-rung and call it invert

Full set in the markdown is not permission to rest every rung. Retired `2bfb1b68`. The 1-limit rescore exists because that reading is cheap.

### R2 — Do not treat live 00028 as the invert rest

After a buy fill, invert arms the **sell**. A leftover **buy** is a second recipe. Flag it. Leave the live book. Do not import two-buy arming into 2023.

### R3 — Do not invent the rescore

No archive in this git tree. Public OHLC cap is last week. No 2023 PASS line. Missing data ≠ GREEN.

### R4 — Do not promote

Live n=1. Paper engine: instant full fills, slippage 0 (Kraken paper skill). Method markdown is not a fund memo.

---

## YELLOW

### Y1 — Named score, no numbers

`invert-wf-2023 1-limit rescore` is the next **row name**. Slice researchers must disclose 15m source (CSV hash, first/last bar, gap list) and obey PR #199 L1–L6 **plus** P1–P5. Unknown source = do not stamp GREEN on the slice.

### Y2 — Live TP is 24h H, not a fib lesson

`PAPER-00030` @ 1.26778 = journal 24h H. Do not backfill 2023 `P_tp` from that latch. Do not “fix” 00030 from this page.

### Y3 — 00028 side/arm time

Journal now states **buy LIMIT**. Coder 01 (earlier sitting) did not have side in Surge HTML. Side is now on the hosted journal; **arm timestamp is still unknown here.** Do not invent when it was placed relative to 00029.

### Y4 — Connector / recipe file

Kraken MCP may be down. `/workspace/paper-recipes/` is not in `solana-invoice`. This pack does not dump engine JSON and must not place paper orders to “verify” one-limit.

### Y5 — Gap-through vs live queue

Touch-fill at `P` is already optimistic vs live LIMIT queue. One-limit does not fix that. Gap shadow stays a shadow column.

---

## GREEN

### G1 — Pick rule is two prices, one rest

Nearest below / nearest above last **closed** close. Wait if a side is missing. Inventory picks **which one** of those two is working.

### G2 — Look-ahead stops named

`N=8` confirm. Armed `t` → eligible `t+1`. `DUAL_TOUCH_SKIP`. No two buys on bar one.

### G3 — Clip cited, live books left alone

Full sha256:

`sha256:c9689f5d7d583320e724900b0ce4ef68193878c880d11939badd1dd59016e390`

No `paper reset` on `invert-paper` or `dca-paper`. No flatten of 00028. No Phantom send. No API keys.

### G4 — Gate language not redefined

Still: return > 0 after fees **and** ≥ 8 prints **and** maxDD ≤ 8%, on the book you claim. One-limit method ≠ “method exists so gate is green.” Live book still **1** fill. Named 2023 book still **unscored**.

### G5 — FACTUUR / keys / treasury

Out of this research. Treasury receive strings stay Wallet’s, never Kraken float:

- Solana USDC `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3`
- Base USDC `0x9eb954b567ef3616424a6e1bf42c63724930aa54`

---

## NOTES

- **Report-only.** No paper order, no live order, no journal HTML patch, no shop edit, no mail, no reseal, no reset. This file does not ping 00028.
- **Sources:** [PR #199](https://github.com/eyeskull2220/solana-invoice/pull/199) walk-forward method pack; [PR #132](https://github.com/eyeskull2220/solana-invoice/pull/132) `01-adv-research.md`; [PR #144](https://github.com/eyeskull2220/solana-invoice/pull/144) `02-adv-plan.md`; [PR #118](https://github.com/eyeskull2220/solana-invoice/pull/118) `docs/ultra-seats/CODER.md`; CEO machine [PR #142](https://github.com/eyeskull2220/solana-invoice/pull/142); live journal https://dca-paper-journal.surge.sh/ (this sitting: fills **1**, 00028 **buy LIMIT** 1.23084, 00030 24h H, clip cited); `kraken-paper-strategy` (0.26% taker, no slippage/partials); `kraken-autonomy-levels` (level 2 = paper).
- **Retired hashes stay retired.** `2bfb1b68` / `9056f296` / `094513` are not the 1-limit rescore.
- **Tax (not advice):** a simulated 2023 replay is not a tax event. Paper is not a tax event. Phantom sales-USDC = beroepsinkomen. Live Kraken later = apart handelsdossier. No invented FIFO.
- **PII:** no personal mailbox, no IBAN, no invented KBO. Operator: natural person, Geel. **KBO/BTW: nog niet toegekend.**
- Concurrent slice agents must **follow** PR #199 **and** this pick. They must not rest two buys “to get to 8 faster.” They must not **reseal** this pack with a PASS line.

**Promotion: no.** Stay paper. Do not reseal `c9689f5d`. Do not reset `invert-paper`. Do not reset `dca-paper`. Flag 00028 as a second recipe. Name `invert-wf-2023 1-limit rescore` without scoring it.

---

## Re-check (copy/paste)

```bash
# This pack must exist, cite PR 199, flag 00028, and must not contain a fake 2023 PASS:
rg -n 'DUAL_TOUCH_SKIP|N = 8|PAPER-00028|second recipe|invert-wf-2023 1-limit|two buys on bar one' \
  docs/rgy-2026-08-27/coder/RESEARCH-one-limit-arming.md

# Live journal is a different book — extra buy still open, fills 1:
curl -sS https://dca-paper-journal.surge.sh/ | rg -n 'PAPER-00029|PAPER-00030|PAPER-00028|fills 1|buy LIMIT|c9689f5d'

# Never:
# kraken paper reset --workspace invert-paper
# kraken paper reset --workspace dca-paper
# kraken order …
```

Count historical prints only from a **causal** 15m XRPEUR archive under PR #199 L1–L6 **and** one-limit P1–P5. If a slice rests two buys, it is not this method. Still paper.
