# Solana request sweep: invoice / USDC freelance billing tools

**Sweep date:** 2026-08-26 (UTC)  
**Product under test:** [Solana Invoice](https://solana-invoice-treasury.surge.sh/) — one HTML file, amount + QR + copy-address, offline, no account, **9 USDC**.  
**Pay-to (USDC on Solana only):** `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3`  
**USDC mint:** `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v`

This is a **read-only** inventory of public request threads. Nothing was posted, emailed, listed, or applied.

## Hard constraints (followed)

| Constraint | What happened |
|---|---|
| No X | X/Twitter was not queried, not opened, not cited. |
| No Solana Forum post | Forum used **read-only** (Discourse JSON). No login, no topic, no reply. `can_create_topic` was `false` on search responses. |
| Skip Superteam | Superteam Discord, Earn, and Grant listings were not searched and are not in this file. |
| No session | No Discord login, no Forum account, no wallet connect. |
| Pay-to | Only the treasury address above is printed. Third-party wallets from threads were not copied. |

## What counts as a hit

A **request thread** is someone asking for a way to bill, invoice, or collect USDC/SOL as a merchant, freelancer, or simple site — not a SIMD about inflation, not a protocol spec unless it names a merchant/payment use case.

Closest product shape: a static page a client can pay without creating an account (QR / copy-address / Solana Pay transfer request).

## Verdict

There is **no Forum topic whose title or body is “I need a freelance USDC invoice tool.”** The Forum is almost entirely sRFCs and governance. Demand for this product shows up as **Stack Exchange how-do-I-get-paid / how-do-I-show-a-QR** questions, plus one Forum merchant-QR request that explicitly wants the flow **off X**.

Public Discord **message archives are not readable without a session**. Invite metadata is public; history is not. That gap is recorded, not filled with invented quotes.

---

## 1. Solana Developer Forum (read-only)

**Host:** `https://forum.solana.com`  
**API:** `GET /search.json?q=…` (unauthenticated)

### Search log (2026-08-26)

| Query | Topics | Notes |
|---|---:|---|
| `invoice` | 0 | Empty. |
| `invoicing` | 0 | Empty. |
| `freelancer` | 0 | Empty. |
| `freelance` | 0 | Empty. |
| `get paid` | 0 | Empty. |
| `escrow freelance` | 0 | Empty. |
| `stablecoin payment` | 0 | Empty. |
| `merchant` | 1 | Topic 2539 (below). |
| `USDC payment` | 1 | Same topic 2539. |
| `receive USDC` | 2 | 2539 + a staking-rewards SIMD (not billing). |
| `payment request` | 3 | 2539, sRFC 25, sRFC 34. |
| `QR code payment` | 3 | Same three. |
| `Solana Pay` | 23 | Mix of sRFCs; payment-relevant subset listed. |
| `billing` | 5 | False positives (inflation “billing” / validator economics). Not invoicing. |

### Included (payment / merchant request)

#### 1.1 Merchant QR blinks off X — **closest Forum request**

- **URL:** https://forum.solana.com/t/directly-supporting-blinks-in-wallets-aside-from-external-sites-x/2539
- **Posted:** 2024-11-30 · **Views (at fetch):** 152 · **Likes:** 3 · **Replies:** 0
- **Handle:** `@silostack`
- **Ask:** Wallets should run the same blink UX when **scanning a QR**, not only when the URL sits on a website or on X. Stated use case: **merchant displays a blink as a QR**; customer’s mobile wallet GETs payment options (USDC / USDT / …), user picks, signs.
- **Why it matters:** The product is exactly “show a QR, client pays USDC, no social post.” This thread is a wallet-capability request, not a request for a $9 HTML file, but it is the only Forum hit that names **merchant + QR + USDC** as the job to be done.
- **Fit:** Partial. Solana Invoice already emits a Solana Pay transfer-request QR (fixed mint, fixed amount). It does not implement blink option-picking. It does not need X.

#### 1.2 sRFC 25 — Solana Actions (QR / iOS payment breakage)

- **URL:** https://forum.solana.com/t/srfc-25-solana-actions-v1/1719
- **Posted:** 2024-06-25 · **Views:** 206 · **Likes:** 3
- **Handle:** `@jnwng`
- **Ask / spec:** Actions v1 is Solana Pay **transaction request** with `solana-action:` because `solana:` QR scans on iOS open the wrong app. Spec exists because **payment QR** was an observed failure case.
- **Fit:** Background. Confirms QR payment is a real surface. Not a freelancer invoice request.

#### 1.3 sRFC 27 — Blinks (pay from a URL, no wallet-aware site)

- **URL:** https://forum.solana.com/t/srfc-27-blockchain-links-blinks/1721
- **Posted:** 2024-06-25 · **Views:** 410 · **Likes:** 7
- **Handle:** `@jnwng`
- **Ask / spec:** Any page that can show a URL should be able to start a Solana tx. Motivation includes e-commerce without the site being a dApp.
- **Fit:** Background. Matches “static HTML + pay link” better than a hosted dashboard.

#### 1.4 sRFC 34 — Relayer so payers can send SPL without holding SOL

- **URL:** https://forum.solana.com/t/srfc-34-standardized-relayer-api/2876
- **Posted:** 2025-01-07 · **Views:** 970 · **Likes:** 5
- **Handle:** `@ilan_g`
- **Ask / spec:** Standard relayer API. First named use case: **Payments: transferring tokens without needing SOL.**
- **Fit:** Adjacent. Clients paying a USDC invoice often have USDC and no SOL. The HTML invoice cannot sponsor gas; this is a wallet/relayer gap, not a missing invoice generator.

### Excluded (searched, not billing tools)

- SIMD-0550 / SIMD-0411 / SIMD-0228 and other inflation threads that matched `billing`.
- sRFC 28 blinks chaining (UX for multi-step actions; not invoicing).
- sRFC 11 on-chain data storage (matched `Solana Pay` via incidental text).
- Validator / Alpenglow / scheduler papers.

**Forum conclusion:** Zero threads ask for a freelance invoicing product. One thread asks wallets to support **merchant QR USDC payment off X**. Specs (Actions, Blinks, Relayer) assume merchants will collect SPL/USDC via QR or URL.

---

## 2. Stack Exchange

**Sites:** `solana.stackexchange.com` (API `site=solana`), plus `stackoverflow.com` for the same keywords.  
**API:** Stack Exchange 2.3, 2026-08-26. `solana-pay` tag: **47 questions** total.

`q=invoice` on Solana SE returned **one** hit (HTML pay button). `q=freelancer` returned **zero**. `intitle=invoice` returned unrelated noise (the word does not appear in those titles; treated as a miss).

### Strongest product matches

#### 2.1 HTML page + Phantom “pay” (unanswered) — **closest to this repo**

- **URL:** https://solana.stackexchange.com/questions/18810/need-help-sending-coin-to-wallet-via-html-website-using-phantom-wallet
- **Asked:** 2025-01-06 · **Score:** 1 · **Views:** 161 · **Answers:** 0
- **Handle:** Santiago (unregistered)
- **Ask:** Single HTML file, CDN web3.js, connect Phantom, **pay / send an SPL token to another wallet from the website**. Author says they searched everywhere and still cannot get a working pay function (devnet custom token).
- **Fit:** High. Same shape as Solana Invoice (one HTML file, no Node app). Gap: they need a working transfer; the live tool is a **receive invoice** (QR + copy-address), not a send SDK. Still the clearest “I want this in HTML” request.

#### 2.2 “We want to accept Solana as a payment” on a simple site

- **URL:** https://solana.stackexchange.com/questions/16266/solana-pay-on-wordpress-or-react
- **Asked:** 2024-08-28 · **Score:** 1 · **Views:** 62 · **Answers:** 1
- **Handle:** Anthony
- **Ask:** Building a simple WordPress + React site. Does Solana Pay work there? **We want to accept Solana as a payment.**
- **Fit:** High intent, low technical bar. A static invoice HTML is a valid answer when they do not need WooCommerce cart state.

#### 2.3 Customer-POV / non-DeFi checkout example

- **URL:** https://solana.stackexchange.com/questions/7494/solana-pay-examples-required-from-customer-pov
- **Asked:** 2023-09-03 · **Score:** 1 · **Views:** 96 · **Answers:** 1
- **Handle:** marvincharmin
- **Ask:** Wants to **test Solana Pay from the customer side**. Looked at Shopify, found nothing useful. Asks for a **non-DeFi** example.
- **Fit:** High. This is “show me a normal bill I can pay,” which is what the invoice page is.

#### 2.4 Merchant accepting a token (not only SOL)

- **URL:** https://solana.stackexchange.com/questions/3279/how-to-accept-spl-tokens-as-merchant-with-solana-pay
- **Asked:** 2022-09-22 · **Score:** 1 · **Views:** 350 · **Answers:** 1
- **Handle:** user14262770
- **Ask:** Jr. dev, merchant idea: accept an SPL token **other than SOL & USDC** via the Solana Pay storefront example; local POS demo broke when they changed the token.
- **Fit:** Medium. Confirms merchants start from the POS sample and get stuck. This product is **USDC-only**, which is the default they were departing from.

#### 2.5 Non-dev: “do I have to create a USDC account to receive USDC?”

- **URL:** https://solana.stackexchange.com/questions/7535/do-i-have-to-explicitly-create-a-usdc-account-to-be-able-to-receive-usdc-coins
- **Asked:** 2023-09-10 · **Score:** 1 · **Views:** 1416 · **Answers:** 3
- **Handle:** Camila326
- **Ask:** Has SOL + USDT, **no USDC**, sent test USDC, nothing arrived. Asks if they must generate a USDC address, and whether Solana has an official web tool to do that from the main address.
- **Fit:** Medium. Receive-side confusion is what a copy-address + QR invoice is supposed to remove. Highest view count in this sweep.

#### 2.6 Non-dev author: printed QR cards for merchant payments (2026)

- **URL:** https://solana.stackexchange.com/questions/24466/can-a-solana-pay-transfer-request-invoke-a-custom-anchor-program
- **Asked:** 2026-07-27 · **Score:** 1 · **Views:** 21 · **Answers:** 0
- **Handle:** Val Archer
- **Ask:** Author (not a dev) writing a handbook for non-tech entrepreneurs. Merchants **display printed QR cards**. Transfer-request URI for a static amount + memo. Wants to know whether a transfer request can hit a custom program, or whether they must run an HTTPS transaction-request server. Trying to **avoid requiring merchants to host a server**.
- **Fit:** High for the “static QR, no server” constraint. Loyalty-token architecture is out of scope for Solana Invoice; the **no-server QR** requirement is in scope.

#### 2.7 Ecommerce QR checkout: mark order paid

- **URL:** https://stackoverflow.com/questions/72285268/solana-identify-account-transactions
- **Asked:** 2022-05-18 · **Score:** 0 · **Views:** 657 · **Answers:** 1
- **Ask:** Ecommerce site, cart → checkout → **QR to pay**. How to know the checkout is paid (Solana Pay `reference`?).
- **Fit:** Medium. Same QR surface; they need confirmation, which the offline invoice does not do (honor-system / explorer).

### Additional Solana Pay requests (weaker / builder-SDK)

These are tagged `solana-pay` and are **implementation stuck**, not “please sell me an invoice HTML.” Listed so the tag sweep is not silently incomplete.

| Date | Q | Ask (short) | URL |
|---|---|---|---|
| 2022-08-01 | 1310 | Ecommerce demo; Phantom **exits** on Solana Pay QR (USDC endpoint) | https://solana.stackexchange.com/questions/1310 |
| 2022-08-19 | 2278 | Phantom iOS cannot simulate Solana Pay QR | https://solana.stackexchange.com/questions/2278 |
| 2022-12-27 | 5006 | Phantom cannot identify token on Solana Pay QR | https://solana.stackexchange.com/questions/5006 |
| 2023-01-31 | 5567 | Solana Pay with **PHP/Laravel**, prefer **no plugin** | https://solana.stackexchange.com/questions/5567 |
| 2024-01-25 | 9720 | Payment **description / comment** on a transfer | https://solana.stackexchange.com/questions/9720 |
| 2024-08-14 | 15978 | Solana Pay deeplink/QR via a **Telegram bot** | https://solana.stackexchange.com/questions/15978 |
| 2024-08-17 | 16054 | `createQR` from `@solana/pay` | https://solana.stackexchange.com/questions/16054 |
| 2025-09-08 | 23345 | QR pay SOL; Solflare “Request Failed” | https://solana.stackexchange.com/questions/23345 |
| 2026-06-13 | 24408 | Consumer-facing **payment app** validation before mainnet | https://solana.stackexchange.com/questions/24408 |
| 2022-08-22 | SO 73445944 | Phantom + Solana Pay in **plain HTML `<script>`**, no Node (`Buffer is not defined`) | https://stackoverflow.com/questions/73445944 |
| 2022-03-05 | SO 71363136 | Vue app wants Solana Pay as **payment processor**; SDK install failed | https://stackoverflow.com/questions/71363136 |

Q16054 and similar posts contain third-party pubkeys in sample code. Those keys are **not copied here**.

### Stack Exchange conclusion

People are not filing tickets titled “freelance USDC invoice.” They are filing:

1. **HTML / WordPress / no-Node** pay buttons (18810, 16266, SO 73445944).
2. **Customer-POV / printed QR / no server** (7494, 24466).
3. **How do I receive USDC at all** (7535).
4. SDK/QR breakage in Phantom/Solflare (many `solana-pay` tagged Qs).

That is the demand this 9 USDC HTML file is built for. Unanswered 18810 is the open hole.

---

## 3. Discord — public archives only

**Guilds probed without login (2026-08-26):**

| Invite | Guild | Guild id | Channel on invite | Approx members | Presence |
|---|---|---|---|---:|---:|
| https://discord.com/invite/solana | Solana Tech | `428295358100013066` | `#guidelines` (`517161607248347156`) | 149000 | 5916 |
| https://discord.com/invite/solanamobile | Solana Mobile Community | `988649555283308564` | (invite landing only) | (invite JSON, not counted here) | — |

**What is public without a session**

- Invite JSON (`/api/v10/invites/solana?with_counts=true`) — metadata only.
- Official public article pointing people at that Discord for Solana Pay support: https://solana.com/news/solana-pay-transaction-requests-bring-on-chain-interactivity-to-the-off-chain-world (“join the Solana Tech Support Discord”).
- Forum SIMD-0228 notes “rough consensus achieved on Discord” — governance, not invoicing.

**What is not public**

- `GET /api/guilds/<id>/widget.json` for Solana Tech and Solana Mobile → **403**.
- `discord.com/channels/…` message URLs → login wall.
- No GitHub-hosted Solana Tech message dump matching invoice / freelancer / USDC billing was found in this sweep.
- Superteam Discord was **not** opened.

**Request threads found in Discord archives:** **none.** Channel history is not a public archive. This file does not quote Discord users.

**Not counted as request threads (products, not asks):** Discord invoicing bots (e.g. Cordvo) and escrow bots exist as marketing sites. They are supply, not a Forum/SE/Discord-archive request, so they are out of this inventory.

---

## 4. Product fit (Solana Invoice vs what people asked)

| Asked for | In this sweep | 9 USDC HTML invoice |
|---|---|---|
| One HTML file, Phantom, send/receive SPL | SE 18810, SO 73445944 | Receive side: yes (QR + copy-address). Send SDK: no. |
| Accept payment on a simple site / WordPress | SE 16266 | Yes, if they host/send the HTML. |
| Non-DeFi customer-POV pay demo | SE 7494 | Yes. |
| Printed QR, no merchant server | SE 24466, Forum 2539 | Transfer-request QR: yes. Blink multi-token picker: no. Custom program: no. |
| USDC receive without understanding ATAs | SE 7535 | Copy-address + Circle mint on the page. |
| Freelance invoice / escrow / milestones | Forum: 0. SE `freelancer`: 0 | Out of scope (no escrow). |
| Pay USDC when payer has no SOL | Forum sRFC 34 | Out of scope (relayer). |

**Do not reply on Forum.** If a reply is wanted later, the honest one-liner for 2539 / 16266 / 7494 / 18810 is: static Solana Pay transfer request, USDC mint `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v`, pay-to `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3` is the **treasury** address for buying the HTML file, not a sample merchant wallet. Merchants paste **their** receive address into the tool.

---

## 5. PII scan

Scanned this file before commit.

| Class | Result |
|---|---|
| Email addresses | None. |
| Phone numbers | None. |
| Government IDs | None. |
| Third-party Solana addresses | Not copied. SE 16054 / 5006 / 6067 / 8421 sample keys left on the source pages. |
| Treasury pay-to | Present once as allowed: `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3`. |
| Circle USDC mint | Present as a public mint id, not a person. |
| Real names | Forum/SE display names reduced to **public handles** where a legal name appeared in Discourse JSON (`@jnwng`, `@silostack`, `@ilan_g`). SE display names that are already handles kept as on-site attribution. |
| Discord usernames / user ids | None (no message archive access). |
| Superteam | Not present. |
| X handles / tweet URLs | None. |

Quotes are paraphrased or shortened so sample code (and any keys inside it) is not reproduced.

---

## 6. What this sweep did not do

- Did not post on Forum, Discord, SE, or X.
- Did not join Solana Tech or Solana Mobile.
- Did not search Superteam.
- Did not search Reddit, HN, or Telegram (out of requested sources).
- Did not invent listings or quote Discord DMs.

---

## Source timestamps (all 2026-08-26 UTC)

- `https://forum.solana.com/search.json?q=invoice` → 0 posts.
- `https://forum.solana.com/t/2539.json`, `/t/1719.json`, `/t/1721.json`, `/t/2876.json`.
- Stack Exchange API `site=solana` `tagged=solana-pay` (47 items); `q=invoice` (1 item); `q=freelancer` (0).
- Stack Overflow API questions 72285268, 72635319, 71363136, 73445944.
- `https://discord.com/api/v10/invites/solana?with_counts=true`.
- `https://solana.com/news/solana-pay-transaction-requests-bring-on-chain-interactivity-to-the-off-chain-world`.
