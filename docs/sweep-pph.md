# PeoplePerHour sweep — 2026-08-26

**Research window:** 2026-08-26 00:45–00:48 UTC  
**Result: 0** jobs the TEAM can take without a PeoplePerHour (PPH) freelancer account.

Nothing was bid, emailed, or applied. **No PPH profile was created.** The logged-out job pages all use **Create an account now and send a proposal** (or an expired/ended state). That is bid-as-freelancer only, so the takeable count is **ZERO**.

The user does not code. This pass does not ask them to sign up or send a proposal.

---

## What counts as takeable

A listing is takeable only if **all** of these are true:

| Filter | Rule |
|---|---|
| Scope | Small **HTML**, **CSV** / spreadsheet, or **invoice** work a team can deliver as a one-file or short HTML/CSV job |
| Contact | A **public hiring contact** on the listing itself (mailto, contact form, or business mailbox published as how to apply) |
| Path | The TEAM can reach that contact **without** creating a PPH profile as the user |
| PII | No personal emails, phones, or private addresses copied into this file |

A website URL posted so a freelancer can **see a bug** is a work sample, not a hiring contact. Harvesting `info@` from that site is out of scope (PII scan + PPH off-platform rule).

PPH support: [communication must stay on the platform](https://support.peopleperhour.com/hc/en-us/articles/17825988320785-Can-I-take-communication-off-the-site). WorkStream policy forbids exchanging contact details before a proposal is accepted.

---

## Takeable (0)

None.

No live HTML / CSV / invoice listing in this window published a public apply mailbox or form. Every open match required **Sign up** to send a proposal.

---

## Closest live matches (bid-gated — not takeable)

These are the nearest open jobs. They are listed so the sweep is not an empty search. **Do not bid. Do not sign up.**

| Job | Price (as shown) | Why it is close | Why it is ZERO |
|---|---|---|---|
| [Need my header making more responsive](https://www.peopleperhour.com/freelance-jobs/technology-programming/website-development/need-my-header-making-more-responsive-4517558) `#4517558` | £20 / ~$27, entry, remote | Small HTML/CSS: overlapping mobile header icons | **Create an account now and send a proposal.** The URL in the brief is the site to inspect, not an apply address. 45 proposals. Posted ~20 hours ago. Open, ends in 29 days. |
| [Create excel tabel](https://www.peopleperhour.com/freelance-jobs/technology-programming/databases/create-excel-tabel-4517471) `#4517471` | ~$20, entry, remote | Small spreadsheet (conditional-format tracker). CSV-adjacent | Same signup wall. No email or form on the public page. ~20 proposals. Posted ~1 day ago. Open. |
| [I need the exact column headers of Shopify Stocky's CSV exports](https://www.peopleperhour.com/freelance-jobs/technology-programming/programming-coding/i-need-the-exact-column-headers-of-shopify-stocky-s-csv-expo-4514588) `#4514588` | $20 | Tiny CSV-header question | Listed on [Programming & Coding](https://www.peopleperhour.com/freelance-jobs/technology-programming/programming-coding) (17 days ago, 18 proposals). Public path is still a PPH proposal. No hiring mailbox on the category card. |

Hourlies (freelancer packages such as “fix mobile responsiveness”) are **seller listings**. Posting or fulfilling them also needs a PPH freelancer profile. Not used.

---

## Checked and excluded

| Listing | What we saw | Why excluded | Fetched |
|---|---|---|---|
| `GET /freelance-jobs?q=invoice` `?q=csv` `?q=html` `?q=html+csv+invoice` | HTTP 200, title “Freelance Jobs … Aug 2026”, “300+ results”, **same latest 20 cards** (admin assistant, kit-builder site, video editing, …) | Query string does **not** filter. Not treated as an invoice/CSV/HTML result set. | curl + browser 00:45 UTC |
| [Programming & Coding](https://www.peopleperhour.com/freelance-jobs/technology-programming/programming-coding) | 29 results. Solidworks macro, long-term SaaS, $5.7k SVG-in-HTML illustration, HTML5 arcade game, Airtable/Anthropic script, Xero–Shopify connect | Too large, wrong stack, or bid-only. None published a public apply email. | 00:46 UTC |
| [Website Development](https://www.peopleperhour.com/freelance-jobs/technology-programming/website-development) | Full-stack kit builder, salon booking setup, Senior Front-End (Next.js), WordPress rebuilds, BuddyBoss hub, world-map WP, Stripe/Airtable app | Not small HTML/CSV/invoice, or the header job above (bid-gated). | 00:46 UTC |
| [Databases](https://www.peopleperhour.com/freelance-jobs/technology-programming/databases) | 8 results including the Excel table job; Airtable charity DB; Supabase review | Excel table is bid-only. Others are not small CSV/invoice HTML. | 00:46 UTC |
| [Finance & Accounting](https://www.peopleperhour.com/freelance-jobs/business/finance-accounting) | 12 results: EIS, UK accountant, CT600, PayPal certificate, actuarial Excel model | Accounting/compliance, not HTML/CSV micro-gigs. Bid-only. | 00:46 UTC |
| [Technology & Programming](https://www.peopleperhour.com/freelance-jobs/technology-programming) | 163 results; mixed | Same bid wall. No public apply mailboxes in the first page of cards. | 00:45 UTC |
| [Invoice extraction `#4510782`](https://www.peopleperhour.com/freelance-jobs/artificial-intelligence/artificial-intelligence-data-services/invoice-extraction-4510782) | HTTP 200, **Ended / Expired**, signup CTA still in the shell | Dead. Python/Excel extract of ~300 invoices; not a small HTML tool. | curl 00:47 UTC |
| [Excel & Automation Specialist / invoices `#4488878`](https://www.peopleperhour.com/freelance-jobs/technology-programming/databases/excel-automation-specialist-needed-fix-data-tool-4488878) | **Ended.** WordPress **CSV** export → invoice PDF + email. Clarification board dated 16–17 Apr 2026. CTA: create account and send a proposal | Expired, 3–4 weeks, bid-only. Company name is on the public PPH card; this sweep does not copy harvested mailboxes. | 00:46–00:47 UTC |
| [Invoice template for Enerpize (HTML)](https://www.peopleperhour.com/freelance-jobs/design/web-design/invoice-template-for-use-on-enerpize-similar-to-xero-html-4463976) | Indexed copy dated 19 Jan 2026 | Too old to treat as live. Not re-opened this window. | search snippet |
| CSV→PDF invoice script `#1743368`, DomPDF HTML templates `#1496512`, WooCommerce HTML invoice `#724397` | Search hits | Historical (2015–2018). Not live. | search |
| Past Databases card: Excel sheet count objects | Marked **Past Projects** on the Databases page | Closed. | 00:46 UTC |

---

## Hard constraints (this run)

| Constraint | What happened |
|---|---|
| Do **not** create a PPH profile as the user | Only logged-out GET/browse. Sign-up was not submitted. |
| User does not code | No “you should bid” instruction. TEAM would deliver if a public contact existed. |
| If bid-as-freelancer only → **ZERO** | Applied. |
| PII scan | No personal emails, phones, or home addresses in this file. Buyer first-name + initial as PPH prints them is omitted; jobs are identified by title and numeric id. Company work-sample hostnames that were **already in a job brief** are not copied here (they are on the PPH URL). |
| No secrets | No API keys, passwords, or session tokens. |

---

## Source log (URLs actually opened)

| Time (UTC) | URL | Result |
|---|---|---|
| 00:45 | https://www.peopleperhour.com/freelance-jobs?q=html+csv+invoice | 200, unfiltered latest jobs |
| 00:45 | https://www.peopleperhour.com/freelance-jobs?q=invoice | 200, unfiltered; UI “300+ results” |
| 00:45 | https://www.peopleperhour.com/freelance-jobs?q=csv | 200, same card set |
| 00:45 | https://www.peopleperhour.com/freelance-jobs?q=html | 200, same card set; 0 emails in DOM |
| 00:45 | https://www.peopleperhour.com/freelance-jobs/technology-programming | 200, 163 results |
| 00:46 | https://www.peopleperhour.com/freelance-jobs/technology-programming/programming-coding | 200, 29 results |
| 00:46 | https://www.peopleperhour.com/freelance-jobs/technology-programming/website-development | 200 |
| 00:46 | https://www.peopleperhour.com/freelance-jobs/technology-programming/databases | 200, 8 results |
| 00:46 | https://www.peopleperhour.com/freelance-jobs/business/finance-accounting | 200, 12 results |
| 00:46 | https://www.peopleperhour.com/freelance-jobs/technology-programming/website-development/need-my-header-making-more-responsive-4517558 | Open; **Create an account now and send a proposal**; 0 emails in page text |
| 00:46 | https://www.peopleperhour.com/freelance-jobs/technology-programming/databases/excel-automation-specialist-needed-fix-data-tool-4488878 | Ended; signup CTA |
| 00:47 | https://www.peopleperhour.com/freelance-jobs/technology-programming/databases/create-excel-tabel-4517471 | Open; **Create an account now and send a proposal**; 0 emails |
| 00:47 | https://www.peopleperhour.com/freelance-jobs/artificial-intelligence/artificial-intelligence-data-services/invoice-extraction-4510782 | Ended / Expired |
| 00:47 | https://support.peopleperhour.com/hc/en-us/articles/17825988320785-Can-I-take-communication-off-the-site | Off-platform contact is not allowed |
| 00:47 | https://support.peopleperhour.com/hc/en-us/articles/205218197-WorkStream-Policies | Contact details before accept = policy breach |

`GET https://www.peopleperhour.com/signup` timed out in this environment. That is fine: sign-up was not required and was not completed.

---

## Honest gap

PPH is a **login-to-bid** board. Logged-out, there is no public apply path for the small HTML/CSV/invoice jobs that were actually open today.

A later pass that creates a freelancer profile would still be **the user’s** account and is **out of scope** for this file.

**This document is research only. Do not apply from this PR.**
