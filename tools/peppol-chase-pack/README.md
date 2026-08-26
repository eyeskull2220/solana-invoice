# Peppol Client-Chase Pack

Pack date: **2026-08-26**. Price: **399 USDC** on Solana.

Pay-to (USDC on Solana only):

```
96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3
```

USDC mint: `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v`

This folder is static files. No account. No wallet connect. Nothing is sent on the Peppol network from here.

## HARD limits

- **We are not a Peppol Access Point.** We are not an OpenPeppol member. We cannot register a Peppol ID. We cannot send or receive Peppol documents.
- **Do not claim compliance.** Opening these files is not Peppol certification, not EN 16931 validation, and not proof that a Belgian B2B invoice is legal.
- **Do not invent VAT or KBO numbers.** Paste identifiers from the Crossroads Bank for Enterprises (KBO/BCE) public search or from the enterprise’s own records. Sample XML uses `REPLACE_WITH_*` tokens, not fake enterprise numbers.
- **AP shortlist is public Belgian Access Points only**, snapshotted from the OpenPeppol certified service-provider list. It is not an endorsement. Recheck the live list before you contact anyone.

## What you get

| File | Role |
|---|---|
| [index.html](index.html) | Offer page, copy-address pay, not-an-AP banner |
| [intake.html](intake.html) | Local intake. Empty identifier fields. Nothing is submitted. |
| [sample-ubl-invoice.xml](sample-ubl-invoice.xml) | Peppol BIS Billing 3.0 UBL **shape** with placeholder identifiers. Not for transmission. |
| [ap-shortlist.html](ap-shortlist.html) | Public BE Access Points from OpenPeppol (BOSA / Belgium, AP certified). Snapshot 2026-08-26. |
| [handoff-checklist.html](handoff-checklist.html) | What to give a real Access Point. What this pack did not do. |
| [pii-scan.md](pii-scan.md) | PII scan report for this folder |
| [scan-pii.sh](scan-pii.sh) | Re-runnable scanner |

## Official sources (not us)

- OpenPeppol certified service providers (filter Country = Belgium or Authority = BOSA): https://peppol.org/members/peppol-certified-service-providers/
- Belgian Peppol authority pointer: https://digital.belgium.be/e-invoicing/PEPPOLinBelgium.html
- FPS Finance e-invoice FAQ (how Peppol IDs work in Belgium, scheme 0208): https://einvoice.belgium.be/en/FAQ/general-questions-about-peppol
- Peppol Directory lookup: https://directory.peppol.eu/public/
- KBO public search: https://kbopub.economie.fgov.be/
- Peppol BIS Billing 3.0 (May 2026 release) invoice syntax: https://docs.peppol.eu/poacc/billing/3.0/syntax/ubl-invoice/

The FPS Finance “software solutions” page is an **end-user software** list, not the Access Point registry. This pack’s shortlist is APs only.

## What you do not get

- Certified Access Point operation
- OpenPeppol membership
- Live Peppol send or receive
- Registration of a Peppol ID
- A stamp that you, your client, or this XML is compliant
- Invented VAT, KBO, IBAN, or contact details
- Bookkeeping, tax advice, itsme/eID, or identity onboarding
