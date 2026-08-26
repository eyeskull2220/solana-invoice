# Wallet ultra ideas — payment / rail side

**Date:** 2026-08-26  
**Scope:** bigger automated-income offers from the *payment rail*, not trading.  
**Banned:** perps, Hyperliquid, new wallet keys, a third receive address, SIWE unless named as a blocker.

## Treasury (do not invent)

| Role | Address | Asset |
|---|---|---|
| Phantom Solana USDC receive | `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3` | native USDC mint `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v` |
| Base receive | `0x9eb954b567ef3616424a6e1bf42c63724930aa54` | native USDC `0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913` |

These two addresses are the only settlement destinations in this note. Do not generate a key, a PDA, a CDP smart wallet, an embedded Helio wallet, or any other receive address.

Existing catalog prices are 9 USDC (Solana Invoice) and 49 USDC (CSV / form / RSS). The five offers below sit at **490–1490 USDC** one-shot, plus (where noted) ongoing rail income after the buyer is live.

## Who does what

| Role | Job |
|---|---|
| **Wallet** | Pin the two addresses and the two USDC contracts. State the exact land path (SPL transfer vs EIP-3009 vs hosted pay-link). Refuse any flow that needs a new key, SIWE, or a third address. Name fees and KYC. Confirm Phantom can *see* the landed USDC on that chain. |
| **Builder** | Ship the HTML / server / middleware / UBL / QR. Never change receive addresses. Never add wallet-connect as a pay step unless Wallet marked it allowed. |
| **Scout** | Keep product pages, fee tables, and legal (Peppol / FPS Finance) current. Do not enroll X pay-per-use. |

## Research notes (2026-08-26)

