# Newsletter sweep — tool URL by email

Sweep date: **2026-08-26**.

Goal: find newsletters that still accept a **tool URL by email this week**, skip Console.dev (already mailed), keep copy to **product facts only**, and do not write for a coding audience.

## Hard rules

- **Do not mail a second Console.** `hello@console.dev` was already used on 2026-08-25. No resend, no follow-up, no draft to that inbox.
- **PII scan** on every body and on this file: no personal name, no personal inbox, no home place, no wallet, no GitHub. Product URLs and product facts only.
- **Product copy only.** What the pages do, the live URLs, price in USDC, no account / no wallet connect. No bio, no “I built”, no source-code pitch.
- **User does not code.** Pitch as one-file HTML pages for freelancers and small studios. Not as libraries, CLIs, or “dev tools.”
- **Inbox rule.** A real unused *newsletter* inbox → **draft only**, unless the public page is clearly “email us this product URL.” A directory that publishes that instruction may be sent. Forms, reply-to-an-issue, Twitter/Bluesky, and generic “say hello” inboxes are not send.

## Product URL (the one to send)

Hub: https://treasury-tools.surge.sh/

Live pages used in copy:

- https://solana-invoice-treasury.surge.sh/ — invoice, QR, copy-address. Offline. 9 USDC.
- https://csv-cleaner-treasury.surge.sh/ — trim, drop empty/duplicate rows, pick columns. 49 USDC.
- https://form-to-email-treasury.surge.sh/ — mailto + copy form builder. 49 USDC.
- https://rss-to-webhook-treasury.surge.sh/ — check a feed, POST new items as JSON. 49 USDC.

These pages do not trade. No account. No wallet connect.

## Already mailed (do not touch)

| Outlet | Inbox | When | Status |
|---|---|---|---|
| Console.dev weekly | hello@console.dev | 2026-08-25 | Sent. Autoreply: they review submissions for the next newsletter and do not reply one-by-one. **No second mail.** |

Console’s public submit line is still “email hello@console.dev with the details” on https://console.dev/selection-criteria. That is why it was mailed once. It is out of this sweep.

## Sent this week (public product submit-by-email)

| Outlet | Inbox | Why send | When |
|---|---|---|---|
| IndieHackerTools | submit@indiehackertools.dev | Public page https://indiehackertools.dev/submit says: submit the tool by email (name, URL, short description, features, audience). That is a product URL inbox, not a “hello” desk. | 2026-08-26 |

Note: IndieHackerTools is a **directory**, not a weekly newsletter (no `/newsletter` page on 2026-08-26). It is the only unused inbox this week whose public copy is clearly “email us the product.” Sent for that reason only.

## Draft only (real newsletter inboxes, not a dedicated product-submit)

Left in Drafts. Not sent.

