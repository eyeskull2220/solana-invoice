# PII / secrets scan — dual-invoice-desk

**Overall: PASS**

Scanned 2026-08-26. Method: read the three files under `tools/dual-invoice-desk/`, strip the bundled QR encoder before wallet-shape matching, then regex for keys / seeds / tokens / passwords / emails / phones / street addresses / extra wallets. Also `node tools/dual-invoice-desk/verify.mjs`.

| | |
|---|---|
| Verdict | **PASS** — no keys, seeds, tokens, passwords, phone numbers, home addresses, or emails |
| Wallet connect / SIWE | **Absent as a flow.** Copy only mentions them to forbid them. |

## Allowlist

Receive addresses (two only — do not invent a third):

| Chain | Address | Role |
|---|---|---|
| Solana | `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3` | Pay-to |
| Base | `0x9eb954b567ef3616424a6e1bf42c63724930aa54` | Pay-to |

Public token identifiers (not pay-to, not extra wallets):

| Chain | Identifier |
|---|---|
| Solana USDC mint | `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v` |
| Base USDC | `0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913` |

Invoice number `INV-20260826` is a business id, not personal data. Amount is 490 USDC.

## Files

| Path | Role |
|---|---|
| `index.html` | Invoice desk (QR encoder + page) |
| `README.md` | Price, pay-to, Solana Pay URL |
| `verify.mjs` | Assertions + PII regex |

**Flagged:** none.

**Reviewed, not flagged:**

- Footer and README say “No wallet connect” / “No SIWE” as prohibitions.
- `verify.mjs` contains the strings `tel:` and `SIWE` inside the scanner patterns.
- Bundled QR encoder is the same davidshimjs library already used by `solana-invoice.html`. It is not a wallet and holds no addresses of its own.
- No Solana Pay `reference=` parameter (that would mint a third keypair).

## What was searched for

| Class | Result |
|---|---|
| PEM / PKCS8 private keys, Solana secret-key arrays, 64-byte hex privkeys | None |
| BIP-39 / seed phrase / mnemonic / recovery phrase | None |
| API tokens (`sk-`, `sk_live_`, `ghp_`, `xoxb-`, `AKIA…`, JWTs) | None |
| Passwords | None |
| Emails | None |
| Phone numbers / `tel:` hrefs | None in the desk; scanner source only |
| Street / home addresses | None |
| Unexpected wallets (base58 32–44 or `0x` + 40 hex other than allowlist + token ids) | None |
| wallet-connect protocol / SIWE / `ethereum.request` / `window.ethereum` / Phantom SDK | None as a flow |

## SHA-256

| File | SHA-256 |
|---|---|
| `index.html` | `c7919fa0ee6e795aec6c9295bac3eecb9e1db17836db8f9ea249199f93745554` |
| `README.md` | `b3788ea153ed825edef5aa0f5c6eb67e083e1f9a2b2393611c004c58307b03a4` |
| `verify.mjs` | `64b3030ad3169a5b435ffaf20f7996eb5015212aacabbab2b0df1aa8e8cbacae` |
