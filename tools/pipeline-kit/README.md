# Lead-to-invoice pipeline kit

One offline flow: **form → Dutch offerte → factuur → herinnering**. Line items travel with the job. Demo-branded for a fake freelancer (**Studio Noord**). Rebrand once, reuse for many clients.

**399 USDC.** Not four leftover 9 USDC toys glued together. Not a Peppol Access Point. Not the 299 USDC inbox-ops pack.

Open [`index.html`](index.html). No account. No wallet connect. Works offline after you open this file.

## Price / pay-to

Send **exactly 399 USDC** on **Solana** (USDC only — not SOL, not Base, not ETH, not XRP) to:

`96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3`

Mint: `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v`

Copy-address only. Use **Copy address** on the page.

## Flow

1. **Form** — capture the lead. Download a Dutch brief, or send the lead into the offerte.
2. **Offerte** — Dutch quote, default **21%** BTW, live excl / BTW / incl. Download standalone HTML.
3. **Factuur** — Belgian BTW invoice. Same lines as the offerte. Download standalone HTML.
4. **Herinnering** — overdue letter from the invoice totals. Download standalone HTML, or open mailto.

Downloaded HTML files are standalone: no scripts, no HTTP, no treasury address.

## Demo (fake only)

- Studio: **Studio Noord**
- Client: **Client BV**
- Mail: **hello@studio.example**, **alex@client.example**, **billing@client.example** (RFC 2606)
- Address: Voorbeeldlaan 1, 2000 Antwerpen / Klantplein 8, 1000 Brussel
- BTW/KBO: BE 0999.999.992 / BE 0888.888.888

No real client names. No live personal surnames. No Gmail. No live company inboxes.

Run the scan from this folder:

```bash
sh scan-pii.sh
```

## How to rebrand

Do this in `index.html` (the `DEMO` object and visible copy). Recolor `:root` if they want their own ink.

1. Replace **Studio Noord** with the practice name.
2. Replace **Voorbeeldlaan 1, 2000 Antwerpen** with the work address.
3. Replace **BE 0999.999.992** with the real BE BTW / KBO number.
4. Replace **hello@studio.example** with their inbox. For a still-fake demo, keep an RFC 2606 host (`.example`, `.invalid`, `.test`).
5. Replace **Client BV** and the other demo client fields — or clear them and type them per job.
6. Set a real offerte / invoice number series, dates, line items, and due window.
7. Leave the sell-page pay-to as the treasury address unless you are selling the kit itself.
8. Do **not** delete the Peppol answers.

## Peppol (read this)

- **B2C:** a PDF (or this HTML printed to PDF) sent by mail is still allowed.
- **B2B:** since **1 January 2026** a PDF is **not** a legal invoice in Belgium. Structured e-invoicing via Peppol is required.
- This kit does **not** make B2B invoices Peppol-compliant. We do not run a Peppol Access Point. We do not send live Peppol documents.

## What we refuse

- Peppol Access Point setup or hosting
- Live Peppol send / receive
- Bookkeeping, VAT filings, or accountant work
- Azure AD / Entra / identity-tenant jobs
- Restacking leftover **9 USDC** toys as this kit
- Applying the operator to coding jobs

This is not tax or legal advice. 21% is Belgium’s standard BTW rate; the freelancer must confirm the rate that applies to the job.
