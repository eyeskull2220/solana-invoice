# Active Passive income |CEO|

**Seat:** CEO (dispatch only)  
**Operator:** Eyeskull2220, Geel (Flemish Region). **Not the freelancer.**  
**Date of this page:** 2026-08-27  
**Repo:** `eyeskull2220/solana-invoice` (`main` at write time: treasury HTML catalog only)  
**This file is research + plan.** It does not send mail. It does not edit kit HTML. It does not invent a KBO, a BTW number, or a Peppol ID.

The CEO seat exists because the last 48 hours of cloud-agent work produced **kits, sweeps, and ideas** without a page that says what may start, what is blocked, and what must wait. This is that page.

---

## 0. Who sits where

| Role | Is | Is not |
| --- | --- | --- |
| **Operator (Eyeskull2220, Geel)** | Capital, yes/no, keys-last, forwards logo / IBAN / KBO **after** a real loket issues one | Coder, host, on-call debugger, day-rate Angular seat, named freelancer on the public face |
| **CEO seat (this page)** | Dispatch, stop, invert-gate, 7-day board | A sender identity, a shop, a FACTUUR |
| **Teammates** | Builder / Scout / Coder / Wallet / Compliance **deliver** | Allowed to mail, mint KBO, or go live on Kraken |
| **Public face** | EUR, Dutch, OFFERTE / VOORBEELD, Belgian club & KMO language | USDC, Solana, Phantom, “crypto tools”, “I am a freelance developer” |

If a prompt would put Eyeskull2220 on a job board, a day-rate seat, or a “hire me” mail, **stop**. The operator is not the freelancer. The team is.

---

## 1. Hard locks (do not bargain)

These override every teammate page, every kit PR, and every “just this once.”

| Lock | Meaning | Failure mode already seen |
| --- | --- | --- |
| **No fake KBO** | No `BE0…`, no 10-digit ondernemingsnummer, no `0208:` Peppol ID until an *erkend ondernemingsloket* issues a real one. Stamp **KBO/BTW: nog niet toegekend**. | Peppol/invoice kits shipped invented identifiers; later PRs had to strip them. |
| **OFFERTE only** | Public commercial paper is an offer / VOORBEELD. Never FACTUUR / INVOICE until KBO + VAT identification exist. | Dual-invoice desk and pipeline kits needed “stamp OFFERTE / not FACTUUR” rescue PRs. |
| **Phantom receive-only** | Read balances, receive into the published treasury address. No send, swap, rebalance, perps, new key, third address. | Wallet-ideas already had to ban SIWE, CDP wallets, Helio email-embedded wallets, Solana puller keys. |
| **Kraken paper until invert gate** | Spot paper only. Invert to live **only if all three** are true on the **same** paper book: **return > 0 after fees**, **≥ 8 fills**, **max drawdown ≤ 8%**. Human yes still required. | `dca-paper` journal exists as VOORBEELD. Kraken MCP for this run is **error / undiscoverable**. Do not reset `dca-paper`. |
| **EUR-first public face** | Mails, shop face, OFFERTE, and demo pages speak **EUR**. No USDC, no Solana, no “crypto” in those surfaces. Settlement may still land as USDC **internally**; that is Wallet’s rail, not the shop. | Live `catalog.html` / README / Surge still bill **9 / 49 USDC**. That is a shop-face violation until hide-the-coin lands. |
| **No new connectors without a yes** | Use what is already bound. Do not enroll X pay-per-use, a new Peppol Access Point, Stripe, Circle custody, Helio as default, or any extra MCP. | Scout/Wallet research already hit X `user-not-enrolled` and correctly **did not enroll**. Keep that. |

**Treasury receive (Wallet, not shop copy):** Solana USDC `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3`, mint `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v`. Do not print this on mails or the EUR shop face.

---

## 2. Inventory — what CEO can dispatch

Dispatch means: **open or resume a cloud agent / teammate / routine with a written page**, then stop if the page is missing. CEO does not implement kits in this seat.

### 2.1 Cloud agents (Cursor Cloud, this environment)

Observed on 2026-08-27 against `github.com/eyeskull2220/solana-invoice`. CEO may **read, resume, or spawn the same seat types**. CEO may **not** spawn a nameless sweep fleet.