Web pages used: [x402.org](https://x402.org/), [docs.x402.org sellers](https://docs.x402.org/getting-started/quickstart-for-sellers), [x402 networks](https://docs.x402.org/core-concepts/network-and-token-support), [x402 facilitators](https://docs.x402.org/dev-tools/facilitators), [Dexter facilitator](https://dexter.cash/facilitator) and [Dexter networks](https://docs.dexter.cash/docs/facilitator-and-chains/supported-networks/), [CDP x402 FAQ](https://docs.cdp.coinbase.com/x402/support/faq), [DeskCrew agents](https://deskcrew.io/agents), [Request Network](https://request.network/) + [chains](https://docs.request.network/resources/supported-chains-and-currencies) + [fees](https://docs.request.network/request-network-api/fees), [Request Finance pricing](https://www.request.finance/pricing), [MoonPay Commerce / Helio fees](https://docs.hel.io/docs/pricing-fees) + [subscriptions](https://docs.hel.io/docs/subscriptions) + [payout wallets](https://docs.hel.io/docs/for-creators), [Solana Subscriptions](https://solana.com/news/subscriptions-and-allowances) + [program](https://github.com/solana-foundation/subscriptions), [Base subscriptions](https://docs.base.org/base-account/guides/accept-recurring-payments), [Phantom Solana Pay](https://docs.phantom.com/recipes/payments/request-payment), [Peppol UNCL4461](https://docs.peppol.eu/poacc/billing/3.0/2025-Q4/codelist/UNCL4461/), Belgian mandate coverage (FPS Finance grace ended 1 Apr 2026), [Linux Foundation x402 Foundation 2 Apr 2026](https://www.linuxfoundation.org/press/linux-foundation-is-launching-the-x402-foundation-and-welcoming-the-contribution-of-the-x402-protocol).

**X:** `get_usage_credits` returned `user-not-enrolled` / Pay-per-use. Per instructions, **did not enroll**. Direct fetches of `x.com` search, Nitter, and FixTweet public pages returned 403/500. Indexed public coverage (Linux Foundation press, Coinbase x402 launch, CryptoBriefing volume piece citing Base-led x402 traffic) is used instead of live X posts.

---

## Idea 1 — Dual-chain USDC invoice desk

**Price:** 490 USDC (one HTML + print pack; ~50× the live 9 USDC Solana Invoice).

**What it is.** A B2B invoice the buyer fills once: amount, due date, memo. It emits (a) a Solana Pay `solana:` URL + QR to the Phantom Solana address, and (b) a Base USDC pay card (copy address + amount in 6-decimal atomic units) to the Base receive address. Same invoice number on both legs so the payer picks one chain. No Request Finance account. No Helio 2% cut. This is the catalog Solana Invoice, grown into a dual-rail desk for invoices that are actually large enough to matter (hundreds–thousands of USDC), not 9 USDC toys.

**How USDC actually lands.**

- **Solana path:** payer’s wallet (Phantom scan of Solana Pay) sends SPL USDC `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v` to `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3`. Phantom docs already describe this as `encodeURL({ recipient, amount, splToken })` then `findReference` / `validateTransfer`. Network fee is Solana compute, paid by the *payer*. Treasury does not sign.
- **Base path:** payer sends native USDC `0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913` to `0x9eb954b567ef3616424a6e1bf42c63724930aa54`. Direct ERC-20 `transfer`. Payer pays Base gas. Treasury does not sign.
- **Do not** route through Request Network for the Solana leg: Request Network payment destinations are **7 EVM chains + Tron only**. Solana is not a payee chain on that protocol. Request Finance *does* detect Solana payments, but that product is a KYB SaaS (from ~$50/month, KYB on Business Account).
- **Do not** use Helio/MoonPay Commerce as the default land path: 2% standard / 1% with HelioX NFT, even though payouts can be pointed at an existing Phantom / EVM wallet and they do not custody.

**Wallet vs Builder vs Scout**

- Wallet: freeze both receive strings in `config.js`; print the Solana mint and the Base USDC contract next to them; reject any “we’ll generate a per-invoice address.”
- Builder: one file, QR, copy buttons, PDF/print. Optional Solana Pay `reference` pubkey for matching — that reference is *not* a receive address.
- Scout: keep Helio 2% and Request Network “no Solana destination” as the reason this desk stays self-hosted.

**Blockers**

| Kind | Status |
|---|---|
| SIWE | None on the self-hosted path. **Blocked** if someone later “simplifies” via Request Network dashboard (EVM wallet sign-in) or MoonPay Commerce email/embedded-wallet signup. |
| KYC | None if payer sends on-chain to the two addresses. **Blocked:** Request Finance Business Account KYB; Coinbase Business (US+SG, custodial, no self-custody); Stripe USDC (1.5% + KYB). |
| Fees | Self-hosted: network gas only (payer). Helio 2%/1% if used as a hosted overlay. Request Network protocol 0.05% (capped ~$25) *and* Solana cannot be the payee. |
| New key | A unique Solana Pay `reference` is a throwaway pubkey for matching, not a treasury. Do not fund it. |

---

## Idea 2 — x402 seller door (Base + Solana)

**Price:** 990 USDC for a production seller pack (middleware + `/.well-known/x402` + dual `payTo`). After that, **automated income** is per successful call, in USDC, to the listed addresses.

**What it is.** An HTTP resource that answers unpaid calls with **402 Payment Required** and an `accepts[]` quote. Buyer (human or agent) signs USDC and retries. This is the rail Coinbase contributed to the Linux Foundation **x402 Foundation** (announced 2 Apr 2026; members include Circle, Solana Foundation, Stripe, Visa, Cloudflare). Solana Foundation has publicly claimed a large share of 2026 x402 volume; Base is the default EVM path (EIP-3009 `transferWithAuthorization` on USDC). Indexed coverage in Aug 2026 described millions of agent-initiated x402 transfers, Base-led.

Seller `payTo` on this pack is **only**:

- Base `eip155:8453` → `0x9eb954b567ef3616424a6e1bf42c63724930aa54`, asset `0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913`
- Solana `solana:5eykt4UsFv8P8NJdTREpY1vzqKqZKvdp` → `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3`, mint `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v`

**How USDC actually lands.**

1. Client hits the route with no payment → **402** + quote (`scheme: exact`, network, asset, `payTo`, `maxAmountRequired` in 6-decimal atomic USDC).
2. Client signs. On Base that is EIP-3009 (payer never sends a tx). On Solana that is `exact-svm`.
3. A **facilitator** broadcasts and settles. USDC is transferred *to `payTo`*, not to the facilitator.
4. Preferred facilitator for this treasury: **Dexter** `https://x402.dexter.cash` — public, **no account**, **no facilitator fee**, production Base + Solana, facilitator sponsors gas / Solana fee-payer. Minimum on Dexter Solana is **0.01 USDC**.
5. CDP Facilitator is optional later: it can use `payToConfig: address` so Coinbase does **not** provision a receive wallet (`CDP_WALLET_SECRET` skipped). It still wants a **CDP API key** (app credential, not a receive key) and runs OFAC/KYT on every tx. Not required if Dexter is used.

The seller server never holds a hot receive key. It only advertises the two listed addresses.

**Wallet vs Builder vs Scout**

- Wallet: hard-code `payTo` to the two treasury strings; refuse `createX402Server` default that mints a CDP EOA; refuse a self-hosted facilitator (that needs a **gas wallet key**).
- Builder: Express/Hono/Fastify `paymentMiddleware`, `/.well-known/x402`, HTTPS. Price the protected route high enough that Dexter’s 0.01 USDC floor is irrelevant (this pack is sold at 990; the live route can charge e.g. 1–25 USDC per call).
- Scout: watch Dexter `/supported` and x402.org facilitator table; do not treat `x402.org` facilitator as mainnet (testnet only).

**Blockers**

| Kind | Status |
|---|---|
| SIWE | Not part of x402. **Blocked** if Builder adds a “log in with Ethereum” admin. |
| KYC | Dexter: none. CDP facilitator: KYT/OFAC screening of *payer* addresses (seller is not KYB’d by that). |
| Fees | Dexter: 0% facilitator, sponsored gas. CDP: check current seller docs; screening can **decline** a payer. Self-hosted facilitator: **blocked** (new gas key). |
| New key | **Blocked:** CDP `eoa`/`smart` payTo, facilitator hot wallet, MCP *client* private keys (`EVM_PRIVATE_KEY` / `SVM_PRIVATE_KEY` in x402 MCP examples). Those keys are for *buyers*. This idea is sell-side only. |

---

## Idea 3 — DeskCrew-class agent door (micro rail, big kit)

**Price:** 790 USDC for the kit (MCP door + priced tools + Bazaar metadata). Ongoing income is **micro** (DeskCrew’s live catalog is **$0.02–$5.00** per call in USDC), which is the point of the rail — many small settlements to the same two addresses.

**What it is.** Copy the DeskCrew pattern, not DeskCrew’s product: one keyless MCP door, discovery free, writes return HTTP 402, USDC on Base (primary) and Solana. DeskCrew’s public door (`https://deskcrew.io/agents`, `/.well-known/x402`) is the class example: no account, no API key, gasless EIP-3009 on Base, `exact-svm` on Solana with the relayer as fee-payer, verify → run → settle (failed tools are not charged). Their `create_board` at **$5.00** is the top of that micro ladder.

We do **not** send our treasury USDC *to* DeskCrew. We sell a door whose `payTo` is **our** Base and Solana addresses. Commodity call to lead with: a high-value, stateless tool (invoice-from-text, Peppol-field check, CSV→UBL) priced **$1–$25** per call — still “micro” vs 490+ one-shots, big vs DeskCrew’s $0.05 drafts.

**How USDC actually lands.** Same x402 handshake as Idea 2. DeskCrew’s own 402 quote shape (from their docs):

- `scheme: "exact"`
- `network: "base"` / Solana entry in `accepts[]`
- `asset`: Base USDC `0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913`
- `payTo`: **must be** `0x9eb954b567ef3616424a6e1bf42c63724930aa54` (and the Solana treasury on the SVM accept), never a platform cold wallet
- `maxAmountRequired`: atomic 6-decimal USDC

Facilitator: Dexter (no account). Do not run DeskCrew’s self-hosted relayer (that is *their* ops, and it implies a broadcaster key).

**Wallet vs Builder vs Scout**

- Wallet: reject any `payTo` that is not the two treasuries; reject minting `mcp_` credentials as a paid path (DeskCrew’s free-account door is a different product and wants an account).
- Builder: MCP `tools/call` paywall, free `tools/list`, `/.well-known/x402`, Bazaar `declareDiscoveryExtension` so agents can find the door. No SIWE session.
- Scout: re-read `https://deskcrew.io/.well-known/x402` for live prices; do not scrape X for this.

**Blockers**

| Kind | Status |
|---|---|
| SIWE | None on the anonymous 402 door. **Blocked:** “free account + Bearer mcp_” as a required path. |
| KYC | None for anonymous pay-per-call. |
| Fees | Same as Idea 2 (Dexter 0%). If a call is priced below Dexter’s **0.01 USDC** Solana floor, Solana accept must be omitted or the price raised. DeskCrew’s $0.02 tools are above that floor. |
| New key | **Blocked:** throwaway `X402_KEY` as in `npx try-x402` (buyer-side demo). **Blocked:** board-ownership keys from DeskCrew `create_board` ($5) — that is a third address/key. We are not opening a DeskCrew board; we are selling our own door. |

---

## Idea 4 — Recurring USDC retainer (push, not pull)

**Price:** 490 USDC for the retainer checkout + reminder pack. The *income* after that is a published plan (example: **190 USDC / 30 days**) paid into the same two addresses.

**What it is.** Recurring USDC without a new merchant key. Three real rails were checked; only the **push** ones fit the no-new-key rule.

| Rail | Pull or push? | Lands on listed treasury? | Allowed? |
|---|---|---|---|
| **MoonPay Commerce (Helio) subscriptions** | Push. Email / `nextChargeUrl`; buyer taps wallet each cycle. Not an on-chain pull. | Yes, if payout wallet is set to the Phantom Solana and/or Base address in Settings → Wallets. Non-custodial, P2P. | Allowed as an *optional hosted overlay*, with fee haircut. |
| **Solana Subscriptions & Allowances** (`De1egAFMkMWZSN5rYXRj9CAdheBamobVNubTsi9avR44`, mainnet Jun 2026) | Pull. Merchant or a **whitelisted puller** signs `transferSubscription` each period. | Yes, destination can be the Solana treasury. | **Blocked for automation:** the puller is a signing key we do not have and must not invent. Human signing each pull in Phantom is allowed but is not automated income. |
| **Base Spend Permissions / Base Subscriptions** | Pull. `charge()` is Node-only and uses a **CDP smart wallet** as `subscriptionOwner`. `recipient` can be a different address. | Recipient *can* be the Base treasury. | **Blocked for automation:** CDP subscription-owner wallet is a new key. SIWE-class Base Account connect is also in this stack. |

Default build: **self-hosted push**. A dated Solana Pay + Base pay card (Idea 1) re-issued every period. Optional Helio Pay Link with `isSubscription: true` only if Wallet accepts the 1–2% fee and the dashboard login (email or wallet — email creates an **embedded wallet**, which is a third address; **do not use email signup**. Link the existing Phantom + Base addresses as payout wallets).

Helio renewal is still a buyer signature every cycle (`nextChargeUrl`). That is automated *reminders*, not silent pulls. Honest copy: “renew with one wallet tap,” not “we debit you.”

**How USDC actually lands.**

- Self-hosted: same SPL / ERC-20 transfers as Idea 1, once per period, to the two listed addresses.
- Helio overlay: buyer pays the Pay Link; Helio’s contract forwards USDC to the **linked payout wallet**. Configure Solana payout = `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3`. For EVM, payout = `0x9eb954b567ef3616424a6e1bf42c63724930aa54`. Enable “USDC on Base & Solana” swaps only if Wallet wants EVM payers compressed onto Base (Helio swap fee **0.25%** on top of 2%/1%). Auto-offramp to fiat is **0.50% extra and KYC** — skip it.

**Wallet vs Builder vs Scout**

- Wallet: never publish a Solana plan that lists a puller other than “human in Phantom.” Never create a CDP `subscriptionOwner`. If Helio is used, verify the payout-wallet screenshot matches the two treasuries before going live.
- Builder: period counter, `nextChargeUrl` display, webhook listener that only *records* `STARTED` / `RENEWED` (does not move funds).
- Scout: Loop Crypto is winding down (2026 comparison tables). Stripe stablecoin billing is 1.5% + KYB + often fiat settlement — out of scope.

**Blockers**

| Kind | Status |
|---|---|
| SIWE | **Blocked** on Base Account `subscribe()`. Helio wallet-link is wallet-connect, not SIWE; still do not add SIWE. |
| KYC | Helio crypto-to-crypto: wallet-only. Helio auto-offramp: KYC — **blocked**. Stripe / Coinbase Business: KYB — **blocked**. |
| Fees | Self-hosted: gas only. Helio: **2%** standard, **1%** with HelioX NFT, +0.25% swaps, +0.50% offramp. Solana program rent for a Plan account is ~0.004 SOL — irrelevant next to the puller-key block. Base subscriptions advertise **0% merchant fee** but need the CDP owner wallet. |
| New key | **Blocked:** Solana whitelisted puller, CDP `CDP_WALLET_SECRET`, Helio email embedded wallet. |

---

## Idea 5 — Belgian Peppol dual-rail invoice (the gap)

**Price:** 1490 USDC (compliance pack, not a 9 USDC PDF). Highest ticket in this set because the buyer is a Belgian VAT-liable firm that must already emit Peppol, and today **cannot put a USDC wallet in the legal payment means**.

**What it is.** Since **1 Jan 2026** Belgian-established VAT-registered businesses must issue and receive structured B2B e-invoices (EN 16931, Peppol BIS). FPS Finance’s three-month grace **ended 1 Apr 2026**; penalties scale **€1,500 / €3,000 / €5,000**. Peppol BIS 3.0 payment means are a **restricted UNCL4461 subset** (credit transfer 30, SEPA 58, bank account 42, etc.). Official Peppol payment text is built for **SEPA / IBAN / BIC**. A Solana or Base address is not an IBAN. Putting a wallet in `PayeeFinancialAccount/ID` will fail Access Point validation. Code `68` (online payment service) exists in the full UNCL4461 list but is **not** in the Peppol BIS allowed subset cited by implementers; code `1` (instrument not defined) is explicitly rejected.

So the **gap** is: Belgium now *requires* a Peppol XML that only knows bank rails, while the treasury only *receives* USDC on Solana/Base. Nobody in the 9 USDC catalog closes that. This pack does, as two documents, not one fake field:

1. **Legal Peppol UBL** (EN 16931 / Peppol BIS 3.0): EUR (or USD if the AP accepts), IBAN payment means filled by the *buyer’s accountant* — this file does **not** invent a bank account for us. If the seller has no IBAN, the UBL uses payment terms note + BTW fields and a **zero or informational** payment-means strategy the buyer’s AP will still reject until they supply their own IBAN. The honest product is: generate valid UBL **structure** (parties, VAT, lines, totals) and a **companion** payment annex.
2. **USDC annex** (not transported as Peppol PaymentMeans): invoice number, amount, Solana Pay URL to `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3`, Base USDC to `0x9eb954b567ef3616424a6e1bf42c63724930aa54`. Optional `cac:AdditionalDocumentReference` pointing at the annex hash so the legal invoice and the crypto pay instruction share an ID.

This is not “crypto is a Peppol payment means.” It is “Peppol for the tax file, USDC for the money,” which is the actual 2026 Belgian gap.

**How USDC actually lands.** Same as Idea 1. The Peppol XML never moves USDC. The annex is the land path. If the Belgian buyer insists on SEPA, **USDC does not land** — Wallet must say that in the FAQ. No Circle CPN Managed Payments (Circle custody + licenses + KYB). No Request Finance fiat IBAN (KYB, subscription).

**Wallet vs Builder vs Scout**

- Wallet: forbid stuffing the Solana or Base string into `PayeeFinancialAccount`. Forbid a “we’ll add an IBAN later” placeholder. Confirm USDC still only lands on the two listed addresses.
- Builder: UBL 2.1 generator (Peppol BIS customization IDs), Belgian party/VAT fields, annex HTML. Reuse the live Belgian BTW 9 USDC tool as the cheap sibling; this pack is the mandate-grade one.
- Scout: FPS Finance / BOSA Mercurius / 2028 5-corner e-reporting. Watch whether Peppol ever adds a digital-asset payment-means code — until then, keep the two-file design.

**Blockers**

| Kind | Status |
|---|---|
| SIWE | None. |
| KYC | None for USDC annex. **Blocked:** selling this as a certified Peppol Access Point (that is a BOSA/Peppol AP contract). We generate files; the buyer’s existing AP (Billto, Peppol, ERP) transports the UBL. |
| Fees | File generation: 1490 USDC to treasury (Idea 1 land path). Access Point fees are the buyer’s. No protocol cut. |
| Legal | A USDC payment does **not** by itself satisfy Belgian B2B invoice *format* law. The UBL still has to go over Peppol. Do not claim otherwise. |
| New key | None. |

---

## Cross-cuts Wallet must keep saying

1. **Only two receive addresses.** Solana `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3`, Base `0x9eb954b567ef3616424a6e1bf42c63724930aa54`.
2. **USDC only**, native on that chain. Not SOL, not XRP, not USDC.e, not a CCTP mint onto a third chain.
3. **No new keys.** Facilitator gas is *their* key (Dexter). CDP/Helio embedded/Solana puller/Base subscriptionOwner are ours-if-we-made-them, so they stay unmade.
4. **No SIWE** on any of the five. Where a vendor login is SIWE-shaped, that vendor is listed blocked.
5. **No trading / perps.** Phantom `withdraw_from_perps` / Hyperliquid is out of scope even when it mentions Base or Solana USDC.
6. **X.** Public pages were attempted; X API pay-per-use was not enrolled.

## Suggested build order

1. Idea 1 (490) — extends the live invoice, dual-chain, no vendor.  
2. Idea 2 (990) — x402 `payTo` on the same two addresses, Dexter.  
3. Idea 3 (790) — MCP skin on Idea 2.  
4. Idea 4 (490 + 190/period) — push retainers; Helio only if Wallet signs off on 2%.  
5. Idea 5 (1490) — Peppol UBL + USDC annex; do not wait for a crypto UNCL code.
