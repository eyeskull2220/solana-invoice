# Builder DESIGN — RGY 2026-08-27

**Seat:** Builder / DESIGN  
**Stance:** adversarial first, then RGY. Start from 0. Layout judged bad until it is not.  
**Overall: RED**  
**Mail:** not sent. **Phantom:** not opened, not spent.

## What was reviewed (and what was not)

| Object | Used as |
|---|---|
| Live shop `https://sovereignforge.surge.sh/` (home, `/pakketten.html`, `/betalen.html`, `/contact.html`, `/privacy.html`, `styles.css`, `betalen.js`) | **The product under review.** Fetched + rendered 2026-08-27 (desktop + 390×844). |
| DESIGN.md intent (EUR-first, no USDC on face, Young Serif + Atkinson, jullie/u, betaalgegevens na akkoord) | The contract. **DESIGN.md is not in this repo and 404s on the shop** (`/DESIGN.md`, `/design.md`, `/docs/DESIGN.md`). Intent is reconstructed from the brief, not from a live file. |
| This checkout (`eyeskull2220/solana-invoice`: `index.html`, `solana-invoice.html`, `catalog.html`, `README.md`) | **Leftover invoice HTML. Not the live shop.** Do not score the chalkboard shop by these files, and do not redeploy these files to `sovereignforge.surge.sh`. |

Hard locks (fail any one → cannot be GREEN): no fake KBO · OFFERTE only · no leftover HTML.

---

## RGY table

| # | Check | Grade | Notes |
|---|---|---|---|
| 0 | **Overall DESIGN** | **RED** | Face is a dark USDC catalog with stacked phone frames, not a bestuur-voorstel. Four DESIGN-intent locks fail (EUR-first, no-USDC-on-face, jullie/u, betaalgegevens na akkoord). Fonts and the two legal hard locks (KBO, OFFERTE) are the only things that hold. |
| 1 | Layout (home) | **RED** | Single 42rem column. Four “live telefoonbeeld” PNGs stacked; at 390px the club frame is 339×733 in an 844 viewport and home is **4437px** tall. Preview widths are ungoverned: club 339px / menu 182px / sponsor+lid 234px. No card grid, no paper sheet, no visual order a secretary can forward. Chalkboard (`oklch(0.20 0.025 145)` board, chalk type, brass CTA, wood picture-frame) fights the H1 (“voorstel naar het bestuur”). Nav is three text links; primary tab is **Betalen**. |
| 2 | Layout (pakketten) | **RED** | Nine-column table, `min-width: 52rem` (**936px**) inside a **333px** wrap at 390px. Horizontal scroll is the page. USDC is its own column *before* `€ indicatief`. Eleven kits as spreadsheet rows, not as OFFERTE-bladen. |
| 3 | Layout (betalen / contact) | **RED** | `/betalen.html` H1 is “Kies het pakket. Betaal dat USDC-bedrag.” Eleven radios, then **address + QR + copy** in the same viewport with **zero akkoord**. Address `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3` is visible on first paint (`panel.hidden === false`). Contact is a mailto and a void. |
| 4 | EUR-first | **RED** | Every face price is `N USDC · ±€M`. Lede: “Charge blijft USDC op Solana. Euro is omrekening.” Home CTAs: “Betaal 900 USDC”. Pakketten pay links: “Betaal 199 USDC”. Inverse of EUR-first. |
| 5 | No USDC on face | **RED** | Home body text: **12× USDC**. Pakketten: **26×**. Betalen: **17×** plus H1. Meta description: “Charge in USDC, euro is omrekening.” Nav item **Betalen** is the coin door. USDC is the face, not a back-of-house rail. |
| 6 | Young Serif + Atkinson | **GREEN** | Self-hosted `@font-face` in `styles.css`. Computed: `h1` → `"Young Serif", "Iowan Old Style", Palatino, serif`; `body` → `"Atkinson Hyperlegible", "Segoe UI", sans-serif`. `document.fonts.check` true for both. Files `fonts/young-serif-400.woff2` and `fonts/atkinson-400.woff2` 200. Residual: Iowan/Palatino still in the display stack (leftover invoice serif). |
| 7 | jullie / u | **RED** | Shop face is informal **je**: “Eén voorstel dat je doorstuurt”, “Eén OFFERTE-kit die je doorstuurt”, “die je vanavond kunt doorsturen”, pakketten “die je vanavond doorstuurt”. **jullie = 0** on home/pakketten/betalen/contact. Privacy uses **u** (legal). Mixed, and the buyer-facing pages lost. |
| 8 | Betaalgegevens na akkoord | **RED** | No “akkoord” / “voorwaarden” / “aanvaard” string on `/betalen.html`. Wallet, QR (`qr/900.svg`), and copy-button render before any gate. Home and pakketten deep-link `#club` etc. straight into that panel. DESIGN lock is not implemented. |
| 9 | Hard lock: no fake KBO | **GREEN** | Live copy: “KBO/BTW: nog niet toegekend”. Privacy: “Er is geen ondernemingsnummer (KBO) en geen vennootschap.” No `BE0…` / `0xxx.xxx.xxx` invented number. Held. |
| 10 | Hard lock: OFFERTE only | **GREEN** | Shop face is OFFERTE/VOORBEELD throughout. Prices carry “geen BTW-factuur (OFFERTE)”. Privacy: “geen FACTUUR-module”. No `INVOICE` word on shop HTML. Held **on the live shop**. |
| 11 | Hard lock: no leftover HTML | **YELLOW** on shop / **RED** in this repo | Live shop pages are NL chalkboard kits, not `solana-invoice.html`. **This repo is leftover invoice HTML** (English USDC paywall, embedded INVOICE sheet, catalog billed in USDC). Shop still sells leftover as a kit: “Eén klus” → `https://solana-invoice-treasury.surge.sh/` and Dual-invoice still says “Solana-offerte”. Reviewers who open *this* checkout are not looking at the shop. |
| 12 | DESIGN.md as source of truth | **RED** | Intent exists in the brief only. Not in this repo. 404 on the live host. Next DESIGN pass will keep reconstructing. |

