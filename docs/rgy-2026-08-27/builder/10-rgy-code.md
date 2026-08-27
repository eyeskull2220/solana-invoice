# REVIEWER — Builder CODE stage RGY

**Seat:** REVIEWER  
**Stage:** Builder CODE (not research, not plan, not design)  
**Stance:** adversarial first, then RGY. Start from 0.  
**Date:** 2026-08-27  
**Overall: RED**  
**This file:** judgment only. **No implement.** No mail. No Phantom.

Verdict for the stage is the worst row. One RED fails CODE.

| Gate | Score |
| --- | --- |
| HTML/CSS quality | **RED** |
| Leftover digits | **RED** |
| FACTUUR | **GREEN** |
| USDC on face | **RED** |
| robots.txt | **RED** |
| Google Fonts | **GREEN** |
| Mobile | **RED** |
| **CODE stage** | **RED** |

GREEN would be: shop HTML + CSS + `betalen.js` + `robots.txt` on `https://sovereignforge.surge.sh/` that a secretary can open at 390px, with euro on the face, USDC only after kit + akkoord, `Allow: /`, no leftover street/IBAN/SKU digits, no `FACTUUR` stamp, no Google Fonts, and kit landings that match the shop (not Desk Noord cream one-files). That tree is not live.

---

## What was judged (CODE sources, not this leftover invoice repo)

CODE means: the HTML/CSS/JS a buyer actually loads. Fetched + rendered 2026-08-27 (desktop + **390×844**).

| Source | Used as |
| --- | --- |
| Live shop `https://sovereignforge.surge.sh/` (`index.html`, `/pakketten.html`, `/betalen.html`, `/contact.html`, `/privacy.html`, `/404.html`, `styles.css`, `betalen.js`, `robots.txt`, `fonts/*.woff2`, `qr/*.svg`, `previews/*.png`) | **The product under review.** |
| Live kits linked from home: `https://menu-kit-treasury.surge.sh/`, `https://lid-kit-treasury.surge.sh/`, `https://club-site-kit-treasury.surge.sh/`, `https://sponsor-kit-treasury.surge.sh/` (plus inner `menu.html`, `allergenen.html`, `lid.html`, `offerte.html`, club `styles.css` / `site.js`) | **The demos the shop sells.** Same CODE pass. |
| This checkout (`eyeskull2220/solana-invoice`: `index.html`, `solana-invoice.html`, `catalog.html`, `config.js`) | **Leftover invoice HTML. Not the live shop.** Do not score the chalkboard shop by these files. Do not redeploy them to `sovereignforge.surge.sh`. Adversarial leftover scan of *this* tree is `04-adv-code.md`, a different seat. |

Hard locks that still apply at CODE: no fake KBO · OFFERTE only · no leftover HTML as the shop face.

---

## Adversarial pass (what a hostile reader hits first)

1. Home H1 is a bestuur-voorstel. The first price string is `900 USDC`. CTA is `Betaal 900 USDC`. Meta description: `Charge in USDC`.
2. `/pakketten.html` caption: **“Elf live kits.”** Nine-column table, `min-width: 52rem` (measured **936px** inside a **333px** wrap at 390px). USDC column before euro.
3. `/betalen.html#menu` applies the hash (kit = menu, QR `qr/199.svg`) then still paints address `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3` with `panel.hidden === false`. No akkoord. No `hashchange` listener.
4. `robots.txt` on shop **and** all four kit hosts: `User-agent: *` / `Disallow: /`. 26 bytes. No `Allow:`.
5. Open the menukaart voorbeeld the home sells: title `199 USDC · Desk Noord`, footer link to `twelve.tools`, print sheet `Noorderlaan 12 · 2030 Antwerpen`.
6. Open the lid voorbeeld: sell-wrap kicker `Desk Noord · OFFERTE · 349 USDC`. Shop home claims the form has telefoon, gemeente, repetitie, startdatum. Live `lid.html` has naam, e-mail, instrument, type, nota. Copy lies.
7. Shop `styles.css` is a chalkboard system (skip link, 44px targets, self-hosted fonts). Then two leftover width rules fight: `.feat--menu img, .feat--lid img { width: min(11rem, 55%); }` **and** `.feat--sponsor img, .feat--lid img { width: min(14rem, 70%); }`. Measured at 390px: club 333×710, menu 183×385, sponsor/lid 233×493. Home scroll height **4372px**.
8. Kits are a second codebase: inline `<style>`, cream `#f3efe6` / sage `#123c2e`, `font-weight: 650`, `style=` on club pages, USDC + mint on the named-club demo.

