# Directory sweep: Uneed-like no-login, free queue under 14 days

Date: 2026-08-26

Product checked: [https://treasury-tools.surge.sh/](https://treasury-tools.surge.sh/)

## Result

ZERO

No qualifying directory was posted to. Nothing was submitted.

Rule used: submit **once** only if the live form is **truly no-login** (no account, no OAuth, no email-created account) **and** the **free** queue is **under 14 days**. If login / paid / dead / queue ≥ 14 days / identity fields required → ZERO.

## Skipped on purpose

Not visited for a new post (already covered or explicitly out of scope):

| Directory | Why skipped |
| --- | --- |
| Launching Next | Skip list. Do not resubmit. |
| Free Startup Listing (FSL) | Skip list. Do not resubmit. |
| Tarkle | Skip list. Do not resubmit. (Would otherwise be the closest match: no account, no email, review in 48h.) |
| Tiny Tool Town | Skip list. GitHub issue/PR, not a no-login form. |
| OSSDrop | Skip list. GitHub/login. |
| Uneed paid | Skip list. Free waiting line closed 2026-08-17. Fast-track is $14.99; Skip the line is $29.99. Login required. |
| BetaList | Skip list. Login required. |

Also not resubmitted (same rule as the Toolify sweep): Console.dev, Indie Hacker Projects.

## Live checks (2026-08-26)

Closest Uneed-style and “open form” alternatives that were actually opened. None passed all three gates (no-login **and** free **and** queue &lt; 14 days).

| Directory | Submit URL | Login | Free queue | Gate failed |
| --- | --- | --- | --- | --- |
| Uneed | [uneed.best/pricing](https://www.uneed.best/pricing) | Account | Closed to new products (was 6+ months; first free slots Feb 2027). Paid Fast-track ~14 days at $14.99. | Paid / login. Skip list. |
| Spotlitely | [spotlitely.com/submit](https://www.spotlitely.com/submit) | **Login.** Marketing page says “paste a link.” Clicking Submit redirected to `/login?callbackUrl=%2Fsubmit`. | Instant if logged in | Login |
| Twelve.tools | [twelve.tools/submit-your-tool](https://twelve.tools/submit-your-tool) | No account on step 1 (URL only). Later field is email ([AllDirectories](https://alldirectories.org/directory/twelve-tools/)). | Review 72h, then free queue. AllDirectories: 203 in queue, 12/day → **~17 days**. Submitator (Jul 2026): **~30 days**. Firsto: **31 days** free. Pro $36 / $25.20 with FROGDR skips to 24h. | Free queue ≥ 14 days. Email. Search for “treasury” on twelve.tools: no listing. Catalog footer already links twelve.tools (badge), which is not a completed listing. |
| Startups.fm | [startups.fm/submit](https://www.startups.fm/submit) | No account | **Paid £49** one-off. Homepage CTA is paid. Form still asks name + email. | Paid. Identity fields. |
| LaunchFree.io | [launchfree.io/submit](https://launchfree.io/submit) | No account | 24h human review | Name, email, bio required (PII). Not truly identity-free. |
| Tiny Startups | [tinystartups.com/submit](https://tinystartups.com/submit) | “No signup needed — we create your account with this email” | Viral Bucket: free slot ~420 days (Oct 2026). SubmitSaaS claims instant if complete. | Email creates an account. Queue not proven under 14 days. |
| Unite List | unitelist.com | Account (AllDirectories: login required) | A few days | Login |
| LLM Relevance | [llmrelevance.com/submit](https://www.llmrelevance.com/submit) | No account | 48h review | First name, last name, email required. |
| CurlShip | [curlship.com](https://curlship.com/) / `POST /api/submit` | No account. Instant live. | 0 days | **Email required** in the body. No product contact mailbox to send. Cannot complete without PII. |
| AlternativeTo | [alternativeto.net/contribute/new](https://alternativeto.net/contribute/new) | Cloudflare challenge in this environment | n/a | Could not complete a no-login post. Favors.dev atlas (Jun 2026) lists only **1** open-form free directory among 46, and most remaining paths are account-gated. |
| Toolify.ai | [toolify.ai/submit](https://www.toolify.ai/submit) | n/a | n/a | Paid $99. Separate sweep. Not reused here. |
| SubmitAiTools / Future Tools / AI Tools Neil Patel | (AI-only forms) | Often no login | Short if accepted | Catalog is one-file HTML tools, not an AI product. Out of category. |
| Made with Lovable / madewithbolt | n/a | No login claimed | Instant-ish | Built-with-X only. This catalog is not Lovable or Bolt. |
| Fazier, StartupBase, Peerlist, TinyLaunch, DevHunt, MicroLaunch, StartupFA.me, PeerPush, IdeaKiln, Openhunts | various | Account | Mixed; several have paid skip | Login. Not posted. |
| Tolodora | [tolodora.com](https://tolodora.com/) | Launch form claims instant live | 0 days claimed | Not confirmed as truly no-login without identity fields. Not posted. |

## Why ZERO

After the skip list, **no remaining directory** was:

1. Truly no-login (no account, no OAuth, no email-created session), and
2. Free, and
3. Showing a live free queue **under 14 days**.

The last no-login, no-email, short-queue pattern (Tarkle / FSL / Launching Next) is already done and skipped. Everything else that still goes live in under two weeks either charges, requires a login, or requires a name/email.

## Not done (on purpose)

- Did not create accounts or log in.
- Did not pay Uneed Fast-track, Twelve.tools Pro, Startups.fm £49, Toolify $99, or any card fee.
- Did not POST to CurlShip (email required).
- Did not submit product copy to any directory.
- Did not restack HTML tools.
- Did not resubmit Launching Next, Free Startup Listing, Tarkle, Tiny Tool Town, OSSDrop, Console.dev, or Indie Hacker Projects.
- Did not apply anyone as a freelancer. User does not code.

## Product identity (not submitted)

Kept here only so this sweep is complete. Not posted anywhere.

- Name: Treasury tools
- URL: https://treasury-tools.surge.sh/
- What: One-file HTML tools. No accounts. No wallet connect on the pages. No trading.
- Pay: USDC on Solana only. Not XRP, not native SOL.

Pay-to (allowed on this date):

- Solana: `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3`
- USDC mint: `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v`

## PII scan

Catalog `https://treasury-tools.surge.sh/` and linked tool pages:

- No personal names, phone numbers, home addresses, passwords, keys, seeds, or API tokens.
- Placeholder examples only (`you@studio.example`, `ada@example.com`).
- Treasury Solana pay-to above is published on several tool pay pages. That is an allowed pay-to, not a private identity.
- This file contains no keys, seeds, tokens, passwords, phone numbers, or home addresses. The wallet pay-to above is the only identifier included.
