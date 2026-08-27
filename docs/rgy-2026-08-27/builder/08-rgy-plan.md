# REVIEWER — Builder PLAN stage RGY

**Seat:** REVIEWER  
**Stage:** Builder PLAN (not research, not design, not code)  
**Date:** 2026-08-27  
**This file:** judgment only. **No implement.** Do not merge shop HTML, kits, or CSS from this PR.

Verdict for the stage is the worst row. One RED fails PLAN.

| Gate | Score |
| --- | --- |
| One-pass complete shop vs punch list | **RED** |
| EUR-first | **RED** |
| Six kits only | **RED** |
| robots Allow | **RED** |
| No junk SKUs | **RED** |
| **PLAN stage** | **RED** |

GREEN would be: one written shop plan that, in a single CODE pass, ships a closed Belgian shop (home + pakketten + betalen + privacy + contact + `robots.txt` Allow) with **exactly six** EUR-priced kits, USDC off the face, and an explicit drop-list of leftover SKUs. That page does not exist. What exists is a punch list.

---

## What was judged (PLAN sources, not a CODE audit)

PLAN means: the written intent that would tell CODE what to ship. Sources opened 2026-08-27:

| Source | What it plans |
| --- | --- |
| `docs/ideas-builder-ultra.md` (#81) | Five week-scale **USDC** done-for-you offers. Explicitly not leftover HTML. Not a shop. Not six kits. |
| `docs/ultra-seats/CEO.md` (#113) | Dispatch locks (EUR-first, OFFERTE, no fake KBO). Sell lane: **one** offer this week. Not a six-kit shop bill of materials. |
| Live `https://sovereignforge.surge.sh/` | De facto catalog: **11 kits**, USDC on the home face, `Disallow: /`. |
| Live `https://treasury-tools.surge.sh/` | Same **11 kits**, euro chips on the face, still `Disallow: /`, no privacy page. |
| `cursor/euro-shop-face-00e2` (#111) | Hide-the-coin punch: `Allow: /`, euro on home/catalog/pakketten/betalen — then sells **€9 / €49 toys**, not the six Belgian kits. No `privacy.html`. |
| Kit / leftover PRs | Club-site ×2, pipeline, Peppol ready, dual-invoice, review-retainer, km-log, FAQ, UTM, waitlist, paywall, intake-form, … |
| `docs/ultra-2026-08-27/REVIEW-RUBRIC.md` (#112) | REVIEWER instrument. Not a Builder PLAN. |

`main` still has the USDC treasury catalog (`catalog.html` chips `9 USDC` / `49 USDC`). There is **no** `docs/…/BUILDER-PLAN.md` that names a one-pass shop.

---

## Scores

### 1. One-pass complete shop vs punch list — **RED**

**Notes.** A complete shop, one pass, is a closed set of surfaces shipped together:

- `index.html` (shop home)
- `pakketten.html`
- `betalen.html` (charge after kit choice)
- `privacy.html` + footer link
- `contact.html`
- `robots.txt` → `Allow: /`
- six kit demos, each openable before pay

Builder PLAN is the opposite: parallel leftovers.

- Ideas page plans **services** (club go-live, inbox desk, Peppol, pipeline, retainer). It does not list shop files, robots, or a kit cap.
- Live SovereignForge already has home / pakketten / betalen / privacy / contact — and then an **eleven-row** table plus USDC on the face plus `Disallow: /`. That is a live punch list, not a planned close.
- #111 plans a second shop face that **drops** the Belgian kits and puts the 9/49 toys back on home.
- CODE/FIX seats already spawned as punches (`FIX Builder hide-coin + robots`, named-club demo, seizoenskaart) because PLAN never froze the shop.

**Fix-if-not-green.** Write **one** Builder PLAN page (then stop). Title the shop surfaces, the six kit slugs, the drop-list, EUR-on-face / USDC-on-betalen-only, and `User-agent: *` / `Allow: /`. Forbid merging #111, #81, or any kit PR as a substitute for that page. CODE gets that page or nothing.

---

### 2. EUR-first — **RED**

**Notes.** Face price is euro (`€…` / `Prijs €…`) in `<title>`, `<h1>`, lede, and kit chips. USDC may exist on `/betalen.html` **after** a kit is chosen. Ideas-builder and CEO already know the operator is in Geel; neither turned that into a shop PLAN.

Evidence:

| Surface | Face currency |
| --- | --- |
| ideas-builder #81 | **USDC** — 1,500 / 1,800 / 2,500 / 3,500 / 2,000 USDC. Euro appears only as a *comp*, not the offer price. |
| Live `sovereignforge.surge.sh` home | **USDC** — lede “Charge blijft USDC op Solana. Euro is omrekening, geen checkout.” Cards: `900 USDC · ±€774`. |
| Live `sovereignforge.surge.sh/pakketten.html` | **USDC** column first; euro “indicatief”. Copy: “Elf live kits.” |
| Live `sovereignforge.surge.sh/betalen.html` | USDC allowed **here**, but the page still leads “Betaal dat USDC-bedrag” and lists all eleven kits as USDC. |
| Live `treasury-tools.surge.sh` | Euro chips (`€900` … `€49`), no `USDC` string in the HTML **this fetch**. Still eleven SKUs. Not in `main`. |
| #111 euro-shop home | Euro (`€9` / `€49`) — wrong catalog (see junk). `kit-pay.html` still titles `Solana Invoice — 9 USDC`. |
| `main` `catalog.html` | `9 USDC` / `49 USDC`; lead “Billed in USDC on Solana.” |

Partial euro on one Surge host does not make PLAN green. The written Builder plan (#81) and the named shop host still teach USDC as the face price.

**Fix-if-not-green.** PLAN must say: every shop/catalog chip is `€N` with no USDC in title, h1, lede, or card. Reprice #81 offers to euro **or** keep them off the shop table (they are week-scale services). Do not ship #111’s €9/€49 face as the Belgian shop. Do not print the treasury address on home/pakketten.

---

### 3. Six kits only — **RED**

**Notes.** Live pakketten copy is explicit: **“Elf live kits.”** Both public catalogs list the same eleven:

| # | Live SKU | Keep? |
| --- | --- | --- |
| 1 | Club- of vzw-site (€900 / 900 USDC) | keep |
| 2 | Menukaart + allergenen (€199 / 199 USDC) | keep |
| 3 | Sponsorblad vzw (€199 / 199 USDC) | keep |
| 4 | Lid-inschrijving (€349 / 349 USDC) | keep |
| 5 | Vakman one-pager (€249 / 249 USDC) | keep |
| 6 | Inbox-ops (€299 / 299 USDC) | keep |
| 7 | Lead tot offerte / pipeline | **drop from shop** (week-scale service, not a sixth HTML kit) |
| 8 | Peppol Client-Chase | **drop from shop** |
| 9 | Dual-invoice | **junk** |
| 10 | Peppol Ready | **junk** (orientation, not a deliverable) |
| 11 | Eén klus (€49 / 49 USDC) | **junk** (toy) |

ideas-builder plans **five services**, not six kits. #111 plans **three** packages (offertebestand €9, studio-tool €49, één opdracht €49). Home on sovereignforge features four kits; pakketten then dumps the rest. No PLAN document says “six” and names them.

**Fix-if-not-green.** Freeze this closed six (EUR, OFFERTE, live demo already exists):

1. Club- of vzw-site  
2. Menukaart + allergenen  
3. Sponsorblad vzw  
4. Lid-inschrijving  
5. Vakman one-pager  
6. Inbox-ops  

Everything else is off `pakketten.html` and off home. Pipeline / Peppol / retainer stay on the **ideas-builder service** page if CEO dispatches them — they are not shop SKUs. Do not add seizoenskaart or named-club VOORBEELD as SKU #7; a demo is a demo, not a seventh chip.

---

### 4. robots Allow — **RED**

**Notes.** Public shop must be indexable: `User-agent: *` then `Allow: /`. `Disallow: /` is a hard fail (REVIEW-RUBRIC check 5). Builder PLAN never states this. Live contradicts it.

| Host | `robots.txt` (2026-08-27) |
| --- | --- |
| `https://sovereignforge.surge.sh/robots.txt` | `User-agent: *` / `Disallow: /` |
| `https://treasury-tools.surge.sh/robots.txt` | same `Disallow: /` |
| `https://club-site-kit-treasury.surge.sh/robots.txt` | same |
| `https://menu-kit-treasury.surge.sh/robots.txt` | same |
| #111 `robots.txt` | `Allow: /` — punch on a toy catalog, not live |

Missing `robots.txt` on `main` is not Allow. A later FIX seat for “hide-coin + robots” is proof PLAN omitted it.

**Fix-if-not-green.** PLAN the file into the one-pass shop: `robots.txt` with `User-agent: *` and `Allow: /` on **sovereignforge** and **treasury-tools** and on each of the six kit hosts. Do not treat #111’s Allow as done until that catalog is the six-kit shop. Do not ship meta `index,follow` while robots still Disallow (live treasury-tools already lied that way once).

---

### 5. No junk SKUs — **RED**

**Notes.** Junk = leftover 9/49 HTML toys, orientation pages, dual-chain leftovers, and any SKU that exists because a PR needed to “ship something.”

On the live eleven-row table: Dual-invoice, Peppol Ready, Eén klus.

Still live as English tools (not the Belgian face, still SKUs): CSV Cleaner, Form to Email, RSS to Webhook, Solana Invoice 9 USDC.

#111 **re-centres** those toys as the shop (`Offertebestand €9`, `CSV-opschoner €49`, `Formulier naar e-mail €49`, `RSS naar webhook €49`). ideas-builder already forbade that (“Another 9 USDC one-file HTML toy”). CEO miss #2 / #3 is the same list.

Open leftover SKU PRs (not a shop plan): km-log, freelance-contract, retainer-invoice, dagtarief-offerte, FAQ, UTM, waitlist, paywall stub, intake-form, link-in-bio, review-retainer 199, Peppol ready 249, dual-invoice 490.

**Fix-if-not-green.** PLAN an explicit **do-not-sell** list. Do not merge those PRs onto pakketten. Do not use #111 as the public face. Keep `solana-invoice.html` as an internal editor if needed; it is not a shop chip. Dual-invoice as a **slug** may remain in git; it must not appear as a price row.

---

## What is already true (does not save PLAN)

These are not GREEN for the **stage**. They are notes so CODE does not “fix” the wrong thing:

- OFFERTE / VOORBEELD language is on the live Belgian shop. Stamp is not the PLAN failure.
- No invented `BE0` / KBO on the live shop (`KBO/BTW: nog niet toegekend`). Keep that.
- Live sovereignforge has a privacy page; treasury-tools does not. One-pass shop must include privacy on **every** public shop origin.
- Demos exist for the six keep-kits (club, menu, sponsor, lid, vakman, inbox). PLAN does not need new toy generators; it needs to **stop listing the other five**.
- CEO EUR-first lock is correct policy. It is not a Builder shop bill of materials.

---

## GREEN looks like (acceptance for a later PLAN rewrite)

A single page, merged before CODE, that a later agent can implement without inventing SKUs:

1. **One pass:** shop home, pakketten, betalen, privacy, contact, shared CSS, `robots.txt` Allow — one PR, one host of record.  
2. **EUR-first:** no `USDC` / Solana / crypto in title, h1, lede, or kit chips. Charge copy only on betalen after a kit is chosen.  
3. **Six kits only:** the keep-list in §3. No seventh chip.  
4. **robots Allow:** `Allow: /` on shop + six kit hosts, live, matching the file in git.  
5. **No junk SKUs:** drop-list in §3 and §5. No 9/49 catalog. No dual-invoice / Peppol Ready / één klus row.

Until that page exists, Builder PLAN stays **RED**. Reviewer does not implement it.

---

## This run

| Did | Did not |
| --- | --- |
| Read #81, #111, #112, #113, live shop/catalog/pakketten/betalen/privacy/robots, `main` catalog | Edit shop HTML, kits, CSS, or Surge |
| Scored five PLAN gates RGY | Merge hide-the-coin or a kit PR |
| Named the six keep-kits and the drop-list | Reprice, rewrite robots live, or ship a substitute plan |

**PLAN stage: RED.**
