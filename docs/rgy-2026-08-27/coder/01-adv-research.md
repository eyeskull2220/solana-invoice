# 01 — Adversarial research (Coder `invert-paper`)

**Seat:** Coder  
**Lens:** adversarial **first**, then RED / YELLOW / GREEN. Research only. Not a plan. Not a fill.  
**Date:** 2026-08-27  
**Stamp:** VOORBEELD · paper / simulated · not FACTUUR · not INVOICE · not live-trade advice  
**HEAD (this repo):** `2170952`  
**Still paper.** Do not reseal `c9689f5d`. Do not reset `dca-paper`.

This file researches the **named funding-gate book** `invert-paper` (EUR 10000, XRPEUR 15m invert). It does not place orders, does not paste keys, does not spend Phantom, does not rewrite shop HTML, and does not republish the journal.

---

## Live book (operator / Coder seat — not the Surge journal)

| Id | Role | Price | Counts as a gate fill? |
|---|---|---|---|
| **PAPER-00029** | **FILL 1** · buy XRPEUR | **1.24496** | **Yes. This is fill 1.** |
| **PAPER-00030** | Resting TP · sell LIMIT | **1.26778** | **No.** Resting is not a fill. |
| **PAPER-00028** | Open | **1.23084** | **No.** Open is not a fill. |

Fill count toward the gate: **1**. Not 0. Not 3.

**Gate (all three, same book):** return > 0 **after fees** · fills **≥ 8** · maxDD **≤ 8%**.  
**Status: NOT MET.** Sleeve 3x FAIL is **not** this gate.

---

## Adversarial first

Attacks that would fake a green invert book. Each is a **stop**, not a note to bargain.

1. **Treat the 8-day lab clip as walk-forward.** Spot PASS 20 fills, +0.681154%, maxDD 0.890854% vs `sha256:c9689f5d…` is a **sealed lab clip**, not funding proof. Do not fund because +0.68% exists. Do not reseal to restamp it as today’s walk-forward.

2. **Treat sleeve FAIL as the gate.** PF_XRPUSD 3x invert flip scored 6 fills, −2.729078%, maxDD 5.326685%, FAIL fills<8. That FAIL does not greenlight live and does not replace the spot gate. Mixing sleeve PnL into `invert-paper` or `dca-paper` is journal fraud.

3. **Count 00030 or 00028 as fills.** Gate language is fills with a `PAPER-*` **print**, not resting limits. 00030 is TP. 00028 is open. Inventing “3 fills” to look closer to 8 is cheating.

4. **Trust `dca-paper-journal.surge.sh` at 0.** Live journal (fetched 2026-08-27): `Status: NOT MET (0 fills on invert-paper)` and snapshot line `Journal republish 2026-08-27 18:56 Europe/Brussels invert-paper` still prints **0**. Operator book is **fill 1**. The Surge page is **stale**. Do not “fix” staleness by resetting any book. Do not treat 0 as the score.

5. **Go live, or treat 10k as a deposit.** Invert-paper capital is a **paper** EUR 10000 target. Paper-to-live skill still needs repeated sessions, explicit human yes, and `--validate`. Autonomy stays at **level 2**. Kraken MCP on this run: **error / undiscoverable**. No CLI dump of the engine JSON from here.

6. **Reset `dca-paper` to make a prettier ledger.** Five BTCUSD slices stay held. Fib → `fib-paper`. Grid → `grid-paper`. Invert stays `invert-paper`. Official `recipe-launch-grid-bot` `paper init` is banned on `dca-paper`.

7. **Reseal `c9689f5d`.** Cite it. Do not rotate, rewrite, or rehash so the journal looks newer.

8. **Rush 8 fills with extra clips / extra pairs.** Adding SOLEUR+ETHEUR or a second invert clip because n=1 feels slow is gate-cheating. Re-arm only on the **opposite** fill of the invert pair. Do not pyramid. Do not flatten 00030/00028 “to clean the book.”

9. **Call a live ticker tag a paper fill.** Kraken public XRPEUR (this sitting, 2026-08-27 19:16 UTC): last **1.24551**, 24h high **1.26778** (exact TP), 24h low **1.19568** (through 1.23084). A live print **through** a limit is not `PAPER-00030` or `PAPER-00028` filling. Paper does not model partials or queue. Do not backfill fills from OHLC.