That is leftover Builder CODE glued to a newer shop shell. Not a one-pass tree.

---

## RGY table

| # | Check | Grade | Notes |
|---|---|---|---|
| 0 | **Overall CODE** | **RED** | Shop shell is real HTML (landmarks, NL, self-hosted fonts). Face still sells USDC, eleven SKUs, `Disallow: /`. Kits are leftover one-file cream with street digits and Desk Noord. |
| 1 | HTML/CSS quality | **RED** | Shop: one shared `styles.css`, skip + `main` + `aria-current`, 44px tap, no `style=` on shop pages. Then leftover CSS (unused `.colophon .privacy`, duplicate `.pay-pick label { display: flex; }`, conflicting preview widths, Iowan/Palatino still in `--font-display`). Kits: entire layout in `<style>` (menu 143 lines, lid/sponsor sell-wrap ~20). Club demo is the only kit with a CSS module — and it still sprinkles `style="color: var(--lane)"`. `font-weight: 650` is leftover token on menu/lid/sponsor. Two skins (chalkboard shop vs cream kit) for one product. |
| 2 | Leftover digits | **RED** | Shop itself: no IBAN digits, no `BE0`, no phone. Kits: **Noorderlaan 12 · 2030 Antwerpen** on `menu.html` / `allergenen.html` / menu sell-wrap. Leftover SKU **49 USDC** “Eén klus” still a pay radio and a pakketten row (opens `solana-invoice-treasury`). Club demo prints mint `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v` on the named-club face. Menu dish prices include leftover **€ 9** (collides with the toy SKU). CSS leftover `650`. |
| 3 | FACTUUR | **GREEN** | No stamp, title, or filename `FACTUUR` on shop or the four kits. Visible stamp is `OFFERTE` / `VOORBEELD`. Privacy negation `geen FACTUUR-module` is allowed (rubric check 3). Inner kits say `geen wettelijke factuur` (lowercase). Dual-invoice is a leftover **slug** on pakketten, not a FACTUUR document face. |
| 4 | USDC on face | **RED** | Rubric check 1. Home innerText **12× USDC** at 390px. Pakketten **26×**. Betalen **17×** plus H1 “Betaal dat USDC-bedrag.” Grep of shop HTML+JS: `index.html` 11, `pakketten.html` 14, `betalen.html` 19, `betalen.js` 3, `privacy.html` 1. CTAs `Betaal 900 USDC`. Euro is `±€774` after the coin. Kits: menu title `199 USDC`, lid/sponsor kickers, club `Pay-to · 900 USDC · Solana`. Privacy USDC (settlement note) would be allowed if the face were clean. It is not. |
| 5 | robots.txt | **RED** | Rubric check 5. Live shop + all four kit hosts: `User-agent: *` then `Disallow: /` (26 bytes). **No `Allow:` line.** `sitemap.xml` 404. A secretary cannot find the shop via search. `#111` Allow on a toy catalog is not this host. |
| 6 | Google Fonts | **GREEN** | Rubric check 7. `rg fonts.googleapis\|fonts.gstatic` on shop + four kits → **0**. Shop `@font-face` → `fonts/young-serif-400.woff2` (26992 B) and `fonts/atkinson-400.woff2` (17208 B), both 200. Computed: body `"Atkinson Hyperlegible", "Segoe UI", sans-serif`; h1 `"Young Serif", "Iowan Old Style", Palatino, serif`. Kits use Iowan / system. No `fonts.google.com` hop. Residual Iowan is leftover serif, not a Google Fonts fail. |
| 7 | Mobile | **RED** | Viewport meta is present. Tap targets 44px (wordmark, nav, feat links, copy, radios ≥44px). Then CODE layout fails at 390×844: home **4372px** tall (four 844-tall PNGs, ungovered widths). `table.kits` **936px** in **333px** wrap — horizontal scroll is the page; **no `@media` except `prefers-reduced-motion`**. Lid/sponsor sell-wrap iframe `height: 1280px` on a 844 viewport. Club kit *does* have nav-toggle + 640/760/880 breakpoints — the shop CSS does not. `apple-touch-icon.png` is **32×32** (leftover favicon). Address on `#menu` sits below the first viewport at 390px only because eleven radios ate it — still in the DOM, still no gate. |

