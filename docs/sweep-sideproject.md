# r/SideProject + r/alphaandbetausers sweep

**Date:** 2026-08-26  
**Target:** https://treasury-tools.surge.sh/  
**Question:** Can we list the catalog this week without the user as a coder?  
**Posts made:** **ZERO**

## Verdict

**No. Do not list this week.**

Hard stop fired: this box has **no Reddit login**. Do not invent a session. Do not post as GitHub user-dev. Do not post from an agent account.

Even if a session existed later, listing **without the user as a coder** still fails the maker-authorship bar both subreddits use (first-person “I built this” / product owner seeking testers). An agent cannot satisfy that while staying honest.

## Exact login need

Reddit returned a network-security interstitial, not a subreddit page:

> You've been blocked by network security.  
> To continue, log in to your Reddit account or use your developer token

Observed URL after navigate: `https://www.reddit.com/mod/SideProject/rules/` → HTTP **403**.  
Only cookie present after that hit: `.reddit.com` / `edgebucket`. **No** `reddit_session`, **no** `token_v2`, **no** OAuth bearer.

To continue a future sweep (still not this run):

1. A **human** Reddit account logs in in this environment at `https://www.reddit.com/login/` until the browser store has `reddit_session` (and typically `token_v2`), **or**
2. A Reddit **developer / OAuth token** with `identity` + `read` (and `submit` only if a later task actually posts) is present as env such as `REDDIT_ACCESS_TOKEN` (or `REDDIT_CLIENT_ID` + `REDDIT_CLIENT_SECRET` + refresh token). None of those env vars exist here.

The account must be the **product owner who can answer comments**. It must **not** be:

- invented for this agent
- this GitHub identity (`eyeskull2220` / user-dev)
- a throwaway used only to drop the catalog URL

After login, re-read **live** `/r/SideProject/about/rules` and `/r/alphaandbetausers/about/rules` as that user before any post. This run could not.

## Session check (this box, 2026-08-26)

| Check | Result |
|---|---|
| `REDDIT_*` / PRAW env | none |
| `~/.reddit`, Reddit config files | none |
| Chrome profile Cookies under `~/.config` | none |
| Playwright Chrome Cookies | 1 cookie: `.reddit.com` `edgebucket` only |
| `reddit_session` | missing |
| Ability to GET subreddit rules JSON | HTTP 403 (curl, WebFetch, Playwright) |

**Posts this week from this box: ZERO.**

## Paid-tool gate

Hard rule: do not post if login is missing **or** rules ban paid tools.

- Login missing → **do not post** (this gate alone is enough).
- Paid-tool **ban**: **not shown** in 2026 third-party reconstructions of either sub. Neither sidebar reconstruction says “no paid products.” Commercial / paid projects are treated as allowed when framed as a real build (SideProject) or a genuine tester ask (alphaandbetausers). Affiliate / referral / vote-manipulation / waitlist-only links are the usual bans, not “has a price.”
- Official live rule text was **unread** (403). If live rules later ban paid tools, that is a second hard stop.

The catalog is explicitly billed (9 USDC / 49 USDC). That is a **paid listing**, not a free beta. That is allowed under reconstructed SideProject commercial-project guidance; it is a **poor fit** for alphaandbetausers (that sub wants testers, often with free/early access), but reconstructions do not call paid tools a ban.

## Without the user as a coder

**No.**

| Sub | Why a non-coder / agent listing fails |
|---|---|
| r/SideProject | Reconstructions: posts must be about something **you actually built**, shown as a build story, not a classifieds link. “Must be a genuine project you built.” Posting a priced catalog as an agent, or as someone who is not the coder/maker, is a misrepresentation. |
| r/alphaandbetausers | Reconstructions: the poster is the builder recruiting testers, states stage + feedback ask, and **replies to every tester**. An agent with no owner account cannot do that. |

Do not paper over this by posting as user-dev.

## Rules as read (with source limits)

Live Reddit HTML/JSON for both subs: **403 / network-security login wall**. Wayback `id_` fetch of `/r/SideProject/about/rules.json` returned empty. PullPush Cloudflare-challenged.

What follows is **reconstruction from 2026 public guides**, not the live sidebar. Treat as guidance, not a substitute for an authenticated rules read.

### r/SideProject

