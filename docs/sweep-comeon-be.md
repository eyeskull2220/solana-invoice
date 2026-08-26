# ComeOn.be / Belgian small-job sweep

**Sweep date:** 2026-08-26 (UTC window 00:43–00:50)  
**This week:** Mon 2026-08-24 through Sun 2026-08-30 (ISO week 35; today is Wednesday)  
**Ship shape:** landing page, CSV, invoice, form — one-file HTML / agent-team delivery  
**Pay-to (OK to quote on a real deliverable):**  
- Solana: `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3`  
- EVM: `0x9eb954b567ef3616424a6e1bf42c63724930aa54`

## Verdict

**ZERO shippable coding REQUESTS this week.**  
**Pitches drafted: 0. Pitches sent: 0.**

No public `mailto:` plus an in-scope request. No no-login intake form for a landing page / CSV / invoice / form job. Nothing was emailed, posted, or submitted.

## Hard rules used

| Rule | How it was applied |
|---|---|
| User does not code | Do not apply them as a human freelancer. Do not create Ring Twice / 2dehands / Malt / Konnekt / Jobat accounts in their name. |
| Agent-team only | Keep only work we can ship this week as HTML tools (landing page, CSV, invoice, form). |
| Requests, not supply | Skip web-designer *offer* ads (“website laten maken €199”). Those are sellers, not buyers. |
| Skip Konnekt / Jobat / Malt seats | Not opened as apply paths. (Jobat/Malt were also Cloudflare-blocked on a sibling BE jobs pass.) |
| Public mailto + we can deliver → draft pitch, do not send unless no-login form | Never met. Else ZERO. |
| PII scan | Personal phones, private emails, and HN job-seeker inboxes are not copied here. |
| No secrets | No API keys, tokens, or private credentials. Pay-to addresses above were supplied for this sweep. |

---

## ComeOn.be

| | |
|---|---|
| **Fetched** | `https://comeon.be` → `https://comeon.be/en-us` (Playwright + curl, 2026-08-26 00:46 UTC) |
| **What it is** | Parked domain. Title: “comeon.be is for sale”. Served by Nameshift (`x-nameshift-region: lax`). Not a Belgian job board. |
| **Seller (public, company)** | NVA Online Advertising B.V. (Nameshift.com footer: Steenplaetsstraat 6, 2288AA Rijswijk, Nederland). |
| **Public mailto** | None (`mailto:` count = 0, `tel:` count = 0). |
| **No-login form** | Nameshift “Make an offer” / buy-or-rent fieldset (`price`, `currency`, `buy-method`). That buys the **domain**, it is not a coding request. |
| **This-week coding request?** | No. |

Do not pitch Nameshift. Do not treat domain escrow as an invoice/form gig.

`www.comeon.be` 301s to `https://comeon.be/`. Same parked page.

---

## Boards actually opened

### 1. Ring Twice (ex-ListMinut) — Belgian small-job marketplace

| URL | Result |
|---|---|
| https://ringtwice.be/fr | 200 in browser. Public homepage is **prestataire (supply) directories** + “Demander un service”. Popular IT copy is on-site PC help / Excel *lessons*, not a dated client brief. |
| https://ringtwice.be/fr/creation-site-web/bruxelles | 200. **504 créateurs site web** (supplier list). First-name profiles, hourly rates, reviews. No public list of this-week *demandes*. |
| https://ringtwice.be/fr/jobs | Redirects to **login**: `https://ringtwice.be/users/sign_in?locale=fr&redirect=jobs` |
| https://www.listminut.be/ | Same Ring Twice product. |

Client requests exist behind “devenir prestataire” / app login. Opening that would mean applying the non-coding user as a human jobber. **Skipped.** No public mailto on the listing pages we fetched.

### 2. 2dehands.be — classifieds (NL)

Category https://www.2dehands.be/l/diensten-en-vakmensen/webdesigners-en-hosting/?offeredSince=EenWeek — 200.

