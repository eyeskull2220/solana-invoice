# Replit sweep — 2026-08-26

**Window:** 2026-08-26 00:46–00:49 UTC  
**Question:** are there live Replit **bounties** or **paid templates** today?  
**Answer:** **ZERO** open Replit bounties. **ZERO** paid templates.

Nothing was applied. Nothing was posted. This file is a fetch log, not a job list.

## Hard constraints (this run)

| Rule | What we did |
|---|---|
| User does not code | Did **not** apply to any listing, Contra expert program, or “Hire / Get hired” flow. Coding gigs are out of scope even when a successor page shows them. |
| Do not apply | No accounts created. No Contra applications. No Replit logins. |
| Prior 403 | Replit GraphQL is still **403** without Origin/Referer. Per instruction: **if still 403 → ZERO**. Count stays **0**. |
| Do not invent | Dead, redirected, or blocked boards are logged. They are not filled in from memory. |
| PII scan | This file contains **no** personal emails, phone numbers, government IDs, home addresses, or wallet keys. Public URLs only. |

## Verdict

| Bucket | Count today | Why |
|---|---|---|
| Open Replit bounties | **0** | `/bounties` is gone. GraphQL bounty feed is still 403 (then unusable). |
| Paid Replit templates | **0** | `/templates` and `/marketplace` 404. Gallery is free remix only (82 items, no price field). |

Do not treat Contra as a Replit bounty board. The old bounty URL now **301s** to a Contra “hire experts” landing page. That is a different product. Those gigs require coding or design work. **Not counted. Not applied.**

## What we actually fetched

### Bounties

| Time (UTC) | URL | Result |
|---|---|---|
| 00:46 | `GET https://replit.com/bounties` (no follow) | **301** → `https://contra.com/replit/?utm_source=replit&utm_medium=referral&utm_campaign=bounties` (120 bytes, Cloudflare on Replit) |
| 00:46 | same, follow redirects | **200** on Contra HTML (“Hire Replit Experts for Your Web Project”). Not a Replit listing API. |
| 00:46 | `https://replit.com/community/bounties` | **404** (“Page not found \| Replit”) |
| 00:46 | `https://replit.com/api/bounties` | **404** |
| 00:47 | `POST https://replit.com/graphql` `{ __typename }` | **403**, body: `Expected X-Requested-With header` (32 bytes) |
| 00:48 | same + `X-Requested-With: XMLHttpRequest` | **403**, body: `Expected referrer, referer, or origin header` (44 bytes) |
| 00:48 | same + Origin `https://replit.com` + Referer | **400** JSON: `Persisted query hash required`. No public bounty query. |
| 00:48 | GraphQL `bounties` / `bountySearch` / `BountiesFeed` | Same **403** then **400**. No feed. |
| 00:46 | `https://replit.com/blog/bounties` | **200** — **historical launch post**, not a live board. |
| 00:48 | `https://news.ycombinator.com/item?id=44643875` | **200** — 22 Jul 2025 thread: Bounties shut down **2025-09-06**; users pointed at Contra. |

GraphQL is the same **403** class as the prior run. Instruction: **ZERO**. We did not guess leftover Cycles bounties.

### Paid templates

| Time (UTC) | URL | Result |
|---|---|---|
| 00:46 | `https://replit.com/templates` | **404** |
| 00:46 | `https://replit.com/templates/` | **404** |
| 00:46 | `https://replit.com/marketplace` | **404** |
| 00:47 | `https://replit.com/templates-community` | **404** |
| 00:47 | `https://replit.com/community/templates` | **404** |
| 00:47 | `https://replit.com/talk/share` | **404** |
| 00:47 | `https://replit.com/store` | **404** |
| 00:47 | `https://store.replit.com` | DNS fail (`Could not resolve host`) |
| 00:46 | `https://replit.com/gallery` | **200**. `__NEXT_DATA__` has `allGalleries` = **82** items. Keys: title, slug, deck, remixCount, viewCount, creatorName, tags. **No** `price`, `paid`, `cost`, `cycles`, `isPaid`, `isPremium`. |
| 00:48 | `https://replit.com/gallery/life/entertainment/be-mine-valentine` | **200**. “Remix” present. **Buy / Purchase / Add to cart / paid template = 0**. |
| 00:46 | `https://replit.com/design` | **200** Replit Design (remix/start), not a store. |
| 00:48 | `https://docs.replit.com/design/start-from-a-template` | **200**. Official path is remix a featured template. No sale price. |

Gallery `$` hits in the JSON were blurHashes and a **Core plan** “or $20” promo string, not template SKUs.

## Successor page (not counted)

`https://replit.com/bounties` lands on Contra. Browser snapshot of `https://contra.com/replit/jobs` (00:48 UTC) showed a “Jobs hiring Replit experts” list. Those are **Contra** freelance posts (coding / design), not Replit bounties and not paid templates.

**Out of scope:** user does not code. **Not applied.** Titles are omitted here so this file is not a hidden apply list.

Contra also advertises an “Apply to be an Expert” opportunity URL. That is an expert-network signup, not a Replit bounty. **Not applied.**

## PII scan (this file)

Scanned before commit:

| Class | Result |
|---|---|
| Email addresses | **None** |
| Phone numbers | **None** |
| Government IDs / passport numbers | **None** |
| Home / street addresses | **None** |
| Wallet / private keys | **None** |
| Login cookies / tokens | **None** (Cloudflare cookie names appeared only in the live fetch log on disk, not in this file) |

Public hostnames (`replit.com`, `contra.com`, `news.ycombinator.com`) are not PII.

## Honest gap

- Replit Bounties as a product is **not live** on 2026-08-26. The canonical path is a **301 to Contra**.
- The GraphQL surface that used to serve a bounty feed is still **403** without browser Origin/Referer, then **400 persisted-query** if those headers are added. That is not a listing.
- There is **no** Replit paid-template storefront in this window. Gallery templates are remixable, not for sale.

Re-fetch from a logged-in residential browser only if the question changes to “Contra gigs.” That is a different sweep. **This sweep’s count is ZERO.**
