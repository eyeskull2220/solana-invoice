# Solana Pay USDC invoice URLs

Date: **2026-08-26**

Wallet-drafted **transfer requests** (`solana:<recipient>?…`) for the live invoice amounts. Pay-to is the public treasury address already on the pay page. Not Helio. Not wallet-connect. No second address.

## Pay-to (do not invent or replace)

| Field | Value |
| --- | --- |
| Recipient | `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3` |
| USDC mint | `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v` |
| Network / asset | Solana / USDC |
| Spec | [Solana Pay transfer request](https://docs.solanapay.com/spec) |

Same string as `window.TREASURY.solanaAddress` in `config.js`. Amount is ui amount (not raw 6-decimal units). `spl-token` is required so this is not a SOL transfer.

## Invoice URLs

Same construction as `solanaPayUrl` in `solana-invoice.html`: recipient + `amount` + `spl-token`. Memo only where two invoices share an amount.

### 199 USDC

```
solana:96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3?amount=199&spl-token=EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v
```

### 249 USDC

```
solana:96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3?amount=249&spl-token=EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v
```

### 299 USDC

```
solana:96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3?amount=299&spl-token=EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v
```

### 399 USDC — pipeline

```
solana:96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3?amount=399&spl-token=EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v&memo=pipeline
```

### 399 USDC — peppol-chase

```
solana:96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3?amount=399&spl-token=EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v&memo=peppol-chase
```

### 490 USDC

```
solana:96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3?amount=490&spl-token=EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v
```

### 900 USDC

```
solana:96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3?amount=900&spl-token=EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v
```

Builders that emit these strings: [`solana-pay-urls.js`](../solana-pay-urls.js). `node solana-pay-urls.js` prints them.

## Out of scope

- Helio / MoonPay Commerce hosted checkouts
- Wallet-connect (`wc:`)
- Invented receive addresses or extra amounts
- SOL, XRP, ETH, Base USDC
- HTTPS `solana:https://…` transaction requests