---

## Evidence (CODE, not design praise)

### Shop CSS leftover (live `styles.css`)

```233:241:styles.css
.feat img {
  display: block;
  width: min(18.5rem, 100%);
  ...
}
.feat--menu img, .feat--lid img { width: min(11rem, 55%); }
```

Later, same file:

```373:375:styles.css
.feat--club img { width: min(20rem, 100%); }
.feat--sponsor img, .feat--lid img { width: min(14rem, 70%); }
.pay-pick label { display: flex; }
```

`.pay-pick label { display: flex; }` is already set at line 286. `.colophon .privacy` has no matching markup. `--font-display` still lists Iowan/Palatino. No mobile breakpoint.

### `betalen.js` (live)

- Hash on first load works (`#menu` → kit menu, `qr/199.svg`).
- **No** `hashchange` / `popstate`. In-page hash change does not re-apply.
- **No** clipboard fallback (`document.execCommand`). Club `site.js` has one; shop copy fails silently to “Kopiëren mislukt.”
- Line 15 always writes `usdc + " USDC · ±€" + eur`. Face string is minted in JS.
- Never sets `panel.hidden = true`. Address is first paint.

### Kit leftover (live)

| Host | Leftover CODE |
| --- | --- |
| menu-kit | Inline CSS; title `Desk Noord`; footer `treasury-tools.surge.sh` + `twelve.tools`; print sheet `Noorderlaan 12 · 2030 Antwerpen`; pay block + mint on the sell page |
| lid-kit | Inline CSS; title/kicker `Desk Noord`; iframe 1280px; form fields ≠ shop bullet list |
| sponsor-kit | Inline CSS; iframe 1180px; IBAN digits stripped (good) but sell-wrap still `199 USDC` |
| club-site-kit | Real multi-page + `styles.css` + nav-toggle. Then USDC paybox + mint on the **named-club** home, `style=` kickers, favicon 404, privacy 404, robots Disallow |

### FACTUUR / KBO (held)

Shop footer: `KBO/BTW: nog niet toegekend`. Privacy: no ondernemingsnummer. No `BE0`. Stamp OFFERTE/VOORBEELD. Keep these. Do not “fix” them into a fake number or a FACTUUR module.

### This repo (out of scope for this stage)

`index.html` / `solana-invoice.html` / `catalog.html` on `main` (`2170952`) are leftover English USDC one-files. They are **not** what `sovereignforge.surge.sh` serves. Scoring them as the shop is a miss (CEO FIX-BOARD). Do not deploy them.

---

## Exact code fixes

Do all of these on the **live shop origin** (and the four kit hosts). Partial EUR-swap with USDC still in the H1 is still RED. Do not patch this leftover invoice repo instead.

### Shop — `robots.txt`

1. Replace the 26-byte deny-all with:

```
User-agent: *
Allow: /
```

2. Deploy the same file to `sovereignforge.surge.sh` **and** `menu-kit-treasury`, `lid-kit-treasury`, `club-site-kit-treasury`, `sponsor-kit-treasury`.
3. Do not add `noindex` meta while Allow is live.

### Shop — `index.html`