10. **Mark-to-market the buy into “return > 0.”** Last 1.24551 vs fill 1.24496 is a tiny mark (~+0.04%). Starter taker **0.26%** already on the buy (~0.003237 on the rate). Gate 1 is shadowed round-trip after fees, not “XRP ticked up.” 00030 is **not** profit until it prints **and** the sell fee is subtracted.

11. **Use a retired invert hash.** Live lock name `fib-grid-invert-xrpeur-15m` vs `c9689f5d`. Retired: `2bfb1b68` fill-every-rung · `9056f296` entry-waits-TP · `094513` arming-only (99 fills PASS on that old hash is not live).

12. **Naked short on spot after a sell-TP.** Recipe: after sell-TP you are **flat cash**; next entry is buy-back. Sleeve 3x may flip long↔short on PF_XRPUSD. Spot invert-paper may not.

13. **Invent qty, fees, maxDD, or engine JSON.** This repo has no `paper-recipes/invert-paper.md`. Kraken MCP is down. This run does **not** know 00029 size. Do not invent FIFO, CAP, or a walk-forward equity curve from three prices.

14. **Collapse books.** `dca-paper` is USD hold. `invert-paper` is EUR gate. `fib-paper` leftover BTCUSD is not the gate. Sleeve is futures paper. One scoreboard row per book.

