# REVIEWER rubric — SovereignForge / shop HTML

Seat: **REVIEWER**. Date: **2026-08-27**.

This file is the hard-fail instrument for shop HTML. A later builder PR is allowed to fix the sites. **This PR only adds the rubric.** Do not ship shop, kit, or CSS changes here.

Verdict for a surface is **FAIL** if any hard-fail row is FAIL. Verdict for the shop as a whole is **FAIL** if any in-scope shop face fails.

## Scope

Score both sources. Do not pretend they are the same tree.

| Source | What it is |
| --- | --- |
| **This repo (`main`)** | Pay page `index.html`, catalog `catalog.html`, product `solana-invoice.html`, `config.js`. There is **no** SovereignForge shop HTML in this checkout. |
| **Live Surge** | Shop face `https://sovereignforge.surge.sh/` (plus `/pakketten.html`, `/betalen.html`, `/contact.html`, `/privacy.html`, `styles.css`, `robots.txt`). Catalog `https://treasury-tools.surge.sh/`. Kit hosts listed below. |

Live kit hosts (linked from the shop / catalog on 2026-08-27):

- https://club-site-kit-treasury.surge.sh/
- https://menu-kit-treasury.surge.sh/
- https://sponsor-kit-treasury.surge.sh/
- https://lid-kit-treasury.surge.sh/
- https://vakman-kit-treasury.surge.sh/
- https://inbox-ops-treasury.surge.sh/
- https://pipeline-treasury.surge.sh/
- https://peppol-chase-treasury.surge.sh/
- https://dual-invoice-treasury.surge.sh/
- https://peppol-ready-treasury.surge.sh/
- https://solana-invoice-treasury.surge.sh/

Older English tool hosts still live (not the Belgian shop face, still score robots + leftover template):

- https://csv-cleaner-treasury.surge.sh/
- https://form-to-email-treasury.surge.sh/
- https://rss-to-webhook-treasury.surge.sh/

## How to run

1. Read the repo HTML listed above.
2. Fetch each live URL (HTML, `robots.txt`, linked CSS). Do not score a Surge 404 page as a kit.
3. Mark every hard-fail row PASS or FAIL with a one-line evidence quote (element, URL, or file).
4. One FAIL on a shop face (`index.html` / `catalog.html` / `sovereignforge.surge.sh` / `treasury-tools.surge.sh`) fails the shop.
5. Kit hosts inherit the same ten checks. A kit FAIL does not excuse a shop PASS, and a shop FAIL does not wait on kit fixes.

## Hard fails

These are binary. No “almost”. No “disclaimer nearby”.

### 1. USDC-on-face

**FAIL if** USDC is the face price or appears in the first viewport of a **shop / catalog** page: `<title>`, `<h1>`, hero/lede, kicker, or price chips/cards.

Allowed: USDC on `/betalen.html` (or an equivalent pay panel *after* a kit is chosen), in a privacy note about settlement, or inside a kit’s pay block that is not the shop home.

Required on shop face: euro first (`€…` / `Prijs €…`). Charge may stay USDC **off the face**.

**FAIL examples:** title `Solana Invoice — 9 USDC`; catalog chip `900 USDC` with no euro; home lede “Afrekening in USDC” above the fold; example card `afrekening 900 USDC` on the home list.

### 2. No demo

**FAIL if** the shop or kit sell-page does not let a buyer **open or see the deliverable** before paying.

Pass requires at least one of: a live named-club / printblad / form demo, an in-page preview (`iframe` or screenshot of that live demo), or a working editor that is not locked behind “unlock download”.

A paragraph describing the file is not a demo. A paywall with no sample is not a demo.

### 3. FACTUUR leftover

**FAIL if** a page stamps, titles, or modules a document as `FACTUUR` (heading, watermark, filename, or UI that presents a legal Belgian invoice).

Allowed: the negation in running text — `geen FACTUUR`, `nooit FACTUUR`, `geen wettelijke factuur` — when the visible stamp is `OFFERTE` or `VOORBEELD`.

