# SovereignForge board — 27 Aug–2 Sep 2026 PT

Companion: `docs/ultra-2026-08-27/PLAN.md`. Seats execute from those two files; no chat history required.

**Window:** Thursday 27 Aug 2026 00:00 PT → Wednesday 2 Sep 2026 23:59 PT.

**Entity:** SovereignForge (Geel). Public face is Dutch OFFERTE, EUR-first. Operator is not the freelancer. Phantom is receive-only internally. Kraken is paper until invert gate.

**Hard locks (any NOW item that breaks one is a fail):** no fake KBO; OFFERTE/VOORBEELD never FACTUUR; no leftover 9 USDC HTML on the shop; do not rewrite kit HTML; no new connectors; no live Stripe; `robots.txt` must `Allow: /`.

**Public shop host:** `https://treasury-tools.surge.sh/` (verified 200). Do not invent `*-treasury.surge.sh` names. Kit URL table lives in PLAN.md.

Legend: **NOW** = this window. **NEXT** = after NOW gates, still in or immediately after this window. **WAIT** = blocked on a person, a legal number, or invert gate.

| | NOW | NEXT | WAIT |
| --- | --- | --- | --- |
| **Sell** | Align repo + live shop to Dutch EUR OFFERTE (prices already on the live catalog: €900 clubsite, €199 menu, €199 sponsor, €349 lid, €249 vakman, €299 inbox-ops, €399 pipeline, €399 Peppol chase, €490 dual-invoice, €249 Peppol Ready, €49 één klus). Copy: “Betaalgegevens na akkoord.” Unlink every public CTA whose host or page shows USDC/Solana/Phantom/crypto/wallet, including `solana-invoice-treasury.surge.sh` (hostname leak). Strip personal Gmail from the shop (live leak today on pipeline + één-klus hosts — unlink, do not rewrite kit HTML). Do not mail Geel clubs this week. Do not apply the operator as a developer. | After shop PASS (PLAN Task 6): EUR wrapper pages (new files only) for clubsite / inbox-ops / Peppol packs so the catalog can href without landing on USDC copy. Re-check the eight researched `info@` candidates (Aqua Ski, Defence Lab, Geelse Zaalvoetbal, Holvensche Hondenschool, Harmonie De Eendracht, Goju-Ryu Geel-Ten Aard, TC Netevallei, ’t Geels Bieke) against modern-site + later-list rules before any send. Named-club work stays the fake Golfbreker demo unless a club asked in writing. | Real KBO/BTW (ondernemingsloket). Legal FACTUUR / Peppol send. Live Stripe Checkout. Helio/x402/Request Network seller doors. Mailing later-list clubs (ASV Geel, Valberta, Den Bruul, BBC Geel, ’t StAt, zwemclubkst) or any modern-site `info@`. Freelancer.be / Twago / PPH bids in the operator’s name. Publishing IBAN or a wallet on the shop. |
| **Paper** | Kraken **paper only**. Keep `dca-paper` (do not reset). Operator journal is VOORBEELD (PR #110, not a shop card, host `dca-paper-journal-treasury.surge.sh` is 404 — do not invent it). Paper is not a tax event. Snapshot language from 26 Aug stays: paper mode, do not treat fills as income. | Optional paper recipes in **new** workspaces only: `fib-paper`, `grid-paper`. Futures paper sleeve cap **3x** with kill switch; do not mix that PnL into the DCA journal. If Kraken MCP is down, write “disconnected — no fills invented” and stop. | **Invert gate (closed).** No live Kraken orders, no Withdraw Funds keys, no selling the `dca-paper` stack. Gate opens only when a dated `docs/` file contains the exact phrase `INVERT GATE ACK`, a paper snapshot date, and a first live pair/size, signed by the operator. Until then Paper/WAIT owns live trading. |
| **Rails** | Phantom **receive-only**, internal. Addresses (do not print on the public face): Solana `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3` / mint `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v`; Base `0x9eb954b567ef3616424a6e1bf42c63724930aa54`. No wallet-connect, no SIWE, no Phantom SDK, no send, no perps, no third address. Public pay line is euro + “na akkoord.” Existing Stripe link `https://buy.stripe.com/test_dRmdR9gFd1Yt05D7E95os00` is sandbox; **default this week: remove it from the shop.** `robots.txt` on the shop: `User-agent: *` / `Allow: /` (live kits currently `Disallow: /` — fail for the shop). | EUR receive-log pack (PR #91, columns `date,usdc,eur_mid,memo,tx,notes`) as **operator-only** HTML/CSV. Operator enters `eur_mid`; do not fetch or bake a rate. Not a tax filing. Do not Surge it as a catalog card. Dual-invoice desk stays an internal OFFERTE (490) — not a public crypto page. | Live Stripe. New connectors (x402, Dexter facilitator, Helio subscriptions, Request Network, CDP wallets, Google APIs). New receive addresses or keys. Solana Pay URLs on the public face. IBAN. Peppol Access Point contract. Circle/Coinbase Business KYB. |
| **Capabilities** | Planner: PLAN.md + this board. Design: Dutch paper/OFFERTE visual, no coin chrome. Builder: replace leftover `index.html`/`catalog.html`/`README.md`; add Allow `robots.txt`; do **not** rewrite `solana-invoice.html` or kit HTML. Web: outreach law + Gmail strip; research-only Geel list. Reviewer: PLAN Task 6 rubric (leftover HTML, rail words, robots Allow, pending KBO, no FACTUUR stamp, no live Stripe, no kit diffs). | Builder hide-the-coin wrappers (new files). Design seizoenskaart / menukaart only if they are EUR OFFERTE packs, not a 9 USDC restack, and not a rewrite of an existing kit. Web: citation log for buyers; still no send unless Sell/NOW is updated. Reviewer re-runs Task 6 after wrappers. | Compliance track A/B (bijberoep vs hoofdberoep) until a real KBO exists (`docs/compliance-be-sidegig.md` is a plan, not a claim). Wallet ultra ideas (x402 door, DeskCrew-class MCP, pull retainers, Peppol+USDC annex) stay ideas. Leftover 9 USDC toy catalog (`csv-cleaner`, `form-to-email`, `rss-to-webhook`, `tip-jar`, …) stays off the public shop. |

## Seat checklist (same window)

- [ ] **planner** — PLAN.md + BOARD.md frozen; invert gate closed; kit URLs only from the verified table
- [ ] **web** — no personal Gmail on shop files; no outbound mail; Geel `info@` rules held
- [ ] **design** — EUR/Dutch OFFERTE surface; fake Golfbreker only; no wallet QR
- [ ] **builder** — leftover USDC homepage gone; robots Allow; kits not rewritten; leaking hosts unlinked
- [ ] **reviewer** — Task 6 PASS on the builder branch and on `https://treasury-tools.surge.sh/` after deploy

## Done when

1. `docs/ultra-2026-08-27/PLAN.md` and this board exist.
2. A later agent can ship the shop from those files without chat history.
3. Kit HTML was not rewritten.
4. Public face is Dutch, EUR, OFFERTE, pending KBO, robots Allow, no USDC/Solana/Phantom/crypto/wallet, no live Stripe, no leftover 9 USDC toys.
