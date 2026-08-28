# REVIEWER — club-stuk PR 224 (kits/club/)

**Seat:** REVIEWER (adversarial; **not** Builder; **not** the author of [PR #224](https://github.com/eyeskull2220/solana-invoice/pull/224))
**Stage:** Builder **club-stuk** only (`kits/club/` member pages)
**Date:** 2026-08-28
**Artifact:** [PR #224](https://github.com/eyeskull2220/solana-invoice/pull/224) head `1b4457e` (`cursor/club-voorbeeld-chrome-6638`) on base `3168e54` (`cursor/eur-first-shop-code-6d16`)
**This file:** judgment only. **No implement.** No shop HTML edit. No kits edit. No mail. No Surge. No merge. Still **OFFERTE**.

GREEN for this stage only if the scorecard has **no RED and no YELLOW**. One yellow fails GREEN. Start from zero. The PR body is not the tree.

Builder (`bc-47a7a375`) says seller chrome was stripped from member pages, shop files were not touched, live club host is not published. This seat (`bc-7162b336`) re-read the member HTML, grepped the kit, served `kits/club/` locally at `http://127.0.0.1:8766/`, walked Home / Over / Agenda / Lid worden / Contact at **390×844**, opened the mobile Menu. **Did not fetch, publish, or touch https://sovereignforge.surge.sh/.** **Did not mail.**

---

## The machine (said back)

SovereignForge is **one** Belgian income machine. Agents deliver. This stuk is the club VOORBEELD a Vlaamse vzw **secretaris** can forward to the **bestuur**: Dutch, whole-euro, no USDC/Phantom/crypto on the face, OFFERTE not FACTUUR, no fake KBO, no leftover US catalog, no Studio Noord leftovers, readable on a phone.

Live shop later: **https://sovereignforge.surge.sh/**. This review does not publish it. This review does not score the live host. Seller €900 / Gmail stay on the shop, not on Golfbreker member pages.

Still **OFFERTE**. `KBO/BTW: nog niet toegekend`. No FACTUUR. No invented `BE0`. No KBO number. No mail. No Surge.

---

## Verdict

**Club-stuk stage: YELLOW.**

Seller pay chrome that REVIEW-08 named is **gone** on this head: no `#kit-pay`, no `.foot-pay`, no €900 pitch, no operator Gmail, no Agents sentence, no `editor.html` on disk or in links, no `PAY_TO` in `kits/club/site.js`. Shop files are a **0-diff**. This PR did not Surge. Club HTML has **0** hits for `USDC` / `Solana` / `Phantom` / `crypto` / `FACTUUR` / `Studio Noord` / invented `BE0`. Lidgeld is euro integers. Footer stamp is `OFFERTE / VOORBEELD`. KBO line is `nog niet toegekend`.

That is not enough for GREEN. A secretaris still cannot forward these pages to the bestuur without sending **kit voice**, a **seller Privacy host**, and **inner pages that first-paint as a live Geel club**.

**RED rows: none.**
**YELLOW rows: three.** GREEN is therefore **not** available.

Author of #224 (`bc-47a7a375`) is not this seat (`bc-7162b336`). This file does not ship HTML. This file does not publish. This file does not merge.

---

## What was scored (and what was not)

| Object | Used as |
| --- | --- |
| PR #224 `kits/club/{index,over,agenda,lidworden,contact}.html` + `styles.css` at `1b4457e` | **The stuk.** Served locally. First viewport at 390×844. |
| PR #224 `kits/club/{site.js,robots.txt}` | Unchanged vs base. Still scored: no `PAY_TO`; robots `Allow: /`. |
| PR #224 file list vs base `3168e54` | Shop-untouched check. Six paths, all under `kits/club/`. |
| Live https://sovereignforge.surge.sh/ | **Out of scope.** Not fetched. Not published. Footer `href` on member pages **is** in scope (seller chrome). |
| Leftover root `index.html` / `catalog.html` / `solana-invoice.html` | **Not the shop.** Not the club face. |
| Other kits / shop origin | **Not this grade.** Confirmed not in the PR diff. |
| Mail, Surge, merge, KBO number | **Not done.** Not invented. |
| Builder PR body / commit 2 “kit voice dropped” | Exhibit only. The tree is the colour. |

---

## This-run checks (2026-08-28)

Served `kits/club/` at `http://127.0.0.1:8766/` from head `1b4457e` only. **Did not publish to Surge.** **Did not open the live shop URL.**

| Check | Result |
| --- | --- |
| Files in PR | `kits/club/agenda.html`, `contact.html`, `index.html`, `lidworden.html`, `over.html`, `styles.css` only. Shop / catalog / root invoice = **0 diff**. |
| `editor.html` | **Absent** from `kits/club/` on this head. No member-page link to it. |
| `site.js` | Nav toggle + year. **No** `PAY_TO`. **No** clipboard. |
| Forbidden strings on `kits/club/` | `USDC` / `Solana` / `Phantom` / `crypto` / `wallet` / `FACTUUR` / `Studio Noord` / `Gmail` / `kit-pay` / `foot-pay` / `PAY_TO` / `editor.html` / `€900` / `BE0` / chalkboard = **0**. |
| OFFERTE vs FACTUUR | Footer + meta: `OFFERTE / VOORBEELD`. No FACTUUR stamp. |
| KBO | `KBO/BTW: nog niet toegekend` on member footers + contact/home praktisch. No digits. |
| 390×844 home | `.voorbeeld-stamp` **VOORBEELD** in view (top 0–29). H1 + lid/agenda CTAs in view. Horizontal overflow **0** (`scrollWidth` 374 = `clientWidth` 374). Document height **2720px**. Footer OFFERTE at **2554** (below fold — expected on this long home). Menu → Sluit; five club links. |
| 390×844 lidworden | **No** header stamp. Lead **“Geen formulier-backend…”** in first paint. Footer OFFERTE top **≈893** — **below** 844. Overflow **0**. |
| 390×844 over / contact / agenda | **No** `.voorbeeld-stamp`. Footer OFFERTE in view on the short pages. Overflow **0** on over. Agenda events: Stadsvijver, Binnenzwembad, Clubhuis, 50m-bad — no `(demo)` tags. |
| Favicon | Local 404 `/favicon.ico`. Note, not colour. |
| This review wrote HTML / sent mail / ran Surge / merged | **No.** |

---

## Scorecard

Worst row fails the stage. GREEN only if every row is GREEN.

| Gate | Score |
| --- | --- |
| Dutch; euro lidgeld; no USDC / Solana / Phantom / crypto on the club HTML face | **GREEN** |
| OFFERTE not FACTUUR | **GREEN** |
| No fake KBO (`nog niet toegekend` only) | **GREEN** |
| No leftover US catalog on this PR | **GREEN** |
| No Studio Noord leftovers on `kits/club/` | **GREEN** |
| Shop files untouched | **GREEN** |
| Live club host not published (this PR / this seat) | **GREEN** |
| Mobile: viewport, Menu, no horizontal scroll at 390 | **GREEN** |
| Seller pay chrome gone (`#kit-pay` / `.foot-pay` / €900 / Gmail / editor / Agents) | **GREEN** |
| Seller chrome actually gone from member chrome (Privacy host) | **YELLOW** |
| Inner pages still read as VOORBEELD in first paint | **YELLOW** |
| Kit/operator voice gone so a secretaris will forward to the bestuur | **YELLOW** |
| **Club-stuk stage** | **YELLOW** |

**RED rows: none.**
**YELLOW rows: 3.**
GREEN is therefore **not** available.

---

## 1. Kit voice still on the face — **YELLOW**

Commit `1b4457e` claims leftover kit voice was dropped so a secretaris can forward the VOORBEELD. The member tree still talks like a kit author.

**`kits/club/lidworden.html`** (first viewport at 390×844):

- Lead: `Geen formulier-backend, geen account. De knop opent het mailprogramma van de bezoeker.`
- Card: `Voorbeeldtarief. De club zet hier haar lidgeld, eventueel met jeugd- en gezinskorting.`
- Body: `een <code>.example</code>-adres.` and `Deze pagina int geen lidgeld.`

A bestuur does not need “formulier-backend”. That sentence is operator/kit. It sits **above** the OFFERTE footer (footer top ≈893px).

**`kits/club/contact.html`:**

- Lead: `Eén mailto. Telefoon en huisadres horen hier niet thuis tot de club ze zelf inzet.`

“Mailto” + “tot de club ze zelf inzet” is fill-in-the-blank kit copy, not a club secretaris writing to her board.

**`kits/club/index.html`:**

- Praktisch list: `Taal van de site: Nederlands` — a live club does not inventory its own HTML language.
- Lidworden prose: `Het lidmaatschap loopt via een mailto-knop. De club gebruikt haar eigen adres.` plus `een <code>.example</code>-adres.`

RFC 2606 `info@golfbreker.example` as the **only** inbox is correct for a VOORBEELD (no Gmail). Explaining `.example` in `<code>` on the member face is still kit. Combined with “formulier-backend”, a cautious secretaris **will not** forward.

Pay-box / €900 / Agents **are** gone. That is real. It does not clear this row.

---

## 2. Privacy footer still points at the seller host — **YELLOW**

Builder: seller chrome stripped from member pages. Shop stays the shop.

Every member footer still has:

```html
<a href="https://sovereignforge.surge.sh/privacy.html">Privacy</a>
```

Cited on:

- `kits/club/index.html`
- `kits/club/over.html`
- `kits/club/agenda.html`
- `kits/club/lidworden.html`
- `kits/club/contact.html`

The visible word is `Privacy`. The `href` is the **live shop host**. REVIEW-08 recorded that live origin as held **USDC-first**. This seat **did not open** that URL. A secretaris who forwards Golfbreker and whose bestuur taps Privacy still leaves the club stuk for the seller host.

That is leftover seller chrome. `#kit-pay` is gone; this leak is not. Not RED: club HTML has no coin strings. Yellow because the forwardable page hands the bestuur a shop door.

---

## 3. Inner pages first-paint as a live Geel club — **YELLOW**

Builder kept **one** `.voorbeeld-stamp` on **home only**. Inner pages deleted `.demo-banner` and did not replace it.

| Page | Header VOORBEELD at 390×844 | Footer OFFERTE in first 844px |
| --- | --- | --- |
| `kits/club/index.html` | **Yes** (tape 0–29) | No (footer ~2554) |
| `kits/club/over.html` | **No** | Yes (short page) |
| `kits/club/contact.html` | **No** | Yes (short page) |
| `kits/club/agenda.html` | **No** | Depends on scroll; no header tape |
| `kits/club/lidworden.html` | **No** | **No** (footer ~893) |

Home H1 world: `ZWV De Golfbreker is een zwemclub in Geel` — stated as fact, not as mal. Over H1: `Een kleine zwemclub in Geel.` Titles dropped `(demo)`. Event rows dropped `(demo)` / `demo-locatie` as intended.

Honesty left: home tape + footer `OFFERTE / VOORBEELD` + `KBO/BTW: nog niet toegekend`. That keeps this **off RED**.

It does not keep it off YELLOW:

- `lidworden.html` first paint is a live lidgeld blad with kit jargon and **no** OFFERTE in view.
- A Geel bestuur already has **ZGEEL** (Zwemclub Geel vzw). Googling **De Golfbreker** hits **G.S.Z.V. De Golfbreker** (Groningen), not a Geel vzw. Inner pages no longer say the club is verzonnen. Forwarding this as “onze nieuwe site” is a confusion risk.

Places kept (Stadsvijver, Binnenzwembad, Clubhuis, 50m-bad) are fine once the page is clearly a VOORBEELD. Inner first paint is not clearly a VOORBEELD.

---

## 4. What Builder got right (not enough for GREEN)

These would have been RED if still present. They are **not** present on `1b4457e`:

| Claim | Tree |
| --- | --- |
| No `#kit-pay` / `.foot-pay` / €900 kit pitch | Gone from member HTML |
| No operator Gmail | `info@golfbreker.example` only |
| No Agents / README / editor links | `editor.html` not in `kits/club/`; CSS editor extras dropped in `kits/club/styles.css` |
| No `PAY_TO` / Kopieer adres | `kits/club/site.js` is nav + year |
| OFFERTE not FACTUUR | Footer/meta `OFFERTE / VOORBEELD` |
| No fake KBO | `nog niet toegekend` only |
| Euro on the face | Recreant **€ 85**, jeugd **€ 65**, gezin **€ 150** |
| Dutch `lang="nl"` | All five member pages |
| No Studio Noord / US catalog on this PR | Grep 0; PR paths club-only |
| Shop untouched | Diff vs `3168e54` is six `kits/club/` files |
| Not published | PR body; this seat did not Surge |
| Mobile | `width=device-width`; `.nav-toggle`; overflow **0** at 390; agenda table `overflow-x:auto` |

`kits/club/styles.css` still opens with `Club-site kit — rebrand here.` That is a file comment, not the face. **Note**, not yellow.

---

## Notes (not colour)

- Favicon 404 on local serve. Not a bestuur-forward fail.
- `robots.txt` remains `Allow: /` and pages send `index,follow`. Fine while unpublished. Do not ship inner pages that read as a live Geel club under `Allow: /` without the stamp problem in §3 being closed.
- over.html branding line (`het beton dat de branding houdt terwijl de branding zelf mag woelen`) is agency copy. Not Studio Noord. Not yellow alone.
- Privacy `href` scored in §2. This seat did **not** GET the live shop. Do not treat live Surge as this tree.
- Home `.voorbeeld-stamp` is the right kind of tape. Inner pages need the same honesty in the first 844px, in club Dutch, without “formulier-backend”.

---

## What YELLOW does **not** unlock

Builder does **not** ship `kits/club/` from this file. No preview. No cutover. No mail. Still OFFERTE. Still `KBO/BTW: nog niet toegekend`. **Do not surge `main`.** **Do not touch https://sovereignforge.surge.sh/.**

Holes to close before a later reviewer can be GREEN (this seat does not implement):

1. Drop kit voice from `lidworden.html` / `contact.html` / `index.html` (formulier-backend, mailto-knop, “de club zet hier”, “tot de club ze zelf inzet”, “Taal van de site”).
2. Stop sending bestuur to `https://sovereignforge.surge.sh/privacy.html` from member footers.
3. Make inner first paint read as VOORBEELD without restoring seller chrome (lidworden especially).

---

## This run

| Did | Did not |
| --- | --- |
| Scored PR #224 club tree from zero on head `1b4457e`, adversarial | Rubber-stamp the PR body or commit 2 |
| Served `kits/club/` locally; measured 390×844; opened Home, Menu, Over, Agenda, Lid worden, Contact | Publish to Surge; fetch live chalkboard; mail anyone |
| Named pay-box gone **and** three remaining yellows | Edit shop HTML; edit kits; merge #224 |
| Kept leftover root invoice HTML as **not the shop** | Invent a KBO/BTW number; stamp FACTUUR |

**Club-stuk after this file: YELLOW.** Next seat is another reviewer after Builder closes the three yellows, not publish.

End. No shop HTML. No mail. No Surge. No merge. Still OFFERTE.
