# Solana USDC receipt generator

Offline, single-file receipt generator. Open `index.html` in a browser — no server, no build, no network.

## Defaults

| Field | Value |
|---|---|
| Amount | **9 USDC** |
| Pay to | `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3` |
| Network | Solana |
| Token | Circle USDC (`EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v`) |

## Use

1. Open `tools/receipt/index.html`.
2. Confirm **Amount** (defaults to 9 USDC).
3. Enter **Payer** (name or wallet).
4. Optionally enter a **Memo**.
5. Review the live receipt on the right.
6. Click **Download HTML receipt**. The file is a standalone, printable HTML receipt with the same fields plus a Solana Pay URI.

**Copy pay-to** copies the default Solana address.

## Notes

- Payer is required before download. Amount must be greater than 0.
- User-supplied text is escaped in both the preview and the downloaded file.
- The receipt documents the intended transfer. It does not prove on-chain settlement.
