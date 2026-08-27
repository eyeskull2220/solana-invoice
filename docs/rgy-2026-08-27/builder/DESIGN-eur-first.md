# DESIGN — EUR-first voorstel (designs out #159 RED)

**Seat:** Builder / DESIGN
**Date of this page:** 2026-08-27
**File:** `docs/rgy-2026-08-27/builder/DESIGN-eur-first.md`
**Stage:** DESIGN only. **Docs only. No shop HTML. No mail. No Surge. Do not start CODE.**

This file is the DESIGN of record for the EUR-first shop. A **different** design reviewer scores **this** page. CODE starts only if that review is GREEN. A PLAN GREEN does not substitute.

> **For agentic workers:** do not implement from this PR. Do not write `shop/sovereignforge/*.html`. Do not send mail. Do not publish to Surge. Do not port [PR #137](https://github.com/eyeskull2220/solana-invoice/pull/137).

**The object:** one page a Belgian club secretaris in Geel will forward tonight. Later live URL: **https://sovereignforge.surge.sh/**. Later git origin: **`shop/sovereignforge/`**. Face is Dutch. Stamp is **OFFERTE**. Operator is **Sasha · SovereignForge (Geel)**. Contact: **sasha.de.vree.rene@gmail.com**.

---

## 0. Sequence (lock)

Honour [PR #195](https://github.com/eyeskull2220/solana-invoice/pull/195) PLAN GREEN and [PR #192](https://github.com/eyeskull2220/solana-invoice/pull/192) RESEARCH GREEN.

1. RESEARCH lock — GREEN (#192 on #185).
2. PLAN lock — GREEN (#195 on #188).
3. **This DESIGN** — this file.
4. **A different design reviewer** scores this file. GREEN only if there is no RED and no YELLOW on the scorecard in §16.
5. **THEN CODE:** one pass onto `https://sovereignforge.surge.sh/` from `shop/sovereignforge/`. Preview, then cutover. **Do not surge `main`.**

**After this file: design review. Not CODE. Not live Surge.**

---

## 1. What this DESIGN closes

[PR #159](https://github.com/eyeskull2220/solana-invoice/pull/159) `03-adv-design.md` scored the live chalkboard **RED** (heuristic 9/32). Named reds: **chalkboard costume**, **coin in the first viewport**. That file is an exhibit. It is **not** closed DESIGN. This page is the replacement world.

[PR #137](https://github.com/eyeskull2220/solana-invoice/pull/137) chalkboard shop HTML is **PARKED CODE**. Do not continue that look. Do not copy `--board` / `--chalk` / `--brass` / `--wood`. Do not copy Young Serif + Atkinson as the shop face. Do not merge #137 as the EUR pass.

[PR #119](https://github.com/eyeskull2220/solana-invoice/pull/119) unpublished shop is a **second costume** (iron `#07090c`, ember `#ff3d12`, brass, Bricolage Grotesque, fixed mobile dock). Prices there are the frozen six. **Paint is not.** Do not port that chrome. Later origin path `shop/sovereignforge/` is the deploy folder; this DESIGN paints it.

[PR #130](https://github.com/eyeskull2220/solana-invoice/pull/130) asked for “paper + Young Serif + Atkinson.” That split is how the chalkboard survives. **Killed.** New type. New paper. Not a softer board.

Live [sovereignforge.surge.sh](https://sovereignforge.surge.sh/) this run is still USDC-first world-state. This file does not claim the live origin already moved.

---

## 2. GREENS kept (RESEARCH + PLAN)

These stay. DESIGN paints them. DESIGN does not reopen prices, jobs, or sequence.

| Keep | Lock |
| --- | --- |
| Frozen six | menu **€199**, sponsor **€199**, vakman **€249**, inbox-ops **€299**, lid **€349**, club **€900**. Integers. No seventh chip. Order: menu → sponsor → vakman → inbox-ops → lid → club. |
| EUR-first public face | No `USDC`, `Solana`, `Phantom`, `crypto`, or wallet on the public face. No treasury address in `<title>`, `<h1>`, lede, chips, CTAs, or meta. |
| Privacy | STORE **Versie 3 — 27 augustus 2026**. Copy lock is PLAN §8. This DESIGN only paints the chrome around it. |
| Betalen | **Betaalgegevens na akkoord.** No address, no USDC, no QR, no IBAN, no card form on that page. |
| robots | `User-agent: *` then `Allow: /` on the shop and the six kit hosts. (CODE. Not this PR.) |
| Kill | Freelancer line. Leftover **9/49**. **Peppol Ready**. **Dual-invoice**. **Eén klus**. **Pipeline / chase** as home / pakketten chips. “Elf live kits.” `SITE.md`. |
| Origin | `shop/sovereignforge/` → `https://sovereignforge.surge.sh/` only. Do not surge `main`. Leftover [#111](https://github.com/eyeskull2220/solana-invoice/pull/111) is not the shop. |
| Stamp | OFFERTE / VOORBEELD. Never FACTUUR as a document stamp. Negation `geen wettelijke factuur` is allowed. `KBO/BTW: nog niet toegekend`. No invented `BE0`. No FAVV. |
| Address | Secretaris as **u**. Bestuur as **jullie**. No `je` / `jouw` on shop-face strings. |
| Operator | Sasha · SovereignForge · Geel. Not “Demo freelancer · Antwerpen.” Not Desk Noord. Not hire-me. |
| `editor.html` | STOP. Cite-only. Do not feature. Do not rebuild. |
| Voorbeeld names | Stencils, not Tos. Voorbeeldharmonie / Voorbeeldkeuken / Voorbeeldloodgieter / ZWV De Golfbreker (VOORBEELD). Not mail targets. |

Uitkomst lines (PLAN, do not invent a seventh):

| Kit | Uitkomst |
| --- | --- |
| Menukaart + allergenen | Printkaart plus QR naar de EU-14. Geen FAVV-claim. |
| Sponsorblad vzw | Eén printblad naar het bestuur. Drie voorbeeldpakketten. |
| Vakman one-pager | Eén blad voor de zaak. Contact, diensten, voorbeeldofferte. |
| Inbox-ops | Intake tot herinnering voor één KMO. Geen freelancer-desk. |
| Lid-inschrijving | Aanvraag naar het secretariaat. Formulier + jaarbijdrage-tabel. |
| Club- of vzw-site | Home, agenda, lid worden, contact. Maatstaf: ZWV De Golfbreker. |

Club maatstaf on the **shop face** is a text line plus **Open het voorbeeld**, not a 3-band screenshot. The demo remains VOORBEELD (not a To). Shop copy may keep the PLAN uitkomst sentence. Shop **paint** must not embed the gold/navy/cream header as proof.

---

## 3. Conflicts closed (so the reviewer does not re-open them)

| Source | Said | This DESIGN |
| --- | --- | --- |
| #159 RED-1 replacement copy | `Prijs €774` | **Out.** €774 is leftover omrekening of 900 USDC. Club face is **€900**. |
| #159 NOTES | Pick **one** kit; eleven died Persuade | One **forwarded URL** (`/`). Six posten on that blad. Not eleven. Not a seventh. First viewport carries the six euro integers as a prijsregel, not a settlement ticker. |
| #159 RED-4 | Shop home must not be a cream card grid | PLAN IA (hero + six units) stays. Paint is **voorstel-posten** (hairline rows), not sage rounded cards. |
| #159 GREEN-4 / #130 | Young Serif + Atkinson | **Burn with the board.** That pairing *is* the chalkboard. New type in §6. |
| #159 RED-1 | Settlement on Betalen after choice | PLAN is stricter and wins: Betalen has **no** address, QR, USDC, or chain. Gegevens per mail after akkoord. |
| #159 YELLOW-4 | Contact H1 `Alleen mail.` is a locked door | PLAN copy lock stays. DESIGN paints an OFFERTE-blok around it (what to mail). |
| #119 | Iron / ember / brass / Bricolage / dock | **Burn.** Dark app costume is not a keukentafel-voorstel. |
| #137 | Euro chalkboard shop HTML | **PARKED.** Not this look. |

---

## 4. The object — one blad, not a theme

A **keukentafel-voorstel** is a sheet the secretaris can:

1. Open on a phone without a costume header.
2. Screenshot or print as one page that still makes sense.
3. Forward to bestuur with subject `voorstel — ter goedkeuring vanavond`.
4. Defend in the notulen in **euro**, OFFERTE, six kits, one city (Geel), one name (SovereignForge), one person (Sasha).

The shop URL **is** the voorstel. It is not a lobby in front of the voorstel. It is not a pub chalkboard. It is not a cream SaaS catalog. It is not a dark app with a dock.

**Impeccable:** refinement preserves; redesign replaces. This pass is redesign. Do not split the difference (cream board, brass on paper, Young Serif on white, Bricolage on white, “softer chalkboard”). That is how the costume survives.

---

## 5. Burn list (paint)

CODE that ships any row below has not implemented this DESIGN.

### 5.1 Chalkboard (live + #137)

| Token / surface | Value | Status |
| --- | --- | --- |
| `--board` | `#0f190f` / `oklch(0.20 0.025 145)` | **Burn** |
| `--chalk` | `#e8e9da` | **Burn** |
| `--brass` | `#ca9d33` / `#e0b44a` | **Burn** |
| `--wood` | `#432610` | **Burn** |
| CSS comment | `/* SovereignForge — chalkboard. */` | **Burn** |
| Wood bezel | `border: 6px solid var(--wood)` around 390×844 PNGs | **Burn** |
| Brass scrollbar / `::selection` | brass on board | **Burn** — use OS scrollbar |
| Type pairing | Young Serif + Atkinson Hyperlegible | **Burn** on the shop face |
| Fallback serifs | Iowan Old Style, Palatino in `--font-display` | **Burn** |

### 5.2 PR 119 iron / ember (unpublished, not the look)

| Token / surface | Value | Status |
| --- | --- | --- |
| `--iron` / `--slate` | `#07090c` / `#12181f` | **Burn** |
| `--ember` | `#ff3d12` | **Burn** |
| `--brass` (119) | `#e0b44a` | **Burn** |
| Type | Bricolage Grotesque | **Burn** |
| `.dock` | fixed two-button bar on mobile | **Burn** |
| Repeating slant hatch on `body` | costume texture | **Burn** |

### 5.3 Cream catalog slop (treasury-tools + kit generators)

| Surface | Value | Status |
| --- | --- | --- |
| Cream paper as shop identity | `#f4f1ea` / `#f6f3ee` / `#f3efe6` | **Burn on the shop** |
| Sage / forest accent | `#123c2e` / `#0c4a36` | **Burn on the shop** |
| Rounded grocery cards | `#fffdf8` + border-radius ≥ 8px as the shop grid | **Burn** |
| Inter | Google Fonts or self-hosted | **Burn** — never load |
| Iowan / Palatino as shop face | cream-kit leftover | **Burn on the shop** |

Print **artefacts** (inner `menu.html`, `lid.html`, sponsor `offerte.html`, vakman `offerte.html`) may stay paper sheets. That is the product. The **shop wrap** and **kit sell wrap** use §6–§7 only.

### 5.4 3-band club costume as shop chrome

| Layer | Value | Status |
| --- | --- | --- |
| Gold demo tape | `#d9a441` | **Not on the shop.** Not in the first viewport. |
| Navy hero | `#0b283c` | **Not on the shop.** |
| Cream rest | `#efebe3` | **Not on the shop.** |
| Sunburst / pinstripe hero | conic + repeating-linear | **Not on the shop.** |
| “Live telefoonbeeld” PNG | 390×844 in a frame | **Burn.** No phone PNGs on shop home. |

The Golfbreker **demo site** (the deliverable) is a named VOORBEELD. CODE does not restack that inner site in this shop pass. CODE does not **sell** it by screenshotting the 3-band header on `sovereignforge.surge.sh`.

### 5.5 Coin (first viewport and the whole shop face)

Forbidden on home, pakketten, betalen, contact, privacy — including `<title>`, meta, H1, lede, prijsregel, posten, CTAs, footer:

`USDC` · `Solana` · `Phantom` · `crypto` · `wallet` · `Charge blijft` · `omrekening` · `Kraken` · `FOD-koers` · `900 USDC` · `±€774` · `€774` · `1 USDC` · treasury address `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3` · mint id · `Betaal N USDC`

€774 is not “the euro price.” It is the leftover conversion. Club is **€900**.

---

## 6. Type (professional, not leftover HTML, not a costume)

One pairing for every shop page and every kit **sell wrap**.

| Role | Family | Weight | Size | Notes |
| --- | --- | --- | --- | --- |
| Display (H1, H2) | **Source Serif 4** | 600 | H1 2.00rem (390) / 2.50rem (1280). H2 1.25rem / 1.375rem | Line-height 1.25. Letter-spacing 0. Not compressed. Not 800 grotesk. |
| Body, nav, footer, lede | **Source Sans 3** | 400 | 17px (390) / 18px (1280) | Line-height **1.5**. Measure 36rem for lede, 40rem for prose. |
| Price | **Source Sans 3** | 600 | 1.25rem in the prijsregel; 1.375rem on a post | `font-variant-numeric: tabular-nums lining-nums`. Euro sign + integer. No decimals. No `±`. |
| Stamp OFFERTE | **Source Sans 3** | 600 | 0.75rem | Letter-spacing `0.12em`. Uppercase. Not rotated. Not a gold badge. |
| Wordmark | **Source Sans 3** | 600 | 0.9375rem | `SovereignForge`. Not steel, not brass, not 800 negative tracking. |

**Stacks (exact):**

```
--font-display: "Source Serif 4", Georgia, "Times New Roman", serif;
--font-body:    "Source Sans 3", "Segoe UI", system-ui, sans-serif;
```

**Never in any stack:** Inter, Young Serif, Atkinson Hyperlegible, Iowan Old Style, Palatino, Bricolage Grotesque, Comic Sans, Arial-as-the-designed-face.

**Hosting:** self-hosted WOFF2 in `shop/sovereignforge/fonts/`. Latin + Latin-ext (é, ë, ï, è needed). `font-display: swap`. **No Google Fonts. No Adobe CDN. No bunny.net.**

Files CODE vendors (SIL OFL):

- `source-serif-4-600.woff2` (+ latin-ext if split)
- `source-sans-3-400.woff2` (+ latin-ext if split)
- `source-sans-3-600.woff2` (+ latin-ext if split)

Italic is not required for this pass.

This is a **letter**, not a startup landing and not leftover invoice HTML (browser default, no `font-face`, 16px Times in a dump).

---

## 7. Colour, spacing, chrome

### 7.1 Colour — ink on a sheet

Not cream. Not board. Not iron. Not sage. Not gold tape.

| Token | Hex | Use |
| --- | --- | --- |
| `--paper` | `#ffffff` | `body` background. White sheet. |
| `--ink` | `#171717` | Text, wordmark, filled CTA, rules that are “written.” |
| `--mute` | `#4a4a4a` | Lede, uitkomst, footer meta. Contrast ≥ 7:1 on `--paper` (WCAG AAA for body). |
| `--rule` | `#d4d4d4` | Hairlines between posten, under header, over footer. 1px. |
| `--stamp` | `#8b1515` | OFFERTE box only. Not a wash. Not a hero. Contrast of stamp text on paper: the box is **outline** (`1px solid var(--stamp)`; text `--stamp`), never a filled red banner. |
| `--focus` | `#171717` | `:focus-visible { outline: 2px solid var(--ink); outline-offset: 3px; }` |

Links: `--ink`, underline, underline-offset 0.15em. Hover: underline thickens to 2px. **No brass. No ember. No sage.**

`::selection`: `--ink` on `#e8e8e8`. Not brass.

Visited: same as link. This is a five-page shop, not a web of articles.

### 7.2 Spacing (8px base)

Leftover HTML fails as: no vertical rhythm, 936px tables, 4437px phone stacks, 52rem min-width.

| Token | Value | Use |
| --- | --- | --- |
| `--space-1` | 4px | Stamp padding |
| `--space-2` | 8px | Tight gaps (stamp to kicker) |
| `--space-3` | 16px | H1 → lede; name → uitkomst |
| `--space-4` | 24px | Page padding 390; CTA gap |
| `--space-5` | 40px | Header → hero; lede → prijsregel; section gaps |
| `--space-6` | 64px | Footer offset; desktop page padding |

**Page padding:** 24px (390) / 48px (≥960).
**Max width:** 40rem for hero + prose; **42rem** for the zes posten (still one column). Never `min-width: 52rem`. Never a 9-column table.
**Header height:** auto. Nav may wrap. Min tap 44×44.
**Posten:** padding 20px 0; hairline `border-bottom: 1px solid var(--rule)`. No box-shadow. No border-radius. No sage fill. No `#fffdf8` card.

**Radius:** 0 everywhere. A voorstel is square corners.

**Buttons:** min-height 44px; padding 12px 16px; filled CTA is `--ink` background, `#ffffff` text, 0 radius. Ghost is 1px `--ink` outline, `--ink` text, transparent fill. Width: hug on ≥960; full-width stacked on 390.

### 7.3 Shared chrome (every shop page)

PLAN IA, this paint:

- `lang="nl"`
- Skip link “Naar de inhoud” (ink on paper, not brass)
- Header: wordmark **SovereignForge** → `/`. Under or beside, 0.75rem mute: `Geel`.
- Nav: **Home · Pakketten · Contact · Privacy**. `aria-current="page"` = `font-weight: 600` + `border-bottom: 1px solid var(--ink)`. Not brass.
- **Betalen is not a primary tab.** Footer link, label still `Betalen`, page is the akkoord page. Never “Betaal USDC”.
- Stamp in the hero (home) or under H1 (inner pages): `OFFERTE` in the stamp box.
- Footer: §11. Not empty. Not a KBO punchline.

No sticky dark bar. No fixed dock. Header may be sticky **white** with a 1px `--rule` under it (so print/screenshot still looks like a blad).

Favicon: ink letters `SF` on white, square, no coin, no board.

---

## 8. First viewport (the #159 RED that must die)

The voorzitter’s screenshot of the first screen is the product. If that screenshot contains a coin, a board, a wood phone, or brass, DESIGN has failed.

### 8.1 Copy in the first viewport (Dutch, euro, u)

**`<title>`:** `SovereignForge — voorstel voor het bestuur`

**Meta description:** `OFFERTE-kits voor club, vzw en KMO. Zes pakketten in euro. Geen wettelijke factuur.`

**Kicker:** `Sasha · SovereignForge · Geel`

**Stamp:** `OFFERTE`

**H1 (keep):** `Voor de secretaris die vanavond nog een voorstel naar het bestuur stuurt.`

**Lede:** `Eén OFFERTE-kit die u doorstuurt. Prijzen in euro. Geen kaart, geen IBAN op deze pagina. Geen wettelijke factuur.`

No second sentence about settlement. No `Charge blijft`. No `je`.

**Prijsregel (must be in the first viewport at 390 and at 1280):**

`€199 · €199 · €249 · €299 · €349 · €900`

Mute caption under it: `Zes OFFERTE-kits. Geen wettelijke factuur.`

**CTA row:**

1. Primary: `De zes pakketten` → `#pakketten` on home (same page) and also the same six posten listed below. On a short mobile viewport the hash is the six posten.
2. Secondary: `Vraag een OFFERTE` → `/contact.html`

Never `Betaal 900 USDC`. Never `Alle 11 pakketten`. Never `Bekijk de pakketten` as a brass pill over a ticker.

### 8.2 Wireframe — 1280×800 (no scroll)

```
[ skip ]
SovereignForge          Home  Pakketten  Contact  Privacy
Geel
─────────────────────────────────────────────────────────
Sasha · SovereignForge · Geel          [ OFFERTE ]

Voor de secretaris die vanavond nog
een voorstel naar het bestuur stuurt.

Eén OFFERTE-kit die u doorstuurt. Prijzen in euro.
Geen kaart, geen IBAN op deze pagina. Geen wettelijke factuur.

€199 · €199 · €249 · €299 · €349 · €900
Zes OFFERTE-kits. Geen wettelijke factuur.

[ De zes pakketten ]   [ Vraag een OFFERTE ]
─────────────────────────────────────────────────────────
  (first posten may peek; phone PNG must not exist)
```

Coin: **absent**. Board: **absent**. Wood frame: **absent**.

### 8.3 Wireframe — 390×844 (no scroll)

```
SovereignForge    Home
Geel              Pakketten
                  Contact  Privacy
──────────────────────────────────
Sasha · SovereignForge · Geel
[ OFFERTE ]

Voor de secretaris die vanavond
nog een voorstel naar het
bestuur stuurt.

Eén OFFERTE-kit die u doorstuurt.
Prijzen in euro. Geen kaart, geen
IBAN op deze pagina. Geen
wettelijke factuur.

€199 · €199 · €249
€299 · €349 · €900
Zes OFFERTE-kits. Geen wettelijke factuur.

[ De zes pakketten ]
[ Vraag een OFFERTE ]
```

Nav **wraps**. It does not overflow. Prijsregel **wraps to two lines** of tabular figures. Still in the first 844px. H1 may wrap to four lines; that is allowed. A settlement paragraph is not.

**Hard fail if, in the first 844px at 390 or the first 800px at 1280, any of these appear:** USDC, Solana, Phantom, crypto, wallet, chalkboard green, wood bezel, 390×844 PNG, brass CTA, `€774`, freelancer, Peppol Ready, dual-invoice, één klus, pipeline, chase, 9, 49 as a leftover SKU.

### 8.4 What is *not* in the first viewport

- The Golfbreker 3-band site, as iframe or PNG
- A conversion ticker
- A QR
- A pay-to address
- Eleven kits
- “Live telefoonbeeld”
- KBO/BTW as the hero’s last line (voids live on Privacy; footer close is §11)

---

## 9. Home below the fold — zes voorstel-posten

PLAN: home is one hero + six cards. DESIGN: the six units are **posten on the blad**, id `pakketten`.

Each post, in order:

```
Menukaart + allergenen                         €199
Printkaart plus QR naar de EU-14. Geen FAVV-claim.
geen BTW-factuur (OFFERTE)
Open het voorbeeld · Vraag deze OFFERTE
```

**Desktop (≥960):** name left, price right, same baseline. Uitkomst full width under. Links in a row.

**390:** name, then price on the next line (not a squeezed two-column that truncates). Then uitkomst. Then links stacked, each min-height 44px.

**Open het voorbeeld** → that kit’s live host (PLAN table). **Vraag deze OFFERTE** → `mailto:sasha.de.vree.rene@gmail.com?subject=OFFERTE%20<slug>` **or** `/contact.html`. Same on every post. Never a pay CTA.

No images in the posten. No iframe of the demo. The voorbeeld is a link, on the blad, next to the euro.

Home at 390 without phone frames should land **under ~2200px**, not 4437px. Six posten × ~180px + hero ~520px + footer ~280px ≈ 1900px. If it exceeds 2400px, the posten are too fat — cut padding, do not add pictures.

No “Alle 11 pakketten”. No leftover chips.

---

## 10. Inner shop pages (paint)

Copy locks from PLAN §7–§8. Paint from §6–§7. First viewport of **each** inner page: euro-or-identity, no coin, no board.

### 10.1 Pakketten — `pakketten.html`

**H1:** `Pakketten`

**Lede:** `Zes OFFERTE-kits. Prijzen in euro. Open het voorbeeld vóór u akkoord gaat.`

First viewport (390 and 1280): H1 + lede + the same prijsregel `€199 · €199 · €249 · €299 · €349 · €900`. Then the same six posten as home. No 9-column table. No `min-width: 52rem`. No horizontal scroll at 390. No USDC column. No “Elf live kits.” No junk SKU names as rows, chips, or nav.

Drop-list (must not appear as a price row, chip, or nav item):

- Lead tot offerte / pipeline (`pipeline-treasury.surge.sh`)
- Peppol Client-Chase (`peppol-chase-treasury.surge.sh`)
- Dual-invoice (`dual-invoice-treasury.surge.sh`)
- Peppol Ready (`peppol-ready-treasury.surge.sh`)
- Eén klus / Solana Invoice (`solana-invoice-treasury.surge.sh`)
- CSV Cleaner, Form to Email, RSS to Webhook
- Offertebestand €9, studio-tools €49, één opdracht €49
- km-log, freelance-contract, retainer-invoice, dagtarief, FAQ, UTM, waitlist, paywall, intake, link-in-bio as shop rows
- Seizoenskaart or named-club as SKU #7

### 10.2 Betalen — `betalen.html`

This is a **step**, not a wallet panel, not a chalkboard pay pad (`#fffdf0` QR). Same white sheet.

**`<title>`:** `Betalen — SovereignForge`

**H1:** `Betaalgegevens na akkoord.`

**Lede:** `Hier staan geen rekeningnummers en geen ontvangstadres. Geen kaartformulier. Na uw akkoord op de OFFERTE sturen wij de gegevens apart, per mail.`

**Volgorde** (numbered in body sans, not ember circles):

1. Kies een van de zes pakketten. Open het voorbeeld.
2. Bevestig de OFFERTE per mail naar `sasha.de.vree.rene@gmail.com`. Dit is geen wettelijke factuur.
3. Daarna volgen de betaalgegevens. Niet eerder, niet op deze pagina.

**Prijzen (hele euro)** — the six rows only, same posten treatment, no radios that reveal a pay panel, no hash-deep-links that skip akkoord.

**Identiteit:** `KBO/BTW: nog niet toegekend.` No invented number. No IBAN.

Forbidden on this page: treasury address, mint, QR, copy-address, `USDC`, `Solana`, `Phantom`, wallet, radios that unhide a pay panel.

First viewport: H1 + lede. No QR. No address. The six euro integers may sit below the volgorde; they must not appear as `N USDC`.

### 10.3 Contact — `contact.html`

**H1 (PLAN lock):** `Alleen mail.`

**Body (OFFERTE-blok, this DESIGN):** Geen formulier. Geen telefoon. Mail is voor het voorstel of het akkoord. Zeg wat u stuurt: **kit-naam + club- of zaaknaam**.

Mailto: `sasha.de.vree.rene@gmail.com`

Colophon on this page: `SovereignForge · Geel / België · KBO/BTW: nog niet toegekend.`

No `hello@studio.example` on the shop contact page. No freelancer / hire-me / day-rate. No Desk Noord. No Antwerpen as the operator city.

Paint: the mail address is 1.125rem, ink, underlined. Not a void. Not a locked brass door.

### 10.4 Privacy — `privacy.html`

Copy: PLAN §8, **Versie 3 — 27 augustus 2026**, verbatim locks (Sasha · Geel · `sasha.de.vree.rene@gmail.com`; host/mailhost **niet geverifieerd**; Gmail buiten de EER alleen om te antwoorden; no USDC / IBAN / kaartnummer; no SCC / adequacy; no AVG-conform badge; no banner).

Paint: same sheet. Prose measure 40rem. H1 `Privacy`. Lede is the versie line. Voids (`KBO/BTW: nog niet toegekend`, geen Peppol Access Point) **live here**, not as the shop footer’s last beat.

This DESIGN PR does not write `privacy.html` onto disk.

---

## 11. Footer as a voorstel close (designs out #159 RED-6)

The live footer **exists** and is a compliance dump. Peak–end is ticker → gmail + geen KBO. Replace the **close**, keep the identity.

**Order (top to bottom):**

1. **Close (body, ink):** `Dit blad is het voorstel. Mail het naar het bestuur. Na akkoord sturen wij de betaalgegevens apart.`
2. **Who (body, ink):** `Sasha · SovereignForge · Geel`
3. **Mail:** `sasha.de.vree.rene@gmail.com`
4. **Nav:** Home · Pakketten · Contact · Privacy · Betalen
5. **Quiet meta (mute, last):** `OFFERTE / VOORBEELD · geen wettelijke factuur` then, on a new line, `KBO/BTW: nog niet toegekend` as a **secondary** fact, not the punchline. Privacy link already in (4).

Do **not** end on `geen Peppol Access Point`. That negation lives on Privacy.

No freelancer. No Desk Noord. No USDC. No “elf kits.”

---

## 12. Print (the secretaris actually prints this)

`@media print` on **every shop page**:

- White paper, ink text, no background fills on buttons (ghost them).
- Hide skip, hide sticky header shadow, hide nav wrap if it repeats; keep wordmark + Geel.
- Show H1, lede, prijsregel, zes posten, footer close.
- No `390×844` images (none exist).
- Page margins 12mm. A4. Colour is ink; stamp outline prints.

Live chalkboard cannot print as a voorstel. This sheet can.

---

## 13. Mobile (390) — professional, not leftover HTML

Leftover HTML on a phone is: horizontal scroll, truncated columns, overlapping nav, 16px blue links, no tap targets, 4437px of stacked PNGs.

This DESIGN:

| Rule | Spec |
| --- | --- |
| Viewport | `width=device-width, initial-scale=1`. No `user-scalable=no`. |
| Horizontal scroll | **0** on home, pakketten, betalen, contact, privacy. `overflow-x: hidden` is not the fix — do not set a min-width above 100%. |
| Tap | Every nav link, CTA, and post link ≥ 44×44. |
| Nav | Wraps. No hamburger required. If a details/summary is used, the summary is “Menu”, 44px, ink outline — **not** a brass burger on a board. Prefer wrap. |
| Prijsregel | May wrap. Tabular nums. No comma-USDC. |
| Dock | **None.** |
| Safe area | Footer padding includes `env(safe-area-inset-bottom)`. |
| Home length | Target ≤ 2200px at 390. Hard cap 2400px. |
| Contrast | Body text ≥ 7:1. Mute ≥ 7:1 on white (`#4a4a4a` on `#ffffff` is ~8.6:1). Stamp `#8b1515` on white is ~8.3:1. Filled CTA white on `#171717` is fine. |

Also walk **1280**. Same blad, wider measure, price on the right of each post.

---

## 14. Kit sell wraps (same pass, same paint)

Home links six live hosts. A shop that says €199 while inbox-ops still says `299 USDC` is not one CODE pass (PLAN). DESIGN for those **sell wraps**:

- Same `--paper` / `--ink` / type as the shop. **Not** chalkboard. **Not** iron/ember. **Not** cream-sage generator. **Not** 3-band gold tape on the wrap.
- Face prices: €199 / €199 / €249 / €299 / €349 / €900.
- Kill **Demo freelancer · Antwerpen** (inbox-ops). Use `Studio Noord · demo KMO · Antwerpen` or drop the kicker. Never hire-me.
- CTA: Open het voorbeeld / Vraag deze OFFERTE / Betaalgegevens na akkoord. Never `Betaal 299 USDC`.
- Footer Privacy → `https://sovereignforge.surge.sh/privacy.html` (one policy).
- `robots.txt` Allow.
- Inner **artefacts** (the menukaart, the lid form, the sponsorblad, the vakman OFFERTE, the Golfbreker pages) stay the product documents. CODE does not restyle Golfbreker into chalkboard. CODE does not screenshot Golfbreker onto the shop home.

`editor.html` stays unfeatured (STOP).

Demo mail **inside** kits: RFC 2606 (`hello@studio.example`, `info@golfbreker.example`). Operator Gmail is the **shop** contact, not the public demo.

---

## 15. CODE implements after GREEN design review — not from this PR

Closed file set (PLAN §6). Styles and fonts from **this** DESIGN, not from #137, not from #119, not from live chalkboard.

```
shop/sovereignforge/
  index.html
  pakketten.html
  betalen.html
  contact.html
  privacy.html
  robots.txt
  styles.css          # tokens in §6–§7
  fonts/              # Source Serif 4 600, Source Sans 3 400/600
  favicon.svg
  favicon.ico
```

No `catalog.html`. No `SITE.md`. No `kit-pay.html`. No `betalen.js` that paints a treasury address. No `previews/*.png` phone dump. If a later CODE wants a preview, it is not a 4437px wood stack; this DESIGN prefers **zero** preview images on the shop.

Grep locks after CODE (not this PR): PLAN §12 plus `wallet` and `€774` and `freelancer` and `--board` and `Young Serif` and `Bricolage` and `Inter` and `Atkinson` = 0 on `shop/sovereignforge/`.

**This DESIGN PR does not run those greps against HTML it did not write. It does not surge. It does not land the tree.**

---

## 16. Scorecard for the **next** reviewer (this file)

GREEN only if this page has **no RED and no YELLOW**. One yellow fails GREEN.

| Gate | What GREEN looks like on **this markdown** |
| --- | --- |
| Designs out #159 RED-1 (coin in first viewport) | First viewport spec is euro-only; €774 killed; forbidden-string list includes USDC / Solana / Phantom / crypto / wallet |
| Designs out #159 RED-2 (chalkboard costume) | Burn table for `--board` / `--chalk` / `--brass` / `--wood`; Young Serif + Atkinson burned; #137 parked |
| Does not continue #137 | Explicit PARKED; CODE must not port that CSS |
| Does not continue #119 iron/ember/dock | Explicit burn |
| One forwarded page | Shop `/` is the blad a secretaris forwards |
| Dutch · OFFERTE · Sasha · Geel · mail | Copy locked |
| Frozen six integers | €199 / €199 / €249 / €299 / €349 / €900 |
| Privacy STORE Versie 3 | Points at PLAN §8; no Versie 1 on-chain USDC |
| Betalen = Betaalgegevens na akkoord | No QR / address / coin on that page |
| Kill leftover chips | 9/49, Peppol Ready, dual-invoice, één-klus, pipeline/chase, freelancer line |
| Type specified | Source Serif 4 + Source Sans 3; Inter forbidden |
| Spacing specified | 8px scale; 0 radius; 40–42rem measure; no 52rem table |
| Mobile specified | 390 first viewport wireframe; no horizontal scroll; no dock; home length cap |
| u / jullie | `je` killed on the face |
| No shop HTML / mail / Surge / CODE in this PR | This file only |
| Next seat | Design review, then CODE |

Do not GREEN this file because the live shop moved. Do not hold this file until the live shop moves. Do not treat a later CODE GREEN as a DESIGN GREEN.

---

## 17. This run

| Did | Did not |
| --- | --- |
| Wrote **one** DESIGN page that replaces the chalkboard world | Shop HTML, kits, CSS on disk, fonts on disk |
| Designed out #159 RED-1 (coin) and RED-2 (board), plus RED-3..6 as paint | Treat #159 as closed DESIGN; polish `--board` |
| Locked first viewport: euro prijsregel, no coin, no wood PNG | Keep €774 / 900 USDC as a “euro” face |
| Named Source Serif 4 + Source Sans 3, white sheet, ink, stamp outline | Pick Inter, Young Serif, Atkinson, Bricolage, cream-sage, iron-ember |
| Kept RESEARCH/PLAN GREENS (six, Versie 3, betalen, kill list, origin) | Reopen prices; add a seventh chip; surge `main` |
| Parked #137 and #119 as costumes not to continue | Port chalkboard HTML; port the dock |
| Locked next seat: **design review**, then CODE | Start CODE; send mail; publish Surge |

**DESIGN stage after this file:** the #159 reds are designed out on paper. **Next seat: a different design reviewer.** Not live Surge. Not CODE.

End. No shop HTML. No mail. No Surge. Do not start CODE.
