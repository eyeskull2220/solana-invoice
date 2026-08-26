# HN / Indie Hackers sweep (read-only)

Sweep date: **2026-08-26** (Wednesday). Window: calendar week **Mon 2026-08-24 00:00 UTC → Wed 2026-08-26 ~00:50 UTC**. Last-7-day hits (Wed 2026-08-19 onward) are listed separately so they are not mixed into “this week.”

**Hard constraints honored**

- Box has **no Hacker News session** and **no Indie Hackers session**.
- **Nothing was posted.** No Show HN. No IH comment. No reply.
- Public pages and APIs only (HN Algolia + Firebase item JSON; IH newest feed in a logged-out browser).
- **If a public email exists on a matching ask, draft a pitch. Else ZERO.**

**Pitches this sweep: ZERO.**

Catalog this research is for (not posted anywhere):

- Hub: https://treasury-tools.surge.sh/
- Solana Invoice: https://solana-invoice-treasury.surge.sh/
- CSV Cleaner: https://csv-cleaner-treasury.surge.sh/
- Form to Email: https://form-to-email-treasury.surge.sh/

---

## Verdict

One Indie Hackers post this week asked what freelancers use to make invoices. The author already ships a competing invoice generator. The post, the profile, and the product page expose **no public email**. Hacker News this week has **no Ask HN / comment** asking for an invoice, CSV, or form tool — only launches and off-topic mentions.

No public email → **no draft**. Do not log in later to answer the IH thread from this box.

---

## Matching ask this week

### 1. IH — “Freelancers: What Do You Use to Create Invoices?”

