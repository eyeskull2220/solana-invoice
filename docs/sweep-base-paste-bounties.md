# Sweep: Base / ETH USDC “build this” bounties (paste address, no SIWE)

Research snapshot: **2026-08-26** (UTC).  
This file is a source-backed inventory. It is **not** an application, claim, or payout request.

**Nothing was submitted.** No private key was generated. No SIWE / Connect Wallet flow was completed.

## Constraints used

| Constraint | Value |
|---|---|
| Date | 2026-08-26 |
| Paste address | `0x9eb954b567ef3616424a6e1bf42c63724930aa54` |
| Asset / chains | Circle USDC on **Base** (`eip155:8453`) or **Ethereum**. Native Base USDC: `0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913` ([Circle](https://developers.circle.com/stablecoins/usdc-contract-addresses)) |
| Work type | “Build this” (ship a tool, feature, or artifact). Not Q&A, not exploit PoCs |
| Payout mechanic | Board must accept that **pasted 0x address** without SIWE or Connect Wallet |
| HARD | Do not invent a key. Do not SIWE |
| HARD | Skip BountyBook (SIWE / nonce-sign wall) |
| HARD | Skip Immunefi exploits |
| HARD | DeskCrew Base rows: **list only, do not submit**. Wallet 08:00 is Solana ticket **239** only |

The Solana treasury in this repo (`96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3`) cannot receive Base/ETH USDC. This sweep uses the EVM paste address above only.

## Result

**Zero high-credibility “build this” bounties on Base/ETH USDC accept a pasted `0x` address without SIWE or Connect Wallet.**

The only open board that literally asks you to paste `Method / Address / Network` in a GitHub comment is ClankerNation/OpenAgents. That board fails a credibility check (see below). Every other live Base USDC “build this” board found today either (a) requires a private key or wallet signature, (b) is a SIWE wall, (c) is Q&A rather than build work, or (d) has an empty funded inventory.

Do **not** treat “paste this address somewhere” as equivalent to “the board will pay this address.” Payment still depends on each board’s own escrow, KYC, and settlement rules.

## How this was checked

Pulled on 2026-08-26 UTC:

| Source | What was fetched |
|---|---|
| DeskCrew arena | `GET https://deskcrew.io/api/arena/contests` (6 open bounties) |
| BountyBook jobs | `GET https://api.bountybook.ai/jobs?status=open` pages 1–6 (111 open jobs; **not claimed**) |
| Agent Bounties | `GET https://api.agentbounties.app/v1/opportunities?view=ready_to_earn` (15 claimable, escrowed, `verification_ready=true`) |
| Taskmarket | `GET https://api.taskmarket.dev/api/tasks?status=open&limit=100` (5 open) plus [docs](https://docs-market.daydreams.systems/getting-started/quick-start) |
| ubounty.ai | https://ubounty.ai/bounties (empty filter page); demo issue [#3](https://github.com/ubounty-app/ubounty-demo/issues/3) already paid/closed |
| OpenAgents | `gh issue list --repo ClankerNation/OpenAgents --state open` (100 listed; 29 “Add …” build-style) |
| Algora | `GET https://algora.io/api/bounties?status=open` (0 open; USD/Stripe anyway) |
| Dework | Product docs + [gigs.sh/p/dework](https://gigs.sh/p/dework): Connect Wallet / MetaMask / WalletConnect required |
| Immunefi | Skipped by constraint (exploit programs) |
| Superteam Earn | Solana rail — out of scope for this Base/ETH paste address |

---

## DeskCrew Base rows (list only — do not submit)

Public board: [deskcrew.io/arena](https://deskcrew.io/arena) · JSON: `GET https://deskcrew.io/api/arena/contests`

Payout is **not** a pasted address. USDC settles on `payoutNetwork` to **the wallet that paid the x402 draft fee**. That needs a funded key. Hard rule for this sweep: **do not submit**. Wallet 08:00 is reserved for Solana ticket **239**.

| Ticket | Subject | Gross | Net (85%) | `payoutNetwork` | Entrants | `decidesAt` (UTC) |
|---|---|---|---|---|---|---|
| [235](https://deskcrew.io/arena) | How do I let an AI agent answer my support tickets without giving it access to my inbox? | $1.00 | $0.85 | **base** | 6 | 2026-08-26T15:43:46Z |
| [236](https://deskcrew.io/arena) | What is x402 and how does an agent pay for an API call with it? | $1.00 | $0.85 | **base** | 6 | 2026-08-26T15:44:36Z |
| [237](https://deskcrew.io/arena) | Can an AI agent hold and spend USDC on its own, and what are the risks? | $1.00 | $0.85 | **base** | 6 | 2026-08-26T15:45:30Z |
| [238](https://deskcrew.io/arena) | How should a small business decide what a support answer is worth paying for? | $1.00 | $0.85 | **base** | 6 | 2026-08-26T15:46:20Z |
| [240](https://deskcrew.io/arena) | How do I stop an AI agent from being tricked by instructions hidden inside a customer's message? | $1.00 | $0.85 | **base** | 6 | 2026-08-26T15:48:52Z |

These are rubric Q&A tickets, not “build this” artifacts. Listed only because they are the live Base-funded DeskCrew rows on this date.

### Wallet 08:00 / ticket 239 (Solana — out of this paste address)

| Ticket | Subject | `payoutNetwork` | Entrants | `decidesAt` (UTC) |
|---|---|---|---|---|
| [239](https://deskcrew.io/arena) | How can an agent that resells research or support answers keep a margin without cheating the client? | **solana** | 2 | 2026-08-26T15:47:20Z |

Do **not** send a Base `0x` address at this row. A Solana wallet cannot be paid on Base, and this Base address cannot be paid on Solana. Board text: “a bounty cannot pay out on any other one.”

---

## Paste-address surface that exists, but is not credible

### ClankerNation/OpenAgents — GitHub comment paste (do not treat as payable)

Repo: [github.com/ClankerNation/OpenAgents](https://github.com/ClankerNation/OpenAgents)

The bot comment on every bounty issue asks solvers to paste payment in `/attempt` and `/claim` with **no wallet connect**:

```
Method: USDC / USDT / BTC / ETH / XMR / PayPal
Address: <your wallet address or PayPal email>
Network: <Base / Ethereum / Solana / Bitcoin / Monero>
```

That **is** a paste-address mechanic. Issues titled `Add …` are “build this” (SDK helpers, OpenAPI schema, Permit2, gas relay, etc.), not Immunefi exploit reports.

**Why this is not a match for work:**

- Issues are authored by GitHub App `clanker-journalist` (bot).
- Duplicate titles at different dollar labels (`$1k`–`$9k`) for the same “Add …” spec.
- Acceptance criteria demand pasting the **entire session initialization block** (instructions, runtime config, home directory) into source. That is a secret-harvest pattern. Do not do it.
- `gh pr list --state merged` on 2026-08-26 returned **zero** merged PRs. No on-chain payout evidence was found.
- Comments already contain competing paste addresses; none of those claims were closed as paid.

If a human maintainer later proves settlement on Base/ETH USDC, the paste format would accept `0x9eb954b567ef3616424a6e1bf42c63724930aa54` / Base. Until then, treat the board as unpaid agent bait.

Unique “Add …” templates still open (first 100 issues; amounts collide across duplicates):

| Template | Example issue |
|---|---|
| Add OpenAPI schema generation with authentication documentation | [#185](https://github.com/ClankerNation/OpenAgents/issues/185) |
| Add event subscription and decoding to OpenAgentsSDK | [#196](https://github.com/ClankerNation/OpenAgents/issues/196) |
| Add structured error responses with error codes | [#202](https://github.com/ClankerNation/OpenAgents/issues/202) |
| Add contract deployment helpers to SDK | [#199](https://github.com/ClankerNation/OpenAgents/issues/199) |
| Add batch operations to AgentRegistry for gas efficiency | [#194](https://github.com/ClankerNation/OpenAgents/issues/194) |
| Add audit log for all admin actions | [#192](https://github.com/ClankerNation/OpenAgents/issues/192) |
| Add gas sponsorship relay for agent transactions | [#190](https://github.com/ClankerNation/OpenAgents/issues/190) |
| Add permit2 support to all token interaction contracts | [#175](https://github.com/ClankerNation/OpenAgents/issues/175) |
| Add flash loan integration to LendingPool for liquidation bots | [#160](https://github.com/ClankerNation/OpenAgents/issues/160) |
| Add delegation snapshot for governance votes at proposal creation | [#149](https://github.com/ClankerNation/OpenAgents/issues/149) |
| Add time-locked admin transfers for all Ownable contracts | [#146](https://github.com/ClankerNation/OpenAgents/issues/146) |

“Fix …” issues in the same repo are closer to exploit/bug work and were not counted as “build this.”

---

## Skipped (with reason)

### BountyBook — SIWE / nonce-sign wall (skipped as ordered)

API: `https://api.bountybook.ai/jobs?status=open` · Docs: [bountybook.ai/docs](https://www.bountybook.ai/docs)

Live on this date: **111** open jobs on chain `8453` (Base). **90** `job_type: code`, **74** titles starting with `Build `. Rewards are USDC (examples: EventBus 5.00, FastAPI news aggregator 20.00, OpenAPI→pytest CLI 25.00).

Claim/submit requires `Authorization: Bearer` from the nonce → sign → verify flow (`api.bountybook.ai/auth/*`). That is a SIWE-class wall. **Not listed as actionable. Not claimed.** No key was generated for it.

### Immunefi — exploits (skipped as ordered)

Standing Base/ETH security programs were not opened or inventoried. This sweep is “build this,” not vulnerability reports.

### Agent Bounties — escrowed, but not paste

`GET https://api.agentbounties.app/v1/opportunities?view=ready_to_earn` at 2026-08-26T00:48:51Z returned **15** `claimable` + `verification_ready=true` rows on `base-mainnet`, 3 or 6 USDC each. They are GMV competitions (“Highest externally funded canonical GMV”), not “build this” tools.

Claim path: `prepare_agent_to_earn` → `agent_native_claim` → **sign `wallet_request`**. Check-in accepts `--solver-wallet 0x…` as a public address, but settlement still requires a signature from that wallet. That is not paste-only. Not signed.

### Taskmarket — real “build this” on Base USDC, needs a key

Public list: [taskmarket.dev](https://taskmarket.dev) · `GET https://api.taskmarket.dev/api/tasks?status=open`

JSON `status=open` on this snapshot returned 5 rows. Two are “build this”:

| Reward | Mode | Task id | Title (from description) |
|---|---|---|---|
| 2 USDC | bounty | `0xfc767ac1fd6349c1726d6d7ac37633ba611519d5cedd05f85c15fe6c19f4c90b` | Create a Complete Brand Kit for Leaf Box |
| 20 USDC | bounty | `0xf0f5e908e155c6da0318634c1443886641d36df2b3e866321d94aee324350928` | Design & Build an Exceptional Anime / Movie / TV Tracking App |

Payout is Circle USDC on Base to the **registered worker wallet**. Registration is `taskmarket init` (generates a key) or `taskmarket wallet import` (requires the private key for the paste address). This sweep does not have that key and must not invent one. **Not submitted.**

### Dework — Connect Wallet wall

[app.dework.xyz/bounties](https://app.dework.xyz/bounties) pays USDC/ETH from DAO Safes, but onboarding is MetaMask / WalletConnect / Gnosis Safe. That is Connect Wallet. Not a paste field.

### ubounty.ai — paste-in-settings exists, inventory empty

Docs say developers paste an `0x` address at [ubounty.ai/settings](https://ubounty.ai/settings) after GitHub login (not SIWE). https://ubounty.ai/bounties rendered **no open rows** on this date. The funded demo ([ubounty-app/ubounty-demo#3](https://github.com/ubounty-app/ubounty-demo/issues/3), 10.5 USDC on Base) is already paid and closed.

### Algora — not USDC

Open bounty count 0. When Algora pays, it is Stripe USD, not Base/ETH USDC.

### Superteam Earn — Solana

Agent listings pay USDC/SOL to a Solana wallet via a human claim-code. Out of scope for this EVM paste address.

---

## If a qualifying board appears later

Paste **exactly**:

```
0x9eb954b567ef3616424a6e1bf42c63724930aa54
```

Network: **Base** (preferred) or **Ethereum**. Token: native Circle USDC, not USDbC (`0xd9aAEc86B65D86f6A7B5B1b0c42FFA531710b6CA`).

Do not generate a burner key “so the agent can claim.” Do not SIWE. Do not submit DeskCrew Base rows from this wallet. Do not use this address on DeskCrew 239 (Solana).
