# REVIEWER — CEO RESEARCH stage RGY

Seat: **REVIEWER**. Stage: **CEO RESEARCH only**. Date: **2026-08-27**.

Score **starts at 0**. This file does not reuse PR [#142](https://github.com/eyeskull2220/solana-invoice/pull/142) notes as the score. Live hosts, chain, Linear, GitHub, leftover `main`, and Phantom were probed again this run. Plan, design, and code were **not** reviewed. No mail was sent. No spend. No Phantom send. No Kraken live. No fake KBO.

Judged artifact: `docs/rgy-2026-08-27/ceo/01-adv-research.md` on PR #142 (`cursor/ceo-adv-research-e41b`).

Success tests for this pack (only): **money in operator accounts** **and** **a shop a secretaris forwards**. The machine is **one Belgian income machine**. This leftover `solana-invoice` checkout is **not** the shop.

**GREEN only if no RED and no YELLOW remain.** They remain. **Stage: not GREEN.**

| item | RED/YELLOW/GREEN | note | fix-if-not-green |
| --- | --- | --- | --- |
| leftover repo is not the shop | GREEN (finding closed) | This `main` (`2170952`) is English `Solana Invoice — 9 USDC`. Unlock **downloads on RPC failure** (`honorUnlock` in `index.html` catch). `catalog.html` title `Treasury tools`; README lists 9/49 USDC toys. Live shop is [sovereignforge.surge.sh](https://sovereignforge.surge.sh/) (title `SovereignForge — voorstel voor het bestuur`). Live [solana-invoice-treasury.surge.sh](https://solana-invoice-treasury.surge.sh/) title is already `Eén klus — €49 · OFFERTE`. Live [treasury-tools.surge.sh](https://treasury-tools.surge.sh/) schema.org `numberOfItems: 11`, not the README four-toy list. Artifact named the trap correctly. | — |
| one Belgian income machine | GREEN (finding closed) | GitHub this owner: three repos — public leftover `solana-invoice`; private `SovereignForgeV1` (~646 MB); private `SovereignForgeGrokbot` (`desktop trading app`). Linear [SovereignForge](https://linear.app/sovereignforge) users: **Sasha De Vree** (only human, admin), Cursor OAuth app, Linear bot. Issue bodies still name Manager/Working seats with no users. Artifact correctly kills leftover PRs, Linear costume, and Bybit/Grokbot as the shop. | — |
| money in | RED | Shop pay address `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3` (printed on [betalen.html](https://sovereignforge.surge.sh/betalen.html) and on the Golfbreker kit). This run, public Solana RPC: `getSignaturesForAddress` → `[]`; `getBalance` → **0** lamports; `getTokenAccountsByOwner` USDC mint `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v` → `[]`. No inbound. Success test 1 fails. | A real USDC credit on the **published** receive address (or the shop print updated to an operator-held receive address). Do not invent a balance. |
| forwardable page | RED | Live H1 is the right buyer: “Voor de secretaris die vanavond nog een voorstel naar het bestuur stuurt.” That is not enough. (1) Maatstaf [club-site-kit-treasury.surge.sh](https://club-site-kit-treasury.surge.sh/) title `ZWV De Golfbreker — zwemclub in Geel (demo)`; banner **geen echte club of vzw**; `info@golfbreker.example`; pay box **900 USDC** on the club home. (2) Checkout is USDC-only — “Geen kaart, geen IBAN, geen andere keten.” Every SKU `geen BTW-factuur (OFFERTE)`. Footer **KBO/BTW: nog niet toegekend**; **geen Peppol Access Point**. (3) [robots.txt](https://sovereignforge.surge.sh/robots.txt) `User-agent: *` / `Disallow: /`. (4) `/club.html` **404**. (5) No screenshot/thread of a real secretaris forward. A URL that exists is not a page a bestuur can execute. Artifact scored the page cell YELLOW; this review does not. Success test 2 fails. | Named **VOORBEELD** a secretaris can send without learning the club is fake; offer a bestuur can actually pay; evidence of a real forward. Do not count `robots` Disallow + fake maatstaf as forwardable. |
| Sell (lane) | RED | [pakketten.html](https://sovereignforge.surge.sh/pakketten.html): **11** live kits, USDC charge, euro as omrekening (`1 USDC ≈ €0,86`; Kraken public `USDCEUR` last **0.8586** this run, in-range, not FOD). Featured club kit 900 USDC · ±€774. Peppol Client-Chase 399 USDC and Peppol Ready 249 USDC while seller is not an Access Point and cannot FACTUUR. SKU count is a catalog, not a machine. | First inbound **or** a documented secretaris forward of the **live** host. Do not add SKUs. Do not merge leftover-HTML PRs and call that a deploy. |
| Paper (lane) | RED | Invert gate in the artifact is clear: return > 0 after fees ∧ ≥ 8 fills ∧ maxDD ≤ 8% on invert-paper. This leftover `main` has **no** invert-paper journal. Kraken MCP tool discovery **failed** this run (same class as the artifact). Did not live-trade. Bybit `SovereignForgeV1` / Grokbot are the wrong venue: [SOV-55](https://linear.app/sovereignforge/issue/SOV-55/g32-belgian-tax-classification-memo-accountant-sig) **Canceled**; [SOV-63](https://linear.app/sovereignforge/issue/SOV-63/g40-walk-5-pre-live-gates-with-dollar300) **Canceled**; [SOV-78](https://linear.app/sovereignforge/issue/SOV-78/grokbot-soft-launch-sl-efg-flip-rehearsal-dollar100-dollar300-micro) **Backlog**. Paper cannot satisfy money-in until a later operator GNG. | Three printed invert-paper numbers from Kraken **paper**. Do not soften the gate. Do not promote V1/Grokbot into this lane. |
| Rails (lane) | RED | Honest identity is not a pay rail. Live privacy: natuurlijke persoon, Geel, **geen ondernemingsnummer**. Contact: Gmail only, `KBO/BTW: nog niet toegekend`. Phantom `wallet_status` **timed out** this run — printed address still **unmatched** to an operator wallet. Empty unused key may be a generated treasury string. No IBAN/Bancontact. Belgian tax memo SOV-55 canceled. | Phantom **read** showing the shop print equals a receive-only address the operator holds (still no send). Real KBO is operator-only. Until then keep OFFERTE, not FACTUUR. |
| Capabilities | YELLOW | HTTP + chain probes worked (enough to score Sell). Linear + GitHub readable. Phantom timed out. Kraken MCP down. Gmail exists and **must not send**. Cursor agents can write; they are still pointed at leftover HTML (this public repo is the only easy PR surface). Capability without aim is a cost, not a lane. | Phantom read works; Kraken paper CLI works; stop opening shop PRs against leftover `index.html`. Still no mail/spend/send. |
| team layout | RED | **BAD**, not “needs a shuffle.” Headcount 1. “Release Manager / Orchestrator / QA / OFG Core” are labels on Sasha. 100+ Ultra PRs into leftover HTML are a collision, not a team. One operator cannot staff that chart and also sell. | Collapse to operator + four lanes. Agents may write. They are not seats. |
| hard locks this turn | GREEN (locks only) | Held here: operator ≠ freelancer; no fake KBO written; Phantom receive-only (timeout, no send); no Kraken live; **no mail**; no spend. Locks held is not income. | — |

**GREEN count: 3 / 11** (leftover-vs-shop identification, one-machine identification, locks). Remaining: **6 RED + 1 YELLOW**. Stage not closed.

## Design-out (every RED and YELLOW)

Until the matching row is GREEN, design **must not**:

1. **Treat this leftover repo as the shop.** Out: rewriting `index.html` / `catalog.html` / README 9/49 USDC toys as SovereignForge; honor-unlock-on-RPC-fail as a paywall; claiming a merge to `solana-invoice` deployed [sovereignforge.surge.sh](https://sovereignforge.surge.sh/). Live host ≠ this git tree.
2. **Treat Linear Manager/Working names, Ultra seat factory, or V1/Grokbot as the income machine.** Out: staffing a Release Manager; counting SOV-71…78 peels as Sell; Bybit OFG-DCA as Paper; a seventh Reviewer/Planner/Web/Design factory.
3. **Count SKU count, Peppol kits, or dual-invoice as progress.** Out: Peppol Client-Chase / Peppol Ready on a seller who is not an Access Point and cannot FACTUUR. Out: 11 cards with 0 inbound.
4. **Fake Golfbreker / “demo” as the maatstaf a secretaris forwards.** Out: `geen echte vzw`, `info@golfbreker.example`, pay-900-USDC on the club home as the board pack. Public stamp is **VOORBEELD**, not “demo.”
5. **USDC-only checkout as board-executable.** Out: telling a vzw treasurer to send ~€774 of crypto to a nameless empty key. Out: inventing IBAN/Bancontact/kaart this turn (spend/rails). Out: inventing a BE0… KBO to “look serious.”
6. **`robots.txt` Disallow as a discoverable shop.** Forwarding is the only distribution; nothing forwarded has paid.
7. **Empty pay address as a proven Phantom receive rail.** Out: designing as if `96BT6…` is known-held. Match is unproven (Phantom timed out again).
8. **Paper theater.** Out: live Kraken; softening invert gate; mixing sleeve FAIL / `dca-paper` / Bybit into invert-paper; calling “no journal on main” a pass.
9. **Mail, spend, Phantom transfer, freelancer enroll** — locks; still designed out.

GREEN findings design must still honour: leftover HTML is residue; live shop is the Surge host; operator is not the freelancer; OFFERTE / `KBO/BTW: nog niet toegekend`; no Peppol Access Point; no mail from this seat.

## Live cites (this run)

| Probe | Result |
| --- | --- |
| https://sovereignforge.surge.sh/ | H1 secretaris/bestuur; Dutch catalog; USDC on face; KBO not assigned |
| https://sovereignforge.surge.sh/pakketten.html | 11 kits, euro omrekening, OFFERTE |
| https://sovereignforge.surge.sh/betalen.html | USDC-only; address `96BT6…`; no kaart/IBAN |
| https://sovereignforge.surge.sh/contact.html | Gmail only; `KBO/BTW: nog niet toegekend` |
| https://sovereignforge.surge.sh/privacy.html | natuurlijke persoon, geen vennootschap, geen ondernemingsnummer |
| https://sovereignforge.surge.sh/robots.txt | `Disallow: /` |
| https://sovereignforge.surge.sh/club.html | **404** |
| https://club-site-kit-treasury.surge.sh/ | Golfbreker **demo**, verzonnen zwemclub, 900 USDC pay on home |
| https://solana-invoice-treasury.surge.sh/ | `Eén klus — €49 · OFFERTE` (not this git tree) |
| https://treasury-tools.surge.sh/ | 11-item catalog |
| Solana RPC `96BT6…` | 0 signatures, 0 SOL, 0 USDC ATA |
| Kraken public `USDCEUR` | last 0.8586 |
| Linear users | 1 human (Sasha), Cursor OAuth, Linear bot |
| SOV-55 / 63 / 78 | canceled / canceled / backlog |
| GitHub | 3 repos as above |
| Phantom MCP | `wallet_status` timeout; no send |
| Kraken MCP | discovery failed; no live |
| Gmail | not called |
| This leftover `main` | English 9 USDC invoice; `honorUnlock` on RPC fail |

## Verdict

CEO RESEARCH is **not GREEN**. Identification of the leftover-repo trap and of the fake team is closed. Both success tests fail: **0 money in**, **no board-forwardable shop**. Sell, Paper, Rails, and team layout stay **RED**. Capabilities stay **YELLOW**. Locks held is not a machine.

No implementation in this PR. No mail. Do not review plan, design, or code from this file.
