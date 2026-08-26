# PII / secrets scan — dual-invoice-desk

**Overall: PASS**

Scanned 2026-08-26. Method: read the three files under `tools/dual-invoice-desk/`, strip the bundled QR encoder before wallet-shape matching, then regex for keys / seeds / tokens / passwords / emails / phones / street addresses / extra wallets / invented KBO-BTW digit shapes. Also `node tools/dual-invoice-desk/verify.mjs`.

| | |
|---|---|
| Verdict | **PASS** — no keys, seeds, tokens, passwords, phone numbers, home addresses, emails, or invented KBO/BTW digits |
| Wallet connect / SIWE | **Absent as a flow.** Copy only mentions them to forbid them. |
| Document stamp | **OFFERTE** — not a Belgian legal-invoice stamp |
| KBO/BTW | Exact line `KBO/BTW: nog niet toegekend` only |
| Peppol | Denied: Not Peppol. Not an Access Point. |

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

Document number `INV-20260826` is a matching / memo id, not personal data. Amount is 490 USDC. Visible stamp is OFFERTE.

## Files

| Path | Role |
|---|---|
| `index.html` | Offerte desk (QR encoder + page) |
| `README.md` | Price, pay-to, Solana Pay URL, compliance lines |
| `verify.mjs` | Assertions + PII regex |

**Flagged:** none.

**Reviewed, not flagged:**

- Footer and README say “No wallet connect” / “No SIWE” / “Not Peppol” / “Not an Access Point” as prohibitions.
- `verify.mjs` contains the strings `tel:` and `SIWE` inside the scanner patterns, and regexes that reject Belgian enterprise-number digit shapes without printing a placeholder number.
- Bundled QR encoder is the same davidshimjs library already used by `solana-invoice.html`. It is not a wallet and holds no addresses of its own.
- No Solana Pay `reference=` parameter (that would mint a third keypair).
- No IBAN field. Product HTML does not mention Phantom.
- Emails: none. If any were added, only generic `*.example` would be allowed.

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
| Belgian KBO/BTW digit shapes (`BE` + 10 digits, dotted enterprise-number groups) | None |
| IBAN field / Phantom in a bank field | None |
| Peppol compliance claim / Access Point claim | None (denials only) |

## SHA-256

| File | SHA-256 |
|---|---|
| `index.html` | `6a847efe9e8ff1b5f113182f6cdcf97919fc8d3daf194e92f9cd3e54a1796a6e` |
| `README.md` | `aab98a9201235e62debb99b182ec852d2cf80bff1996b1566b71b1270a3064e7` |
| `verify.mjs` | `6f7049471f7d0348819e771161e1064e42881e0a677dc1f7c287445ac6e0f8c2` |
