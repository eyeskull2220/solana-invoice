# Sweep: Codementor requests and similar live Q&A-for-pay

**Date verified:** 2026-08-26 (UTC; fetch window ~00:43–00:49)  
**Scope:** public, no-login inventory of Codementor open requests and similar paid Q&A / live-help boards that a **team can fulfill without the user on camera**.  
**Not an application.** Nothing was posted, bid, messaged, or booked.

## Constraints (hard)

| Rule | How it was applied |
|---|---|
| User does not code | Do not treat “pair as the user” as a path. |
| No live pair as them | Live 1:1 / screen-share sessions that require the named user are out. |
| Team can work off-camera | Only async text, written code review, or freelance delivery (no face, no voice of the user). |
| If login required: **ZERO** | Do not sign in. If the request list is behind auth, inventory for that board is **0**. |
| If live-video required: **ZERO** | Do not join calls. Camera/screen-share marketplaces are **0** for tonight. |
| PII scan | No requester names, emails, phones, tutor handles, or student-identifying assignment text in this file. |
| No secrets | No passwords, API keys, session cookies, or wallet material. |

## Verdict

**Takeable requests tonight: 0.**

Codementor’s open-request queue is behind Arc login. Every similar live Q&A-for-pay board that still exists either (a) hides the work behind login or an expert application, (b) is live video/audio, (c) is dead / shut down, or (d) is already-answered SEO homework, not an open bid.

There is **no public grab-and-go list** of paid coding questions the team can answer today without an account.

---

## Codementor (primary)

Product (public pages, 2026-08-26): on-demand marketplace for **live 1:1 help**, long-term mentorship, **freelance jobs**, and **code reviews**. Mentors are advertised as 5000+ vetted experts. Apply page: https://www.codementor.io/mentor/apply

Official request types (support, no login needed to read):

1. **Get live help** — live 1:1 session (one-off or long-term mentorship). Screen sharing, video, and text. **Camera / live pair.** Out under hard rules, even after a future login.
2. **Post a freelance job** — hire a mentor to complete a job. **Could** be off-camera team work *after* a mentor account exists. Queue is not public.
3. **Get code reviewed** — written review. **Could** be off-camera team work *after* a mentor account exists. Queue is not public.
4. **Hire Arc Developers** — full-time / 40+ hour contracts. Not a Q&A request board.

### What was actually visible without login

| URL | HTTP | What you get | Takeable requests |
|---|---|---|---|
| https://www.codementor.io/ | 200 | Marketing: “Get live 1:1 coding help”. Log in / Sign up / Become a mentor. | 0 |
| https://www.codementor.io/mentor/apply | 200 | Mentor apply. Two tracks: live 1:1 mentorship **and** freelance projects. “Become a Codementor Now” is a signup CTA. | 0 |
| https://www.codementor.io/m/dashboard/open-requests | 200 → **redirect** `https://arc.dev/login?service=codementor&to=…open-requests` | Arc login: “Log in to continue to Codementor”. Same account for Codementor and Arc. | **0 (login)** |
| https://www.codementor.io/login | 200 → `https://arc.dev/login?service=codementor` | Same login wall. | 0 |
| https://www.codementor.io/freelance-jobs | **404** | Path does not exist. | 0 |
| https://www.codementor.io/freelance/javascript (and `/python`, `/full-stack`, …) | 200 | **Mentor directory** (“Hire Top Freelance … Developers”, August 2026). How-to for *clients* posting a request. No open job list. | 0 |
| https://www.codementor.io/javascript-experts (and `/full-stack-experts`, …) | 200 | Client-side “get expert help in 6 minutes”: post a request → chat → live session or job. Expert cards, not incoming requests. | 0 |
| https://www.codementor.io/community | 200 | Public blog / “Learn to Code” posts (React vs Vue, clone tutorials, etc.). **Not paid requests.** | 0 |
| https://www.codementor.io/community/topics | 404 | | 0 |
| https://support.codementor.io/en/articles/4218305 | 200 | How Codementor works (live 1:1, freelance, code review). | — |
| https://support.codementor.io/en/articles/4219841 | 200 | “POST REQUEST” is on the **Dashboard** (auth). | — |
| https://support.codementor.io/en/articles/4224321 | 200 | Mentors are told to check **notifications and open requests** (auth). | — |
| https://www.codementor.io/terms | 200 | Featured Request: live 1:1, freelance jobs, code reviews, long-term mentorship. Featured list is **provided to mentors** (auth). | 0 |

**Codementor inventory: ZERO.** The only page that would list live requests (`/m/dashboard/open-requests`) is an Arc sign-in wall. No login was performed.

Live 1:1 on Codementor would also fail the camera / “no live pair as them” rule even if the queue were public.

---

## Similar live Q&A-for-pay (same hard rules)

