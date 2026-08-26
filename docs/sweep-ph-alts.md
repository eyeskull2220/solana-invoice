# Directory sweep: Product Hunt alternatives

Date: 2026-08-26

Week checked: 2026-08-24 (Mon) through 2026-08-30 (Sun)

Product checked: [https://treasury-tools.surge.sh/](https://treasury-tools.surge.sh/)

Named platforms: Open Launch, Fazier, Tiny Launch

## Result

ZERO

No free, no-login launch this week. Nothing was posted.

Prior finding (login or paid) still holds. All three named boards are live. Each submit path stops at a login wall before a listing can be created. Paid “publish now” tiers exist; they were not used.

## Why ZERO

Rule used: if **login** / **paid** / dead → write ZERO. Do not create accounts. Do not pay a card fee.

Live checks on 2026-08-26 (UTC). HTTP follow-redirects and a logged-out browser were used. No Google / GitHub / X / email sign-in. No forms filled.

| Platform | Live | Submit path (logged out) | Free this week? | Verdict |
| --- | --- | --- | --- | --- |
| Open Launch | Yes. `GET https://open-launch.com/` → **200**. Homepage showed “Top Projects Launching Today” (Formflow, CLORA, Time, …). | `GET https://open-launch.com/projects/submit` → **200** at `https://open-launch.com/sign-in?redirect=/projects/submit`. Copy: “Welcome back / Sign in to your account to continue.” Google, GitHub, or email + password. | Unknown. The form is behind login. | **ZERO (login)** |
| Fazier | Yes. `GET https://fazier.com/` and `/submit` → **200**. Homepage listed “Today” launches (Freight Calculator Hub, SyncGallery, …). | `/submit` is a public pricing page. Clicking **Submit** on the free Basic card opened a **“Login to Fazier”** dialog (Continue with Google / Continue with Email). Stopped there. | **No.** Basic (Free) copy: “Reviewed & listed within **30 days**” plus a required homepage/footer backlink. Same-week publish is **Lite $29** (“Publish now or schedule”), then Premium $49 / Super $119. | **ZERO (login; free is not this week; this-week is paid)** |
| Tiny Launch | Yes. `GET https://www.tinylaunch.com/` and `/pricing` → **200**. Homepage showed “Launching Now” (streakmate, Toolsy, FindyourAI, …). | `GET https://tinylaunch.com/submit` → **200** at `https://www.tinylaunch.com/login?returnTo=%2Fsubmit`. Copy: “Welcome Back.” Email Continue, or Google / GitHub / X. | **No path without login.** Pricing lists **Standard Launch Free** (“Standard launch queue”) vs **Premium Launch $39/launch** (“Skip the queue”). Queue length for a free slot this week is not visible until signed in. | **ZERO (login; same-week skip is paid)** |

Independent 2026 checks agree with the live pages:

| Source | Platform | Finding |
| --- | --- | --- |
| Firsto (`firsto.co/sites/fazier`) | Fazier | Account required: yes. Free approval ~15 days. Backlink required on free. |
| Firsto (`firsto.co/sites/tinylaunch`) | TinyLaunch | Account required: yes. Free = standard queue. Premium $39 skips queue. |
| Submitator / IndieHunt Fazier pages | Fazier | Basic free + badge/backlink, review wait; Lite paid for publish-now. |
| TinyLaunch pricing page | TinyLaunch | Standard Free vs Premium $39/launch. |

## Nearby Product Hunt alt (not named, same week)

**Uneed** (`https://www.uneed.best/`) is live. On 2026-08-17 they closed the free waiting line to new products (queue was 6+ months). Same-week launch on Uneed is paid: Fast-track **$14.99** or Skip the line **$29.99**. Not a free this-week slot. Not submitted.

## Existing listing

None found for `treasury-tools.surge.sh` or “Treasury tools” as this catalog on Open Launch, Fazier, or Tiny Launch homepages while logged out.

## Not done (on purpose)

- Did not create accounts.
- Did not log in (Google, GitHub, X, or email).
- Did not click Fazier “Continue with Google / Email” after the login dialog appeared.
- Did not pay Lite $29, Premium $39–$49, Super $119, TinyLaunch Premium $39, or Uneed skip fees.
- Did not add a Fazier or TinyLaunch badge/backlink to the catalog.
- Did not submit product copy.
- Did not restack HTML tools.
- Did not resubmit Launching Next, Free Startup Listing, Tarkle, Console.dev, or Indie Hacker Projects.

## Product identity (not submitted)

Kept here only so this sweep is complete. Not posted anywhere.

- Name: Treasury tools
- URL: https://treasury-tools.surge.sh/
- What: One-file HTML tools. No accounts. No wallet connect on the pages. No trading.
- Pay: USDC on Solana only. Not XRP, not native SOL.

Public treasury pay-to (from this repo’s README / catalog; not a seed or private key):

- Solana: `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3`
- USDC mint: `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v`

Live catalog HTML fetched 2026-08-26 still showed the older banner (“Pay on Solana USDC only via the Solana Invoice page”) and did not print the pay-to on the page. Pay-tos above come from repo `README.md` / `catalog.html` after the treasury-address merge.

## PII scan

Checked: this file, live `https://treasury-tools.surge.sh/` HTML, and the three submit/login pages as loaded logged-out.

- No keys, seeds, mnemonic phrases, tokens, passwords, phone numbers, or home addresses.
- No personal email addresses.
- Live catalog: no emails, phones, or wallet strings. “address” appears only as product copy (invoice / tip-jar fields).
- Wallet pay-tos in the identity section are the public treasury Solana address from this repo. They are not a private key.
