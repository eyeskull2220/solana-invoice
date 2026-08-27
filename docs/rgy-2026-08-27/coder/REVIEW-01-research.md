# REVIEWER — Coder RESEARCH stage RGY

Seat: **REVIEWER**. Stage: **Coder RESEARCH** only. Date: **2026-08-27**.

Score **starts at 0**. A row is GREEN only when the research pack is sourced, live-checked this sitting, internally consistent, and a later Coder plan/journal ping can proceed **without inventing fills, qty, engine JSON, a reseal, a `dca-paper` reset, or a live order**. This file does not implement. No live. No mail. No keys. No Phantom spend. No shop HTML.

**Artifact judged:** [PR #132](https://github.com/eyeskull2220/solana-invoice/pull/132) `docs/rgy-2026-08-27/coder/01-adv-research.md` (branch `cursor/rgy-coder-adv-research-7775`, HEAD of this leftover repo `2170952`).

**Not judged this batch:** Coder PLAN (#144 `02-adv-plan.md`), invert-paper journal HTML (#155), shop/Builder, Wallet, CEO punch-lists.

**GREEN on this page means the research pack is clean. It does not mean the invert-paper funding gate is met. The gate stays NOT MET.**

**GREEN count: 12 / 12. Stage: closed (research).** Promotion / live remains **RED** as a *finding inside the pack*, not as a fail of the pack.

| item | RED/YELLOW/GREEN | note | fix-if-not-green |
| --- | --- | --- | --- |
| fill count honesty | GREEN | Pack counts **1** (`PAPER-00029` buy XRPEUR @ **1.24496**). Resting TP `PAPER-00030` sell LIMIT @ **1.26778** is not a fill. Open `PAPER-00028` @ **1.23084** is not a fill. Matches operator / Coder seat [#118](https://github.com/eyeskull2220/solana-invoice/pull/118) `CODER.md`. This prompt lock: fill 1, TP 00030, 00028 open. Live Surge still prints **0** (see journal row). Not 0. Not 3. | — |
| gate conjuncts + NOT MET | GREEN | Gate = return > 0 **after fees** **and** fills **≥ 8** **and** maxDD **≤ 8%** on **`invert-paper`**. Have **1** print. Fail any one conjunct → stay paper. Return-after-fees and maxDD are **unknown** (n=1, no closed round-trip, no equity series). Unknown is not a pass. Sleeve 3x FAIL is **not** this gate. | — |
| journal 0 is stale, not the score | GREEN | Live-checked this sitting: https://dca-paper-journal.surge.sh/ still `Status: NOT MET (0 fills on invert-paper)`. Snapshot: `Journal republish` **2026-08-27 18:56 Europe/Brussels invert-paper** · `Funding gate` **NOT MET · 0 fills on invert-paper**. No `PAPER-00029` / `00030` / `00028` on that HTML. Pack treats 0 as **stale hosted HTML**, not as fill count, not as permission to reset. Git [#110](https://github.com/eyeskull2220/solana-invoice/pull/110) is an older DCA VOORBEELD (equity 9995.71, no invert ids). Three surfaces, two wrong counts if you trust Surge or git-only. | — |
| lab clip ≠ walk-forward; `c9689f5d` cited not resealed | GREEN | Live journal full hash `sha256:c9689f5d7d583320e724900b0ce4ef68193878c880d11939badd1dd59016e390` · name `fib-grid-invert-xrpeur-15m` · XRPEUR 15m 2026-08-18 21:00 → 2026-08-26 08:00 Europe/Brussels · 20 fills · +0.681154% · maxDD 0.890854% · PASS. Pack: sealed lab clip is **not** funding proof; 00029 is fill 1 of walk-forward, **not** fill 21; do not reseal; do not 20+1. Retired hashes `2bfb1b68` / `9056f296` / `094513` cited as not live. This PR does not rewrite the hash. | — |
| sleeve FAIL excluded | GREEN | Live journal: PF_XRPUSD 3x invert flip, 6 fills, −2.729078%, maxDD 5.326685%, numeric FAIL fills<8, **not the seal verdict**. Pack does not mix that PnL into `invert-paper` or `dca-paper`. Kill switch stays on the sleeve book. Does not invent a sleeve pass. Does not reopen at 5x. | — |
| still paper / no live | GREEN | Pack is report-only. Kraken MCP this run: **error / undiscoverable** (namespace failed discovery). `which kraken`: empty. No `kraken order`. No API-key fields. Autonomy **level 2**. `kraken-paper-to-live` still wants multi-session paper, working errors, positive return after fees, **user yes**, `--validate`, first live 10–25% of paper at autonomy 3. n=1 fails that. 10k is a **paper** EUR target, not a deposit. This reviewer run placed **no** orders. | — |
| `dca-paper` HOLD / not reset | GREEN | Five BTCUSD slices @ 78900.6 stay held (`PAPER-00002`…`00010`). Pack cites Coder/journal snapshot 2026-08-26: fills 5, equity **9995.71**, fee −3.25 at fill. Live Surge this sitting prints equity **9996.66** at 08:54 uPnL −3.34 — a later **mark**, not a reset. Fib → `fib-paper`. Grid → `grid-paper`. Official `recipe-launch-grid-bot` `paper init` banned on `dca-paper`. This PR does not touch that book. | — |
| no invented qty / FIFO / engine JSON | GREEN | This leftover `solana-invoice` tree has **no** `/workspace/paper-recipes/invert-paper.md` and no engine dump. Pack does **not** invent 00029 size, CAP, FIFO, or a walk-forward equity curve from three prices. Hypothetical 00030 round-trip (gross `1.26778 / 1.24496 − 1` = **+1.833%**; two taker 0.26% = **0.52%**; net ≈ **+1.31%**) is labeled **not a fill** and **not** scoreboard return. Rechecked this sitting: arithmetic holds. | — |
| live ticker tag ≠ paper print | GREEN | Public XRPEUR this sitting (after the pack’s 19:16 UTC quote): last **1.24802** (pack sitting last **1.24551** — timestamped; last moved). 24h high **1.26778000** = TP **1.26778**. 24h low **1.19568000** through **1.23084**. Today VWAP `p[today]` **1.24474549** ≈ pack **1.24474**. 15m OHLC: **2026-08-27 15:45 UTC** candle high **1.26778**. Many UTC candles today traded through 1.23084. Pack does **not** backfill 00030 or 00028 from OHLC. Paper does not model partials or queue. Operator book remains: 1 fill, TP resting, 00028 open. | — |
| allowlist fork documented | GREEN | Live journal CEO allowlist (2026-08-26 08:53 BXL): XRPEUR, XLMEUR, HBAREUR, **ADAEUR**, QNTEUR, XDCEUR, ALGOEUR. Coder seat [#118](https://github.com/eyeskull2220/solana-invoice/pull/118): wider EUR set including **`ADTEUR`** (not `ADAEUR`) plus BTCEUR/ETHEUR/…. XRPEUR is on **both** → this fill’s pair is fine. Extra pairs while n=1 are WAIT. Pack does not union the lists. IOTA unknown — not invented. | — |
| paper ≠ proof disclosed | GREEN | Matches `kraken-paper-strategy`: 0.26% taker applied; **slippage and partials not modeled**. Coder “ten ways” apply to n=1. Mark last vs fill is not gate 1. Pack does not promote. | — |
| scope hygiene | GREEN | Single new markdown on #132. Stamp VOORBEELD. Not FACTUUR / INVOICE. No shop/catalog/pay HTML. No journal republish. No reseal. No `dca-paper` reset. No Phantom send. Treasury strings cited as Wallet receive-only (Solana `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3`, Base `0x9eb954b567ef3616424a6e1bf42c63724930aa54`) — never as Kraken float. KBO/BTW: **nog niet toegekend**. Sibling PLAN (#144) is out of this batch. | — |

## Design-out (honour the pack — no RED/YELLOW rows to close)

Research is **closed**. A later Coder plan or journal ping **must not**:

1. **Treat pack GREEN as funding GREEN.** Invert-paper gate is **NOT MET** (1 < 8). Stay paper.
2. **Count 00030 or 00028 as fills** until they **print** as `PAPER-*` on `invert-paper`.
3. **Trust Surge at 0** as the score, or **reset any book** to make Surge match. A journal ping may reprint 00029; reseal/reset is not that ping.
4. **Reseal `c9689f5d`**, add 20+1, or treat the 8-day lab clip as walk-forward.
5. **Reset / convert `dca-paper`.** Five BTCUSD slices stay held.
6. **Mix sleeve FAIL PnL** into invert or DCA journals. Do not reopen at 5x.
7. **Go live**, paste keys, treat 10k as a deposit, or send Phantom treasury to Kraken.
8. **Backfill fills from the live ticker / OHLC** because high tagged 1.26778 or low traded through 1.23084.
9. **Invent qty, fees, maxDD, FIFO, CAP, or engine JSON** while Kraken MCP / `kraken` CLI / `invert-paper.md` are missing from this checkout.
10. **Broaden the EUR allowlist** (union of journal vs CODER.md, SOLEUR+ETHEUR, memecoins, invented IOTA) while invert has 1 fill.
11. **Naked short on spot** after a sell-TP. After TP you are flat cash; next entry is buy-back.
12. **Collapse books** (`dca-paper` USD hold, `invert-paper` EUR gate, leftover `fib-paper`, sleeve futures).

## Live cites (this reviewer sitting)

| URL / probe | What was opened |
| --- | --- |
| https://dca-paper-journal.surge.sh/ | `NOT MET (0 fills on invert-paper)`; republish **2026-08-27 18:56 Europe/Brussels invert-paper**; full `c9689f5d…` hash; lab clip 20 / +0.681154% / 0.890854%; sleeve 6 / −2.729078% / 5.326685% FAIL; no PAPER-00029; dca five slices @ 78900.6 equity **9996.66** |
| https://api.kraken.com/0/public/Ticker?pair=XRPEUR | last **1.24802**; 24h high **1.26778**; 24h low **1.19568**; VWAP today **1.24474549** |
| https://api.kraken.com/0/public/OHLC?pair=XRPEUR&interval=15 | 2026-08-27 **15:45 UTC** high **1.26778**; many session candles through **1.23084** |
| Kraken MCP | error / tools unavailable |
| `which kraken` / `/workspace/paper-recipes/` | empty / not in this git tree |
| [#132](https://github.com/eyeskull2220/solana-invoice/pull/132) `01-adv-research.md` | artifact — adversarial first, then RGY; fill 1; gate NOT MET |
| [#118](https://github.com/eyeskull2220/solana-invoice/pull/118) `CODER.md` | operator book 00029/00030/00028; ADTEUR allowlist fork; still paper |
| [#113](https://github.com/eyeskull2220/solana-invoice/pull/113) `CEO.md` | invert gate three conjuncts; no `dca-paper` reset; Kraken paper until gate |
| [#110](https://github.com/eyeskull2220/solana-invoice/pull/110) `dca-paper-journal/` | older VOORBEELD; equity 9995.71; no invert fill ids |
| `kraken-paper-strategy` / `kraken-paper-to-live` / `kraken-autonomy-levels` | 0.26% taker; slippage/partials unmodeled; level 2; first live 10–25%; `--validate`; user yes |

## Verdict

Coder RESEARCH pack (#132) is **GREEN**. Twelve rows closed. The pack is sourced, live-checked, and consistent: **invert-paper fill 1** (`PAPER-00029`), **TP 00030** and **00028 open** are not fills, **gate NOT MET**, Surge **may print 0** and that is still paper, **do not reseal `c9689f5d`**, **do not reset `dca-paper`**, **no live**.

Do not promote. Do not treat this GREEN as walk-forward. A later journal ping that reprints 00029 is still paper.

No implementation in this PR. No live.
