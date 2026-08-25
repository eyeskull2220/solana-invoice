# Listing research (week of 2026-08-25)

Research only. Nothing in this file was posted. No Solana pay address is included because none exists yet. X/Twitter was not used.

**Live URLs (do not invent others):**

- Hub: https://treasury-tools.surge.sh/
- Invoice: https://solana-invoice-treasury.surge.sh/
- CSV Cleaner: https://csv-cleaner-treasury.surge.sh/
- Form to Email: https://form-to-email-treasury.surge.sh/
- RSS to Webhook: https://rss-to-webhook-treasury.surge.sh/

**Accounts we can actually use this week:** GitHub `eyeskull2220` and Gmail `sasha.de.vree.rene@gmail.com`. Indie Hackers, Hacker News Show HN, and the Solana Forum are login-walled in our browser. Origin is missing. Official Solana ecosystem submit requires X/Twitter.

**Public GitHub repo today:** only https://github.com/eyeskull2220/solana-invoice (no `LICENSE` file yet). The other four live pages do not have public repos.

---

## 1. Tiny Tool Town

| Field | Value |
| --- | --- |
| Site | https://www.tinytooltown.com/ |
| Submit URL | https://github.com/shanselman/TinyToolTown/issues/new?template=submit-tool.yml |
| How | GitHub issue form (or a PR adding `src/content/tools/<slug>.md`) |
| GitHub enough? | **Yes.** Gmail is not needed. |
| Phantom / X? | Not asked. |

**What to post:** one GitHub issue per tool, using their form. Required fields: tool name, one-line tagline, a few sentences, GitHub repo URL, author name, GitHub username (`eyeskull2220`), tags. Optional: demo URL (the matching `*.surge.sh` page), thumbnail, license, language (`HTML` / `JavaScript`). You must tick:

- This tool is free and open source
- This tool is not enterprise software or paid SaaS
- The GitHub repo is public and the tool works

Automation then checks that the repo exists, is public, has a `README.md`, and has an open-source license file. Maintainers label `approved`; the site republishes from GitHub.

Verified this week: new `[Tool]` issues were opened on 2026-08-24 and 2026-08-25.

**Catch:**

- The checklist is a hard gate. The hub currently shows **9 USDC / 49 USDC** prices. If those stay, you cannot honestly submit. Tiny Tool Town rejects paid SaaS and “anything with a pricing page.”
- Only `solana-invoice` has a public GitHub repo. CSV Cleaner, Form to Email, and RSS to Webhook each need their own public repo before a listing.
- `solana-invoice` still has **no `LICENSE` file**. Triage will fail until one is added (MIT is what they suggest).
- One GitHub repo = one listing. Do not try to list the whole hub from the invoice repo.
- Do not invent a pay address to “complete” the product page for this directory.

If you list invoice at all, pitch it as a tiny offline HTML invoice generator, demo at https://solana-invoice-treasury.surge.sh/, and only after the repo is clearly free + licensed.

---

## 2. OSSDrop

| Field | Value |
| --- | --- |
| Site | https://ossdrop.com/ |
| Submit URL | https://github.com/OSSDrop/OSSDrop (see [CONTRIBUTING.md](https://github.com/OSSDrop/OSSDrop/blob/main/CONTRIBUTING.md)) |
| How | GitHub pull request: add one JSON object to `data/tools.json`. Do **not** edit `README.md` (it is generated). |
| GitHub enough? | **Yes.** Self-submissions are encouraged. Gmail is not needed. |
| Phantom / X? | Not asked. |

**What to post:** one PR per tool. Shape:

```json
{
  "name": "Solana Invoice",
  "repo": "eyeskull2220/solana-invoice",
  "homepage": "https://solana-invoice-treasury.surge.sh/",
  "category": "finance-business",
  "description": "Offline HTML invoice generator: type amount, address, and optional memo, then download a client-ready file.",
  "license": "MIT",
  "added": "2026-08-25"
}
```

Keep `description` to **140 characters or less** (CI rejects longer). No hype, no emoji, no star counts. Category slugs that fit later tools: `finance-business` (invoice), `productivity` (CSV cleaner), `communication-social` (form-to-email), `automation-iot` (RSS to webhook). Use today’s date for `added`.

