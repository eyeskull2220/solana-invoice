# Solana Pay USDC invoice URLs

Date: **2026-08-26**

Transfer-request URLs for five USDC invoices to the public treasury address already on the pay page. Built by [`solana-pay-urls.js`](../solana-pay-urls.js). Print them with `node solana-pay-urls.js`. Check them with `node solana-pay-urls.test.js`.

These are **Solana Pay transfer requests** (`solana:<recipient>?…`). They are not Helio / MoonPay Commerce checkouts, not wallet-connect sessions, and not native SOL transfers.

## Pay-to (do not invent or replace)

| Field | Value |
| --- | --- |
| Recipient (Solana USDC) | `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3` |
| Token mint (Circle USDC on Solana) | `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v` |
| Network | Solana |
| Asset | USDC |
| Scheme | `solana:` transfer request ([spec](https://docs.solanapay.com/spec)) |

The recipient is the same string as `window.TREASURY.solanaAddress` in `config.js`. No second address. No EVM / Base string. Amount is Solana Pay **ui amount** (249 USDC, not raw 6-decimal units).

## Invoice URLs

Open in a Solana Pay wallet (or encode as a QR). Copy-address still works if the wallet does not handle `solana:`.

### 249 USDC

```
solana:96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3?amount=249&spl-token=EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v&label=Solana%20Invoice&memo=invoice-249-2026-08-26
```

### 299 USDC

```
solana:96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3?amount=299&spl-token=EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v&label=Solana%20Invoice&memo=invoice-299-2026-08-26
```

### 399 USDC

```
solana:96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3?amount=399&spl-token=EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v&label=Solana%20Invoice&memo=invoice-399-2026-08-26
```

### 490 USDC

```
solana:96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3?amount=490&spl-token=EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v&label=Solana%20Invoice&memo=invoice-490-2026-08-26
```

### 900 USDC

```
solana:96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3?amount=900&spl-token=EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v&label=Solana%20Invoice&memo=invoice-900-2026-08-26
```

## Builder

```js
var pay = require("./solana-pay-urls.js");
pay.builders[249]();
pay.buildUsdcInvoiceUrl(399);
pay.buildAllInvoiceUrls();
```

Only `249`, `299`, `399`, `490`, and `900` are accepted. The recipient is a constant; the builder does not take another address.

Query fields (Solana Pay transfer request):

| Param | Role |
| --- | --- |
| `amount` | USDC ui amount |
| `spl-token` | USDC mint (required so this is not a SOL transfer) |
| `label` | `Solana Invoice` |
| `memo` | `invoice-<amount>-2026-08-26` (on-chain SPL Memo; not private) |

No `reference` key is generated. No HTTPS `solana:https://…` transaction request (that path is how hosted checkouts such as Helio work).

## Out of scope

- Helio, MoonPay Commerce, or any hosted pay link
- Wallet-connect (`wc:`)
- Invented receive addresses
- SOL, XRP, ETH, Base USDC
- Changing `index.html`, `catalog.html`, or the one-file invoice product

## PII scan (2026-08-26)

Scanned `solana-pay-urls.js`, `solana-pay-urls.test.js`, and this file.

| Check | Result |
| --- | --- |
| Email / Gmail | none |
| Phone | none |
| Home address / personal name | none |
| Seed / private key | none |
| Extra Solana addresses | none — only treasury + USDC mint |
| EVM `0x` address | none |
| Helio / wallet-connect in builders | none |

Memos are amount + date only. Do not put a client name, mail, or invoice narrative in the `memo` field (validators record it).
