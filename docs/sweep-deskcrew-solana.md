# DeskCrew Solana-USDC sweep

Snapshot date: **2026-08-26** (UTC).  
Fetched at **2026-08-26T00:46:43Z**.

This file is a source-backed inventory of **startable DeskCrew rows that pay Circle USDC on Solana**. It is **not** a submission.

**Nothing was submitted.** Ticket **239 was not entered tonight.** The wallet was not used.

## Startable Solana-USDC rows

**None.**

There is no startable DeskCrew contest or bounty besides ticket 239 that pays Solana USDC on this snapshot.

That empty list is the result of the filters below applied to the live board. No rows were invented.

## Hard constraints applied tonight

| Constraint | Action taken |
|---|---|
| Do not submit 239 tonight | Ticket 239 was **not** entered. No `draft_reply`, `propose_resolution`, or other paid write. |
| Wallet 08:00 only if USDC ≥ 0.06 | Wallet was **not** used. No balance check, no x402 payment, no spend. Next wallet use is 08:00 **and** only if Solana USDC ≥ 0.06. |
| Solana USDC payout, not Base | A row counts only if `payoutNetwork` is exactly `"solana"`. `toolPayableNetworks` including `"solana"` is **not** a Solana payout. |
| Do not invent | Only rows returned by the live board APIs below. |
| Still open | Row must be present on the live board. `closesAt: null` on every listed bounty. |
| Besides 239 | Ticket 239 is excluded from the startable list even though it is the only Solana payout row. |

Treasury receive address (this repo, `config.js` / README): `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3`  
Circle USDC mint on Solana mainnet: `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v`

A DeskCrew bounty pays the wallet that paid the draft fee, on that row's `payoutNetwork` only. Base USDC cannot land at the Solana treasury address.

## How this was checked

Primary sources, all pulled on the snapshot timestamp:

1. `GET https://deskcrew.io/api/arena/contests` — HTTP 200, `cache-control: public, max-age=60`. Canonical board JSON. `GET https://deskcrew.io/api/bounties` **302**s here.
2. Anonymous MCP `list_bounties` — `POST https://deskcrew.io/api/mcp/deskcrew` with `{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"list_bounties","arguments":{}}}`. Same six `ticketId`s, same `payoutNetwork` values.
3. `GET https://deskcrew.io/.well-known/x402` — `arena.contests.enabled: false`, `arena.contests.open: 0`, `arena.bounties.enabled: true`, `arena.bounties.open: 6`. Solana tool asset is Circle USDC mint `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v`.
4. Human board: [deskcrew.io/arena](https://deskcrew.io/arena). Agent index: [deskcrew.io/llms.txt](https://deskcrew.io/llms.txt).

Board semantics from that JSON (`howToEnter`) and [deskcrew.io/llms.txt](https://deskcrew.io/llms.txt):

- Payment settles on that row's `payoutNetwork`, in USDC, to the wallet that paid for the draft.
- A bounty cannot pay out on any other chain.
- `toolPayableNetworks` is only which chains can pay the **tool fee** (draft ~$0.06). It is not the payout chain.
- Named **contests** add an entry fee and a cap. Plain **bounties** cost only the normal tool price.

## Named contests

From `GET https://deskcrew.io/api/arena/contests` and `/.well-known/x402` → `arena.contests`:

| Field | Live value |
|---|---|
| `enabled` / `arena.contests.enabled` | `false` |
| `contests` array | `[]` |
| `arena.contests.open` | `0` |

There are **no open named contests** on this snapshot. The six open rows are plain bounties (`bountiesEnabled: true`, `count: 6`, `economics.openBounties: 6`).

## Filter

A row is startable in this sweep only if **all** of these hold:

1. Present on the live board (`bounties[]` or `contests[]`).
2. `payoutNetwork === "solana"` (not `"base"`, not Polygon/Sei/Avalanche).
3. `ticketId !== 239`.
4. Still open (`closesAt` null or in the future; still listed).

No row besides 239 passed step 2.

## Excluded live rows (not startable)

All six live bounties: `tenantSlug: "deskcrew"`, `bountyUsd: 1`, `netRewardUsd: 0.85`, `toolPriceUsd: 0.06`, `mode: "winner-take-all"`, `judge: "rubric"`, `closesAt: null`, `refundPolicy: "tool-fee-not-refundable"`. Each lists `toolPayableNetworks: ["base","polygon","sei","avalanche","solana"]` — that does **not** make the payout Solana.

| ticketId | payoutNetwork | entrants | decidesAt (UTC) | Why excluded |
|---|---|---|---|---|
| 235 | `base` | 6 | 2026-08-26T15:43:46.448Z | Pays Base USDC, not Solana. Subject: *How do I let an AI agent answer my support tickets without giving it access to my inbox?* |
| 236 | `base` | 6 | 2026-08-26T15:44:36.259Z | Pays Base USDC, not Solana. Subject: *What is x402 and how does an agent pay for an API call with it?* |
| 237 | `base` | 6 | 2026-08-26T15:45:30.251Z | Pays Base USDC, not Solana. Subject: *Can an AI agent hold and spend USDC on its own, and what are the risks?* |
| 238 | `base` | 6 | 2026-08-26T15:46:20.514Z | Pays Base USDC, not Solana. Subject: *How should a small business decide what a support answer is worth paying for?* |
| **239** | `solana` | 2 | 2026-08-26T15:47:20.697Z | **Only Solana-USDC payout on the board. Hard skip tonight: do not submit.** Subject: *How can an agent that resells research or support answers keep a margin without cheating the client?* |
| 240 | `base` | 4 | 2026-08-26T15:48:52.361Z | Pays Base USDC, not Solana. Subject: *How do I stop an AI agent from being tricked by instructions hidden inside a customer's message?* |

Ticket 239 is recorded only so the skip is auditable. It is **not** a startable row for this sweep.

## Wallet gate (not executed)

Draft entry on any of these rows costs `toolPriceUsd: 0.06` USDC (not refundable). Tonight:

- No wallet RPC, no Phantom call, no x402 `X-PAYMENT`.
- No spend until **08:00**, and then only if Solana USDC ≥ **0.06**.
- Even at 08:00, 239 stays skipped unless a later instruction lifts that hard rule.

DeskCrew Solana settlement (from `/.well-known/x402`, not used tonight):

| Item | Value |
|---|---|
| Tool-fee Solana asset (Circle USDC) | `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v` |
| Tool-fee Solana `payTo` | `ATubF1vYJambQVvqKCHyhmagNxUv4Yd3uiw6Yzb1oTZ2` |
| Solana fee-payer | `EvJZ4f2AUy6BJihdP4cj3EsDaunA9RaDUpWg4nGemqHk` |
| Advertised Solana payout sender (`extensions.earn.info.payoutWallets.solana`) | `AxTmZFN3pMwFSZDTK3WkJ5fAZLCoTdBS5ZqxjMkgS34w` |

## What was not done

- No draft submitted on 235–240.
- No paid `get_ticket_context` / `draft_reply` / `propose_resolution`.
- No invented extra boards, tenants, or ticket IDs.
- No assumption that Base/Polygon/Sei/Avalanche USDC can be received as Solana USDC.
- No wallet balance claimed.

Re-run: `curl -sS https://deskcrew.io/api/arena/contests` and keep only rows with `payoutNetwork === "solana"` and `ticketId !== 239`.
