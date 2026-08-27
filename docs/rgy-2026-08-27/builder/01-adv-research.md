# Builder layout — adversarial research (start from zero)

**Date:** 27 Aug 2026  
**Scope:** Live Builder face and the four kits the home page sells. Assume the Builder layout is bad until a live URL proves otherwise.  
**Operator ≠ freelancer.** Operator is SovereignForge in Geel (secretaris → bestuur). Leftover English “for freelancers” SKUs are not the buyer.  
**Not done:** no mail sent, no KBO invented, no implementation.

## Live URLs opened

| Surface | URL | HTTP |
|---|---|---|
| Builder home | https://sovereignforge.surge.sh/ | 200 |
| Pakketten (11) | https://sovereignforge.surge.sh/pakketten.html | 200 |
| Betalen | https://sovereignforge.surge.sh/betalen.html | 200 |
| Contact | https://sovereignforge.surge.sh/contact.html | 200 |
| Privacy | https://sovereignforge.surge.sh/privacy.html | 200 |
| robots (Builder) | https://sovereignforge.surge.sh/robots.txt | 200 `User-agent: *` / `Disallow: /` |
| Club kit | https://club-site-kit-treasury.surge.sh/ | 200 |
| Club lid | https://club-site-kit-treasury.surge.sh/lidworden.html | 200 |
| Club editor | https://club-site-kit-treasury.surge.sh/editor.html | 200 |
| Club robots | https://club-site-kit-treasury.surge.sh/robots.txt | 200 `Disallow: /` |
| Menu kit sell | https://menu-kit-treasury.surge.sh/ | 200 |
| Menu kaart | https://menu-kit-treasury.surge.sh/menu.html | 200 |
| Menu allergenen | https://menu-kit-treasury.surge.sh/allergenen.html | 200 |
| Menu QR PNG | https://menu-kit-treasury.surge.sh/allergenen-qr.png | 200 320×320 PNG |
| Menu robots | https://menu-kit-treasury.surge.sh/robots.txt | 200 `Disallow: /` |
| Lid kit sell | https://lid-kit-treasury.surge.sh/ | 200 |
| Lid form | https://lid-kit-treasury.surge.sh/lid.html | 200 |
| Lid robots | https://lid-kit-treasury.surge.sh/robots.txt | 200 `Disallow: /` |
| Sponsor kit sell | https://sponsor-kit-treasury.surge.sh/ | 200 |
| Sponsor blad | https://sponsor-kit-treasury.surge.sh/offerte.html | 200 |
| Sponsor robots | https://sponsor-kit-treasury.surge.sh/robots.txt | 200 `Disallow: /` |
| Leftover catalog | https://treasury-tools.surge.sh/ | 200, euro-first, Stripe sandbox copy |
| Leftover robots | https://treasury-tools.surge.sh/robots.txt | 200 `Disallow: /` (HTML still `index,follow`) |
| Leftover CSV | https://csv-cleaner-treasury.surge.sh/ | 200, English, no USDC |
| Leftover Form | https://form-to-email-treasury.surge.sh/ | 200, English, 49 USDC |
| Leftover RSS | https://rss-to-webhook-treasury.surge.sh/ | 200, English, 49 USDC |
| Eén klus (live) | https://solana-invoice-treasury.surge.sh/ | 200, **€49**, no USDC on face |
| Inbox-ops | https://inbox-ops-treasury.surge.sh/ | 200, “Demo freelancer · Antwerpen” |
| Pipeline | https://pipeline-treasury.surge.sh/ | 200, “Demo freelancer · Antwerpen”, title €399 |

This repo’s working tree (`index.html`, `catalog.html`) is still the English 9 USDC freelancer invoice. That is leftover SKU source, not the Builder buyer.

## Verdict

