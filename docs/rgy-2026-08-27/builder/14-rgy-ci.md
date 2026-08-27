# 14 — RGY CI (Builder in-house CI)

**Seat:** Builder / RGY 14 (CI)  
**Lens:** adversarial, then RGY  
**Date:** 2026-08-27  
**HEAD:** `2170952` (`Merge pull request #27 … treasury-address-9594`)  
**Verdict:** **RED**  
**This file does not implement.** It does not add a workflow. It does not add a paid CI product. It does not send mail. It does not invent a KBO.

In-house CI here means **GitHub Actions on this public repo** (`runs-on: ubuntu-latest`, `rg` / `curl` / `test`). That is free. Paid products (CodeRabbit CI, CircleCI, Codecov, Snyk paid, GitHub paid runners, third-party review bots) are **out**. A later Builder PR may add the three jobs below. This PR only names them.

---

## What was scored (from zero)

| Source | What it is |
| --- | --- |
| `main` @ `2170952` | Five files: `index.html`, `catalog.html`, `solana-invoice.html`, `config.js`, `README.md`. **No** `.github/`. **No** `robots.txt`. **No** `package.json`. **No** Makefile. **No** test runner. |
| GitHub checks | PR #112 head: **0 check runs**. Same for other open Builder PRs sampled. Nothing gates merge. |
| Live shop | `https://sovereignforge.surge.sh/robots.txt` → `User-agent: *` / `Disallow: /`. Same 26-byte deny-all on `treasury-tools.surge.sh` and kit hosts. |
| PR #111 euro-shop-face | Unmerged. Adds `robots.txt` with `Allow: /`. Done-check is a **manual** `rg` on four HTML files — not CI. |
| PR #112 REVIEW-RUBRIC | Hard-fail #1 USDC-on-face, #5 robots `Disallow: /`. Shop already **FAIL**. No CI runs those rows. |
| PR #122 adv-plan | Named leftover 9/49 SKUs and the too-narrow `rg` done-check. Still no gate. |

HEAD file list has no workflow to miss-configure. The miss is **absence**.

---

## Scorecard

| # | Check | In git | On live | Color |
| --- | --- | --- | --- | --- |
| A1 | leftover-digit CI | missing | n/a | **RED** |
| A2 | USDC-grep CI | missing | n/a | **RED** |
| A3 | robots CI | missing (`robots.txt` also missing) | `Disallow: /` | **RED** |
| B1 | Paid CI products | none present | none | **GREEN** |
| B2 | FACTUUR / Google Fonts / fake BE0 on HEAD | 0 hits | (rubric: live PASS on BE0/fonts) | **GREEN** (content, not a gate) |
| B3 | PR #111 manual `rg` | unmerged, four files only | live shop untouched | **YELLOW** |

**Overall: RED.** Builder in-house CI does not exist. The three named checks are unspecified in any workflow. HEAD would fail all three if they ran.

---

## RED — the three missing jobs

Each job is one shell step. Fail the step → fail the PR. Required-on: `push` to `main` and `pull_request`. Vehicle: `.github/workflows/builder-ci.yml` (not in this PR). Runner: `ubuntu-latest`. Tool: `ripgrep` (`rg`) already on GitHub-hosted Ubuntu, or `grep -E` if `rg` is missing.

Shop-face paths (the Belgian secretary pages). Kit checkout is **not** shop face:

```
SHOP_FACE='index.html catalog.html pakketten.html betalen.html SITE.md README.md config.js'
```

Kit / product files (`solana-invoice.html`, `kit-pay.html`) are **out of these three greps**. USDC is allowed there. Leftover 9/49 as a **shop** SKU is not.

If a listed path does not exist yet, the job still runs on the files that do. Missing `pakketten.html` / `betalen.html` / `SITE.md` on HEAD is not a skip for `index.html` / `catalog.html` / `README.md` / `config.js`.

### A1 — leftover-digit CI — RED (missing)

**Why it exists.** CEO stop-list: no 9/49 leftover HTML on the shop. Hide-coin that only deletes the word `USDC` leaves the digits (`9`, `49`, `9000000`). Euro stickers (`€9` / `€49`) are the same leftover SKUs. Fake KBO leftover digits (`BE0…`) are the same class.

**Job name:** `leftover-digit`

**Exact check** (must exit 1 if any match):