### Still online, but ZERO takeable requests tonight

| Board | Public URL checked | HTTP | Model | Why ZERO tonight |
|---|---|---|---|---|
| **JustAnswer — Computer Programming** | https://www.justanswer.com/computer-programming/ | 200 | Paid async text (and optional phone) with verified experts. Category page said programmers were online. | Answering requires expert application + login. “Recent questions” listing `…/computer-programming/recent.html` returned **403**. Indexed question pages also **403** from this fetch. Expert apply: https://era.justanswer.com/ (200) — identity / credential check, first+last name, email, phone on the form. **Not filled.** |
| **StudyPool programming Q&A** | https://www.studypool.com/programming-homework-help | 200 | Students post a budget; tutors bid. Messenger Q&A plus **video tutoring**. | Public list is **already-answered** teasers. Banner: “Private questions are not visible.” Bidding / taking a question requires Login / Sign Up / Become a Tutor. **Academic-integrity risk** (university homework). See exclusion below. |
| **MentorCruise** | https://mentorcruise.com/mentor/ | 200 | Mentors list packages; mentees book. Official copy: chat, live, or both; some relationships are text-only. | No public incoming-request board. Becoming a mentor is an application (they claim a low acceptance rate). Bookings are not visible logged-out. Live calls are common. |
| **Wyzant** | https://www.wyzant.com/ | 200 | Hourly 1:1 tutoring. `/tutor` redirected to **login**. | Live lessons. Tutor approval + login. **Video.** |
| **Experts Exchange** | https://go.experts-exchange.com/ | 200 | Private paid Q&A community for tech people (points / conversation). Question search `experts-exchange.com/questions` → **403**. | Login required to see questions. |
| **Code911** (`code911.dev`) | https://code911.dev/ , `/developers`, `/pricing`, `/create-request`, `/signup` | 200 each, ~10 KB | Marketing copy (search index): live matching, chat **or call**, pay-per-minute. | Fetched HTML is a **Lovable SPA stub** (`<title>help-mate-coders</title>`, “Lovable Generated Project”). No public request list in the document. Signup would be login. Live call is video/voice. |
| **Clarity.fm** | https://clarity.fm/ and `/browse` | 200 | On-demand **phone** advice; expert sets a per-minute rate. | Live audio of the user. `/browse` did not return a usable expert/request list (JS “Loading…”). |
| **ADPList** | https://adplist.org/ | 200 | Mentorship marketplace. | Sessions are typically live video. **Not for-pay for the mentor** (free mentoring). Out of scope. |
| **Bartleby Expert Q&A** | https://www.bartleby.com/ | 200 | Student homework Q&A / textbook solutions. Expert portal historically at experts.bartleby.com. | Student-facing site is login/trial. `https://experts.bartleby.com/` → **404** (nginx) in this window. No public expert question queue. Homework-for-pay: academic-integrity exclusion. |
| **Fiverr programming** | https://www.fiverr.com/categories/programming-tech | **403** | Gig marketplace; buyer requests are logged-in. | Cloudflare/block. Would be login anyway. |
| **Superprof programming** | https://www.superprof.com/lessons/programming.html | **403** | Tutoring, usually live. | Blocked. Would be video + login. |
| **PrestoExperts** | https://www.prestoexperts.com/ | timeout | Time-based expert chat (secondary sources). | Unreachable this window. Not inventoried. |

### Dead or closed (do not hunt)

| Board | Status on 2026-08-26 | Source |
|---|---|---|
| **Chegg Q&A Expert** | Expert Q&A operations ended **2026-03-18**. `/expertqa` and `/tutors` → **404**. Study product still exists for students (`/study`, 200, compressed). | Secondary writeups citing Chegg India’s Q&A support portal; Chegg Q1 2026 earnings still a student-subscription company: https://investor.chegg.com/Press-Releases/press-release-details/2026/Chegg-Reports-First-Quarter-2026-Earnings/default.aspx |
| **HackHands** | Sunset; `hackhands.com` → Pluralsight (`/hackhands` **404**). | https://hackhands.com/ redirect target |
| **AirPair** | Deadpooled (live video pairing). Homepage **403**. | Tracxn 2026 profile; fetch |
| **Quora Partner Program** | Ended (2022–2023). Does not pay for answers. | Not re-fetched; recorded as closed so it is not “missed.” |

---

## What the team *could* do later (not tonight)

These are **not** open requests. They are the only Codementor-like shapes that could be off-camera **after** a human creates an account. Listed so the next pass does not re-discover them as “live tonight.”