---

## Exact design-outs that would make this GREEN

Do all of these. Partial EUR-swap with USDC still in the H1 is still RED.

1. **EUR-first, everywhere on the face.** Kit price reads `±€774` (or `€774`) as the only large figure. USDC amount is not adjacent on home/pakketten/contact. Conversion note, if any, is after akkoord.
2. **Zero `USDC` / `Solana` / `Charge blijft` on the face.** That includes `<title>`, meta description, H1, lede, nav, kit tiles, and CTA labels. Grep of those pages for `USDC` returns 0.
3. **Kill the Betalen nav tab.** Primary nav is Home / Pakketten / Contact. Payment is a step, not a destination.
4. **Betaalgegevens only after akkoord.** Address, QR, copy-button, and Solana amount are `hidden` until a checked control: OFFERTE aanvaard · geen wettelijke factuur · KBO nog niet toegekend. Direct `/betalen.html#club` must not skip the gate.
5. **CTA copy is OFFERTE, not pay.** Face buttons: “Vraag deze OFFERTE” / “Open het voorbeeld”. Never “Betaal N USDC”.
6. **jullie/u on every shop-face string.** Replace `je`/`jouw` on home, pakketten, betalen, contact. Board-facing copy uses **u** (secretaris) or **jullie** (bestuur). Privacy may keep `u`. Grep of face pages for `\bje\b` returns 0.
7. **Stop the screenshot dump.** Home: one hero preview + a card grid of four kits. All previews the same width. Home at 390px under ~2.5 viewports, not 4437px of wood-framed phones.
8. **Kill the 9-column 52rem table.** Pakketten = stacked cards (kit name, uitkomst, **euro**, OFFERTE, voorbeeld). No horizontal scroll at 390px. `table.kits { min-width: 52rem }` is gone.
9. **Paper, not chalkboard, as the default face.** Bestuur-voorstel = light sheet, dark ink, Young Serif display + Atkinson body. Chalkboard may exist as an alternate, not as the first paint a secretary forwards tonight.
10. **Drop leftover invoice serif from the stack.** `--font-display` is `"Young Serif", serif` — no Iowan / Palatino.
11. **Contact is an OFFERTE-blok, not a void.** Still mail-only (no form). Still Geel, KBO niet toegekend, geen Peppol AP. Say what to mail (kit + clubnaam), not just the address.
12. **This repo is not the shop.** Do not deploy `index.html` / `solana-invoice.html` / `catalog.html` to `sovereignforge.surge.sh`. Put DESIGN.md in the *shop* source. Quarantine leftover invoice files so a DESIGN reviewer cannot confuse them with the live shop. “Eén klus” must not open a USDC **INVOICE** file as if it were the shop face.
13. **Re-render proof.** After the outs: 390 and 1280 screenshots of home + pakketten + post-akkoord pay step; `USDC` grep = 0 on face pages; address/QR absent until akkoord; fonts still Young Serif + Atkinson.

Until 1–13 are visible on `https://sovereignforge.surge.sh/`, DESIGN stays **RED**.