4. `<title>` / `<meta name="description">`: euro + OFFERTE. **Zero** `USDC` / `Solana` / `Charge blijft`.
5. Lede: euro is the price. No coin. No Kraken rate on the face.
6. `.feat-price`: `€774` (or `±€774`) only. Drop `900 USDC ·`.
7. Feat CTAs: `Open het voorbeeld` + `Vraag deze OFFERTE` (link to `/contact.html` or `/betalen.html` **after** akkoord). Never `Betaal N USDC`.
8. Lid bullets must match live `lid.html` **or** add the missing fields (telefoon, gemeente, repetitie, startdatum) to the kit. Pick one. Current copy is a lie.
9. Drop the sponsor mini-table leftover if it collides with kit prijs (`€900` hoofdsponsor vs kit `€171`). Keep it only if caption stays “voorbeeldbedragen van de club, niet de kitprijs”.
10. Nav: Home / Pakketten / Contact. Kill **Betalen** as a primary tab.

### Shop — `pakketten.html`

11. Delete five leftover SKU rows: Lead tot offerte, Peppol Client-Chase, Dual-invoice, Peppol Ready, Eén klus (`49 USDC`).
12. Keep six: club, menu, sponsor, lid, vakman, inbox-ops.
13. Kill `table.kits { min-width: 52rem }`. Stack cards. At 390px, wrap width === content width. No horizontal scroll.
14. Price cell is euro. No `USDC` column. Pay link is not `Betaal 900 USDC`.
15. Caption must not say “Elf live kits.”

### Shop — `betalen.html` + `betalen.js`

16. Six radios only (same keep-list). Delete `klus` / `dual` / `ready` / `pipeline` / `chase`.
17. `#panel` starts `hidden`. Address, `#qr`, copy-button stay out of the DOM or `hidden` until a checked akkoord (OFFERTE aanvaard · geen wettelijke factuur · KBO nog niet toegekend).
18. `#betalen.html#menu` must **not** skip that gate.
19. Add `window.addEventListener("hashchange", …)` (and `popstate`) so kit apply runs after first paint.
20. Copy button: clipboard API + `textarea`/`execCommand` fallback (copy club `site.js` fallback). Do not leak a third-party QR URL — keep local `qr/{amount}.svg`.
21. `amt.textContent` / mail subject may mention USDC **after** akkoord only. H1 must not be “Betaal dat USDC-bedrag.”
22. Drop leftover `49.svg` / junk QR files when those SKUs die.

### Shop — `styles.css`

23. One preview width token: e.g. `.feat img { width: min(16rem, 100%); }`. Delete `.feat--menu img, .feat--lid img` and the later `.feat--sponsor img, .feat--lid img` override.
24. Delete unused `.colophon .privacy` and the duplicate `.pay-pick label { display: flex; }` at EOF.
25. `--font-display: "Young Serif", serif;` — drop Iowan / Palatino.
26. Add a real mobile breakpoint **or** (better) stop using a 52rem table. `prefers-reduced-motion` alone is not a mobile layout.
27. Home at 390px: one hero + card grid. Scroll height under ~2.5 viewports, not 4372px.

### Shop — other files

28. `privacy.html`: keep the negation in running text (`geen wettelijke factuur`). Optional: drop the all-caps token `FACTUUR-module` so grep of `FACTUUR` is 0. Do not add a FACTUUR UI.
29. `contact.html`: still mail-only. Say what to mail (kit + clubnaam). No form.
30. Replace `apple-touch-icon.png` 32×32 with a 180×180 (or drop the file). Leftover favicon size.
31. Footer identity (Geel, mail, `KBO/BTW: nog niet toegekend`, privacy link, OFFERTE/VOORBEELD) stays.

### Kits (the four URLs the shop already sells)