```bash
set -euo pipefail
files=$(ls index.html catalog.html pakketten.html betalen.html SITE.md README.md config.js 2>/dev/null || true)
test -n "$files"

# Toy SKU leftovers: 9 / 49 as USDC or euro face prices.
rg -n -e '9 USDC' -e '49 USDC' -e '€9' -e '€49' -e '&euro;9' -e '&euro;49' \
   -- $files && { echo 'leftover-digit: 9/49 toy SKU on shop face'; exit 1; }

# Config leftover after a string-strip of "USDC".
rg -n -e 'priceUsdc:' -e 'priceLabel:' -e 'EXPECTED_RAW' -e '9000000' -e 'one-job-automation' \
   -- $files && { echo 'leftover-digit: raw 9-USDC amount or leftover config'; exit 1; }

# Fake Belgian enterprise leftover digits (not the allowed "nog niet toegekend" line).
rg -n -e 'BE0[0-9]' -e '[0-9]{4}\.[0-9]{3}\.[0-9]{3}' \
   -- $files && { echo 'leftover-digit: invented KBO/BTW digits'; exit 1; }

echo 'leftover-digit: PASS'
```

**HEAD evidence (would FAIL today):**

| File | Hit |
| --- | --- |
| `index.html:6` | `<title>Solana Invoice — 9 USDC</title>` |
| `index.html:108` | `49 USDC · due on receipt` |
| `index.html:136` | `var EXPECTED_RAW = "9000000";` |
| `index.html:113` | `Memo: one-job-automation` |
| `catalog.html:128` | `<span class="price">9 USDC</span>` |
| `catalog.html:139,150,161` | `49 USDC` chips |
| `config.js:6-7` | `priceUsdc: 9` / `priceLabel: "9 USDC"` |
| `README.md:15-18` | `9 USDC` invoice + three `49 USDC` tools |

PR #111 would still FAIL this job: it reprints the same toys as `€9` / `€49`. Euro sticker is leftover-digit, not a pass.

### A2 — USDC-grep CI — RED (missing)

**Why it exists.** REVIEWER hard-fail #1: USDC must not be the shop-face price or appear in the first viewport of home/catalog (`<title>`, `<h1>`, hero, kicker, price chips). Coin words on the sales face are the hide-the-coin miss.

**Job name:** `usdc-grep`

**Exact check:**

```bash
set -euo pipefail
files=$(ls index.html catalog.html pakketten.html betalen.html SITE.md README.md 2>/dev/null || true)
test -n "$files"

# Shop face: no coin, no wallet vendor, no chain name.
# (config.js is leftover-digit, not this grep — `usdcMint` is settlement wiring.)
if rg -n -i -e 'USDC' -e 'Phantom' -e 'Solana' -- $files; then
  echo 'usdc-grep: coin/chain/wallet vendor on shop face'
  exit 1
fi
echo 'usdc-grep: PASS'
```

**Not a pass:** the PR #111 done-check, copied here so it cannot be reused as CI:

```bash
# INCOMPLETE — do not ship this as the job.
rg -i 'USDC|Phantom|Solana' index.html catalog.html pakketten.html betalen.html
```

That four-file list omits `README.md`, `SITE.md`, live Surge HTML, and (on that branch) still leaves `config.js` / `kit-pay.html` printing `9 USDC`. A green four-file `rg` with USDC on the live home is punch-list theater. The job above is the in-house check. Live hosts are the robots job’s curl, not a substitute for grepping git.

**HEAD evidence (would FAIL today):** USDC counts `rg -c -i USDC`: `index.html` 15, `catalog.html` 9, `README.md` 8, plus `config.js` / product file out of this job. Cited shop-face lines: `index.html:6-7,82,95,98`; `catalog.html:7,116,128`; `README.md:3,5,15`.

`solana-invoice.html` is **allowed** to say USDC. Do not add it to `usdc-grep`.

### A3 — robots CI — RED (missing)

**Why it exists.** REVIEWER hard-fail #5: `robots.txt` must not `Disallow: /` for `User-agent: *` on a **public shop**. Missing `robots.txt` in git is how Surge keeps serving the 26-byte deny-all. `#111` writes `Allow: /` in an unmerged tree; live `sovereignforge.surge.sh` and `treasury-tools.surge.sh` still deny everything.

**Job name:** `robots`

**Exact check:**

```bash
set -euo pipefail

# 1. File exists in git (Surge will not invent Allow:).
test -f robots.txt || { echo 'robots: robots.txt missing in git'; exit 1; }

# 2. Must not block the whole origin.
if rg -n -e '^[[:space:]]*Disallow:[[:space:]]*/[[:space:]]*$' robots.txt; then
  echo 'robots: Disallow: / is a shop fail'
  exit 1
fi

# 3. Public shop must be explicitly allowed.
rg -q -e '^[[:space:]]*Allow:[[:space:]]*/[[:space:]]*$' robots.txt \
  || { echo 'robots: missing Allow: /'; exit 1; }

# 4. Live public shop (in-house curl, still free). Fail closed on HTTP error.
for host in \
  https://sovereignforge.surge.sh/robots.txt \
  https://treasury-tools.surge.sh/robots.txt
do
  body=$(curl -fsS "$host") || { echo "robots: curl failed $host"; exit 1; }
  echo "$body" | rg -q -e '^[[:space:]]*Disallow:[[:space:]]*/[[:space:]]*$' \
    && { echo "robots: live $host still Disallow: /"; exit 1; }
done

echo 'robots: PASS'
```

