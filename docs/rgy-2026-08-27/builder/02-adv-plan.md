# Adversarial plan review — Builder

**Seat:** RGY 02 (adv-plan)  
**Date:** 2026-08-27  
**Verdict:** **RED**  
**This file does not implement.** It does not send mail. It does not invent a KBO/BTW/Peppol ID.

Builder plans are treated as a **bad layout**. This review is not a punch-list rewrite of those plans. It attacks whether a Builder agent could ship from them without failing the shop.

---

## What was scored (from zero)

| Source | What it is |
| --- | --- |
| `main` | Pay page + catalog still titled/priced in USDC (`Solana Invoice — 9 USDC`, chips `9 USDC` / `49 USDC`). No shop HTML. No `SITE.md`. |
| PR #81 `docs/ideas-builder-ultra.md` | Five week-scale offers, **all priced in USDC** (1,500 / 1,800 / 2,500 / 3,500 / 2,000 per month). |
| PR #111 `cursor/euro-shop-face-00e2` | “Hide the coin”: string-strip of this repo’s marketing pages. Home/catalog/pakketten sell **€9 / €49 toys**. `kit-pay.html` is the old 9 USDC checkout, unlinked. No `SITE.md`. |
| PR #112 REVIEW-RUBRIC | Hard-fail instrument. Shop as a whole is already **FAIL**. USDC-on-face is check 1. |
| PR #113 CEO page | Locks: EUR-first face, no 9/49 leftover HTML, no one-kit unlocks, no fake KBO, no mail. |
| Live `https://sovereignforge.surge.sh/` | The actual Belgian shop. Home still prints **900 USDC**. Pakketten: “Charge blijft USDC.” `robots.txt` is `Disallow: /`. |
| Live `https://sovereignforge.surge.sh/SITE.md` | Exists. Body: *“Deze pagina bestaat niet. De shop zit op home en pakketten.”* So SITE.md **defers to those faces**, which still say USDC. |
| Live `https://treasury-tools.surge.sh/` | Parallel catalog. Club kit at **€900** on one fetch; still not the week-scale EUR board. |

No Builder document named “one-pass shop plan” exists in git or on the live origin.

---

## Scorecard

