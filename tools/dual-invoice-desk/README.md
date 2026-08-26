# Dual-chain USDC offerte desk

One document number. **490 USDC**. Pay on **Solana** (Solana Pay URL + QR) or **Base** (copy card). Open `index.html` in a browser. Offline. No account.

The visible stamp is **OFFERTE**. Until a real KBO exists, print OFFERTE or VOORBEELD only — never a Belgian legal-invoice stamp.

## Offerte

| Field | Value |
|---|---|
| Document number | **INV-20260826** (memo / matching id — not a legal-invoice stamp) |
| Stamp | **OFFERTE** |
| KBO/BTW | **KBO/BTW: nog niet toegekend** (exact line; no enterprise number) |
| Issued | 26 August 2026 |
| Due | On receipt |
| Amount | **490 USDC** (pay once — Solana *or* Base, not both) |

## Pay-to (two addresses only)

Do not invent a third receive address. There is no Solana Pay `reference` keypair. There is no IBAN field. Do not put a wallet name in a bank field.

| Rail | Receive address | How to pay |
|---|---|---|
| Solana | `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3` | Scan QR or copy Solana Pay URL |
| Base | `0x9eb954b567ef3616424a6e1bf42c63724930aa54` | Copy address, send native USDC |

## Token identifiers (not pay-to)

These are Circle native USDC contracts / mints, not extra wallets:

| Chain | Identifier |
|---|---|
| Solana USDC mint | `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v` |
| Base USDC | `0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913` (chain id 8453, 6 decimals) |

Solana Pay URL (no `reference`):

`solana:96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3?amount=490&spl-token=EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v&memo=INV-20260826&label=Dual-chain%20USDC%20offerte`

## What this page does not do

- No Belgian legal-invoice document stamp (OFFERTE or VOORBEELD only until a real KBO exists)
- No invented KBO/BTW digits — only the exact line `KBO/BTW: nog niet toegekend`
- No IBAN field
- Not Peppol. Not an Access Point. No Peppol compliance claim
- No wallet connect
- No SIWE
- No Phantom SDK
- No wallet-connect protocol
- No form fields for names, emails, or phones
- Emails, if any were added later, must be generic `*.example` only

## Check

```bash
node tools/dual-invoice-desk/verify.mjs
```