| Outlet | Inbox | Why draft, not send | Draft id |
|---|---|---|---|
| Frontend Focus (Cooper Press) | editor@cooperpress.com | Issue #754 (2026-08-12) says “Got a link for us? Reply and tell us.” Next issue is **2026-08-26** after a one-week break. That is a public *link* invite, not a dedicated “submit your product” address. Editorial inbox on https://cooperpress.com/. | `r7527864399452778308` |
| Dense Discovery | new@densediscovery.com | Issue footers (e.g. archive #6, #20) say send suggestions for GIFs, apps, accessories, visual inspiration to this address. That is a suggestion slot, not “submit your product.” Current site is behind Cloudflare; address taken from published issue footers, not guessed. | `r-166957782214046632` |

## Checked this week — not email-submit (do not mail)

These are live this week but the public path is a **form**, a **login**, or **social**, not “email a tool URL.”

| Outlet | This week | Public path | Why not mail |
|---|---|---|---|
| Console.dev | Latest email 2026-08-20 (Thu) | hello@console.dev | Already mailed. Hard skip. |
| Frontend Focus | Back 2026-08-26 | Reply to the issue, or editor@ | Drafted. Not a product-submit inbox. |
| JavaScript Weekly | Issue #799, 2026-08-25 | Same Cooper Press family | Same editorial inbox as Frontend Focus. One draft covers the house. JS Weekly’s current issue does not print a submit-by-email line. |
| PyCoder’s Weekly | Site live; latest sample #749 | https://pycoders.com/submissions → form | Form, not email. |
| Changelog News | Submit page live | https://changelog.com/news/submit (sign-in). editors@changelog.com is terms/support. | Form + support inbox. Not product submit-by-email. |
| Sidebar | Submit page live | https://sidebar.io/submit (log in) | Form. |
| Web Tools Weekly | Subscribe page live | Submit via X (@LouisLazaris), not email | Social, not email. |
| Tech Productivity | Submit page live | X / Bluesky to the same editor | Social, not email. |
| Hacker Newsletter | Subscribe page live | Curates from Hacker News; no public “email us a URL” | No direct submit. |
| OrangeBot Weekly | Issue #3, 2026-08-07; weekly still advertised | https://orangebot.ai/submit (sign-in form). Mentions a shot at the weekly digest. | Form. Also AI-tool shaped; these pages are not AI products. |
| Launch Llama newsletter | Weekly still advertised | Directory + newsletter **forms**. contact@launchllama.co is a general contact, not the submit path. | Form. Do not mail the contact desk. |
| Cool Tools / Recomendo | Submit-a-tool page live | Form. Pays $25 for a **reader review** after six months of use. Asks for the reviewer’s name. | Form + PII. Not a maker product pitch. |
| CSS Weekly | Contact page live | Form for “send a link.” info@css-weekly.com is ads. | Form / ads inbox. |
| Python Weekly | Issue 759, 2026-08-20 | No public submit-by-email on the live issues | No inbox to use. |
| Founder Weekly | Issue 745, 2026-08-19 | Same house as Python Weekly; no public submit-by-email | No inbox to use. |
| Programmer Weekly | Archive through 2026-07-30 | Same house; no public submit-by-email | No inbox to use. |
| Bytes.dev | Advertise page live | sponsor@fireship.dev is **paid ads** | Not a free product submit. |
| TLDR | Live daily | No verified tips@ / submit-by-email on the public site this week | Do not guess an inbox. |
| The Browser | Live | editor@thebrowser.com is “say hello,” long-form writing, not tools | Not a product-submit inbox. Do not draft. |
| NoCodeWorkflows newsletter | Weekly Tuesday advertised | Product submit is a **form** (asks for phone and location) | Form + PII fields. Skip. |
| Indie Hackers newsletter | Subscribe live | No public “email us a tool URL” | Skip. |
| Smallweb | submit@smallweb.cc | Personal sites / blogs, not products | Out of scope. |

## Not a fit (audience or format)

- ToolAtlas / ToolChase / AITrendTool: email submit exists, but they are **directories**, not newsletters, and they ask for AI/DevOps categories these pages do not match. Not mailed.
- IndieHackerTools: directory (see Sent). Weak newsletter match; mailed only because the submit page is explicit.
- OrangeBot, Launch Llama, Future-tools-style lists: AI-tool weeklies/directories. These pages are offline HTML, not AI products.

## Copy used (product only)

Shared facts in every body:

- Tiny HTML tools. No account.
- Each one is a single static page.
- Hub URL + the four live tool URLs.
- These pages do not trade. No wallet connect.

Omitted on purpose (PII / off-brief):

- Personal name and personal inbox
- GitHub / “source”
- Treasury wallet and USDC mint
- Pay-page address
- Location, bio, “I built this”

IndieHackerTools extra fields (their submit page asks for them): tool name, website URL, brief description, key features, target audience, prices in USDC.

## PII scan (this file + mail)

| Check | Result |
|---|---|
| Personal name in bodies or this file | None |
| Personal inbox in bodies or this file | None (only public outlet inboxes) |
| Wallet / mint | Not in mail. Not in this file. |
| GitHub | Not in mail. Not in this file. |
| Home / city | None |
| Console second send | None. Only the 2026-08-25 thread. |
| Cooper Press / Dense Discovery | Draft only |

## This week in one line

The only **newsletter** that still prints “email us a tool URL” as the product path is Console.dev — already mailed, not reused. Frontend Focus is the live newsletter this week that invites a **link by reply** (drafted). Dense Discovery still has a public **suggestion** address in old issue footers (drafted). The only unused inbox whose live page says “email us the product” is IndieHackerTools (sent; directory, not a newsletter).
