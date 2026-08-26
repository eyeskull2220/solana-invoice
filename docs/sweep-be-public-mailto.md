# BE/NL public-mailto sweep — 2026-08-26

**Research window:** 2026-08-26 00:44–00:50 UTC  
**Question:** are there live Belgian/Dutch “website gezocht” / “klus website” ads whose **contact is a public email**, not a 2dehands/Marktplaats login?  
**Answer:** **No.** This pass found demand-side ads, but **zero** of them printed a mailbox on the public page.

This file is research only. **The team delivers.** The operator is **not** the freelancer and is not applying from this PR. Nothing was emailed, chatted, or bid.

## Constraints used

- Demand only: someone wants a site built or upgraded. Supply ads (“wij maken websites”) are not leads.
- **Public email required.** Chat / “stuur een berichtje” / platform bid / ATS login is a skip.
- **HARD skip:** 2dehands Kasterlee (Josy) and 2dehands PureAntep (Alva). Login/Chat. Do not treat them as mailto leads.
- **Do not invent Josy’s inbox.** First name + city on the listing is not an email. Other public “Josy” mailboxes belong to other people.
- Geography: Belgium first, Dutch-language NL classifieds allowed when they are the same “klus website” shape.
- PII: copy only what the advertiser already published on the fetched page. No people-search, no WHOIS, no guessed local-parts.

---

## Hits with a public email

**None.**

If a later pass finds a listing that prints `mailto:` or a visible `name@domain` in the ad body (not behind login), put it here. Until then this table stays empty on purpose.

---

## HARD skips (do not contact via 2dehands)

### 1. Kasterlee — Josy — website upgrade (login/Chat)

| | |
|---|---|
| **Title** | Freelance Webdesigner :Geef onze website een upgrade! |
| **URL** | https://www.2dehands.be/v/diversen/overige-diversen/m2430643166-freelance-webdesigner-geef-onze-website-een-upgrade |
| **Who (as published)** | Seller display name **Josy**. Profile `/u/josy/42876478/`. Private seller, phone-verified, 5 years on 2dehands, 5.0 from 2 reviews, no other live ads. **Kasterlee.** Posted 13 Aug 2026 21:01. 221 views when opened. |
| **Ask** | Redesign/upgrade of an existing site from a prepared draaiboek. Mobile + conversion. Listed as Gratis / Ophalen. |
| **Public email** | **None.** Expanded description (`Toon minder` state) still ends at “visueel aantrekkelijk ontwerp.” No `@`, no mailto. Contact control is **Chat**. Header **Inloggen**. |
| **Why skipped** | HARD: 2dehands Kasterlee / login. |

**Do not invent Josy’s inbox.** These addresses were **not** used and are **not** this listing:

