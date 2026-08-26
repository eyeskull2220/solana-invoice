# Collaborators.build sweep

**Sweep time:** 2026-08-26T00:47:09Z  
**Verdict: ZERO** — no new startable ACTIVE row exists that can be started without inventing a wallet.

Hard constraints honored: no private key generated, no SIWE, no GitHub OAuth completed, no Privy login completed. The paste-only Base address `0x9eb954b567ef3616424a6e1bf42c63724930aa54` was **not used** because this marketplace is not paste-only Base; payouts are Solana via Privy.

## Method

Public, unauthenticated reads only:

| Check | Result |
|---|---|
| `GET https://collaborators.build/` | Marketing landing. Steps: GitHub login, then "Link your Solana wallet". No public bounty table. |
| `GET https://collaborators.build/dashboard` | HTML exists; unauthenticated browser session redirected back to `/`. |
| `GET https://collaborators.build/api/bounties` | JSON list. Default payload is the live ACTIVE set. |
| `GET https://collaborators.build/api/bounties?status=ACTIVE` | Same single row. |
| `GET https://collaborators.build/api/bounties?status=SOLVED` | Two historical rows. |
| `GET https://collaborators.build/api/bounties?status=CANCELLED` | Empty list. |
| Other status filters (`PENDING`, `COMPLETED`, `CLOSED`, `OPEN`, `DRAFT`, `INACTIVE`) | `500 {"error":"Failed to fetch bounties"}` — not valid enum values. |
| `POST https://collaborators.build/api/bounties/submissions` (no `Authorization`) | `401 {"error":"Unauthorized"}` |
| `GET https://collaborators.build/api/user/me` (no `Authorization`) | `401 {"error":"Unauthorized"}` |
| `GET https://collaborators.build/api/bounties/my` | `401 {"error":"Missing or invalid authorization header"}` |
| Homepage "Start Earning Rewards" | Opens Privy dialog `Log in or sign up` with footer link to `https://www.privy.io/`. Closed immediately. No login. |

No public browse/list HTML route (`/bounties`, `/browse`, `/explore`) exists (404). API Access is listed under "Coming Soon".

## Live ACTIVE rows

**Count: 1.** Same row as prior (README $100, Oct 2025, crowded, Privy-gated). Not new.

| Field | Value |
|---|---|
| id | `cmhds5ikz0018jr04b8cuym4g` |
| title | Enchance README |
| amount | 100 (USDC label on the site) |
| status | `ACTIVE` |
| isSolved | false |
| createdAt | 2025-10-30T18:50:56.723Z |
| updatedAt | 2025-10-30T18:50:56.723Z (unchanged since create) |
| poster | andr-drgm (Andrei Dragomir) |
| repo | [andr-drgm/collaborators](https://github.com/andr-drgm/collaborators) |
| issue | [andr-drgm/collaborators#40](https://github.com/andr-drgm/collaborators/issues/40) |
| labels | `bounty`, `usdc-reward` |
| platform submissions | 10, all `PENDING` |
| GitHub PRs that close #40 | 14 (`closed_by_pull_requests.total_count`) |
| README-shaped PRs since the issue opened | 21+ (PRs 41, 43–45, 48–64) |

Platform-tracked submissions (all PENDING):

| PR | Submitter | Submitted |
|---|---|---|
| [#41](https://github.com/andr-drgm/collaborators/pull/41) | sam-gwala10 / sachingwala | 2025-12-18 |
| [#44](https://github.com/andr-drgm/collaborators/pull/44) | notjamyfriench | 2026-02-24 |
| [#48](https://github.com/andr-drgm/collaborators/pull/48) | TamerMansour-AI | 2026-05-12 |
| [#52](https://github.com/andr-drgm/collaborators/pull/52) | aigrouphobinh | 2026-05-18 |
| [#55](https://github.com/andr-drgm/collaborators/pull/55) | zr9959 | 2026-05-21 |
| [#53](https://github.com/andr-drgm/collaborators/pull/53) | qingfeng312 | 2026-05-21 |
| [#59](https://github.com/andr-drgm/collaborators/pull/59) | egoriklok | 2026-05-28 |
| [#61](https://github.com/andr-drgm/collaborators/pull/61) | Choonsiks | 2026-06-08 |
| [#64](https://github.com/andr-drgm/collaborators/pull/64) | fastrack0926 | 2026-08-11 |

The issue is still `open`. Latest issue comment (2026-08-08) reports that Collaborators **Submit Solution** failed with `prompt() is not supported`.

## Why this row is not startable under the constraints

Starting / claiming a payout on this marketplace requires a Privy session. That is not paste-only.

Evidence from the live Next.js bundle (`/_next/static/chunks/app/layout-9298de16a26638a8.js`):

- Privy `appId`: `cmgl6okij000fl50clhilr9og`
- `loginMethods: ["github"]` only (no wallet-first login, no SIWE login method)
- `embeddedWallets.solana.createOnLogin: "users-without-wallets"` — Privy **creates a Solana wallet on login** for users who do not already have one
- Supported chains: Solana mainnet (`0x536f6c4d`) and Solana Devnet (`0x536f6c4e`); default chain is Devnet
- No Base / EVM paste-address field in the start flow

Evidence from the dashboard bundle:

- `Submit Solution` POSTs to `/api/bounties/submissions` with `Authorization: Bearer <privyAccessToken>`
- Unauthenticated POST to that path returns `401 Unauthorized`
- UI copy: "No Privy access token available. Please log in."
- Rewards copy: "Solana wallet where rewards are accumulated and claimed."

Independent confirmation on issue #40 (comment by Nexu0ps, 2026-06-05): registering a PR through the public submissions endpoint "requires a Privy bearer token".

Therefore:

| Gate | Needed to start? | Allowed by this sweep? |
|---|---|---|
| Invent / generate a key | Yes, via Privy `createOnLogin: users-without-wallets` | **No** |
| SIWE | Not this site's login method (GitHub OAuth via Privy instead) | **No** (not performed) |
| Paste-only Base address | No. Payouts are Solana, not Base. | N/A — address unused |
| Unauthenticated GitHub PR only | Can open a PR, but cannot register for the bounty or receive payout | Does not count as startable |

## SOLVED rows (not startable)

Returned by `?status=SOLVED`. Both are 2025, both self-solved by the poster.

| Title | Amount | Issue | Solved at | Approved PR |
|---|---|---|---|---|
| Improve README | 100 | [#37](https://github.com/andr-drgm/collaborators/issues/37) | 2025-10-30T18:20:07.578Z | [#38](https://github.com/andr-drgm/collaborators/pull/38) andr-drgm |
| Change README title | 10 | [#26](https://github.com/andr-drgm/collaborators/issues/26) | 2025-10-29T20:35:01.909Z | [#34](https://github.com/andr-drgm/collaborators/pull/34) andr-drgm |

## New-row check vs prior

Prior knowledge: one README $100 from 2025 with 20+ PRs and Privy.

Live check 2026-08-26:

- ACTIVE count is still **1**
- Same id `cmhds5ikz0018jr04b8cuym4g`, same issue #40, same create timestamp
- `updatedAt` still equals `createdAt`
- No second ACTIVE bounty appeared
- Wallet gate is still Privy + Solana embedded wallet, not a Base paste field

**New startable rows that do not need inventing a wallet: ZERO.**
