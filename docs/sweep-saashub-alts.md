# SaaSHub alternatives that accept Surge URLs

Sweep date: **2026-08-26**.

**HARD constraint:** SaaSHub was **not** resubmitted. The live submit page still bans free subdomains. This file records alternatives, a PII scan of the live Surge pages, and one no-login listing that accepted `*.surge.sh`.

Product URL used everywhere below: [https://treasury-tools.surge.sh/](https://treasury-tools.surge.sh/)

---

## Why SaaSHub is out

Checked (read-only) on 2026-08-26: [https://www.saashub.com/services/submit/](https://www.saashub.com/services/submit/)

Still listed as rejected:

- Products using free subdomains (examples on the page: `my-cool-app.vercel.com`, `myproduct.saasify.com`).
- Waitlist-only landing pages, unreleased products, agencies, non-English products.

`*.surge.sh` is the same class of free host as those examples. The Website URL field was **not** filled. The Continue button was **not** clicked.

SaaSHub also wants an email on the product’s own domain for verification priority. The live catalog is on Surge, not a custom domain.

---

## PII scan (live Surge, 2026-08-26)

Scanned HTML of:

- [https://treasury-tools.surge.sh/](https://treasury-tools.surge.sh/)
- [https://solana-invoice-treasury.surge.sh/](https://solana-invoice-treasury.surge.sh/)
- [https://csv-cleaner-treasury.surge.sh/](https://csv-cleaner-treasury.surge.sh/)
- [https://form-to-email-treasury.surge.sh/](https://form-to-email-treasury.surge.sh/)
- [https://rss-to-webhook-treasury.surge.sh/](https://rss-to-webhook-treasury.surge.sh/)

| Check | Result |
| --- | --- |
| Personal emails | None. Form-to-email uses placeholder `you@studio.example` only. |
| Phone numbers / `tel:` | None. |
| Government IDs, street addresses, names | None. |
| Wallet / pay address on live Surge | Invoice page still uses `ADDRESS_PENDING` / `TREASURY_SOLANA_USDC_ADDRESS` placeholders. Catalog HTML had no base58 pay address. |
| USDC mint | Public SPL mint id appears in invoice markup (not personal data). |

This sweep file itself contains **no** contact mailbox, **no** pay address, and **no** personal name. Directory mail used the existing listing mailbox and is omitted here on purpose.

---

## One submission (no-login + accepts Surge)

### CurlShip — submitted once

| Field | Value |
| --- | --- |
| Site | [https://curlship.com/](https://curlship.com/) |
| Why it is a SaaSHub alternative | Public SaaS/product directory with instant listings. Terms do **not** ban free subdomains. |
| Login | **None.** `POST /api/submit` (also a paste form on the homepage). |
| Surge evidence | Directory already listed other `*.surge.sh` products before this sweep (`signal-gradient-studio.surge.sh`, `hirethomas-ai-ops.surge.sh`) plus `*.vercel.app` and `*.github.io`. Terms reject aggregators, blocklisted hosts, and private IPs — not Surge. |
| Payload | Catalog URL only. OG title/description scraped from the live page. Free tier. No badge added to the catalog. |
| Result | **201 Listed.** Live page: [https://curlship.com/l/2592](https://curlship.com/l/2592) |
| API check | `GET https://curlship.com/api/listing/2592` → `ok: true`, `url: https://treasury-tools.surge.sh/`, `tier: free`, title `Treasury tools`, description `Small offline tools billed in USDC on Solana.` |
| Outbound link | Nofollow until a CurlShip badge is on the catalog ([badge guide](https://curlship.com/badge)). Not done in this sweep. |
| Not done | No second CurlShip POST. No paid upgrade. No SaaSHub POST. |

Terms note “one listing per root domain,” but two distinct `*.surge.sh` hosts were already live, so hostname (not the shared `surge.sh` registrable domain) is what they enforce in practice.

---

## Alternatives checked (not submitted this sweep)

Closest SaaSHub-shaped directories: alternatives/comparison catalogs. Launch platforms (Product Hunt, BetaList, Startup Buffer) are out of this sweep’s one-shot rule.

| Directory | Submit path | Login? | Accepts `*.surge.sh`? | Action |
| --- | --- | --- | --- | --- |
| **AlternativeTo** | [FAQ: Suggest new application](https://alternativeto.net/faq/) (behind account). Cloudflare challenge in this agent. | Yes (email verify before new apps) | **Likely yes.** No published free-subdomain ban. The hoster [surge.sh](https://alternativeto.net/software/surge-sh/) is itself listed. Not proven for a `*.surge.sh` *app* URL without an account. | Not submitted (login). |
| **Alternative.me** | [How to submit software](https://alternative.me/how-to/submit-software/) | Yes | Unpublished. No free-subdomain ban on the how-to page. | Not submitted (login). |
| **directree** | [https://www.directree.io/submit](https://www.directree.io/submit) — paste URL, crawl in ~30s | Yes (“Sign in to continue”) | Unpublished. Any web product with a public URL is eligible; no subdomain ban on the docs. | Not submitted (login). |
| **Tulimoa** | [https://tulimoa.com/saas](https://tulimoa.com/saas) — name, URL, category, 300-char description | Yes (magic link / Google) | Unpublished. No free-subdomain ban on the SaaS page. | Not submitted (login). |
| **SaaS Cubes** | [https://saascubes.com/submit](https://saascubes.com/submit) — Product URL field visible | Form visible without login; nav still has Log in / Sign up. Later steps not completed. | Unpublished. Did not finish the wizard (one-shot already used on CurlShip). | Not submitted. |
| **SaaSworthy** | [https://www.saasworthy.com/offerings](https://www.saasworthy.com/offerings) vendor inquiry | Public inquiry, then vendor-portal email. Asks **phone** + business email. | Unpublished. Typical B2B listing, not a URL-only accept test. | Not submitted (PII-heavy form). |
| **SoftwareSuggest** | [https://www.softwaresuggest.com/vendors](https://www.softwaresuggest.com/vendors) | Vendor signup. **Rejects Gmail / Outlook / Hotmail.** | Unpublished. | Not submitted (consumer mail blocked). |
| **GoodFirms** | Vendor “List Software” (sign in) | Yes | Unpublished. B2B firm/software profile, HQ/location fields. | Not submitted (login). |
| **G2** | [https://www.g2.com/products/new](https://www.g2.com/products/new) / [sell.g2.com](https://sell.g2.com/create-a-profile) | Yes. Work email on the product domain. Research rules: seller needs a **unique web domain**. | **Unlikely.** Shared `surge.sh` is not a unique vendor domain. | Not submitted. |
| **OpenAlternative** | [https://openalternative.co/submit](https://openalternative.co/submit) | Yes | N/A — curated **open-source alternatives to proprietary SaaS**, paid skip-queue packages. | Not submitted (account + OSS mismatch). |
| **GetApp / Crozdesk / Capterra** | Vendor portals | Yes | Sibling Gartner-style catalogs; not exercised here. | Left to other sweeps. |

---

## Already done elsewhere (do not duplicate)

Not part of this sweep’s POST, recorded so we do not pile on:

- Launching Next — confirmation mail already in the listing inbox (queue, 2–4 months).
- Console.dev — editorial email already sent.

Those are launch/newsletter surfaces, not SaaSHub-style alternatives catalogs.

---

## Practical next steps (not done here)

1. Keep SaaSHub off the list until there is a **custom domain** (not `*.surge.sh`).
2. Optional: add the CurlShip badge to the catalog if a dofollow outbound link is wanted ([https://curlship.com/badge](https://curlship.com/badge)).
3. When an AlternativeTo or directree account exists, those are the next closest “alternatives directory” fits; both look hostname-tolerant, both need login.
4. G2 / SoftwareSuggest / SaaSworthy wait on a unique domain and a same-domain mailbox.

---

## PII scan of this file

Grep target before commit: mailboxes, phone numbers, base58 pay addresses, street addresses, personal names.

Expected hits: public product URLs, CurlShip listing URL, placeholder `you@studio.example` (described, not a real inbox), SaaSHub’s own example hosts.
