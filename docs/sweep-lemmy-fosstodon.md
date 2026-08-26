# Lemmy / Fosstodon sweep — 2026-08-26

Public-community hunt for listing https://treasury-tools.surge.sh/ on Lemmy and Fosstodon/Mastodon.

## Result

**ZERO posts.** No existing Lemmy or Mastodon session. No anonymous compose path. Every create-post attempt stopped at a login (or invite) wall. Exact walls are below.

X was not used. The listing copy does not present anyone as a coder. Pay-to addresses below are the only payment identifiers in this file.

## What we would list (not posted)

Live catalog: https://treasury-tools.surge.sh/

One-file pages for invoices, quotes, receipts, CSV cleanup, and contact forms. Open in a browser. No account. Billed in USDC on Solana only.

**Authorized pay-to (this sweep):**

| Chain | Address | Use on a listing? |
| --- | --- | --- |
| Solana USDC | `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3` | Yes. Matches the live catalog. |
| EVM | `0x9eb954b567ef3616424a6e1bf42c63724930aa54` | Authorized here. Do **not** put this on a public post: the catalog says pay on Solana USDC only and not to send any other chain. |

USDC mint on Solana (public, not a wallet): `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v`

## Constraints checked

| Constraint | How |
| --- | --- |
| No X | No X URLs, no X API, no X handles. |
| Not as a coder | Copy talks about invoices and bookkeeping pages, not repos, not “I built,” not FOSS maintainer. Skipped programmer/FOSS homes. |
| PII | No names, emails, phones, or account handles in this file. |
| Secrets | None. Pay-to is public catalog data. |
| Post only if no-login or existing session | Session store empty. APIs returned 401. Browser showed Login / Sign Up. |

## Communities that fit (public to read; login to post)

None of these allow a guest post. Ranked by whether a later logged-in listing of the **catalog** (not a GitHub repo) would match the room.

### 1. `!selfpromo@lemmy.world` — best Lemmy fit

- URL: https://lemmy.world/c/selfpromo
- Actor: `https://lemmy.world/c/selfpromo`
- Title: Self Promotion
- Description (exact): `Promote your channel, book, etc.  Keep it SFW!`
- Stats on 2026-08-26: 45 subscribers, 13 posts, 2 users active this month. Not restricted to mods.
- Why it fits: the room already holds product links (example still up: “YouTube Transcript Generator – Convert Videos to Text Easily” → autotranscriptor.com, 2025-05-06). A catalog of invoice/CSV pages is the same class: a thing people can open, not a coder changelog.
- Why it is quiet: last post 2026-04-03. A listing would be seen by few people.

### 2. `!selfpromotion@lemmy.ml`

- URL: https://lemmy.ml/c/selfpromotion
- Actor: `https://lemmy.ml/c/selfpromotion`
- Description (exact): `For advertising anything you've made.`
- Stats: 135 subscribers, 7 posts, 5 users active this month. Not restricted to mods.
- Why it fits: advertising a made product is in-scope. Recent posts include apps, not only Fediverse media.
- Catch: “you've made” is creator-talk. Keep the post about the pages, not about who coded them.

### 3. `!smallbusiness@lemmy.world`

- URL: https://lemmy.world/c/smallbusiness
- Stats: 62 subscribers, 2 posts, 4 users active this month. Empty description. Not restricted to mods.
- Why it fits: invoices, quotes, waitlists, expense CSV are small-business pages.
- Catch: existing posts are questions (“how do I get clients”), not storefronts. A link dump may sit unread.

### 4. `!sidehustle@lemmy.world`

- URL: https://lemmy.world/c/sidehustle
- Stats: 38 subscribers, 2 posts, 8 users active this month. Empty description.
- Why it fits: one-file invoice/quote pages for people billing on the side.
- Catch: almost empty. No posted rules to quote.

### 5. `!solana@lemmy.ml`

- URL: https://lemmy.ml/c/solana
- Stats: 101 subscribers, 4 posts, 2 users active this month. Empty description.
- Why it fits: catalog is Solana USDC only. Existing posts are Solana-economy / wallet questions, not programmer showcases.
- Catch: a paid catalog can look like a shill. Keep one link, no price-talk thread, no seed-phrase talk.

### 6. `!freelancers@feddit.uk`

