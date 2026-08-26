# Twago Belgium / EU sweep — 2026-08-26

**Startable project briefs the team can deliver: 0**

Research only. Nothing was bid, emailed, or applied. No freelancer profile was created. The user does not code; this pass does not ask them to.

| Field | Value |
|---|---|
| Sweep date | 2026-08-26 (UTC fetch window 00:45–00:51) |
| Target | Twago Belgium / EU — small, startable **project briefs**, not contractor seats |
| Team delivery | One-file HTML tools already in this repo (invoice, CSV cleaner, form-to-email, RSS-to-webhook). No trading. |
| Login / register | **Forbidden.** If a board walls listings or bidding behind login, count is **ZERO**. |
| Pay-to | Authorized, **unused**. No coins bought. Bid-coins on the clone still require an account. |
| PII / secrets | Scanned. Personal emails, phones, bidder names, and chat handles are not in this file. |

---

## Result

**ZERO.** Two independent walls:

1. **Official Twago (the historic Belgium/EU marketplace)** — `https://www.twago.com/` (and `/s/jobs/`) **301 to** `https://www.talent-pool.com/`, then **HTTP 403** (`nginx`) in curl **and** in a headed Playwright session. That is a login / WAF wall. Rule: ZERO.
2. **Public clone `https://twagofreelance.com/`** — job **listings are readable without an account**. Every “Bid on the project” button on a job page goes to `https://twagofreelance.com/freelancer/login`. Taking work requires registering a freelancer profile. Rule: do not register → **not startable**.

No listing on either surface is a Belgium-located, still-open, small HTML-tool brief that the team can start this week without an account.

---

## What Twago is in 2026

Historic **twago.com** (Randstad-owned European freelance marketplace) no longer serves a public project board. The domain now points at Talent Pool, a **corporate white-label talent-pool product**, not a public “post a brief / bid a brief” marketplace. From this environment the successor origin is **403**, so no Talent Pool project list was read.

`twagofreelance.com` is a **separate** Olance-style board that uses the Twago name. It is not Belgium-scoped. Treat it as a clone, not as official Twago BE/EU.

---

## Clone board (public read only)

Fetched `https://twagofreelance.com/freelance-jobs` pages 1–9.

| Metric | Count |
|---|---|
| Listing cards parsed | **144** |
| Sidebar “All” category label | 158 |
| Cards mentioning Belgium / Brussels / Geel / Flanders / Antwerp | **0** |
| Job detail pages fetched (web / automation / invoice-shaped) | 59 (4 of those returned HTTP 500) |
| Detail pages with a future **Deadline** on 2026-08-26 | 8 |
| Those 8 that are **Project Scope: Small** | **1** |
| Those 1 that can be started without a freelancer login | **0** |

Listing “Posted / Ends in …” text is **stale** compared with the job-page `Deadline` field. Several cards still say “Ends in N months” after the deadline has already passed. This sweep uses the job-page **Deadline**, not the listing countdown.

Bid path (GET only, no form submit): `https://twagofreelance.com/freelancer/login` → HTTP 200 login page with password field + register link.

---

## Filters (why the count is zero)

A brief is **startable** only if all of these hold:

- Public text is readable without login (passed for the clone; failed for official Twago).
- **Deadline ≥ 2026-08-26**.
- **Project brief**, not a seat (no “Senior … Engineer”, VA, sales, BDR, long-term enhancement, 1:1 coaching, laptop remote-control).
- Small enough to start this week (scope Small, or a discrete HTML-tool-sized deliverable).
- Something this team can ship (invoice / CSV / form / webhook / one-file HTML), without the user writing code.
- Apply path does **not** require a freelancer profile.

Nothing passed the last two checks together.

---

## Near-misses (not startable — do not bid)

These were **read** because they look adjacent. They are **not** next actions.