| Seat type | What it is allowed to produce | What it is not |
| --- | --- | --- |
| **CEO** (this run) | This page, STARTABLE/BLOCKED/WAIT, 7-day board, stop-list | Mail, kit HTML, live trade |
| **Builder** | Week-scale EUR offers (club site, inbox ops, Peppol go-live, lead-to-invoice, retainer). EUR shop / hide-the-coin / seizoenskaart / named-club **demo** as VOORBEELD | 9–49 USDC leftover HTML; FACTUUR; fake KBO |
| **Scout** | Public buyer **categories** + public `info@` / `bestuur@` / `secretariaat@` lists. RFP refresh (e.g. Freelancer.be 12294 if still Open) | Send mail; named-person inboxes; operator as applicant; HN/IH reopen; X enroll |
| **Coder** | Paper suite, invert-gate counters, VOORBEELD journal (no `dca-paper` reset). Fibonacci → `fib-paper`. Grids → `grid-paper` | Live Kraken; mixing leverage PnL into DCA journal |
| **Wallet** | Receive-only audit, EUR receive-log **operator pack**, freeze the two known receive strings, refuse third addresses | Send, swap, rebalance, perps, new keys, SIWE, crypto on shop face |
| **Compliance** | Belgian bijberoep/hoofdberoep plan, Peppol-as-user not Access Point, USDC booked in **EUR on receipt** after KBO | Invented KBO; “already compliant”; tax advice as a ruling |
| **Reviewer** | Shop rubric: EUR-first, OFFERTE stamp, no crypto in face, no fake KBO | Merge one-kit unlocks |
| **Planner** | 7-day board (Sell / Paper / Rails / Capabilities) aligned to **this** page | A second source of truth that contradicts hard locks |
| **Web (buyers / outreach law)** | Mailto **rows for a human**. Outreach **law** (what may be said in EUR, OFFERTE only) | **Send.** This CEO page forbids mail. Sibling send is a miss (see §3.6). |
| **Design** | EUR-first shop copy and layout spec | Shipping USDC prices on the public face |

**Concurrent Ultra wave (2026-08-27, do not wait, do not duplicate):** Compliance BE plan, Wallet treasury ops, Coder paper suite, Scout capabilities, Builder capabilities, web Belgian buyers, web outreach law, reviewer shop rubric, builder seizoenskaart, builder named-club demo, builder hide-the-coin, design EUR-first shop, planner 7-day board. If those PRs conflict with this page, **this page wins on locks**. Merge order: Compliance + this CEO page before any kit HTML.

**Already-idle research CEO may cite (not re-fan-out):**