The Builder face at https://sovereignforge.surge.sh/ is a stacked-phone catalog that cannot be forwarded to a bestuur tonight. Four featured kits disagree with each other (zwemclub vs fanfare vs keuken vs freelancer), seven extra SKUs sit behind “Alle 11 pakketten”, a twin euro catalog and three English tools are still live, crawlers are told `Disallow: /`, and the menu URL the home page sells has no print control and no QR.

---

## RED / YELLOW / GREEN

| ID | Attack | Finding | Grade |
|---|---|---|---|
| A1 | Kit research — four live kits vs claimed job | Club demo is ZWV De Golfbreker (zwemmen, Geel) with a **900 USDC pay-box on the homepage** the secretaris would forward. Lid + sponsor demos are a different invented club (**Voorbeeldharmonie**, fanfare). Menu demo is **Voorbeeldkeuken / Desk Noord / Studio Noord**, Antwerpen, plus a Twelve.tools footer. One buyer job, four identities. | **RED** |
| A2 | Buyer job — secretaris → bestuur vanavond | Home H1 is the right job. The artefact you open is not. Club kit puts vendor checkout (`Stuur 900 USDC`, memo `club-site-900`, Solana Pay, editor link) on the club page. Lid form is a fanfare sheet that mails `hello@studio.example`, not a club secretariaat. Sponsor blad says “zaal nog in te vullen” four times. Board packet is three different fictional orgs plus a pay address. | **RED** |
| A3 | Buyer job — claimed lid fields vs live form | Forge home lists: naam, e-mail, **telefoon, gemeente**, instrument/stem, type lid, **repetitie en startdatum**. Live `lid.html` fields: naam, e-mail, instrument/stem, type lid, nota. **Missing telefoon, gemeente, repetitie, startdatum.** Club-site `lidworden.html` is thinner still: mailto only (naam / geboortejaar / groep in the mail body). Two “lid” products, neither matches the home bullet list. | **RED** |
| A4 | Leftover SKUs — English tools still live | https://csv-cleaner-treasury.surge.sh/ (English CSV tool, **0 USDC**, no Solana). https://form-to-email-treasury.surge.sh/ and https://rss-to-webhook-treasury.surge.sh/ still sell **49 USDC billed via Solana Invoice** in English. This repo’s `catalog.html` still lists them. Operator is not that freelancer. | **RED** |
| A5 | Leftover SKUs — twin euro catalog | https://treasury-tools.surge.sh/ is still a live SovereignForge catalog: **prijs in euro** (€900 / €199 / €349 …), **0× USDC**, “Stripe sandbox / test only”, JSON-LD ItemList of 11 kits, `<meta name="robots" content="index,follow">` while `robots.txt` says `Disallow: /`. Builder home and leftover catalog disagree on unit of charge. | **RED** |
| A6 | Leftover SKUs — 11-pack dump on Builder | Home features 4 kits then CTA “Alle 11 pakketten”. Table adds vakman, inbox-ops, pipeline, Peppol chase, dual-invoice, Peppol Ready, één klus. Inbox-ops and pipeline still brand **“Demo freelancer · Antwerpen”**. Peppol kits are not a secretaris-tonight job. | **RED** |
| A7 | USDC-first face — split with live één klus | Builder home: “Charge blijft USDC op Solana. Euro is omrekening.” Live één klus https://solana-invoice-treasury.surge.sh/ title **“Eén klus — €49”**, H1 **“€49”**, “Betaalgegevens na akkoord. Mail …gmail.com”. **No USDC on that face.** Pipeline title is **“Lead tot offerte — €399”**. Leftover catalog is euro-only. USDC-first is not the estate; it is one page. | **RED** |
| A8 | Generic Voorbeeldharmonie | https://lid-kit-treasury.surge.sh/lid.html and https://sponsor-kit-treasury.surge.sh/offerte.html both title **Voorbeeldharmonie**, kicker “Harmonie · vzw-voorbeeld”. Copy admits “verzonnen fanfare”. Club kit on the same home is a **zwemclub**. A bestuur cannot tell which club they are buying. | **RED** |
| A9 | robots `Disallow: /` | Builder + all four kits + leftover catalog: `User-agent: *` / `Disallow: /`. The intended public offer tells crawlers not to index. Leftover catalog HTML still asks `index,follow`. Search and link-preview will not carry the secretaris job; the twin catalog’s meta fights its own robots.txt. | **RED** |
| A10 | No print / QR on the URL the Builder sells | Forge home “Open het voorbeeld” for menu → https://menu-kit-treasury.surge.sh/ (sell page). That page: **no `<img>` QR, no `@media print`, no `window.print`, no print button.** Claim “Printkaart en QR naar de EU-14” / “Gedrukte QR (lokaal gegenereerd)” is false on the linked URL. Inner `menu.html` has a **static** `allergenen-qr.png` (320×320, loads) and print CSS, still **no print button**; copy says “via uw browser”. Sponsor/lid inner sheets: print CSS only, no print control, no QR. | **RED** |
| A11 | Pay-on-demo (club) | https://club-site-kit-treasury.surge.sh/ homepage and footer: pay-to `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3`, 900 USDC, memo, Solana Pay. The “voorbeeld dat je vanavond doorstuurt” is a vendor checkout wearing a zwemclub skin. | **RED** |
| A12 | Brand soup | Kickers/footers seen live: SovereignForge, Desk Noord, Studio Noord, Twelve.tools, Treasury tools, “Demo freelancer · Antwerpen”. Operator Gmail on Builder footer. Not one name a bestuur can write in the notulen. | **RED** |
| B1 | Menu inner sheet vs sell page | `menu.html` does contain EU-14 codes, allergenen URL, and a real PNG QR (naturalWidth 320). Allergenen page lists the 14 names. So the kit *contains* a kaart; the Builder link does not open it, and nothing prints it. | **YELLOW** |
| B2 | Sponsor inner blad vs “geen drie bullets” | https://sponsor-kit-treasury.surge.sh/offerte.html has a real three-row table (Vriend €150 / Seizoen €400 / Hoofdsponsor €900) matching the Builder mini-table. Still Voorbeeldharmonie, venues unfilled, no print button, sell chrome is a pay address above an iframe. | **YELLOW** |
| B3 | Betalen QR SVGs | https://sovereignforge.surge.sh/betalen.html has payment QR SVGs for 49, 199, 249, 299, 349, 399, 490, 900 (all HTTP 200). That is vendor pay QR, not the kitchen allergen QR the menu kit promised. | **YELLOW** |
| B4 | Euro as omrekening (Builder home only) | Home/pakketten/betalen: “1 USDC ≈ €0,86 (Kraken, 27 aug 2026), geen FOD-koers.” Honest on that host. Contradicted by leftover euro catalog and €49 één klus. | **YELLOW** |
| B5 | Club kit specificity | Golfbreker is a fuller static club (home/over/agenda/lid/contact, demo banner, `.example` mailbox) than Voorbeeldharmonie. It is still the wrong sport for a fanfare lid/sponsor pair, and it still bills 900 USDC on the demo. | **YELLOW** |
| B6 | Mailto as “formulier” | Lid kit uses `action="mailto:hello@studio.example"`. Club lid is a mailto button to `info@golfbreker.example`. Neither is a secretariaat inbox. Mailto is declared; it is not the claimed job. | **YELLOW** |
| C1 | No fake KBO number | Every opened page that mentions KBO says **“nog niet toegekend”**. No invented enterprise number. Privacy: natuurlijke persoon, Geel, geen vennootschap. | **GREEN** |
| C2 | Demo mailboxes are RFC 2606 | Club: `info@golfbreker.example`. Lid/sponsor/menu: `hello@studio.example`. Not a harvested inbox. (Operator Gmail is on the Builder colophon, not inside the club demo identity.) | **GREEN** |
| C3 | No wallet-connect on kit pages | Club/menu/lid/sponsor do not connect a wallet. Pay is copy-address / Solana Pay URI / (Builder) static QR. | **GREEN** |
| C4 | Allergenen EU-14 list exists | https://menu-kit-treasury.surge.sh/allergenen.html has the 14 legal names + demo dishes. Claimed on the inner sheet; not on the sell URL. | **GREEN** |
| C5 | Treasury address is consistent where USDC is shown | `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3` + mint `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v` on Builder betalen, club pay-box, menu sell, lid/sponsor sell chrome. | **GREEN** |
| C6 | Honest Peppol non-claim on Builder footer | “geen Peppol Access Point” on SovereignForge colophon. (Peppol SKUs still sit in the 11-pack; the non-claim is the green part.) | **GREEN** |
| C7 | Privacy page exists | https://sovereignforge.surge.sh/privacy.html v1 27 Aug 2026: no first-party cookies claimed, Gmail = possible transfer outside EER, GBA link. | **GREEN** |