32. **menu-kit `index.html`:** delete Desk Noord, `twelve.tools`, treasury-tools footer, the on-page “Betaal 199 USDC” card and mint line. Title is the menukaart, not the coin.
33. **menu-kit `menu.html` / `allergenen.html`:** replace `Noorderlaan 12 · 2030 Antwerpen` with a digit-free demo place (`Voorbeeldkeuken · Geel` / “straat nog in te vullen”). No leftover postal digits. Keep `hello@studio.example`. Dish **€ 9** may stay as menu voorbeeldbedragen; do not reuse 9 as a shop SKU.
34. **lid-kit `index.html`:** replace `Desk Noord` with SovereignForge / the club name. Kill 349 USDC kicker on the sell-wrap. Shrink iframe (`height: 1280px` is leftover).
35. **lid-kit `lid.html`:** add telefoon, gemeente, repetitie, startdatum **or** change shop bullets. Keep `mailto:hello@studio.example`. Keep no IBAN digits (already held).
36. **sponsor-kit `index.html`:** same sell-wrap strip (USDC kicker, 1180px iframe). Inner `offerte.html` already has `IBAN: nog niet toegekend` — keep, do not invent digits.
37. **club-site-kit:** remove the USDC paybox + mint + Solana Pay URI from the **named-club** home/footer (`#kit-pay`, `#pay-addr-foot`). Demo is ZWV De Golfbreker, not a second betalen page. Delete inline `style=`. Add `favicon.svg`. Link shop `/privacy.html` or ship a kit privacy page. Keep nav-toggle (that part is GREEN).
38. Extract kit CSS from `<style>` into a file **or** accept one-file print sheets **only** for `menu.html` / `offerte.html` / `lid.html` — not for the sell-wrap the shop “Open het voorbeeld” opens.
39. `font-weight: 650` → `600` or `700` on menu/lid/sponsor.

### Do not

40. Do not deploy this repo’s `index.html` / `solana-invoice.html` / `catalog.html` to `sovereignforge.surge.sh`.
41. Do not invent a `BE0` / KBO number to “fill the footer”.
42. Do not load `fonts.googleapis.com`.
43. Do not add a cookie banner (there are no trackers).
44. Do not treat `#111` euro-shop (`€9` / `€49` toys + `Allow: /`) as this CODE pass.

---

## Re-grep after a CODE pass (copy/paste)

```bash
# Face must be 0
curl -sS https://sovereignforge.surge.sh/ | rg -c 'USDC|Solana|FACTUUR|fonts\.googleapis|fonts\.gstatic'
curl -sS https://sovereignforge.surge.sh/pakketten.html | rg -c 'USDC|Elf live|49 USDC|Dual-invoice'
curl -sS https://sovereignforge.surge.sh/robots.txt
# expect: User-agent: * / Allow: /

# Leftover digits / leftover brand
curl -sS https://menu-kit-treasury.surge.sh/menu.html | rg 'Noorderlaan|2030|Desk Noord|twelve\.tools|650'
curl -sS https://lid-kit-treasury.surge.sh/ | rg 'Desk Noord|USDC'
curl -sS https://lid-kit-treasury.surge.sh/lid.html | rg 'telefoon|gemeente|repetitie|startdatum|IBAN|BE[0-9]'

# Fonts still local
curl -sS -o /dev/null -w '%{http_code} %{size_download}\n' \
  https://sovereignforge.surge.sh/fonts/young-serif-400.woff2 \
  https://sovereignforge.surge.sh/fonts/atkinson-400.woff2
```

Mobile proof: 390×844 home + pakketten + post-akkoord betalen. Pakketten wrap scrollWidth === clientWidth. Home scrollHeight ≲ 2.5×844. Preview imgs share one width.

---

## This run

| Did | Did not |
| --- | --- |
| Fetched shop + four kit hosts (HTML/CSS/JS/robots/fonts/QR/previews) | Edit shop HTML, kits, CSS, or Surge |
| Rendered shop at 390×844 (home 4372px / 12× USDC; pakketten table 936px in 333px wrap / 26× USDC; `#menu` hash apply) | Merge hide-the-coin, leftover invoice HTML, or a kit PR |
| Grepped FACTUUR, USDC, Google Fonts, IBAN/BE0, Desk Noord, street digits | Mail, Phantom, or treat `solana-invoice` checkout as the shop |

**CODE stage: RED.**