- URL: https://feddit.uk/c/freelancers
- Title: Freelance Hub
- Description (excerpt, exact start): `Welcome to the freelancers hub. A place to share experiences, tips & tricks, shout out to great opportunities, build working relationships and just generally discuss everything related to freelance or even contract work.`
- Promo rule (exact): `Happy for you to promote yourself if you are a freelancers but please be respectful and no spamming.`
- Stats: 126 subscribers, 1 post, 1 user active this month.
- Why it fits: invoice/quote/intake pages are freelance office tools.
- Catch: the one live post is a resource sticky from 2023-07-05. “Promote yourself” means a person, not a store. One catalog link, no spam.

### 7. `!bookkeeping@lemmy.world`

- URL: https://lemmy.world/c/bookkeeping
- Description (exact): `A place for bookkeepers`
- Stats: 21 subscribers, 0 posts, 0 users active this month.
- Why it fits: CSV cleaner, expense CSV, receipts, invoices.
- Catch: empty room. Listing would be the first post.

### Mastodon hashtags (Fosstodon + general Mastodon)

Hashtags are the Mastodon stand-in for communities. Public timelines exist without login. Compose does not.

| Tag | Public feed sampled 2026-08-26 | Fit for this catalog |
| --- | --- | --- |
| `#smallbusiness` | Live on Fosstodon and mastodon.social (shops, services) | Yes |
| `#freelance` | Live | Yes (invoice/quote pages) |
| `#invoicing` | Live (invoice-tool posts exist) | Yes |
| `#USDC` | Live | Yes, if paired with Solana pay-to |
| `#solana` | Live (mostly market news) | Weak; noise |
| `#selfpromo` | Live (writers, not shops) | Weak |
| `#indieweb` | Live (sites/blogs) | Weak; often webdev talk |

Fosstodon local timeline is **not** a listing home even after a future login. See skip list.

## Skip (wrong room, or extra wall)

| Place | Why skip |
| --- | --- |
| `!selfpromo@lemmy.ml` | Exact rule: promote content **on the Fediverse or under Creative Commons licenses**. The Surge catalog is neither. |
| Fosstodon local / member posts | Invite-only **and** CoC ban on commercial promotions (exact text below). Paid USDC catalog is commercial. |
| `!tools@lemmy.world` | Exact: `Tools of all sorts are welcome. They include hand tools, power tools, automotive tools, welding, etc...` Physical tools. |
| `!makerstuff@lemmy.world` | Physical making (“woodworking… 3d printing…”). “Look what I made” would read as a builder, which this sweep avoids. |
| `!cryptolancing@lemmy.wtf` | For-hire job board. Not a product catalog. |
| `!cryptocurrency@lemmy.ca` | Exact: `No posts by bots allowed - prove you're not a bot by having a post history`. News room, not listings. |
| `!cryptocurrencyprojects@lemmy.world` | 11 subscribers; old posts scored negative; “no price talk.” |
| `!defi@lemmy.ml` | Protocol/lending talk, not office pages. |
| `!indieweb@lemmy.ml` / `!indieweb@programming.dev` | Blogs / webdev. Coder-adjacent. |
| Programmer homes (`programming.dev`, self-hosted, Linux) | Out of scope: would frame the lister as a coder. |

## Post attempts (ZERO)

No Lemmy JWT, no Mastodon access token, no browser cookies for these hosts.

### Lemmy.world — create post

1. Browser: `GET https://lemmy.world/create_post`
   - HTTP 302 `Found. Redirecting to /login?prev=/create_post`
   - Landed on `https://lemmy.world/login?prev=%2Fcreate_post`
   - Title: `Login - Lemmy.World`
   - Exact UI wall:
     - Heading: `Login`
     - Label/field: `Email or Username`
     - Label/field: `Password` (placeholder: `Password length must be between 10 and 60 characters.`)
     - Button: `Login`
     - Links: `Sign Up`, `forgot password`
2. API: `POST https://lemmy.world/api/v3/post` (no auth, JSON body with catalog URL, `community_id` 48700 = selfpromo)
   - HTTP 401
   - Exact body: `{"error":"incorrect_login"}`
3. Signup from this host (not used; recorded as a second wall):
   - Browser `GET https://lemmy.world/signup` → HTTP 403
   - Exact body: `{"error":"Signup blocked from Datacenter"}`
4. Site registration mode (API `/api/v3/site`): `RequireApplication`. Application prompt starts: `Please agree to our [Terms of Service (TOS)](https://legal.lemmy.world) and [Privacy Policy](https://legal.lemmy.world/privacy-policy/) by typing `I agree to the TOS` in the form below.`

### Lemmy.ml — create post

