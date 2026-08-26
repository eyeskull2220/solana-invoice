# Algora + Polar sweep — 2026-08-26 UTC

**Verdict: ZERO**

No unclaimed docs / HTML / small-fix bounties were created or updated on **2026-08-26** (UTC). Nothing was claimed, attempted, or piled onto.

Sweep time: **2026-08-26 ~00:48 UTC** (calendar day only ~48 minutes old at scan). Window is the UTC date only, not a multi-day lookback.

## Hard filters (applied)

| Filter | Result |
|---|---|
| Created **or** updated today (2026-08-26 UTC) | Required. Older boards ignored. |
| Unclaimed | Required. |
| Work type: docs, HTML, or small fix | Required. |
| User does not code | No `/attempt`, no `/claim`, no PR into foreign repos. |
| No exploits | Nuclei templates, scanners, and exploit-shaped work skipped. |
| Do not pile onto nuclei / drizzle | Excluded even if they had open dollars. |
| PII | This file has no emails, phones, names, or wallet addresses. |

## ZERO — takeable today

Empty. No row qualifies.

## Sources checked

### Algora

| Source | Today (created/updated 2026-08-26) |
|---|---|
| Global tRPC `https://console.algora.io/api/trpc/bounty.list` (no org, and with `status=active`) | `items: []` |
| Global HTML `https://algora.io/bounties` and `/explore` | 404 |
| GitHub: `commenter:algora-pbc` created/updated today | 0 |
| GitHub: `involves:algora-pbc` created/updated today | 0 |
| GitHub: `author:algora-pbc` / app `algora-pbc` created today | 0 |
| GitHub labels `💎 Bounty`, `bounty`, `$10`–`$250`, `funded`, `polar` created/updated today | 0 |

Org HTML boards that still list **open** dollars (all stale; none say hours/minutes/today):

| Org board | Open pile (age on board) | GitHub `updated_at` (UTC) | Today? |
|---|---|---|---|
| [projectdiscovery](https://algora.io/projectdiscovery/bounties) | nuclei#6674 $100 (5 months); nuclei#6532 $100 (6 months) | 2026-05-04; 2026-08-08. Both **closed**. | No. Excluded (nuclei). |
| [drizzle-team](https://algora.io/drizzle-team/bounties) | drizzle-orm #1603 $50, #1083 $30, #554 $30, #376 $50, #1188 $200 (31–36 months) | Latest 2026-08-25 (#1188). Others 2026-08-24 or older. | No. Excluded (drizzle). |
| [tscircuit](https://algora.io/tscircuit/bounties) | Several $1–$170 items (3–21 months on board) | Latest open-board issue `updated_at` 2026-08-25 (pgstrap#2). None on 2026-08-26. | No. Not today. Not docs/HTML/small-fix for a non-coder. |
| [triggerdotdev](https://algora.io/triggerdotdev/bounties) | zod#2654 $25 (36 months) | Issue **closed**, updated 2026-08-13 | No |
| supabase, algora, infisical boards | “No open bounties” | — | No |

Drizzle and nuclei are recorded only to show they were **not** piled onto. They are not candidates.

### Polar

Polar is a merchant-of-record / billing product now. The public issue-funding bounty surface is gone.

| Source | Result today |
|---|---|
| `https://api.polar.sh/v1/issues` | 404 `{"detail":"Not Found"}` |
| `/v1/issues/search`, `/v1/issue-funding`, `/v1/pledges`, `/v1/rewards` | 404 |
| `https://polar.sh/issues`, `/polarsource/issues`, `/explore` | 404 |
| Polar docs `llms.txt` | No issue-funding, bounty, or pledge pages |
| GitHub `repo:polarsource/polar` issues created/updated 2026-08-26 | 0 |
| GitHub `org:polarsource` issues created/updated 2026-08-26 | 0 |
| GitHub issues mentioning `polar.sh` created/updated today | Dependency-bump / tools-list PRs only. Not bounties. |

## PII scan

| Check | Result |
|---|---|
| Emails | None in this file |
| Phone numbers | None |
| Personal names | None |
| Wallet / receive addresses | None (not copied here) |
| Secrets / tokens | None |

Foreign GitHub issue URLs above are public tracker links, not personal data.

## Not done

- No `/attempt` or `/claim` comments.
- No forks or PRs into Algora/Polar target repos.
- No nuclei template or exploit work.
- No drizzle-orm pile-on.

Re-run after more of 2026-08-26 UTC has elapsed if a same-day recheck is needed. This snapshot is ZERO for the window scanned.
