# Gitcoin + OnlyDust bounty sweep

**Date:** 2026-08-26 (UTC)  
**Checked live:** 2026-08-26 00:46 UTC  
**Scope:** Gitcoin and OnlyDust only. Non-exploit. Unclaimed. Startable today. Operator does not code.  
**Not an application.** Nothing was claimed, emailed, or submitted.

## Verdict

**ZERO** startable bounties.

Prior lesson (Gitcoin empty, OnlyDust closed) still holds on a live recheck. Neither board has a claimable, non-exploit, non-coding task today. Successor sites (Buidlbox, Ctrl+G, poidh.xyz) were not treated as Gitcoin or OnlyDust listings.

| Board | Live status 2026-08-26 | Startable non-exploit, non-coding bounties |
|---|---|---|
| Gitcoin bounty explorer / API | Dead (404 / DNS NXDOMAIN) | **0** |
| OnlyDust contribution board | Closed (shutdown page) | **0** |
| **Total** | | **0** |

---

## Filters (hard)

A listing had to pass **all** of these to count:

1. Hosted on Gitcoin or OnlyDust themselves, not a catalog blurb pointing elsewhere.
2. Open and unclaimed (or openly claimable) on 2026-08-26.
3. Not a security / vulnerability / exploit / bug-bounty / PoC task.
4. Operator does not code: no GitHub PR, no program work, no “submit a patch.”
5. Startable today: a real claim or apply button on a live board, not a grants round and not an explainer article.

Fail any filter → not counted. Invented listings → not counted.

---

## Gitcoin — empty as a bounty board

Gitcoin’s site is live as a **grants / research / mechanisms catalog**. The old funded-issue explorer is gone.

### Live HTTP (2026-08-26 00:46 UTC)

| URL | Result | What it is |
|---|---|---|
| https://gitcoin.co/ | **200** | Homepage: campaigns, research, apps, mechanisms. No bounty list. |
| https://gitcoin.co/explorer | **404** | “Page not found.” Old Issue Explorer URL. |
| https://gitcoin.co/explorer/ | **404** | Same. |
| https://gitcoin.co/bounties | **404** | Same 404 shell. |
| https://gitcoin.co/api/v0.1/bounties/ | **404** | Historical bounties API is not served. |
| https://gitcoin.co/api/v0.1/bounties/?is_open=true | **404** | Same. |
| https://gitcoin.co/api/v1/bounties/ | **404** | Same. |
| https://explorer.gitcoin.co/ | **DNS fail** (`Could not resolve host`) | Grants Stack explorer host is gone. |
| https://grants.gitcoin.co/ | **DNS fail** | Grants subdomain does not resolve. |
| https://app.gitcoin.co/ | **DNS fail** | No app host. |
| https://gitcoin.co/mechanisms/bounties | **200** | **Explainer article** dated Feb 25, 2026. Names Dework/Gitcoin as example platforms. No open-task table, no claim UI. |
| https://gitcoin.co/apps | **200** | App catalog, not a board. |
| https://gitcoin.co/apps/poidh | **200** | Catalog card for **poidh.xyz** (external). Not a Gitcoin-hosted listing. Out of scope. |
| https://support.gitcoin.co/gitcoin-knowledge-base/misc/cgrants-bounties-and-hackathons-sunsetting-faq.md | **200** | Official sunset: cGrants/bounties platform closed; data retrieval deadline was **2023-07-30**. |
| https://support.gitcoin.co/gitcoin-knowledge-base/misc/cgrants-bounties-and-hackathons-sunsetting-faq/whats-happening-to-the-hackathons-and-the-bounties-program.md | **200** | Official: hackathons and bounties **moved to Buidlbox**. Gitcoin kept Grants. |

Homepage visible copy (fetched same minute) is campaigns and research (Gitcoin Grants 20–24, TheDAO Security Fund, Protocol Guild, mechanism essays). There is no “open bounties” index.

### Checked and excluded (still Gitcoin-adjacent, fail filters)

| Item | URL | Why it is not a startable bounty here |
|---|---|---|
| Mechanisms article “Bounties” | https://gitcoin.co/mechanisms/bounties | Essay, not a board. |
| Gitcoin Security Bounty Program | https://support.gitcoin.co/gitcoin-knowledge-base/misc/gitcoin-security-bounty-program | **Exploit / vulnerability reports.** Requires a proof of concept. Operator does not code. Pays ETH. **Hard exclude.** No PoC was written. |
| poidh catalog card | https://gitcoin.co/apps/poidh | Points at an external protocol. Not Gitcoin’s board. |
| Buidlbox (sunset successor) | https://buidlbox.io/ (host **200**) | Not Gitcoin. Not in this sweep. |

**Gitcoin startable count: 0.**

---

## OnlyDust — closed

The contribution marketplace is shut. Remaining pages are a closure notice or a pivot, not a board.

### Live HTTP (2026-08-26 00:46 UTC)

| URL | Result | Visible copy / meaning |
|---|---|---|
| https://app.onlydust.com/ | **200** | Title still “Find Open Source Projects…”. Body: **“Service discontinued”** / **“OnlyDust Has Closed”**. No project list, no open issues. |
| https://app.onlydust.com/projects | **503** | Same shutdown HTML. Old project route is not a board. |
| https://app.onlydust.com/contributions | **503** | Same shutdown HTML. |
| https://www.onlydust.com/ | **200** | Manifesto: “The OnlyDust chapter closes here.” Directs to **ctrlg.com**. Not a bounty board. |
| https://onlydust.com/ | **200** | Same manifesto as www. |
| https://docs.onlydust.com/ | **200** | Docs shell still up (“Last updated 9 months ago”). No live issues feed. |
| https://api.onlydust.com/ | **530** | Cloudflare error 1016 (origin down). |
| https://hasura.onlydust.com/ | **DNS fail** | API host gone. |

`app.onlydust.com` page text used for this verdict (full visible body, 2026-08-26):

> Service discontinued  
> OnlyDust Has Closed  
> Thank you for the journey. We're proud of what we built together  
> After an incredible journey empowering open source contributors, we've decided to close this chapter. Thank you to our amazing community for making this adventure possible.  
> With gratitude • The OnlyDust Team

Ctrl+G (`https://ctrlg.com/`, host **200**) is the stated successor. It is not OnlyDust bounties. Out of scope.

**OnlyDust startable count: 0.**

---

## PII scan (this file)

| Check | Result |
|---|---|
| Personal emails | None |
| Phone numbers | None |
| Government IDs / KYC documents | None |
| Private wallet keys / seed phrases | None |
| Home addresses | None |
| Personal names of private individuals | None (public org bylines on live pages were not copied in) |
| Public org URLs | Yes — required as sources |
| Public shutdown quotes | Yes — OnlyDust close notice, Gitcoin 404 text |

No applications, no outbound mail, no screenshots of private dashboards.

---

## What this file is not

- Not a Buidlbox, Superteam, Immunefi, or Algora sweep.
- Not a Gitcoin Grants apply list (grants ≠ startable bounties).
- Not exploit research. The Gitcoin security page was opened only to classify and skip it.
- Not a recommendation to use Ctrl+G or poidh.

If the bar is “unclaimed, non-exploit, non-coding, startable today on Gitcoin or OnlyDust,” the honest count on **2026-08-26** is **zero**.
