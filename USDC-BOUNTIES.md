# Currently open USDC bounties (Solana-first)

Research snapshot: **2026-08-25** (UTC).  
This file is a source-backed inventory. It is **not** an application or a submission.

**This research did not apply to any program.**

## Constraints used

| Constraint | Value |
|---|---|
| Receive address | `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3` |
| Asset / chain | Circle USDC on **Solana mainnet only** |
| Circle USDC mint (Solana mainnet) | `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v` ([Circle contract addresses](https://developers.circle.com/stablecoins/usdc-contract-addresses)) |
| Excluded | Anything that **requires X (Twitter)** to submit |
| Excluded | Anything that **requires launching a token** |
| Excluded | Invented listings, expired contests, grants that are not bounties, and payouts that are not USDC |

Circle native USDC on Solana is the mint above. Other “USDC” mints (devnet tokens, wrapped copies, or USDC on Ethereum/Base) **cannot** be received at the treasury address as Solana mainnet USDC without a separate bridge/swap. This file does not assume a bridge.

## How this was checked

Primary sources pulled on the snapshot date:

- Superteam Earn live listings: `GET https://earn.superteam.fun/api/listings?status=open` (28 `OPEN` rows) plus per-listing `GET https://earn.superteam.fun/api/listings/details/{slug}`
- Superteam Earn FAQ: [docs.superteam.fun …/superteam-earn-faq](https://docs.superteam.fun/the-superteam-handbook/community/faqs/superteam-earn-faq)
- Immunefi program pages linked below (live/paused/ended status and payout text taken from those pages)
- Kamino’s own bounty docs: [kamino.com/docs/security/bug-bounty](https://kamino.com/docs/security/bug-bounty)
- Raydium disclosure: [docs.raydium.io/security/disclosure](https://docs.raydium.io/security/disclosure)
- Drift `SECURITY.md`: [github.com/drift-labs/protocol-v2/blob/master/SECURITY.md](https://github.com/drift-labs/protocol-v2/blob/master/SECURITY.md)
- DeskCrew public board: `GET https://deskcrew.io/api/bounties` and [deskcrew.io/llms.txt](https://deskcrew.io/llms.txt)
- Agent Overflow: `GET https://agentoverflow-app.vercel.app/api/bounties/crypto` and [SKILL.md](https://agentoverflow-app.vercel.app/SKILL.md)
- Circle Grants: [circle.com/grant](https://www.circle.com/grant) and [Arc community relaunch post (2026-05-14)](https://community.arc.io/public/blogs/circle-developer-grants-program-relaunches-2026-05-14)

If a program is not listed as matching, it was either not found as currently open, failed a constraint, or its payout rail was not documented as Solana mainnet USDC.

---

## Matching: currently open, USDC, no X required, no token launch

These are the listings this research could verify against the constraints. Payout-to-`96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3` still depends on each program’s own KYC/wallet form; this file does not claim they will honor that address.

### 1. Kamino — Immunefi (standing)

| Field | Source text |
|---|---|
| Status | Immunefi page: live since 6 Oct 2025; last updated 10 Jul 2026; not marked paused |
| Chain | Solana |
| Payout | “Kamino provides rewards in USDC on Solana, denominated in USD.” / “payments are done in USDC on SOL.” |
| Max | $1,500,000 (critical smart contract: 10% of funds at risk, min $150,000) |
| Also | Web/app critical $20,000–$50,000; high up to $10,000; smart-contract high up to $100,000; medium $10,000 |
| KYC | Required (full name, DOB, proof of address, government ID) |
| PoC | Required for all severities |
| X / token launch | Not required |
| Submit | [immunefi.com/bug-bounty/kamino/information/](https://immunefi.com/bug-bounty/kamino/information/) |
| Same terms | [kamino.com/docs/security/bug-bounty](https://kamino.com/docs/security/bug-bounty) |

Kamino docs also state: testing on mainnet or public testnet is prohibited; use local forks.

### 2. GMTrade — Immunefi (standing)

| Field | Source text |
|---|---|
| Status | Live since 6 Jul 2026; last updated 13 Aug 2026 |
| Chain | Solana |
| Payout | “GMTrade provides rewards in USDC on Solana, denominated in USD.” |
| Max | $100,000 (critical 10% of funds at risk, min $25,000), **further capped at 10% of protocol treasury** at `4tf9zEjvj2BUR9ZaAr53sQdULDWGGpJTr2zngSrmjtN6` |
| Also | High $10,000–$20,000; medium $2,500–$7,500 |
| KYC | “KYC not required” |
| PoC | Runnable PoC required |
| X / token launch | Not required |
| Submit | [immunefi.com/bug-bounty/gmtrade/information/](https://immunefi.com/bug-bounty/gmtrade/information/) |

### 3. OnRe — Immunefi (standing)

| Field | Source text |
|---|---|
| Status | Live since 11 May 2026; last updated 20 Jul 2026 |
| Chain | Solana program `onreuGhHHgVzMWSkj2oQDLDtvvGvoepBPkqyaubFcwe` |
| Payout | Immunefi header: “OnRe provides rewards in USDC on Solana, denominated in USD.” Reward body: “payments are done in USDC.” |
| Max | $100,000 (critical 10% of on-chain funds at risk, min $10,000). Off-chain Bermuda SAC capital is excluded from funds-at-risk. |
| Also | High $5,000; medium $2,000; low $1,000 |
| KYC | Required (identity document + proof of address via Onfido). OFAC / excluded-jurisdiction residents ineligible. |
| PoC | Required for all listed severities |
| X / token launch | Not required |
| Submit | [immunefi.com/bug-bounty/onre/information/](https://immunefi.com/bug-bounty/onre/information/) |

### 4. Drift Protocol — self-hosted (standing)

| Field | Source text |
|---|---|
| Status | `SECURITY.md` on `master` is published as a current program (no end date on that file) |
| Scope | Drift on-chain program code; UI-only bugs omitted |
| Payout | “Bug bounties will be paid in USDC. Alternative payment methods can be used on a case-by-case basis.” |
| Amounts | Critical: 10% of hack value up to $500,000; high $10,000–$50,000; medium/low $1,000–$5,000 |
| Chain of USDC | **Not specified** in `SECURITY.md`. Drift is a Solana protocol; the file does not say “USDC on Solana.” |
| X / token launch | Not required |
| Submit | Email `hello@drift.trade` with attack vector; PoC on a privately deployed mainnet contract required for critical/moderate |

Source: [github.com/drift-labs/protocol-v2/blob/master/SECURITY.md](https://github.com/drift-labs/protocol-v2/blob/master/SECURITY.md)

Do not treat Drift as a confirmed Solana-mint payout until the team states the rail.

### 5. Manic Trade — Superteam Earn (time-boxed)

| Field | Source text |
|---|---|
| Listing | [$1,000 USDC Manic Bug Bounty](https://superteam.fun/earn/listing/dollar1000-usdc-manic-bug-bounty/) (`dollar1000-usdc-manic-bug-bounty`) |
| Status | `OPEN`, `isWinnersAnnounced: false` |
| Token | `USDC` |
| Pool | 1,000 USDC (P0 300×1; P1 100×3; P2 50×4; P3/improvement 10×20). Unused slots may be reallocated; total will not exceed 1,000. |
| Deadline | 2026-09-07T06:59:59.000Z (winner announcement commitment 2026-09-14) |
| Agent access | `HUMAN_ONLY` |
| X required? | **No.** Community links include X, but submission is Typeform + Superteam Earn. Eligibility Q3 allows “wallet address, email, **or** X account used to log in to Manic” as an account identifier — that is not a requirement to post on X. |
| Token launch? | No |
| Work | Test Manic Polymarket integration at `app.manic.trade/pm` with **real USDC**; report via [Typeform](https://form.typeform.com/to/TzfbvaPZ) then Superteam |
| Sponsor | Manic Trade (`isFndnPaying: false` → external sponsor) |
| Superteam payout path | External-sponsor listings “will be paid out to the wallet associated with the winner's Superteam Earn account.” Occasional invoice/KYC possible. ([Earn FAQ](https://docs.superteam.fun/the-superteam-handbook/community/faqs/superteam-earn-faq)) |

Superteam does not print “Solana USDC mint …” on this listing. Earn is a Solana marketplace and pays to a linked Solana wallet; this research did not find a Manic-specific statement of the mint.

### 6. DeskCrew board row 239 — live, small, Solana-settled

Public board snapshot from `GET https://deskcrew.io/api/bounties` on 2026-08-25:

| Field | Value |
|---|---|
| Ticket | 239 |
| Subject | “How can an agent that resells research or support answers keep a margin without cheating the client?” |
| Gross / net | $1.00 / $0.85 (85% agent share) |
| `payoutNetwork` | `solana` |
| Judge | `rubric`; `decidesAt` `2026-08-26T15:47:20.697Z` |
| Entrants at snapshot | 2 |
| X / token launch | Not required |
| Board copy | “Approved answers settle in USDC to the wallet that submitted, on the chain the task was funded on.” ([deskcrew.io/bounties](https://deskcrew.io/bounties), [llms.txt](https://deskcrew.io/llms.txt)) |

The other five open rows in the same snapshot had `payoutNetwork: "base"`. Those are USDC, but **not** Solana.

This row is time-sensitive (`decidesAt` is 2026-08-26). Re-fetch the API before treating it as still open.

---

## Open on Solana, USDC possible but not guaranteed

These programs are live and Solana-scoped. They **may** pay USDC; the team chooses the token.

### Orca — Immunefi

- Live since 19 May 2022; last updated 18 Aug 2026.
- “Orca provides rewards in USDC, ORCA on Solana.”
- “Payouts of up to USD 250 000 are done in ORCA or USDC (SPL Version) **at the discretion of the team**. Payouts above USD 250 000 will be done in ORCA and will be vested monthly over a 12-month period.”
- Max $500,000. KYC not required. PoC required.
- [immunefi.com/bug-bounty/orca/information/](https://immunefi.com/bug-bounty/orca/information/)

### Raydium — Immunefi

- Live since 25 Apr 2023; last updated 9 Jul 2026.
- “Raydium provides rewards in RAY, SOL, USDC on Solana.”
- “payouts are done in RAY, SOL or USDC.” Raydium docs repeat: paid in **RAY, SOL, or USDC**. No KYC.
- Max $505,000 (critical 10% of funds at risk, min $50,000).
- [immunefi.com/bug-bounty/raydium/information/](https://immunefi.com/bug-bounty/raydium/information/)
- [docs.raydium.io/security/disclosure](https://docs.raydium.io/security/disclosure)

---

## Open USDC Superteam listings that fail the X / token-launch filter

All of these were `status: OPEN` and `token: USDC` on Superteam Earn at snapshot. They are listed so this file is not silently incomplete.

| Listing | Pool | Deadline (UTC) | Why excluded |
|---|---|---|---|
| [Why Digital Credit Matters](https://superteam.fun/earn/listing/why-digital-credit-matters/) (Apyx) | 2,000 | 2026-08-27 | “Create an educational **X (Twitter) thread**”; “Publish an original X thread”; tag `@Apyx_Fi` |
| [Superteam Nepal Creator Bounty: The Superteam Story](https://superteam.fun/earn/listing/superteam-nepal-creator-bounty-the-superteam-story/) | 400 | 2026-08-27 | “Be published on **X/Twitter (mandatory)** and LinkedIn (mandatory)”; Nepal region |
| [Twitter Post about NFT Locks on Streamflow](https://superteam.fun/earn/listing/twitter-post-about-nft-locks-on-streamflow/) | 500 | 2026-08-28 | “Single **X post**, video, or thread”; tag `@streamflow_fi` |
| [Create Content About KriptoK League](https://superteam.fun/earn/listing/kriptok-league-content-bounty/) | 750 | 2026-08-30 | Accepted formats include long-form **X** posts / QRTs / threads; “Either tag `@KriptoKGlobal` or QRT …” |
| [Superteam Nepal Ambassador Campaign](https://superteam.fun/earn/listing/superteam-nepal-ambassador-campaign/) | 205 | 2026-08-31 | Requires social share links including X; Nepal Campus Ambassadors only |
| [Compose X Thread Explaining Segmento](https://superteam.fun/earn/listing/compose-x-thread-explaining-segmento-and-on-chain-user-intelligence/) | 300 | 2026-09-02 | “The submission must be an **X (Twitter) thread**”; follow Segmento on X |
| [FairScale QRT Campaign for Custom $ANSEM Score](https://superteam.fun/earn/listing/fairscale-ansem/) | 100 | 2026-09-03 | **X QRT required** (“ONLY QRTs WILL COUNT”) **and** `$ANSEM` token score campaign |
| [Create The Best X Thread About My Crypto Casino](https://superteam.fun/earn/listing/create-the-best-x-thread-about-my-crypto-casino/) | 1,500 | 2026-09-04 | X thread; account must be verified, ≥6 months old, ≥100 followers |
| [Post: Why Flint Beats Building Your Own Prop AMM](https://superteam.fun/earn/listing/post-why-flint-beats-building-your-own-prop-amm/) | 1,500 | 2026-09-07 | “A single **X post**, video, or thread”; tag `@flint_trade_` |
| [Write an X Thread Explaining Aeonian Trade](https://superteam.fun/earn/listing/aeonianbounty/) | 500 | 2026-09-09 | “The submission must be an **X (Twitter) thread**” (≥4 posts) |
| [🟢 ZNS Solana Creator Challenge](https://superteam.fun/earn/listing/zns-sol/) | 500 | 2026-09-09 | **Token launch required**: “Launch a new token through ZNS Launchpad on Solana”; min $500 volume, 20 holders, 7 days active |
| [Trade, Tweet & Earn](https://superteam.fun/earn/listing/trade-tweet-and-earn-1/) | 500 | 2026-09-20 | “Submit one **tweet** about your experience” |

The remaining Superteam `OPEN` listings at snapshot paid **USDG**, not USDC, and are omitted from the USDC set.

---

## Checked and excluded (with reason)

### Not currently open, or not USDC

| Program | What the source says | Why excluded |
|---|---|---|
| Immunefi **Audit Comp \| Firedancer V1** | Page title: “This Audit Competition Is Over.” Window 9 Apr 2026 17:00 UTC – 9 May 2026 17:00 UTC. Would have paid “USDC on Solana.” | Ended |
| **Alpenglow** competition | Submission window 2026-08-05 16:00 UTC – 2026-08-19 16:00 UTC; prize pool up to 50,000 **SOL** ([RULES.md](https://github.com/anza-xyz/alpenglow/blob/master/RULES.md)) | Ended; pays SOL |
| **Squads** perpetual bounty | Pays “USD in **locked SOL** tokens (locked for 12 months)” ([docs.squads.so/main/security/bug-bounty](https://docs.squads.so/main/security/bug-bounty)) | Not USDC |
| **Jito** Immunefi | “payments are done in **JTO** on Solana.” Live, last updated 12 Aug 2026 | Not USDC |
| **Marinade** Immunefi | Rewards in mSOL / MNDE | Not USDC |
| **Solana Mobile** bug bounty | Colosseum Codex (20 Aug 2026): paid in **SKR** under a signed Award Agreement with vesting | Not USDC |
| Superteam `OPEN` **USDG** listings | 16 of 28 live Earn rows at snapshot, including Breakpoint content (8,000 USDG) | Token is USDG, not USDC |

### USDC, but not Solana mainnet (treasury cannot receive as-is)

| Program | Payout rail in source | Notes |
|---|---|---|
| **Pyth Network** Immunefi | “rewards in **USDC on Ethereum**.” Live; last updated 16 Jun 2026; KYC required; max $250,000 | Solana ecosystem program, Ethereum USDC |
| **0x** Immunefi | “rewards in **USDC on Ethereum**.” Solana is in the ecosystem list; last updated 18 Aug 2026 | Not Solana USDC |
| **KAST** Immunefi | “payments are done in **USDC on Ethereum**.” Codebase cited includes Solana M extensions | Not Solana USDC |
| **TruYields / TruFin** Immunefi | “USDC on Ethereum” | Solana in ecosystem list |
| **DeskCrew** tickets 235–238, 240 | `payoutNetwork: "base"` at snapshot | USDC on Base |
| **Agent Overflow** | SKILL.md: **Network: Solana devnet**; mint `GKFJwYjcV5pDhSCsRZeuSSVgpbRSPo2HMRVGRH5KzzEu` **(devnet)**; faucet is “0.05 SOL + $50 USDC (devnet).” 17 `funded` rows in the public API all had deadlines in May–Jul 2026 | Devnet USDC has no dollar backing ([Circle testnet warning](https://developers.circle.com/stablecoins/usdc-contract-addresses)). Deadlines already passed at snapshot |

### Open, but not a bounty, or payout rail not shown as Solana USDC

| Program | What it is | Why not in the matching table |
|---|---|---|
| **Circle Developer Grants** | Milestone USDC grants, $5,000–$100,000 stated on [circle.com/grant](https://www.circle.com/grant). 14 May 2026 relaunch is **Arc-forward** (“Arc is core to your flow of value…”). Apply at [circle.questbook.app](https://circle.questbook.app/) | Grant application, not a bounty. Chain of USDC disbursement is not stated as Solana. **Not applied.** |
| **Solana Foundation Funding** | Rolling grants / RFPs ([solana.org/grants-funding](https://solana.org/grants-funding)) | Grants, not bounties; currency not specified as Solana USDC on that page |
| **Circle BBP** on HackerOne | Program page exists: [hackerone.com/circle-bbp](https://hackerone.com/circle-bbp). Circle’s [solana-cctp-contracts SECURITY.md](https://github.com/circlefin/solana-cctp-contracts/blob/master/SECURITY.md) says report via that program | This research did **not** get a non-JS render of the full HackerOne policy. Public reward tables indexed for the program are **USD ranges** ($150–$5,000). **No Circle page fetched here states “USDC on Solana” as the Circle BBP settlement rail.** Arc-specific HackerOne campaign text (Arc blog, 9 Apr 2026) ran **through 1 Jun 2026**. |
| **Firedancer standing bounty** | Firedancer V1 contest page tells researchers to use “the standing bug bounty” for Frankendancer-only code | Contest is over. This research did **not** retrieve a live Immunefi standing-program page at `/bug-bounty/firedancer/` (that URL 404’d / timed out). Not listed as verified-open. |

---

## Practical notes for the treasury address

1. **Do not send** Circle grants, HackerOne, or Ethereum-USDC payouts to `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3` and expect them to appear as Solana USDC. That address is specified here as a **Solana USDC receive** wallet only.
2. Programs that pay “USDC on Solana” (Kamino, GMTrade, OnRe header, DeskCrew Solana rows, Orca/Raydium if they choose USDC) are the ones whose documented rail matches the mint above.
3. Superteam external-sponsor payouts go to **the Solana wallet on the Earn profile**, not automatically to an unpublished address. If a Superteam win is claimed, the Earn profile wallet must be this treasury address (or the sponsor must be told that address).
4. Immunefi KYC programs (Kamino, OnRe) will not pay until identity checks pass.
5. Immunefi and Kamino/Raydium rules prohibit mainnet exploitation. This file does not describe attacks.

## What this file is not

- Not a submission, application, or claim of work done.
- Not a complete map of every USDC bounty on every chain.
- Not a promise that any sponsor will pay the treasury address.
- Not advice to trade, deposit real funds, or test on mainnet.

Re-check Superteam `?status=open`, Immunefi program headers, and `https://deskcrew.io/api/bounties` before acting; live boards change.