| Field | Value |
| --- | --- |
| URL | https://www.indiehackers.com/post/freelancers-what-do-you-use-to-create-invoices-42a12ec071 |
| Author | [Jan_andy](https://www.indiehackers.com/Jan_andy) |
| Posted | 2026-08-25 (~10 hours before this sweep) |
| Thread | 1 like, **0 comments** |
| Public email | **None.** Post body: none. Profile: none (`mailto:` none). Product page: none. |
| Pitch | **ZERO** |

Quoted body (public, logged-out):

> Freelancers: what do you use to create invoices? I’m curious what everyone uses — Excel, Google Docs, Canva, Invoice Ninja, etc. What’s the most annoying part of your current workflow?

This is a research question, not “please send me a tool.” The same account lists **Invoice Blade** (“simple invoicing tool built for freelancers… Free to use”) with demo https://invoiceblade1.pages.dev/ (local dashboard, PDF download, no contact email in the page source we loaded). Pitching Solana Invoice into that thread would be a logged-in product comment on a competitor’s validation post. Out of scope, and there is still no email to draft to.

---

## HN this week — no demand posts

Algolia `search_by_date`, `typoTolerance=false`, `created_at_i` in `[1787529600, 1787788800)`.

### Stories that hit invoice / CSV / form keywords (all launches, not asks)

| When (UTC) | ID | Author | Title | Notes |
| --- | --- | --- | --- | --- |
| 2026-08-25 12:10 | [49432565](https://news.ycombinator.com/item?id=49432565) | alexgoldwyn | Show HN: What one invoice actually costs across 33 invoicing plans | Launch. 1 point. **0 comments.** https://billinghub.online/invoice-cost-calculator |
| 2026-08-24 18:48 | [49424212](https://news.ycombinator.com/item?id=49424212) | jitukedir | InvoiceFlow AI – Smarter invoicing for freelancers and businesses | Launch. 1 point. 0 comments. https://invoiceflowdesign.app |
| 2026-08-25 03:32 | [49428785](https://news.ycombinator.com/item?id=49428785) | Sharanxxxx | Show HN: JSON Support – Free JSON and CSV to Excel Conversion Without Signups | Launch. Adjacent to CSV cleaning, not an ask. https://www.jsonsupport.com/ |
| 2026-08-25 12:01 | [49432437](https://news.ycombinator.com/item?id=49432437) | arafat-92 | Show HN: FormForge – offline form filler for QA | Chrome QA autofill. Not form-to-email. |

Exact-phrase story searches this week for `"form builder"`, `"contact form"`, `mailto`: **0 hits**.

### Ask HN this week

58 Ask/Tell posts in the window (paginated). None asked for an invoice generator, CSV cleaner, or form-to-email builder. Closest misses:

- [Ask HN: Those making $500/month on side projects](https://news.ycombinator.com/item?id=49417766) — show-and-tell, not a tool request.
- [How Much to Charge-Freelance…](https://news.ycombinator.com/item?id=49427649) — rates, not invoicing software.
- [Ask HN: Good large format touchscreen E-Paper](https://news.ycombinator.com/item?id=49428842) — hardware.

### Comments this week (keyword hits, not asks)

| ID | Author | Thread | Why it is not an ask |
| --- | --- | --- | --- |
| [49436025](https://news.ycombinator.com/item?id=49436025) | gabrielsroka | [Show HN: Dev tools in one static site](https://news.ycombinator.com/item?id=49423029) | Bug note: CSV can contain `\n`. Not looking for a cleaner. |
| [49428223](https://news.ycombinator.com/item?id=49428223) | AyyEye | [IPFS Maintainers Winding Down](https://news.ycombinator.com/item?id=49421489) | Prefers `mailto:` over Google Forms for Shipyard feedback. Not asking for a form builder. The address in the comment is **shipyard’s**, not the commenter’s. |
| Several | various | [How Europe is killing makers](https://news.ycombinator.com/item?id=49419237) | VAT / packaging “invoices” as paperwork. Not a product request. |
| [49430517](https://news.ycombinator.com/item?id=49430517) | littlecranky67 | Nostr | Lightning **hold invoices**. Wrong domain. |

HN user `/user?id=` about-pages were **rate-limited (HTTP 429)** when batched. That does not change the pitch count: there was no demand-side HN author to email.

---

## IH this week — rest of newest

Logged-out newest feed, pages 1–13, until timestamps roll to **2026-08-23** (so Monday 24th is fully covered).

**No other post** asked for an invoice tool, a CSV cleaner, or a form-to-email / contact-form builder.

Nearby titles that are **not** asks:

| When | Title | Why skipped |
| --- | --- | --- |
| ~18h before sweep | “The too complex for spreadsheets, too small for SAP gap…” | Logistics software positioning, not a CSV-cleaner request. |
| 2026-08-25 00:14 | Inc. 5000 dataset **(CSV/PDF/EPUB)** | Selling a data dump. |
| 2026-08-24 20:10 | “What would you automate first in a local service business?” | Generic validation. Title does not ask for invoice/CSV/form tools. |
| 2026-08-24 03:15 | “I built a $39 AI contract reviewer so freelancers stop signing bad client contracts” | Launch, contracts not invoices. |
| Pages 2 / 7 / 8 | Sage 50 / QuickBooks “error code” posts | Support spam, not tool requests. |

IH Top This Week had no invoice / CSV / form-builder threads.

---

## Last 7 days (outside this calendar week — not pitched)

Included so a later sweep does not rediscover them as “new.” Still **no public emails collected; still ZERO drafts.**

| When (UTC) | Where | What |
| --- | --- | --- |
| 2026-08-20 22:01 | HN [49380837](https://news.ycombinator.com/item?id=49380837) guerrerocarlos | “Super-simple free tool to create invoices” — **launch** (brother’s pain). https://www.invoices-templates.com/ |
| 2026-08-19 19:13 | HN [49365926](https://news.ycombinator.com/item?id=49365926) wowinter15 | Show HN: Invoicing and Tax for UK Tradespeople — **launch**. |
| 2026-08-21 18:53 | HN [49392389](https://news.ycombinator.com/item?id=49392389) v512 | Show HN: CSVtoTable — CSV/XLSX → one HTML file — **launch**. |
| 2026-08-20 20:09 | HN [49379569](https://news.ycombinator.com/item?id=49379569) cakbeslik | Show HN: Emd — CSV/XLS EDA CLI — **launch**. |
| 2026-08-20 | HN comment [49376164](https://news.ycombinator.com/item?id=49376164) SyneRyder | Harvest usage pricing complaint. Adjacent to invoicing SaaS, not a request for a one-file invoice page. |

Older IH invoice/CSV/form posts that web search still surfaces (ParseMyInvoice, img2sheet, FORMLOVA, InvoiceGenie, etc.) are **months old**. Not this week.

---

## What was not done (on purpose)

- No HN account, no IH account, no Show HN, no thread replies.
- No Gmail send. No invented contact addresses.
- No draft sitting in this file for Jan_andy — the rule is email-or-zero, and the email is absent.
- No email was sent and nobody was asked to send funds. A later pitch (only if a public email appears) can link the catalog; it should not paste a wallet into a forum comment.

---

## How to repeat next sweep

1. HN: `https://hn.algolia.com/api/v1/search_by_date` with `typoTolerance=false` (otherwise `invoice` matches `invoke` / `voice`). Filter `created_at_i` to the new week. Search stories **and** comments; also paginate `tags=ask_hn`.
2. IH: logged-out https://www.indiehackers.com/newest until dates leave the week. Curl HTML is a JS shell — use a real browser or a reader that executes the feed.
3. Only draft if the **asker** published an email on the post, profile, or linked site. IH “Say something nice…” requires login; that is not a public email.
