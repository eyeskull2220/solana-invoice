# Paywall stub

Copyable one-file gate for the other treasury HTML tools.

- **Price:** 9 USDC
- **Network:** Solana
- **Token:** USDC (`EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v`)
- **Pay to:** `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3`
- **Unlock:** paste a transaction signature (or a Solscan / Explorer URL)
- **No wallet connect.** Honor-system paste-tx.

Open `index.html` in a browser. Pay, paste the signature, the `#product` block appears.

## Copy into another tool

1. Copy `index.html`.
2. Replace the inner HTML of `#product` with your tool.
3. If the tool is not 9 USDC, change `CONFIG` only:

```js
priceUsdc: 49,
expectedRaw: "49000000", // price × 10^6
storageKey: "pw-unlock:<payTo>:<price>"
```

Leave `payTo` and `usdcMint` as they are.

Classes are prefixed `pw-` so they do not collide with the tool CSS.

## Loose verify

A paste unlocks if it looks like a Solana signature (base58, 86–88 chars).

Then, if a public RPC answers:

- **Found, and it is 9 USDC to the pay-to address** → unlock (verified)
- **Found, but it is not that payment** → stay locked
- **RPC error / tx not found / CORS** → unlock anyway (honor system)

That last path is intentional. Missing a paid user is worse than a determined skip; do not turn this into a hard on-chain checkout.

Persisted in `localStorage` under `CONFIG.storageKey` so a refresh stays unlocked on the same browser.

## What this is not

- Not Phantom Connect
- Not Solana Pay confirmation polling
- Not a backend
- Not XRP / other chains — USDC on Solana only
