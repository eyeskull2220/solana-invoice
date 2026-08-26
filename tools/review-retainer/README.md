# Belgian local-shop Review-and-follow-up retainer

**199 USDC setup** (one-shot) + **199 USDC/month** done-for-you labor. Solana USDC only. Copy-address. Static HTML a buyer opens offline.

This is **not** a QR dump and **not** a self-serve SaaS. [Reviewi.be](https://reviewi.be/) already sells QR/review self-serve cheaper. The setup files land first (review link, mailto drafts, ICS, counter QR). The **monthly is agent labor** after that: weekly Google review scan, draft replies, one-page report.

We **do not** auto-post to Google. We draft replies; the shop owner posts. There is **no** Google API, OAuth, or scraping in this pack — placeholders and worksheets only.

Pay-to (USDC on Solana, exactly this address):

```
96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3
```

USDC only. Not SOL, not Base, not ETH, not XRP.

USDC mint: `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v`

Optional memos: `review-setup-199` (setup) · `review-monthly-199` (retainer).

## What you get

| File | Role |
|---|---|
| [index.html](index.html) | Shop / sell page for Surge. 199 setup + 199/mo, copy-address |
| [review-link.html](review-link.html) | Customer page + Place ID / review-URL worksheet |
| [follow-up.html](follow-up.html) | After-visit mailto drafts (NL + short FR) |
| [qr.html](qr.html) | Counter QR of the Google review URL (client-side, no API key) |
| [qrcode.js](qrcode.js) | Vendored QR library for `qr.html` (offline) |
| [reminder.html](reminder.html) | Weekly reminder page + download |
| [reminder.ics](reminder.ics) | Monday 09:00 Europe/Brussels, repeating |
| [weekly-report.html](weekly-report.html) | One-page report template + draft-reply worksheet |
| [HANDOFF.html](HANDOFF.html) | After monthly is paid: we scan / draft / report each week |
| [pack.css](pack.css) | Shared styles |

Public kit is generic. Dutch is primary. French is a short optional block on the mail drafts only.

## Prices

| Item | Amount | What it is |
|---|---|---|
| Setup | **199 USDC** one-shot | The files in this folder |
| Monthly | **199 USDC/month** | Done-for-you labor: weekly scan, draft replies, one-page report |

Labor does **not** start on setup alone. It starts after the monthly 199 USDC is paid. See [HANDOFF.html](HANDOFF.html).

## What this pack is not

- Not a QR sticker dump. Not Reviewi.be. Not a login product.
- Not auto-posting to Google. The owner copies the draft and posts.
- Not Google API, OAuth, Maps scraping, or a review database.
- Not SOL / ETH / Base / XRP. No wallet connect.
- Not the leftover 9 USDC Solana Invoice restack.

## Demo shop only

Bakkerij Noord · `hello@bakkerij.example` (RFC 2606). No Gmail. No real inboxes. No named Belgian buyers.

## Surge

`index.html` in this folder is the shop page. Host the folder as-is.
