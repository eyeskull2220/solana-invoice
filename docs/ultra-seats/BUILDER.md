# BUILDER seat

Builder owns **paid static kits on Surge**. Not leftover HTML toys. Not Wallet rails. Not Scout lists. The operator in Geel **does not code**.

This file is the seat SSOT. The public EUR face lives at [`shop/sovereignforge-builder/`](../../shop/sovereignforge-builder/). Live kit demos stay where they already are. Do not restack root `index.html`, `catalog.html`, or `solana-invoice.html`.

## Who does what

| Seat | Owns | Does not |
| --- | --- | --- |
| **Builder** | Static kits, EUR shop, Dutch copy, Surge demos, rebrand after pay | Operator-as-developer, legal/tax advice, mailing clubs |
| **Operator** | Collects EUR, forwards logo / colours / IBAN / KBO / photos, yes/no on copy | Code, host, debug, deploy, invent a KBO |
| **Wallet** | How money actually lands (internal) | The public shop face |
| **Scout** | Buyer lists with public `info@` | Shipping kits |

Agents ship. The operator reviews a screenshot and says yes or no. If a task needs the operator at a keyboard, it is not a Builder task.

## Public-face law (non-negotiable)

The shop and every kit **the buyer sees** follow this. Internal treasury notes may name rails. The public face may not.

1. **EUR-first.** Prices are €199 / €249 / €299 / €349 / €900. No USDC, Solana, Phantom, crypto, or wallet on the public face.
2. **OFFERTE / VOORBEELD.** Stamped. Visible. Not a whisper in the footer.
3. **No FACTUUR.** Do not title a page INVOICE. Do not emit a numbered invoice. Write “geen wettelijke factuur” where a buyer could confuse the sheet with one.
4. **No fake KBO.** Write `KBO/BTW: nog niet toegekend`. Never invent `BE0…`. Never invent an IBAN.
5. **robots Allow.** `User-agent: *` then `Allow: /`. The live kits currently Disallow — that is a defect, not a policy.
6. **Self-host fonts.** `@font-face` to files in-tree. No Google Fonts, no Typekit, no jsDelivr at runtime.
7. **No leftover HTML.** Do not paste Solana Invoice, catalog toys, or pay-QR chrome into a club or kitchen page.
8. **Do not mail.** Builder does not send outreach. Scout owns lists. The shop has no newsletter and no live inbox.

Demo contact stays RFC 2606: `hello@studio.example` or `info@golfbreker.example`. No personal Gmail, phone, or home street.

## Inventory (live Surge)

Five kits. Link these, do not clone them into a sixth stencil.

