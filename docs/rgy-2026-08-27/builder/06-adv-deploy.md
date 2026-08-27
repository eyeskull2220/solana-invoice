# 06 — Adversarial deploy / CI

**Seat:** Builder (attack research only)  
**Date:** 2026-08-27  
**Repo at write:** `eyeskull2220/solana-invoice` `main` `2170952`  
**Assumption:** deploy is a **bad layout**. Start from zero. Do not inherit a “we already ship” story.  
**This file does not publish.** No Surge. No DNS. No GitHub Pages. **No new connectors.**

Overall: **RED**. There is no honest Belgian shop deploy here. There is a leftover invoice toy in git, a swarm of Surge hosts that anyone with a token can overwrite, crawler `Disallow: /` on every live origin probed, and no `.be`. GitHub Actions is empty. Red/green does not exist.

---

## 0. What “deploy” is on this tree

| Layer | What exists on 2026-08-27 | Shop-grade? |
| --- | --- | --- |
| Git origin of truth | Public repo **`solana-invoice`**. Description: *“Solana Invoice — one HTML file, 9 USDC.”* Files on `main`: `index.html`, `catalog.html`, `solana-invoice.html`, `config.js`, `README.md`. **No** `robots.txt`. **No** `.github/`. **No** `CNAME`. | No. Leftover toy. |
| CI | GitHub Actions: **0 workflows, 0 runs**. Combined status on `main`: empty (`total_count: 0`). Rulesets: `[]`. Environments: **0**. Deployments API: **[]**. Pages: **404**. | No. Not even a lying green stamp. |
| Publish path | Manual `surge` to `*.surge.sh`. Not recorded in GitHub. Not gated by a check. Overwrite in place. | No. |
| Live hosts (probed) | At least **16** Surge origins, all `robots.txt` = `User-agent: *` / `Disallow: /`. | No. Invisible to search. |
| Belgian origin | `sovereignforge.be` / `www.sovereignforge.be`: **NXDOMAIN**. `treasury-tools.be`: **NXDOMAIN**. | No. |

If a teammate treats this leftover repo as “the shop” and `surge`s from `main`, they publish a **9 / 49 USDC English catalog** and a **9 USDC paywall**, not a Dutch EUR OFFERTE. If they `surge` HTML that is **not** on `main`, git and live diverge and nobody has a SHA to roll back to. Both happened.

---

## 1. Attack board (named)

These six attacks are the brief. Evidence is from this run (HTTP GET, `gh api`, DNS) plus the 2026-08-26 read-only PII scan on branch `cursor/pii-scan-surge-c7fb` (`docs/pii-scan-surge.md`), which already recorded `Disallow: /` and was **not** a publish gate.

| ID | Attack | Color | Lands today? |
| --- | --- | --- | --- |
| D1 | Surge with no check | **RED** | Yes |
| D2 | `robots` Disallow live | **RED** | Yes — all 16 probed hosts |
| D3 | `.be` not ready | **RED** | Yes — NXDOMAIN |
| D4 | Leftover repo `solana-invoice` treated as shop | **RED** | Yes — name, description, `main` files, README |
| D5 | No red/green deploy | **RED** | Yes — overwrite is the release |
| D6 | No inhouse CI | **RED** | Yes — 0 workflows |

No row is GREEN. Partial mitigations sit in **YELLOW** below. They do not make a shop.

---

## 2. RED

### D1 — Surge with no check

**Attack.** A laptop (or a cloud agent) with a Surge token runs `surge <dir> --domain <host>.surge.sh`. There is no required check, no SHA pin, no robots lint, no USDC-on-face lint, no PII lint, no “does this tree match this host?” lint. The previous HTML is gone. GitHub never sees a deployment.

**Evidence (this run).**

- Repo has **no** workflow, **no** `surge.json`, **no** publish script, **no** token-in-Actions (and this seat must not add one).
- GitHub `deployments`: empty array. `environments`: empty. Pages: not configured. The publish path is **outside** git.
- Live HTML **does not match** `main`:
  - README / `catalog.html` still advertise *Treasury tools* at https://treasury-tools.surge.sh/ billed in **USDC**.
  - Live `/` title on that host: **“SovereignForge — clubsite, inbox-ops, Peppol en menukaart voor clubs en KMO’s”** (`lang="nl"`, `canonical` = the Surge URL, `meta robots` = `index,follow`).
  - README still says Solana Invoice is *one HTML file, 9 USDC* at https://solana-invoice-treasury.surge.sh/.
  - Live `/` title there: **“Eén klus — €49 · OFFERTE”** (3027 bytes). Repo `solana-invoice.html` is 34267 bytes of English 9 USDC product. They are not the same file.
