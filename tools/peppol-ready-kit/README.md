# Peppol Ready Kit

**249 USDC** on Solana. Copy-address only. Static HTML + sample XML. Demo data only.

This is **not** a Peppol Access Point. We cannot register a Peppol ID. We do **not** send or receive on the network. Opening these files is **not** compliance. There is **no compliance stamp**.

Pay-to (USDC on Solana, exactly this address):

```
96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3
```

USDC only. Not SOL, not Base, not ETH, not XRP. Price is **249**.

USDC mint: `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v`

## What you get

| File | Role |
|---|---|
| [index.html](index.html) | Sell/demo page, copy-address, not-an-AP, no stamp |
| [screening.html](screening.html) | Seven questions → work-hypothesis result (never a certificate) |
| [template.html](template.html) | Fillable VOORBEELD sheet (never stamped FACTUUR) + SAMPLE XML |
| [invoice-sample.xml](invoice-sample.xml) | Static Peppol BIS Billing 3.0 / UBL SAMPLE — no KBO/VAT digits |
| [ap-pick-list.html](ap-pick-list.html) | Official lists first, then a short AP pick-list (no affiliates) |
| [DISCLAIMER.html](DISCLAIMER.html) | Not an AP, not a bookkeeper, not a legal invoice, no stamp |

Demo UI copy is Dutch. This README is English.

## B2C PDF vs B2B PDF

- **B2C** (invoice to a private individual): PDF is still allowed.
- **B2B** (Belgian VAT-registered businesses in scope): PDF-by-email is **not** a legal Belgian B2B invoice since **1 January 2026**. Structured e-invoice via Peppol is required.
- Tolerance period ended **31 March 2026**. Fine for having **no technical means** starts at **€1,500**. Check FPS Finance for current amounts. Not legal advice.

## Refuse list

Do not sell or do any of these from this kit:

- Certified Access Point / running Peppol for them
- OpenPeppol membership
- Live Peppol send or receive
- Registering their Peppol ID
- A compliance stamp, badge, or “you are Peppol-ready/certified”
- Bookkeeping
- Azure AD / itsme / eID onboarding
- Leftover 9 USDC Solana Invoice restack
- Invented, demo, or placeholder KBO/VAT numbers — leave blank or print exactly `KBO/BTW: nog niet toegekend`
- Stamping FACTUUR before a real KBO exists — this kit prints **VOORBEELD** (or OFFERTE) only

## Demo parties only

Studio Noord / Client BV / `hello@studio.example`. **KBO/BTW: nog niet toegekend** — no invented KBO or VAT digits. No Gmail. No real inboxes. No named staff emails from OpenPeppol.

Document stamp is **VOORBEELD** (or OFFERTE), never **FACTUUR**, until a real KBO exists. This kit never stamps FACTUUR.

The official Peppol BIS Billing 3.0 `CustomizationID` URN contains the word `compliant`. That is the spec identifier, not a claim that this kit or the sample file is Peppol-compliant.

## Official links (not us)

- Certified APs: https://peppol.org/members/peppol-certified-service-providers/ (filter BOSA / Belgium)
- Software list (FPS Finance): https://efactuur.belgium.be/nl/article/softwareoplossingen-voor-het-verzenden-ontvangen-en-verwerken-van-elektronische-facturen
- Peppol Directory: https://directory.peppol.eu/public/ (`0208:` + 10-digit KBO)
- KBO public search: https://kbopub.economie.fgov.be/
