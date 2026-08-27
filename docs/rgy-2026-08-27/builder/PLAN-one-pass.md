# Builder PLAN — one EUR-first shop pass

> **For agentic workers:** this is **one** CODE job after a **different** reviewer greens this page. It is not a punch list. Do not implement from this PR. Do not send mail. Do not publish to Surge from this PR.

**Goal:** After one later CODE pass, a Belgian secretary who opens **https://sovereignforge.surge.sh/** sees one closed EUR shop: six kits, euro faces, STORE Versie 3 privacy, robots Allow, no USDC on the face, betaalgegevens only after akkoord.

**Architecture:** Git tree `shop/sovereignforge/` **is** the live origin. CODE publishes that folder to a **preview** Surge project, then **cutover** to `sovereignforge.surge.sh`. Leftover PR #111, leftover root `index.html` / `catalog.html` / `solana-invoice.html`, and `treasury-tools.surge.sh` are not the shop.

**Tech stack:** Static HTML + CSS. Self-hosted Young Serif + Atkinson (already on the live chalkboard). No Google Fonts. No Inter. No cream-card catalog. No accounts. No forms that store data. No cookie banner.

## Global constraints

- **Origin of record:** `https://sovereignforge.surge.sh/` only. Preview first, then cutover. Never treat leftover [PR #111](https://github.com/eyeskull2220/solana-invoice/pull/111) as the EUR pass.
- **Face six only:** menu **€199**, sponsor **€199**, vakman **€249**, inbox-ops **€299**, lid **€349**, club **€900**. Integers. No seventh chip.
- **EUR-first:** no `USDC`, `Solana`, `Phantom`, `crypto`, or treasury address in `<title>`, `<h1>`, lede, chips, CTAs, or meta on shop pages. Charge copy is not on the face.
- **Betalen:** the page exists. Copy is **Betaalgegevens na akkoord**. No receive address, no QR, no IBAN, no card form.
- **Privacy:** STORE **Versie 3** (verbatim below). Contact **sasha.de.vree.rene@gmail.com**. One page on the shop origin. Footer link required.
- **robots:** `User-agent: *` then `Allow: /` on the shop and on the six featured kit hosts. `Disallow: /` is a fail.
- **Kill:** freelancer line, live `SITE.md`, “elf live kits”, junk SKUs. Stamp **OFFERTE / VOORBEELD**. **KBO/BTW: nog niet toegekend**. No FACTUUR stamp. No fake `BE0`. No mail send. No Surge publish from **this** PLAN PR.
- **Operator is not the freelancer.** Team delivers. Shop copy never says hire-me / freelancer / day-rate.

---

## Why previous Builder plans are RED (do not repeat them)

[PR #161](https://github.com/eyeskull2220/solana-invoice/pull/161) refused GREEN because the written plan was a **punch list**: strip strings on leftover HTML, Allow robots on the wrong tree, hide an address, spawn the next FIX seat. That sequence cannot close the shop.

| Artifact | Why it is not this job |
| --- | --- |
| Live chalkboard today | Eleven kits, USDC on home (`900 USDC · ±€774`), lede “Charge blijft USDC.”, `robots` `Disallow: /`, privacy **Versie 1** still says payment is on-chain USDC, `SITE.md` stubs to those faces. |
| [PR #111](https://github.com/eyeskull2220/solana-invoice/pull/111) | Euro sticker on **€9 / €49 toys**. `Allow: /` on the leftover catalog. Not SovereignForge. **Do not merge. Do not port. Do not treat hide-the-coin as the EUR pass.** |
| [PR #121](https://github.com/eyeskull2220/solana-invoice/pull/121) | Unpublished parallel tree. Five kits, sponsor **€299**, inbox-ops dropped, contact `hello@studio.example`, privacy H1 “Geen cookies” (not STORE Versie 3). |
| [PR #137](https://github.com/eyeskull2220/solana-invoice/pull/137) | Partial git shop; kit hosts still USDC; not cut over; leftover root mixed in. |
| ideas-builder #81 | Five **USDC services**. Off this shop table. |
| `main` catalog | `9 USDC` / `49 USDC`. Leftover invoice HTML. **Do not deploy to sovereignforge.** |

This page is the missing one-pass job. A later CODE agent ships it whole, or not at all.

---

## Sequence (this file does not skip it)

1. **This PR** — merge this markdown only.
2. **A different reviewer** — scores **this file** against the PLAN gates in #161. GREEN only if there is no RED and no YELLOW on: one complete pass vs punch list · EUR-first face · six kits only · robots Allow · no junk SKUs / #111 is not the shop. If RED, rewrite this page. Do not start CODE.
3. **CODE** — one PR that lands the closed file set below, plus the six featured kit euro faces, plus preview, then cutover. Not a second punch-list of hide-coin / robots / SITE stub.

No mail in any of those three steps unless a later CEO page plus operator yes says send. This PLAN never says send.

---

## Origin of record

| Role | URL / path |
| --- | --- |
| Live shop (after cutover) | `https://sovereignforge.surge.sh/` |
| Git source that deploys | `shop/sovereignforge/` in this repo |
| Preview (CODE only, after review) | a **new** Surge project, e.g. `sovereignforge-eur-preview.surge.sh`, published from `shop/sovereignforge/` |
| Cutover (CODE only, after preview walk) | same folder → `sovereignforge.surge.sh` |

**Not the shop**

- Leftover [PR #111](https://github.com/eyeskull2220/solana-invoice/pull/111) (`cursor/euro-shop-face-00e2`)
- Repo root `index.html`, `catalog.html`, `solana-invoice.html`, `config.js`, `README.md`
- `https://treasury-tools.surge.sh/`
- Live `https://sovereignforge.surge.sh/SITE.md` (delete on cutover; do not add `SITE.md` to the git shop)
- Kit PRs that sell pipeline, Peppol, dual-invoice, één klus, 9/49 toys

Surge publish from `.` (repo root) would put leftover USDC invoice HTML on the Belgian origin. CODE publishes **only** `shop/sovereignforge/`.

---

## Closed six (face prices)

Nothing else on home or pakketten. A demo is a demo, not a seventh chip. Seizoenskaart VOORBEELD and named-club VOORBEELD stay demos.

| Slug | Kit | Face price | Live demo (keep host, euro the wrap) |
| --- | --- | ---: | --- |
| `menu` | Menukaart + allergenen | **€199** | https://menu-kit-treasury.surge.sh/ |
| `sponsor` | Sponsorblad vzw | **€199** | https://sponsor-kit-treasury.surge.sh/ |
| `vakman` | Vakman one-pager | **€249** | https://vakman-kit-treasury.surge.sh/ |
| `inbox-ops` | Inbox-ops | **€299** | https://inbox-ops-treasury.surge.sh/ |
| `lid` | Lid-inschrijving | **€349** | https://lid-kit-treasury.surge.sh/ |
| `club` | Club- of vzw-site | **€900** | https://club-site-kit-treasury.surge.sh/ |

Order on home and pakketten: menu → sponsor → vakman → inbox-ops → lid → club.

Each row has: Dutch name, one-line uitkomst, **€N**, stamp OFFERTE (geen wettelijke factuur), **Open het voorbeeld** (live demo), **Vraag deze OFFERTE** (mailto or `/contact.html`, not “Betaal N USDC”).

---

## Closed file set (the job)

CODE creates or replaces **exactly** this shop tree. One PR. Not leftover root.

```
shop/sovereignforge/
  index.html
  pakketten.html
  betalen.html
  contact.html
  privacy.html
  robots.txt
  styles.css          # from live chalkboard: Young Serif + Atkinson @font-face
  fonts/*.woff2       # copy from live origin; no fonts.googleapis.com
  favicon.svg
  favicon.ico
  previews/           # optional; if kept, one width, not a 4437px phone dump
```

No `catalog.html` on the shop origin. No `SITE.md`. No `DESIGN.md` required on the host. No `kit-pay.html` linked from the face. No `betalen.js` that paints a treasury address.

Shared chrome on every shop page:

- `lang="nl"`
- Wordmark SovereignForge → `/`
- Nav: Home · Pakketten · Contact · Privacy. **Betalen** may sit in the footer as a step, not as a coin door. If it stays in the header, the label is still “Betalen” and the page is the akkoord page below — never “Betaal USDC”.
- Footer (not empty): `SovereignForge · OFFERTE/VOORBEELD · Geel / België · sasha.de.vree.rene@gmail.com · KBO/BTW: nog niet toegekend · geen Peppol Access Point · Privacy`
- Stamp: OFFERTE / VOORBEELD. Never FACTUUR as a document stamp. Negation `geen wettelijke factuur` is allowed.
- Address the secretaris as **u** (or **jullie** for the bestuur). No hire-me / freelancer / day-rate.

### `robots.txt` (shop + each of the six kit hosts)

```
User-agent: *
Allow: /
```

No `Disallow: /`. Missing `robots.txt` on a public shop host is not Allow — write the file.

---

## Home — `index.html`

What a secretary forwards tonight.

**`<title>`:** `SovereignForge — voorstel voor het bestuur`

**Meta description:** `OFFERTE-kits voor club, vzw en KMO. Zes pakketten in euro. Geen wettelijke factuur.`

**H1:** `Voor de secretaris die vanavond nog een voorstel naar het bestuur stuurt.`

**Lede (no USDC, no Solana, no “Charge blijft”):** `Eén OFFERTE-kit die u doorstuurt. Prijzen in euro. Geen kaart, geen IBAN op deze pagina. Geen wettelijke factuur.`

**Featured:** all **six** kits as cards, each with:

- Name from the table
- One uitkomst line (Dutch)
- Face price `€199` / `€199` / `€249` / `€299` / `€349` / `€900` — euro only
- `geen BTW-factuur (OFFERTE)`
- Link **Open het voorbeeld** → that kit’s live host
- Link **Vraag deze OFFERTE** → `mailto:sasha.de.vree.rene@gmail.com?subject=OFFERTE%20<slug>` or `/contact.html` — never “Betaal N USDC”

Uitkomst lines (use these, do not invent a seventh):

| Kit | Uitkomst |
| --- | --- |
| Menukaart + allergenen | Printkaart plus QR naar de EU-14. Geen FAVV-claim. |
| Sponsorblad vzw | Eén printblad naar het bestuur. Drie voorbeeldpakketten. |
| Vakman one-pager | Eén blad voor de zaak. Contact, diensten, voorbeeldofferte. |
| Inbox-ops | Intake tot herinnering voor één KMO. Geen freelancer-desk. |
| Lid-inschrijving | Aanvraag naar het secretariaat. Formulier + jaarbijdrage-tabel. |
| Club- of vzw-site | Home, agenda, lid worden, contact. Maatstaf: ZWV De Golfbreker. |

No “Alle 11 pakketten”. Pakketten CTA: `De zes pakketten`.

No freelancer line. No 9/49 toys. No conversion ticker (`1 USDC ≈ €0,86`). No treasury address.

---

## Pakketten — `pakketten.html`

**H1:** `Pakketten`

**Lede:** `Zes OFFERTE-kits. Prijzen in euro. Open het voorbeeld vóór u akkoord gaat.`

Kill every string: `Elf live kits`, `Charge blijft USDC`, `Euro is omrekening`, `indicatief`, USDC column.

Six stacked cards (not a 9-column 52rem table). At 390px: no horizontal scroll. Each card: naam, uitkomst, **€N**, OFFERTE, Open het voorbeeld, Vraag deze OFFERTE.

Drop-list (must not appear as a price row, chip, or nav item):

- Lead tot offerte / pipeline (`pipeline-treasury.surge.sh`)
- Peppol Client-Chase (`peppol-chase-treasury.surge.sh`)
- Dual-invoice (`dual-invoice-treasury.surge.sh`)
- Peppol Ready (`peppol-ready-treasury.surge.sh`)
- Eén klus / Solana Invoice 9 USDC (`solana-invoice-treasury.surge.sh`)
- CSV Cleaner, Form to Email, RSS to Webhook
- Offertebestand €9, studio-tools €49, één opdracht €49 (the #111 catalog)
- km-log, freelance-contract, retainer-invoice, dagtarief, FAQ, UTM, waitlist, paywall, intake, link-in-bio, review-retainer as shop rows
- Seizoenskaart or named-club as SKU #7

Pipeline / Peppol / retainer may live on an ideas-builder **service** page. They are not shop SKUs.

---

## Betalen — `betalen.html`

This is the pay **step**, not a wallet panel.

**`<title>`:** `Betalen — SovereignForge`

**H1:** `Betaalgegevens na akkoord.`

**Lede:** `Hier staan geen rekeningnummers en geen ontvangstadres. Geen kaartformulier. Na uw akkoord op de OFFERTE sturen wij de gegevens apart, per mail.`

**Volgorde**

1. Kies een van de zes pakketten. Open het voorbeeld.
2. Bevestig de OFFERTE per mail naar `sasha.de.vree.rene@gmail.com`. Dit is geen wettelijke factuur.
3. Daarna volgen de betaalgegevens. Niet eerder, niet op deze pagina.

**Prijzen (hele euro)** — the six rows only, `€199` … `€900`.

**Identiteit:** `KBO/BTW: nog niet toegekend.` No invented number. No IBAN.

Forbidden on this page: treasury address `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3`, mint, QR, copy-address, `USDC`, `Solana`, `Phantom`, radios that reveal a pay panel, hash-deep-links that skip akkoord.

---

## Contact — `contact.html`

**H1:** `Alleen mail.`

**Body:** Geen formulier. Geen telefoon. Mail is voor het voorstel of het akkoord.

**Mailto (shop, not demo kits):** `sasha.de.vree.rene@gmail.com`

Say what to mail: kit-naam + club- of zaaknaam. Do not put `hello@studio.example` on the shop contact page (that address stays **inside kit demos** as RFC 2606).

Colophon: `SovereignForge · Geel / België · KBO/BTW: nog niet toegekend.`

No freelancer / hire-me / day-rate.

---

## Privacy — STORE Versie 3

One file: `shop/sovereignforge/privacy.html`. Linked from every shop footer. Kits may link here; they do not get a second policy. Label the page **Versie 3 — 27 augustus 2026**.

Locks from the GREEN fill-in ([PR #152](https://github.com/eyeskull2220/solana-invoice/pull/152)): no AVG badge, no banner, no USDC / IBAN / card, no SCC / adequacy words, host is this origin only.

CODE ships this copy (Dutch, `u`). Do not restore Versie 1 “Betaling is on-chain in USDC”.

```html
<!DOCTYPE html>
<html lang="nl">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Privacy — SovereignForge</title>
  <meta name="description" content="Wie in Geel, mail voor offerte, geen cookies van ons, Gmail buiten de EER alleen om te antwoorden. Geen keurmerk, geen banner.">
  <link rel="canonical" href="https://sovereignforge.surge.sh/privacy.html">
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <!-- shared chrome: skip, header, footer as on home -->
  <main id="inhoud">
    <h1>Privacy</h1>
    <p class="lede">Versie 3 — 27 augustus 2026. Geen keurmerk. Geen banner.</p>

    <h2>Wie, in Geel</h2>
    <p>Sasha, natuurlijke persoon in Geel (België), handelend onder de naam SovereignForge. Geen vennootschap. KBO/BTW: nog niet toegekend. Geen functionaris voor gegevensbescherming.</p>
    <p>Mail voor een offerte of voor deze verklaring: <a href="mailto:sasha.de.vree.rene@gmail.com">sasha.de.vree.rene@gmail.com</a>.</p>

    <h2>Wat deze pagina is</h2>
    <p>Statische catalogus van kits. Bestellen loopt via OFFERTE (geen checkout, geen FACTUUR-module, geen kaartformulier).</p>

    <h2>Welke gegevens, waarom</h2>
    <p>Als u mailt, verwerken wij wat u zelf stuurt: naam, e-mailadres, bericht, eventueel welke kit u vraagt. Doel: de vraag beantwoorden en een offerte opstellen. Rechtsgrond: AVG artikel 6(1)(b) — stappen op uw verzoek vóór een overeenkomst. U bent dat niet verplicht. Zonder contactgegevens geen offerte.</p>

    <h2>Geen kaart, geen IBAN</h2>
    <p>Wij vragen geen kaartnummers en geen IBAN. Op deze pagina staat geen betaalformulier.</p>

    <h2>Trackers</h2>
    <p>Wij zetten zelf geen cookies, pixels of analytics. Of Surge of de mailhost logs of cookies zet, is niet geverifieerd. Daarom is er geen cookiebanner.</p>

    <h2>Ontvangers en bewaartermijn</h2>
    <p>Geen verkoop aan adverteerders. Alleen de verwerkingsverantwoordelijke, de e-mailprovider voor mailboxverkeer, en de hosting van de statische HTML (geen formulierdata). Offerte-mail blijft zolang nodig voor de vraag en de offerte, daarna wissen, tenzij een wettelijke plicht tot langer bewaren.</p>
    <p>Offerte-mail loopt via Gmail, een dienst buiten de EER. Alleen om uw vraag te beantwoorden. Deze pagina noemt geen SCC- of adequacy-claim.</p>
    <p>Geen profilering. Geen geautomatiseerde besluitvorming.</p>

    <h2>Uw rechten</h2>
    <ul>
      <li>inzage</li>
      <li>verbetering</li>
      <li>wissing</li>
      <li>beperking</li>
      <li>bezwaar</li>
      <li>overdraagbaarheid, waar van toepassing</li>
    </ul>
    <p>Uitoefenen: <a href="mailto:sasha.de.vree.rene@gmail.com">sasha.de.vree.rene@gmail.com</a>.</p>

    <h2>Klacht bij de GBA</h2>
    <p>U kunt een klacht indienen bij de Gegevensbeschermingsautoriteit: <a href="https://www.gegevensbeschermingsautoriteit.be/burger/acties/klacht-indienen">https://www.gegevensbeschermingsautoriteit.be/burger/acties/klacht-indienen</a>.</p>
  </main>
</body>
</html>
```

Do not add an AVG-conform badge. Do not add a cookie overlay. Do not name a card, IBAN, or USDC on this page.

---

## Featured kit euro faces

Home links the six live kit hosts. Those wraps are part of **this same CODE pass**. A shop that says €199 while the featured landing still says `299 USDC` is not one pass.

Keep the demo documents (Golfbreker, Voorbeeldharmonie, Voorbeeldkeuken, Voorbeeldloodgieter, Studio Noord). Change the **sell wrap** only.

Kit HTML is not in leftover `main`. CODE, in the **same** pass, puts each featured landing in git and republishes the **existing** treasury host (no seventh origin):

| Slug | Git folder in the CODE PR | Publish to |
| --- | --- | --- |
| menu | `kits/menu/` | `menu-kit-treasury.surge.sh` |
| sponsor | `kits/sponsor/` | `sponsor-kit-treasury.surge.sh` |
| vakman | `kits/vakman/` | `vakman-kit-treasury.surge.sh` |
| inbox-ops | `kits/inbox-ops/` | `inbox-ops-treasury.surge.sh` |
| lid | `kits/lid/` | `lid-kit-treasury.surge.sh` |
| club | `kits/club/` | `club-site-kit-treasury.surge.sh` |

Start from the live host HTML (or the unmerged `tools/…` kit PRs). Do not start from leftover root invoice files. Each folder gets its own `robots.txt` Allow.

| Host | Face now (2026-08-27) | Face after this job |
| --- | --- | --- |
| menu-kit-treasury | already **€199**, VOORBEELD | Keep euro. `robots` Allow. Footer Privacy → shop `/privacy.html`. Kill any leftover USDC. |
| sponsor-kit-treasury | document demo, no USDC in the blad | Kit wrap price **€199** if a price is shown. Allow. Privacy link. |
| vakman-kit-treasury | already **€249** | Keep euro. Allow. Privacy link. |
| inbox-ops-treasury | **299 USDC**, pay-to address, mint, **Demo freelancer · Antwerpen** | **€299**. Kill freelancer line (use `Studio Noord · demo KMO · Antwerpen` or drop the kicker). Kill address, mint, QR, “Betaal 299 USDC”. CTA: Betaalgegevens na akkoord / mail. Allow. Privacy link. |
| lid-kit-treasury | already **€349** | Keep euro. Allow. Privacy link. |
| club-site-kit-treasury | named-club demo, no USDC | Keep as VOORBEELD demo (no seventh SKU). No USDC. Allow. Privacy link to the shop. |

Inbox-ops also drops: `Wij solliciteren niet als menselijke developer` is fine as a negation; **do not** replace it with hire-me copy. Kill `9 USDC-tools` from the wrap. Demo mail inside kits stays `hello@studio.example` / `info@golfbreker.example` (RFC 2606), never the operator Gmail on the public demo.

Kit hosts are not cream-card **shop homes**. A print sheet may look like paper. Do not load Inter or Google Fonts.

---

## Kill list (explicit)

| Kill | How CODE does it in the one pass |
| --- | --- |
| **Freelancer line** | No `freelancer` / `freelance` / `hire me` / day-rate on shop HTML. Inbox-ops kicker is not “Demo freelancer”. Root leftover “For freelancers…” is **not deployed**. |
| **`SITE.md`** | Do not add it to `shop/sovereignforge/`. On cutover, the live stub `https://sovereignforge.surge.sh/SITE.md` must 404 (or no longer point at USDC faces). A stub that says “de shop zit op home en pakketten” while those pages print USDC is the #122 A2 fail. |
| **Elf kits** | No “Elf live kits”, no “Alle 11 pakketten”, no eleven-row table. Six. |
| **Junk SKUs** | Drop-list in Pakketten. Do not merge #111. Do not port €9/€49 cards. Do not sell dual-invoice / Peppol Ready / één klus / English CSV-form-RSS as shop chips. |
| **USDC on face** | Grep below = 0 on shop pages. Kit featured wraps match euro faces. |
| **Treasury address on face** | Not on home, pakketten, betalen, contact, privacy. Wallet rail stays off the shop. |

---

## Look and chrome (enough for CODE, not a second DESIGN punch)

Reuse live chalkboard tokens already on the origin: `--board` / `--chalk` / Young Serif display + Atkinson body, **self-hosted** `fonts/*.woff2`. Drop Iowan/Palatino from `--font-display` (`"Young Serif", serif` only). No Inter. No `#f4f1ea` / `#f6f3ee` cream shop home. No `fonts.googleapis.com`.

Home is a bestuur-voorstel: one hero + six cards. Not eleven phone frames. Pakketten is stacked cards, not a 936px table.

This is still the **same** CODE pass, not a follow-up “fix fonts” seat.

---

## CODE pass — one PR, then preview, then cutover

After a **different** reviewer marks **this** page GREEN:

### 1. Land the tree

Write every file in the closed set. Euro the six featured kit wraps. Commit in that CODE PR (not this PLAN PR).

### 2. Done-check (must be empty / matching before preview)

```bash
# Shop face — zero coin strings
rg -i 'USDC|Phantom|Solana|crypto' \
  shop/sovereignforge/index.html \
  shop/sovereignforge/pakketten.html \
  shop/sovereignforge/betalen.html \
  shop/sovereignforge/contact.html \
  shop/sovereignforge/privacy.html
# expected: no matches

# Leftover-digit junk must not sit on the shop face
rg -n '9 USDC|49 USDC|Elf live|Charge blijft|Demo freelancer|BE0' \
  shop/sovereignforge/
rg -n '€9[^0-9]|€49[^0-9]' shop/sovereignforge/
# expected: no matches (do not use a bare €9 pattern — it would hit €199 / €900)

# robots on the shop tree
grep -n 'Allow: /' shop/sovereignforge/robots.txt
grep -n 'Disallow: /' shop/sovereignforge/robots.txt
# expected: Allow present, Disallow absent

# Privacy Versie 3 locks
rg -n 'Versie 3' shop/sovereignforge/privacy.html
rg -n 'niet geverifieerd' shop/sovereignforge/privacy.html
rg -n 'dienst buiten de EER' shop/sovereignforge/privacy.html
rg -n 'sasha.de.vree.rene@gmail.com' shop/sovereignforge/privacy.html shop/sovereignforge/contact.html
rg -i 'USDC|IBAN|kaartnummer|SCC|adequacy|AVG-conform' shop/sovereignforge/privacy.html
# last command: no matches

# Six prices present; junk hosts absent from shop HTML
rg -n '€199|€249|€299|€349|€900' shop/sovereignforge/index.html shop/sovereignforge/pakketten.html
rg -n 'pipeline-treasury|peppol-chase|dual-invoice|peppol-ready|solana-invoice-treasury|csv-cleaner|form-to-email|rss-to-webhook' \
  shop/sovereignforge/*.html
# second command: no matches
```

Inbox-ops wrap (featured):

```bash
rg -i 'USDC|freelancer|96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3' kits/inbox-ops/index.html
# expected: no matches
rg -n '€299' kits/inbox-ops/index.html
# expected: match
```

Each of the six kit folders also has `robots.txt` with `Allow: /` and no `Disallow: /`.

### 3. Preview (not the live origin)

```bash
# illustrative — CODE uses a fresh preview project, not sovereignforge.surge.sh yet
npx surge shop/sovereignforge/ sovereignforge-eur-preview.surge.sh
```

Walk as a buyer at 1280 and 390: Home → six cards → each voorbeeld → Pakketten → Betalen (no address) → Contact mailto → Privacy Versie 3. Confirm `robots.txt` is Allow. Confirm `SITE.md` is not in the preview tree.

### 4. Cutover

Only after the preview walk holds:

```bash
npx surge shop/sovereignforge/ sovereignforge.surge.sh
```

Then fetch live: home euro six, pakketten not elf, betalen without address, privacy Versie 3, `robots.txt` Allow, `SITE.md` gone or not a USDC stub. Push Allow `robots.txt` to the six kit hosts in the same pass.

**This PLAN PR does not run those surge commands.**

---

## What the secretary sees after cutover (acceptance)

Open `https://sovereignforge.surge.sh/`:

1. Dutch, euro chips **€199 / €199 / €249 / €299 / €349 / €900**, six kits, demos openable.
2. No USDC / Solana / Phantom / freelancer on the first viewport or the shop files.
3. Pakketten does not say elf kits and does not list junk SKUs.
4. Betalen says **Betaalgegevens na akkoord** and shows no pay-to string.
5. Privacy is **Versie 3**, names Sasha · Geel · `sasha.de.vree.rene@gmail.com`, tracker line unverified for host/mailhost, Gmail buiten de EER alleen om te antwoorden, no coin, no banner.
6. `robots.txt` is Allow. Footer has identity + privacy.
7. Featured kit landings that still sell a wrap price do it in euro. Inbox-ops is not a freelancer USDC desk.
8. Leftover #111 was not merged. Root leftover invoice HTML was not the deploy folder.

Until that is true on the **live origin**, the shop is not shipped. Until a **different reviewer** greens **this page**, CODE does not start.

---

## This PR (PLAN only)

| Did | Did not |
| --- | --- |
| Wrote one complete EUR-first shop job | Punch-list of strip / Allow / hide-address |
| Locked origin, six kits, Versie 3, contact, robots, betalen, kill list | Shop HTML, kits, CSS |
| Named preview-then-cutover and a different reviewer before CODE | Mail, Surge publish, merge #111, reprice live, rewrite live robots |

**Next seat:** a **different** reviewer scores this file. Then CODE. Not this run.