`dual-invoice` as a **kit slug** is leftover naming; fail the row only if the **document face** still says FACTUUR.

### 4. Empty footer

**FAIL if** there is no `<footer>`, or the footer’s visible text is empty / whitespace-only.

Pass requires identity in the footer: who, where or mail, and the OFFERTE/VOORBEELD + KBO line on Belgian shop pages. A filled product colophon on a print sheet counts for that sheet only.

### 5. robots Disallow

**FAIL if** `robots.txt` contains `Disallow: /` for `User-agent: *` (or equivalent “block everything”).

Missing `robots.txt` on a **public shop host** is not a Disallow fail by itself. An explicit `Disallow: /` on `sovereignforge.surge.sh` or `treasury-tools.surge.sh` **is** a shop fail — the face cannot be indexed.

Kit hosts with the same `Disallow: /` fail this row for that host.

### 6. Inter / cream slop

**FAIL if** the **shop or catalog face** uses the Inter webfont **or** the cream-paper + sage-card template:

- Inter: `font-family` containing `Inter`, or a file named/served as Inter.
- Cream slop: shop background in the `#f4f1ea` / `#f6f3ee` / `#f3efe6` family with sage accent `#123c2e` / `#0c4a36` and rounded white cards.

Pass: chalkboard / board face (e.g. Young Serif + Atkinson, `--board` dark green). Pass: a **print invoice / menukaart sheet** that is supposed to look like paper. Fail: using that cream card grid as the **shop home**.

### 7. Google Fonts

**FAIL if** the page loads fonts from `fonts.googleapis.com`, `fonts.gstatic.com`, or `fonts.google.com`.

Self-hosted `@font-face` (`url("fonts/….woff2")`) and system stacks (`ui-sans-serif`, Palatino, Iowan) pass.

### 8. Fake BE0

**FAIL if** a Belgian KBO / BTW number is invented (`BE0` + digits, `0xxx.xxx.xxx`, or any made-up ondernemingsnummer).

Pass: `KBO/BTW: nog niet toegekend` with no number. Demo mail like `hello@studio.example` is not a BE0 fail.

### 9. Missing privacy

**FAIL if** a **shop or catalog** origin has no privacy page, or the footer does not link to it.

Pass: a real `/privacy.html` (or equivalent) that states controller, what is processed, USDC/no card, cookies/trackers, Gmail/Surge, and GBA. Kits may point at the shop privacy page; a kit with no link and no page still fails this row for that host.

### 10. Cookie banner with zero trackers

**FAIL if** a cookie-consent banner / overlay / “accept cookies” bar is present **and** the page has no analytics, pixels, beacons, or other trackers.

No banner + no trackers = PASS. A privacy sentence that *refuses* a banner because there are no trackers = PASS. Banner without trackers = theater = FAIL.

## Surfaces (what “shop HTML” means)

| Surface | Role |
| --- | --- |
| Shop home | First thing a Belgian secretary sees. Must be EUR-first, demo-first, chalkboard (not cream Inter), indexable, footered, privacy-linked. |
| Pakketten | Table may list USDC as charge **next to euro**. Euro column required. |
| Betalen | USDC is allowed here. Still no FACTUUR stamp, no fake BE0, no Google Fonts, no empty footer, no cookie theater. |
| Catalog `treasury-tools.surge.sh` | Same shop-face rules as home. |
| Repo `index.html` / `catalog.html` | Same shop-face rules if they are still the checkout tree’s public pages. |
| Kit hosts | Demo must exist. Sell-wrap may mention price; shop-face USDC/cream rules still apply to a kit **landing** that is linked as the public example. |

---

## Run — 2026-08-27

Fetched live Surge HTML/CSS/`robots.txt` and scored this repo’s HTML. **No shop files were changed.**

### Overall: **FAIL**

Shop HTML does not exist in this repo. Live `sovereignforge.surge.sh` is a chalkboard Belgian face with demos and privacy, but it is **blocked from crawlers** and still **puts USDC on the home face**. Live `treasury-tools.surge.sh` is a cream USDC catalog with **no privacy** and the same robots block. Repo pay/catalog pages fail the shop-face checks.

