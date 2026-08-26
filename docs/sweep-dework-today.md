# Dework.xyz sweep — 2026-08-26

**Count: 0**

No live paid Dework tasks this week match **build-this** (docs / HTML / small), after the hard filters below.

This file is a source-backed recheck. **No applications, claims, or submissions were made.**

## Verdict

Dework’s public bounties board is **stale**, not empty and not login-walled.

- Browse URL loaded without signing in: [app.dework.xyz/bounties](https://app.dework.xyz/bounties) (Connect button present; listings were readable).
- **Featured** paid `TODO` bounties: **0**.
- **All** paid `TODO` bounties: **647**, sorted creation date newest first.
- Newest listing on that sort: **2026-07-25** (`Use Diba`, Diba org, `$100 in SOL`). That is **32 days** before this sweep.
- Hard rule for this recheck: **if stale or login-blocked → ZERO.** The board is stale → **ZERO**.

This week = **2026-08-24 through 2026-08-30** (Monday–Sunday containing 2026-08-26). Checked **2026-08-26** ~00:45–00:50 UTC.

## Hard filters applied

| Filter | Rule |
|---|---|
| Window | Created **this week** (2026-08-24–2026-08-30). Older `TODO` rows are not “live this week.” |
| Stale / login | If the board is stale or requires login to see listings → count is **0**. |
| Shape | **build-this** only: docs, HTML, or other small non-code artifacts a non-coder can ship. |
| Not trade | Skip trader / DeFi-use / market-making / “use this protocol” work. |
| Not X | Skip Twitter/X threads, Superteam Earn X tasks, social-follower growth. Superteam was not queried (Dework-only sweep). |
| User does not code | Skip Development, Solidity, audits, dApp/frontend engineering. |
| No exploit | Skip security-engineer, audit-verification, bug-bounty, exploit, and PoC work. No payloads. |
| PII | Do not copy emails, phones, Discord invites, or API usernames into this file. Org names on the public board are kept. |
| Pay-to | If a task had qualified, payouts would be requested to the addresses below. None qualified. |

## Pay-to (OK if a task had qualified)

| Rail | Address |
|---|---|
| Solana USDC | `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3` |
| EVM | `0x9eb954b567ef3616424a6e1bf42c63724930aa54` |

Same Solana address as this repo’s treasury (`README.md`, `config.js`). No funds were requested. Dework payouts are DAO-chosen tokens via wallet/Safe, not guaranteed USDC on Solana.

## How this was checked

Public sources only. No wallet connect.

| Source | Result on 2026-08-26 |
|---|---|
| [dework.xyz](https://dework.xyz/) marketing site | Live. |
| [app.dework.xyz/bounties](https://app.dework.xyz/bounties) | Open Bounties UI. Default sort: **Creation date (newest first)**. 10 / page, pager **1…65**. |
| `GET https://api.dework.xyz/health` | `200` `{ "status": "ok" }` (DB up). |
| `POST https://api.deworkxyz.com/graphql?op=GetPaginatedTasksWithOrganizationQuery` | Same query the bounties page uses. Filter: `statuses: [TODO]`, `reward.exists: true`, `sortBy: createdAt DESC`. |

GraphQL totals (unauthenticated):

| Filter | `total` | Newest `createdAt` |
|---|---|---|
| `featured: true` | **0** | — |
| `featured: false` (all paid TODO) | **647** | **2026-07-25T02:30:49.025Z** |
| Writing skill `aed4f03e-9973-4b45-bee6-ee13a6406820` | **96** | **2026-07-25T02:30:49.025Z** (same `Use Diba` row) |
| `name: "docs"` | **0** | — |
| `name: "html"` | **0** | — |
| `name: "documentation"` | **0** | — |
| `name: "readme"` | **5** | **2022-08-20** (Webaverse MMO README tasks) |

UI Writing chip (after click) showed the same stale Writing-tagged rows (`Use Diba` a month ago, then year-old social/video listings). None were created this week.

Because the default sort is newest-first, **zero this-week rows on page 1 means zero this-week rows on later pages.**

## Matching this week: none

**Qualifying live paid build-this tasks: 0.**

There is no Dework docs/HTML/small bounty created in 2026-08-24–2026-08-30 that a non-coder can ship, paid, without trade/X/exploit/code.

## Checked, excluded (evidence of staleness — not apply targets)

Public titles and org names only. Dates are GraphQL `createdAt`. These fail the week window even before other filters.

| Created | Title (public) | Org | Why excluded |
|---|---|---|---|
| 2026-07-25 | Use Diba | Diba | Stale (32 days). App-test + KYC, not build-this. Pays SOL. |
| 2026-07-06 | (unreadable glyph spam) | (glyph org) | Stale. Spam. Open to bids, no token amount. |
| 2026-05-21 | Sales Growth Partner - Web3 Engineering | Oferli | Stale. Sales/marketing hire, not a small HTML/docs build. |
| 2026-05-04 | Heavy 1Inch Users | Despark | Stale. Tags `trader` / `defi` → trade. |
| 2026-02-08 | Web3 Developer Needed | Web3 Developer Needed | Stale. Development. User does not code. |
| 2026-01-26 | Solidity Security Engineer — Post Audit Verification (Uniswap V2 Fork) | Security Verification | Stale. Audit/security → **no exploit**. Past due date 2026-02-08. |
| 2025-09-28 | United Wallet Social Engagement & Followers Growth | DAO'n'Frens | Stale. Social growth, not build-this. |
| 2025-03-05 | [X Thread or Long Post] How to Get Discord Roles | NodeShift | Stale. **X**. |
| 2022-08-20 | Update README + example (hovercraft) and four sibling README tasks | Webaverse MMO | Name search `readme`. Four years stale. Also tagged Development. |

Open-to-bids rows with no posted amount were not treated as paid.

Superteam Earn / Superteam X listings were **not** opened. This sweep is Dework only.

## PII scan

| Check | Result |
|---|---|
| Emails copied into this file | **None** |
| Phone numbers | **None** |
| Discord / Telegram invite links | **None** |
| API `creator.username` fields | Present on the public GraphQL payload; **omitted here** |
| Org / workspace names | Kept (they are on the public bounties table) |
| Raw GraphQL dumps | **Not committed** |

## What was not done

- Did not click Connect / did not attach a wallet.
- Did not apply, bid, or submit.
- Did not open Superteam Earn.
- Did not write exploits, PoCs, or audit procedures.
- Did not invent a this-week listing.

If the bar is “Dework paid build-this (docs/HTML/small) created this week, no trade/X/code/exploit,” the honest count is **zero**.
