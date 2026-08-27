# REVIEW-01 — Builder RESEARCH pack

**Seat:** REVIEWER  
**Batch:** RESEARCH only (new score; old notes are not this grade)  
**Date:** 2026-08-27  
**Artifacts scored:**
- [PR #154](https://github.com/eyeskull2220/solana-invoice/pull/154) `docs/rgy-2026-08-27/builder/01-adv-research.md`
- [PR #156](https://github.com/eyeskull2220/solana-invoice/pull/156) `docs/rgy-2026-08-27/builder/07-rgy-research.md`

**Live check this run:** [sovereignforge.surge.sh](https://sovereignforge.surge.sh/) is still **USDC-first**. That is a shop fact, not a pack GREEN.

**GREEN rule for this file:** the research pack is GREEN only when it has **no RED and no YELLOW left**. A designer can then proceed without inventing an inventory, a price, or a live cite. This batch does not reach that bar.

**Not done:** no shop HTML, no kit HTML, no CSS, no Surge publish, no mail, no invented KBO.

---

## Verdict: **not GREEN**

The pack is two unmerged trees. #154 grades the live face (12 RED / 6 YELLOW / 7 GREEN). #156 grades research completeness (4 / 12 GREEN) and **did not have #154 on GitHub at judge time**. This run re-fetched the live hosts. Several #154 / #156 cites are already stale. Worst-row fails the stage.

| item | this batch | why |
| --- | --- | --- |
| pack is one SoT | **RED** | Two files, two taxonomies, contradictory colours. #156 did not ingest #154. |
| kit research | **RED** | Four featured vs five BUILDER.md vs eleven live pakketten. Kit-index USDC cites in both files are false this run. |
| buyer jobs | **RED** | No sourced job that a secretaris or keuken pays the EUR integers. #81 sources a different product. |
| leftover SKUs | **YELLOW** | Named, not frozen. Live leftover set has drifted (pipeline euro face; inbox still 299 USDC). |
| USDC-first face | **RED** | Shop origin still USDC-first. Four kit indexes are euro this run. Pack disagrees with itself and with live. |
| generic Voorbeeldharmonie | **YELLOW** | Live lid + sponsor still admit “verzonnen fanfare.” Keep-vs-replace not closed. |
| robots Disallow | **GREEN** | Defect, not policy. Live-confirmed on shop + kits + leftover catalog. |
| print / QR | **YELLOW** | Attack surface not agreed (sold URL vs inner sheet). Menu sell still has no print CSS and no QR. |
| offer-set / price SoT | **RED** | Three written trees plus a fourth live state. Designer cannot pick a card. |
| operator is not the freelancer | **GREEN** | Lock holds. Inbox/pipeline “Demo freelancer · Antwerpen” is leftover, not the operator. |
| FACTUUR / fake KBO / FAVV | **GREEN** | Live still OFFERTE / `nog niet toegekend` / zero FAVV. |
| public `editor.html` | **GREEN** | Identified STOP. Still HTTP 200 on the club host. |
| live vs unpublished shop | **YELLOW** | [PR #121](https://github.com/eyeskull2220/solana-invoice/pull/121) EUR shop is still draft. Live origin did not move. |
| lid-field claim in #154 | **RED** | #154 A3 is false this run. Live `lid.html` now has telefoon, gemeente, repetitie, start. |

**GREEN count: 4 / 14. Stage: not closed.**

---

## RED

### R1 — Pack is two trees, not one research SoT

#154 and #156 are both RESEARCH. They do not agree.

| Claim | #154 | #156 | this run |
| --- | --- | --- | --- |
| What is graded | live face | research completeness | the pack |
| Kit count | four featured + 11-pack leftover | five (BUILDER.md) | home 4, pakketten **Elf live kits**, BUILDER.md 5, #81 five *services* |
| USDC-first | **RED** (estate split) | **GREEN** (defect documented) | shop origin USDC; four kit indexes euro |
| Print / QR | **RED** on the sold URL | **YELLOW** (inner menu has print + PNG) | both partial; not closed |
| Lid fields | **RED** (missing four fields) | no row | fields present |
| Advocate file | this file | “not on GitHub at judge time” | now PR #154 |

A designer cannot follow both. GREEN for the pack requires one inventory table, one price tree, and live cites that survive a re-fetch.

### R2 — Kit research (inventory)

Live [pakketten](https://sovereignforge.surge.sh/pakketten.html) caption this run: **“Elf live kits.”** Home features four. BUILDER.md / #156 inventory five (adds vakman, drops the other six). #81 is a different five (club 1,500 USDC, inbox 1,800, Peppol 2,500, pipeline 3,500, retainer 2,000/mo).

This run, kit **indexes** are not the USDC pay-walls #156 cited:

| Host | #156 cite | this run |
| --- | --- | --- |
| [menu-kit-treasury](https://menu-kit-treasury.surge.sh/) | `199 USDC` + `Open wallet` | title **€199**, **0× USDC**, 0× Solana, 0× wallet |
| [lid-kit-treasury](https://lid-kit-treasury.surge.sh/) | index 2641 B, `349 USDC` | 11 KB OFFERTE sheet, **€349**, 0× USDC |
| [sponsor-kit-treasury](https://sponsor-kit-treasury.surge.sh/) | `199 USDC` | Voorbeeldharmonie OFFERTE, 0× USDC |
| [vakman-kit-treasury](https://vakman-kit-treasury.surge.sh/) | `249 USDC` + `Open wallet` | title **€249**, 0× USDC |
| [club-site-kit-treasury](https://club-site-kit-treasury.surge.sh/) | Golfbreker, `900 USDC`, `editor.html` 200 | **still true**: kicker `Deze kit · 900 USDC`, `Stuur 900 USDC`, editor 200 |

#154 mapped four identities (Golfbreker / Voorbeeldharmonie / Voorbeeldkeuken / freelancer leftovers). That identity split is still live. It is not an inventory freeze. Vakman (Voorbeeldloodgieter) is a fifth identity on a live host the shop table already sells.

### R3 — Buyer jobs

#81 sources category jobs (16,673 Flemish sportclubs; Peppol mandate since 1 Jan 2026; VA/CRM comps) for **done-for-you USDC services**, not for a static-kit shop at €199 / €249 / €299 / €349 / €900.

No public quote in the pack shows a Kempen keuken or secretaris paying those integers instead of Word/Canva. Sponsor reprice (€299 in BUILDER.md vs live 199 USDC on the shop table vs euro inner sheet) is a product flip, not a buyer.

Operator-as-buyer is correctly unused. That does not source the SKU.

### R4 — USDC-first face (pack vs live)

**Shop origin this run — still USDC-first** (user constraint, independently fetched):

- Home lede: *“Charge blijft USDC op Solana. Euro is omrekening, geen checkout.”*
- Cards: `900 USDC · ±€774`, `199 USDC`, `349 USDC`.
- Pakketten: USDC column first; “Charge blijft USDC.”
- Betalen H1: *“Kies het pakket. Betaal dat USDC-bedrag.”*
- Privacy still says payment is on-chain USDC.

#156 marked this row GREEN because the defect was documented. That GREEN is unsafe:

1. #154 marks the same fact **RED**.
2. Four kit indexes have **already dropped USDC** this run. Neither file records that split.
3. A designer who trusts #156 GREEN may treat kit-index teardown as the remaining work, or treat kit euro titles as proof the shop moved. Neither is true. The origin a secretaris opens is still USDC-first.

Twin faces still live: [treasury-tools.surge.sh](https://treasury-tools.surge.sh/) “Prijs in euro” + Stripe sandbox + `numberOfItems: 11`; [solana-invoice-treasury.surge.sh](https://solana-invoice-treasury.surge.sh/) title **“Eén klus — €49”**, 0× USDC.

### R5 — Offer-set / price SoT

Four prices for one seat, this run:

1. **PR #81:** Club 1,500 / Inbox 1,800 / Peppol 2,500 / Pipeline 3,500 / retainer 2,000 per month (USDC services).
2. **BUILDER.md (#121, unpublished):** €199 / €249 / **€299 sponsor** / €349 / €900. Five kits.
3. **Live sovereignforge:** 900 / 199 / 199 / 349 / 249 / 299 / 399 / 399 / 490 / 249 / 49 **USDC**, euro as omrekening. Eleven kits. Sponsor **199** not 299.
4. **Live kit indexes (menu/lid/sponsor/vakman):** euro titles, pay-after-mail, no USDC string.

Designer cannot pick a card without inventing.

### R6 — #154 A3 lid fields (stale RED)

#154: live `lid.html` missing telefoon, gemeente, repetitie, startdatum.

This run, `lid.html` fields: `naam`, `mail`, `instrument`, `type`, `telefoon`, `gemeente`, `repetitie`, `start`, `nota`. Labels include Telefoon (optioneel), Gemeente, Voorkeur repetitie, Start (voorbeeld).

The RED is a false live cite. Leaving it in the pack sends FIX to a hole that is already filled. Research that cannot survive a re-fetch is RED for the pack.

---

## YELLOW

### Y1 — Leftover SKUs named, not frozen

Still answering this run:

| Host | Face |
| --- | --- |
| [csv-cleaner-treasury](https://csv-cleaner-treasury.surge.sh/) | English CSV Cleaner, 0 USDC |
| [form-to-email-treasury](https://form-to-email-treasury.surge.sh/) | English, **49 USDC · billed via Solana Invoice** |
| [rss-to-webhook-treasury](https://rss-to-webhook-treasury.surge.sh/) | English, **49 USDC · billed via Solana Invoice** |
| [inbox-ops-treasury](https://inbox-ops-treasury.surge.sh/) | **299 USDC**, “Demo freelancer · Antwerpen”, Desk Noord / Studio Noord |
| [pipeline-treasury](https://pipeline-treasury.surge.sh/) | title **€399**, still “Demo freelancer · Antwerpen” |
| [solana-invoice-treasury](https://solana-invoice-treasury.surge.sh/) | **€49** |
| [treasury-tools.surge.sh](https://treasury-tools.surge.sh/) | 11-item euro catalog, Stripe sandbox, HTML `index,follow` vs robots `Disallow: /` |
| this repo `main` | English 9 USDC `index.html` / `catalog.html` / README |

#154 and #156 both name leftovers. Neither freezes keep / leftover / other-seat against **this** live set (pipeline euro vs inbox USDC is new drift).

### Y2 — Voorbeeldharmonie / Voorbeeldkeuken / Voorbeeldloodgieter

Live this run:

- Lid + sponsor: “Voorbeeldharmonie is een **verzonnen fanfare**.”
- Menu: **Voorbeeldkeuken**, Noorderlaan 12, 2030 Antwerpen.
- Vakman inner: **Voorbeeldloodgieter**.
- Club: **ZWV De Golfbreker**, title/banner still **demo** / “geen echte club of vzw”, not **VOORBEELD**.

BUILDER.md: “Named club Voorbeeldharmonie: keep.” #154 treats generic as RED. #156 leaves keep-vs-replace YELLOW. Not closed.

### Y3 — Print / QR

This run:

| URL | `@media print` | QR on that URL |
| --- | --- | --- |
| [menu-kit index](https://menu-kit-treasury.surge.sh/) (Builder “Open het voorbeeld”) | no | no (copy still claims “Gedrukte QR (lokaal gegenereerd)”) |
| [menu.html](https://menu-kit-treasury.surge.sh/menu.html) | yes | yes, static `allergenen-qr.png` HTTP 200 (PNG 2765 B) |
| [kaart.html](https://menu-kit-treasury.surge.sh/kaart.html) | — | **404** |
| [lid.html](https://lid-kit-treasury.surge.sh/lid.html) | yes | no |
| [sponsor offerte](https://sponsor-kit-treasury.surge.sh/offerte.html) | yes | no |
| club home | no | no (vendor pay QR is not a kitchen QR) |

#154 RED (sold URL) and #156 YELLOW (inner sheet) are both partly true. The pack needs one per-SKU matrix. Until then, design must not invent a seizoenskaart+QR line.

### Y4 — Live vs unpublished #121

EUR-first shop tree lives in draft PR #121 (`shop/sovereignforge-builder/`, robots `Allow: /`). Live [sovereignforge.surge.sh](https://sovereignforge.surge.sh/) is still USDC-first + `Disallow: /`. Repo `main` is still 9/49 USDC toys. Do not design as if the unpublished tree is public.

---

## GREEN (research locks — not shop GREEN)

These rows are closed as **research**. They do not make the pack GREEN while RED/YELLOW remain.

### G1 — robots `Disallow: /`

Exact 26-byte body this run on Builder, club, menu, lid, sponsor, vakman, leftover catalog:

```
User-agent: *
Disallow: /
```

BUILDER.md already names this a defect. Leftover catalog and several kit pages still emit HTML `index,follow`. Intent (public catalog vs hide) is not dual-true. Design-out is `Allow: /` on public hosts — not this PR.

### G2 — Operator is not the freelancer

Locked in #81, BUILDER.md, CEO pages. Operator: yes/no on screenshots, forwards logo/KBO/IBAN/photos, collects. Does not code, host, surge, git, or apply as developer. Inbox/pipeline “Demo freelancer · Antwerpen” is leftover SKU copy, not a research claim that the operator is that person.

### G3 — FACTUUR / fake KBO / FAVV

Live sheets this run: **OFFERTE** / **VOORBEELD**, `KBO/BTW: nog niet toegekend`, no invented `BE0`, no IBAN digits on lid/sponsor. Menu allergenen: EU-14, “geen juridisch advies”, **zero FAVV/FASFC**. Club: no ondernemingsnummer. Hold.

### G4 — Public `editor.html` identified

[club-site-kit-treasury.surge.sh/editor.html](https://club-site-kit-treasury.surge.sh/editor.html) HTTP 200, title “Vul de club in. Download de site.” Club home still links it. BUILDER.md STOP: do not sell the public stencil mill. Finding is closed. The file is still live; that is CODE, not a research gap.

---

## DESIGN-OUT (every RED and YELLOW)

Until the matching row is GREEN, design **must not**:

1. **Two (or four) Builder products.** Do not design from PR #81 (1,500–3,500 USDC done-for-you) and from the €199–€900 static-kit shop and from the live 11-row USDC table and from euro kit indexes in the same face. One inventory SoT, or split seats. Inbox-ops, Peppol, pipeline, dual-invoice, Peppol Ready, retainer, één klus — **out of the Builder shop face** until an explicit keep.
2. **EUR SKUs without a sourced job.** Do not put €199 / €249 / €299 / €349 / €900 on a card until a public buyer job exists for that artefact. Do not use the unsourced sponsor reprice (€299 vs live 199 USDC).
3. **Leftover toys on the Builder face.** Out: Solana Invoice 9 USDC, CSV/form/RSS 49 USDC, root `index.html`/`catalog.html` restack, “Eén klus”, dual-invoice, colour-swap kits, English SKUs.
4. **Voorbeeldharmonie / Voorbeeldkeuken / Voorbeeldloodgieter** as the thing a bestuur is asked to imagine themselves in. Out: “demo” stamp on Golfbreker — the word is **VOORBEELD**. RFC 2606 mail on a **named** VOORBEELD is fine (`info@golfbreker.example`).
5. **A sixth stencil kit**, public `editor.html` as product, or seizoenskaart+QR as a new inventory line.
6. **`kaart.html`** (404). Do not link it.
7. **Unpublished shop as live.** Do not write copy that claims sovereignforge is already EUR-first. Live [sovereignforge.surge.sh](https://sovereignforge.surge.sh/) is USDC-first with euro omrekening.
8. **Treat kit-index euro titles as the shop moving.** Menu/lid/sponsor/vakman indexes are euro this run. The origin a secretaris forwards is still USDC. Do not strip USDC from pages that already have 0× USDC and call that the EUR-first pass.
9. **Design from #154 A3.** Lid fields telefoon / gemeente / repetitie / start are on the live form this run. Do not “fix” them as missing.
10. **Mail, fake KBO, FACTUUR title, FAVV badge, operator-as-freelancer** — already GREEN locks; still designed out.

GREEN findings design must still honour: keep OFFERTE/VOORBEELD and `KBO/BTW: nog niet toegekend`; do not ship public `editor.html`; `robots.txt` `Allow: /` on public hosts; pay off the artefact a bestuur forwards; do not print USDC/Solana/Phantom on that origin until the origin actually changes.

---

## Live cites (this run — not copied from #154 / #156)

Fetched 2026-08-27. HTTP 200 unless noted.

| URL | What was opened |
| --- | --- |
| https://sovereignforge.surge.sh/ | USDC-first lede and price cards; euro as omrekening |
| https://sovereignforge.surge.sh/pakketten.html | “Elf live kits”; USDC column first |
| https://sovereignforge.surge.sh/betalen.html | H1 “Betaal dat USDC-bedrag”; 11 USDC radios |
| https://sovereignforge.surge.sh/privacy.html | Geel, geen KBO, OFFERTE; payment described as on-chain USDC |
| https://sovereignforge.surge.sh/robots.txt | `Disallow: /` (26 bytes) |
| https://treasury-tools.surge.sh/ | 11-item euro catalog; Stripe sandbox; JSON-LD `numberOfItems: 11`; HTML `index,follow` |
| https://treasury-tools.surge.sh/robots.txt | `Disallow: /` |
| https://club-site-kit-treasury.surge.sh/ | Golfbreker **demo**, 900 USDC pay on the club home, link to `editor.html` |
| https://club-site-kit-treasury.surge.sh/editor.html | 200 |
| https://menu-kit-treasury.surge.sh/ | **€199**, 0× USDC; claims printed QR; no `@media print`, no QR image |
| https://menu-kit-treasury.surge.sh/menu.html | Voorbeeldkeuken, print CSS, `allergenen-qr.png` |
| https://menu-kit-treasury.surge.sh/allergenen.html | EU-14, no FAVV |
| https://menu-kit-treasury.surge.sh/allergenen-qr.png | 200, PNG |
| https://menu-kit-treasury.surge.sh/kaart.html | **404** |
| https://lid-kit-treasury.surge.sh/lid.html | Voorbeeldharmonie verzonnen fanfare; print CSS; fields include telefoon/gemeente/repetitie/start; 0× USDC |
| https://sponsor-kit-treasury.surge.sh/offerte.html | Voorbeeldharmonie; print CSS; no QR; 0× USDC |
| https://vakman-kit-treasury.surge.sh/ | **€249**, 0× USDC |
| https://vakman-kit-treasury.surge.sh/offerte.html | Voorbeeldloodgieter OFFERTE |
| https://solana-invoice-treasury.surge.sh/ | **€49**, 0× USDC |
| https://inbox-ops-treasury.surge.sh/ | 299 USDC, “Demo freelancer · Antwerpen” |
| https://pipeline-treasury.surge.sh/ | **€399**, “Demo freelancer · Antwerpen” |
| https://form-to-email-treasury.surge.sh/ | English, 49 USDC via Solana Invoice |
| https://csv-cleaner-treasury.surge.sh/ | English, 0 USDC |
| this repo `main` @ `2170952` | leftover 9/49 USDC `index.html` / `catalog.html` / README |

PII: operator mailbox appears on live Builder/kit colophons. It is not copied here.

---

## What would make this pack GREEN

One research page (or a rewritten #156 that ingests #154) that:

1. Freezes **one** keep / leftover / other-seat table against live hosts, re-fetched.
2. Sources **one** public job per SKU that remains, or drops the SKU.
3. Kills all but one price tree. States that live sovereignforge is USDC-first until **that origin** changes. Does not cite kit-index euro as the shop.
4. Closes Voorbeeld* keep-vs-replace.
5. Publishes the print/QR per-SKU matrix (sold URL vs inner sheet).
6. Drops stale #154 A3.
7. Leaves the four GREEN locks above in place.

Until that page exists, Builder RESEARCH stays **not GREEN**. Reviewer does not implement it.

---

## This run

| Did | Did not |
| --- | --- |
| Read #154 and #156 as artifacts | Reuse #156 colours as this grade |
| Re-fetched live shop, kits, leftover hosts, robots | Edit shop HTML, kits, CSS, or Surge |
| Scored the pack: 4 GREEN / rest RED or YELLOW | Mail; invent KBO; treat #121 as live |
| Wrote exact design-outs | Ship a substitute research tree as GREEN |

**Builder RESEARCH pack: not GREEN.**
