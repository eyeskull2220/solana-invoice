# WALLET seat

Receive-only treasury watch. Phantom listed addresses only. No spend. No trade. No Helio. No sales USDC to Kraken.

**Stamp:** operator page, not a FACTUUR.  
**Date:** 2026-08-27  
**Mode:** watch listed Phantom receive strings. Confirm pay-proofs. Keep File-1.

Do not invent a third address, a PDA, an embedded Helio wallet, a CDP EOA, a seed, or an IBAN.

## Watched addresses (do not invent)

These two strings are the only receive destinations this seat watches. Copy them. Do not generate replacements.

| Rail | Role | Address | Asset this seat counts |
|---|---|---|---|
| Solana | Phantom USDC receive | `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3` | native USDC mint `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v` |
| Base | Phantom USDC receive | `0x9eb954b567ef3616424a6e1bf42c63724930aa54` | native USDC `0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913` |

Mints/contracts above are token identifiers, not pay-to. Catalog payments are **USDC only** — not SOL, not ETH, not XRP, not USDT, not USDC.e.

A Phantom MCP session address is **not** a treasury. Do not publish it. Do not watch it as inbound.

## Snapshot — 2026-08-27 20:56

Operator snapshot: **0 SOL / 0 USDC**.

RPC re-check from this seat (read-only, no send):

| Rail | Check | Result |
|---|---|---|
| Solana `api.mainnet-beta.solana.com` | `getBalance` | `0` lamports |
| Solana | `getTokenAccountsByOwner` (USDC mint) | `[]` — no USDC ATA yet |
| Solana | `getSignaturesForAddress` (limit 5) | `[]` |
| Base `base-rpc.publicnode.com` | `eth_getBalance` | `0x0` |
| Base | USDC `balanceOf` | `0x0` |

Zero is a valid watch result. Zero is not an inbound. Do not invent a fill to make the ledger look busy.

## Inventory of read tools

### Allowed — treasury watch (listed addresses)

Public JSON-RPC. This is the inbound watch, not the MCP session.

| Tool | Use |
|---|---|
| Solana `getBalance` | Native SOL on `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3`. Catalog does not bill in SOL. |
| Solana `getTokenAccountsByOwner` | USDC ATA for mint `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v`. Empty array = no USDC account yet. |
| Solana `getSignaturesForAddress` | New signatures since last 08:00 / 16:00. |
| Solana `getTransaction` (`jsonParsed`, `maxSupportedTransactionVersion: 0`) | Pay-proof confirm: `meta.err` empty + USDC token-delta to the listed owner. |
| Base `eth_getBalance` | Native ETH on `0x9eb954b567ef3616424a6e1bf42c63724930aa54`. Not a catalog asset. |
| Base `eth_call` `balanceOf` | Native USDC `0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913`. |
| Base `eth_getTransactionReceipt` | Pay-proof confirm on the Base rail. |
| Explorers (Solscan / Basescan) | Human read. File-1 stores **last-6** of the tx id only. |

Working public nodes from this seat: `https://api.mainnet-beta.solana.com`, `https://solana-rpc.publicnode.com`, `https://base-rpc.publicnode.com`.

Failed from this seat (do not treat as zero): `https://mainnet.base.org` HTTP 403, `https://base.llamarpc.com` 403, `https://1rpc.io/base` 403, `https://rpc.ankr.com/base` unauthorized.

### Allowed — Phantom MCP read (session only)

Use to see whether a Phantom session exists. **Do not** treat session balances as File-1 inbound to the listed treasuries.

| Tool | Use | Do not |
|---|---|---|
| `wallet_status` | Session present? Timeout ≠ balance. This seat’s status call timed out; that is not 0 USDC. | Do not page, spend, or invent inbound from a timeout. |
| `wallet_addresses` | Confirm a session, then **discard**. | Do not publish. Not a third treasury. |
| `wallet_balances` | Session balances, if needed to explain a mismatch. | Do not copy into File-1 as listed-treasury inbound. |
| `price` | USD mark for SOL/USDC. | Not a tax figure. Not `eur_mid`. |
| `simulate` | Preview only. | Never follow with `confirmed: true` / send. |
| `evm_allowance` | Read an allowance if asked. | This seat has no spender to approve. |

### Read but banned on this seat (do not trade)

`perps_account`, `perps_history`, `perps_markets`, `perps_orders`, `perps_positions`, `wallet_rebalance` (`analyze` included), `buy` even with `execute: false`. Perps/Hyperliquid are out of scope even when they mention USDC.

### Spend / write — see BLOCKED

`buy` `execute: true`, `transfer`, `pay`, `solana_send`, `solana_sign`, `evm_send`, `evm_sign`, `evm_sign-typed`, `wallet_rebalance` `execute`, `perps_open`, `perps_close`, `perps_cancel`, `perps_deposit`, `perps_withdraw`, `perps_withdraw-hl-spot`, `perps_transfer`, `perps_leverage`.

Kraken MCP discovery failed in this environment. Even when it is up: **no sales USDC to Kraken**.

## 10 miss-inbound failures

Ways this seat can miss a real inbound, or book a fake one. Each is a fail.

