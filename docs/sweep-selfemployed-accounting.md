# Sweep: r/selfemployed and r/Accounting (invoice / CSV help with a mailto)

**Date:** 2026-08-26  
**Window:** this week — 2026-08-19 00:00 UTC through 2026-08-26 00:40 UTC  
**Result: ZERO**

Nothing was posted. Nobody was emailed. There is no one to write to from this sweep.

This note is for a person who does not write code. It is a read-only check of public Reddit posts. It is not a script, not a mailing list, and not a go-ahead to contact anyone.

## What had to match

A post (or a public comment on it) only counted if **all** of these were true:

1. It was in **r/selfemployed** or **r/Accounting**.
2. It was posted **this week** (window above).
3. The writer was **asking for help** with an **invoice** or a **CSV** (or invoicing / cleaning a spreadsheet file).
4. The same public text included a **mailto** — a real `mailto:` link or a visible email address someone could open in their mail app.

No mailto → not a match. A discussion about invoices that says “reply here” is not a match.

## Direct answer

**Qualified matches this week: 0**

Do not post on those subreddits. Do not send mail. There is no inbox from this hunt.

## How the pages were read

Reddit’s own site did **not** return a usable public feed from this machine:

| Address tried | What came back |
|---|---|
| `reddit.com` JSON (`/r/selfemployed/new.json`, `/r/Accounting/new.json`, search JSON) | **HTTP 403** “Blocked” |
| `old.reddit.com` JSON | **HTTP 403** “Blocked” |
| Pullpush archive | **HTTP 403** Cloudflare wall |

That is a block, not a list of posts. **HTTP 429** (too many requests) was **not** the status on this run. The standing rule still applies: if Reddit returns **429**, treat the hunt as **ZERO** and stop. Nobody posts.

Because the live Reddit hosts were blocked, the same public posts were read from the **Arctic Shift** public index (`arctic-shift.photon-reddit.com`), which answered **HTTP 200**. That index is a copy of public Reddit threads, not a private inbox.

Counts from that index in the window:

- **r/selfemployed:** 36 posts; 54 comments scanned. **Mailto: 0**
- **r/Accounting:** 800+ posts (the board is busy; pages were walked through 2026-08-26 00:39 UTC). **Mailto: 0** on those posts.
- Comments on every thread that even *mentioned* invoice or CSV: **mailto: 0**
- First 1,000 r/Accounting comments in the window (high volume; not every comment on the whole board): **mailto: 0**

Hidden / obfuscated addresses (`name [at] domain [dot] com`) were also checked on those posts. **None.**

## Nearby posts that still fail (not leads)

These public threads talk about invoices, CSV, or spreadsheets. **None of them include a mailto.** They are listed only so this ZERO is not a silent “we did not look.” **Do not comment. Do not DM. Do not invent an email.**

### r/selfemployed

- [India] Freelancers/solopreneurs of India: How do you handle leads, quotes, invoicing ? — 2026-08-22 — body empty in the index — [thread](https://www.reddit.com/r/selfemployed/comments/1vvp6av/)
- Caught between a spreadsheet and a price tag… — 2026-08-23 — body **[removed]** — [thread](https://www.reddit.com/r/selfemployed/comments/1vw0sam/)

### r/Accounting (invoice / CSV mention, no mailto)

Examples only. Same gate: **no mailto, not a lead.**

- Why are so many businesses still processing invoices manually? — 2026-08-20 — **[removed]** — [thread](https://www.reddit.com/r/Accounting/comments/1vtgcas/)
- Built a local setup to stop chasing vendor invoices every morning — 2026-08-20 — author describing their own AP intake, not asking for a tool with a mail link — [thread](https://www.reddit.com/r/Accounting/comments/1vtnnb8/)
- Any recommendations for payment process to automate ACH pulls from clients? — 2026-08-20 — chasing invoices, no mailto — [thread](https://www.reddit.com/r/Accounting/comments/1vtqkx5/)
- I need help with intercompany reconciliation — 2026-08-21 — entities invoice each other; no mailto — [thread](https://www.reddit.com/r/Accounting/comments/1vuo5fy/)
- Managing multiple clients as Accounting firm — 2026-08-24 — billing & invoicing ops; no mailto — [thread](https://www.reddit.com/r/Accounting/comments/1vwzctf/)
- Small business owners who send invoices regularly — what's actually your bottleneck with unpaid payments? — 2026-08-25 — founder research, not a help-ask with mail — [thread](https://www.reddit.com/r/Accounting/comments/1vxmew9/)
- How much of your week is wasted typing PDF invoices into Quickbooks… — 2026-08-25 — empty body in the index — [thread](https://www.reddit.com/r/Accounting/comments/1vxsid1/)
- What are you using for automated invoice data extraction? — 2026-08-25 — tool question, no mailto — [thread](https://www.reddit.com/r/Accounting/comments/1vxy29d/)
- How do you handle invoice exceptions that fail 3-way matching? — 2026-08-25 — AP process, no mailto — [thread](https://www.reddit.com/r/Accounting/comments/1vy3kbw/)
- How much of your reconciliation process is still manual? — 2026-08-25 — mentions CSV/settlement files; research question, no mailto — [thread](https://www.reddit.com/r/Accounting/comments/1vyde3d/)

The India invoicing thread is the closest *ask* on r/selfemployed. It still has **no mailto**, so it stays **out**.

## PII scan

This file must not become a contact sheet.

| Check | Result |
|---|---|
| Email addresses copied into this file | **None** (none found on matching asks; none copied from nearby threads) |
| `mailto:` links copied | **None** |
| Phone numbers copied | **None** (a few digit strings showed up on unrelated Accounting posts; they were not copied here) |
| Chat-app invites copied | **None** |
| Reddit usernames listed as people to contact | **None** |
| Action taken with any personal data | **None** |

If a later sweep finds a public mailto, copy only what the person already published, keep it in this kind of note, and still do not post on the thread unless a human decides that separately.

## What you should do

1. **This week: nothing.** There is no email to open.
2. **Do not post** on r/selfemployed or r/Accounting about the treasury tools from this hunt.
3. **Do not** paste the catalog or the invoice/CSV pages under those threads. That would be posting, which this sweep forbids.
4. If you want buyers who already said “email me,” wait for a week where a public mailto actually appears, or use a channel that is already yours (your own site, your own inbox).

## What this is not

- Not a list of customers.
- Not permission to scrape Reddit every hour (live Reddit was already blocked).
- Not a coding task. No script to run. No API key to add.
- Not a change to the live tools (Solana Invoice, CSV Cleaner, Form to Email).

## Snapshot

- **Qualified (invoice/CSV help + mailto, this week, those two boards): 0**
- **Posted: no**
- **Emailed: no**
- **PII in this file: none**