Verified this week: they merged community “drop your tool” PRs on 2026-08-17 and 2026-08-18.

**Catch:**

- Must be **open source**: public repo **and** an OSI-approved license that matches the `license` field. Same missing-`LICENSE` problem as Tiny Tool Town.
- **Paywalled-core tools are rejected.** USDC prices on the hub will get a “no.”
- One tool per PR. Four extra live pages without repos cannot be dropped yet.
- Listing is a GitHub JSON row plus ossdrop.com; claiming extra screenshots later is optional and is **not** required to get on the list.
- Do not invent a Solana address for the homepage or the JSON.

---

## 3. Console.dev (email pitch)

| Field | Value |
| --- | --- |
| Site | https://console.dev/ |
| Criteria | https://console.dev/selection-criteria |
| Submit URL | Email **hello@console.dev** (that is the published submit path; `/submissions/` 404s) |
| How | One plain email from Gmail. No directory account. |
| Gmail enough? | **Yes.** Send from `sasha.de.vree.rene@gmail.com`. GitHub is optional (link the public invoice repo if you want). |
| Phantom / X? | Not asked. They review commercial and open-source tools. |

**What to post:** a short editorial pitch, not a wallet, not a tweet. Three tight paragraphs plus working demo URLs that do not require signup:

1. What it is in one sentence (hub of tiny HTML tools; invoice / CSV / form-to-email / RSS-to-webhook).
2. Who it is for (freelancers and indie builders who want a client-ready invoice or a one-file utility, no account).
3. The unusual bit: each tool is a single static page on Surge, no wallet lives on the pages, pay address is pending so nobody should send funds.

Attach the five live URLs above. Mention https://github.com/eyeskull2220/solana-invoice as the only public source repo. Do **not** invent a pay address. Do **not** CC an X handle.

They publish a Thursday newsletter. A pitch sent this week can be reviewed this week; a feature is **not** guaranteed this Thursday.

**Catch:**

- Editorial, not a directory form. They pick 2–3 tools a week against a published bar: developer as primary user, self-service, fits a regular toolchain, quality, docs, maintenance.
- Invoice-for-clients is a stretch vs their usual CLI/library set. CSV Cleaner, Form to Email, and RSS to Webhook are closer to “devtools” than the invoice page.
- Reviews include a public “what we don’t like” section. Pitch only if that is acceptable.
- No published SLA. Similar pitches are often answered in weeks, not hours.
- The old `https://console.dev/submissions/` form is gone (404 as of 2026-08-25). Use email only.

---

## Checked and skipped (so we do not retry them this week)

| Place | Why not this week |
| --- | --- |
| Indie Hackers, HN Show HN, Solana Forum | Login-walled in our browser. |
| X / Twitter | Out of scope. |
| Origin | Namespace missing. |
| solana.com/ecosystem | Submit flow requires an official Twitter account. |
| tiny-helpers.dev | Contributions closed; PRs disabled because of AI-slop submissions. |
| SaaSHub | Publicly rejects products on free subdomains (`*.vercel.com` examples; Surge is the same class). |
| csjcode/awesome-solana | Maintainer is not adding new project links unless they already have ecosystem traction. |
| helius-labs/solana-awesome | Open “add my project” PRs sitting unmerged for months. |
| 1000.tools | Paid listing + account (`$1` then `$5.99/month`). |
| Product Hunt | Typical launch path uses X/Twitter or a full Product Hunt profile; skipped. |

---

## Practical order if we later get a green light to post

Do not post from this research PR.

1. Add a real OSI `LICENSE` (and a README screenshot) to `eyeskull2220/solana-invoice` **only if** the tools will stay free to use. Without that, Tiny Tool Town and OSSDrop will bounce.
2. GitHub issue to Tiny Tool Town for invoice only.
3. GitHub PR to OSSDrop for invoice only (`finance-business`).
4. One Gmail to `hello@console.dev` covering the hub + all five live URLs, no pay address.

CSV Cleaner, Form to Email, and RSS to Webhook wait until each has its own public repo (and, for 1–2, a license).
