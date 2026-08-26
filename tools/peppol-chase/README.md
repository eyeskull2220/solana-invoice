# Belgian Peppol Client-Chase Pack

**399 USDC** on Solana. Copy-address only. Static HTML + sample XML. Demo data only.

This is **not** a Peppol Access Point. We cannot register a Peppol ID. We do **not** make the buyer compliant. Opening these files is **not** compliance.

Pay-to (USDC on Solana, exactly this address):

```
96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3
```

USDC only. Not SOL, not Base, not ETH, not XRP. Price is **399**, not 499.

USDC mint: `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v`

## What you get

| File | Role |
|---|---|
| [index.html](index.html) | Sell/demo page, copy-address, not-an-AP disclaimer |
| [intake.html](intake.html) | Company block + up to 10 B2B buyers + VAT-case picker (placeholders) |
| [master-data-checklist.html](master-data-checklist.html) | What a real AP will need |
| [invoice-preview.html](invoice-preview.html) | Human-readable 21% Peppol-style invoice |
| [invoice-preview-reverse-charge.html](invoice-preview-reverse-charge.html) | Matching reverse-charge preview |
| [invoice-sample-21pct.xml](invoice-sample-21pct.xml) | Peppol BIS Billing 3.0 / UBL SAMPLE |
| [invoice-sample-reverse-charge.xml](invoice-sample-reverse-charge.xml) | SAMPLE, VAT category AE |
| [creditnote-sample.xml](creditnote-sample.xml) | SAMPLE credit note |
| [reminder-buyer-not-ready.html](reminder-buyer-not-ready.html) | Copy-paste mail **we do not send** |
| [client-chase-mail-1.html](client-chase-mail-1.html) | First chase mail |
| [client-chase-mail-2.html](client-chase-mail-2.html) | Follow-up with FOD list + lookup |
| [software-shortlist.html](software-shortlist.html) | Official FPS/FOD list + Billit / Dexxter / e-invoice.be as examples we checked (not affiliates) |
| [peppol-lookup-worksheet.html](peppol-lookup-worksheet.html) | Official Directory: `0208:` + 10-digit KBO |
| [HANDOFF.html](HANDOFF.html) | Next clicks in a real AP tool; what we did not do |
| [DISCLAIMER.html](DISCLAIMER.html) | Not an AP, not a bookkeeper, not a legal invoice until a certified AP sends it |

Demo UI copy is Dutch. This README is English.

## B2C PDF vs B2B PDF

- **B2C** (invoice to a private individual): PDF is still allowed.
- **B2B** (Belgian VAT-registered businesses in scope): PDF-by-email is **not** a legal Belgian B2B invoice since **1 January 2026**. Structured e-invoice via Peppol is required.
- Fine for having **no technical means** starts at **€1,500**. Check FPS Finance for current amounts. Not legal advice.

## Refuse list

Do not sell or do any of these from this pack:

- Certified Access Point / running Peppol for them
- OpenPeppol membership
- Live Peppol send or receive
- Registering their Peppol ID
- Bookkeeping
- Azure AD
- itsme / eID onboarding
- Leftover 9 USDC Solana Invoice restack
- Coding-job applications
- Claiming they are compliant because they have these files

## Demo parties only

Studio Noord / Client BV / `hello@studio.example` / `KBO/BTW: nog niet toegekend`. No invented KBO, VAT, or IBAN digits in HTML or sample XML. Document stamp is **VOORBEELD**, not FACTUUR. No Gmail. No real inboxes.

## Official links (not us)

- Software list (FPS Finance): https://efactuur.belgium.be/nl/article/softwareoplossingen-voor-het-verzenden-ontvangen-en-verwerken-van-elektronische-facturen
- Peppol Directory: https://directory.peppol.eu/public/
- KBO public search: https://kbopub.economie.fgov.be/
