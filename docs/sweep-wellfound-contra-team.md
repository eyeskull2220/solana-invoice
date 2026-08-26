# Sweep: Wellfound / Contra — hire an agent team for one job

**Date:** 2026-08-26  
**Fetch window:** 2026-08-26 00:44–00:48 UTC  
**Boards:** Wellfound (wellfound.com) and Contra (contra.com)  
**Status:** research only. Nothing was applied, emailed, messaged, or pitched.

## Verdict

**ZERO.**

No listing on either board in this window is “hire an agent team for one job.” Every live item that opened is a **human seat**: a person (or named independent) filling an Angular/dev/designer/PM/recruiter/CFO role, usually ongoing, often senior.

The instruction was hard: the user does not code. Do not apply them as Angular/dev. If only human seats: **ZERO**. That is the result.

## Pass bar (all required)

A listing counts only if **every** line is true:

1. The buyer is hiring a **team of agents** to finish **one discrete job**, not a human to occupy a seat.
2. The work is a **contract / one-job gig**, not a full-time or ongoing staff role.
3. The human on this side **does not have to code**. Angular, .NET, FastAPI, Framer-native, Webflow-custom-JS, and similar “you are the developer” seats fail.
4. Apply path is public (form or email). Login-only feeds are recorded as blocked, not as matches.
5. No application is sent from this file.

Fail any line → reject. If the board only has human seats → **ZERO**.

## What these two boards actually sell

| Board | What it is | What it is not |
|---|---|---|
| **Wellfound** | Startup job board (ex-AngelList Talent). Homepage copy: post jobs, deploy AI **sourcing** agents, or hire a recruiter. Candidates apply to **roles**. | Not a marketplace for buying a finished job from an agent team. Wellfound Reach / Autopilot are **employer** tools that source **human** candidates. |
| **Contra** | Freelance network for **independents** (human creatives/engineers). Clients browse people and portfolios, or post a job for a named contractor. Logged-out `/independent/opportunities` **302s to `/jobs`**. | Not a “hire an agent team” catalog. Discover `?view=jobs` still shows **people’s past projects**, not client briefs that hire agents. |

Neither product is shaped as “paste a one-job brief, pay a team of agents, get the artifact.” Both assume a human contractor or employee.

---

## Wellfound — opened, all human seats

Public jobs index: https://wellfound.com/jobs (HTTP 200, 2026-08-26 00:47 UTC).

Trending / role lists on that page and linked role pages are **seats**. Samples fetched in-window:

| Listing | URL | Why it fails |
|---|---|---|
| Senior Backend Engineer — AI Video Systems (Contract, Remote) — Overvak | https://wellfound.com/jobs/4570542-senior-backend-engineer-ai-video-systems-contract-remote | Contract, but a **senior engineer seat**. 5+ years Python/FastAPI, sit with the Founding Engineer, review PRs, own production code. User does not code. |
| Solutions Architect / Technical Lead (1099) — Friends From The City | listed on https://wellfound.com/jobs | 1099, still a **named human technical lead**. |
| Digital Product Lead (1099) — Friends From The City | listed on https://wellfound.com/jobs | 1099 product **seat**. |
| Product Manager (AI Agents) — Traba | listed on https://wellfound.com/jobs | PM **seat** for an AI-agents *product*, not a buyer hiring an agent team for one job. |
| Staff GNC Software Engineer — Ursa Major | listed on https://wellfound.com/jobs | Full-time engineering **seat**. |
| Senior Back End Engineer, Data and Cloud — LearnLux | listed on https://wellfound.com/jobs | Full-time engineering **seat**. |
| Angular Developer (Volunteer) — LifeBonder | https://wellfound.com/role/r/angular-developer | Angular **dev** (volunteer). Hard skip. |
| Full Stack Developer (Angular & Node JS) — Trixicon | same role page | Angular/Node **full-time seat**. Hard skip. |
| Senior Fullstack Developer (Angular/.Net) — journi | https://wellfound.com/jobs/4496944-senior-fullstack-developer-angular-net-uk-mainly-remote (also on the Angular role page) | Angular/.NET **full-time seat**, UK. Hard skip. Do not apply. |
| Full Stack .Net Developer (Contractor) — UpClear | https://wellfound.com/jobs/4167098-full-stack-net-developer-contractor-role | Contractor, still **Angular + C# human**, NYC on-site. Hard skip. |
| Senior Software Engineer - Frontend — awork | https://wellfound.com/jobs/4612599-senior-software-engineer-frontend | Full-time **Angular 20** seat, Hamburg. Hard skip. |
| Agentic Developer — Cleverstreet | https://wellfound.com/jobs/4505639-agentic-developer | Title has “agentic”; body is a **human** building multi-agent systems (full-time/contract engineer seat). |
| AI Architect (iGaming) — Neurons Lab | https://wellfound.com/jobs/4574463-ai-architect-igaming | Freelance contract, **0.5+ FTE human** with 7+ years AI/ML and iGaming math. Seat, not “one job for an agent team.” |
| Product Designer (Contract) — Clariti | https://wellfound.com/jobs/4557338-product-designer-contract | 4–6 month **designer seat**, $70–100/hr, through end of 2026. |
| FAA Part 107 Drone Pilot (Independent Contractor) | https://wellfound.com/jobs/4493410-faa-part-107-drone-pilot-independent-contractor | Human with an FAA certificate, local missions. Not an agent-team job. |
| Fractional CFO, Path to Full-Time — ArcHaus | https://wellfound.com/jobs/4463451-fractional-cfo-path-to-full-time | Human CFO **seat** (8–12 hrs/week → full-time). |
| Senior Technical Recruiter (Contract) — Coalition | https://wellfound.com/jobs/4335905-senior-technical-recruiter-contract | Human recruiter **seat**. |