1. **Codementor freelance jobs + code reviews** — async delivery, no user on camera. Blocked on: Arc/Codementor mentor apply, vetting, then the auth-only open-request dashboard. Live 1:1 stays out.
2. **JustAnswer Computer / Programming** — async written answers; phone optional (skip phone). Blocked on: expert application, third-party credential check, login. PII-heavy apply form (legal name, email, phone).
3. **MentorCruise text-only packages** — possible if a mentor profile is accepted and the package is chat-only. Blocked on: apply + wait. No public request firehose.

Do **not** treat university homework boards (StudyPool, Bartleby, leftover Chegg-style Q&A) as team work. That is graded-assignment answering, not product Q&A.

---

## Adjacent (not live Q&A-for-pay)

Fetched so they are not confused with Codementor request queues. These are **AI-training / expert-network apply pages**, not a public list of a stranger’s live coding question.

| Site | Fetch | Note |
|---|---|---|
| https://www.mercor.com/ | 200 | Homepage shows sample roles and “View all roles”. `work.mercor.com` (200) is a thin apply shell. Work is contracted expert tasks, not a live help queue. Applying is login. |
| https://www.dataannotation.tech/ | 200 | Public role cards (including coding). “Sign in / Apply Now.” Assessment + account. Not a Codementor request board. |

---

## PII scan (this file)

Scanned before commit:

- **No** requester, student, or client names.
- **No** tutor / expert display names copied from StudyPool or JustAnswer directories.
- **No** emails, phone numbers, or physical addresses.
- **No** student assignment bodies, screenshots, or course-section identifiers.
- **No** passwords, cookies, API keys, or wallet addresses.
- University names appeared in StudyPool *already-answered* teasers; they are **not reproduced** here.
- JustAnswer apply form fields (name / email / phone) are mentioned only as the reason the apply path is PII-heavy — **no values**.

If a later pass logs in, strip the same classes from any copied request text before it hits git.

---

## Source log (2026-08-26 UTC)

Anonymous `curl -L` (browser UA). No cookies, no accounts.

| Resource | Status | Notes |
|---|---|---|
| `codementor.io/` | 200 | Marketing |
| `codementor.io/mentor/apply` | 200 | Apply CTA |
| `codementor.io/m/dashboard/open-requests` | 200 → Arc login | **Hard stop** |
| `codementor.io/login` | 200 → Arc login | |
| `codementor.io/freelance-jobs` | 404 | |
| `codementor.io/freelance/javascript` | 200 | Mentor directory, not jobs |
| `codementor.io/javascript-experts` | 200 | Client CTA |
| `codementor.io/full-stack-experts` | 200 | Client CTA |
| `codementor.io/community` | 200 | Blog, not requests |
| `codementor.io/community/topics` | 404 | |
| `codementor.io/terms` | 200 | Featured Request = mentor-side list |
| `support.codementor.io` articles 4218305, 4219841, 4224321 | 200 | Dashboard / POST REQUEST |
| `arc.dev/login?service=codementor` | 200 | Login wall |
| `justanswer.com/computer-programming/` | 200 | Category + expert directory |
| `justanswer.com/computer-programming/recent.html` | 403 | |
| `era.justanswer.com/` | 200 | Expert apply (not submitted) |
| `studypool.com/programming-homework-help` | 200 | Answered teasers; private hidden |
| `mentorcruise.com/mentor/` | 200 | Mentor apply marketing |
| `wyzant.com/` | 200 | Tutoring marketplace |
| `wyzant.com/tutor` | 200 → login | |
| `go.experts-exchange.com/` | 200 | Private community pitch |
| `experts-exchange.com/questions` | 403 | |
| `code911.dev` (home, developers, pricing, create-request, signup) | 200 | Lovable stub |
| `clarity.fm/`, `/browse` | 200 | JS shell |
| `adplist.org/` | 200 | Free mentoring |
| `bartleby.com/` | 200 | Student homework product |
| `experts.bartleby.com/` | 404 | |
| `chegg.com/study` | 200 | Student product |
| `chegg.com/expertqa`, `/tutors` | 404 | |
| `fiverr.com/categories/programming-tech` | 403 | |
| `superprof.com/lessons/programming.html` | 403 | |
| `prestoexperts.com/` | timeout | |
| `hackhands.com` | 404 on Pluralsight path | |
| `airpair.com/` | 403 | |
| `mercor.com/` | 200 | Adjacent |
| `work.mercor.com/` | 200 | Adjacent apply shell |
| `dataannotation.tech/` | 200 | Adjacent |

Search indexes still list some JustAnswer programming threads; those URLs returned **403** from this environment and were not copied.

---

## Bottom line

For 2026-08-26, **the team has nothing to pick up on Codementor or a Codementor-like board without logging in or going on camera.** The honest next step is not a second anonymous scrape. It is a human decision: either skip this channel, or (later) create a mentor/expert account **without** enabling live video, then re-sweep the auth-only freelance / code-review / written-Q&A queues only.