| Page (open PR / branch) | Use |
| --- | --- |
| `docs/ideas-builder-ultra.md` (#81) | Five week-scale offers (club / inbox / Peppol / pipeline / retainer). Reprice to **EUR** on the public face. |
| `docs/ideas-scout-ultra.md` (#83) | Buyer categories + public mailboxes. Only priced open public-email RFP in that window: Dolfijnen Middelkerke. |
| `docs/ideas-wallet-ultra.md` (#82) | Rails, receive-only, no new keys. Dual-chain / x402 / Peppol annex stay **behind** the shop face. |
| `docs/compliance-be-sidegig.md` (#92) | Track A default (bijberoep) while employee hours hold. Open work list. Not a certificate. |
| `dca-paper-journal/` (#110) | VOORBEELD paper checklist. Do not reset `dca-paper`. |
| Geel clubs / BE club buyers / UNIZO inbox / Peppol chase buyer PRs | Lists for Scout. **Not** a send queue. |

**Live `main` (not dispatch, just facts):** `index.html`, `catalog.html`, `solana-invoice.html`, `config.js`, README. Four Surge tools at 9 / 49 USDC. That catalog is **not** the EUR public face.

### 2.2 Teammates (named seats)

| Teammate | CEO dispatches when | Done looks like |
| --- | --- | --- |
| **Builder** | A page exists for **one** week-scale EUR offer, not a 9 USDC toy | Live Dutch deliverable on the **client** stack (mailbox, Teamleader/Billit, club CMS). Operator only yes/no + forwards. |
| **Scout** | Buyer refresh is on the 7-day board | Category + public mailbox table. Zero sends. Zero invented customers. |
| **Coder** | Paper / invert-gate work is on the board | Journal stamp, fill count, fee-adjusted return, maxDD. No live orders. |
| **Wallet** | Rail work is on the board | Receive-only confirmation. EUR receive log for the operator. Crypto strings absent from shop/mail. |
| **Compliance** | Before any FACTUUR-shaped artefact or KBO-shaped field | Plan stays open until loket + fund + e604. Kits stay OFFERTE / VOORBEELD. |

Linear workspace in this principal is **SovereignForge / Grokbot** (Sasha De Vree). That project is **out of this income seat**. Do not file Active Passive work there. Do not mix Grokbot soak / MICRO / ARM language into Belgian OFFERTE work.

### 2.3 Routines

Checked 2026-08-27:

- Cursor Cloud **automations** source: **0** agents.
- This run’s event **subscriptions**: **none**.
- No automation UUID was supplied to this seat.

Until the operator says yes to a named routine, CEO treats “routines” as **proposed**, not live:

| Proposed routine | Cadence | Page required first | Stop if |
| --- | --- | --- | --- |
| Paper journal stamp | Daily | `dca-paper-journal` VOORBEELD | Anyone resets `dca-paper` or places live |
| Invert-gate read | After every paper session / weekly | Coder paper suite page | Kraken MCP still error **and** someone “just lives it” |
| Scout public-RFP refresh | Weekly | Scout capabilities page | Mail, or a 20-agent sweep fan-out |
| EUR-face lint | On every shop PR | Reviewer shop rubric | USDC/crypto strings on public face |
| Connector freeze | On every new MCP / enroll prompt | This CEO page | Enroll without operator **yes** |

Do not turn these on as nameless automations. A routine without a page is fan-out.

### 2.4 Connectors already bound (no adds)

| Bound | Use for this seat | Do not |
| --- | --- | --- |
| GitHub | PRs, pages, branches | Merge kit HTML from this CEO run |
| Linear | Read only if needed | File income work on Grokbot |
| Gmail | **Do not send.** Drafts only if a later page + operator yes | Fan-out to club `info@` |
| Phantom MCP | Receive-only / balances | `wallet_rebalance`, send, perps |
| Kraken | Paper, when the MCP is healthy | Live; this run’s Kraken namespace was **error** |
| Playwright | Verify EUR shop **after** a Builder/Design PR | “Verify” by mailing |
| Cursor Cloud | List / resume seats | Spawn 50 sweep agents |
| X / eToro docs / Stripe / Circle / Vercel / Cloudflare / Hugging Face / Context7 / Shadcn / Snyk / Link / Phantom Connect | Default **idle** for this income week | New enroll, new seller account, new Access Point |

**No new connectors without a yes.** That includes X pay-per-use, a certified Peppol AP contract, Helio/MoonPay as default land path, Circle custody, Stripe USDC, and any second GitHub identity posting duplicate grant PRs as if they were this operator.

---

## 3. Fifteen adversarial misses

These are ways this seat already failed or will fail if CEO dispatches without this page. Each miss is a **stop**, not a “note”.

1. **Fan-out without a page.** 26–27 Aug produced dozens of `sweep-*` PRs (Gitcoin, OnlyDust, Wellfound, Twago, Lemmy, Farcaster, TAAFT, …) whose honest verdict was **ZERO**. That is not Scout. That is unpaged fan-out. Stop spawning sweep agents unless this board has a named Scout cell.

2. **Small-scope kit factory.** `split-bill`, `km-log`, `btw-invoice`, `retainer-invoice`, `dagtarief-offerte`, FAQ/UTM/waitlist/paywall stubs at 9–49 USDC. Builder ultra already said these are toys next to Belgian club/Peppol work. CEO does not unlock another one.

3. **One-kit unlocks.** Club-site 900, inbox-ops 299, pipeline 399, Peppol ready 249, Peppol chase 399, review retainer 199 — each as its own SKU/PR — fragments the week into merge lottery. One offer on the board, or none.

4. **Fake KBO / placeholder BTW / invented Peppol `0208:`.** Compliance plan forbids it. Rescue PRs (#97, #102, #106 class) exist because kits shipped identity. Any field that looks like an ondernemingsnummer without a loket receipt is a halt.

5. **FACTUUR before KBO.** Belgian B2B invoicing is illegal-shaped without registration + (for in-scope B2B) Peppol. Until then: **OFFERTE / VOORBEELD** only. “Invoice desk” in the catalog sense is a shop word, not a legal invoice.

6. **Mail from the connected mailbox.** This CEO run is **do not mail**. On 2026-08-27 a sibling web seat was already sending to club `info@` addresses from the bound Gmail (hundreds of sent threads in the prior 14 days, including a same-hour burst). That is fan-out **and** it burns the operator identity as if they were the freelancer. CEO does not continue it. Outreach law may exist; **send** waits for a human pick of **one** mailbox and **one** EUR OFFERTE.

7. **USDC / crypto on the public face.** Live catalog, README, and Surge pages lead with USDC on Solana. Hard lock is EUR-first. Until hide-the-coin + EUR shop land, treat `main` shop as **non-compliant face**. Do not put USDC in mails “to match the catalog.”

8. **Operator-as-freelancer.** Closed PRs (`INCOME-RESEARCH`, `BE-JOBS`, EU paid trials) and Konnekt/Kingfisher-class seats pitch Eyeskull2220 as labour. The operator is not the freelancer. Team delivers. Day-rate apply is a miss.

9. **Kraken live before invert gate — or live while MCP is dead.** Invert needs return > 0 after fees, ≥ 8 fills, maxDD ≤ 8%, then human yes. Kraken MCP was **undiscoverable/error** on this run. “We’ll just CLI it live” is a miss. Do not reset `dca-paper` to fake a clean book.

10. **Phantom send / new key / third address.** Rebalance, swap, SIWE admin, CDP `subscriptionOwner`, Helio email-embedded wallet, Solana subscription puller, DeskCrew board-ownership keys. Wallet ultra listed these. Receive-only means **receive-only**.

11. **New connector without yes.** X pay-per-use, extra bounty platforms, a self-hosted x402 facilitator (needs a gas key), a Peppol Access Point contract, Stripe/Circle KYB. Scout already refused X enroll. Keep refusing.

12. **Invented buyers / “already sold” logos.** Builder ideas correctly used **categories** (16k Flemish sportclubs, Peppol late slice). Scout named public mailboxes from Stad Geel / club pages — that is research. Committing a named club as a customer, or mailing every row, is a miss.

13. **Wallet string in Peppol PaymentMeans.** Peppol BIS does not take a Solana address as IBAN. Wallet ultra’s two-file design (UBL for the tax file, USDC annex off-Peppol) is the only honest split — and the annex is **not** shop face. Stuffing the treasury address into UBL is a miss.

14. **Crypto income booked as “not income.”** Compliance: USDC fees are *beroepsinkomen*, EUR on receipt, after KBO. Holding the token does not defer the fee. Mixing a personal Phantom with professional receipts without a dedicated receive address is a bookkeeping miss **after** registration — not a reason to invoice today.

15. **Foreign project bleed + fork noise.** SovereignForge Grokbot Linear (MICRO, soak, ARM) is not this seat. Duplicate grant/RFP PRs from a fork account are not operator dispatch. CEO ignores both.

---

## 4. STARTABLE / BLOCKED / WAIT

### STARTABLE (this week, with a page)

| Item | Who | Note |
| --- | --- | --- |
| This CEO page + stop-list | CEO | This PR. |
| EUR-first shop **spec** (copy, rubric, hide-the-coin) | Design / Reviewer / Builder | Spec only until operator yes on HTML. |
| VOORBEELD paper journal + invert-gate counters | Coder | No `dca-paper` reset. New books: `fib-paper`, `grid-paper`. |
| OFFERTE / VOORBEELD templates **without** KBO fields filled | Builder / Compliance | Stamp *nog niet toegekend*. |
| Scout refresh of **public** RFPs and category lists | Scout | No send. Re-check Dolfijnen Middelkerke 12294 if still Open. |
| Receive-only Wallet audit (read balances, no send) | Wallet | If Phantom MCP times out, report WAIT, do not send “to test.” |
| Compliance plan stays open; loket conversation is operator | Compliance | Plan is not a filing. |
| One named-club **demo** as VOORBEELD | Builder | Demo file, not a mailed claim that the club bought. |

### BLOCKED

| Item | Until |
| --- | --- |
| Fake KBO / BTW / Peppol ID | Never. Real loket or nothing. |
| FACTUUR / INVOICE as legal invoice | KBO + VAT ID + (B2B) Peppol-capable software as **user** |
| Mail send / Gmail fan-out | Human picks **one** mailbox + **one** EUR OFFERTE **and** CEO says send |
| USDC / Solana / “crypto” in mails or shop face | Hide-the-coin + EUR face merged |
| Phantom send, swap, rebalance, perps, new key | Operator yes **and** a Wallet page that is not this lock |
| Kraken live / any invert | Gate numbers on one paper book **and** human yes **and** healthy Kraken connector |
| New MCP / X enroll / new AP / Stripe / Circle / Helio-default | Operator **yes** in writing |
| Another 9–49 USDC HTML toy | Never on this board |
| Operator apply as freelancer | Never on this board |
| Kit HTML edited by **this** CEO run | Out of scope (user lock) |
| Merge of an isolated kit SKU as “the product” | Board names **one** offer |

### WAIT

| Item | Waiting on |
| --- | --- |
| Invert gate | ≥ 8 fills, return > 0 after fees, maxDD ≤ 8% on the paper book; Kraken MCP repaired |
| First real OFFERTE send | Operator yes + one mailbox + EUR copy with no crypto |
| KBO / e604 / fund affiliation | Operator at Liantis (Geel, Diestseweg 63) or another of the eight loketten; **Track A default** while employee hours hold |
| Accountant engagement | Compliance §8 triggers (crypto settlement already is one) — operator, not an agent filing |
| Named Cursor automations | Operator yes + a page per routine |
| EUR shop HTML on `main` | Design/Builder PR that passes Reviewer rubric **and** operator yes |
| Peppol send of a real B2B invoice | KBO + VAT + end-user software + a real Belgian VAT customer |
| Live catalog as public face | It is currently USDC-first; treat as **internal treasury**, not the Belgian shop |

---

## 5. Seven-day board — Sell / Paper / Rails / Capabilities

Window: **Thu 27 Aug 2026 → Wed 2 Sep 2026**. One cell per lane per day. If a cell needs a teammate, CEO dispatches **that** teammate with a pointer to this page. No fourth lane (“sweeps”).

| Day | Sell | Paper | Rails | Capabilities |
| --- | --- | --- | --- | --- |
| **D0 Thu 27** | Freeze send. This page is the sell law: EUR OFFERTE, operator is not the freelancer. | Do not reset `dca-paper`. Read #110 VOORBEELD. | Phantom receive-only. No rebalance. Kraken = paper or idle. | Inventory seats. Stop unpaged Ultra fan-out. |
| **D1 Fri 28** | Scout: one-page EUR OFFERTE skeleton (club site **or** inbox ops — not both). No mail. | Coder: invert-gate fields on the journal (fills, fee-adjusted return, maxDD). | Wallet: confirm receive address unchanged; do not print it on the OFFERTE. | Design: EUR shop copy. Reviewer: rubric (no crypto strings). |
| **D2 Sat 29** | Scout: refresh public RFP 12294 + Geel gids categories. Mailto **table** only. | Coder: one paper session into `dca-paper` if MCP is healthy; else document BLOCKED connector. | Wallet: EUR receive-log as **operator pack**, not a shop card. | Builder: hide-the-coin spec (catalog USDC → internal). |
| **D3 Sun 30** | Builder: named-club **demo** VOORBEELD (seizoenskaart-class). Not sent. | Coder: fill count check. If < 8, gate stays WAIT. | Rails idle unless a receive happened — then evidence pack shape (Compliance), still no FACTUUR. | Compliance: keep open-work list; no numbers invented. |
| **D4 Mon 31** | Human (operator) picks **at most one** mailbox. Agent does **not** send. | Paper continues. New strategy → new book, never reset. | Wallet: refuse any PR that adds a third address or SIWE. | Builder: lock **one** week-scale EUR offer from ideas-builder (club **or** Peppol go-live **or** inbox — one). |
| **D5 Tue 1 Sep** | If operator said yes on D4: CEO may dispatch **one** send of **one** EUR OFFERTE. Else Sell stays WAIT. | Invert-gate read. Live still BLOCKED. | Same receive-only. | Reviewer: any shop PR fails if USDC/crypto visible. |
| **D6 Wed 2 Sep** | Close the week: either 0 or 1 OFFERTE in flight. No blast. | Week paper summary. Invert only if **all three** numbers + human yes. | No new connector. | Capabilities shipped = **pages + one demo**, not ten kits merged. |

**Lane rules**

- **Sell** never contains USDC, Solana, Phantom, or “crypto.” Price in EUR. Stamp OFFERTE.
- **Paper** never contains live orders, leverage mixed into DCA, or a reset of `dca-paper`.
- **Rails** never contains send. Settlement copy stays off the shop face.
- **Capabilities** never contains a 9 USDC toy or a one-kit unlock.

---

## 6. Stop-list (CEO says no)

### No small-scope

- No 9 / 49 USDC leftover HTML (invoice toys, km-log, split-bill, FAQ, UTM, waitlist, paywall stub, ICS, webhook tester, status stub, …).
- No “tinytools / directory / bounty sweep” whose expected output is ZERO.
- No day-rate seat, no operator-as-applicant, no HN/IH reopen.

### No one-kit unlocks

- Do not merge club-site / Peppol / inbox / pipeline / retainer as unrelated SKUs “so something ships.”
- Do not treat a single HTML file as a Belgian go-live.
- Do not unlock FACTUUR, KBO, or Peppol send by shipping a kit that *looks* complete.

### No fan-out without a page

- No second Ultra wave until this page names the seat.
- No Gmail blast, no “all Geel `info@`,” no 50-agent sweep.
- No new connector, no X enroll, no automation UUID without a routine row above.
- No Linear Grokbot tickets for this income work.
- If a teammate has no page, **do not start them**.

---

## 7. Invert gate (Coder + CEO, not Wallet)

Paper → live is **closed** unless every line is true on the **same** Kraken paper book:

1. **Return > 0 after fees** (paper already applies a taker-fee model; do not ignore it).
2. **≥ 8 fills** (not 8 orders sitting, 8 fills).
3. **Max drawdown ≤ 8%**.
4. Kraken connector healthy (this run: **not**).
5. Operator **yes**.
6. First live size is a fraction of paper (Kraken paper-to-live skill: 10–25%), autonomy supervised — and that is a **later** page, not this week’s default.

Until then: stamp VOORBEELD, keep `dca-paper`, do not mix futures/leverage into that journal.

---

## 8. Belgian rails (Compliance summary for dispatch)

Full plan: `docs/compliance-be-sidegig.md` on `cursor/compliance-be-sidegig-f998` (#92). CEO only needs:

- **Not registered.** Do not say otherwise.
- **Track A (bijberoep)** default while the employee job stays ≥ half-time and ≥ 235 h/quarter.
- KBO only via an *erkend ondernemingsloket* (Acerta, Eunomia, Group S, Liantis, Partena, Securex, UCM, Xerius). Liantis has a Geel office. Fee snapshot 2026: **€111.50** per establishment unit. **Do not invent the number.**
- VAT: identification still required; €25,000 vrijstellingsregeling is a **choice**, not a reason to skip Peppol **receive** capability after registration.
- Operator is **not** a Peppol Access Point.
- This CEO page does not file, affiliate, or e604.

---

## 9. What this run did / did not do

| Did | Did not |
| --- | --- |
| Wrote this page | Mail |
| Listed dispatchables from live Cloud + open PRs | Edit kit HTML / `catalog.html` / Surge |
| Named 15 misses from the actual PR flood | Enroll X or any new connector |
| Set a 7-day Sell/Paper/Rails/Capabilities board | Place Kraken live or Phantom send |
| Locked OFFERTE / no fake KBO / EUR-first | Fill a KBO or FACTUUR |

---

## 10. Sources (opened or listed this research)

- Repo `main`: README, `catalog.html`, `config.js` (USDC-first live face).
- Open PRs / branches cited in §2.1 (ideas-builder #81, ideas-scout #83, ideas-wallet #82, compliance #92, paper journal #110, OFFERTE-stamp kits #97/#102/#106).
- Cursor Cloud agent list (Ultra seats 2026-08-27; 0 automations-source agents).
- Kraken plugin skills: `kraken-paper-to-live`, `kraken-autonomy-levels`, `kraken-paper-strategy` (paper fees, no silent live).
- This run: Kraken MCP namespace **error**; Phantom balance call **timeout**; Gmail search showed send activity from a sibling seat — cited as miss §3.6, **not** continued.
- Compliance / FPS / RSVZ / e-invoice.belgium.be URLs live inside #92 — do not duplicate a fake ID from them.

**PII:** No personal mailbox, phone, or home street is copied here. Treasury addresses stay in §1 for Wallet, not for shop/mail.

---

End of CEO page. Next dispatch is a teammate **with a pointer to this file**, or nothing.