Sources: [mediafa.st/subreddit/sideproject](https://www.mediafa.st/subreddit/sideproject) (claims 3 community rules, 2026), [redditmaster.com/subreddit-rules/sideproject](https://www.redditmaster.com/subreddit-rules/sideproject), [founderreply.com/reddit/sideproject](https://founderreply.com/reddit/sideproject), [varnan-tech opendirectory playbook](https://raw.githubusercontent.com/varnan-tech/opendirectory/main/skills/reddit-post-engine/references/subreddit-playbook.md). [redditgrowthdb](https://www.redditgrowthdb.com/database/subreddits/sideproject) (updated 2026-07-13) says promotion allowance was **not independently verified** and to read official live rules.

Reconstructed community/norms:

1. Radical transparency / show the real product (no email-gate / waitlist-only landing).
2. Engage; reply to comments; do not post-and-ghost.
3. No landing-page-only spam (mediafa.st’s third rule: “No Landing Page Gates”).

Also consistently reported: you built it; tell the build story; no affiliate/referral schemes; no hiring posts; no rapid reposts of the same project; commercial OK if it is not a hard sell; Reddit 90/10 self-promo guideline still cited.

**Paid tools banned?** Not in these reconstructions.

### r/alphaandbetausers

Sources: [mediafa.st/subreddit/alphaandbetausers](https://www.mediafa.st/subreddit/alphaandbetausers) (claims 4 community rules, 2026), [launchkit.me alphaandbetausers guide](https://launchkit.me/blog/how-to-post-on-r-alphaandbetausers/), [iwe.md community note](https://iwe.md/templates/marketing-workspace/data/communities/reddit/alphaandbetausers/) (2026-07-26: promo is on-topic; read sidebar before submitting). RedditMaster has no matching rules page (404).

Reconstructed rules:

1. Clearly state what the product does and the stage (alpha / beta / launched).
2. Include what feedback you want.
3. Respond to all testers who give feedback.
4. Do not spam the same product repeatedly.

Also reported: tag platform + stage (e.g. `[Web, Beta]`); link a **working** product; self-promo is the point of the sub; still not a dump of a priced storefront with no tester ask.

**Paid tools banned?** Not in these reconstructions. Incentives for testers (free access, lifetime deal) are commonly recommended; a 9–49 USDC checkout with no tester offer is off-culture, not documented as a ban.

## Catalog / PII / secrets scan

Scanned 2026-08-26: live catalog, live invoice + `config.js`, linked `*.surge.sh` tools, and this repo after `origin/main` (includes treasury address from PR #27).

**Pay-to allowlist for this sweep (OK to appear):**

- Solana: `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3`
- Ethereum: `0x9eb954b567ef3616424a6e1bf42c63724930aa54`

| Finding | Where | Notes |
|---|---|---|
| Solana pay-to (allowlisted) | Repo `config.js`, `README.md`, `catalog.html`, `index.html`; live `https://solana-invoice-treasury.surge.sh/config.js` | Expected. Invoice HTML fallback still says `ADDRESS_PENDING` if `config.js` fails to load. |
| Ethereum allowlisted address | nowhere | Product is Solana USDC only. Not a leak. |
| USDC mint `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v` | invoice/tools | Public Solana USDC mint, not a personal wallet. |
| Live catalog HTML | https://treasury-tools.surge.sh/ | **Stale vs repo:** no pay-to in the catalog page; still “Pay on Solana USDC only via the Solana Invoice page.” |
| Emails | form-to-email, waitlist, intake, link-in-bio | Placeholders only: `you@studio.example`, `ada@example.com`. No personal inboxes. |
| Phone-like `2166136261` | receipt tool JS | Hash seed, not a phone number. |
| Secrets / mnemonic / private key / API keys | none | No `sk-`, no seed phrases, no private keys. |
| Names / home addresses / government IDs | none | |

No extra wallets beyond the allowlisted Solana pay-to and the public USDC mint.

## This week (week of 2026-08-26)

| Action | Status |
|---|---|
| Post to r/SideProject | **ZERO** — no session; not the coder; do not post as user-dev |
| Post to r/alphaandbetausers | **ZERO** — same |
| Invent Reddit cookies / OAuth | **not done** |
| Draft published on Reddit | **none** |

Re-run only after: (1) human Reddit login or developer token as specified above, (2) authenticated live rules read, (3) a human maker (not this agent, not user-dev) owns the thread and will answer comments.