Angular role index (fetched): https://wellfound.com/role/r/angular-developer — **41 results**, page 1 of 2. Every card is a human Angular/frontend/fullstack **seat** (or intern/volunteer). **Do not apply any of them.** The user does not code.

Wellfound `/role/c/contract` and `/role/contract` returned **404**. Contract filter is account-preference based (help.wellfound.com/article/1036). Public contract samples above were reached by search and by job URLs, not by a working public contract index.

---

## Contra — opened, all human independents

### Login wall

- https://contra.com/independent/opportunities → **HTTP 302 to `/jobs`** (2026-08-26 00:47 UTC). The live client-brief feed is not public without an Independent account.
- https://contra.com/jobs — marketing shell; no public list of open client briefs in the logged-out DOM.
- https://contra.com/discover?view=jobs — Discover “jobs” view is **portfolio projects by people**, not “hire this agent team for one job.”

Blocked ≠ empty. It also ≠ a match. Do not invent briefs behind the login.

### Hire-page “AI Agent Developers” — closed human seats

https://contra.com/hire/ai-agent-developers (fetched 2026-08-26):

- CTA is **Hire AI Agent Developers** → Discover **people**, and **Get hired** → `/jobs`.
- Sample client posts on that page: **CLOSED** “Founding Developer” (ongoing, $50/hr, 4 hrs/wk) and **CLOSED** “Senior AI Developer” (ongoing, $4,000–$5,000/mo). Both are **human seats**, both closed, both ongoing.

That page is “hire a freelance human who builds agents,” not “hire an agent team for one job.”

### One-time Contra gigs that still fail

Public opportunity URLs that opened (human freelancer, one deliverable or a named expert):

| Listing | URL | Why it fails |
|---|---|---|
| Webflow Developer Needed for Digi Hotshot | https://contra.com/opportunity/l3LEoQRB-webflow-developer-needed-for-digi-hotshot | Human Webflow **dev** seat. Custom JS, Loom of Designer, AI-to-code-faster is a **tool** requirement for a human. Apply email is a human hiring a human. |
| Framer CMS expert to finalize ProjChecks.com | https://contra.com/opportunity/Mo63vk2P-framer-expert-needed-to-finalize-existing-consulting-website-not-a-redesign | One-time $1,000–$2,000, 1–2 weeks — still a **human Framer expert**. |
| Framer rebuild, 3 pages, pixel-perfect — Stilta | https://contra.com/opportunity/NlbvXmm6-framer-rebuild-from-existing-figma-make-design-3-pages-identical-match | One-time coding/design seat. User does not code. |
| Freelance Web Developer, eSIM.tech, Framer | https://contra.com/opportunity/RmvLEoE6-freelance-web-developer-for-corporate-telecom-website-in-framer | Human web **developer**. |
| Framer Developer/Designer — agency site | https://contra.com/opportunity/cZ2bcRPO-framer-developerdesigner-needed-to-complete-agency-website | Human designer/dev. |
| B2B email copywriter | https://contra.com/opportunity/v36P6QAX-freelance-b2-b-email-copywriter-outbound-and-nurture-sequences | Human copywriter **seat**. |
| Copywriter, professional-services content | https://contra.com/opportunity/koQoYlUN-freelance-copywriter-for-professional-services-content | Human copywriter **seat**. |
| Environmental designer, JCK Las Vegas booth | https://contra.com/opportunity/XRFQkRWR-urgent-environmental-designer-who-thinks-in-surfaces-not-pages-luxury-jewelry-booth-jck-las-vegas-2026 | Human environmental designer; path to **ongoing**. |
| Featured coding jobs (collection) | https://contra.com/featured-jobs/freelance-coding-jobs | Cards include “WordPress Developer…”, “3D Web Developer…”, “Freelance Web Designer/Developer (Project-Based)” — all **human coder** gigs. Hard skip. |

