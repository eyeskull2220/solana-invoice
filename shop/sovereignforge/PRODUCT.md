# SovereignForge shop — product

Public EUR face for the Kempen kits. Path: `shop/sovereignforge/`.

This folder is a **static Dutch shop**. It sells existing HTML packs. It does not add tools, Peppol, or pipeline kits. It does not touch `tools/peppol-*` or `tools/pipeline-kit/`.

## Who it is for

A secretary, kitchen, plumber, sponsor chair, or one-person practice in Flanders who wants a **print-ready HTML map** they can host or print. Not a SaaS seat. Not a monthly desk. Not a coding job.

## What is on sale (EUR on the face)

| Pakket | EUR | Live demo | What they actually get |
| --- | ---: | --- | --- |
| Menukaart + allergenen | **€199** | [menu-kit-treasury.surge.sh](https://menu-kit-treasury.surge.sh/) | Printable Dutch menu, QR to the EU-14 allergen list, PDF-ready HTML. Stamp **VOORBEELD**. |
| Sponsorblad | **€199** | [sponsor-kit-treasury.surge.sh](https://sponsor-kit-treasury.surge.sh/) | One printable sheet: calendar, three example packages, secretariat. Stamp **OFFERTE**. |
| Vakman one-pager | **€249** | [vakman-kit-treasury.surge.sh](https://vakman-kit-treasury.surge.sh/) | One Dutch **OFFERTE** sheet (clogging, tap, boiler-check as demo). Rename and print. |
| Inbox-ops | **€299** | — (no public demo URL on this shop) | Four working files for one client: intake, Belgian BTW **VOORBEELD**, reminder, client FAQ. Not a legal **FACTUUR**. Not a Peppol Access Point. |
| Lidformulier | **€349** | [lid-kit-treasury.surge.sh](https://lid-kit-treasury.surge.sh/) | Membership table (gewoon / jeugd / steunend) + application to the secretariat. Stamp **OFFERTE**. |
| Clubsite | **€900** | [club-site-kit-treasury.surge.sh](https://club-site-kit-treasury.surge.sh/) | Six static pages for a Belgian club / vzw: home, over, agenda, lid worden, contact, privacy. Mailto, no account. Private rewrite for one named club after payment. |

Demos are **examples**. Demo kitchens, clubs, and plumbers are fictional. Demo mail is RFC 2606 (`hello@studio.example` and similar). No live inbox, no street of a real person, no invented KBO digits.

## How a buyer pays

Public pages show **euro amounts only**.

1. Buyer picks a pack.
2. Buyer mails `hello@studio.example` (contact form is `mailto:` only).
3. Buyer receives an **OFFERTE** (or a **VOORBEELD**). **Not a FACTUUR.**
4. **KBO/BTW: nog niet toegekend.** No invented enterprise number. No IBAN printed on these pages.
5. Euro payment instructions go in that OFFERTE, not on the public face.
6. After the euro amount is received, Builder ships the HTML folder (and, for club, a later private named-club copy).

## Stamps that must stay visible

- **OFFERTE** / **VOORBEELD** — always.
- **Geen wettelijke FACTUUR.**
- **KBO/BTW: nog niet toegekend.**

## What this shop is not

- Not a legal invoice.
- Not bookkeeping, VAT filing, or accountant work.
- Not a Peppol Access Point. We do not send live Peppol documents.
- Not identity login, members area, or a weekly admin seat.
- Not leftover 9-euro HTML toys restacked as these packs.

## Contact on the public face

- Mail: `hello@studio.example` (RFC 2606 until a real work mailbox is set).
- Region: Kempen (Geel). No home street, no personal webmail, no phone number invented for this shop.
- Phone-first means **layout**: one column, thumb reach, 48px taps. It does not mean inventing a GSM.

## Public HTML pages

`index.html` · `pakketten.html` · `betalen.html` · `contact.html` · `privacy.html`

Hard rule for those five files (and their CSS/JS): **euro on the face**. Do not print settlement-asset names, chain names, client-app names, the word for on-chain money, the word for a signing app, or any receive string.

`PRODUCT.md` and `DESIGN.md` are operator notes. They are not the shop face.
