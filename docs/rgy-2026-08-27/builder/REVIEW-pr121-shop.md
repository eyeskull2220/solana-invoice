# REVIEWER — PR 121 shop tree (`shop/sovereignforge-builder/`)

**Seat:** REVIEWER  
**Object:** PR [#121](https://github.com/eyeskull2220/solana-invoice/pull/121) · branch `cursor/builder-seat-shop-153a` · head `6350431`  
**Date:** 2026-08-27  
**This file:** judgment only. **No implement.** Do not publish to Surge. Do not restack leftover root HTML.

**Overall: YELLOW.** This is a real EUR shop tree, not leftover `index.html` / `catalog.html` / `solana-invoice.html`. Live `https://sovereignforge.surge.sh/` is still the old chalkboard (USDC face, eleven kits, `Disallow: /`) until Builder ports. GREEN is refused while the named yellows below remain.

Worst-row does not fail the shop as leftover/chalkboard **RED**. It also does not pass. GREEN only if every yellow in the table is gone.

---

## What was scored (and what was not)

| Object | Used as |
| --- | --- |
| `shop/sovereignforge-builder/` on PR 121 (`index`, `pakketten`, `betalen`, `contact`, `privacy`, `robots.txt`, `css/shop.css`, `fonts/`, `favicon.svg`) | **The product under review.** Grepped and read 2026-08-27. |
| `docs/ultra-seats/BUILDER.md` on the same PR | Seat SSOT that **encodes** the five-kit / sponsor-€299 miss. Cited, not excused. |
| Live `https://sovereignforge.surge.sh/` | **Not this tree.** Still chalkboard. Noted so nobody treats Surge as the port. |
| Root `index.html`, `catalog.html`, `solana-invoice.html` | **Leftover invoice HTML. Not scored.** |

Required face prices (frozen six):

| Kit | Must |
| --- | ---: |
| Menukaart + allergenen | **€199** |
| Sponsorblad vzw | **€199** |
| Vakman-offerte | **€249** |
| Inbox-ops | **€299** |
| Lid-inschrijving | **€349** |
| Club-site kit | **€900** |

---

## RGY table

| # | Check | Grade | Notes |
| --- | --- | --- | --- |
| 0 | **Overall shop tree** | **YELLOW** | EUR-first pages exist. Coin is off the shop HTML. robots Allow is in git. Stamps and KBO hold. Catalog is five kits with sponsor at €299 and inbox-ops dropped. Privacy is a slogan, not STORE Versie 3. Shop contact is a demo mailbox. Fonts are Source Serif/Sans, not Young Serif + Atkinson. |
| 1 | USDC / Solana / Phantom on public shop pages | **GREEN** | `rg -i 'USDC\|Solana\|Phantom\|wallet\|crypto\|96BT6\|EPjFW' shop/sovereignforge-builder/` → **0**. No pay-QR, no mint, no Open wallet. Charge copy is euro overschrijving on `/betalen.html`. |
| 2 | robots Allow | **GREEN** (this tree) | `shop/sovereignforge-builder/robots.txt` is exactly `User-agent: *` / `Allow: /`. No `Disallow: /`. **Not live:** `sovereignforge.surge.sh/robots.txt` and the kit hosts are still deny-all until a port. |
| 3 | Prices (frozen six) | **YELLOW / RED** | Menu €199, vakman €249, lid €349, club €900 match. **Sponsor is €299** on home, pakketten table, pakketten card, and `SPONSOR-299` mededeling. Frozen price is **€199**. The €299 slot is inbox-ops, which this tree does not sell. |
| 4 | Six kits on the face, not five | **YELLOW / RED** | Home/pakketten/contact say **vijf**. Cards: menu, vakman, sponsor, lid, club. Inbox-ops is absent. `pakketten.html` even writes “Geen zesde kit die alleen van kleur wisselt.” Inbox-ops is not a colour-swap of Golfbreker; it is keep-kit #6 (`https://inbox-ops-treasury.surge.sh/`). BUILDER.md STOP list calls inbox-ops the wrong seat — that SSOT is what this tree implemented, and it is the miss. |
| 5 | Privacy vs STORE Versie 3 | **YELLOW** | H1 is “Geen cookies. Geen tracking. Geen serverformulier.” That is not Versie 3. Missing: named identity in Geel, offerte Gmail, host logs **UNVERIFIED**, Gmail buiten EER, GBA klacht. Host logs are mentioned (“IP, tijdstip, bestand”) but not labelled UNVERIFIED. No `sasha.de.vree.rene@gmail.com`, no Gegevensbeschermingsautoriteit URL. Better than live Versie 1 on coin (this page has zero USDC). Still not STORE Versie 3. |
| 6 | `hello@studio.example` on shop contact vs demo kits | **YELLOW** | Shop `contact.html` is the desk. It prints **hello@studio.example** as the only address, RFC 2606, “geen echte inbox.” That mailbox belongs on **demo kits** (Voorbeeldkeuken / Voorbeeldharmonie). Shop offerte mail is the Geel Gmail. Mixing them hides the operator and makes the shop look like another VOORBEELD. Kits may keep `hello@studio.example`. The shop may not. |
| 7 | OFFERTE / VOORBEELD, no fake KBO, no FACTUUR stamp | **GREEN** | Stamp-bar on every page: `OFFERTE · VOORBEELD · geen wettelijke factuur · KBO/BTW: nog niet toegekend`. Footer repeats KBO/IBAN pending. `rg BE0` → 0. `FACTUUR` / `INVOICE` as a stamp/title → 0. Denials (“geen wettelijke factuur”) are allowed. Betalen refuses to invent an IBAN. |
| 8 | DESIGN fonts: Young Serif + Atkinson vs Source Serif self-hosted | **YELLOW** | Method is right: `@font-face` to in-tree `fonts/*.woff2` (OFL). No Google Fonts / Typekit / jsDelivr. Faces are **Source Serif 4 + Source Sans 3**, fallback Georgia. DESIGN lock is **Young Serif + Atkinson Hyperlegible**. Self-hosting the wrong pair is not GREEN. |

---

## Evidence (this tree, not Surge)

### Coin off the face — GREEN

Shop HTML is Dutch euro. Betalen is “U betaalt in euro. Dit blad is geen factuur.” No treasury address. Root leftover pay page is untouched (correct: do not restack it into the shop).

### Catalog miss — YELLOW / RED

What the face prints:

| Face row | PR 121 | Required |
| --- | ---: | ---: |
| Menukaart | €199 | €199 |
| Vakman | €249 | €249 |
| Sponsorblad | **€299** | **€199** |
| Inbox-ops | **dropped** | **€299** |
| Lid | €349 | €349 |
| Club-site | €900 | €900 |

Sponsor at €299 is not a typo in one card. It is the SSOT: BUILDER.md inventory, home card, pakketten table, pakketten `#sponsor`, betalen `SPONSOR-299`. Live chalkboard still prices sponsor **199 USDC / €199**; this tree “corrected” the wrong direction.

Inbox-ops is keep-kit #6 on the frozen six and on live pakketten. PR 121 treats it as stencil/wrong-seat and forbids a sixth kit. That is the YELLOW/RED.

### Privacy — not Versie 3

STORE Versie 3 needs, on the shop privacy page:

1. Identity: natuurlijke persoon in **Geel**, handelsnaam SovereignForge.  
2. Offerte mail: Gmail.  
3. Host logs **UNVERIFIED**.  
4. Gmail **buiten EER**.  
5. Rechten + **GBA** klacht URL.

PR 121 privacy has none of 1–5 as named facts. It leads with a no-cookie slogan. Demo RFC 2606 addresses are listed under “Demo-inhoud” — fine for kits, not a substitute for the controller.

### Contact

`contact.html` tells the buyer to write `hello@studio.example`. Pakketten correctly uses that address on Voorbeeldkeuken. The shop desk is the other mailbox. Until contact shows the Geel Gmail (and privacy matches), this stays YELLOW.

### Fonts

```
shop/sovereignforge-builder/fonts/source-serif-4-*.woff2
shop/sovereignforge-builder/fonts/source-sans-3-*.woff2
```

`css/shop.css` `@font-face` + `font-family: "Source Serif 4"` / `"Source Sans 3"`. Zero `Young Serif` / `Atkinson`. Self-hosted OFL is not the DESIGN pair.

---

## GREEN looks like

Do all of these on `shop/sovereignforge-builder/`. Partial euro with five kits is still YELLOW.

1. **Six kits, frozen euro.** Home + pakketten + betalen + contact mededelingen: menu €199, sponsor **€199**, vakman €249, **inbox-ops €299**, lid €349, club €900. Demo link for inbox-ops: `https://inbox-ops-treasury.surge.sh/`. Drop “vijf” / “Geen zesde kit” as a catalog cap.  
2. **Privacy = STORE Versie 3.** Geel identity, Gmail, host logs UNVERIFIED, Gmail buiten EER, GBA. Kill the H1 “Geen cookies. Geen tracking” as the whole policy. Still zero USDC.  
3. **Shop contact ≠ kit demo mail.** Offerte desk = Gmail. `hello@studio.example` only on named VOORBEELD kits.  
4. **Fonts = Young Serif + Atkinson**, self-hosted. Source Serif/Sans out of the shop face. No Georgia-as-design (fallback only if needed).  
5. **Keep what already holds:** no USDC/Solana/Phantom on shop pages; `Allow: /`; OFFERTE/VOORBEELD; `KBO/BTW: nog niet toegekend`; no FACTUUR stamp; do not invent BE0/IBAN; do not publish leftover root HTML to Surge.

Until 1–4 are in this tree, the shop stays **YELLOW**. Reviewer does not implement them. Reviewer does not publish to Surge.

---

## This run

| Did | Did not |
| --- | --- |
| Read PR 121 shop HTML/CSS/robots/fonts + BUILDER.md | Edit shop HTML, kits, CSS, or BUILDER.md |
| Grepped coin, FACTUUR, BE0, Google Fonts, Gmail, GBA | Publish to Surge |
| Compared frozen six vs five-kit face | Port live chalkboard |
| Scored leftover root and live Surge as **out of scope** | Mail, invent KBO, open Phantom |

**Shop tree (PR 121): YELLOW. Not GREEN.**