| SKU | EUR (shop) | Live demo still says | Demo | What the buyer actually opens |
| --- | ---: | --- | --- | --- |
| Menukaart + allergenen | **€199** | 199 USDC | [menu-kit-treasury.surge.sh](https://menu-kit-treasury.surge.sh/) | [menu.html](https://menu-kit-treasury.surge.sh/menu.html) · [allergenen.html](https://menu-kit-treasury.surge.sh/allergenen.html) |
| Vakman-offerte | **€249** | 249 USDC | [vakman-kit-treasury.surge.sh](https://vakman-kit-treasury.surge.sh/) | [offerte.html](https://vakman-kit-treasury.surge.sh/offerte.html) |
| Sponsorblad vzw | **€299** | 199 USDC | [sponsor-kit-treasury.surge.sh](https://sponsor-kit-treasury.surge.sh/) | [offerte.html](https://sponsor-kit-treasury.surge.sh/offerte.html) |
| Lid-inschrijving | **€349** | 349 USDC | [lid-kit-treasury.surge.sh](https://lid-kit-treasury.surge.sh/) | [lid.html](https://lid-kit-treasury.surge.sh/lid.html) |
| Club-site kit | **€900** | 900 USDC | [club-site-kit-treasury.surge.sh](https://club-site-kit-treasury.surge.sh/) | Home, over, agenda, lid worden, contact · Golfbreker |

Shop source of truth is the EUR column. The USDC labels on Surge are a teardown finding, not a second price list.

### What each SKU contains (sold)

- **€199 Menukaart.** Print-ready Dutch menu (voorgerecht / hoofdgerecht / dessert / drank) with EU-14 codes on the dish. QR + URL to the allergenen matrix. Stamp **VOORBEELD**. Print / save PDF from the browser. Demo kitchen: Voorbeeldkeuken, Noorderlaan 12, 2030 Antwerpen, `hello@studio.example`.
- **€249 Vakman.** One Dutch **OFFERTE** sheet for a tradesperson. Demo: Voorbeeldloodgieter — ontstopping, kraan, boiler-check, euro as prijsindicatie. Print / save PDF. `KBO/BTW: nog niet toegekend`. `IBAN: nog niet toegekend`.
- **€299 Sponsorblad.** Print-ready vzw sponsor sheet. Demo: **Voorbeeldharmonie** concertkalender + three voorbeeldpakketten. Stamp **OFFERTE**. Not three bullets on a landing page — the sheet itself.
- **€349 Lid-inschrijving.** The form itself: jaarbijdrage-tabel (gewoon / jeugd / steunend) + aanvraag to the secretariaat. Named club **Voorbeeldharmonie**. Stamp **OFFERTE**. Bijdragen are **VOORBEELD**. No IBAN on the sheet.
- **€900 Club-site.** Multi-page Dutch club/vzw site. Named demo club **ZWV De Golfbreker** (zwemclub, Geel). Home, over, agenda, lid worden, contact. Static, no account. Editor exists for rebrand after pay — it is not a product to sell as a public stencil factory.

## Adversarial teardown (fetched 2026-08-27)

Read this as a punch list. Do not ship another stencil until the live kits match the public-face law.

### All five hosts

| Defect | Evidence | Why it matters |
| --- | --- | --- |
| **robots Disallow: /** | Every kit `robots.txt` is 26 bytes: `User-agent: *` / `Disallow: /` | Buyers and search must see the VOORBEELD. Hide is not a privacy strategy. Morning fix: `Allow: /`. |
| **USDC / Solana on the public face** | Club home: 5× USDC, 3× Solana, treasury `96BT6…` in the pay box **and** the footer of over/agenda/lid/contact. Menu + vakman titles: “199 USDC” / “249 USDC”, Solana Pay URI, **Open wallet**. Lid + sponsor index: USDC + address. | A Flemish secretary who opened a club demo should not land on a chain. Wallet chrome is Wallet-seat, not Builder-face. |
| **No self-hosted fonts** | Zero `@font-face` on all five. System UI + Georgia. | Shop now self-hosts Source Serif 4 + Source Sans 3 (OFL). Kits still look like a draft. |
| **Pay box on the artefact** | Club: kit pay on the club home. Menu/vakman: pay URI + copy-address above the product. Lid/sponsor: thin index that is mostly pay. | The artefact the club prints must not carry the vendor’s rail. Pay lives on **our** shop `/betalen.html`. |

### Club-site (`club-site-kit-treasury`)

- Named club **Golfbreker** is the right shape (not “Voorbeeldclub vzw”). It is labelled **demo**, not **VOORBEELD**. Morning: one stamp, one word.
- No `privacy.html` on the live host (a closed PR had one; the live tree does not).
- `editor.html` is a public stencil mill (club name, colours, zip download). **STOP** selling or featuring that as the product. Rebrand happens privately after €900. The public demo is the named club.
- Footer pay-to repeats the treasury address on pages a member would bookmark.
- Copy mentions “wallet” on home and lidworden.
- No print-PDF affordance on club pages.

### Menu (`menu-kit-treasury`)

- **Keep:** VOORBEELD stamp, print/PDF, allergenen matrix, **no FAVV claim**, no invented KBO, `hello@studio.example`.
- **Tear down:** title and index are a 199 USDC pay wall with “Open wallet”. The product pages (`menu.html`, `allergenen.html`) are already closer to EUR-first — they speak euro dishes, not rails.
- Allergenen table is EU-14 with codes + per-dish matrix. Disclaimer: voorbeeld, geen juridisch advies, kruisbesmetting niet in kaart. **Do not add FAVV, FASFC, or “erkend door”.**

### Lid (`lid-kit-treasury`)

- Index is a stub (~2.6 KB) that still talks USDC. The **sheet** `lid.html` is the product and is already OFFERTE / VOORBEELD.
- Named club Voorbeeldharmonie: keep. Do not genericise.
- Mailto on the form points at `hello@studio.example`. Fine for demo. Do not wire a real inbox on the public host.

### Sponsor (`sponsor-kit-treasury`)

- Same stub-index pattern as lid. The sheet `offerte.html` is the product.
- Live rail price 199 USDC vs shop **€299**. Do not print both. EUR shop wins; strip the USDC index.
- Three pakketten with euro VOORBEELD amounts: keep. No FACTUUR numbering.

### Vakman (`vakman-kit-treasury`)

- Index is another USDC pay wall + Open wallet. Sheet `offerte.html` is the OFFERTE.
- “BTW n.v.t.” on a voorbeeld total is acceptable only while KBO is pending. Never fill a fake VAT line.

### Leftover HTML

None of the five kits embed `solana-invoice.html` or the root catalog. Good. Do not reverse that. Root leftover tools stay leftover — they are not Builder inventory.

## STARTABLE before morning

Work that fits in one night **without a new stencil kit**. Do these; then stop.

1. **EUR-first face** — Shop at `shop/sovereignforge-builder/` (this PR). Then strip USDC / Solana / Open wallet / treasury address from the five Surge **indexes**. Leave the artefact pages (menu, allergenen, offerte, lid, Golfbreker content) as the demo.
2. **robots Allow** — Replace every kit `robots.txt` (and the shop, already Allow) with `Allow: /`.
3. **Named-club VOORBEELD** — Golfbreker and Voorbeeldharmonie stay named. Add the **VOORBEELD** stamp on club-site (it currently says “demo”). Do not revert to a nameless “Voorbeeldclub vzw”.
4. **Print PDF** — Menu and vakman already say “Afdrukken of bewaren als PDF via uw browser.” Mirror that line + `@media print` hide-nav on club, lid, sponsor if missing.
5. **Allergenen matrix, no FAVV** — Already on menu-kit. Do not stamp FAVV. Do not claim the matrix is a legal fiche. If a buyer asks for FAVV language, refuse.

That is the morning board. It is rework of inventory, not five new products.

## STOP: stencil kits

Do **not** ship another generic template with placeholders, an editor.html, and a pay box.

Stop list:

- A sixth “kit” that is only a colour-swap of Golfbreker.
- Public `editor.html` as a product.
- Inbox-ops / Peppol / pipeline HTML packs dressed as Builder SKUs (wrong seat or wrong artefact).
- Leftover 9/49 USDC toys restacked as “clubs”.
- Fake KBO, fake IBAN, FACTUUR title, FAVV badge.
- Mailing the Scout lists from this seat.
- Asking the operator to npm, surge, or git.

If the artefact is not a **named** club, kitchen, or vakman the buyer can print before lunch, it is a stencil. Stop.

## Shop (EUR-first)

Path: [`shop/sovereignforge-builder/`](../../shop/sovereignforge-builder/)

| Page | Role |
| --- | --- |
| `index.html` | Persuade. What Builder sells. Links to demos. |
| `pakketten.html` | Five SKUs, euro prices, what you get, demo links. |
| `betalen.html` | Overschrijving in euro. OFFERTE, not FACTUUR. KBO/IBAN pending. No rails. |
| `contact.html` | How to reach the desk. No newsletter. No live mail-out. |
| `privacy.html` | Static host, no cookies, no tracking. |
| `robots.txt` | `Allow: /` |
| `css/shop.css` + `fonts/` | Self-hosted Source Serif 4 + Source Sans 3 (OFL). |

Deploy (agent, not operator): `npx surge shop/sovereignforge-builder --domain <host>`. Do not instruct the operator to run it.

## After a yes

1. Operator forwards logo, colours, photos, legal name, and — when they have them — KBO and IBAN.
2. Agent copies the **matching** live kit privately. Renames the club/kitchen/vakman. Drops vendor pay boxes. Keeps OFFERTE/VOORBEELD until the buyer’s own numbers exist.
3. Agent hosts the paid copy. Operator does not deploy.
4. If KBO is still pending, it stays `nog niet toegekend`. Never invent one to look finished.

## Out of scope for this seat

- Legal or tax advice. The boekhouder remains the boekhouder.
- Peppol go-live, CRM pipelines, inbox retainers (other offers, other PRs).
- Applying the operator as a developer on a marketplace.
- Changing leftover HTML in the repo root.