1. Browser: `GET https://lemmy.ml/create_post`
   - HTTP 302 `Found. Redirecting to /login?prev=/create_post`
   - Landed on `https://lemmy.ml/login?prev=%2Fcreate_post`
   - Title: `Login - Lemmy`
   - Exact UI wall: same shape as Lemmy.world — heading `Login`, `Email or Username`, `Password`, button `Login`, links `Sign Up` / `forgot password`
2. API: `POST https://lemmy.ml/api/v3/post` (no auth)
   - HTTP 401
   - Exact body: `{"error":"incorrect_login"}`
3. Registration mode: `RequireApplication` (screening questions; not filled, not submitted).

### Fosstodon — compose

1. API: `POST https://fosstodon.org/api/v1/statuses` (no auth)
   - HTTP 401
   - Exact body: `{"error":"The access token is invalid"}`
   - Exact header: `WWW-Authenticate: Bearer realm="Doorkeeper", error="invalid_token", error_description="The access token is invalid"`
2. Browser sign-in: `https://fosstodon.org/auth/sign_in`
   - Title: `Log in - Fosstodon`
   - Exact UI wall:
     - Heading: `Login to fosstodon.org`
     - Paragraph: `Login with your fosstodon.org credentials. If your account is hosted on a different server, you will not be able to log in here.`
     - Fields: `E-mail address *`, `Password *`
     - Button: `Log in`
     - Links: `Sign up`, `Forgot your password?`, `Didn't receive a confirmation link?`
3. Browser compose URL: `https://fosstodon.org/publish` (logged out)
   - Exact sidebar wall:
     - `Mastodon is the best way to keep up with what's happening.`
     - `Follow anyone across the fediverse and see it all in chronological order. No algorithms, ads, or clickbait in sight.`
     - Button: `Create account`
     - Link: `Login` → `/auth/sign_in`
4. Registrations (`GET /api/v2/instance`): `enabled: false`
   - Exact message HTML: `Fosstodon is invite only` then `We have decided to make Fosstodon invite only (read about why that is, here). So you will need to know someone on the server in order to get an account.`
5. CoC (https://hub.fosstodon.org/coc/) — would block this listing even with a session, exact:
   - `DO NOT post commercial promotions, or advertise through posts that are exclusively links and/or which contain excessive hashtags. This includes repetitive self-promotion for profit. We don’t want spam.`
   - `DO NOT use automated tools to post without also monitoring and/or interacting from your account.`

### mastodon.social — compose (general Mastodon, not Fosstodon)

1. API: `POST https://mastodon.social/api/v1/statuses` (no auth)
   - HTTP 401
   - Same token wall: `{"error":"The access token is invalid"}` with `WWW-Authenticate: Bearer realm="Doorkeeper", error="invalid_token", error_description="The access token is invalid"`
2. Browser compose URL: `https://mastodon.social/publish` (logged out)
   - Exact sidebar wall:
     - `Mastodon is the best way to keep up with what's happening.`
     - `Follow anyone across the fediverse and see it all in chronological order. No algorithms, ads, or clickbait in sight.`
     - Link: `Create account` → `/auth/sign_up`
     - Link: `Login` → `/auth/sign_in`
3. Registrations are open (`enabled: true`, `min_age: 16`) but that is a **new account**, not an existing session. Not used.

## Copy ready for a later session (do not post from this sweep)

Lemmy title:

```text
One-file invoice, quote, and CSV pages. No account.
```

Lemmy body:

```text
Public catalog of one-file pages for invoices, quotes, receipts, CSV cleanup, and contact forms. Open in a browser. No account. Pay in USDC on Solana only.

https://treasury-tools.surge.sh/

Solana USDC: 96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3
```

Mastodon (≤500 characters, Fosstodon limit). **Do not post on Fosstodon** (commercial-promo ban). If a non-Fosstodon Mastodon session appears later:

```text
One-file pages for invoices, quotes, receipts, and CSV cleanup. No account. USDC on Solana.

https://treasury-tools.surge.sh/

Solana USDC: 96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3

#smallbusiness #freelance #invoicing #USDC
```

Do not add `#FOSS`, `#opensource`, or “I coded this.” Do not attach the EVM address. Do not link X.

## PII / secret scan (this file)

Scanned before commit:

- No emails, phones, or personal names
- No X / Twitter URLs or handles
- No API tokens, JWTs, or passwords
- Pay-to strings present only as authorized public addresses
- No GitHub account names