### Repo (`main`)

| Check | `index.html` | `catalog.html` | `solana-invoice.html` |
| --- | --- | --- | --- |
| 1. USDC-on-face | **FAIL** — title `Solana Invoice — 9 USDC`; sub `One file. 9 USDC`; pay card on the face | **FAIL** — price chips `9 USDC` / `49 USDC`; lead “Billed in USDC” | n/a (product sheet, not shop face) |
| 2. No demo | **FAIL** — editor is behind unlock; face does not open a sample | **FAIL** — links to live tools only; this file is not a demo | PASS — the file *is* the working editor |
| 3. FACTUUR leftover | PASS — no `FACTUUR` stamp | PASS | PASS — word is `INVOICE` (EN product), not `FACTUUR` |
| 4. Empty footer | **FAIL** — no `<footer>` | PASS — footer has billing line | PASS — network/mint colophon |
| 5. robots Disallow | n/a — no `robots.txt` in repo | n/a | n/a |
| 6. Inter / cream slop | PASS face — dark `#07090f`, system-ui (cream is only inside the embedded product) | **FAIL** — `#f6f3ee` + sage `#0c4a36` cards | n/a — paper invoice sheet |
| 7. Google Fonts | PASS | PASS | PASS |
| 8. Fake BE0 | PASS — none | PASS | PASS |
| 9. Missing privacy | **FAIL** | **FAIL** | **FAIL** as a public host would be; file has no privacy link |
| 10. Cookie banner, zero trackers | PASS — no banner, no trackers | PASS | PASS |
| **Surface** | **FAIL** | **FAIL** | product only |

### Live shop hosts

| Check | `sovereignforge.surge.sh` | `treasury-tools.surge.sh` |
| --- | --- | --- |
| 1. USDC-on-face | **FAIL** — home lede “Afrekening in USDC op Solana”; example cards `Prijs €774 · afrekening 900 USDC` (euro present, USDC still on the face). `/betalen.html` h1 “Betaal dat USDC-bedrag” is the pay surface (allowed). | **FAIL** — price chips are USDC-only (`900 USDC`); lead “Jullie betalen in USDC”; no euro on the face |
| 2. No demo | PASS — live kits + club screenshot (`previews/club.jpg` / `club.webp`); menu/sponsor/lid are openable demos | PASS — each card links a live kit host |
| 3. FACTUUR leftover | PASS — stamp OFFERTE/VOORBEELD; privacy says “geen FACTUUR-module” (negation) | PASS — “Stempel OFFERTE, geen FACTUUR” (negation); dual-invoice slug only |
| 4. Empty footer | PASS — colophon: SovereignForge, Geel, mail, KBO line, privacy | PASS — filled footer (no privacy link — scored in row 9) |
| 5. robots Disallow | **FAIL** — `User-agent: *` / `Disallow: /` | **FAIL** — same `Disallow: /` (meta `index,follow` is contradicted by robots) |
| 6. Inter / cream slop | PASS — chalkboard, Young Serif + Atkinson self-hosted, no Inter | **FAIL** — cream `#f4f1ea` + sage `#123c2e` card grid |
| 7. Google Fonts | PASS — local `fonts/*.woff2` | PASS — Iowan / system |
| 8. Fake BE0 | PASS — `KBO/BTW: nog niet toegekend` | PASS — same |
| 9. Missing privacy | PASS — `/privacy.html` linked from footer | **FAIL** — `/privacy.html` 404; footer has no privacy link |
| 10. Cookie banner, zero trackers | PASS — no banner; privacy states no trackers | PASS — no banner, no trackers |
| **Surface** | **FAIL** | **FAIL** |

`sovereignforge.surge.sh` also has `/pakketten.html` (euro + USDC columns), `/betalen.html` (USDC allowed), `/contact.html` (mail only). Those inner pages still inherit the host `robots.txt` FAIL.

### Live kit hosts

All eleven kit hosts plus the three English tool hosts return `robots.txt`:

