# CODER seat — Kraken paper (still paper)

**Date:** 2026-08-27  
**Stamp:** VOORBEELD · paper / simulated · not a FACTUUR · not an INVOICE · not live-trade advice  
**Operator:** natural person, Geel. **KBO/BTW: nog niet toegekend.** Do not invent a firm name or a BE0… number.  
**Status:** **STILL PAPER.** Coder does not go live, does not paste API keys, does not spend Phantom, does not reset `dca-paper`, does not reseal `c9689f5d`.

This page is the Coder seat contract. Builder owns kits/shop. Scout owns buyers. Wallet owns the two treasury receive strings. Coder owns **Kraken paper books** and the honest journal around them.

Pay-to for *sales* USDC (not trading capital):

- Phantom Solana USDC: `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3`
- Base USDC: `0x9eb954b567ef3616424a6e1bf42c63724930aa54`

Those addresses are **treasury**. Never send them to Kraken. Never run a Phantom bot against them. Never treat sales-USDC as trading float.

---

## Who does what

| Seat | Owns | Does not |
| --- | --- | --- |
| **Coder** | Kraken paper inventory, EUR-pair allowlist, fee shadow, honest journal, fill ping, the fund **gate** | Live orders, API keys, Phantom spend, memecoins, applying the operator as a developer |
| **Builder** | HTML kits / shop / Peppol packs | Kraken books |
| **Scout** | Buyer lists, public mailtos | Coding-job applies in the operator’s name |
| **Wallet** | The two receive addresses above | Trading, perps, new keys |
| **Operator (Geel)** | Own Kraken account later, SEPA, exports, accountant | Code, host, debug, or “be the freelancer” |

Coder stays at **autonomy level 2** (paper). Level 3+ (live keys, `--validate` then live, dead-man) is **WAIT** until the CEO says live **and** the fund gate is green.

---

## Fund gate (this is the gate — not the 3x sleeve)

A paper book is **not** a reason to fund live. The sleeve result is **not** the fund gate.

**Gate (all three must hold on the book you want to promote):**

1. **Return > 0 after fees** (Kraken Starter **0.26% taker** per fill already in the paper engine, plus the fee-shadow haircut below — not mark-to-market that ignores round-trip costs).
2. **≥ 8 fills** (closed or fully filled prints with a `PAPER-*****` id). Resting limits are not fills.
3. **maxDD ≤ 8%** from peak equity on that book.

Fail any one → stay paper. Do not “almost.” Do not average the 3x sleeve into spot to make the number pretty.

**3x sleeve FAIL is not the fund gate.** The moderate-leverage futures paper (cap 3x, kill switch: flatten + cancel-all on kill file, **10% sleeve drawdown**, or leverage > 3x) is a **separate** book. Its FAIL does not greenlight live, and it does not redlight the spot gate by itself. **Never mix sleeve PnL into `dca-paper` or `invert-paper` journals.**

---

## Inventory (Coder-owned paper)

Leave running books alone unless the CEO names a change. Named workspaces are **operator books** (do not `init`/`reset` the wrong file).

### `dca-paper` — HOLD. Do not reset.

VOORBEELD snapshot already journaled (2026-08-26 08:38 Europe/Brussels), paper / simulated:

| Field | Value |
| --- | --- |
| Mode | paper |
| Start | 10000 USD |
| Fee | 0.26% |
| Slippage | 0 (unmodeled — see “10 ways”) |
| Fills | **5** BTCUSD market buys (not 8) |
| Per fill | 0.00317 BTC @ 78900.6 · cost 250.114902 · fee 0.6502987452 |
| BTC total | 0.01585 |
| Mark last | 78835.2 |
| Equity | 9995.71 |
| Unrealized | −4.29 (−0.043%) |
| Open orders | 0 |

Wallet first printed **−3.25** at fill (fees). Later the mark moved with spot. **Long-term hold** — do not sell this stack unless the CEO says. Fibonacci and grids do **not** get to recycle this book.

Gate read on this snapshot: return after fees is **not** > 0; fills **5 < 8**. Stay paper. Do not reset.

### `invert-paper` — active paper, do not flatten for cosmetics

| Id | State | Detail |
| --- | --- | --- |
| **PAPER-00029** | **FILL 1** | Fill price **1.24496** |
| **PAPER-00030** | Resting TP | **Sell LIMIT @ 1.26778** (not a fill until it prints) |
| **PAPER-00028** | **Open** | Still working — not a fill |

Fill count toward the gate: **1**. Resting TP and the open 00028 do **not** count. Do not add extra clips to rush 8 fills. Do not cancel 00030/00028 to “clean the book.”

If 00030 prints, journal it as fill 2 (fee shadow on the sell). If 00028 prints, journal it. Then stop and re-read the gate. Still paper.

### `c9689f5d` — sealed. Do not reseal.

Treat `c9689f5d` as a **sealed paper-book stamp**. Coder may *read* it. Coder may *cite* it. Coder must **not** reseal, rewrite, or rotate that stamp to make a journal look newer.