1. **MCP session ≠ listed treasury.** `wallet_balances` / `wallet_addresses` read the Phantom MCP embedded wallet. Inbound to `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3` or `0x9eb954b567ef3616424a6e1bf42c63724930aa54` does not show there. Watch the listed strings on public RPC.
2. **Native SOL mistaken for USDC.** `getBalance` is lamports. Catalog SKUs are USDC. SOL dust is not a 9 / 49 / 490 payment. USDC lives on the token account, not in the SOL balance.
3. **Wrong chain.** SPL USDC sent to the Base `0x…`, or Base ERC-20 sent to the Solana string. Those transfers do not land. File-1 stays quiet until a matching-rail proof exists.
4. **Wrong mint.** USDT, USDC.e, wrapped SOL, or a CCTP mint on a third chain. Count only Solana mint `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v` and Base native USDC `0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913`.
5. **RPC 403 / timeout booked as zero.** A failed node is not quiet-if-zero. Retry a working public node. Do not write File-1 amount `0` from a 403. Do not invent an inbound from a timeout.
6. **Skipped token accounts.** `getBalance == 0` plus skipped `getTokenAccountsByOwner` misses the first USDC inbound (it creates the ATA). Empty `[]` is “no USDC account yet,” not “RPC said SOL is zero so skip USDC.”
7. **Helio “paid” is not inbound.** This seat does not use Helio / MoonPay Commerce. A hosted pay-link dashboard is not File-1. Funds that sit with Helio until a payout wallet is linked have not landed on the listed Phantom addresses.
8. **Kraken credit is not treasury inbound.** Sales USDC to Kraken is banned. A Kraken deposit, trade fill, or DCA slice is not Phantom receive. Do not copy Kraken into File-1.
9. **Pay-proof without RPC confirm.** A pasted signature, a chat screenshot, or the pay-page `honorUnlock` fallback is not confirmed. Confirm with `getTransaction` / receipt: no `meta.err`, USDC token-delta (or ERC-20 transfer) to the listed address, amount matches the SKU. Then File-1 `proof=confirmed` and `tx_last6` only.
10. **Fiat / Revolut / IBAN row.** Revolut is **denied**. No full IBAN. No last-4 until KYC. An EUR bank credit is not USDC inbound. Do not add bank columns to File-1.

## STARTABLE

These three may run now. They do not spend.

### 1. File-1

Keep [`FILE-1-LEDGER.md`](FILE-1-LEDGER.md). Stamp **VOORBEELD**. Header only plus the zero snapshot until a pay-proof confirms. No IBAN. No last-4. No seeds.

### 2. Weekday 16:00 RPC quiet-if-zero

Europe/Brussels, Monday–Friday, 16:00.

1. Solana: `getBalance` + `getTokenAccountsByOwner` (USDC) + `getSignaturesForAddress`.
2. Base: `eth_getBalance` + USDC `balanceOf` on a node that did not 403.
3. If SOL = 0, USDC = 0 on both rails, and no new signatures: **stay quiet**. Do not page. Optional File-1 line with `proof=quiet-if-zero`.
4. If RPC failed: not quiet. Log the fail. Retry. Do not invent 0 or invent inbound.
5. If non-zero: do not spend. Run pay-proof confirm, then File-1.

Quiet-if-zero is not permission to skip 08:00.

### 3. Pay-proof confirm

When a signature or tx hash is pasted:

1. Reject if it does not look like a Solana signature or a `0x` hash.
2. Fetch via allowed RPC (not Helio, not Kraken).
3. Confirm destination is one of the two listed addresses, asset is native USDC on that rail, `err` empty, amount matches the claimed SKU.
4. Write File-1: `proof=confirmed`, `tx_last6` only, no full hash, no names, no email.
5. If ambiguous (timeout, parse error, missing token-delta): `proof=ambiguous`. Do not treat as paid. Do not resend anything — this seat does not send.

## BLOCKED

| Item | Why |
|---|---|
| **Spend** | No transfer, swap, pay, sign-and-send, rebalance execute, perps, or fee-payer. Treasury does not sign. |
| **IBAN** | Revolut denied. No full IBAN. No last-4 until KYC. Wallet strings are not `PayeeFinancialAccount`. |
| **Live** | No live trade, no Helio go-live, no sales USDC to Kraken, no perps, no live DCA. Paper elsewhere is not this seat. |

Also blocked: new keys, SIWE as a pay step, a third receive address, stuffing Phantom into a bank field.

## 08:00 still required

Daily **08:00 Europe/Brussels**, including weekends and including days that already ran 16:00 quiet-if-zero.

Same RPC reads as 16:00. Zero is an allowed outcome. **Skipping the check is not.** Spend-blocked does not cancel 08:00. IBAN-blocked does not cancel 08:00. Live-blocked does not cancel 08:00.

If 08:00 RPC fails, retry; do not wait for 16:00 to notice a missed inbound.

## Hard bans (repeat)

- Do not invent addresses.
- Do not spend.
- Do not trade.
- Do not use Helio.
- Do not sell USDC to Kraken.
- Revolut denied — no full IBAN, no last-4 until KYC.
- No seeds, mnemonics, or private keys in this repo or in File-1.
