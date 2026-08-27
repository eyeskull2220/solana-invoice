# REVIEWER — Builder RESEARCH stage RGY

Seat: **REVIEWER**. Stage: **Builder RESEARCH**. Date: **2026-08-27**.

Score **starts at 0**. A row is GREEN only when research is sourced, live-checked, internally consistent, and a designer can proceed without inventing. This file does not implement. No mail was sent. Operator (Geel) is not the freelancer.

Judged from: live hosts fetched this run, repo `main`, PR [#81](https://github.com/eyeskull2220/solana-invoice/pull/81) (`docs/ideas-builder-ultra.md`), PR [#121](https://github.com/eyeskull2220/solana-invoice/pull/121) (`docs/ultra-seats/BUILDER.md`), PR [#112](https://github.com/eyeskull2220/solana-invoice/pull/112) (shop rubric FAIL). Advocate file `docs/rgy-2026-08-27/builder/01-adv-research.md` was **not on GitHub** at judge time.

**GREEN count: 4 / 12. Stage: not closed.**

| item | RED/YELLOW/GREEN | note | fix-if-not-green |
| --- | --- | --- | --- |
| kit research | YELLOW | Five static kits are mapped in BUILDER.md with live hosts. This run confirmed: [club-site-kit-treasury](https://club-site-kit-treasury.surge.sh/) (Golfbreker, `900 USDC` + `editor.html` 200), [menu-kit-treasury](https://menu-kit-treasury.surge.sh/) (`199 USDC` + `Open wallet`), [lid-kit-treasury](https://lid-kit-treasury.surge.sh/) (index 2641 B, `349 USDC`), [sponsor-kit-treasury](https://sponsor-kit-treasury.surge.sh/) (`199 USDC`), [vakman-kit-treasury](https://vakman-kit-treasury.surge.sh/) (`249 USDC` + `Open wallet`). Live [treasury-tools.surge.sh](https://treasury-tools.surge.sh/) lists **11** packs (schema.org `numberOfItems: 11`), including inbox-ops, pipeline, Peppol Client-Chase, dual-invoice, Peppol Ready, “Eén klus”. BUILDER.md inventories five and STOP-lists the rest without a full leftover-host table. A second research tree (PR #81) still sells a different five offers at 1,500–3,500 USDC. | One inventory SoT. Put every live pack in a keep / leftover / other-seat table. Do not design from two offer lists. |
| buyer jobs | RED | PR #81 sources category jobs (16,673 Flemish sportclubs; Peppol mandate since 1 Jan 2026; VA/CRM comps) for **done-for-you** USDC work. BUILDER.md’s EUR shop SKUs (€199 menukaart, €249 vakman, €299 sponsor, €349 lid, €900 club) have **no sourced job** that a Kempen kitchen or secretaris pays those integers instead of Word/Canva. €299 sponsor vs live 199 USDC is a product flip, not a buyer quote. No named customer (correct). Operator-as-buyer is forbidden and not used. | Source one public job per SKU the shop will sell, or drop the SKU. Do not copy #81 prices onto the EUR face. |
| leftover SKUs | YELLOW | Root `main` still sells toys: `index.html` title `Solana Invoice — 9 USDC`; README lists CSV Cleaner / Form to Email / RSS to Webhook at **49 USDC**. BUILDER.md correctly keeps those out of Builder inventory. Live treasury-tools is **not** that README: it is an 11-item cream catalog. Extra live kits from #112 still on Surge: inbox-ops 299 USDC, pipeline 399, peppol-chase 399, dual-invoice 490, peppol-ready 249, solana-invoice-treasury. Research named leftovers but did not freeze the live leftover set. | One leftover table (root toys + extra Surge hosts). All of them designed out of the Builder shop face. |
| USDC-first face | GREEN | Live-checked. [sovereignforge.surge.sh](https://sovereignforge.surge.sh/): lede “Charge blijft USDC op Solana”, cards `900 USDC · ±€774`, `Betaal 900 USDC`. Club home kicker `Deze kit · 900 USDC` + Solana Pay + mint. Menu/vakman titles and “Open wallet”. Lid/sponsor indexes stamp 349/199 USDC + treasury `96BT6…`. BUILDER.md and #112 agree. EUR-first shop exists only in unpublished PR #121 `shop/sovereignforge-builder/` — not live. | — |
| generic Voorbeeldharmonie | YELLOW | Live lid + sponsor sheets: “Voorbeeldharmonie is een **verzonnen fanfare**.” Demo mail `hello@studio.example`. Menu kitchen is **Voorbeeldkeuken**, Noorderlaan 12, 2030 Antwerpen — also a stencil name. Club **ZWV De Golfbreker** is the named shape, but title/banner still say **demo** / “geen echte vzw”, not **VOORBEELD**. BUILDER.md says “Named club Voorbeeldharmonie: keep. Do not genericise.” That keep is wrong: the live copy already admits it is generic. Parallel named-club work treated Voorbeeldharmonie as the thing to replace. Keep-vs-replace is not closed. | Design-out Voorbeeldharmonie / Voorbeeldkeuken / Voorbeeldloodgieter as public demos. Public VOORBEELD must be a named club/kitchen/vakman (Golfbreker-shape). Stamp **VOORBEELD**, not “demo”. |
| robots Disallow | GREEN | Live-checked, all `User-agent: *` / `Disallow: /` (26 bytes): club, menu, lid, sponsor, vakman, [sovereignforge.surge.sh/robots.txt](https://sovereignforge.surge.sh/robots.txt), [treasury-tools.surge.sh/robots.txt](https://treasury-tools.surge.sh/robots.txt). BUILDER.md names this a defect, not policy. Unpublished shop robots in #121 is `Allow: /` — not live. | — |
| print / QR | YELLOW | Not a blanket miss. **Menu artefact:** `@media print`, line “Afdrukken of bewaren als PDF”, `allergenen-qr.png` HTTP 200, URL to allergenen. **`kaart.html` 404** (dead path). **Lid `lid.html` and sponsor `offerte.html`:** `@media print` present; **no QR**. **Club home:** no print affordance, no QR; pay box on the club page. BUILDER.md STARTABLE says “mirror print if missing” without a per-SKU matrix. Advocate “no print/QR” overstates menu and understates club. | Per-SKU matrix: print CSS on every artefact; QR only where it serves the buyer (allergenen), never on the vendor pay index. Design-out `kaart.html`. Do not invent a seizoenskaart+QR SKU in this stage — it is not in the five-kit inventory. |
| offer-set / price SoT | RED | Three prices for one seat. (1) PR #81: Club 1,500 USDC, Inbox 1,800, Peppol 2,500, Pipeline 3,500, retainer 2,000/mo. (2) BUILDER.md shop: €199 / €249 / **€299** / €349 / €900. (3) Live sovereignforge: 900 / 199 / 199 / 349 USDC with euro as “omrekening” (`1 USDC ≈ €0,86` Kraken 27 Aug 2026). Sponsor live 199 USDC vs shop €299. Inbox/Peppol/pipeline are Builder ideas in #81 and STOP in #121. Designer cannot pick a card without inventing. | Kill one tree. Shop EUR column wins only after buyer-job GREEN. Design-out #81 USDC price list from the public face. Design-out dual “USDC charge / euro omrekening” on sovereignforge. |
| operator is not the freelancer | GREEN | Locked in #81, BUILDER.md, CEO #113. Operator: yes/no on screenshots, forwards logo/KBO/IBAN/photos, collects. Does not code, host, surge, git, or apply as developer. Research does not put the operator on a marketplace. | — |
| FACTUUR / fake KBO / FAVV | GREEN | Live sheets stamp **OFFERTE** / **VOORBEELD**, `KBO/BTW: nog niet toegekend`, no invented `BE0`, no IBAN digits on lid/sponsor. Menu allergenen: EU-14 matrix, “geen juridisch advies”, **zero FAVV/FASFC**. Club: “geen ondernemingsnummer”. Research lock matches live artefacts. (Vendor pay indexes still say USDC; that is the USDC-face row, not a FACTUUR miss.) | — |
| public editor.html (stencil mill) | GREEN | Club home links `editor.html` (HTTP 200) as “open de editor”. BUILDER.md STOP: do not sell or feature the public stencil mill; rebrand privately after pay. Finding is closed. | — |
| live vs unpublished shop | YELLOW | EUR-first shop + BUILDER.md teardown live in **draft** PR #121 only. Live faces remain USDC-first + Disallow. Repo `main` `index.html` / `catalog.html` / README are still 9/49 USDC toys. Research mixed an unpublished tree with live Surge. Designer must not treat #121 as shipped. | Cite live URL and git tree separately. Do not design as if `shop/sovereignforge-builder/` is public until it is. |

## Design-out (every RED and YELLOW)

Until the matching row is GREEN, design **must not**:

1. **Two Builder products.** Do not design from PR #81 (1,500–3,500 USDC done-for-you) and from the €199–€900 static-kit shop in the same face. Pick one SoT or split seats. Inbox-ops, Peppol, pipeline, dual-invoice, Peppol Ready, retainer — **out of Builder shop** until an explicit keep.
2. **EUR SKUs without a sourced job.** Do not put €199 / €249 / €299 / €349 / €900 on a card until a public buyer job exists for that artefact. Do not use the unsourced sponsor reprice (€299 vs live 199 USDC).
3. **Leftover toys on the Builder face.** Out: Solana Invoice 9 USDC, CSV/form/RSS 49 USDC, root `index.html`/`catalog.html` restack, “Eén klus”, dual-invoice, any kit whose only job is a colour-swap.
4. **Voorbeeldharmonie / Voorbeeldkeuken / Voorbeeldloodgieter** as the thing a buyer is asked to imagine themselves in. Out: `hello@studio.example` as the club identity (RFC 2606 mail on a **named** VOORBEELD is fine). Out: “demo” stamp on Golfbreker — the word is **VOORBEELD**.
5. **A sixth stencil kit**, public `editor.html` as product, or seizoenskaart+QR as a new inventory line (not in the five-kit map; print/QR research is not closed).
6. **`kaart.html`** (404). Do not link it.
7. **Unpublished shop as live.** Do not write copy that claims sovereignforge is already EUR-first. Live sovereignforge is USDC-first with euro omrekening.
8. **Mail, fake KBO, FACTUUR title, FAVV badge, operator-as-freelancer** — already GREEN locks; still designed out.

GREEN findings that design must still honour (not in the list above because the **research** is closed): strip USDC/Solana/Phantom/wallet/treasury address from every **public** shop and kit index; pay off the artefact; `robots.txt` `Allow: /` on public hosts; keep OFFERTE/VOORBEELD and `KBO/BTW: nog niet toegekend`; do not ship public `editor.html`.

## Live cites (this run)

| URL | What was opened |
| --- | --- |
| https://sovereignforge.surge.sh/ | USDC-first lede and price cards; euro as omrekening |
| https://sovereignforge.surge.sh/robots.txt | `Disallow: /` |
| https://treasury-tools.surge.sh/ | 11-item catalog (not the repo README 4-toy list); `Disallow: /` |
| https://club-site-kit-treasury.surge.sh/ | Golfbreker **demo**, 900 USDC pay on the club home, link to `editor.html` |
| https://club-site-kit-treasury.surge.sh/editor.html | 200 |
| https://club-site-kit-treasury.surge.sh/robots.txt | `Disallow: /` |
| https://menu-kit-treasury.surge.sh/ | 199 USDC, Open wallet |
| https://menu-kit-treasury.surge.sh/menu.html | VOORBEELD sheet, print CSS, `allergenen-qr.png` |
| https://menu-kit-treasury.surge.sh/allergenen.html | EU-14, no FAVV |
| https://menu-kit-treasury.surge.sh/allergenen-qr.png | 200 |
| https://menu-kit-treasury.surge.sh/kaart.html | **404** |
| https://lid-kit-treasury.surge.sh/ | 349 USDC index + iframe to `lid.html` |
| https://lid-kit-treasury.surge.sh/lid.html | Voorbeeldharmonie verzonnen fanfare; print CSS; no QR |
| https://sponsor-kit-treasury.surge.sh/ | 199 USDC index |
| https://sponsor-kit-treasury.surge.sh/offerte.html | Voorbeeldharmonie; print CSS; no QR |
| https://vakman-kit-treasury.surge.sh/ | 249 USDC, Open wallet |

## Verdict

Builder RESEARCH is **not GREEN**. Four rows closed (USDC-first face as a documented defect, robots Disallow, operator lock, FACTUUR/KBO/FAVV lock + public editor identified). The stage still has **two RED** (buyer jobs, offer-set/price SoT) and **six YELLOW**. Design must not start from a merged inventory until those are designed out or sourced.

No implementation in this PR. No mail.
