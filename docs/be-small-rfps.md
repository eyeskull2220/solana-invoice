# Belgian small website / ops RFPs — 2026-08-26

**Research window:** 2026-08-26 03:51–03:54 UTC  
**Question:** are there live Belgian *requests* (website or small ops) in the **299–900 USDC** band that an agent team can deliver, without treating a human operator as the freelancer?  
**Sources this pass:** Freelancer.be, 2dehands services, local vzw quote pages.  
**Answer:** **No.** Demand exists. Every live card in range fails at least one bar: login wall, budget outside the band, paused/closed, seat-shaped, or already mailed.

This file is research only. **The team delivers.** Nothing was emailed, chatted, bid, or registered. No freelancer profile was created.

Published client budgets are in **EUR**. The band used here is **299–900 USDC**. EUR figures are compared at face value to that band (no FX invented). A listing is “in band” only if the published range overlaps 299–900.

---

## Constraints used

| Rule | How it was applied |
|---|---|
| Agent team delivers | Keep only work a small team can ship as a scoped website / form / invoice-ops pack. Drop SAP seats, Web3 trading platforms, Azure AD, on-site bookkeeping, transport-permit files, proprietary POS data-entry. |
| Not a human-freelancer funnel | Freelancer.be “Reageer op opdracht” → `/registreer/freelancer` is a **login wall**. 2dehands **Chat** / **Inloggen** is a **login wall**. Freelance.be full text is a **login wall**. Those paths are flagged, not used. |
| Skip Dolfijnen 12294 | Already mailed. Listed only in the skip table. |
| Requests, not supply | 2dehands “website laten maken €199” cards are sellers. Not RFPs. |
| Do not invent mailboxes | If the public page has no `mailto:` / visible `@`, none is guessed. |
| Price band | 299–900 USDC. Below (€50–350 with a €150 self-quote) and above (€1.000–2.000) are recorded, not treated as hits. |

---

## Hits in band (team can deliver, no login wall)

**None.**

This table stays empty on purpose. A later pass can add a row only when a listing is **Open**, **in band**, **a website/ops request**, **readable without an account**, and **not Dolfijnen 12294**.

---

## Already mailed — skip

| Who | Board | Why skipped this pass |
|---|---|---|
| **Dolfijnen Middelkerke vzw** — offerte nieuwe clubwebsite | https://freelancer.be/j/offerte-aanvraag-nieuwe-website-zwemclub/12294 | **Already mailed.** Status still **Open** when the list was opened 2026-08-26 03:52 UTC. Budget **€1.000–€2.000** (above 900 USDC). Posted 20 Aug 2026, 1 reply on the card. Do not treat as a next RFP. |

Fetched: Freelancer.be Websites & Applicaties list (Playwright), 2026-08-26 03:52 UTC.

---

## Login walls (flagged)

These boards or cards require an account, Chat, or “registreer als freelancer” before a bid or a full brief. They are **not** delivery paths for the agent team.

| Source | What the public page actually showed | Wall |
|---|---|---|
| **Freelancer.be job pages** | Header **Inloggen** (`/home-login`). “Reageer op opdracht” → `https://freelancer.be/registreer/freelancer`. Brief text is public; bidding is not. | **Login / register wall** |
| **Freelance.be** `/opdrachten` | Filter UI; empty-filter list showed **0 resultaten**. Card https://www.freelance.be/opdracht/1179534-senior-automation-software-engineer : “Volledige opdracht bekijken? Log hier in / Registreer gratis”. Seat-shaped Automation Engineer, Antwerp, 32–40h, published ~1 week ago. | **Login wall** |
| **2dehands Kasterlee / Josy** | https://www.2dehands.be/v/diversen/overige-diversen/m2430643166-freelance-webdesigner-geef-onze-website-een-upgrade — demand: upgrade existing site from a draaiboek. Seller **Josy**, Kasterlee, since 13 Aug 2026, 249 views. Header **Inloggen**. Contact control **Chat**. No `@` / mailto in the fetched DOM. Price listed as Gratis. | **Login / Chat wall** |
| **2dehands PureAntep / Alva** | https://www.2dehands.be/v/diensten-en-vakmensen/webdesigners-en-hosting/m2418821929-gezocht-wordpress-woocommerce-partner-voor-2-websites — WooCommerce + SEO/CRO/Shopping *partner*, not a 299–900 one-shot. Antwerpen, since 9 Jul 2026. Public page ends at “Meld aan 2dehands”. | **Login / Chat wall** |
| **FreelanceNetwork.be** webdesign | https://www.freelancenetwork.be/nl/freelance-opdrachten/webdesign — “Maak een gratis account”. Open cards in this window were Revit, WINDEV, NT2 teacher, in-person marketeer (Limburg/Kempen), videograaf Brecht 3 Sep, grafisch DM Wilsele. Closed website-build 42134 from an earlier pass was not re-opened as a hit. | **Login wall** |

