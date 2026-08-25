# USDC tip jar

One HTML file. **9 USDC** on Solana. QR plus copy-address. Offline. No account.

Open `index.html` in a browser. Scan the QR with Phantom (or any Solana Pay wallet), or copy the address and send **exactly 9 USDC**. Not SOL.

## Pay-to

Hardcoded receive address:

`96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3`

Token: Circle native USDC on Solana mainnet.

Mint: `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v`

The QR is a [Solana Pay](https://docs.solanapay.com/spec) transfer request:

`solana:<pay-to>?amount=9&spl-token=<USDC mint>&label=USDC tip jar&message=9 USDC`

No extra wallet addresses are generated. There is no `reference` keypair.

## Sell this file

On the page, paste **your** Solana address and download `tip-jar.html`. That copy has your address baked in as pay-to (same 9 USDC amount, same mint). Leave the field empty to download a copy of this page’s address.

The downloaded file is still a single HTML file. It works offline after save.

## Notes

- No wallet connect and no server.
- Copy uses the browser clipboard when available.
- Do not send SOL. The QR asks for USDC.
