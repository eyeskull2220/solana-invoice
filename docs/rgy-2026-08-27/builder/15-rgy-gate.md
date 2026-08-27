# Builder GATE / FIXLIST — remaining RGY before GREEN

**Seat:** Builder / GATE (15)  
**Stance:** adversarial first, then RGY. Layout is bad until the live origin is not.  
**Date:** 2026-08-27  
**Verdict:** **RED**  
**This file is the one list.** Remaining reds, yellows, and notes that must be designed out before Builder is GREEN. It does not implement. It does not send mail. It does not invent a KBO/BTW/Peppol ID. It does not rewrite leftover invoice HTML.

Fetched live HTML/`robots.txt`/`privacy.html` on 2026-08-27. Sibling RGY (02, 04, 05, 08, 09, 14) and REVIEW-RUBRIC (#112) are sources, not substitutes. If a later punch-list PR in this leftover repo goes green, **re-fetch the live origin** — that is the only scoreboard.

---

## Canonical target (read this first)

| Thing | Is | Is not |
| --- | --- | --- |
| **The shop** | [https://sovereignforge.surge.sh/](https://sovereignforge.surge.sh/) — home, `/pakketten.html`, `/betalen.html`, `/contact.html`, `/privacy.html`, `styles.css`, `robots.txt` | This git checkout |
| **This repo** (`eyeskull2220/solana-invoice` `main` @ `2170952`) | Leftover English invoice HTML: `index.html`, `catalog.html`, `solana-invoice.html`, `config.js`, README. Five files. No shop. | Shop progress. A Belgian public face. |
| **treasury-tools.surge.sh** | Parallel cream catalog. Same eleven kits, euro chips, **no privacy**, `Disallow: /` | The shop |
| **PRs against leftover `index.html` / `catalog.html`** (#111 euro-face, kit SKUs, Ultra ideas) | Residue in the leftover repo | Evidence the shop moved |

A GREEN Builder pass lands on **sovereignforge.surge.sh** (or the EUR-first successor of that **same host**). Merging leftover invoice HTML, or shipping another kit PR in this repo, cannot close this GATE.

---

## Adversarial pass (then RGY)

Attacks that would still fail a secretary tonight, after every unmerged leftover-repo PR is ignored:

1. **Wrong tree.** Agents keep scoring `main` `index.html`. The secretary opens `sovereignforge.surge.sh`. Those are different files. Punch-lists on the leftover tree leave the live face untouched.
2. **Euro nearby ≠ hide-the-coin.** Live home already prints `±€774` **and** `900 USDC` in the same kicker. Rubric check 1 FAILs that.
3. **Eleven unlocks.** Live pakketten copy is “Elf live kits.” CEO success is one forwardable page. PLAN freeze is six. Live is eleven. That is not a shop; it is a SKU dump.
4. **Crawlers are told to leave.** Live `robots.txt` is `User-agent: *` / `Disallow: /` (26 bytes) on the shop, the parallel catalog, and kit hosts.
5. **Pay is the front door.** Nav tab **Betalen**. Home CTA **Betaal 900 USDC**. `/betalen.html` paints treasury address + QR on first paint. Zero `akkoord`.
6. **SITE.md is a 404 that still names the USDC faces.** Missing path and `/SITE.md` both render “De shop zit op home en pakketten.” Those pages still sell USDC.
7. **A second catalog still exists.** `treasury-tools.surge.sh` hid the coin in visible copy this fetch and still fails cream, privacy 404, Surge-default 404, `Disallow: /`. Two public origins. One GATE.

None of those attacks are answered by #111 (`€9` / `€49` toys in this leftover repo).

---

## Scorecard — remaining only

Worst row wins. One RED fails GATE. GREEN rows are already true on the **live shop** and must not be “fixed” into leftovers.

| ID | Remaining item | Color | Design out on |
| --- | --- | --- | --- |
| R1 | Two trees: leftover repo treated as the shop | **RED** | Live origin = git shop source. Stop deploying / scoring this leftover checkout. |
| R2 | USDC-on-face (home, pakketten, meta, CTAs) | **RED** | `sovereignforge.surge.sh` `/` and `/pakketten.html` |
| R3 | `robots.txt` `Disallow: /` | **RED** | Shop + catalog + every public kit host |
| R4 | SKU dump: eleven kits, no freeze | **RED** | Live `/pakketten.html` and home chips |
| R5 | Junk SKUs still on the shop table | **RED** | Dual-invoice, Peppol Ready, Eén klus (€49 / 49 USDC), English 9/49 tools |
| R6 | Address / QR / copy before akkoord | **RED** | `/betalen.html` first paint |
| R7 | Parallel catalog `treasury-tools.surge.sh` | **RED** | That host (redirect, retire, or stop calling it a shop) |
| R8 | Kit landings still coin-faced | **RED** | Linked demo hosts (club, menu, …) |
| Y1 | SITE.md / DESIGN.md absent as spec | **YELLOW** | Live origin + shop source |
| Y2 | `je` on bestuur-facing copy | **YELLOW** | Home / pakketten / contact strings |
| Y3 | Layout: phone dump + 52rem table | **YELLOW** | Home + pakketten at 390px |
| Y4 | Privacy / 404 missing on catalog + kits | **YELLOW** | Every public origin a secretary can open from the shop |
| Y5 | In-house CI does not exist (and would grep the leftover tree) | **YELLOW** | Only after R1: CI must curl **live shop**, not leftover `index.html` |
| N1 | OFFERTE / no fake KBO / no Google Fonts / chalkboard fonts | **GREEN** | Do not regress. Do not restamp FACTUUR. Do not invent BE0. |
| N2 | Demos exist for the keep-kits | **GREEN** | Do not replace demos with paywalls. |
| N3 | Custom 404 + privacy on sovereignforge | **GREEN** | Keep. Do not “fix” by editing leftover `index.html`. |

**Overall: RED.** Do not implement from leftover-repo punch-lists. Do not declare GREEN because a four-file `rg` passed on this checkout.

---

## RED — must design out

### R1 — Leftover invoice repo is not the shop

**Evidence.** `main` is five English treasury files. Live shop is a Dutch chalkboard origin with different HTML (home 5313 B vs leftover `index.html` 50251 B). #111 / #119 / #121 rewrite **this** tree. CEO FIX-BOARD (#123): Ultra PRs here are not shop movement.

**Design out.** Name one shop source tree that **deploys to** `sovereignforge.surge.sh`. Put shop HTML there. Quarantine leftover `index.html` / `catalog.html` / `solana-invoice.html` so a Builder cannot confuse them with the shop. A PR that only edits this leftover repo **cannot** close GATE.

### R2 — USDC is still the live face

**Evidence, live `https://sovereignforge.surge.sh/` (visible text):**

- Meta: “Charge in USDC, euro is omrekening.”
- Lede: “Charge blijft USDC op Solana. Euro is omrekening, geen checkout.”
- Club card: “900 USDC · ±€774 · geen BTW-factuur (OFFERTE)” + CTA “Betaal 900 USDC”
- Visible `USDC` on home: **13**. Pakketten: **27** including column header **USDC** and “Charge blijft USDC.”
- Dual-invoice row: “Solana-offerte met hetzelfde nummer.”

Euro in a second clause does not pass. REVIEW-RUBRIC check 1 is binary.

**Design out.** On `/` and `/pakketten.html` (title, meta, h1, lede, chips, CTAs): `USDC` / `Solana` / `Phantom` / `Charge blijft` = **0**. Face price is `€N` (or `Prijs €N`). Nav is not a coin door (kill **Betalen** as a primary tab). Charge copy only after kit choice **and** akkoord, on `/betalen.html`.

### R3 — Crawlers are disallowed

**Evidence.**

```
GET https://sovereignforge.surge.sh/robots.txt
GET https://treasury-tools.surge.sh/robots.txt
GET https://club-site-kit-treasury.surge.sh/robots.txt
→ 26 bytes: User-agent: * / Disallow: /
```

Same deny-all on other kit hosts this wave. #111 `Allow: /` in leftover git is not live.

**Design out.** `User-agent: *` then `Allow: /`. No `Disallow: /`. File in the **shop** source, **deployed**. Re-`curl` the live shop. Kit hosts linked from the shop must match.

### R4 — Eleven kits, no freeze

**Evidence.** Pakketten meta: “Alle 11 OFFERTE-pakketten.” Body: “Elf live kits.” Home stacks four kits then dumps the rest on pakketten. CEO: one forwardable page, no one-kit unlock factory. PLAN (#125): freeze six. Live implements neither.

**Design out (pick one and write it on the live origin — do not keep both stories):**

- **One hero:** home is a single week-scale OFFERTE (club-site is the existing maatstaf) a secretary can forward tonight. Other keep-kits are not home chips.
- **Closed six** (if the shop remains a catalog): Club-site, Menukaart, Sponsorblad, Lid-inschrijving, Vakman, Inbox-ops.

Pipeline / Peppol / retainer stay off the shop table (services, not HTML unlocks). No seventh chip (seizoenskaart / named-club VOORBEELD is a demo, not a SKU).

### R5 — Junk SKUs on the live table

**Evidence.** Live pakketten still rows: Dual-invoice 490 USDC, Peppol Ready 249 USDC, Eén klus 49 USDC → `solana-invoice-treasury.surge.sh`. English leftover hosts still live (`csv-cleaner-treasury`, `form-to-email-treasury`, `rss-to-webhook-treasury`). #111 would put those toys **back on home** as `€9` / `€49`.

**Design out.** Those rows gone from shop home and pakketten. Eén klus / 9/49 HTML is not a Belgian shop chip. Dual-invoice may remain a git slug; it must not be a price row. Do not merge leftover-repo toy PRs onto the live table.

### R6 — Rails on first paint

**Evidence.** `/betalen.html` h1: “Kies het pakket. Betaal dat USDC-bedrag.” Body contains treasury `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3`, `qr/`, copy control. String `akkoord`: **0**. Home/pakketten deep-link into that panel. DESIGN lock “betaalgegevens na akkoord” is not implemented.

**Design out.** Address, QR, copy, and chain amount stay hidden until an explicit OFFERTE-akkoord (geen wettelijke factuur · KBO nog niet toegekend). Direct `#club` must not skip the gate. Face CTAs: “Open het voorbeeld” / “Vraag deze OFFERTE” — never “Betaal N USDC.”

### R7 — Parallel catalog is still a public shop face

**Evidence.** `https://treasury-tools.surge.sh/` this fetch: euro chips (`€900` … `€49`), visible USDC=0, cream `#f4f1ea`, Stripe “sandbox / test only” on the face, `/privacy.html` **404** (Surge default “powered by surge.sh”), `Disallow: /`. Same eleven kits. Not `main` `catalog.html`. Not sovereignforge.

**Design out.** One public shop origin. Retire or 301 `treasury-tools.surge.sh` to sovereignforge (after R2–R5 on sovereignforge). Do not keep a cream euro catalog as a second face. Stripe sandbox copy off any remaining public page.

### R8 — Linked kit hosts still print the coin

**Evidence.** Shop home’s “Open het voorbeeld” goes to kit hosts. Those hosts are what a secretary actually opens.

- `club-site-kit-treasury.surge.sh`: visible `900 USDC` (3), treasury address (3), `demo` (14), `VOORBEELD` (3), `OFFERTE` (0). Public `editor.html` is a stencil mill (STOP). `robots` Disallow. No privacy on that origin.
- `menu-kit-treasury.surge.sh`: title “199 USDC”, cream wrap, Solana pay copy on the landing.

**Design out.** A kit **landing** linked from the shop follows shop-face rules: euro / no coin / VOORBEELD stamp (not only “demo”) / no public editor mill / `Allow: /` / privacy link (shop privacy is enough if linked). Pay rails stay off the demo home. Golfbreker stays a named VOORBEELD, not a USDC storefront.

---

## YELLOW — must design out or explicitly accept

Acceptance is a written line on the live origin (or shop SITE spec), not a vibe.

### Y1 — No SITE / DESIGN spec on the shop

`/SITE.md` and `/DESIGN.md` 404 into the shop 404: “De shop zit op home en pakketten.” Those pages fail R2. Intent lives in briefs and leftover-repo markdown.

**Design out.** Either delete the stub route so it stops naming USDC faces, or publish a short EUR spec **in the shop source** that home/pakketten must match. Reconstructing DESIGN from chat is how punch-lists ship.

### Y2 — Informal `je` on bestuur copy

Home: “Eén OFFERTE-kit die je doorstuurt.” Pakketten: “die je vanavond doorstuurt.” Privacy correctly uses `u`. DESIGN asked jullie/u.

**Design out.** Buyer-facing shop strings: `u` (secretaris) or `jullie` (bestuur). Grep `\bje\b` on `/`, `/pakketten.html`, `/contact.html` = 0. Or explicitly accept informal `je` in SITE — do not leave it accidental.

### Y3 — Layout still a catalog, not a voorstel

Home: stacked phone frames, long chalkboard scroll. Pakketten: nine-column table `min-width: 52rem` inside a ~333px wrap at 390px (horizontal scroll is the page). Nav primary is Betalen.

**Design out.** Home: one hero preview + card grid of the **frozen** set (R4), same preview width, under ~2.5 viewports at 390px. Pakketten: stacked cards (name, uitkomst, **euro**, OFFERTE, voorbeeld) — no 52rem table. Paper sheet as the forwardable face is allowed; chalkboard as first paint is the current miss if the page is meant to be mailed to a bestuur.

### Y4 — Privacy / 404 only on sovereignforge

Sovereignforge: privacy 200, footer link, custom 404 (GREEN). treasury-tools and kit hosts: privacy 404 + Surge-default 404.

**Design out.** Every origin linked from the shop: privacy 200 or a footer link to shop `/privacy.html`; shop-owned 404, not “powered by surge.sh.” Do not add a cookie banner (there are no trackers).

### Y5 — CI cannot save a leftover tree

RGY 14: no `.github/workflows`. Proposed greps target leftover `index.html` / `catalog.html`. Live shop would still fail R2/R3 after a leftover CI pass.

**Design out.** After R1, in-house CI (`rg` + `curl`, no paid product) must fail PRs that (a) put leftover 9/49 digits on the **shop** face, (b) put `USDC|Solana|Phantom` on shop-face paths, (c) leave live `sovereignforge.surge.sh/robots.txt` as `Disallow: /`. YAML without a live curl is punch-list theater.

---

## NOTES — locks, not punch-list extras

1. **Do not mail.** GATE is a list. Scout/CEO own send. Footer `mailto:` is not a send.
2. **Do not invent KBO.** Live line “KBO/BTW: nog niet toegekend” stays. `BE0…` is a fail.
3. **OFFERTE / VOORBEELD only.** FACTUUR as a stamp is a fail. Denial (“geen FACTUUR”) on privacy is allowed. Do not “fix” English `INVOICE` inside leftover `solana-invoice.html` by deploying that file as the shop.
4. **USDC on privacy as settlement honesty** is allowed **after** R2. It does not excuse USDC on home chips.
5. **USDC on `/betalen.html` after akkoord** is allowed. It does not excuse h1 “Betaal dat USDC-bedrag” with address visible.
6. **Demos already exist** for club / menu / sponsor / lid / vakman / inbox. Do not build new toy generators. Do not lock them behind unlock-signature.
7. **No cookie theater.** No banner. No trackers. Keep it.
8. **No Google Fonts.** Live shop self-hosts Young Serif + Atkinson. Keep it. Drop leftover Iowan/Palatino if the stack still names them.
9. **Success is not a merged leftover PR.** CEO: money in + one forwardable EUR OFFERTE page on the live origin. GATE GREEN is the **page** side of that test (R1–R8 designed out on live). Money-in is Wallet, not Builder.
10. **Do not implement from RED plans** (02, 08). Next Builder write that is not this list is a **one-pass live shop change**, not another markdown punch-list in this leftover repo.

---

## Already GREEN on the live shop (do not regress)

| Lock | Live evidence 2026-08-27 |
| --- | --- |
| No fake BE0 | “KBO/BTW: nog niet toegekend.” Privacy: no ondernemingsnummer. |
| OFFERTE only (shop face) | Prices carry “geen BTW-factuur (OFFERTE).” No FACTUUR stamp. Privacy negation allowed. |
| No Google Fonts / no Inter | Local `fonts/*.woff2`. Chalkboard, not cream Inter on sovereignforge. |
| Privacy + identity footer | `/privacy.html` 200, footer linked, Geel, Gmail, GBA, no cookiebanner. |
| Custom 404 | HTTP 404, title “Pagina niet gevonden — SovereignForge”, links home + privacy. |
| Demos | “Open het voorbeeld” → kit hosts 200 (club Golfbreker, menu, sponsor, lid). |
| Contact has no coin | `/contact.html` visible USDC/Solana/Phantom = 0. Mail only, no form. |
| Tap 44 on SF chrome | `.btn` / `nav a` declare `min-height: 44px` (keep). |

treasury-tools cream + privacy 404 **is not** in this GREEN table.

---

## Bar for GREEN (closed test)

Builder GATE is GREEN only when **all** of the following are true **on live `https://sovereignforge.surge.sh/`** in one pass (re-fetch, do not trust leftover git):

1. **One origin.** Shop HTML in the deploy tree **is** this host. leftover `solana-invoice` `index.html` / `catalog.html` are not the shop. `treasury-tools.surge.sh` is not a second shop face.
2. **EUR-first face.** Visible `USDC` / `Solana` / `Phantom` = 0 on `/` and `/pakketten.html` (title, meta, h1, lede, chips, CTAs). Price is `€N`.
3. **Crawlable.** Live `robots.txt` is `Allow: /` and does not contain `Disallow: /`. Same for kit hosts still linked from the shop.
4. **Frozen SKUs.** Either one hero OFFERTE on home, or the closed six — never eleven. Dual-invoice / Peppol Ready / Eén klus / 9/49 toys **off** the table.
5. **Rails after akkoord.** No treasury address, QR, or copy-button on first paint. No “Betaal N USDC” on the face.
6. **REVIEWER ten hard-fails PASS** on this host (USDC-on-face, demo, FACTUUR, footer, robots, cream/Inter, Google Fonts, fake BE0, privacy, cookie theater). Rubric: [docs/ultra-2026-08-27/REVIEW-RUBRIC.md](https://github.com/eyeskull2220/solana-invoice/blob/cursor/review-rubric-6fa9/docs/ultra-2026-08-27/REVIEW-RUBRIC.md) on #112 — score **live shop**, not leftover `main`.
7. **YELLOW Y1–Y4** designed out or explicitly accepted in the shop spec (not left as accidents).

Until then: **RED**. Partial euro stickers, leftover-repo `rg` clean, and unmerged `#111` are not GREEN.

---

## This run

| Did | Did not |
| --- | --- |
| Fetched live sovereignforge (home, pakketten, betalen, contact, privacy, robots, 404, SITE.md, DESIGN.md) and treasury-tools + sample kit hosts | Edit shop HTML, leftover `index.html`, kits, CSS, or Surge |
| Wrote this one remaining list | Mail, KBO, a twelfth kit, a leftover €9/€49 catalog |
| Pointed GATE at the live shop | Treat #111 / `main` / Ultra PRs as shop movement |

**GATE: RED.** Remaining reds R1–R8 must be designed out on [sovereignforge.surge.sh](https://sovereignforge.surge.sh/) before GREEN.