---

## Open cards this window that are *not* hits

Opened or listed live. Fail the band, the team-delivery bar, or both. **Not next actions.**

### Freelancer.be — websites

| ID | Title | Status / budget | Why not a hit |
|---|---|---|---|
| **12288** | [Website bouwen - Maak democratie toegankelijker](https://freelancer.be/j/website-bouwen-maak-democratie-toegankelijker/12288) | **Open.** €50–350. Leuven 3000. Posted 14 Aug, modified 16 Aug. 0 replies. | Budget sits **below** 299 except the €350 cap. Brief asks for a starter / partial **sponsor**. No mailbox on the card. Apply = register wall. A visual redesign of an existing burgerinspraak site is team-shaped; the published price and the wall are not. Identity of the poster is **not** confirmed from this card. |
| **12359** | [Full-Stack Web3 Engineer – Developer Reputation Platform](https://freelancer.be/j/full-stack-web3-engineer-developer-reputation-platform/12359) | **Open.** > €80 p.u. 8260. Posted 24 Aug. | Ongoing platform work, Web3. Not a small website/ops pack. Hourly, no fixed 299–900 brief. Login wall. |
| **12285** | [Frontend Engineer](https://freelancer.be/j/frontend-engineer/12285) | **Open.** €25–40 p.u. Postcode **GU46**. Posted 10 Aug. | Web3 **trading** frontend. Out of geography and out of “small website/ops”. Login wall. |
| **12284** | [Haalbaarheidstudie Hogeschool](https://freelancer.be/j/haalbaarheidstudie-hogeschool/12284) | **Open.** €25–40 p.u. 2000. Posted 10 Aug. | Cost *estimate* for a mobile-app MVP (auth, profiles, search, locations). Not a website delivery. Login wall. |
| FEL\* Elia / Python-React | e.g. [12355](https://freelancer.be/j/fel260727p5a1-senior-.net-ontwikkelaar-brussel-60-remote-4-maanden/12355), [12307](https://freelancer.be/j/fel260828p5a1-senior-python-react-ontwikkelaar-brussel-60-remote-15-maanden/12307) | **Open.** Budget unknown. 4–15 months, Brussels/Gent hybrid. | Day-rate **seats**, not a scoped RFP in band. |

### Freelancer.be — finance / ops (posted 25 Aug 2026)

| ID | Title | Status / budget | Why not a hit |
|---|---|---|---|
| **12361** | [Hulp bij factuur maken en transport vergunning regelen](https://freelancer.be/j/hulp-bij-factuur-maken-en-transport-vergunning-regelen-/12361) | **Open.** €25–40 p.u. Brugge. 0 replies. Full public text: “Factuur maken via peppol / Bijhouden betaling klanten / Nazicht ivm verzekering dossiers / Nazicht huurcontracten / 4 u werk per week max / Ons bedrijf is te Brugge”. | Peppol *invoicing* is adjacent to team invoice tools, but the rest is weekly human admin + **transport permit** and insurance-file review. No public mailbox. Login wall. No fixed 299–900 price (hourly retainer). |
| **12362** | [Kassasysteem BLC](https://freelancer.be/j/kassasysteem-blc-/12362) | **Open.** Posted band €50–350; body says **about €150**, 4–6 hours, “deze week”. Product name / barcode / price / BTW into **BLC** POS. | **Below band.** Proprietary till login; not a website. Team cannot load a shop’s BLC catalog without that account. Login wall. |
| **12283** | [Opstart van een zelfstandige praktijk](https://freelancer.be/j/opstart-van-een-zelfstandige-praktijk/12283) | **Open.** €50–350. 9910. Posted 7 Aug. | Bank start calculation for a babyspa / vakantieverhuur. Not a website/ops pack. Below band. Login wall. |

### Freelancer.be — paused / closed (would-have-been or never in band)

| ID | Title | Status / budget | Note |
|---|---|---|---|
| **12262** | [website ontwikkelen](https://freelancer.be/j/website-ontwikkelen-/12262) — Fit Drum Fun, 2980 | **Gepauzeerd.** €350–1000. Posted 20 Jul, modified 24 Jul. 1 reply (Patrick). | **Would overlap the band.** Five-page info site + quote form + video, no webshop. Team-shaped. Paused. No mailbox on the card. Login wall. Not a live RFP. |
| **12274** | [Freelance Excel Specialist / Procesautomatisering](https://freelancer.be/j/freelance-excel-specialist-procesautomatisering/12274) | **Gepauzeerd.** €60–80 p.u. 2440. | Ongoing Excel retainer, not one website. Paused. |
| **12257** | [Ontwikkeling van drie websites](https://freelancer.be/j/ontwikkeling-van-drie-websites/12257) | **Gepauzeerd.** €50–350. | Same PureAntep-class three-brand ask. Below band + paused. |
| **11881** | [Notion Expert – Help Center Setup](https://freelancer.be/j/notion-expert-help-center-setup/11881) | **Gesloten.** €25–40 p.u. 9070. | Closed 17 Jun. |
| **11724** | Wordpress site (alternatief therapeut, Siteground) | Listed in search indexes as €50–350, 2870, Feb 2026 | Direct GET in this window hit Cloudflare challenge; not used as Open. Budget below band even if it were live. |

Page 3 of Websites & Applicaties (offset=20) was **all Gesloten** (ecommerce €50–350, Figma rebuild >€2000, Shopware subscriptions >€2000, webshop admin €40–60 p.u., Divi artikeldatabank, bijlesplatform, Teamleader/Power BI 2440, Shopify-ERP). None revived.

---

## 2dehands services — demand vs supply

Category https://www.2dehands.be/l/diensten-en-vakmensen/webdesigners-en-hosting/ — facet **Aangeboden sinds: Vandaag 0 / Gisteren 0 / Een week 3**. Those three this-week cards are **supply** (Mokso Koersel €200, OnYourSite Evergem, Leuven €199 webshop). Contact is platform Chat. Not RFPs.

Query https://www.2dehands.be/q/webdesigner+gezocht/ — **Vandaag 0 / Gisteren 0 / Een week 0**. Only two demand cards: Josy/Kasterlee and PureAntep/Alva (login walls above). Query https://www.2dehands.be/l/diensten-en-vakmensen/webdesigners-en-hosting/q/gezocht/ — PureAntep only.

No 2dehands demand card published a mailbox or a 299–900 USDC (or €) figure.

---

## Local vzw quotes

Searched for public *requests* (offerte-aanvraag / nieuwe website) from Belgian vzw’s / clubs, not directory “vraag een offerte” widgets.

| What was opened | Result |
|---|---|
| Freelancer.be 12294 Dolfijnen Middelkerke vzw | Live vzw website quote. **Skipped — already mailed.** Budget also above 900 USDC. |
| https://www.zgeel.be/ (Zwemclub Geel vzw) | Live **modern** club site (lidgeld 2026–2027, zwemschool inschrijvingen 23 Jun 2026). This is **not** an offerte-aanvraag. `/contact` returned **404**. Not treated as a quote request. Club secretariat mailboxes on a wedstrijd-PDF were **not** copied as a lead. |
| Webhero “Offertes aanvragen / Website laten maken” on Geel vzw directory pages (e.g. DE SPRINTERS, kanoeto) | Lead-gen chrome on a company listing. The vzw did not post an RFP. Ignored. |
| Meer Democratie VZW contact https://www.meerdemocratie.be/en/graag-horen-wij-van-u | Public `welkom@meerdemocratie.be`, Koetsweg 13, 3010 Kessel-Lo. **Not confirmed** as the poster of Freelancer.be 12288 (card says 3000, no org name). Not listed as a hit. Address recorded only to state the inference was **not** used. |

No other local vzw website quote with a public brief in the 299–900 USDC band was found in this window.

---

## PII scan

| Field | In this file | Rule |
|---|---|---|
| Public seller / poster handles already on the ad | Josy, Alva, Patrick (Freelancer.be reply name on paused 12262) | Kept: on the public listing. |
| Cities / postcodes on the listing | Kasterlee, Antwerpen, Brugge, 3000, 2980, 2440, 8260, 8432, 9910, 9070, Geel | Kept. |
| Personal inbox for Josy | **Not present. Not invented.** | Chat wall. |
| Meer Democratie mailbox | Named once, labeled **unconfirmed** for 12288 | Not a hit. |
| ZGEEL secretariat Gmail | **Not copied as a lead** | Club is not requesting a site. |
| Operator personal Gmail / phone | Not used | Team delivers; operator is not the freelancer. |
| Treasury pay address | Not required in this research file | No quote was issued. |

No people-search, no guessed `info@` for unnamed posters.

---

## Source log (URLs actually fetched this window)

| Time (UTC) | URL | Result |
|---|---|---|
| 03:51 | https://freelancer.be/opdrachten/websites-en-applicaties | 200, 10 cards incl. 12294 Open, 12288 Open |
| 03:51 | https://freelancer.be/opdrachten | 200, SAP seats + 12361 + 12362 + Web3 |
| 03:51 | https://freelancer.be/j/website-bouwen-maak-democratie-toegankelijker/12288 | WebFetch: Cloudflare interstitial |
| 03:51 | https://freelancer.be/opdrachten/finance-en-administratie | 200, 12361/12362 Open; older bookkeeping **Gesloten** |
| 03:52 | Playwright same Websites & Applicaties list | Full cards + pagination; **Inloggen** in header |
| 03:52 | Playwright https://freelancer.be/j/website-bouwen-maak-democratie-toegankelijker/12288 | Open, €50–350, full brief, Reageer → `/registreer/freelancer` |
| 03:52 | https://www.2dehands.be/q/webdesigner+gezocht/ | 200, Josy + PureAntep; Een week 0 |
| 03:52 | https://www.2dehands.be/l/diensten-en-vakmensen/webdesigners-en-hosting/q/gezocht/ | 200, PureAntep only |
| 03:52 | Playwright https://freelancer.be/opdrachten/websites-en-applicaties?offset=10 | 12285/12284 Open; 12262 not on this page; 12257 Gepauzeerd |
| 03:53 | Playwright finance list | IDs **12361**, **12362** |
| 03:53 | Playwright https://freelancer.be/j/website-ontwikkelen-/12262 | **Gepauzeerd**, €350–1000, Fit Drum Fun, 2980 |
| 03:53 | Playwright https://freelancer.be/j/hulp-bij-factuur-maken-en-transport-vergunning-regelen-/12361 | Open, full Peppol/admin text, no `@` |
| 03:53 | Playwright https://freelancer.be/j/kassasysteem-blc-/12362 | Open, €150 self-quote, BLC POS |
| 03:53 | https://freelancer.be/opdrachten/websites-en-applicaties?offset=20 | Page 3 all **Gesloten** |
| 03:53 | https://www.2dehands.be/l/diensten-en-vakmensen/webdesigners-en-hosting/ | Supply ads; Een week 3 |
| 03:53 | https://www.zgeel.be/ | 200, live club site, not an RFP |
| 03:53 | https://www.zgeel.be/contact | **404** |
| 03:53 | https://freelancer.be/j/wordpress-site/11724 | Cloudflare challenge |
| 03:53 | https://www.freelance.be/opdracht/1179534-senior-automation-software-engineer | Login to read full brief |
| 03:54 | Playwright 2dehands m2430643166 | **Chat** + **Inloggen**; no mailto |
| 03:54 | https://www.2dehands.be/v/.../m2418821929-... | 200, PureAntep demand, no email |
| 03:54 | Playwright https://www.freelance.be/opdrachten | Account-to-react copy; no public small-website cards |
| 03:54 | https://www.meerdemocratie.be/en/graag-horen-wij-van-u | 200, public mailbox, **unconfirmed** for 12288 |
| 03:51 | https://www.freelancenetwork.be/nl/freelance-opdrachten/webdesign | 200, login to contact |

---

## Honest gap

On 2026-08-26 the only **Open** Belgian *website* quote that named a vzw and a mailbox was **Dolfijnen 12294**, and that one is **already mailed** (and priced above 900 USDC).

The only Open website brief still on Freelancer.be in this window is **12288** (€50–350, sponsor ask, login wall, no email on the card). The only Freelancer.be brief whose published EUR range overlapped 299–900 USDC and that a team could actually ship as a small site (**12262 Fit Drum Fun**, €350–1000) is **Gepauzeerd**.

2dehands still has demand (Josy, PureAntep) behind **Chat**. Freelance.be still hides opdracht text behind **login**. Local Geel club ZGEEL already has a site and did not post a quote request.

**Do not bid, Chat, or register from this PR. Team delivers when a live, in-band, public brief exists.**