| # | Attack | Score |
| --- | --- | --- |
| A1 | Punch-list rebuilds | **RED** |
| A2 | `SITE.md` still USDC-on-face | **RED** |
| A3 | Missing one-pass shop plan | **RED** |
| A4 | Junk SKUs on home | **RED** |
| B1 | Fake KBO / invented BTW | **GREEN** |
| B2 | Mail / Gmail fan-out in the plan | **GREEN** |
| B3 | FACTUUR stamp in the plan | **GREEN** |
| B4 | Reviewer hard-fails as a gate | **YELLOW** |
| B5 | Week-scale offer *research* (#81) | **YELLOW** |
| B6 | `robots.txt` Allow in #111 vs live Disallow | **YELLOW** |

**Overall: RED.** Do not implement from these Builder plans.

---

## A1 — Punch-list rebuilds — RED

A plan that can ship is one pass: git tree = live shop = SITE spec, and REVIEWER’s ten hard-fails go green together.

What Builder actually produced is a **sequence of partial strips**:

1. Live chalkboard shop already exists (demos, privacy, OFFERTE). Face still USDC. `robots` still `Disallow: /`.
2. `SITE.md` on that origin was stubbed (“shop zit op home en pakketten”) instead of rewritten as the EUR spec.
3. PR #111 rebuilds a **different** tree in this repo: Dutch euro labels on the **9/49 leftover catalog**, `rg` “no USDC on four files” as the done-check, old checkout renamed to `kit-pay.html`.
4. A follow-up seat (`FIX Builder hide-coin + robots`) was already spawned the same afternoon. That is the next punch-list, not a plan.

Punch-list tells: “strip these strings; Allow robots; hide the address.” It does not say which origin is canonical, which SKUs die, or what a secretary sees after one merge. #111 can merge and **live sovereignforge still says 900 USDC**. That is the definition of a rebuild that does not close the shop.

---

## A2 — `SITE.md` still USDC-on-face — RED

REVIEWER check 1 (binary): USDC as face price or in the first viewport of a shop/catalog page.

Evidence, 2026-08-27:

- Live home (`sovereignforge.surge.sh`): “**900 USDC** · ±€774 · geen BTW-factuur (OFFERTE)” and CTA “**Betaal 900 USDC**”.
- Live pakketten: first paragraph “**Charge blijft USDC.** Euro is omrekening, geen checkout.” Eleven rows with a **USDC** column and “Betaal N USDC” links. Dual-invoice row still names Solana.
- Live `SITE.md`: not a spec. It points at home and pakketten. Those pages fail check 1. **SITE.md still says USDC-on-face by reference.**
- Builder ideas (#81): every public price is USDC. CEO already required “reprice to EUR on the public face.” The ideas file was not that reprice.
- PR #111: **does not add, edit, or replace `SITE.md`.** Done-check is `rg` on four HTML files in this repo. Live SITE is untouched.

A plan that leaves SITE.md (or the pages it names) printing USDC as the face charge is not a hide-the-coin plan. Euro in a second clause (“±€774”) does not pass. Rubric: *“euro present, USDC still on the face”* is FAIL.

---

## A3 — Missing one-pass shop plan — RED

Required and absent: **one** written plan that, in a single Builder pass, makes all of this true at once:

| Must be true after the pass | In the plans today |
| --- | --- |
| Git `index.html` **is** the live shop home | #111 is a parallel euro toy catalog. Live shop is Surge-only. |
| Home first viewport: euro, Dutch, one week-scale offer, demo | Live: 900 USDC. #111: €9 / €49 toys, no demo. |
| `SITE.md` either gone or EUR shop spec (not a stub to USDC faces) | Stub on live. Missing in git. |
| Pakketten: euro required; USDC only on `/betalen` (or next to euro, never as the only face price) | Live: “Charge blijft USDC.” #111: no USDC (good) on a junk SKU table (bad). |
| Junk 9/49 HTML toys **off** home | Both live and #111 keep them (live as “één klus 49 USDC”; #111 as the whole home). |
| One offer on the board, not eleven kit unlocks | Live pakketten: 11 kits. #81: five ideas, no pick. CEO: pick one. |
| `robots.txt` must not `Disallow: /` on the public shop | Live FAIL. #111 Allow only in this repo. |
| Privacy linked from footer; no cookie theater; no fake KBO; OFFERTE | Live privacy exists (and still says payment is USDC). #111: no privacy page, thin footer. |
| Demo before pay | Live PASS. #111 FAIL (no sample, unlock still on `kit-pay.html`). |

Without that document, every new Builder PR is another strip. Reviewer stays FAIL. CEO’s “EUR shop HTML on `main`” stays WAIT.

---

## A4 — Junk SKUs on home — RED

CEO stop-list: no 9/49 leftover HTML; no isolated kit SKU as “the product.” Builder ideas: week-scale club / inbox / Peppol / pipeline / retainer. Reviewer: shop home is what a Belgian secretary sees.

**#111 home** (the supposed EUR face) sells:

- Offertebestand **€9** (the Solana Invoice toy, renamed)
- Studio-tools **€49** (CSV cleaner, form-to-email, RSS-to-webhook)

Catalog and pakketten repeat the same three leftover tools plus “één opdracht €49.” Week-scale offers from #81 do not appear. `config.js` on that branch still has `priceLabel: "9 USDC"`. `kit-pay.html` title remains `Solana Invoice — 9 USDC`.

**Live home** sells the club kit at **900 USDC** (better SKU, illegal face copy). Live pakketten then dumps eleven kits including dual-invoice 490 USDC and “één klus 49 USDC.”

Neither home matches the board. One is crypto-on-face for a real kit. The other is a euro sticker on the toys this repo already failed to sell. Putting junk SKUs on home is not a shop. It is a catalog of leftovers.

---

## B — Adjacent scores (not the named attacks)

### B1 Fake KBO — GREEN

#111 stamps **KBO/BTW: nog niet toegekend**. Live shop same. #81 does not mint an ondernemingsnummer. This review invents none.

### B2 Mail — GREEN

Builder plans scored here do not include a send. This review does not draft or send mail.

### B3 FACTUUR — GREEN

Plans and #111 use OFFERTE / VOORBEELD. Live shop uses the allowed negation (“geen FACTUUR”). Dual-invoice remains a leftover **slug** on live pakketten (YELLOW for naming, not a FACTUUR stamp fail).

### B4 Reviewer as gate — YELLOW

The rubric exists and already FAILs the shop. Builder #111’s done-check (`rg` four files) **does not run the rubric**. A plan that ignores the gate will keep shipping punch-lists that still FAIL check 1, 2, 4, 9 on the new tree (no demo, thin footer, no privacy).

### B5 Week-scale research — YELLOW

#81 is the right *class* of work (club site, inbox ops, Peppol go-live, pipeline, retainer) and correctly refuses leftover HTML toys. It is still a USDC price list, not a shop plan, and it does not pick **one** offer.

### B6 robots — YELLOW

#111 writes `Allow: /`. Live public shop is still `User-agent: *` / `Disallow: /`. Punch-list in git does not flip the origin that REVIEWER scores.

---

## NOTES

1. **Two shops.** This git repo and `sovereignforge.surge.sh` are not the same tree. Builder plans that only edit the repo cannot close live USDC-on-face. Plans that only edit Surge cannot land SITE.md in git. One-pass means one tree.

2. **Euro sticker ≠ EUR-first.** #111 proves a secretary can see €9 / €49 and still be looking at the 9/49 USDC toys. Live home proves a secretary can see €774 **and** 900 USDC in the same kicker. Rubric check 1 cares about USDC on the face, not whether a euro number exists nearby.

3. **`SITE.md` is not optional.** On the live origin it still exists and routes to USDC faces. In git it does not exist. A passing plan either deletes it on Surge **and** stops the stub, or replaces it with the EUR spec that home/pakketten must match.

4. **Done-check is the wrong test.** `rg -i 'USDC|Phantom|Solana' index.html catalog.html pakketten.html betalen.html` can go green while `kit-pay.html`, `config.js`, `solana-invoice.html`, live SITE, and junk SKUs stay. That is how punch-lists declare victory.

5. **Do not implement from RED.** Next Builder write is a one-pass shop plan (new file, not a rebuilt punch-list). Not mail. Not a KBO. Not another 9/49 HTML file. Not a twelfth kit on home.

---

## Bar for GREEN (plan only)

A later Builder **plan** (not this file, not an implementation) is GREEN only if it states, in one pass:

1. Canonical origin: this repo’s shop HTML **is** what deploys to the public shop (or an explicit, single Surge path). No parallel catalog.
2. Rewrite or remove live `SITE.md` so it no longer points at USDC-on-face pages.
3. Home: euro, Dutch, **one** week-scale offer from the CEO board, working demo, no 9/49 leftover SKUs.
4. USDC only on `/betalen` (or equivalent after kit choice). Not in `<title>`, `<h1>`, hero, or price chips on home/catalog.
5. Pakketten does not say “Charge blijft USDC.”
6. REVIEWER’s ten hard-fails listed as the merge gate, including robots not `Disallow: /`, privacy linked, footer identity, no fake KBO, OFFERTE, no cookie theater.
7. Explicit kill list: CSV / form-to-email / RSS / 9 USDC invoice **off home**. Dual-invoice Solana row off the shop face.

Until that plan exists, Builder stays **RED**.

---

End. No implementation. No mail. No KBO.