| Public title | URL | Deadline | Why not startable |
|---|---|---|---|
| Senior Software Engineer with experience in AI and Web development. | https://twagofreelance.com/explore-job/invoice-generation | 31 Aug 2026 | Only small-scope job still open. Body is “fix an existing AI invoice web app” ($500, remote). **Bid CTA → freelancer login.** Title is a contractor seat. Needs their codebase, not a one-file tool from this repo. Not Belgium. |
| Website Developer Needed to Build or Improve Business Website | https://twagofreelance.com/explore-job/website-developer-needed-build-improve-business-website | 04 Jul 2026 | **Expired.** Medium, 1–3 months, WordPress/Shopify/Webflow. Login to bid. |
| Logo, Brand, and Web Design for Non-Profit | https://twagofreelance.com/explore-job/creative-design | 18 Sep 2026 | Still open, but **brand/logo seat**, not an HTML-tool brief. Login to bid. |
| N8n automatisierung | https://twagofreelance.com/explore-job/n8n-automatisierung | 11 Feb 2026 | **Expired.** DACH-language, but it is live 1:1 setup / remote laptop control at an hourly rate — a coaching **seat**, not a shipped brief. Login to bid. |
| Automation Specialist Needed: n8n + Google Sheets → Telegram/whatsapp Alert System | https://twagofreelance.com/explore-job/n8n-google-sheets-telegram-deal-alert-automation | 07 Feb 2026 | **Expired.** Medium automation build. Login to bid. |
| Go Entwickler für den Export von Messdaten in Excel & PDF | https://twagofreelance.com/explore-job/go-developer-for-export-of-data-in-excel-and-pdf | 28 Feb 2026 | **Expired.** Small, German-language, Go/Excelize — not this team’s one-file HTML stack. Login to bid. Page contained a personal mailbox; **not copied here**. |
| LuxuryTaste — Improve Restaurant Discovery Near Customers | https://twagofreelance.com/explore-job/ecommerces | 20 Aug 2026 | **Expired** (deadline before sweep day). Next.js/Nest/Postgres feature work on an existing app. Login to bid. |
| Software Engineer Full-Stack Freelance - Remoto (España) | https://twagofreelance.com/explore-job/software-engineer-full-stack-freelance---remoto-espaa | 02 Dec 2027 | Open date, but **Large** scope / contractor seat. Login to bid. |

EU-flavored cards that are seats or off-stack (sales, video, VA, on-site visits, translation) were not treated as project briefs.

---

## PII scan

Ran after the fetch, before this file was written.

| Check | Result |
|---|---|
| Personal emails | One expired German job page had a personal mailbox. **Omitted.** Platform support address not copied. |
| Phones | None copied. |
| Bidder / buyer display names | Present on clone job pages. **Omitted.** |
| Telegram / chat handles | Present on several listing cards (likely unsolicited). **Omitted.** |
| Secrets / API keys / private keys | None found. Pay-to addresses were not written into this file. |
| Freelancer account | **Not created.** Login page was GET-only. |

---

## Source log (URLs actually fetched)

| Time (UTC) | URL | Result |
|---|---|---|
| 00:45 | https://www.twago.com/ and https://twago.com/ | 301 → https://www.talent-pool.com |
| 00:45 | https://www.twago.be/ | 404 |
| 00:45 | https://www.twago.de/ | 404 |
| 00:45 | https://twago.de/ | 301 → talent-pool.com |
| 00:45–00:46 | https://www.talent-pool.com/ and `/projects` | **403** nginx (curl) |
| 00:47 | https://www.talent-pool.com/ (Playwright) | **403 Forbidden** |
| 00:48 | https://twago.com/ (Playwright) | landed on talent-pool.com **403** |
| 00:51 | https://www.twago.com/s/jobs/ | 301 then **403** |
| 00:45 | https://twagofreelance.com/robots.txt | 200; sitemap `sitemap-index.xml` |
| 00:45 | https://twagofreelance.com/sitemap-jobs.xml | 200; 142 job URLs |
| 00:46 | https://twagofreelance.com/freelance-jobs | 200; public list |
| 00:47 | https://twagofreelance.com/freelance-jobs?page=2 … 9 | 200; page 9 = 0 cards |
| 00:48–00:50 | 59 `https://twagofreelance.com/explore-job/…` detail URLs | 54×200, 4×500, 1 skipped |
| 00:51 | https://twagofreelance.com/freelancer/login | 200 login form; **no submit** |

Query-string filters on `/freelance-jobs` (`?q=`, `?scope=`) did not change the first page; filtering was done on parsed cards + detail fields.

---

## Honest gap

Official Twago was **not emptied**. It was **blocked**. A later pass from a residential / Belgian IP still cannot create a freelancer profile under the current rule, and Talent Pool is not a public brief board from this vantage.

The clone’s invoice-fix card is the only small, still-open, tool-adjacent text. It is still **not startable**: bidding is login-walled, the title is a seat, and the work is “repair their app,” not ship a one-file HTML tool.

**This document is research only. Do not apply from this PR. Do not register.**
