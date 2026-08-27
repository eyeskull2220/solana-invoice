# REVIEWER — Builder CODE EUR-first (batch 08)

**Seat:** REVIEWER (new batch; **not** the author of [PR #213](https://github.com/eyeskull2220/solana-invoice/pull/213); **not** [PR #215](https://github.com/eyeskull2220/solana-invoice/pull/215) / REVIEW-07)
**Stage:** Builder **CODE** only
**Date:** 2026-08-27
**Artifact:** [PR #213](https://github.com/eyeskull2220/solana-invoice/pull/213) head `3168e54` (`cursor/eur-first-shop-code-6d16`)
**This file:** judgment only. **No implement.** No shop HTML edit. No kits edit. No mail. No Surge. No merge.

GREEN for this stage only if the scorecard has **no RED and no YELLOW**. One yellow fails GREEN. Start from zero. The PR body is not the tree. [PR #215](https://github.com/eyeskull2220/solana-invoice/pull/215) notes are **not** this score.

---

## The machine (said back)

SovereignForge is **one** Belgian income machine. Success is **money in operator accounts** **and** a shop a Flanders vzw secretaris will forward: one light Dutch stuk, whole-euro integer. Kits / mails / paper / cloud are parts.

Live shop later: **https://sovereignforge.surge.sh/** from git **`shop/sovereignforge/`**. Leftover root `index.html` / `catalog.html` / `solana-invoice.html` is **not** the shop. Frozen six euro. **No USDC on the face.** Operator is **not** the freelancer. Still **OFFERTE**. `KBO/BTW: nog niet toegekend`. No FACTUUR. No Peppol claim. No invented `BE0`.

Live host stays **held** until CEO unlocks cutover **after** this review is GREEN **and** a preview exists. This CODE PR did not Surge. This review does not preview. **Do not surge `main`.**

Implements DESIGN [#202](https://github.com/eyeskull2220/solana-invoice/pull/202) after DESIGN review GREEN [#204](https://github.com/eyeskull2220/solana-invoice/pull/204). PLAN GREEN [#195](https://github.com/eyeskull2220/solana-invoice/pull/195) does **not** substitute for this CODE score.

---

## Verdict

**CODE stage: GREEN.**

Head `3168e54` was re-read as a live tree, not as the author’s “two holes now gone” paragraph. Shop origin `shop/sovereignforge/` is a Dutch OFFERTE blad: euro prijsregel in the first viewport, stamp OFFERTE, Sasha · Geel, mailbox, Versie 3, robots `Allow: /`, no coin strings.

The two named holes on this pack are **gone on disk**:

1. **Club demo `kits/club/`.** No `aside.paybox`, no `Kopieer adres`, no empty `PAY_TO`, no operator Gmail on Golfbreker pages, no `.foot-pay`. The VOORBEELD banner is still there. It is not covering a pay-box. There is no pay-box.
2. **Inbox-ops wrap.** First-viewport kicker is `Sasha · SovereignForge · Geel`, same seller slot as the other wraps. Price **€299**. Studio Noord is **not** in the seller slot. Antwerpen is **not** on the wrap.

No red. No yellow. GREEN is therefore available.

Author of #213 (`bc-4744b394`) is not this seat (`bc-62c46eaf`). REVIEW-07 (`bc-82aaa419`) is not this seat. This file does not ship HTML. This file does not publish. This file does not merge.

**After this reviewer: preview is allowed only if CEO says.** Cutover later. Still OFFERTE. Still `KBO/BTW: nog niet toegekend`. **Do not surge `main`.** This seat does not preview.

---

## What was scored (and what was not)

| Object | Used as |
| --- | --- |
| PR #213 `shop/sovereignforge/` at `3168e54` | **Shop origin.** Served locally from the CODE tree. First viewport measured at 390×844 and 1280×800. |
| PR #213 `kits/{menu,sponsor,vakman,inbox-ops,lid}/index.html` + `wrap.css` + `robots.txt` | **Sell wraps.** Same-pass as DESIGN §14 / PLAN §9. |
| PR #213 `kits/club/` | **Featured club host.** Lock: VOORBEELD, **no pay-box**. |
| PR #202 DESIGN + PR #204 REVIEW-05 | Locks this CODE must paint. **Not** this grade. |
| PR #188 PLAN §8 privacy HTML | Copy lock for `privacy.html`. Compared. |
| Live https://sovereignforge.surge.sh/ | **Out of scope.** Held USDC-first world-state. This PR did not Surge. This review did not fetch it as the score. |
| Leftover `main` `index.html` / `catalog.html` / `solana-invoice.html` | **Not the shop.** Not grepped as the face. |
| Inner kit artefacts (`menu.html`, `lid.html`, sponsor/vakman `offerte.html`, inbox-ops intake/invoice/FAQ/reminder, Golfbreker pages as *product documents*) | Unchanged-is-fine. Inner stencil is a **note** unless it reads as the operator-as-freelancer. |
| Mail, Surge, merge, KBO number | **Not done.** Not invented. |
| PR #215 / REVIEW-07 | Prior RED on an **older** head (`0f4f26b`). Exhibit of the two holes. **Not** this colour. |

The author’s “The two holes (now gone)” list is **not** the colour. The tree is.

---

## Frozen six (still locked)

| Kit | Face price | Shop post | Wrap face |
| --- | ---: | --- | --- |
| Menukaart + allergenen | **€199** | €199 | €199 |
| Sponsorblad vzw | **€199** | €199 | €199 |
| Vakman one-pager | **€249** | €249 | €249 |
| Inbox-ops | **€299** | €299 | €299 |
| Lid-inschrijving | **€349** | €349 | €349 |
| Club- of vzw-site | **€900** | €900 | €900 on the **shop blad**, not on a club pay-box |

Integers. No seventh chip. Order on the shop blad: menu → sponsor → vakman → inbox-ops → lid → club. Club is **€900**, not leftover **€774**.

---

## This-run checks (2026-08-27)

Served `shop/sovereignforge/` at `http://127.0.0.1:8765/` and `kits/` at `http://127.0.0.1:8766/` from head `3168e54` only. **Did not publish to Surge.**

| Check | Result |
| --- | --- |
| PR #213 origin vs leftover root | Shop files live under `shop/sovereignforge/`. Root invoice HTML is still the `main` leftover. Not surged. |
| Author of #213 vs this seat vs REVIEW-07 | Different agents (`bc-4744b394` wrote CODE; `bc-82aaa419` wrote REVIEW-07 on `0f4f26b`; this batch is `bc-62c46eaf` on `3168e54`). |
| 390×844 home | Prijsregel `€199 · €199 · €249 · €299 · €349 · €900` in view (top 481). Both CTAs in view (bottom 683). Stamp `OFFERTE`. Kicker `Sasha · SovereignForge · Geel`. No horizontal scroll (`scrollWidth` 374 = `clientWidth` 374). Document height **2375px** (hard cap 2400; target 2200). Paper `#ffffff`. Ink `#171717`. Radius 0. |
| 1280×800 home | Same prijsregel in view (top 390). Both CTAs in view (bottom 527). Posten: name left / price right, same baseline. No dock. Type Source Serif 4 / Source Sans 3. |
| Click walk | Home → Contact (`Alleen mail.`) → Betalen (`Betaalgegevens na akkoord.`) → Privacy (`Versie 3 — 27 augustus 2026`). Inbox-ops wrap and club home served from `kits/`. |
| Forbidden on shop HTML | `USDC` / `Solana` / `Phantom` / `crypto` / `wallet` / chalkboard tokens / `€774` / `je` / `jouw` / invented `BE0` = **0**. |
| Kill list on shop | No leftover 9/49, Peppol Ready, dual-invoice, één-klus, pipeline/chase chips, hire-me, Demo freelancer, `SITE.md`, `editor.html`. |
| Privacy | Lede **Versie 3 — 27 augustus 2026**. Host/mailhost **niet geverifieerd**. Gmail buiten de EER, één zin, no SCC/adequacy *claim*. No AVG-conform badge. No cookie banner element. Matches PLAN §8. |
| Betalen | H1 **Betaalgegevens na akkoord.** No rekeningnummer, no ontvangstadres, no QR, no copy-address, no pay-to. Betalen is footer-only, not a primary tab. Frozen six euro rows only. |
| robots | Shop + six kit folders: `User-agent: *` / `Allow: /`. No `Disallow: /`. |
| Club `kits/club/` | VOORBEELD banner in first viewport. **No** `aside.paybox`. **No** `#kit-pay`. **No** `.foot-pay`. **No** `Kopieer adres`. **No** `PAY_TO` in `site.js`. **No** operator Gmail. RFC 2606 `info@golfbreker.example` only. Remaining `<aside class="card">` is Praktisch (demo), not a pay-box. |
| Inbox-ops wrap | First-viewport kicker **`Sasha · SovereignForge · Geel`** (top 101 at 390). Stamp OFFERTE. Price **€299**. Studio Noord **not** in the kicker. Antwerpen **not** on the wrap. |
| This review wrote HTML / sent mail / ran Surge / merged | **No.** |

---

## Scorecard

Worst row fails the stage. GREEN only if every row is GREEN.

| Gate | Score |
| --- | --- |
| First viewport euro only (frozen six; no USDC / Solana / Phantom / crypto / wallet / chalkboard / coin / €774) | **GREEN** |
| Stamp OFFERTE; u/uw; Sasha · SovereignForge (Geel); mailbox; Betalen = Betaalgegevens na akkoord; no pay-to on first paint | **GREEN** |
| Privacy STORE Versie 3 (27 augustus 2026); host logs UNVERIFIED; Gmail buiten de EER, one true sentence; no SCC/adequacy claim; no AVG badge; no cookie banner | **GREEN** |
| robots `Allow: /` on shop + featured kits; no leftover 9/49, Peppol Ready, dual-invoice, één-klus, pipeline/chase chips, hire-me, Demo freelancer | **GREEN** |
| Inbox-ops wrap first-viewport kicker is Sasha · SovereignForge · Geel (not Studio Noord · Antwerpen in the seller slot) | **GREEN** |
| Club demo stays VOORBEELD, **no pay-box** | **GREEN** |
| Sell wraps match shop paint (inner artefacts may stay) | **GREEN** |
| No Surge / no preview / no merge / no mail / no invented KBO in this seat | **GREEN** |
| **CODE stage** | **GREEN** |

**RED rows: none.**
**YELLOW rows: none.**
GREEN is therefore available.

---

## 1. Shop first viewport — **GREEN**

Hard-fail list on `shop/sovereignforge/{index,pakketten,betalen,contact,privacy}.html` plus `styles.css`: USDC, Solana, Phantom, crypto, wallet, chalkboard, coin, €774, wood PNG, brass CTA, freelancer-as-seller, Peppol Ready, dual-invoice, één-klus, pipeline, chase, leftover 9/49.

Measured on `index.html` at `3168e54`:

- **390×844:** kicker, OFFERTE stamp, H1, lede (`u`), prijsregel, both CTAs, all inside 844px. First post starts at 683 — may peek; no phone PNG. Horizontal scroll **0**. No `overflow-x: hidden` lie.
- **1280×800:** prijsregel + CTA row in the first 800px. Frozen six on the blad. Name left / price right.

Title `SovereignForge — voorstel voor het bestuur`. Meta is euro OFFERTE, not coin. Favicon is ink `SF` on white. Type: Source Serif 4 (H1) + Source Sans 3 (body). Paper `#ffffff`. Ink `#171717`. Radius 0. No dock.

---

## 2. OFFERTE, u/uw, operator, Betalen — **GREEN**

Shop face:

- Stamp `OFFERTE` (outline, not a filled banner). Footer `OFFERTE / VOORBEELD · geen wettelijke factuur`. Negation `geen wettelijke factuur` / `geen BTW-factuur (OFFERTE)` is allowed. No FACTUUR as a document stamp.
- Address: `u` / `uw` on prescribed copy. `je` / `jouw` = 0 on shop HTML.
- From-name: `Sasha · SovereignForge · Geel` (kicker + footer). Contact colophon `SovereignForge · Geel / België · KBO/BTW: nog niet toegekend.`
- Mailbox: `sasha.de.vree.rene@gmail.com` only.
- Betalen H1 **`Betaalgegevens na akkoord.`** Lede: no rekeningnummer, no ontvangstadres, no kaartformulier. No pay-to on home first paint. No IBAN, no QR, no copy-address on the shop. Six euro integers only.

`KBO/BTW: nog niet toegekend` only. No invented number.

---

## 3. Privacy STORE Versie 3 — **GREEN**

`privacy.html` lede: **`Versie 3 — 27 augustus 2026. Geen keurmerk. Geen banner.`**

PLAN §8 copy is on disk: Wie in Geel; OFFERTE not FACTUUR-module; gegevens/rechtsgrond; geen kaart/IBAN; trackers **niet geverifieerd** (host logs UNVERIFIED); Gmail buiten de EER **alleen om uw vraag te beantwoorden**; **Deze pagina noemt geen SCC- of adequacy-claim**; no AVG-conform badge; no banner element. USDC = 0 on this page.

The words SCC / adequacy appear only as the locked negation in PLAN §8. That is not a claim.

---

## 4. robots + kill list — **GREEN**

`robots.txt` on shop and on menu / sponsor / vakman / inbox-ops / lid / club:

```
User-agent: *
Allow: /
```

Shop pakketten is the same six posten. No 9/49 rows. No Peppol Ready. No dual-invoice. No één-klus SKU. No pipeline/chase chips. No hire-me. No Demo freelancer. `editor.html` is absent (STOP). No `SITE.md` under the shop.

Shop uitkomst line `Geen freelancer-desk.` is the PLAN/DESIGN negation of the freelancer line, not hire-me copy.

---

## 5. Inbox-ops wrap seller slot — **GREEN**

Attacked as a new read, not as a restamp of REVIEW-07.

`kits/inbox-ops/index.html` at 390×844:

| Slot | What is there |
| --- | --- |
| `.kicker` (seller slot, top 101) | **`Sasha · SovereignForge · Geel`** |
| Stamp | `OFFERTE` |
| Prijsregel | **€299** |
| Studio Noord in kicker | **No** |
| Antwerpen on the wrap | **No** |
| `Demo freelancer` / hire-me / USDC / pay-to / mint | **No** |
| Footer who | `Sasha · SovereignForge · Geel` |

Same kicker string as menu / sponsor / vakman / lid wraps.

Lede still says `Demo voor Studio Noord`. That is the inner stencil named in the wrap body, not the seller slot. It does not read as the operator-as-freelancer: the operator name in the kicker is Sasha in Geel; Studio Noord is labeled **Demo voor**. Inner artefacts (`intake.html`, `invoice.html`, `faq.html`, `reminder.html`) still use Studio Noord + RFC 2606 `hello@studio.example` + `KBO/BTW: nog niet toegekend`. FAQ: “VOORBEELD studio. Geen echte zaak.” That is a **note**, not yellow.

PLAN §12 wrap grep on `kits/inbox-ops/index.html`: `USDC` / `freelancer` / treasury address = **0**. `€299` present.

---

## 6. Club demo — **GREEN** (no pay-box)

User lock: club demo stays **VOORBEELD**, **no pay-box**. A VOORBEELD banner does not cancel a pay-box **if one is still there**. On this head, one is **not** still there.

Evidence on `3168e54`:

| Surface | What is there |
| --- | --- |
| `kits/club/index.html` | VOORBEELD banner. 3-band Golfbreker (product document). Remaining `<aside class="card">` is Praktisch (demo) with RFC 2606 mail. **No** `aside.paybox`. **No** `#kit-pay`. **No** `.foot-pay`. **No** operator Gmail. Footer is club-demo close + Privacy link. |
| `agenda.html` / `lidworden.html` / `over.html` | No `Kopieer adres`. No `#pay-addr-foot`. No operator Gmail. RFC 2606 only. |
| `contact.html` | No pay-box, no copy-address, no Gmail. One leftover sentence: `Vragen over deze kit (niet over de verzonnen club): prijs €900. Betaalgegevens na akkoord.` No mailto to the operator. Not a pay-box. **Note**, not yellow. |
| `site.js` | Nav toggle + year. **No** `PAY_TO`. **No** clipboard copy rail. |
| `styles.css` | No `.paybox` / `.foot-pay` rules. |

Operator Gmail on the public demo = **0**. Empty `PAY_TO` copy rail = **0**. `Kopieer adres` = **0**.

Club first viewport is gold/navy Golfbreker + VOORBEELD tape. That is the named maatstaf deliverable, not shop chrome. DESIGN forbids screenshotting that header onto `sovereignforge.surge.sh`. This CODE does not. Shop maatstaf is a text line plus **Open het voorbeeld**.

---

## 7. Sell wraps vs shop paint — **GREEN**

Five wraps (`kits/menu|sponsor|vakman|inbox-ops|lid/index.html` + `wrap.css`) are the shop sheet: Source Serif 4 + Source Sans 3, white, ink, 0 radius, OFFERTE stamp, euro integer, Privacy → shop, Betaalgegevens na akkoord, kicker `Sasha · SovereignForge · Geel`. Inner artefacts behind those wraps were not restyled. That match is real.

Club has **no** `wrap.css`. PLAN §9: keep Golfbreker as VOORBEELD; change the sell wrap only where a wrap exists. Club row: keep as VOORBEELD demo. Missing paper wrap is **not** a fail once the pay-box is gone. Selling the club kit happens on the shop blad (`€900` + Open het voorbeeld + Vraag deze OFFERTE).

---

## Notes (not colour)

- Home length 2375px at 390 is inside the 2400 hard cap, above the 2200 target. Post padding is 12px on small viewports (DESIGN said 20px). Length trade, not a costume.
- Shop canonicals already name `https://sovereignforge.surge.sh/`. Live origin is still held USDC-first. That is world-state until a later preview/cutover. This review does not treat live Surge as this tree.
- Shop “Open het voorbeeld” points at existing treasury hosts. Git `kits/` is the CODE. Those hosts are **not** this tree until a later preview republish. This seat did not republish.
- Wordmark `href="/"` is correct when `shop/sovereignforge/` is the document root. It is wrong if someone serves the repo root. Do not surge `main`.
- `Geen freelancer-desk.` on the shop inbox-ops post is DESIGN uitkomst copy, not a freelancer line.
- Privacy heading `Geen kaart, geen IBAN` and the SCC/adequacy negation are PLAN §8, not a pay panel and not a transfer claim.
- Inbox-ops wrap lede `Demo voor Studio Noord` sits in the first viewport. Seller slot is Geel. Inner stencil, not operator-as-freelancer.
- `kits/lid/lid.html` kitbar still mails `sasha.de.vree.rene@gmail.com` on the inner form. The sell wrap in front already uses that mailbox. Inner artefact, behind **Open het voorbeeld**, not the club-demo Gmail fail.
- Club `contact.html` kit-price sentence (`€900`) has no pay-box, no copy rail, no operator Gmail. Not the named hole.
- Inner inbox-ops invoice/FAQ may say “factuur” as a **B2C demo document**. Wrap stamp is OFFERTE. Default VAT fields are `KBO/BTW: nog niet toegekend`. No invented `BE0`.

---

## What GREEN unlocks (not this PR)

Preview Surge from `shop/sovereignforge/` **only after CEO says**. Cutover to https://sovereignforge.surge.sh/ later still. This seat does not preview. Still OFFERTE. Still `KBO/BTW: nog niet toegekend`. **Do not surge `main`.**

---

## This run

| Did | Did not |
| --- | --- |
| Scored PR #213 CODE tree from zero on head `3168e54`, adversarial | Rubber-stamp the PR body; restamp REVIEW-07 |
| Served origin locally; measured 390 and 1280; opened Home, Contact, Betalen, Privacy, inbox-ops wrap, club home + contact | Publish to Surge; preview host; fetch live chalkboard as this grade |
| Named the two prior holes **gone** on this tree; found no new red or yellow | Edit shop HTML; edit kits; merge #213 |
| Kept leftover root invoice HTML as **not the shop** | Invent a KBO/BTW number; send mail; stamp FACTUUR |

**CODE stage after this file: GREEN.** Next seat is **preview only if CEO says**, not cutover from this file.

End. No shop HTML. No mail. No Surge. No merge.
