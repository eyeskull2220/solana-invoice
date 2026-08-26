# Lead-to-invoice pipeline kit

Reusable offline flow: **form → offerte → factuur → herinnering**. Line items travel from the offerte to the invoice. Demo-branded for a fake freelancer (**Studio Noord**). Rebrand once, reuse for many clients.

**399 USDC.** Not four leftover 9 USDC toys glued together. Not a Peppol Access Point. Not the 299 USDC inbox-ops pack (that pack is one-client branding; this kit is the chained process).

## Price / pay-to

Send **exactly 399 USDC** on **Solana** (USDC only — not SOL, not Base, not ETH, not XRP) to:

`96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3`

Mint: `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v`

Copy-address only. No wallet connect. Open [`index.html`](index.html) and use **Copy address**.

## Files

| File | Role |
| --- | --- |
| [`index.html`](index.html) | Sell / demo page (399 USDC, copy-address) plus the working 4-step pipeline |
| [`form.html`](form.html) | Lead capture. Download a brief, then send the lead into the offerte |
| [`offerte.html`](offerte.html) | Belgian offerte, default **21%** BTW, download standalone HTML |
| [`invoice.html`](invoice.html) | Belgian BTW factuur, default **21%**, lines can come from the offerte |
| [`reminder.html`](reminder.html) | Overdue reminder letter, download standalone HTML |
| [`pipeline.css`](pipeline.css) / [`pipeline.js`](pipeline.js) | Shared kit chrome, totals, and local chain state |

Demo studio: **Studio Noord**. Demo client: **Client BV**. Demo mail: **hello@studio.example** (RFC 2606). No Gmail. No live company inboxes.

The chain is stored in this browser only (`localStorage`). Downloaded HTML files are standalone: no scripts, no treasury address, no kit nav.

## How to rebrand

Do this in the working files (`form.html`, `offerte.html`, `invoice.html`, `reminder.html`) and in the `DEMO` object at the top of `pipeline.js`. Recolor `:root` in `pipeline.css` if they want their own ink.

1. Replace **Studio Noord** with the practice name.
2. Replace **Voorbeeldlaan 1, 2000 Antwerpen** with the work address.
3. Replace **BE 0999.999.992** with the real BE BTW / KBO number.
4. Replace **hello@studio.example** with their inbox. For a still-fake demo, keep an RFC 2606 host (`.example`, `.invalid`, `.test`). Do not paste Gmail or a harvested live mailbox.
5. Replace **Client BV**, **Klantplein 8, 1000 Brussel**, **BE 0888.888.888**, **alex@client.example**, and **billing@client.example** with a real client — or clear those fields and type them per job.
6. Set a real offerte / invoice number series, dates, line items, and due window.
7. Leave the sell-page pay-to as the treasury address unless you are selling the kit itself.
8. Do **not** delete the Peppol answers on the sell page or on the factuur.

Host `form.html` as a public lead form if you want. Keep `index.html` for selling the kit.

## Price the work you send

The kit price is **399 USDC** (this folder). The offerte and factuur you generate are priced in **euro**, with Belgian **21% BTW** as the default rate. Change the rate per job; 21% is Belgium’s standard rate, not tax advice.

## Peppol (read this)

- **B2C:** a PDF (or this HTML printed to PDF) sent by mail is still allowed.
- **B2B:** since **1 January 2026** a PDF is **not** a legal invoice in Belgium. Structured e-invoicing via Peppol is required.
- This kit does **not** make B2B invoices Peppol-compliant. We do not run a Peppol Access Point. We do not send live Peppol documents.

## What we refuse

- Peppol Access Point setup or hosting
- Live Peppol send / receive
- Bookkeeping, VAT filings, or accountant work
- Azure AD / Entra / identity-tenant jobs
- Restacking leftover **9 USDC** toys (Solana Invoice, BTW invoice, dagtarief-offerte, reminder) as this kit
- Applying the operator to coding jobs

## Use

Open `index.html` in a browser. No account. Pay 399 USDC on Solana. Walk the pipeline (or open the four working pages). Download the HTML you actually send.

This is not tax or legal advice. 21% is Belgium’s standard BTW rate; the freelancer must confirm the rate that applies to the job.