- `josylaumen@gmail.com` — Josy Laumen, kinesitherapeut, Neeroeteren (https://www.josylaumen.be/) — different person.
- `josy@pechetamarque.be` — Josy, graphiste, pechetamarque.be — different person.

No local-part was guessed (`josy@…`, `info@…` for this seller, etc.).

Fetched: Playwright DOM 2026-08-26 00:48 UTC; description expand 00:49 UTC.

### 2. PureAntep — Alva — WooCommerce partner (login/Chat)

| | |
|---|---|
| **Title** | Gezocht: WordPress/WooCommerce partner voor 2 websites |
| **URL** | https://www.2dehands.be/v/diensten-en-vakmensen/webdesigners-en-hosting/m2418821929-gezocht-wordpress-woocommerce-partner-voor-2-websites |
| **Who (as published)** | Brand **PureAntep** in the body. Seller display name **Alva**. Location on the card: **Antwerpen** (not Kasterlee). Posted 9 Jul 2026; search card still showed 6 Aug 2026. |
| **Ask** | WooCommerce shop + growth partner (SEO, Google Shopping, CRO, email marketing). Long-term, not cheapest-quote. |
| **Public email** | **None** on the listing. Contact is **Chat**. |
| **Own shop** | https://www.pureantep.nl/ fetched 2026-08-26 00:48 UTC: Shopify storefront, newsletter field, **no contact email in the public HTML**. Not used as a backdoor around the 2dehands skip. |
| **Why skipped** | HARD: 2dehands PureAntep / login. |

---

## Other demand ads opened — still no public mailbox

These are real “website gezocht” / small-klus shape. They fail the mailto bar. They are **not** next actions.

| Source | What we actually saw | Why not a mailto hit | Fetched |
|---|---|---|---|
| **2dehands** query `webdesigner gezocht` | Only two demand cards: Josy/Kasterlee and PureAntep/Alva. | Both Chat. | 2026-08-26 00:48 UTC |
| **2dehands** query `wordpress gezocht` | Same PureAntep card only. | Chat. | 2026-08-26 00:47 UTC |
| **2dehands** category Webdesigners + `gezocht` | Same PureAntep card only. | Chat. | 2026-08-26 00:47 UTC |
| **2dehands** query `website gezocht` | Noise (Catawiki, boat buyers). No website-klus demand card. | Not a website klus. | 2026-08-26 00:46 UTC |
| **2dehands** query `klus website` | Hardware/ladder ads, not web work. | Wrong intent. | 2026-08-26 00:49 UTC |
| **2dehands Vacatures** `webdesigner` | Empty: “geen resultaten”. | No listing. | 2026-08-26 00:49 UTC |
| **Marktplaats** `webdesigner gezocht` / `gezocht webdesigner` | Demand card: **Webdesigner gezocht voor Ripsvintage** (Stef, Amsterdam, 4 Jun 2026). Shopify upgrade, 3 shops. Rest of the page is **supply** (Ramon, Bart, bestadsagency, …). | Listing text says contact via Marktplaats. Shop https://ripsvintage.com/ has Instagram + newsletter, **no public contact email** in the fetched pages. | Search 00:47 UTC; shop 00:48 UTC |
| **Marktplaats** `Websitebouwer geozocht` | Indexed listing https://www.marktplaats.nl/v/diensten-en-vakmensen/webdesigners-en-hosting/m2429950963-websitebouwer-geozocht — Almere, kids’ bags, “stuur ons dan een berichtje”, €300, since 11 Aug 2026. | Marktplaats message, no email in the snippet. Direct GET returned **404** on 2026-08-26 00:48 UTC — treat as **not verified live**, not as a mailbox. | Search hit + 404 fetch |
| **Hoofdkraan** 60942 “Gezocht website bouwer met Wordpress” | https://www.hoofdkraan.nl/j/gezocht-website-bouwer-met-wordpress/60942 — WordPress template site, texts/photos from client, SEO. Budget €50–350. **Status: Gepauzeerd** when fetched (search snippet earlier said Open). 15 platform replies. | No email on the public page. Bid on Hoofdkraan. Paused. | 2026-08-26 00:49 UTC |
| **Hoofdkraan** 60930 WordPress beheer/SEO | https://www.hoofdkraan.nl/j/gezocht-freelance-wordpress-specialist-beheer-optimalisat/60930 — €25–40/u, remote. **Gepauzeerd.** | No email. Platform bid. Paused. | 2026-08-26 00:49 UTC |
| **FreelanceNetwork.be** 42134 “Websitebouwer gezocht” | https://www.freelancenetwork.be/nl/freelance-opdracht-detail/42134-websitebouwer-gezocht — SEO site for copywriter + coach. | **“Deze job is reeds afgesloten.”** Contact is “Maak een gratis account / Login”. | 2026-08-26 00:49 UTC |
| **FreelanceNetwork.be** homepage “nieuwste jobs” | Open cards were Revit tekenaar, WINDEV, NT2 teacher, marketeer (Limburg, **sparring over website-opbouw**), videograaf Brecht 3 Sep, grafisch DM Wilsele. | Marketeer card is adjacent, not a build-klus, and contact is the network inbox, not a printed mailto. | 2026-08-26 00:49 UTC |
| **Freelancer.nl** WordPress opdrachten | Index of NL WordPress jobs (kelderbedrijf, Eindhoven on-site vernieuwing, Divi bureau, …). | “Log in om te reageren.” | Search 2026-08-26 00:49 UTC |
| **LinkedIn** Ramon Meulenberg post 2026-03-13 | “Gezocht: Websitebouwer / Webdesigner”. | LinkedIn / DMs. Old. Not a public email. | Search snippet |

Supply ads that **do** print a mailbox (e.g. Marktplaats `info@bestadsagency.com`) are sellers offering to build sites. They are not “website gezocht” clients. Not listed as hits.

---

## PII scan

| Field | In this file | Rule |
|---|---|---|
| Public first names / seller handles already on the ad | Josy, Alva, Stef | Kept: they are on the public listing. |
| Cities already on the ad | Kasterlee, Antwerpen, Amsterdam, Almere | Kept. |
| Personal inbox for Josy | **Not present. Not invented.** | See HARD skip 1. |
| Phone numbers | None copied | Josy’s number is 2dehands-verified, not published on the page we fetched. |
| Extra Josy identities | Named only to **forbid** reuse | Different people; not this lead. |
| PureAntep.nl / ripsvintage.com | URLs only | No mailbox was on those pages. |
| Operator / team identity | Not used as a contact path in this sweep | Team delivers; operator is not the freelancer. |

No people-search, no KvK director harvest, no guessed `voornaam.achternaam@gmail.com`.

---

## Source log (URLs actually fetched)

| Time (UTC) | URL | Result |
|---|---|---|
| 00:46 | https://www.2dehands.be/q/website+gezocht/ | 200, no website-klus demand |
| 00:46 | https://www.2dehands.be/q/webdesigner/ | 200, supply + later demand cards |
| 00:46 | https://www.marktplaats.nl/l/diensten-en-vakmensen/webdesigners-en-hosting/q/webdesigner+gezocht/ | 200, mostly supply |
| 00:47 | https://www.2dehands.be/v/.../m2418821929-... | 200, PureAntep, no email |
| 00:47 | https://www.2dehands.be/l/diensten-en-vakmensen/webdesigners-en-hosting/q/gezocht/ | 200, PureAntep only |
| 00:47 | https://www.marktplaats.nl/q/gezocht+webdesigner/ | 200, Ripsvintage demand + supply |
| 00:47 | https://www.2dehands.be/q/wordpress+gezocht/ | 200, PureAntep only |
| 00:47 | https://www.2dehands.be/v/.../m2430643166-... | 200, Josy/Kasterlee, no email |
| 00:48 | Playwright same Kasterlee URL | Chat + Inloggen; expanded body still no `@` |
| 00:48 | https://www.marktplaats.nl/v/.../m2429950963-websitebouwer-geozocht | **404** |
| 00:48 | https://www.2dehands.be/q/webdesigner+gezocht/ | 200, Josy + PureAntep |
| 00:48 | https://ripsvintage.com/ | 200, no contact email |
| 00:48 | https://www.pureantep.nl/ | 200, no contact email |
| 00:49 | https://www.2dehands.be/l/vacatures/q/webdesigner/ | empty |
| 00:49 | https://www.marktplaats.nl/q/webdesigner+gezocht/ | Ripsvintage still listed |
| 00:49 | https://www.marktplaats.nl/q/websitebouwer+gezocht/ | 200, unrelated “gezocht” goods |
| 00:49 | https://www.freelancenetwork.be/nl/freelance-opdrachten/webdesign | homepage jobs, login to contact |
| 00:49 | https://www.freelancenetwork.be/nl/freelance-opdracht-detail/42134-websitebouwer-gezocht | closed + login |
| 00:49 | https://www.2dehands.be/q/klus+website/ | 200, hardware noise |
| 00:49 | Playwright PureAntep listing | Chat; seller Alva |
| 00:49 | https://www.hoofdkraan.nl/j/gezocht-website-bouwer-met-wordpress/60942 | Gepauzeerd, no email |
| 00:49 | https://www.hoofdkraan.nl/j/gezocht-freelance-wordpress-specialist-beheer-optimalisat/60930 | Gepauzeerd, no email |

Web search (not a page fetch) also surfaced Hoofdkraan/ Freelancer.nl/ LinkedIn indexes; those are in the skip table when the listing URL was then opened or clearly login-gated.

---

## Honest gap

On 2026-08-26 the live Dutch-language classified demand for a small website klus **does exist** (Josy/Kasterlee, PureAntep, Ripsvintage). The contact path is **platform Chat**. That is the product design of 2dehands and Marktplaats; they tell posters not to put email in the ad.

So: **no public-mailto hit, and we did not invent one.** A later sweep can re-open the same queries; if an advertiser pastes a mailbox into the body, that is the first row in the hits table. Until then there is nothing to mail.

**Do not apply from this PR. Do not Chat Josy or PureAntep. Team delivers when a real public email exists.**