One-time + fixed price is **not** enough. The buyer is still hiring a **person** with a craft (Framer, Webflow, copy, booth design).

### Near-miss that is the wrong direction

https://contra.com/community/WU04sLk8-hire-top-ai-engineering-team — community post (published 2026-03-08, last modified 2026-08-18). A **freelancer advertising** SajiCode (“17 specialized agents”). That is supply of an agent-tool product, not a client posting “hire this team for one job.” Zero comments, zero likes. Not a gig.

### Contra Labs

https://contralabs.com/jobs (page `published` 2026-08-25 21:28 UTC). Pays humans (designers, engineers, prompt writers, etc.) up to $100/hr for **taste / eval** briefs. Application wants a video, portfolio, and a short evaluation. That is a **human expert network**, not a buyer hiring an agent team for one job. Also fails the “user does not code” bar for any engineer track.

---

## Explicit non-applies

Do **not** apply, email, or pitch on any of the following from this sweep:

- Any Wellfound Angular / frontend / fullstack / backend / “agentic developer” / AI architect role.
- journi Angular/.NET, awork Angular 20, UpClear Angular+C#, Trixicon Angular+Node, LifeBonder Angular volunteer.
- Overvak senior backend contract.
- Any Contra Webflow / Framer / WordPress / “freelance coding” independent seat.
- Contra Labs engineer or designer network (human eval labor).
- SajiCode community post (not a client brief).

The user does not code. Pretending they are an Angular/dev independent would be a false application.

---

## Source log

| When (UTC) | URL | Result |
|---|---|---|
| 00:47 | https://wellfound.com/jobs | 200. Trending jobs are human seats. |
| 00:47 | https://wellfound.com/role/c/contract | 404 |
| 00:47 | https://wellfound.com/role/contract | 404 |
| 00:47 | https://wellfound.com/role/r/angular-developer | 200. 41 Angular/dev **seats**. All rejected. |
| 00:47 | https://wellfound.com/jobs/4570542-senior-backend-engineer-ai-video-systems-contract-remote | 200. Senior backend **seat**. |
| 00:47 | https://contra.com/independent/opportunities | **302 → /jobs** (login). |
| 00:47 | https://contra.com/jobs | 200 marketing shell, no public brief list. |
| 00:46 | https://contra.com/discover?view=jobs | 200. Portfolio grid, not client briefs. |
| 00:46 | https://contra.com/discover?view=jobs&roles=AI+Agent+Developer | 200. People/projects, not agent-team gigs. |
| 00:46 | https://contra.com/hire/ai-agent-developers | 200. CLOSED human Founding/Senior AI **seats**. |
| 00:47 | https://contra.com/featured-jobs/freelance-coding-jobs | 200. Human coding gigs. |
| 00:47 | https://contra.com/community/WU04sLk8-hire-top-ai-engineering-team | 200. Freelancer ad, not a job. |
| 00:47 | https://contralabs.com/jobs | 200. Human taste/eval network. |
| 00:47 | https://contra.com/features/find-freelance-jobs | 200. Confirms Opportunities tab needs signup. |

## What would have counted

A public brief that says, in substance: pay a **team of agents** to complete **this one job** (artifact, deadline, price), with no requirement that a human occupy an Angular/dev/PM/designer seat. None appeared on Wellfound or Contra in this window.

Re-sweep only if a new public, login-free feed of client briefs shows up. Do not treat Discover portfolios or Angular role indexes as that feed.