**HEAD evidence (would FAIL today):**

```
ls robots.txt
→ no such file
```

```
curl -sS https://sovereignforge.surge.sh/robots.txt
curl -sS https://treasury-tools.surge.sh/robots.txt

User-agent: *
Disallow: /
```

No `Allow:` line. Kit hosts return the same deny-all; this job gates the **two public shop origins**. Kit-host robots are REVIEWER’s row, not a fourth CI product.

---

## GREEN (adjacent, not a substitute)

### B1 — No paid CI products — GREEN

HEAD has no CodeRabbit workflow, no CircleCI orb, no Codecov, no Snyk GitHub app config, no paid runner label. Keep it that way. Do not “fix” RED by buying a review bot. The three jobs are `rg` + `curl`.

### B2 — Content greps that already pass on HEAD (still not CI)

```bash
rg -n 'FACTUUR|fonts\.googleapis|fonts\.gstatic|BE0[0-9]' \
  README.md catalog.html config.js index.html solana-invoice.html
# 0 matches on HEAD
```

Useful later as extra steps in the **same** free workflow. Not a pass for A1–A3. Not a reason to skip leftover-digit.

---

## YELLOW

### B3 — `#111` manual `rg` is not CI

Unmerged `cursor/euro-shop-face-00e2` documents:

```bash
rg -i 'USDC|Phantom|Solana' index.html catalog.html pakketten.html betalen.html
# no matches
```

and commits `robots.txt` with `Allow: /`. That is a punch-list note in a PR body. It does not run on `main`, does not run on other PRs, does not curl live hosts, and would still fail leftover-digit (`€9` / `€49`). Treat it as a draft of A2/A3, not a gate.

---

## Adversarial notes

1. **Absence is the defect.** There is no flaky workflow to debug. There is no `.github/workflows` directory. Claiming “CI is fine, we just have not hidden the coin yet” is false: nothing would catch the coin.

2. **Euro sticker ≠ leftover-digit pass.** Replacing `9 USDC` with `€9` on the same toy is the failure leftover-digit is for. USDC-grep can go green on a tree that leftover-digit still fails.

3. **Four-file USDC-grep ≠ shop.** `README.md` and live `SITE.md` are secretary-visible. `config.js` keeps `priceLabel: "9 USDC"` after HTML string-strips. Live Surge is a different tree; git-only USDC-grep can go green while `sovereignforge.surge.sh` still prints `900 USDC`.

4. **robots.txt in git without deploy still fails step 4.** Committing `Allow: /` and not publishing it leaves live `Disallow: /`. The curl is part of the job, not optional.

5. **Do not add paid CI to close RED.** A CodeRabbit comment is not leftover-digit. A CircleCI badge is not robots `Allow: /`.

---

## Bar for GREEN (CI only)

A later Builder **implementation** PR (not this file) is GREEN on this seat only if:

1. `.github/workflows/builder-ci.yml` exists, `on: [push, pull_request]`, `ubuntu-latest`, **no** paid services.
2. Jobs `leftover-digit`, `usdc-grep`, and `robots` run the exact checks above (same patterns, same shop-face path list, same live curl hosts).
3. All three are required status checks, or the workflow fails the PR as a single `builder-ci` check that includes all three steps.
4. `robots.txt` is in git with `Allow: /` and **no** `Disallow: /`, and live shop hosts match.
5. HEAD (or the implementing branch) actually **passes** the three jobs — not “the YAML exists and HEAD is still 9 USDC.”

Until that lands, Builder CI stays **RED**.

---

## Re-grep (copy/paste, this checkout)

```bash
ls .github/workflows 2>/dev/null || echo 'NO WORKFLOWS'
ls robots.txt 2>/dev/null || echo 'NO robots.txt'
rg -n -e '9 USDC' -e '49 USDC' -e 'priceUsdc:' -e 'EXPECTED_RAW' -e '9000000' \
  README.md catalog.html config.js index.html
rg -n -i -e 'USDC' -e 'Phantom' -e 'Solana' \
  README.md catalog.html index.html
curl -sS https://sovereignforge.surge.sh/robots.txt
curl -sS https://treasury-tools.surge.sh/robots.txt
```

---

End. No workflow. No paid CI. No mail. No KBO.