### `fib-paper` — book (recipe), not a live grid

Fibonacci is a **paper recipe in a new spot workspace** `fib-paper`. Never `init`/`reset` `dca-paper` to start it. No extra pairs beyond the EUR allowlist. No extra clips. Status: book only until Coder actually runs a recipe **without** touching DCA.

### `grid-paper` — book (recipe), not a live bot

Grids are a **paper recipe in a new spot workspace** `grid-paper`. Same rules: do not mix with the DCA stack, do not go live, EUR allowlist only, no memecoin grid, no Phantom bot “grid.”

### 3x futures sleeve — FAIL (separate)

Separate futures paper, leverage cap **3x**. Kill switch already specified. **Result: FAIL.** Record it. Do not reopen at 5x “to recover.” Do not send that PnL into spot journals. **Not the fund gate.**

---

## EUR pairs allowlist only

**New Coder paper (invert, fib, grid, any clip after this page) quotes EUR only.** Belgian SEPA later is EUR. Do not open USD/USDT/USDC-quoted books for new work. `dca-paper` BTCUSD is **grandfathered HOLD** — leave it; do not add a sixth USD slice.

**Allow (spot EUR, established — not a meme list):**

`BTCEUR` / `XBTEUR`, `ETHEUR`, `LTCEUR`, `BCHEUR`, `XRPEUR`, `ADTEUR`, `DOTEUR`, `SOLEUR`, `LINKEUR`, `ATOMEUR`, `XLMEUR`, `AVAXEUR`, `XMREUR` (if the pair exists on Kraken at the time of the paper order).

**Refuse:**

- Memecoins and joke tickers (DOGE, SHIB, PEPE, BONK, WIF, FLOKI, and anything listed as a meme or a brand-new micro).
- Forex (`EURUSD` etc.), tokenized stocks, earn/staking as a “strategy.”
- Perps / live futures except the already-FAILED 3x sleeve which stays closed.
- Extra pairs “for diversification” while invert-paper still has **1 fill**. That is WAIT.

If a pair is not on the allowlist, **do not paper it**. Ask the CEO; do not improvise.

---

## Ten ways paper is not proof

Paper is a rehearsal against a live *ticker*. It is **not** a live fill, not a tax event, and not a fund memo. Coder must say this on every journal, including the VOORBEELD pages.

1. **Instant full fills.** The local paper engine fills the whole size at the quoted price. Live books partial-fill, queue, or reject.
2. **Slippage is zero in the current books.** `dca-paper` slippage = 0. Invert prints at 1.24496 as if size did not move the book. Live market orders walk.
3. **Fee model is Starter taker 0.26% only.** Live makers can be 0.16%; live takers can be worse after volume/spread. Paper does not prove your fee tier.
4. **No matching-engine latency.** A paper TP at 1.26778 does not compete with other sellers. Live LIMIT 00030 can sit while price tags the level and leaves.
5. **One fill is a story, not a sample.** Gate is **≥ 8 fills**. `invert-paper` has **1**. `dca-paper` has **5**. Neither is proof.
6. **No SEPA / KYC / weekend / halt friction.** Live capital has to exist, settle, and survive a halt. Paper 10k USD is a number in a JSON file.
7. **No API 429s, key scopes, or dead-man `cancel-after`.** Those only appear when you are live. They change fills.
8. **Mark-to-market ≠ realized after fees.** `dca-paper` equity 9995.71 includes a mark. Gate 1 is **return > 0 after fees**, not “BTC ticked up.”
9. **Sleeve FAIL is a different movie.** Mixing 3x futures PnL into spot to “show a win” is journal fraud. FAIL stays on the sleeve.
10. **Paper is not a Belgian tax fact and not a live ledger.** Phantom sales-USDC is beroepsinkomen. Kraken live (later) is a separate trade file. The accountant picks cost basis. Do not invent FIFO. Do not export a paper JSON as a CAP / Vak XIII annex.

When in doubt: **paper is not proof.**

---

## STARTABLE (do these; still paper)

Coder may start these **without** live keys, **without** Phantom, **without** resetting DCA, **without** resealing `c9689f5d`.

### 1. Fee shadow

Keep a shadow column next to every `PAPER-*` fill:

| Column | Rule |
| --- | --- |
| Engine fee | 0.26% taker already deducted by `kraken paper` |
| Shadow extra | Conservative unmodeled cost (spread + slippage). Do not set this to 0 because the engine did. |
| Round-trip | A buy fill plus a TP sell is two fee events. 00030 @ 1.26778 is **not** profit until it fills **and** both fees are subtracted. |

Gate 1 uses **shadowed** return, not vanity mark.

### 2. Honest journal (VOORBEELD)

