# 01 — Adversarial research (Wallet)

**Seat:** Wallet
**Lens:** adversarial **first**, then RED / YELLOW / GREEN. Research only. Not a FIX. Not a spend.
**Date:** 2026-08-27
**Stamp:** VOORBEELD · receive-only · not FACTUUR · not INVOICE · not a sale
**HEAD (this repo):** `2170952`
**File-1:** header only. First row **0/0 is valid.**

This file researches the Wallet desk: Phantom public **0 SOL / 0 USDC**, two named pay-tos, inbound ledger empty. It does not send, swap, rebalance, open perps, print a seed, print a full IBAN, invent a third receive address, rewrite shop HTML, or log a fake inbound.

---

## Live desk (this sitting)

| Surface | Finding |
| --- | --- |
| Phantom public | **0 SOL / 0 USDC.** Stamp, not a sale. Agent wallets start empty ([Phantom MCP account types](https://docs.phantom.com/phantom-mcp-server/account-types)). |
| Phantom MCP `wallet_addresses` / `wallet_balances` | **Timed out** twice this run. Did **not** send to test. Did **not** call `buy` / `wallet_rebalance` / `solana_send`. |
| File-1 | **Header only.** No inbound row. A first data row of **0/0** (SOL / USDC, or `usdc_in=0`) is **valid**. Empty is not a parse error. |
| Pay-to Solana | `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3` |
| Pay-to Base | `0x9eb954b567ef3616424a6e1bf42c63724930aa54` |
| Third pay-to | **None.** Never invent one. |

Public RPC (read-only, 2026-08-27, Solana slot ~442169910 / ~442170162):

| Rail | Call | Result |
| --- | --- | --- |
| Solana pay-to | `getBalance` | **0** lamports |
| Solana pay-to | `getAccountInfo` | **null** (account not created; still a valid pubkey) |
| Solana pay-to | `getTokenAccountsByOwner` mint `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v` | **[]** → **0 USDC** (no ATA is 0, not “missing data”) |
| Base pay-to | `eth_getBalance` | `0x0` ETH |
| Base pay-to | `eth_getCode` | `0x` (EOA, not a contract) |
| Base pay-to | `eth_getTransactionCount` | `0x0` (never sent) |
| Base pay-to | `balanceOf` native USDC `0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913` | **0** |

Inbound USDC on either pay-to: **0**. Phantom public 0/0 and File-1 header-only / first-row 0/0 **agree**. Do not “fix” the zero.

Official Circle mainnet USDC ([contract addresses](https://developers.circle.com/stablecoins/usdc-contract-addresses)):

| Chain | Native USDC |
| --- | --- |
| Solana | `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v` |
| Base | `0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913` |

Those are **mints**, not a third pay-to.

---

## Adversarial first

Attacks that would fake a funded Wallet, a third rail, or a sale. Each is a **stop**, not a note to bargain.

1. **Treat File-1 header-only or first row 0/0 as broken.** Empty inbound is the true state. A header with no data rows is valid. A first row of 0 SOL / 0 USDC (or `usdc_in=0`) is valid. Do not invent a payer, offerte, signature, or positive `usdc_in` so the CSV “looks used.”

2. **Treat Phantom 0/0 as a defect that requires a send.** Phantom docs: the agent wallet **starts at zero**. Public 0 SOL / 0 USDC is a **stamp**. Sending “to test connectivity,” to create the Solana account, to open an ATA, or to get a nonce on Base is **spend**. Forbidden.

3. **Invent a third pay-to.** Phantom MCP returns Solana, Ethereum, Bitcoin, and Sui addresses. The Ethereum string is the EVM key used on Base **and** Ethereum mainnet — it is **not** treasury. Bitcoin and Sui are **not** pay-tos. Sui output is deprecated 2026-09-24. A Solana Pay `reference`, facilitator gas key, CDP wallet, Helio email-embedded wallet, MCP session address, or EIP-55 recasing of the Base pay-to is **not** a new treasury. Count remains **two**.

4. **Spend, swap, rebalance, or open perps.** `buy` (even quote-then-execute), `wallet_rebalance`, `solana_send` with `confirmed: true`, CCTP burn/mint, Circle Gateway, bridges. Research is read-only. Missing USDC is recoverable later; a duplicate outbound is not this seat’s job.

5. **Print a full IBAN / Peppol `PayeeFinancialAccount`.** Wallet rails are the two USDC strings. Do not put either string in an IBAN field. Do not invent BE/NL IBAN, Bancontact, or Revolut-X fiat as a receive path. Kraken MCP on this run: **error / undiscoverable** — not a reason to fall back to bank rails.

6. **Confuse Phantom agent wallet with the two pay-tos.** Agent wallet ≠ personal Phantom ≠ treasury. Funding the agent later does not change the pay-to list. Do not replace `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3` or `0x9eb954b567ef3616424a6e1bf42c63724930aa54` with whatever `wallet_addresses` returns.

7. **Bill native SOL / ETH, or XRP.** Shop leftover copy is USDC on Solana, not SOL. Base rail is **USDC**, not ETH for gas-as-product. Do not take XRP. Do not treat 0 lamports / 0 wei as “wrong asset, send native.”

8. **Use Ethereum mainnet USDC, or bridged USDC on Base.** Ethereum USDC `0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48` on the Base pay-to is the wrong token. Bridged USDC.e is the wrong token. Native Base USDC is `0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913` only.

9. **Rewrite File-1 EXAMPLE / 0 into income.** Sibling Wallet FIX (#128) proposed `FILE-1.csv` with one EXAMPLE row, `usdc_in=0`. That row is **not** a customer. This 01 does not merge that CSV and does not upgrade EXAMPLE into a sale.

10. **Fetch or bake a USDC→EUR mid into the ledger.** `eur_note` is an operator note, not FX, not tax, not CAP. Compliance books EUR after KBO. This file does not invent a rate.

11. **Send to create the Solana account / ATA.** `getAccountInfo` null and empty token-accounts mean **unfunded**, not invalid. Rent-exempt creation and ATA init are **spend**. Leave them.

12. **Collapse Wallet into Scout mail, shop HTML, or Coder paper.** Leftover `index.html` / README list the Solana string only. That is not permission to drop Base, and not permission for this research to patch the shop. Do not mail the pay-tos. Do not fund Kraken from treasury.

13. **Print a seed, private key, or `CDP_WALLET_SECRET`.** Receive-only. No new key.

14. **Treat MCP timeout as “balances unknown, therefore maybe funded.”** Timeout ≠ funds. Operator stamp is 0/0. Public RPC on both pay-tos is 0/0. Do not assume hidden SOL/USDC. Do not retry with a transfer.

15. **Add a spend column, outbound ledger, or “test withdraw.”** File-1 is inbound. Outbound is out of scope. No spend.

---

## Verdict: **GREEN** (0/0 valid · two rails · no spend) · **RED** (fake inbound / third rail / IBAN / spend)

File-1 header-only and Phantom public 0/0 are **not** RED defects. They are the desk. Promotion of a sale, a third address, a bank rail, or a test send: **RED**.

| Probe | Result | Color |
| --- | --- | --- |
| File-1 header only / first row 0/0 | Valid empty inbound. Not a parse fail. Not a sale | **GREEN** |
| Phantom public 0 SOL / 0 USDC | Stamp matches pay-to RPC zeros | **GREEN** |
| Pay-tos count | Exactly two (Solana + Base). No third written | **GREEN** |
| Solana pay-to live | 0 lamports, no account, no USDC ATA | **GREEN** (zero) |
| Base pay-to live | EOA, nonce 0, 0 ETH, 0 native USDC | **GREEN** (zero) |
| Native USDC mints | Circle Solana + Base mainnet, not a third address | **GREEN** |
| Spend / swap / rebalance / perps this run | None | **GREEN** |
| Full IBAN / Peppol wallet-as-IBAN | None printed | **GREEN** |
| Phantom MCP live read | Timed out; did not send to test | **YELLOW** |
| Leftover shop HTML vs two Wallet rails | `index.html` / README Solana-only; Base is Wallet-only | **YELLOW** |
| Sibling #128 EXAMPLE CSV | Compatible 0; not merged here; not income | **YELLOW** |
| Invented inbound / third pay-to / IBAN / spend | Would be fraud on this desk | **RED** if done; **GREEN** that this file does not |
| Treating 0/0 as “must fund the agent” | Forbidden by this research | **RED** as attack |

---

## RED

### R1 — Invented inbound is a fake sale

File-1 has **no** real inbound. Header only is enough. First row 0/0 is enough. A signature, payer, offerte id, or `usdc_in>0` without a chain print is a fabricated receipt. Stop.

### R2 — A third pay-to is a different treasury

Only:

- Solana `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3`
- Base `0x9eb954b567ef3616424a6e1bf42c63724930aa54`

Phantom’s extra address types, Ethereum-mainnet USDC, Bitcoin, Sui, gas keys, Pay references, and checksum theatre are **out**. Adding one “for completeness” splits funds and this seat will not find them.

### R3 — Spend is not research

Any transfer, swap, bridge, rebalance, or perps from this sitting is a Wallet failure even if the amount is dust. Timeout, null account, and empty ATA are **not** licenses to send. 0/0 stays 0/0.

### R4 — IBAN is not a Wallet rail

No full IBAN in this file. No Bancontact. No Peppol `PayeeFinancialAccount` stuffed with a base58 or `0x` string. Shop copy may stay EUR-first; that is not a bank account invented here.

### R5 — 0/0 is not a reason to promote a kit as paid

9 USDC / 49 USDC leftover SKUs in this repo are **not** marked received. Unlock-by-signature on `index.html` is unused. Do not stamp FACTUUR.

---

## YELLOW

### Y1 — Phantom MCP timed out

`wallet_addresses` and `wallet_balances` (Solana + Base) returned MCP **-32001** twice. Public RPC on the **pay-tos** is 0/0. Operator: Phantom public 0/0. A later Wallet seat may retry **read-only** and still must not send. Timeout is not a hidden balance.

### Y2 — Shop leftover lists Solana only

`README.md`, `config.js`, `index.html` pay the Solana string. Wallet still has **Base** as the second pay-to. This 01 does **not** add Base to the shop (Builder / CEO). It also does **not** delete Base from Wallet. Two desks, two jobs.

### Y3 — Sibling FIX #128 is not this file

#128 adds `FILE-1.csv` (header + EXAMPLE 0) and `WALLET-FIX.md`. This research does not implement that ledger, does not conflict with “0 is valid,” and does not treat EXAMPLE as money in. If both merge, keep **one** inbound file, still no spend column, still no third address.

### Y4 — Solana account does not exist yet

`getAccountInfo` null means the pubkey has never been rent-funded. Valid. Do not airdrop. Do not send 0.001 SOL “so it shows on explorers.”

### Y5 — Kraken / Circle product surfaces exist and are unused

Kraken MCP: error. Circle docs used only for **mint addresses**. CCTP / Gateway / developer wallets would be a **third** custody path. Designed out.

---

## GREEN

### G1 — File-1 first row 0/0 is valid

Header-only File-1 is a legal ledger. A first row of 0 SOL / 0 USDC is a legal stamp. Neither requires a backfill. Missing inbound stays missing.

### G2 — Exactly two pay-tos

Solana and Base strings above, copied as given. No third. Mints cited as mints.

### G3 — No spend this run

No `buy`, no `wallet_rebalance`, no `solana_send` confirmed, no CCTP, no Gateway, no IBAN transfer. Read-only RPC + docs + timeouts.

### G4 — Phantom 0/0 matches chain

Agent-wallet empty is the documented default. Pay-tos are empty on public RPC. The two zeros are the same story: nothing inbound.

### G5 — Base pay-to is an unused EOA

`eth_getCode` `0x`, nonce 0. Not a token contract, not a Safe we failed to decode. Receive address as given.

### G6 — Native USDC only, named chains only

Solana mint matches `config.js` / Circle. Base mint is Circle native USDC, not Ethereum USDC and not USDbC.

---

## NOTES

- **Report-only.** No CSV written in this PR. No shop edit. No mail. No Gmail. Sibling Wallet FIX (#128) may own `FILE-1.csv`; this 01 scores the desk.
- **Sources:** operator locks (Phantom public 0/0, File-1 header only, two pay-tos, no spend, no IBAN); Solana `api.mainnet-beta.solana.com`; Base `mainnet.base.org`; Circle USDC mainnet table; Phantom MCP account-types + tools list; leftover `README.md` / `config.js` / `index.html` at `2170952`; sibling #128 / #132 format.
- **File-1 columns (if a later FIX writes the CSV):** `date_brussels, usdc_in, eur_note, solana_sig, payer, what_sold, offerte_id`. No spend column. `EXAMPLE` markers stay EXAMPLE. Real row only after USDC **lands** on one of the two pay-tos.
- **Tax (not advice):** 0 inbound is not beroepsinkomen. Do not invent FIFO. KBO/BTW not in this file.
- **PII:** no mailbox, no full IBAN, no seed. Operator Geel / KBO pending is Compliance, not Wallet.
- Concurrent seats (CEO / Scout / Coder / Compliance / Builder) are not this scoreboard. Do not merge shop HTML or paper fills into a Wallet inbound.

**Sale: no. Spend: no. Third pay-to: no. IBAN: no. File-1 0/0: valid.**

---

## Design-outs

1. **Third pay-to.** No Ethereum mainnet treasury, no Bitcoin, no Sui, no Pay reference, no gas key, no CDP/Helio/MCP session address, no recased Base string as a second Base rail.
2. **Spend.** No send, swap, quote-execute, rebalance, perps, bridge, ATA-create, rent-fund, “test tx.”
3. **IBAN / Bancontact / Peppol wallet field.** Wallet is the two USDC pay-tos. EUR-first shop copy does not mint a bank account here.
4. **File-1 as a sales journal.** Header-only / 0/0 stays empty. No invented payer, offerte, or signature.
5. **Phantom agent address as treasury.** Agent wallet is isolated and empty. Pay-tos stay the two named strings.
6. **Wrong USDC.** No Ethereum-mainnet USDC on Base. No bridged USDC.e. No SPL-not-USDC. No native SOL/ETH as the product.
7. **FX in the ledger.** No fetched USDC→EUR mid. `eur_note` is not tax.
8. **Shop / mail / Coder paper from this file.** Do not patch `index.html`. Do not mail pay-tos. Do not fund Kraken from treasury.
9. **Seeds / new keys.** Receive-only.
10. **This RGY 01 implementing FIX.** Research does not add `FILE-1.csv`. Empty header remains valid without a sibling merge.

---

## Re-check (copy/paste, read-only)

```bash
curl -sS -X POST https://api.mainnet-beta.solana.com -H 'Content-Type: application/json' \
  -d '{"jsonrpc":"2.0","id":1,"method":"getBalance","params":["96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3"]}'
curl -sS -X POST https://api.mainnet-beta.solana.com -H 'Content-Type: application/json' \
  -d '{"jsonrpc":"2.0","id":2,"method":"getTokenAccountsByOwner","params":["96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3",{"mint":"EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v"},{"encoding":"jsonParsed"}]}'
curl -sS -X POST https://mainnet.base.org -H 'Content-Type: application/json' \
  -d '{"jsonrpc":"2.0","id":3,"method":"eth_getBalance","params":["0x9eb954b567ef3616424a6e1bf42c63724930aa54","latest"]}'
curl -sS -X POST https://mainnet.base.org -H 'Content-Type: application/json' \
  -d '{"jsonrpc":"2.0","id":4,"method":"eth_call","params":[{"to":"0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913","data":"0x70a082310000000000000000000000009eb954b567ef3616424a6e1bf42c63724930aa54"},"latest"]}'
```

Expect zeros. Do not send if they are zeros. Count pay-tos: **two**. File-1 first row 0/0 is valid.