Facet **Offert depuis / Aangeboden sinds** on the FR twin (same inventory): **Aujourd’hui 0 / Hier 0 / Une semaine 3**. Organic *new* ads this week in that category are a handful of **supply** “website laten maken” cards (Mokso €200 Koersel, OnYourSite Evergem, Leuven €199 webshop, Orp-Le-Grand IA-app offer, Design Office €249 one-pager). Contact is **2dehands login chat**, not mailto.

Search https://www.2dehands.be/l/diensten-en-vakmensen/q/excel/ — **19 results**, facet **Vandaag 0 / Gisteren 0**. Hits are drain-machine “moet op factuur” (equipment sale) and **Excel bijles** (tutor supply). Not a CSV/invoice build request.

Search https://www.2dehands.be/q/website+gezocht/ — **Vandaag 0 / Gisteren 0 / Een week 0**. Top cards were Catawiki / boat-buying ads; query is useless for coding requests this week.

No **Gevraagd** (wanted) coding ads found in this window.

### 3. 2ememain.be — classifieds (FR, same Marktplaats family)

| URL | Result |
|---|---|
| https://www.2ememain.be/l/services-et-artisans/ | **404** “Problème inconnu” |
| https://www.2ememain.be/l/services-professionnels/web-designers-hosting-hebergement/ | 200, **19 résultats**, same supply ads as 2dehands. **mailto: none** on the list page. |

Older supply ads (e.g. 13–15 Aug, before this week) are also sellers. Not scored as this-week requests.

### 4. dropitask.be — Belgian digital micro-jobs

Homepage (WebFetch earlier in the window): four categories, **0 annonce** each (Communication, E-commerce, Admin/automation, Support Web). Playwright later hit **Cloudflare 403** “Just a moment…”. Empty board, then blocked. No requests to pitch.

### 5. Pwiic (nl-be)

https://pwiic.com/nl-be and `/nl-be/s/informatique` (WebFetch). Public cards in this window were **physical / care** (paint a hallway, jungle-gym sand, IKEA wardrobe, petsitting). Matching is login + in-app “Pwiic” message. Example prompt “Me helpen met al computerdingen” is marketing copy, not a dated request. **No public mailto. No this-week coding request.**

### 6. Yoojo.be

https://www.yoojo.be/ — home services (babysitting, IKEA, painting). Recent reviews in this window: dishwasher install, TV wall-mount, IKEA carry. **Not coding. Login/app to take jobs. Skipped as human jobber path.**

### 7. Freelance.be

https://www.freelance.be/opdrachten — ICT filters exist; full opdracht text is **login**. This is a professional-seat board, not a small-job REQUEST feed. Out of the “landing page / CSV / invoice / form this week” bar even if a TS contract were visible. Not used as an apply path.

### 8. HN August 2026 freelancer thread

https://news.ycombinator.com/item?id=49157021  
Algolia `tags=comment,story_49157021` query `"SEEKING FREELANCER"` → **0 hits**. Thread is SEEKING WORK only. Not a Belgian small-job board; recorded so we do not invent a hire post.

### 9. Vivastreet.be

https://www.vivastreet.be/search/be/informatique — search is polluted (voyance, real estate, scaffolding). One household-help *request* was off-scope (not coding). Personal phone numbers on that page were **not copied**.

### Intentionally not used as apply seats

Konnekt, Jobat.be, Malt, ICTJob, VDAB FTE/freelance seats, LinkedIn. User does not code; those are human-freelancer funnels.

---

## Candidate table (must be empty if honest)

| # | Request (this week) | Board | Public mailto or no-login form | Agent-shippable? | Pitch |
|---|---|---|---|---|---|
| — | *none* | — | — | — | **ZERO** |

If a listing had appeared with a public mailbox and a landing-page / CSV / invoice / form brief, a **draft** pitch would live below (NL/FR, agent team, pay-to addresses, no fake CV). That section is unused.