- Stamp **VOORBEELD**. Document type journaal/checklist. Never FACTUUR / INVOICE. Sell copy would be **OFFERTE**.
- Print the ugly parts: 1 fill, open 00028, resting 00030, DCA −4.29, 3x sleeve FAIL, fills < 8.
- Do not reset `dca-paper` to get a prettier equity.
- Do not reseal `c9689f5d`.
- Do not mix sleeve PnL into spot.
- Identity stays: natural person, Geel, KBO/BTW **nog niet toegekend**.
- Existing VOORBEELD page (other PR): `dca-paper-journal/` — Coder may improve **that journal copy** only. Not shop HTML. Not catalog cards. Not leftover 9 USDC restacks.

### 3. Fill ping

When a paper order **prints**, ping the journal the same day (same sitting if Coder is in the loop):

- id (`PAPER-00029` …)
- pair (must be allowlisted EUR for new books)
- side, type, price, fee, shadow fee
- running fill count / 8
- running maxDD vs 8%
- return-after-fees vs 0

Ping **00030** only when it fills, not when it is placed. Ping **00028** when it fills or is cancelled (cancelled is not a fill). Do not add extra clips because the ping feels slow.

---

## WAIT (do not start)

| Item | Why it waits |
| --- | --- |
| **Live** | CEO must say live **and** the fund gate is green. No API keys in this repo. No `kraken order` / `kraken futures order`. No Withdraw Funds permission ever on an agent key. |
| **Extra pairs** | Invert still has 1 fill. Adding SOLEUR+ETHEUR+… to “get to 8 fills faster” is cheating the gate. Allowlist is a fence, not a shopping list. |
| **Extra clips** | Do not add a 6th DCA slice. Do not pyramid invert. Do not start fib/grid clips until the CEO names that book **and** the allowlist holds. |

SEPA 200–3000 EUR of the operator’s own bank is an **operator** later step, not a Coder action. 10k is a paper starting number, not a deposit instruction.

Live keys **later**, never pasted into a journal page, never in git.

---

## Never

Hard bans for this seat (repeat them on every Coder run):

1. **Never a Phantom bot.** No Phantom MCP trading, no memecoin sniper, no SOL/USDC spend from treasury, no “just a small live test” from `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3` or Base `0x9eb954b567ef3616424a6e1bf42c63724930aa54`.
2. **Never memecoins.** Not on paper, not on live, not “as a 0.01 clip.”
3. **Never apply the operator as a developer.** The Geel human does not code. Do not submit Wellfound/Contra/Twago/Freelancer seats in their name. Scout/Builder already have that rule; Coder does not get a workaround.
4. **Never reset `dca-paper`.** Fib → `fib-paper`. Grid → `grid-paper`. Invert stays `invert-paper`.
5. **Never reseal `c9689f5d`.**
6. **Never go live from this page.** Still paper.
7. **Never API keys** in HTML, markdown, screenshots, or chat logs.
8. **Never Capital.com**, never perps above the dead 3x sleeve, never sales-USDC to Kraken.
9. **Never leftover 9 USDC HTML restacks** or shop/catalog rewrites on a Coder ticket.
10. **Never title a journal FACTUUR or INVOICE.**

---

## Gate scoreboard (2026-08-27) — still paper

| Book | Fills | Return > 0 after fees (shadow) | maxDD ≤ 8% | Gate |
| --- | --- | --- | --- | --- |
| `dca-paper` | 5 | No (equity 9995.71, fees already bit) | Yes on this tiny mark | **FAIL** (fills + return) |
| `invert-paper` | **1** (00029); 00030 TP; 00028 open | Unknown until round-trip prints | Not enough sample | **FAIL** (fills) |
| 3x sleeve | n/a | FAIL book | Kill at 10% sleeve DD | **FAIL** — **not the fund gate** |
| `fib-paper` / `grid-paper` | Recipe only | — | — | Not in gate |

**Promotion: no.** Stay on STARTABLE (fee shadow, honest journal, fill ping). Wait on live, extra pairs, extra clips.

---

## Tax split (reminder, not advice)

- Phantom sales-USDC = **beroepsinkomen**.
- Kraken (when live, later) = **apart handelsdossier**.
- Paper = **geen belastingfeit**.
- Not a lawyer. Not live-handelsadvies. Accountant picks cost basis.

---

## Operator checklist (paper until CEO)

- [ ] Paper until the CEO says live. No live keys on Coder pages.
- [ ] Operator opens their **own** Kraken account (Coder does not).
- [ ] SEPA later: 200–3000 EUR from the operator’s bank. 10k is not a deposit.
- [ ] No Phantom USDC/SOL and no sales-USDC to Kraken.
- [ ] No extra pairs, no extra clips, no memecoins, no Phantom bot.
- [ ] Do not reset `dca-paper`. Do not reseal `c9689f5d`.
- [ ] Do not mix 3x sleeve FAIL into spot journals.
- [ ] Fill ping 00029 / 00030 / 00028 as they print. Count fills honestly toward 8.
- [ ] Fee shadow on every print. Gate = return>0 after fees **and** ≥8 fills **and** maxDD≤8%.
- [ ] Do not apply the operator as a developer.

VOORBEELD · Coder seat · still paper · 2026-08-27.
