# REVIEWER — Coder PLAN (02)

**Seat:** REVIEWER  
**Batch:** Coder PLAN only (not research, not CODE, not journal HTML)  
**Date:** 2026-08-27  
**Artifact:** [PR #144](https://github.com/eyeskull2220/solana-invoice/pull/144) `docs/rgy-2026-08-27/coder/02-adv-plan.md`  
**Stamp:** VOORBEELD · paper / simulated · not FACTUUR · not INVOICE · not live-trade advice  
**This file is judgment only.** It does not implement. It does not place paper or live orders. It does not reseal `c9689f5d`. It does not reset `dca-paper`. It does not patch Surge. It does not send mail. It does not invent a KBO.

GREEN for this stage only if the **plan** has no red and no yellow. World-state (walk-forward still NOT MET, Surge still 0) is recorded below and is **not** this grade.

---

## Verdict: **GREEN**

The PLAN page holds the four named locks. It does **not** promote the lab clip. It does **not** promote live. No remaining red or yellow on this artifact.

This is **not** a stamp that `invert-paper` is funded, walk-forward is proven, or Coder may go live. Promotion stays **RED** on the book. The plan itself already says that. Reviewer agrees, and does not convert it.

| Plan gate (this artifact) | Score |
| --- | --- |
| Leave `c9689f5d` (cite, do not rotate) | **GREEN** |
| `dca-paper` stay (do not reset / convert) | **GREEN** |
| Gate on `invert-paper` only | **GREEN** |
| Still paper (autonomy 2) | **GREEN** |
| Plan promotes lab clip as walk-forward / funding | **GREEN** (does not) |
| Plan promotes live / 10k as deposit / CLI-while-MCP-dead | **GREEN** (does not) |
| Fill-count language | **GREEN** (prints = **1**) |
| Orders / reseal / reset from this plan | **GREEN** (forbidden) |
| **PLAN stage** | **GREEN** |

| World (not this grade) | Score |
| --- | --- |
| Walk-forward on `invert-paper` | **RED** — fill **1** < 8; return-after-fees unknown; maxDD unsampled |
| Live Surge journal | stale **0 fills** (operator/Coder book is **1**) — later journal ticket, not this PLAN |
| Lab clip `c9689f5d` as funding proof | still **not** proof — plan refuses; reviewer refuses |

---

## ADVERSARIAL (first)

A PLAN that can ship is a page a later agent could follow **without** turning a sealed lab clip, a hold book, or a stale journal into live money. Attack this file as if it were a bad layout.

### A1 — Would a later agent reseal `c9689f5d` from this page?

Ways it would fail:

1. Restamp the 8-day PASS (20 fills, +0.681154%, maxDD 0.890854%) as today’s walk-forward.
2. Add 20+1 (`PAPER-00029`) and call it 21 fills.
3. Rotate the hash so a journal republish looks newer.
4. Revive retired `2bfb1b68` / `9056f296` / `094513` (99 fills PASS on that old hash is not live).
5. Reseal to “fix” Surge at 0.

**Plan text:** cites the full sha256, names the clip `fib-grid-invert-xrpeur-15m`, calls it lab **not** funding proof, sleeve FAIL on the same lock stays FAIL, next work is fill-ping not a new hash. **Do not reseal.**

**Reviewer:** the page cannot be followed into a reseal without ignoring its own stop. Lock holds.

### A2 — Would a later agent reset `dca-paper` from this page?

Temptations: fills 5 < 8 looks ugly; USD vs EUR invert looks “wrong”; fib/grid want `paper init`; convert BTC to EUR to “unify.”

**Plan text:** five BTCUSD slices stay held (PAPER-00002…00010 @ 78900.6). Reset / sell / convert is a stop. Fib → `fib-paper`. Grid → `grid-paper`. Invert stays `invert-paper`. Official `recipe-launch-grid-bot` `paper init` banned on `dca-paper`. Stay = read-only `status` / `history` / `balance`. Not a sixth slice. Not the gate.

**Reviewer:** cannot be followed into a reset without ignoring a stop. Lock holds.

### A3 — Would a later agent shop a green row that is not `invert-paper`?

Wrong books the desk already owns: lab clip PASS, `dca-paper` “almost 8,” 3x sleeve FAIL-as-story, leftover `fib-paper` BTCUSD, CODER.md Gate column listing `dca-paper`.

**Plan text:** fund gate = `invert-paper` only, all three conjuncts on **that** book (return > 0 after fees **and** ≥ 8 prints **and** maxDD ≤ 8%). Resting `PAPER-00030` / open `PAPER-00028` are not fills. Do not add extra clips or extra pairs to rush 8. Do not flatten 00030/00028 “to clean the book.”

**Reviewer:** the page names one book and forbids the others. CODER.md’s Gate-column leak is **adjacent inventory**, not a second gate this PLAN endorses. Lock holds.

### A4 — Would a later agent go live from this page?

Temptations: lab clip already PASS; Kraken MCP dead so “we’ll CLI it”; 10k paper capital as SEPA deposit; live XRPEUR tagged the TP so “the paper TP would have filled”; autonomy skip 2 → 3; `--validate` then live.

**Plan text:** still paper, autonomy **level 2**, no `kraken order` / `kraken futures order`, no keys in git/HTML/this plan, no Phantom spend, no `--validate` then live. Paper-to-live (10–25%, dead-man, human yes) is a **later** page **after** invert-paper is green **and** CEO yes **and** connector healthy. This week it is not.

**Reviewer:** mentioning the later paper-to-live skill path is WAIT language, not a live order. Same later-page rule already sits on CEO `#113` §7. This PLAN does not promote live. Lock holds.

---

## What was judged (PLAN sources, from zero)

PLAN means: the written locks a later Coder page must repeat. Not a fill. Not a journal patch.

| Source | What it is |
| --- | --- |
| PR #144 `02-adv-plan.md` | The artifact. |
| PR #132 `01-adv-research.md` | Sibling research: gate RED (1 fill); Surge stale at 0; locks GREEN. Plan sits on it. |
| PR #118 `docs/ultra-seats/CODER.md` | Seat contract: inventory, STARTABLE (fee shadow, honest journal, fill ping), WAIT (live / extra pairs / extra clips). Scoreboard still lists `dca-paper` under Gate — inventory, not this PLAN’s pick-list. |
| PR #113 CEO | Invert closed until all three numbers + human yes + healthy connector. Do not reset `dca-paper`. |
| Live https://dca-paper-journal.surge.sh/ | Fetched this sitting. `NOT MET (0 fills on invert-paper)`. LIVE LOCK `c9689f5d` shown, not resealed. Republish **2026-08-27 18:56 Europe/Brussels**. |
| Kraken public Ticker XRPEUR | This sitting: last **1.24706**, 24h high **1.26778** (exact TP), 24h low **1.19568**. A live tag is not a paper print. |
| Kraken skills | `kraken-autonomy-levels` (level 2 = paper); `kraken-paper-to-live` (no silent live; user yes; slippage/partials unmodeled). |
| This run | Kraken MCP **error**. No `kraken` binary. No `/workspace/paper-recipes/` in this git tree. **No orders.** |

`main` still has no Coder RGY tree. The plan exists only on #144.

---

## RED

**None on this artifact.**

Closed as PLAN defects (they would have been RED if the page had done them):

| If the plan had… | What it actually does |
| --- | --- |
| Promoted `c9689f5d` / 20 fills / 20+1 as walk-forward | Cites the seal; lab ≠ funding; fill 1 is new prints after the seal |
| Reset / convert `dca-paper` | Stay. New recipes → new workspaces |
| Gated on sleeve / DCA / leftover fib / “any book that hits 8” | Named book `invert-paper` only |
| Counted 00030 / 00028 / Surge 0 / clip 20 as the fill count | Count stays **1** |
| Gone live, deposited 10k, CLI-while-MCP-dead, `--validate` then live | Autonomy 2. Later page only after gate + CEO + healthy connector |
| Implemented from the PLAN file (orders, HTML, reseal) | “Do not implement from this plan.” |

World-state RED (fill 1 < 8, Surge 0, clip is not proof) remains **true**. It is the reason promotion stays RED. It is not a hole in the lock page.

---

## YELLOW

**None remaining on this PLAN.**

Adjacent items the plan itself scored YELLOW are **world / sibling pages**, designed out of this grade:

### Designed out — Surge stale at 0 (plan B2)

https://dca-paper-journal.surge.sh/ still prints `NOT MET (0 fills on invert-paper)` after the 18:56 BXL republish. Operator/Coder book is fill **1** (`PAPER-00029` buy XRPEUR @ 1.24496). Git #110 is the older DCA checklist.

A PLAN that patched HTML, resealed, or reset to make Surge match would have been RED. This PLAN says: later **journal** ticket may ping 00029; reseal/reset is not that ping; this file does not patch HTML. That is the correct PLAN-stage scope. Stale hosted HTML is not a PLAN-lock fail.

### Designed out — CODER.md Gate column lists `dca-paper` (plan B5)

`#118` inventory table has a Gate cell on `dca-paper` (FAIL fills+return). That is a pick-list leak on the seat page. This PLAN attacks it: keep the inventory; do not let a later agent promote DCA because it has a Gate cell; one named funding book = `invert-paper`.

Fixing `#118` is not this PLAN’s job. Endorsing the leak would have been RED. The plan does not endorse it.

### Designed out — vanity net on unfilled 00030

Plan (and research #132) compute ~+1.31% if 00030 printed at 1.26778 after two 0.26% takers, zero slippage, then immediately: **not a fill**, would still be 2 < 8, do not write it into the scoreboard. Computing the trap in order to forbid it is not a yellow on the PLAN.

### Designed out — STARTABLE vs “do not implement from this file”

A4 lists fee shadow / honest journal / fill ping as STARTABLE inherited from `#118`, “still not implementation in *this* file.” NOTES: no paper order, no live order, no journal HTML patch from this plan. Later Coder work is fill-ping / fee-shadow copy — still paper.

That is a lock page pointing at a later still-paper ticket, not a work order to execute from #144. Reviewer does not treat PLAN GREEN as permission to ping, patch, or order.

---

## GREEN (locks on the artifact)

### G1 — Leave `c9689f5d`

Full hash in the plan, matching live journal:

`sha256:c9689f5d7d583320e724900b0ce4ef68193878c880d11939badd1dd59016e390`

Name `fib-grid-invert-xrpeur-15m`. Window 2026-08-18 21:00 → 2026-08-26 08:00 Europe/Brussels. Spot PASS 20 fills · +0.681154% · maxDD 0.890854%. Sleeve FAIL 6 fills · −2.729078% · maxDD 5.326685% — not the gate, not a reason to reseal. Retired hashes stay retired. Coder may read and cite. Coder may not rewrite, rotate, or rehash.

### G2 — `dca-paper` stay

Five held BTCUSD slices. Grandfathered USD. Equity snapshot on the seat page ~9995.71; journal this fetch still shows the five PAPER-00002…00010 rows @ 78900.6, open orders 0. Not the EUR gate. Not a sixth clip. Stay = read-only.

### G3 — Invert-only gate, count = 1, NOT MET

| Id | Role | Price | Gate fill? |
| --- | --- | --- | --- |
| PAPER-00029 | FILL 1 · buy XRPEUR | 1.24496 | yes |
| PAPER-00030 | resting TP sell LIMIT | 1.26778 | no |
| PAPER-00028 | open | 1.23084 | no |

Fill count = **1**. Not 0 (Surge). Not 3 (rest+open). Not 21 (clip+00029). Not 5 (`dca-paper`). Gate conjuncts are all required on `invert-paper`. **NOT MET.** Plan says so. Reviewer says so.

Public ticker this sitting still prints 24h high **1.26778**. Live tag ≠ paper print. Plan forbids backfill.

### G4 — Still paper

Autonomy **level 2** (`kraken-autonomy-levels`: paper, no live key). Level 3 (`--validate` then live, dead-man) is WAIT. `kraken-paper-to-live` still wants multi-session paper, working errors, return after fees, **user yes**. This sitting: n=1, MCP dead, journal lying about 0, no qty/maxDD path in this git tree. No keys in the plan. No Phantom bot against `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3` or Base `0x9eb954b567ef3616424a6e1bf42c63724930aa54`.

### G5 — Identity / mail / shop

No fake KBO. No FACTUUR title. No mail. No shop/catalog HTML. Operator: natural person, Geel. **KBO/BTW: nog niet toegekend.** Out of this PLAN, and the PLAN leaves it out.

---

## Bar the PLAN already writes (reviewer repeats, does not add work)

A later Coder page that follows #144 must still say, in spirit:

1. **Do not reseal** `sha256:c9689f5d7d583320e724900b0ce4ef68193878c880d11939badd1dd59016e390`. Cite only. Lab clip ≠ walk-forward.
2. **Do not reset `dca-paper`.** Five BTCUSD slices stay held. New recipes → new workspaces.
3. **Fund gate = `invert-paper` only.** All three conjuncts on that book. Sleeve / DCA / fib leftover / lab clip are not the gate.
4. **Count prints, not rests.** 00029 = 1. 00030 and 00028 do not count until they print.
5. **Still paper** until CEO says live **and** the invert-paper gate is green **and** Kraken connector is healthy. Autonomy 2. No keys in git.
6. **Honest journal** may ping 00029; it may not “fix” Surge by reseal or reset.
7. **No extra pairs, no extra clips, no memecoins, no Phantom bot, no FACTUUR.**

**Promotion stays RED** until invert-paper itself is GREEN on the three conjuncts. That is a later scoreboard. Reviewer GREEN on PLAN does not change it.

---

## This run

| Did | Did not |
| --- | --- |
| Read #144 plan, #132 research, #118 seat, #113 CEO invert gate | Place paper or live Kraken orders |
| Fetched live journal + public XRPEUR ticker | Reseal `c9689f5d` |
| Scored PLAN locks RGY from zero | Reset `dca-paper` |
| Confirmed hash, fill-1 language, invert-only, still-paper | Patch Surge / shop HTML / CODER.md |
| | Mail, KBO, Phantom spend, keys in git |

**PLAN stage: GREEN.** Still paper. No reseal. No `dca-paper` reset. Gate on `invert-paper` only — **NOT MET** on the book. No live. No mail. No KBO.

---

## Re-check (copy/paste)

```bash
# hosted journal (expect 0 fills, lock c9689f5d shown not resealed)
curl -sS https://dca-paper-journal.surge.sh/ | rg -n '0 fills|PAPER-00029|NOT MET|c9689f5d'

# public ticker (read-only — not an order)
curl -sS 'https://api.kraken.com/0/public/Ticker?pair=XRPEUR'

# engine (when Kraken MCP / kraken CLI exists — not this VM, not this review):
# kraken paper status --workspace invert-paper -o json
# kraken paper history --workspace invert-paper -o json
# kraken paper orders --workspace invert-paper -o json
```

Count fills only from `PAPER-*` **prints** on `invert-paper`. If 00030 or 00028 prints, that is a **later** ping. Still paper.

End of Coder PLAN review.