- PII scan 2026-08-26 was **read-only after publish**. Verdict PASS on secrets. It did not block a deploy. It is not CI.
- Reviewer rubric (open PR #112, 2026-08-27) already **FAIL**s live shop + kit hosts. That fail is a document. It is not a required check. A later `surge` can ignore it.

**What it does.** Anyone with the token can put USDC, a fake KBO, a FACTUUR stamp, or a real mailbox on a URL that secretaries already have. There is no red build to stop them. Drift is the default: shop HTML lives on Surge; leftover toy lives on GitHub.

**Do not “fix” by adding a hoster.** No Vercel, Netlify, Cloudflare Pages, GitHub Pages, or second Surge account from this seat. Connector freeze holds.

---

### D2 — `robots` Disallow live

**Attack.** Every public origin tells crawlers to stay out. A Belgian shop that cannot be found is not a shop. Flipping to `Allow: /` without an EUR face **in git that matches live** would index the wrong product.

**Evidence (HTTP 200, body exact, 2026-08-27).** Every host below serves:

```
User-agent: *
Disallow: /
```

| Host | `robots.txt` |
| --- | --- |
| https://treasury-tools.surge.sh/robots.txt | Disallow `/` |
| https://sovereignforge.surge.sh/robots.txt | Disallow `/` |
| https://solana-invoice-treasury.surge.sh/robots.txt | Disallow `/` |
| https://csv-cleaner-treasury.surge.sh/robots.txt | Disallow `/` |
| https://form-to-email-treasury.surge.sh/robots.txt | Disallow `/` |
| https://rss-to-webhook-treasury.surge.sh/robots.txt | Disallow `/` |
| https://club-site-kit-treasury.surge.sh/robots.txt | Disallow `/` |
| https://menu-kit-treasury.surge.sh/robots.txt | Disallow `/` |
| https://sponsor-kit-treasury.surge.sh/robots.txt | Disallow `/` |
| https://lid-kit-treasury.surge.sh/robots.txt | Disallow `/` |
| https://vakman-kit-treasury.surge.sh/robots.txt | Disallow `/` |
| https://inbox-ops-treasury.surge.sh/robots.txt | Disallow `/` |
| https://pipeline-treasury.surge.sh/robots.txt | Disallow `/` |
| https://peppol-chase-treasury.surge.sh/robots.txt | Disallow `/` |
| https://dual-invoice-treasury.surge.sh/robots.txt | Disallow `/` |
| https://peppol-ready-treasury.surge.sh/robots.txt | Disallow `/` |

**Contradiction on the would-be catalog host:** live https://treasury-tools.surge.sh/ HTML has `<meta name="robots" content="index,follow" />` **and** `robots.txt` `Disallow: /`. Crawlers that honor `robots.txt` will not index. The meta tag is theatre.

**Repo:** `main` has **no** `robots.txt`. Open PR #111 (`cursor/euro-shop-face-00e2`) adds `Allow: /` on a branch that is **not** live and **not** this leftover `main`. Shipping `Allow` onto current live Surge without matching EUR git is how you index USDC toys.

**What it does.** Search, club federation lists, and “type the name in DuckDuckGo” all miss. Meanwhile the same hosts are world-reachable over HTTPS to anyone who has the URL (mails, chat, screenshots). Disallow is not access control. It is “please don’t list us” on a product that is already the public face.

---

### D3 — `.be` not ready

**Attack.** Treat `*.surge.sh` as the Belgian shop origin. Secretaries, bestuur, and accountants do not. A `.be` that does not resolve is not “soon.” It is absent.

**Evidence (this run).**

| Name | Result |
| --- | --- |
| `sovereignforge.be` | DNS: name or service not known. `https://` curl 6. |
| `www.sovereignforge.be` | Same. |
| `treasury-tools.be` | Same. |
| `solana-invoice.be` | Same. |
| Live canonicals | `https://treasury-tools.surge.sh/`, `https://sovereignforge.surge.sh/` |

No A/AAAA. No HTTP redirect from `.be` to Surge. This seat does **not** register DNS, buy a domain, or add a registrar connector.

**What it does.** Every OFFERTE, mail footer, and “bekijk de site” link that uses Surge teaches the buyer that this is a file dump on a US static host, not a Kempen studio. Indexing (D2) cannot save a TLD that does not exist (D3).

---

### D4 — Leftover repo `solana-invoice` treated as shop

**Attack.** Cloud agents, PRs, and humans use **this** GitHub repo as the shop monorepo: kits under `tools/`, Dutch `shop/`, euro `index.html`, privacy, robots, pakketten. GitHub’s own card still says **Solana Invoice, 9 USDC**. `main` still *is* that toy.

**Evidence.**

- GitHub: `name=solana-invoice`, `description=Solana Invoice — one HTML file, 9 USDC. Offline invoice generator.`, `homepage=null`, `has_pages=false`.
- `main` `index.html` title: **“Solana Invoice — 9 USDC”**. Unlock paywall. Treasury address in `config.js`.
- `main` `catalog.html`: English “Treasury tools”, chips **9 USDC** / **49 USDC**, links to four Surge toys.
- README: live catalog URL + four 9/49 USDC tools. That README is a **lie relative to live** (D1) and a **shop-face violation** if treated as public copy (USDC on face).
- Open PRs dump week-scale Belgian kits, buyer lists, and a euro shop face **onto this leftover name**. Merge lottery does not rename the origin.
- Live https://sovereignforge.surge.sh/ is a chalkboard Dutch face **that is not in this `main` tree**. The shop HTML’s home is not git.

**What it does.** Reviewers, secretaries, and future CI all look at the wrong artefact. A green check on `solana-invoice` would certify the toy. A Surge publish from `main` would **downgrade** the live Dutch overwrite back to 9 USDC. Treating leftover as shop is how you ship the attack in D1 on purpose.

---

### D5 — No red/green deploy

**Attack.** There is one slot per hostname. Publish replaces it. There is no red (preview that must pass) and no green (production pinned to a git SHA). Rollback is “hope someone kept the old folder.”

**Evidence.**

- Surge: in-place overwrite. No GitHub environment `production` / `preview`.
- No Pages, so no `gh-pages` vs source split either (and this seat must not turn Pages on).
- Live vs git mismatch (D1) is the proof: production is **not** a SHA of `main`. There is no green that a reviewer can `git checkout`.
- Kit swarm (16+ hosts) means sixteen independent overwrites, not one shop with a canary.

**What it does.** Hide-the-coin, robots `Allow`, or a privacy page can land on one host and not the others. A bad publish has no second slot. “We rolled forward” is the only story, and it is not in git.

Red/green here does **not** mean “add Kubernetes.” It means: a preview host that is allowed to fail, and a production host that only receives a tree that passed named checks. That layout does not exist.

---

### D6 — No inhouse CI

**Attack.** PRs merge with zero checks. `main` moves. Someone Surges. The gap between merge and publish is unmeasured. The gap between publish and “did robots/USDC/PII/SHA pass?” is infinite because no job exists.

**Evidence.**

```
GET /repos/eyeskull2220/solana-invoice/actions/workflows  →  { "total_count": 0, "workflows": [] }
GET /repos/eyeskull2220/solana-invoice/actions/runs       →  total_count 0
GET /repos/eyeskull2220/solana-invoice/commits/main/status →  state pending, total_count 0, statuses []
GET /repos/eyeskull2220/solana-invoice/rulesets           →  []
```

No `.github/` on `main`. Kit PRs that contain `scan-pii.sh` still run only if a human runs them. Reviewer FAIL (#112) is a markdown file. It does not block merge.

**What it does.** Inhouse CI is the only honest gate that does not add a **new hoster**. This file does **not** add the YAML (sibling **Builder 14 CI**). Until that exists, “CI green” is a sentence with no referent.

---

## 3. YELLOW

Not shop-ready. Not nothing.

| Item | Why yellow, not green | Why yellow, not red-alone |
| --- | --- | --- |
| HTTPS 200 on Surge | Hosts exist; TLS works | Existence is not a shop. Disallow + no `.be` + drift remain. |
| PII scan 2026-08-26 PASS | No keys/seeds/mails on five hosts that day | After-the-fact, five hosts only, not a gate; live HTML has since moved. |
| Live `treasury-tools` HTML currently has **no** `USDC` / `Solana` string | Hide-the-coin happened **on the host** | Not in `main`. Next Surge from leftover git **puts USDC back**. |
| Live `solana-invoice-treasury` is €49 OFFERTE | Face improved vs 9 USDC toy | 3027-byte page is not the git product; still Disallow; still `.surge.sh`. |
| Open PR #111 `robots.txt` `Allow: /` | Someone wrote the later file | Not live. Must not `surge` it from this seat. |
| Reviewer #112 FAIL | Attack D2/D4 already named by another seat | Document ≠ check. |
| No GitHub Pages | Avoids a second accidental publish path | Absence of Pages is not a deploy. |
| Empty Actions | No fake “CI passed” badge | Also D6 RED. |
| Kit `scan-pii.sh` on some branches | Local script exists in kit PRs | Not required; not on `main`; not run on Surge. |

YELLOW items are **notes for later numbered seats** (12 deploy, 14 CI, 15 gate). They are not permission to publish.

---

## 4. GREEN

Green means “this is actually safe / intentionally true,” not “the shop is live.”

| Item | Green because |
| --- | --- |
| This run did not publish | No `surge`, no DNS write, no Pages enable. |
| No new connectors | No Vercel / Netlify / Cloudflare / registrar / extra Surge login from this seat. |
| 2026-08-26 leak-path probe | `.env`, `.git/HEAD`, `wallet.json`, `secrets.json`, source maps **404** on the five scanned hosts. Not a deploy, but the hosts were not serving a git directory. |
| Actions empty is honest | There is no green badge lying that tests ran. |
| Receive address is not a deploy secret | Solana USDC `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3` is public pay-to. Losing a Surge token is still **RED** (D1); the address itself is not the leak. |

There is **no** green row for “shop deploy,” “crawler allow,” “`.be`,” “git = live,” “red/green,” or “inhouse CI.”

---

## 5. Drift table (git leftover vs live overwrite)

This is D1 + D4 in one view. Do not reconcile by publishing from this PR.

| Surface | `main` (leftover) | Live Surge (this run) |
| --- | --- | --- |
| https://treasury-tools.surge.sh/ | README: “Treasury tools” catalog, USDC | Title SovereignForge clubsite/inbox/Peppol/menu, `lang=nl`, no USDC in HTML, **no** `/privacy.html` (404), meta `index,follow` vs robots Disallow |
| https://solana-invoice-treasury.surge.sh/ | 9 USDC pay + 34kB product HTML | Title *Eén klus — €49 · OFFERTE*, 3kB |
| https://sovereignforge.surge.sh/ | **Not in `main`** | Dutch bestuur voorstel; USDC still in HTML; `/privacy.html` 200; robots Disallow |
| Repo card | Solana Invoice, 9 USDC | n/a — GitHub still the leftover name |

---

## 6. What a later deploy would have to be (not this PR)

Order only. **Do not execute here.**

1. Stop treating `solana-invoice` `main` as the shop origin (D4). Shop HTML lives in a tree that is **named and described as the shop**, or this leftover stays a toy and Surge stops pretending.
2. Inhouse CI on **that** tree (D6 / Builder 14): fail on USDC/Solana/Phantom on shop face, fail on `Disallow: /` for the public shop origin, fail on invented KBO, fail on `FACTUUR` as stamp, fail if `robots.txt` missing.
3. Red host (preview Surge **or** local) must pass those checks. Green host receives **only** that SHA (D5). Overwrite-without-SHA stays forbidden.
4. `robots.txt` `Allow: /` **only** on the shop origin **after** EUR face is the git SHA that is live (D2). Do not Allow the 9 USDC leftover.
5. `.be` is an **operator** registrar act, not an agent connector (D3). Until NXDOMAIN clears, do not mail a Surge URL as “onze site.”
6. Still **no** new hoster without a written yes.

---

## 7. NOTES

- **Do not publish** from this file or its PR. No Surge token use. No DNS. No Pages.
- **No new connectors.** Surge is already the (bad) path. Do not add a second one “to get red/green.”
- **Do not flip live `robots.txt` to Allow** until D4+D1 are false: git SHA == live shop, EUR face, no leftover 9 USDC catalog.
- **Do not Surge `main`.** It would restore the USDC toy over the Dutch overwrite.
- **Do not treat Disallow as a privacy control.** Hosts are public. PII scan PASS ≠ shop PASS.
- **Do not invent a KBO or FACTUUR** to make the shop “feel live.”
- Sibling seats: **12 deploy** (layout), **14 CI** (YAML), **15 gate** (go/no-go). This **06** is the attack. It does not implement them.
- Operator Eyeskull2220 (Geel) is **not** the freelancer and is **not** the on-call host. This page does not ask them to debug Surge.
- Gmail / Linear / Kraken / Phantom / X / Stripe / Circle were not used to publish. Keep it that way.

---

## 8. What this run did / did not

| Did | Did not |
| --- | --- |
| GET robots + HTML on 16 Surge hosts | `surge` / republish / delete a host |
| `gh api` workflows, runs, status, pages, environments, deployments, rulesets | Enable Actions, Pages, or branch protection |
| DNS lookup `.be` names | Register or point a domain |
| Write this markdown | Edit `index.html`, `catalog.html`, kit HTML |
| Assume deploy is a bad layout from zero | Pretend hide-the-coin on Surge is a git release |

---

End of 06. Next Builder deploy work is a **later numbered file**, or nothing.