### Unused pitch stub (do not send)

Not filled. No target.

---

## PII scan

| Source | What appeared | Action |
|---|---|---|
| ComeOn.be / Nameshift | Company seller **NVA Online Advertising B.V.** + Dutch KvK/BTW in the page footer | Kept: public company on a sales page. No personal mailbox. |
| 2dehands / 2ememain | Personal first names on **supply** ads | Omitted. Trade names + city + price kept as supply-skip evidence. No phones, no private email. |
| Ring Twice | First names + hourly rates of prestataires | Not copied as leads. Supplier directory, login-walled requests. |
| Vivastreet | Personal mobile numbers on unrelated ads | **Redacted. Not stored in this file.** |
| HN freelancer thread | Job-seeker emails on SEEKING WORK comments | **Not copied.** Wrong direction (they want work). |
| dropitask / Ring Twice login | Username/password fields | Not filled. No credentials. |
| This repo README | `ADDRESS_PENDING` on live tools | Unchanged. Sweep pay-to is documented **here only**. |

**Secrets:** none added. No `.env`, no tokens.

---

## Source log (URLs actually fetched)

| Time (UTC) | URL | Result |
|---|---|---|
| 00:46 | `https://comeon.be` / `https://www.comeon.be` | 307/301 → Nameshift parked sale page |
| 00:46 | Playwright `https://comeon.be/en-us` | “comeon.be is for sale”; offer form; no mailto |
| 00:46 | curl `https://ringtwice.be/fr` | **403 Cloudflare** |
| 00:46 | Playwright `https://ringtwice.be/fr` | 200 homepage (supply + CTA) |
| 00:46 | `https://www.2dehands.be/l/diensten-en-vakmensen/webdesigners-en-hosting/` (+ `offeredSince=EenWeek`) | 200, supply ads |
| 00:46 | `https://www.2dehands.be/q/website+gezocht/` | 200, 0 this-week hits; junk categories |
| 00:46 | `https://pwiic.com/nl-be/s/informatique` | 200, physical/care cards |
| 00:47 | `https://www.2dehands.be/l/diensten-en-vakmensen/q/excel/` | 19 results; Vandaag 0; bijles / hardware |
| 00:47 | `https://ringtwice.be/fr/creation-site-web/bruxelles` | 200, 504 suppliers |
| 00:47 | `https://dropitask.be/` | Playwright **403** challenge (WebFetch earlier: 0 listings) |
| 00:47 | HN item `49157021` + Algolia | 0 SEEKING FREELANCER |
| 00:48 | `https://ringtwice.be/fr/jobs` | redirect **sign_in** |
| 00:48 | `https://www.2ememain.be/l/services-et-artisans/` | **404** |
| 00:48 | `https://pwiic.com/nl-be/s/webontwikkelaar` | redirect homepage |
| 00:48 | `https://www.yoojo.be/` | home services, not coding |
| 00:48 | `https://www.freelance.be/opdrachten` | login for full text |
| 00:49 | `https://www.2ememain.be/l/services-professionnels/web-designers-hosting-hebergement/` | 200, 19 supply ads, 0 mailto |
| 00:49 | `https://www.vivastreet.be/search/be/informatique` | polluted SERP; phones redacted |
| 00:49 | ComeOn.be form probe | GET offer form; mailto 0 |

---

## Honest gap

Belgian small-job **demand** for computer work is concentrated on Ring Twice / ListMinut **after login**, and on 2dehands it shows up as **sellers shouting prices**, not buyers posting briefs. This week’s public HTML does not contain a landing-page, CSV, invoice, or form **request** with a public mailbox or a no-login form.

Re-fetch Ring Twice jobs only with an **agent-owned** prestataire seat if product later allows that — never by signing the human user up as a coder.

**This document is research. Do not apply. Do not send mail.**