Counts: **RED 12 · YELLOW 6 · GREEN 7**. Builder layout does not clear the secretaris job.

---

## NOTES

### 1. Kit research (what a hostile board member would open)

Opened the four “voorbeeld” links from https://sovereignforge.surge.sh/ as a secretaris would: new tab, no editor, no source.

- **Club** (https://club-site-kit-treasury.surge.sh/): Dutch zwemclub skin, demo banner “geen echte club of vzw”, then immediately a 900 USDC pay module on the same homepage the H1 asked you to forward. Agenda is four September 2026 demo rows. Lid path is mailto, not the lid-kit form. `robots.txt` Disallow. Identity: Golfbreker / Geel / zwemmen.
- **Menu** (https://menu-kit-treasury.surge.sh/): Not a kaart. It is a Desk Noord sell letter: 199 USDC, copy address, Solana Pay URI, Twelve.tools footer. The kaart lives one click away at `menu.html`. Favicon 404 (console). Sell page has no QR and no print.
- **Lid** (https://lid-kit-treasury.surge.sh/): Desk Noord sell chrome + iframe of `lid.html`. Title and iframe: **Voorbeeldharmonie seizoen 2026–27**. Form submits mailto `hello@studio.example`. Missing the home-page field list (see A3).
- **Sponsor** (https://sponsor-kit-treasury.surge.sh/): Same iframe pattern. Inner blad is **Voorbeeldharmonie** concert dates with “zaal nog in te vullen”. Three example packages match the Builder table. Print CSS, no print control, no QR.

A kit that cannot survive “open the link, print, put in the map” is not a kit.

### 2. Buyer jobs (operator, not freelancer)

The only job the Builder H1 states: *secretaris, vanavond, één voorstel naar het bestuur.*

| Job | What would pass | What is live |
|---|---|---|
| Forward a club site | One named club, no vendor pay, Dutch, print or share URL | Golfbreker + 900 USDC pay-box + editor.html |
| Forward a lid form | Fields the home page listed, mails the club, not Studio Noord | Fanfare form, 5 fields, `hello@studio.example` |
| Forward a sponsor blad | Named club, filled zaal, print button, no “verzonnen fanfare” | Voorbeeldharmonie, empty venues |
| Kitchen kaart | Print button + QR on the first URL | Sell page; QR only on inner PNG |

Inbox-ops and pipeline still say **“Demo freelancer · Antwerpen”**. That is the leftover freelancer SKU wearing a Dutch kit. Operator is not that person.

### 3. Leftover SKUs

Still answering on the public internet, 27 Aug 2026:

1. English CSV / Form-to-Email / RSS tools (this repo’s `catalog.html` + three surge hosts). Form and RSS still price **49 USDC via Solana Invoice**; that invoice host is now an **€49** Dutch page with no USDC.
2. https://treasury-tools.surge.sh/ — full 11-pack **in euro**, Stripe sandbox sentence, `index,follow` meta vs `Disallow: /`.
3. Builder `pakketten.html` 11-row table (Peppol ×2, dual-invoice, vakman, inbox, pipeline, één klus).
4. This git tree: English “For freelancers… 9 USDC” `index.html`.
5. Twelve.tools links on menu / vakman / peppol-ready kit footers.

Leftovers are not dormant. They are a second storefront with a different currency and a different buyer.

### 4. USDC-first face

Builder home, pakketten, betalen: USDC is the charge, euro is Kraken 27 Aug 2026 ≈ €0,86, “geen FOD”, “geen kaart, geen IBAN”. That sentence is locally true.

It is globally false:

- Leftover catalog: “Prijs in euro”, prices €900 / €199 / …, **USDC count 0**.
- Eén klus live: **€49**, pay-after-mail.
- Pipeline title: **€399**.
- Menu/lid/sponsor sell pages: USDC amount, no euro omrekening (so the Builder lede is not repeated on the artefact).
- Club demo: USDC on the club page itself.

A bestuur that opens the leftover URL or één klus never sees USDC-first. A bestuur that opens the club voorbeeld sees USDC as a shakedown, not as charge policy.

### 5. Generic Voorbeeldharmonie

Live strings:

- Lid `<title>`: “Voorbeeldharmonie — lid worden (OFFERTE)”
- Sponsor `<h1>`: “Voorbeeldharmonie”
- Both: “Voorbeeldharmonie is een verzonnen fanfare voor dit blad/formulier.”

Club kit on the same Builder home is **ZWV De Golfbreker**, zwemmen, Geel. Menu kit is **Voorbeeldkeuken**, Noorderlaan 12, 2030 Antwerpen. Inbox/pipeline: **Studio Noord**, “Demo freelancer · Antwerpen”.

Generic is not a legal-safe placeholder here. It is three clubs and one kitchen sold as one voorstel.

### 6. robots Disallow

Exact body on Builder, club, menu, lid, sponsor, leftover catalog:

```
User-agent: *
Disallow: /
```

Effect: Google, link-unfurlers that honour robots, and any “can I find this club” search are told to skip the offer. The leftover catalog still emits `index,follow` in HTML — the one host that might get indexed is the **euro** twin, not the USDC Builder.

If Disallow is intentional (OFFERTE not a public shop), the home page still presents as a public catalog with canonical `https://sovereignforge.surge.sh/`. Those two intents cannot both be true.

### 7. No print / QR

Attack is against the **URL the Builder puts in the secretaris’s hand**, not against a nested file a researcher can grep.

| URL | Print button | `@media print` | Kitchen/sponsor QR |
|---|---|---|---|
| https://menu-kit-treasury.surge.sh/ | no | no | no |
| https://menu-kit-treasury.surge.sh/menu.html | no (`window.print` absent; text “via uw browser”) | yes | yes, static PNG `allergenen-qr.png` (loads 320×320) |
| https://lid-kit-treasury.surge.sh/lid.html | no | yes | no |
| https://sponsor-kit-treasury.surge.sh/offerte.html | no | yes | no |
| https://sovereignforge.surge.sh/betalen.html | n/a | n/a | **payment** QR SVGs only |

Sell-page copy on the menu kit still claims “Gedrukte QR **(lokaal gegenereerd)**”. The inner QR is a checked-in PNG, not generated in the page. That claim is false even on the inner sheet.

### Constraints honoured

- No mail to `sasha.de.vree.rene@gmail.com` or any demo address.
- No KBO number invented; live text already says “nog niet toegekend”.
- No implementation. This file is research only.

### What would have to be true before Builder is not assumed bad

One named club on all four artefacts; no vendor pay on the forwarded voorbeeld; USDC-first on every live catalog (or the euro twin taken down); leftover English SKUs gone; lid fields match the home list; print control + allergen QR on the **first** menu URL; robots.txt matching the actual index intent; operator name only — no freelancer, no Desk Noord, no Twelve.tools on the bestuur packet.

None of that is live on 27 Aug 2026.