15. **Broaden the EUR allowlist while n=1.** Journal CEO allowlist (ticker-confirmed 2026-08-26): XRPEUR, XLMEUR, HBAREUR, ADAEUR, QNTEUR, XDCEUR, ALGOEUR. CODER seat page (#118) lists a **wider** EUR set (BTCEUR, ETHEUR, … and `ADTEUR`). XRPEUR is on **both**. Extra pairs are WAIT. Do not paper a pair that is only on one list without CEO.

---

## Verdict: **RED** (gate) · **GREEN** (locks this run honoured)

Promotion / funding / “invert is proven”: **RED**.  
Still-paper / no reseal / no `dca-paper` reset / sleeve-is-not-the-gate: **GREEN** as *rules*, not as a reason to fund.

| Probe | Result | Color |
|---|---|---|
| Walk-forward gate on `invert-paper` | 1 fill < 8; return-after-fees unknown; maxDD unsampled | **RED** |
| Surge journal fill count | Prints **0**; book is **1**; republish 18:56 BXL still 0 | **RED** |
| 8-day lab clip as funding proof | PASS clip ≠ walk-forward; do not reseal `c9689f5d` | **RED** |
| Sleeve 3x as gate | FAIL fills<8; separate book; not the gate | **GREEN** (correctly excluded) |
| Resting 00030 / open 00028 counted as fills | Must not be | **GREEN** if counted 1; **RED** if counted 3 |
| Live XRPEUR tag vs paper prints | High = TP 1.26778; low through 1.23084; still 1 fill | **YELLOW** |
| Paper ≠ live (fees/slippage/partials) | Skill + Coder “10 ways”; slippage 0 in engine | **RED** as proof; **GREEN** as disclosed |
| Kraken MCP / engine dump | Namespace error; no `kraken` binary here | **YELLOW** |
| Still paper / no keys / no Phantom | This file + this PR | **GREEN** |
| Do not reseal `c9689f5d` | Cited, not rewritten | **GREEN** |
| Do not reset `dca-paper` | Not touched | **GREEN** |
| Pair XRPEUR on allowlist | On journal + Coder lists | **GREEN** |
| `invert-paper.md` in this git tree | Absent | **YELLOW** |

---

## RED

### R1 — Gate NOT MET (fills)

Need **≥ 8** prints on `invert-paper`. Have **1** (`PAPER-00029`). 00030 and 00028 do not count. `dca-paper`’s 5 BTC slices are a **different** book and also < 8. Fail any one conjunct → stay paper. Do not “almost.”

### R2 — Honest journal is stale at 0

https://dca-paper-journal.surge.sh/ (fetched this sitting):

- `Status: NOT MET (0 fills on invert-paper).`
- Snapshot: `Journal republish` **2026-08-27 18:56 Europe/Brussels invert-paper** · `Funding gate` **NOT MET · 0 fills on invert-paper**.

Git PR #110 (`dca-paper-journal/`) is an older VOORBEELD page (DCA checklist). Live Surge is a **later** invert-gate page that still under-counts. Coder seat `#118` already journals fill 1. Three surfaces, two wrong counts if you trust Surge or git-only.

Stale-at-0 is not permission to reset. It is permission to **distrust the hosted HTML** until a Coder journal ping reprints 00029.

### R3 — Lab clip is not the walk-forward

Sealed name `fib-grid-invert-xrpeur-15m`. Lab window on the journal: XRPEUR 15m, 2026-08-18 21:00 → 2026-08-26 08:00 Europe/Brussels. 20 fills · +0.681154% · maxDD 0.890854% vs

`sha256:c9689f5d7d583320e724900b0ce4ef68193878c880d11939badd1dd59016e390`

Walk-forward is **new** fills on `invert-paper` after that seal. Today’s 00029 is fill 1 of **that** book, not fill 21 of the clip. Do not add 20+1. Do not reseal.

### R4 — Paper is not proof (even when the ticker is live)

Kraken paper skill: 0.26% taker applied; **slippage and partials not modeled**; limits may sit while live tags the level. Coder seat “ten ways” applies to this one fill. A single XRPEUR print at 1.24496 is a **story**, not a sample.

Round-trip **if** 00030 printed at 1.26778 with two full taker fees and zero slippage:

- Gross: `1.26778 / 1.24496 − 1` = **+1.833%**
- Fees: 0.26% + 0.26% = **0.52%**
- Net ≈ **+1.31%** before any shadow spread

That hypothetical is **not** a fill. It would still be **2 < 8**. Do not write it into the scoreboard as return.

### R5 — Do not promote

`kraken-paper-to-live` wants consistent multi-session paper, working error handling, positive return after fees, and **user yes**. This sitting: n=1, MCP dead, journal lying about 0, no qty, no maxDD path. First live size (10–25% of paper) is a **later** page. Not this file.

---

## YELLOW

### Y1 — Live high equals TP; paper still shows resting 00030

Public ticker 24h high **1.26778000** = TP **1.26778**. 15m OHLC: 2026-08-27 15:45 UTC candle high 1.26778. Last now **1.24551**, back under the TP.

Possible without inventing a fill:

- 00030 was armed **after** the high.
- Paper limit did not print on an exact tag (touch vs through).
- Operator book is the source of truth: **still TP**.

Do not close 00030 from this research. Ping only when **it** prints.

### Y2 — Live traded through 1.23084 many times; 00028 still open

Today’s Brussels session traded **below 1.23084** on a large stack of 15m candles (low 1.19568). If 00028 was a **buy** limit already working in that window, live would have been through it. Paper still says open. **Arm timestamp is unknown here.** Side is not in the Surge HTML. User/Coder: open @ 1.23084. Do not backfill. Do not cancel.

### Y3 — Connector / recipe file missing from this checkout

- Kraken MCP: error, tools unavailable.
- `which kraken`: empty on this VM.
- `/workspace/paper-recipes/` : not in `solana-invoice`. Journal says recipes live there (`invert-paper.md`, `fib-paper.md`, …). This git tree cannot show the recipe text. Cite the Surge recipe summary + Coder seat; do not invent a markdown file.

### Y4 — Allowlist fork

Journal (2026-08-26 08:53 BXL): seven spot EUR pairs; sleeve only XRP/XLM/HBAR/ADA/ALGO; QNT+XDC spot-only; IOTA unknown — do not invent.  
CODER.md: longer EUR list including `ADTEUR` (not `ADAEUR`).  

XRPEUR is allowed on both → this fill’s **pair** is fine. Expanding the book to the union of the two lists while invert has 1 fill is WAIT.

### Y5 — maxDD and shadowed return cannot be scored

n=1 open long, no closed round-trip, no equity series in this repo. Gate 1 and gate 3 are **not measurable** yet. That is not a pass. Unknown is not ≤ 8%.

### Y6 — Fee shadow not on Surge

Coder STARTABLE wants engine 0.26% + conservative extra + round-trip. Surge gate copy uses the three conjuncts but does not print a shadow column next to 00029 (because it still thinks fills=0). Missing shadow ≠ set extra to 0.

---

## GREEN

### G1 — Sleeve FAIL is not the gate

Journal sleeve block: 6 fills, −2.729078%, maxDD 5.326685%, numeric FAIL fills<8, **not the seal verdict**. Coder seat repeats it. This research **does not** mix that PnL into invert. Kill switch (kill file / 10% sleeve DD / lev > 3x) stays on the sleeve book. Do not invent a sleeve pass. Do not reopen at 5x.

### G2 — Still paper; locks held on this run

No live `kraken order`. No API keys in this file. No Phantom send. No `dca-paper` reset. No reseal of `c9689f5d` (quoted in full above as the journal prints it). No extra clip. No memecoin. No FACTUUR title.

### G3 — Named book is `invert-paper`, not DCA, not leftover fib

Journal: walk-forward lives on `invert-paper` only. `fib-paper` leftover BTCUSD stays, not the gate. `dca-paper` five slices @ 78900.6 stay held (PAPER-00002…00010). 00029 is an invert-paper id class, not a sixth DCA slice.

### G4 — Fill honesty if you use the operator book

Count **1**. Recipe still invert: 15m, full fib set (retracements 0.236 / 0.382 / 0.5 / 0.618 / 0.786 + extensions 1.272 / 1.618 / 2.0 / 2.618 both sides), every level a rung, after **any** fill swap jobs of **those two** prices, re-arm only on the opposite fill, spot no naked short.

### G5 — XRPEUR is an allowlisted spot EUR pair

Not a meme ticker. Not QNT/XDC sleeve. Not invented IOTA. Matches invert lock pair.

### G6 — `FACTUUR` / live keys / Phantom treasury spend

Out of this Coder research. Treasury receive strings stay Wallet’s, never Kraken float:

- Solana USDC `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3`
- Base USDC `0x9eb954b567ef3616424a6e1bf42c63724930aa54`

---

## NOTES

- **Report-only.** No paper order, no journal HTML patch, no shop edit, no mail. Sibling Coder 02 (adv-plan) may propose a journal ping; this 01 does not implement it.
- **Sources:** operator live triple (00029 / 00030 / 00028); Coder seat `docs/ultra-seats/CODER.md` on `cursor/coder-ultra-seat-8db1` (#118); live journal https://dca-paper-journal.surge.sh/ ; CEO seat invert-gate (#113); Kraken public `Ticker`+`OHLC` interval 15 XRPEUR at 2026-08-27 19:16 UTC; `kraken-paper-strategy` / `kraken-paper-to-live` / `kraken-autonomy-levels` skills. Kraken MCP: **error**.
- **VWAP today** 1.24474 sits next to fill 1.24496. That rhymes; it does not prove the engine, the size, or the gate.
- **dca-paper** snapshot on Coder/journal (2026-08-26): 5 fills, equity 9995.71, fee −3.25 at fill. Gate fail on fills+return. Leave it.
- **Tax (not advice):** paper is not a tax event. Phantom sales-USDC = beroepsinkomen. Live Kraken later = apart handelsdossier. Accountant picks cost basis. No invented FIFO. No CAP / Vak XIII from this JSON.
- **PII:** no personal mailbox, no IBAN, no invented KBO. Operator: natural person, Geel. **KBO/BTW: nog niet toegekend.**
- Concurrent Ultra seats (CEO / Scout / Wallet / Compliance / Builder RGY) are not this scoreboard. Do not merge their shop HTML into a Coder ticket.

**Promotion: no.** Stay paper. Gate NOT MET. Sleeve FAIL is not the gate. Journal may be stale at 0. Do not reseal `c9689f5d`. Do not reset `dca-paper`.

---

## Re-check (copy/paste)

```bash
curl -sS https://dca-paper-journal.surge.sh/ | rg -n '0 fills|PAPER-00029|NOT MET|c9689f5d'
curl -sS 'https://api.kraken.com/0/public/Ticker?pair=XRPEUR'
# engine (when Kraken MCP / kraken CLI exists — not this VM):
# kraken paper status --workspace invert-paper -o json
# kraken paper history --workspace invert-paper -o json
# kraken paper orders --workspace invert-paper -o json
```

Count fills only from `PAPER-*` **prints** on `invert-paper`. If 00030 or 00028 prints, that is a **later** ping. Still paper.
