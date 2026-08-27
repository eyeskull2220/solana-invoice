# VOORBEELD — `invert-paper` journal (still paper)

Stamp: **VOORBEELD**. **Niet te koop / not for sale.** Not a FACTUUR. Not an INVOICE. No API keys.

Operator: natural person, Geel. **KBO/BTW: nog niet toegekend.**

HTML: [`../invert-paper-journal/index.html`](../invert-paper-journal/index.html)

## Named book: `invert-paper`

| Id | State | Detail |
| --- | --- | --- |
| **PAPER-00029** | **FILL 1** | buy **XRPEUR** @ **1.24496** |
| **PAPER-00030** | Resting TP | sell **LIMIT** @ **1.26778** (not a fill until it prints) |
| **PAPER-00028** | **Still open** | @ **1.23084** (not a fill) |

**fills = 1.** Resting TP and the open 00028 do not count.

## Gate — NOT MET

All three must hold. None of these is optional:

1. **≥ 8 fills** (closed or fully filled prints with a `PAPER-*****` id). Have **1**. Resting limits are not fills.
2. **return > 0 after fees** (Starter 0.26% taker already in the paper engine; round-trip needs the sell to print).
3. **maxDD ≤ 8%** from peak equity on this book.

**Gate: NOT MET.** Stay paper. Do not “almost.” Do not add extra clips to rush 8 fills.

## Sleeve FAIL is not the gate

The moderate-leverage futures paper (cap 3x) is a **separate** book. Its **FAIL** does not greenlight live and does not replace the spot gate. Never mix sleeve PnL into `invert-paper` or `dca-paper` journals.

## Leave these alone

- **`dca-paper`** — HOLD. Do not reset. Fibonacci → `fib-paper`. Grids → `grid-paper`.
- **`c9689f5d`** — sealed paper-book stamp. Cite it. Do **not** reseal.
- **Still paper.** Do not go live. No keys in this repo or on the journal page.