```
User-agent: *
Disallow: /
```

That is a **FAIL** on check 5 for every kit host.

| Host | 1 USDC-face | 2 Demo | 3 FACTUUR | 4 Footer | 6 Cream/Inter | 7 GFonts | 8 BE0 | 9 Privacy | 10 Cookie | Surface |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| club-site-kit-treasury | PASS (named club demo, not a price shop) | PASS — ZWV De Golfbreker | PASS | PASS | PASS (club theme) | PASS | PASS | **FAIL** — no privacy | PASS | **FAIL** (robots + privacy) |
| menu-kit-treasury | **FAIL** — title/price `199 USDC` | PASS | PASS (VOORBEELD) | PASS | **FAIL** cream shop wrap | PASS | PASS | **FAIL** | PASS | **FAIL** |
| sponsor-kit-treasury | **FAIL** — kicker `199 USDC` | PASS — iframe `offerte.html` | PASS | PASS | **FAIL** cream wrap | PASS | PASS | **FAIL** | PASS | **FAIL** |
| lid-kit-treasury | **FAIL** — kicker `349 USDC` | PASS — iframe `lid.html` | PASS | PASS | **FAIL** cream wrap | PASS | PASS | **FAIL** | PASS | **FAIL** |
| vakman-kit-treasury | **FAIL** — `249 USDC` | PASS | PASS | PASS | **FAIL** cream | PASS | PASS | **FAIL** | PASS | **FAIL** |
| inbox-ops-treasury | **FAIL** — `299 USDC` | PASS — “Alleen demo” | PASS | PASS | **FAIL** cream | PASS | PASS | **FAIL** | PASS | **FAIL** |
| pipeline-treasury | **FAIL** — `399 USDC` | PASS — reset-demo | PASS | PASS | **FAIL** cream | PASS | PASS | **FAIL** | PASS | **FAIL** |
| peppol-chase-treasury | **FAIL** — `399 USDC` | PASS — file list | PASS (nooit FACTUUR) | thin but not empty | **FAIL** cream | PASS | PASS | **FAIL** | PASS | **FAIL** |
| dual-invoice-treasury | **FAIL** — title/amount `490 USDC` | PASS — working offerte | PASS — OFFERTE, not FACTUUR stamp | PASS | cream sheet (product) | PASS | PASS | **FAIL** | PASS | **FAIL** |
| peppol-ready-treasury | **FAIL** — `249 USDC` | PASS — file list | PASS — “nooit FACTUUR” | PASS | **FAIL** cream | PASS | PASS | **FAIL** | PASS | **FAIL** |
| solana-invoice-treasury | mixed (EUR-first title `€49` on later fetch; still cream wrap) | PASS — open voorbeeld | PASS | PASS | **FAIL** cream wrap | PASS | PASS | **FAIL** | PASS | **FAIL** (robots + privacy + cream) |
| csv-cleaner / form-to-email / rss-to-webhook | **FAIL** English USDC tools | PASS (the tool is the page) | PASS | PASS | **FAIL** cream | PASS | PASS | **FAIL** | PASS | **FAIL** |

No live page loaded Inter or Google Fonts. No live page invented a `BE0` number. No live page showed a cookie banner.

## What would have to be true for PASS

Shop faces (`sovereignforge.surge.sh` and any catalog that is still public):

1. Euro on the face; USDC only on betalen / after kit choice.
2. A real demo (not a paywall) for every kit sold from that face.
3. Stamp OFFERTE/VOORBEELD — never FACTUUR on the document.
4. Footer with identity + privacy link, not empty.
5. `robots.txt` must **not** `Disallow: /` on the public shop.
6. Chalkboard (or other non-Inter, non-cream-card) shop face.
7. No Google Fonts.
8. No fake KBO/BTW number.
9. Privacy page on the shop origin, linked in the footer.
10. No cookie banner unless there are actual trackers.

This repo’s `index.html` / `catalog.html` currently fail that list and are not the live chalkboard shop. Until shop HTML lives in git **or** the live hosts pass, REVIEWER stays **FAIL**.
