# Dev.to / Hashnode sweep (2026-08-26)

Research only. **Nothing was posted.** No accounts were created. No OAuth button was clicked. No magic link was sent. No API key was used.

**Product URL checked:** https://treasury-tools.surge.sh/

## Verdict

| Place | Posts published this sweep | Why |
| --- | --- | --- |
| [DEV Community](https://dev.to/) | **ZERO** | Login wall. See login list below. |
| [Hashnode](https://hashnode.com/) | **ZERO** | Login wall. See login list below. |

Without a session, neither site exposes a write/publish form. Guest publish does not exist on the write URLs or on the write APIs checked today.

## Hard stops followed

- Did not invent accounts.
- Did not sign in with GitHub even though this repo’s public login is `eyeskull2220`. Public profile lookups for that slug are empty on both sites; using “Continue with GitHub” would create a new account. That is out of scope.
- Did not type an email, password, or one-time code.
- Did not write or paste a product-post draft or an author bio.
- PII scan of the live catalog is below. This note does not add a personal email, phone, or wallet.

---

## 1. DEV Community (`dev.to`)

| Field | Value |
| --- | --- |
| Write URL | https://dev.to/new |
| HTTP | `200` (HTML login wall; title `New Post - DEV Community`) |
| Login URL | https://dev.to/enter |
| Editor visible without session? | No |

**Login wall (what login):** heading “Join the DEV Community”, then:

- Continue with Apple
- Continue with Facebook
- Continue with GitHub
- Continue with Google
- Continue with MLH
- Continue with Twitter (X)
- Email + password (“Log in”), plus “Create account”

Navbar on the same page is “Log in” / “Create account” only. There is no Publish control until one of those methods succeeds.

**API without a session**

```
POST https://dev.to/api/articles
```

Response today: **HTTP 401** `{"error":"unauthorized","status":401}`.

Forem docs for “Publish article” require an `api-key` header issued from a logged-in user’s settings (`https://developers.forem.com/api/v1`). Public `GET /api/articles` works without a key (read-only). That is not publish.

**Existing account / existing post**

- `GET https://dev.to/eyeskull2220` → **404**
- `GET https://dev.to/api/users/by_username?url=eyeskull2220` → **404** `{"error":"not found","status":404}`
- `GET https://dev.to/search/feed_content?per_page=10&page=0&search_fields=treasury-tools` → `{"result":[]}`

The logged-out Algolia UI at `https://dev.to/search?q=treasury-tools.surge.sh` tokenizes the query and shows unrelated “treasury” / “surge” posts. None of those hits are this catalog. No product post was published from this sweep.

**Not a substitute:** https://dev.to/showcase is a partner directory (“Have something you'd like to showcase? Get in touch.”). It is not a logged-out self-serve product post.

---

## 2. Hashnode

| Field | Value |
| --- | --- |
| Write URL tried | https://hashnode.com/create → `308` `/drafts` → `307` `/login?callbackUrl=%2Fdrafts` |
| Also | https://hashnode.com/draft → `307` `/login?callbackUrl=%2Fdraft` |
| Login URL | https://hashnode.com/login?callbackUrl=%2Fdrafts |
| Editor visible without session? | No |

First hit on `/login` was a Vercel bot checkpoint (`We're verifying your browser`, HTTP 429). After it passed, the page was still a login wall, not an editor.

**Login wall (what login):** heading “Sign in or create an account”, then:

- Continue with Google
- Continue with LinkedIn
- Continue with GitHub
- Continue with Email → email field (placeholder `you@company.com`) + **Send magic link** (disabled until an address is typed). A human-verification widget appeared on that form. Nothing was typed, and the magic link was not sent.

Sidebar shows “Sign in”. There is no New Article / Publish control until one of those methods succeeds.

**API without a session**

- `POST https://gql.hashnode.com/` with `{ me { username } }` followed a **301** to `https://hashnode.com/changelog/2026-05-13-graphql-api-paid-access` (write GraphQL is not an anonymous public endpoint).
- `POST https://gql-beta.hashnode.com/` same query → **200** with GraphQL error `"You must be logged in"` / `UNAUTHENTICATED`, `data.me = null`.
- `GET https://hashnode.com/api/drafts` → **HTTP 401** `{"success":false,"error":"Unauthorized"}`.

**Existing account / existing post**

- `https://hashnode.com/@eyeskull2220` → **User not found**
- Hashnode search for `treasury-tools.surge.sh` → **No results found.**

---

## PII scan (catalog + this note)

Scanned the live HTML of https://treasury-tools.surge.sh/ on 2026-08-26 (`GET` 200, ~10 KB).

| Pattern | Hits on the catalog |
| --- | --- |
| Email / `mailto:` | 0 |
| Phone | 0 |
| Telegram / X / GitHub profile URLs | 0 |
| Solana-like or `0x` wallet strings | 0 |
| SSN-like | 0 |
| Personal name | none in the page text |

Catalog copy is product names, prices in USDC, and “Pay on Solana USDC only via the Solana Invoice page. Do not send XRP or any other chain.” Pay-to is not printed (repo README still says the pay address is pending). Footer mentions a Twelve.tools listing; that is a directory name, not a person.

This markdown file contains:

- Public product URL and public site URLs only
- The public GitHub username already on this repository (`eyeskull2220`), used only to look up empty Dev.to / Hashnode profile slugs
- No personal email, phone, home address, or wallet
- No author bio and no seniority claim

Unrelated Algolia authors from the noisy Dev.to search were not copied here.

---

## What would be required later (not done)

A human with an **already existing** Dev.to or Hashnode session (or an `api-key` / Hashnode token issued to that session) could publish. That session does not exist in this environment, and creating one would invent an account. Until then: **ZERO** posts on both sites.
