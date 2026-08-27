# Builder 03 — Adversarial design (Impeccable Persuade)

**Seat:** BUILDER · **Pass:** adversarial design · **Date:** 2026-08-27  
**Mode:** Impeccable **Persuade** (the forwarded URL *is* the product)  
**Method:** dual-agent — Assessment A (design director) `bc-73fdd7e5-5cc0-52e3-abc3-b23b863f187e` · Assessment B (browser evidence) `bc-c41bec02-4c8f-5d40-bf3c-e9292f09bf15`  
**CLI detector:** unavailable (`detect.mjs` not in this tree). Browser evidence is live Surge HTML/CSS/screenshots, 27 Aug 2026.  
**Start from zero:** the live shop is a **bad layout**. Do not refine the costume. Replace the world.  
**Do not publish.** This file is a verdict, not a deploy.

Live faces inspected: [sovereignforge.surge.sh](https://sovereignforge.surge.sh/) (`/`, `/pakketten.html`, `/betalen.html`, `/contact.html`, `/privacy.html`, `styles.css`, `robots.txt`), catalog [treasury-tools.surge.sh](https://treasury-tools.surge.sh/), and the eleven kit hosts linked from the shop.

---

## How to read

| Mark | Meaning |
| --- | --- |
| **RED** | Hard fail for Persuade. A secretaris in Geel will not forward this tonight. Rebuild, do not polish. |
| **YELLOW** | The surface almost does the job, then spends the trust. Fix on the same pass as RED. |
| **GREEN** | Keep. Rare. Do not throw these out when the costume burns. |
| **NOTES** | Synthesis, replacement world, euro-only replacement copy, what the next builder must not do. |

Quoted strings below are **live copy** as fetched. New recommended copy in this file never names a settlement ticker.

**Overall: RED.** Heuristic health **9/32** (heuristics 7 and 10 `n/a` on Persuade). Fail band.

---

## Design health (Nielsen, quality 0–4)

Higher is better. A 4 is excellent. Persuade may mark 7 and 10 `n/a`.

| # | Heuristic | Score | Key issue |
| --- | --- | ---: | --- |
| 1 | Visibility of system status | 2 | `aria-current` on the rail works. The first fold still reports a FX desk, not “this is the blad you send.” Club demo is a PNG that starts below the 1440×900 fold. |
| 2 | Match system / real world | 0 | Belgian club paper is euro, OFFERTE, bestuur. Home lede (quoted in RED-1) is a settlement paragraph. Euro is labeled *omrekening, geen checkout*. |
| 3 | User control and freedom | 2 | Kits open. There is no “print this voorstel / stuur als bijlage.” Shop has no print measure. Betalen is copy-address. |
| 4 | Consistency and standards | 0 | Five visual worlds for one vendor: chalkboard shop, 3-band club kit, cream Desk Noord kits, grey inbox-ops, euro catalog. Same SKU is token-priced on the shop and euro-priced on pipeline / catalog. |
| 5 | Error prevention | 2 | Stamp is OFFERTE, not FACTUUR — keep. Eleven SKUs + indicative Kraken rate + “geen wettelijke factuur” next to a pay CTA still lets bestuur buy the wrong object. |
| 6 | Recognition rather than recall | 1 | `/pakketten.html` is a 9-column table, `min-width: 52rem`. Mobile first fold is truncated columns and a brass scrollbar, not a kit. |
| 7 | Flexibility and efficiency | n/a | Persuade landing, not a power-user tool. |
| 8 | Aesthetic and minimalist design | 1 | Type is self-hosted and hits are 44px. The *world* is pub-chalkboard + wood bezels + brass pill. Decoration, not argument. |
| 9 | Error recovery | 1 | Contact is `"Alleen mail."` Footer punchline is `"KBO/BTW: nog niet toegekend · geen Peppol Access Point"`. No recovery path a voorzitter would accept. |
| 10 | Help and documentation | n/a | Privacy exists; it is not the job of this surface. |
| **Total** | | **9/32** | **Fail. Costume shop with a settlement hero.** |

### Cognitive load

Checklist failures (Persuade): single focus, chunking, visual hierarchy, one thing at a time, ≤4 visible choices, progressive disclosure. **6/8 failed** → high load.

Decision points on the forwarded URL tonight: which of 11 kits; site vs blad vs form vs Peppol vs “één klus”; euro vs charge; fake ZWV / Voorbeeldharmonie / Voorbeeldkeuken vs their club; open voorbeeld vs pay vs mail; shop URL vs kit URL vs `treasury-tools.surge.sh`; whether `"geen BTW-factuur (OFFERTE)"` is safe in the notulen. That is a treasury catalog, not a keukentafel.

### Emotional journey (peak–end)

- **Intended peak:** H1 `"Voor de secretaris die vanavond nog een voorstel naar het bestuur stuurt."` — the only line that belongs.
- **Immediate valley:** the lede is a ticker. On 390×844 the H1 wraps and the settlement paragraph still eats the fold; the phone demo is a crop.
- **False peak:** Geel, vzw, `"ZWV De Golfbreker"` — then a 3-band fanfare website in a wood frame, gold strip `"…is geen echte club of vzw"`.
- **Valley:** brass `"Alle 11 pakketten"` — more SKUs, not a decision.
- **End (what bestuur remembers):** footer `"… KBO/BTW: nog niet toegekend · geen Peppol Access Point · Privacy"`. Peak–end is **ticker → gmail + geen KBO**.

---

## Design-specificity verdict

**Costume. Category-interchangeable. Not a document.**

The shop face is a **theme**, not a voorstel. `styles.css` opens `/* SovereignForge — chalkboard. */` and the tokens are the costume list: `--board` `#0f190f`, `--chalk` `#e8e9da`, `--brass` `#ca9d33`, `--wood` `#432610`. Dark green board + chalk type + brass CTA + 6px wood frame around 390×844 phone PNGs. That is pub-chalkboard / fanfare-cosplay, not a sheet a secretaris prints or WhatsApps to the bestuur.

The club kit is a second costume: **gold demo strip `#d9a441` → navy `#0b283c` → cream `#efebe3`** plus a sunburst badge. Amateur club-site cosplay. The shop’s first kit then **embeds that 3-band site as a “Live telefoonbeeld”** in wood. You are selling a phone screenshot of a costume.

Sponsor / lid / menu landings are a third costume: cream `#f4f1ea` / `#f3efe6` + Iowan + `ui-sans-serif` / `system-ui` + forest `#123c2e`. Swap “Voorbeeldharmonie” for any studio name and it is a generic offerte landing. Inbox-ops is a fourth (cool grey `#eef2f4`). Catalog `treasury-tools.surge.sh` is a fifth shop: cream, euro-first, rounded sage cards, **no** settlement ticker.

Five faces, one vendor. Nothing here is a single authored kitchen-table proposal.

**Inter is not loaded** on any measured host (no `@font-face Inter`, no Google Fonts, no computed `Inter`). The named anti-reference still lands: cream paper + system sans + sage pills is the 2024–26 AI catalog. Shop body is Atkinson + Young Serif — better type, **wrong object**.

---

## RED

Hard fails. Ordered by damage to the forwarded URL.

### RED-1 — First viewport is a settlement desk, not a voorstel

**Attack:** token-on-face / settlement hero.

**Evidence (shop `/`, 1440×900 first screen, no scroll):** rail `SovereignForge · Pakketten · Betalen · Contact` → who-line → H1 (the job) → **lede is charge + FX + “geen kaart, geen IBAN”** → H2 Club- of vzw-site → price chip → wood-framed phone PNG **starts at y≈551 and ends at y≈1318 (below the fold).**

Live lede, quoted:

> Eén OFFERTE-kit die je doorstuurt. Charge blijft USDC op Solana. Euro is omrekening, geen checkout. Indicatief: 1 USDC ≈ €0,86 (Kraken, 27 aug 2026), geen FOD-koers. Geen kaart, geen IBAN.

Live club price chip, quoted: `900 USDC · ±€774 · geen BTW-factuur (OFFERTE)`.  
`/pakketten.html` lede, quoted: `Charge blijft USDC. Euro is omrekening, geen checkout.` (26 ticker hits on that page).  
`/betalen.html` H1, quoted: `Kies het pakket. Betaal dat USDC-bedrag.`

On **390×844** the same stack: H1 wraps, settlement paragraph still above the kit, phone crop only. The voorzitter’s screenshot of the first 900px is a coin desk.

**Why it fails Persuade:** the secretaris cannot forward this. Euro is labeled decoration. Match-to-world = 0.

**Fix (euro only):** first viewport = the blad. Title, for whom, **€**, what lands tonight, OFFERTE. Rail-and-wallet mechanics live on Betalen *after* a kit is chosen — never in the H1/lede/price chip of a shop face. Replacement lede, not live copy:

> Eén OFFERTE-kit die je vanavond doorstuurt. Prijs €774. Geen wettelijke factuur.

### RED-2 — Chalkboard is a costume, not a keukentafel-voorstel

**Attack:** chalkboard.

**Evidence:** CSS file comment and tokens (Assessment B, canvas hex):

| Token | oklch | canvas |
| --- | --- | --- |
| `--board` | `0.20 0.025 145` | `#0f190f` |
| `--chalk` | `0.93 0.02 110` | `#e8e9da` |
| `--brass` | `0.72 0.13 85` | `#ca9d33` |
| `--wood` | `0.30 0.055 55` | `#432610` |

Body sits on `--board`. Feat images: `border: 6px solid var(--wood)`. Primary CTA is brass. Scrollbar is `var(--brass) on var(--board)`. Measure is `42rem` web column, not A4. You cannot lay this on the table next to the koffie. You cannot print it. You cannot paste it into a bestuur-mail as “het voorstel.”

**Why it fails:** Persuade on this product is *document-as-interface*. A dark board is a pub specials menu. The brief’s object is a voorstelblad.

**Fix:** burn `--board / --chalk / --brass / --wood`. One paper system: ink on a single sheet, print measure, no picture-frame bezels. The shop URL **is** the voorstel. Do not “warm up the green.” That is polishing the discarded world.

### RED-3 — The maatstaf is a 3-band club costume

**Attack:** 3-band costume.

**Evidence (club kit `club-site-kit-treasury.surge.sh`):**

```html
<header class="site-header">
  <p class="demo-banner">Demo van de club-site kit · ZWV De Golfbreker is geen echte club of vzw</p>
  <div class="bar"> … </div>
</header>
```

| Layer | Class | bg | Height |
| --- | --- | --- | --- |
| 1 | `.demo-banner` | `#d9a441` (`--lane`) | 29px |
| 2 | `.bar` on header `#0b283c` (`--water-deep`) | navy | 60px |
| 3 | body `--paper` | `#efebe3` | rest of page |

Plus a repeating-conic sunburst mark and a lane-striped navy hero (`repeating-linear-gradient` + `border-bottom: 6px solid var(--lane)`). That is amateur fanfare-website cosplay: gold warning tape, navy hero, cream paper.

The **shop itself is not 3-band** (`<header class="rail">`, transparent over the board). Worse: home sells that 3-band page as `"De maatstaf: ZWV De Golfbreker"` inside a wood phone frame. The anti-reference is the product shot.

**Why it fails:** a forwarded link that opens a costume clubsite trains bestuur to see “student demo,” not “our site.” The gold strip literally says the club is fake.

**Fix:** if the deliverable is a clubsite, the demo is **their** club (named, Geel, no sunburst, no gold/navy/cream stack). If the deliverable is a voorstelblad, the maatstaf is a printed OFFERTE, not a 3-band marketing template. Stop embedding the costume as proof.

### RED-4 — Cream catalog + cream kits (Inter-class slop, even without Inter)

**Attack:** cream / Inter slop.

**Evidence:** Inter **absent** everywhere measured. The slop is the **cream-paper + sage-card + system/Iowan** template:

| Host | Body bg | Accent | Face |
| --- | --- | --- | --- |
| `treasury-tools.surge.sh` | `#f4f1ea` | `#123c2e` | rounded `#fffdf8` cards, euro chips, **no demo images** |
| `menu-kit-treasury.surge.sh` | `#f4f1ea` | `#123c2e` | kicker `DESK NOORD`, pill quoted `199 USDC`, pay card before the card |
| `sponsor-kit` / `lid-kit` | `#f3efe6` | `#123c2e` | sell chrome `#fffdf8` above the blad |
| `vakman` / `peppol-ready` / `solana-invoice` / `dual-invoice` | `#f4f1ea` | `#123c2e` | same landing generator |
| `peppol-chase` | `#f6f3ee` | `#0c4a36` | same family |
| Shop QR only | `#fffdf0` | brass | payment pad, not a shop face |

Catalog H1: `"Pakketten voor clubs en KMO’s. Klaar om te gebruiken."` — category-interchangeable. Two public shops for one vendor: chalkboard token-face vs cream euro-face. A secretaris who bookmarks the wrong one forwards a different company.

**Why it fails:** Impeccable Persuade forbids category habit. This *is* category habit (2025 cream SaaS catalog), plus a second habit (chalkboard). Neither is a Geel voorstel.

**Fix:** one origin, one paper. No sage pills, no rounded card grid as the shop, no second catalog face. Print sheets may be paper; the **shop home must not be that card grid**.

### RED-5 — Shop “demo” is a phone frame below the fold (deliverable is elsewhere or missing)

**Attack:** no demo.

**Evidence, shop home:** four `<img>` only — `previews/club.png` etc., alts all `"Live telefoonbeeld van …"`, 390×844, wood border. **No iframe. No in-page editor. No A4.** On desktop the club PNG starts below the fold. `/pakketten.html`: **zero** images; eleven rows of text. `/betalen.html`: eleven radios, no preview of what you buy.

Kits are mixed — this is why shop-home still fails:

| Kit | What you actually get |
| --- | --- |
| Club | Live named multi-page site + `editor.html` — **real**, wearing the 3-band costume |
| Sponsor / lid | Live iframe blad **under** sell chrome whose first line is a ticker kicker |
| Menu landing | Description + pills. The print card is `menu.html` (Voorbeeldkeuken, **Antwerpen**, euro, no ticker) — two clicks and a different city |
| Pipeline | Live in-page form (euro-first) |
| Dual-invoice | Live offerte sheet — wrong object for a club secretaris |
| Vakman / inbox / peppol-* | File lists / “open the offerte.” Not in the first viewport |

**Why it fails:** a menukaart is an A4 on the pass, not a bezel. A voorstel is a blad you scroll, not a PNG of a phone. “Open het voorbeeld” as a text link after a settlement paragraph is not showing the work.

**Fix:** first viewport **is** the print surface at document width. “Open het voorbeeld” is a control *on that blad*, not a consolation prize under a wood frame. Menu: put `menu.html` on the landing. Shop: stop shipping 390×844 PNGs as proof.

### RED-6 — Footer is empty as a close (identity dump, not a voorstel-end)

**Attack:** empty footer.

**Evidence, shop `<footer>` exists and is not whitespace.** Quoted:

> SovereignForge · OFFERTE/VOORBEELD · Geel / België · sasha.de.vree.rene@gmail.com · KBO/BTW: nog niet toegekend · geen Peppol Access Point · Privacy

Plus a five-link foot-nav. That is a **compliance dump**. Persuade-end is “who does this, what happens after akkoord, how the secretaris mails it into the notulen.” The last line bestuur reads is *this person is not a bedrijf*.

`peppol-chase-treasury.surge.sh` has **no `<footer>`** (binary empty). Sponsor/lid demo-contact: `"hello@studio.example."` Menu landing footer: Desk Noord + ticker + Twelve.tools. Catalog footer has no privacy link.

**Why it fails:** peak–end rule. The H1 promises tonight’s voorstel; the end withholds KBO and Peppol as the punchline. Argument-empty = empty.

**Fix:** close as a voorstel close — who, Geel, what happens after akkoord, mail for the secretaris. Legal voids (`nog niet toegekend`) live on Privacy, not as the colophon’s last beat. Every kit host gets a `<footer>` with identity; peppol-chase is currently none.

---

## YELLOW

Not the costume’s headline, still lethal on the same night.

### YELLOW-1 — Eleven SKUs are the product

Home CTA `"Alle 11 pakketten"`. Pakketten table columns: Pakket / Uitkomst / Inhoud / Voor wie / token / € indicatief / BTW-status / Voorbeeld / Betalen. Betalen: **11 radios** before a QR. Mobile pakketten is a clipped grid.

Keukentafel is one choice, maybe two (clubsite **or** the blad). The rest is a treasury inventory. Park it off the forwarded URL.

### YELLOW-2 — Split names, split cities, split prices

Shop wordmark: **SovereignForge** (English steel). Kits: **Desk Noord**, **Studio Noord**, Antwerpen `Noorderlaan 12`, `hello@studio.example`. Catalog: euro. Shop: token units for the same SKU (pipeline is `€399` on its own host and token-priced on the chalkboard list).

Who goes in the notulen? A voorzitter who opens three tabs thinks they were phished.

### YELLOW-3 — `robots.txt` `Disallow: /` on the public shop

Verbatim on `sovereignforge.surge.sh`:

```
User-agent: *
Disallow: /
```

Same on kit hosts. Out of *paint*, in for Persuade: a face that cannot be indexed cannot be found, and a forwarded URL that looks “blocked” to a cautious voorzitter dies. **Do not publish a fix from this PR.** Flag only.

### YELLOW-4 — Wordmark and chrome leak the theme

`SovereignForge` is not a Geel secretariaat. `::selection` and the scrollbar are brass on board. Contact H1 is `"Alleen mail."` — a locked door, not an invitation to send the blad.

### YELLOW-5 — Dual public catalogs

`treasury-tools.surge.sh` is cream, euro-first, sage cards, Stripe-sandbox note, **zero** ticker hits, **no privacy**, **no images**. It is the better price face and the worse object (card grid, no blad). Two shops = two companies. Kill one.

---

## GREEN

Keep these when the world is replaced. Do not treat them as a pass for the shop.

1. **The H1 names the actual job.** `"Voor de secretaris die vanavond nog een voorstel naar het bestuur stuurt."` That sentence is the product. Put it on a blad, not a board.
2. **Stamp is OFFERTE / VOORBEELD, never FACTUUR.** Privacy negation `"geen FACTUUR-module"` is allowed. Dual-invoice *slug* is leftover naming; the sheet still says OFFERTE. Keep the stamp discipline.
3. **Some kits already *are* documents.** Sponsor and lid put a printblad in an iframe (`Voorbeeldharmonie seizoen 2026–27`, euro in the table, `OFFERTE` stamp). `menu.html` is a real print card (EU-14, euro). Club kit is a real multi-page site + editor. Pipeline has a live form. **The shop refuses to *be* those documents.** Lift the blad onto the forwarded URL; do not invent a sixth costume.
4. **Hygiene that is not persuasion:** `lang="nl"`, skip link, 44px targets, self-hosted Young Serif + Atkinson on the shop (no Google Fonts), no cookie banner, no invented `BE0` number, `"KBO/BTW: nog niet toegekend"` (honest — move it off the close).

GREEN does not rescue RED-1 through RED-6. A good H1 on a chalkboard settlement desk is still a fail.

---

## NOTES

### The object

A **keukentafel-voorstel** is a sheet a secretaris in Geel can:

1. Open on a phone without a costume header.
2. Screenshot or print as one page that still makes sense.
3. Forward to bestuur with subject `voorstel clubsite — ter goedkeuring vanavond`.
4. Defend in the notulen in **euro**, OFFERTE, one kit, one city, one name.

The live shop is none of those. It is a **theme park of proof**: chalkboard lobby, 3-band ride, cream gift shop, grey ops kiosk. Start from zero means: **one forwarded URL, one paper, one kit tonight.**

### Replacement world (not a polish)

| Burn | Replace with |
| --- | --- |
| `--board / --chalk / --brass / --wood` | Ink on paper. Print measure. No bezel. |
| Gold / navy / cream club header | Named club, no tape, no sunburst, no pinstripe hero |
| Cream + sage card grid as shop | The blad itself. Cards are for grocery sites. |
| 390×844 PNG “telefoonbeeld” | The deliverable at document width in the first viewport |
| Token in title / H1 / lede / price chip | **€** on the face. Settlement only on Betalen after choice |
| `"Alle 11 pakketten"` as the CTA | One primary kit. Secondary optional. Rest unlinked from the forwarded URL |
| Footer as KBO-void punchline | Voorstel close. Voids on Privacy |
| Two catalogs | One origin |

Impeccable: **refinement preserves; redesign replaces.** This pass is redesign. Do not split the difference (cream board, brass on paper, “softer chalkboard”). That is how the costume survives.

### Replacement copy (new — no settlement ticker)

Use or cut. Dutch. Euro. OFFERTE.

**Home lede**

> Eén OFFERTE-kit. Prijs €774. Vanavond door te sturen. Geen wettelijke factuur.

**Club line**

> Home, agenda, lid worden, contact. Open het voorbeeld hieronder — dat is de site, geen foto van een telefoon.

**Menu line**

> De kaart die de keuken toont, plus QR naar de EU-14. Prijs €171. Geen clubsite.

**Close**

> SovereignForge, Geel. Mail dit blad naar het bestuur. Na akkoord: dezelfde mail, dan leveren we het bestand.

**Do not write** a FX sentence, a chain name, or a token ticker on any shop face. Betalen may explain settlement **after** the kit is chosen; that page is not the forwarded URL.

### Persona red flags (walked)

**(a) Secretaris Geel, forwarding tonight.** Cannot print the shop. Must explain Solana, Kraken, and “geen FOD” in WhatsApp. Eleven lines to defend. From-address is Gmail. Maatstaf is a fake zwemclub. They will not hit send.

**(b) Voorzitter / bestuur receiving the link.** Opens near-black green. Second sentence refuses card and IBAN. Sees a 3-band demo that announces it is fake. Footer: no KBO, no Peppol. Looks like a stall, not a leverancier. Instant “wie heeft dit gestuurd?”

**(c) Keuken / horeca, menu kit.** Shop shows a phone crop. Landing is Desk Noord / Antwerpen / ticker pill / € count = 0. The real card is `menu.html`, two clicks away. A kitchen tapes a card to the pass. This landing is a wallet string.

### What this file is not

- Not a CSS patch, not a Surge deploy, not a robots fix. **Do not publish.**
- Not a pass for the chalkboard because type is self-hosted. Type is GREEN-4; the *object* is RED-2.
- Not a claim that Inter is loaded. It is not. Cream + system sans is the slop that landed.
- Not a claim the shop footer DOM is empty. The `<footer>` has text. The **close** is empty.

### Builder follow-up (after this doc, still not this PR)

1. Replace DESIGN world: paper voorstel, not board.  
2. Euro on every shop-face chip; settlement only on Betalen.  
3. First viewport = deliverable (blad or full site page).  
4. Kill the 3-band club costume as maatstaf; name a real Geel club or drop the pretence.  
5. One origin. One name. One city.  
6. Footer as close. Privacy keeps the voids.  
7. Then — and only then — a later ship PR. Not from here.

### Questions for the next builder

1. **Primary forwarded URL:** clubsite blad, or sponsorblad, or menu card? (Pick **one**. Eleven is how Persuade died.)  
2. **Maatstaf:** named Geel club they may actually mail, or a clearly-stamped VOORBEELD sheet with no 3-band?  
3. **Catalog `treasury-tools.surge.sh`:** delete, or redirect to the one shop? It is already the better price face and the wrong object.

Questions skipped in this seat: this document is the persist. Scope is adversarial design only.

---

## Evidence appendix (Assessment B, compact)

Fetched 27 Aug 2026. Viewport 1440×900 unless noted.

| Surface | Fonts | Face | Ticker hits (live) | Demo | Footer |
| --- | --- | --- | ---: | --- | --- |
| Shop `/` | Young Serif + Atkinson | chalkboard `#0f190f` | 12 | PNG bezels, below fold | identity dump |
| `/pakketten.html` | same | same | 26 | table of links, no iframe | same |
| `/betalen.html` | same | same; QR `#fffdf0` | 17 | 11 radios + QR | same |
| `/contact.html` | same | same | 0 | none | same (in first screen) |
| `/privacy.html` | same | same | 1 | legal | same |
| `treasury-tools.surge.sh` | Iowan / Palatino | cream `#f4f1ea` + sage | **0** | no images | filled, no privacy |
| Club kit | system-ui | 3-band gold/navy/cream | 5 | live named site + editor | PAY-TO line on demo |
| Menu landing | Iowan | cream `#f4f1ea` | 7 | description; card at `menu.html` | Desk Noord |
| Sponsor / lid | Iowan | cream `#f3efe6` | 1 | live iframe blad | exists |
| peppol-chase | system-ui | cream `#f6f3ee` | 8 | file list | **no `<footer>`** |
| pipeline | system-ui | cream `#f3efe6` | **0** | live form | exists |
| solana-invoice kit | Iowan | cream `#f4f1ea` | **0** | `Open het voorbeeld`; title euro | exists |

Shop `:root` (quoted from live `styles.css`): `--font-display: "Young Serif"…; --font-body: "Atkinson Hyperlegible"…`  
No `fonts.googleapis.com` on any fetched page.  
No computed `Inter` on any fetched page.

**First-screen transcript, shop `/` 1440×900:** skip · rail · who-line with `Bekijk de pakketten` · H1 · settlement lede · `Club- of vzw-site` · token price chip · top of wood-framed 3-band PNG. Footer not in view.

**First-screen transcript, shop `/` 390×844:** rail wraps · who · H1 (y≈191–320) · full lede to y≈466 · club h2 + blurb + price · PNG starts y≈716. Footer not in view.

---

*End of 03-adv-design. Do not publish. Rebuild the forwarded URL as one euro OFFERTE blad; burn the board.*
