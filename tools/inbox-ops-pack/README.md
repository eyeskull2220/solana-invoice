# Inbox-ops pack

One branded pack: **intake form + invoice + reminder + FAQ**. Demo-branded for a fake freelancer (**Studio Noord**). An agent later rebrands the four working files for one real client.

**299 USDC** on Solana. Not a leftover 9 USDC restack of Solana Invoice / BTW toy. Not a weekly admin seat. Not a Peppol Access Point. Not the 399 USDC lead-to-invoice pipeline.

## Price / pay-to

Send **exactly 299 USDC** on **Solana** (USDC only — not SOL, not Base, not ETH, not XRP) to:

`96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3`

Mint: `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v`

Copy-address only. No wallet connect. Open [`index.html`](index.html) and use **Copy address**.

## Files

| File | Role |
| --- | --- |
| [`index.html`](index.html) | Sell / demo page (299 USDC, copy-address) |
| [`intake.html`](intake.html) | Branded one-job intake. Download a brief or open a `mailto:` draft |
| [`invoice.html`](invoice.html) | Belgian BTW factuur, default **21%**, download standalone HTML |
| [`reminder.html`](reminder.html) | Overdue reminder letter, download standalone HTML |
| [`faq.html`](faq.html) | Client FAQ, including Peppol / PDF rules |
| [`pack.css`](pack.css) | Shared Studio Noord chrome (recolor `:root` when rebranding) |
| [`PII_SCAN.md`](PII_SCAN.md) | Placeholder / PII scan for this folder (2026-08-26) |

Demo studio: **Studio Noord**. Demo client: **Client BV**. Demo mail: **you@studio.example** (RFC 2606). No Gmail. No live company inboxes.

The four working pages share one brand via `pack.css`. Downloaded HTML (intake brief, factuur, reminder) is standalone: no scripts, no treasury address, no pack nav.

## Rebrand for one client

Do this in the four working files (`intake.html`, `invoice.html`, `reminder.html`, `faq.html`) and in `:root` of `pack.css`. Leave the sell-page pay-to as the treasury address unless you are selling the pack itself.

1. Replace **Studio Noord** with the practice name.
2. Replace **Voorbeeldlaan 1, 2000 Antwerpen** with the work address.
3. Replace **BE 0999.999.992** with the real BE BTW / KBO number (invoice + FAQ).
4. Replace **you@studio.example** with their inbox. For a still-fake demo, keep an RFC 2606 host (`.example`, `.invalid`, `.test`). Do not paste Gmail or a harvested live mailbox.
5. Replace **Client BV**, **Klantplein 8, 1000 Brussel**, **BE 0888.888.888**, and **billing@client.example** with the one client this pack is for — or clear those fields and type them per job.
6. Recolor `--accent` / `--bg` in `pack.css` if they want their own ink.
7. Set a real invoice number series, dates, line items, and due window on `invoice.html` / `reminder.html`.
8. Read `faq.html` with them. Do **not** delete the Peppol answers.

## Peppol (read this)

- **B2C:** a PDF (or this HTML printed to PDF) sent by mail is still allowed.
- **B2B:** since **1 January 2026** a PDF is **not** a legal invoice in Belgium. Structured e-invoicing via Peppol is required.
- This pack does **not** make B2B invoices compliant. We do not run a Peppol Access Point. We do not send live Peppol documents.

## What we refuse

- Peppol Access Point setup or hosting
- Live Peppol send / receive
- Bookkeeping, VAT filings, or accountant work
- Azure AD / Entra / identity-tenant jobs
- Restacking leftover **9 USDC** toys (Solana Invoice, BTW invoice, dagtarief-offerte) as this pack
- Applying the operator to coding jobs

## Use

Open `index.html` in a browser. No account. Pay 299 USDC on Solana, then ship the four working files (rebranded) to one client.

This is not tax or legal advice. 21% is Belgium’s standard BTW rate; the freelancer must confirm the rate that applies to the job.
