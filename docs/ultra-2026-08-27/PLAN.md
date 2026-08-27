# SovereignForge EUR-first OFFERTE shop — week of 27 Aug 2026

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

I'm using the writing-plans skill to create the implementation plan.

**Goal:** Ship a Dutch, EUR-first public OFFERTE shop for SovereignForge (seat: Geel) that another agent can execute from this file plus `docs/ultra-2026-08-27/BOARD.md` with no chat history.

**Architecture:** The public face is a static HTML shop on Surge. Kits already live at `*-treasury.surge.sh` stay as they are — this week does **not** rewrite kit HTML. The shop copy, robots.txt, and repo root pages (`index.html`, `catalog.html`, `README.md`) become the EUR/OFFERTE surface. Crypto rails (Phantom receive-only, Kraken paper) live in operator notes, never on the public face. The operator in Geel is not the freelancer: agents deliver files; nobody applies the operator as a developer.

**Tech Stack:** Static HTML/CSS/JS already in this repo, Surge hosts, `robots.txt`, grep/curl verification. No new npm connectors, no new MCP servers, no live Stripe, no wallet SDK.

## Global Constraints

Every task implicitly includes this section. Copy values verbatim.

- **Brand / seat:** SovereignForge, Geel, Dutch public copy, EUR-first prices.
- **Document stamp:** `OFFERTE` or `VOORBEELD` only. Never `FACTUUR`. Never a legal Belgian B2B invoice.
- **KBO/BTW:** print exactly `KBO/BTW: nog niet toegekend`. No invented `BE0…` digits, no demo IBAN, no fake ondernemingsnummer.
- **Public-face ban (words and hosts):** the public shop and any page linked from it must not show `USDC`, `Solana`, `Phantom`, `crypto`, `wallet`, or a `solana:` URI. Hostnames that contain `solana` must not be used as public CTAs.
- **Do not rewrite kit HTML.** Do not edit live kit files under existing `tools/*/index.html` (or the kit Surge deploys) to “fix” USDC copy. Wrap, unlink, or add **new** shop pages instead.
- **No leftover HTML:** do not restack the 9 USDC toys onto the shop; do not leave repo `index.html` / `catalog.html` as the old USDC pay page.
- **No new connectors:** no new Stripe live products, no new MCP, no SIWE, no Phantom SDK, no wallet-connect, no x402 facilitator, no Helio, no Request Network, no Google APIs.
- **No live Stripe.** The only Stripe URL that already exists on the live catalog is the **test** link `https://buy.stripe.com/test_dRmdR9gFd1Yt05D7E95os00` (sandbox). Prefer removing it from the public face. Never add a live Checkout URL.
- **robots must Allow** on the public shop:

```
User-agent: *
Allow: /
```

Surge’s default `Disallow: /` is a **fail**. Every existing `*-treasury.surge.sh/robots.txt` fetched on 27 Aug 2026 returned `Disallow: /`.
- **Phantom is receive-only and internal.** Do not put the address, mint, QR, or copy-address on the public face. Operator notes may keep Solana `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3` (mint `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v`) and Base `0x9eb954b567ef3616424a6e1bf42c63724930aa54`. No send, no perps, no new key, no third address.
- **Kraken stays paper until invert gate.** Invert gate = a dated operator ACK in `docs/` that names the paper snapshot, the first live pair/size, and the words `INVERT GATE ACK`. Until that file exists: `kraken paper` only; do not reset workspace `dca-paper`; no live orders; no Withdraw Funds keys.
- **Operator is not the freelancer.** Do not apply on Freelancer.be / Twago / PeoplePerHour / Codementor as the Geel operator. Do not publish personal Gmail on the shop. Demo mail is RFC 2606 only (`hello@studio.example`).
- **PII:** no personal Gmail, phones, home addresses, keys, or named real Belgian buyers on public pages. Fake demo club **ZWV De Golfbreker** / `info@golfbreker.example` stays fake.
- **Not a Peppol Access Point.** No compliance stamp. PDF-by-mail is not a legal BE B2B invoice since 1 Jan 2026.
- **Kit URLs:** use only hosts verified HTTP 200 on 27 Aug 2026 (table below). Do not invent `*-treasury.surge.sh` names.

### Verified live hosts (HTTP 200 on 27 Aug 2026) — do not invent others

**Public shop (EUR copy already live, repo main still leftover USDC):**

| Host | Live title (fetched) | Public-face status |
| --- | --- | --- |
| `https://treasury-tools.surge.sh/` | SovereignForge — clubsite, inbox-ops, Peppol en menukaart… | Shop. EUR prices. Stripe **test** link present. Footer still links `solana-invoice-treasury.surge.sh` (hostname leak). `robots.txt` = `Disallow: /` (fail). |

**Catalog-linked kits (from live `treasury-tools.surge.sh` hrefs):**

| Host | Live title | Public-face leak |
| --- | --- | --- |
| `https://club-site-kit-treasury.surge.sh/` | ZWV De Golfbreker — zwemclub in Geel (demo) | USDC / Solana pay box on page |
| `https://menu-kit-treasury.surge.sh/` | Menukaart + QR/allergenen — 199 USDC · Desk Noord | USDC / Solana |
| `https://sponsor-kit-treasury.surge.sh/` | SovereignForge — sponsorblad vzw (OFFERTE) | meta/kicker still “199 USDC op Solana” |
| `https://lid-kit-treasury.surge.sh/` | Desk Noord — lid-inschrijving (OFFERTE) | meta/kicker still “349 USDC op Solana” |
| `https://vakman-kit-treasury.surge.sh/` | Vakman one-pager — 249 USDC · Desk Noord | USDC / Solana |
| `https://inbox-ops-treasury.surge.sh/` | Inbox-ops — 299 USDC · Desk Noord | USDC / Solana |
| `https://pipeline-treasury.surge.sh/` | Lead tot offerte — €399 · SovereignForge | EUR-clean words, **personal Gmail leak** |
| `https://peppol-chase-treasury.surge.sh/` | Belgisch Peppol Client-Chase Pack — 399 USDC | USDC / Solana |
| `https://dual-invoice-treasury.surge.sh/` | Twee-keten USDC-offerte — OFF-20260826 — 490 USDC | USDC / Solana / Base (internal rail, not public) |
| `https://peppol-ready-treasury.surge.sh/` | Peppol Ready Kit — 249 USDC · Desk Noord | USDC / Solana |
| `https://solana-invoice-treasury.surge.sh/` | Eén klus — €49 · OFFERTE | EUR copy, **hostname leak + personal Gmail** |

**Exist (200) but leftover 9 USDC / not on the shop — do not add to the public catalog this week:**

`https://csv-cleaner-treasury.surge.sh/`, `https://form-to-email-treasury.surge.sh/`, `https://rss-to-webhook-treasury.surge.sh/`, `https://dagtarief-offerte-treasury.surge.sh/`, `https://km-log-treasury.surge.sh/`, `https://btw-invoice-treasury.surge.sh/`, `https://retainer-invoice-treasury.surge.sh/`, `https://freelance-contract-treasury.surge.sh/`, `https://quote-calc-treasury.surge.sh/`, `https://scope-sheet-treasury.surge.sh/`, `https://expense-log-treasury.surge.sh/`, `https://time-tracker-treasury.surge.sh/`, `https://invoice-reminder-treasury.surge.sh/`, `https://ics-reminder-treasury.surge.sh/`, `https://utm-builder-treasury.surge.sh/`, `https://faq-page-treasury.surge.sh/`, `https://link-in-bio-treasury.surge.sh/`, `https://md-page-treasury.surge.sh/`, `https://json-clean-treasury.surge.sh/`, `https://waitlist-treasury.surge.sh/`, `https://receipt-treasury.surge.sh/`, `https://tip-jar-treasury.surge.sh/`

**Probed 404 — do not cite as live:** `pipeline-kit-treasury`, `dual-invoice-desk-treasury`, `peppol-ready-kit-treasury`, `inbox-ops-pack-treasury`, `eur-receive-log-treasury`, `review-retainer-treasury`, `dca-paper-journal-treasury`, `seizoenskaart-treasury`.

### EUR price list (public shop — already on live catalog; keep these numbers)

Do not invent new EUR prices. Use the live catalog:

| Pakket | EUR | Live href (may be unlinked this week if it leaks crypto) |
| --- | ---: | --- |
| Club- of vzw-site | €900 | `https://club-site-kit-treasury.surge.sh/` |
| Menukaart + QR/allergenen | €199 | `https://menu-kit-treasury.surge.sh/` |
| Sponsorblad vzw | €199 | `https://sponsor-kit-treasury.surge.sh/` |
| Lid-inschrijving | €349 | `https://lid-kit-treasury.surge.sh/` |
| Vakman one-pager | €249 | `https://vakman-kit-treasury.surge.sh/` |
| Inbox-ops | €299 | `https://inbox-ops-treasury.surge.sh/` |
| Lead tot offerte | €399 | `https://pipeline-treasury.surge.sh/` |
| Peppol Client-Chase | €399 | `https://peppol-chase-treasury.surge.sh/` |
| Dual-invoice / twee ketens | €490 | `https://dual-invoice-treasury.surge.sh/` |
| Peppol Ready Kit | €249 | `https://peppol-ready-treasury.surge.sh/` |
| Eén klus | €49 | do **not** CTA to `solana-invoice-treasury.surge.sh` |

Public pay copy: **“Betaalgegevens na akkoord.”** No IBAN, no wallet, no Stripe live charge.

### Repo vs live (27 Aug 2026)

Git `main` still has leftover USDC pages: `index.html` (title “Solana Invoice — 9 USDC”), `catalog.html` (“Treasury tools”, USDC), `README.md` (USDC catalog), `solana-invoice.html` (kit — **do not rewrite**), `config.js` (internal treasury config — do not put on public face). Live Surge shop has already moved to Dutch EUR. Builder must align **repo public files** with the EUR shop **without** reverting the live shop to leftover HTML and **without** rewriting kit HTML.

### Seats this week

| Seat | Owns | Does not own |
| --- | --- | --- |
| **planner** | This file + `BOARD.md`; freeze URLs/locks; invert-gate definition | Kit HTML, outreach sends |
| **web** | Public PII/Gmail strip, outreach law, Geel `info@` research | Coding the shop, Kraken live |
| **design** | Dutch EUR visual + copy system for the shop | Kit restyles, new connectors |
| **builder** | Replace leftover root HTML, `robots.txt` Allow, unlink leaking kits | Rewriting kit HTML, live Stripe, new Surge names |
| **reviewer** | Rubric gate on shop + linked pages | Shipping new products |

Companion board: `docs/ultra-2026-08-27/BOARD.md` (Sell / Paper / Rails / Capabilities × NOW / NEXT / WAIT, 27 Aug–2 Sep 2026 PT).

---

## File map (locked)

- Create: `docs/ultra-2026-08-27/PLAN.md` (this file)
- Create: `docs/ultra-2026-08-27/BOARD.md`
- Create: `robots.txt` (Allow)
- Create (builder, if needed): `shop/een-klus.html`, `shop/intake.html` — new EUR OFFERTE pages, not kit rewrites
- Modify: `index.html`, `catalog.html`, `README.md` — leftover USDC public face → Dutch EUR OFFERTE shop
- Do **not** modify: `solana-invoice.html` and any existing kit HTML already deployed at the hosts above
- Operator-only (not public): `config.js` may keep the Phantom receive address; do not reference it from public HTML

---

### Task 1: Planner — freeze SSOT and invert gate

**Files:**
- Create: `docs/ultra-2026-08-27/PLAN.md`
- Create: `docs/ultra-2026-08-27/BOARD.md`

**Interfaces:**
- Consumes: live Surge hosts (table above), git `main` leftover HTML, hard locks in Global Constraints
- Produces: this plan + the week board; invert-gate definition other seats must not override

- [ ] **Step 1: Confirm this directory is the only planner deliverable**

```bash
test -f docs/ultra-2026-08-27/PLAN.md && test -f docs/ultra-2026-08-27/BOARD.md && echo OK_PLAN_BOARD
```

Expected: `OK_PLAN_BOARD`

- [ ] **Step 2: Confirm leftover public HTML is still on git main (so builder knows what to replace)**

```bash
git show main:index.html | head -n 6
git show main:catalog.html | head -n 6
```

Expected: `index.html` title contains `Solana Invoice`; `catalog.html` title contains `Treasury tools`.

- [ ] **Step 3: Re-verify kit hosts instead of inventing names**

```bash
for u in \
  https://treasury-tools.surge.sh/ \
  https://club-site-kit-treasury.surge.sh/ \
  https://menu-kit-treasury.surge.sh/ \
  https://sponsor-kit-treasury.surge.sh/ \
  https://lid-kit-treasury.surge.sh/ \
  https://vakman-kit-treasury.surge.sh/ \
  https://inbox-ops-treasury.surge.sh/ \
  https://pipeline-treasury.surge.sh/ \
  https://peppol-chase-treasury.surge.sh/ \
  https://dual-invoice-treasury.surge.sh/ \
  https://peppol-ready-treasury.surge.sh/ \
  https://solana-invoice-treasury.surge.sh/
 do curl -sS -o /dev/null -w "%{http_code} %{url_effective}\n" "$u"; done
```

Expected: every line starts with `200`. If any host is not 200, remove it from the shop; do not guess a replacement hostname.

- [ ] **Step 4: Write invert-gate lock into BOARD.md Paper/WAIT**

Invert gate is **closed**. Required ACK file (when the operator later opens it) must contain the exact phrase `INVERT GATE ACK`, a paper snapshot date, and a first live pair/size. Until then Kraken = paper. Do not reset `dca-paper`.

- [ ] **Step 5: Commit planner docs only**

```bash
git add docs/ultra-2026-08-27/PLAN.md docs/ultra-2026-08-27/BOARD.md
git commit -m "docs: freeze 27 Aug 2026 SovereignForge OFFERTE plan and board"
```

---

### Task 2: Design — EUR-first Dutch shop surface

**Files:**
- Modify: `index.html`, `catalog.html` (visual + copy only; builder lands the files if design works in a branch)
- Create (optional tokens): keep CSS in those files; do not add a design-system package

**Interfaces:**
- Consumes: EUR price list and stamp rules from Global Constraints
- Produces: one visual system — paper/offerte, Dutch, euro, no coin chrome

- [ ] **Step 1: Lock the public words**

Allowed on the shop: `OFFERTE`, `VOORBEELD`, `KBO/BTW: nog niet toegekend`, `Betaalgegevens na akkoord`, euro amounts (`€49` … `€900`), Dutch package names from the live catalog.

Banned on the shop (case-insensitive): `USDC`, `Solana`, `Phantom`, `crypto`, `wallet`, `FACTUUR` as a stamp, live Stripe, personal Gmail, IBAN digits, `solana:` URIs.

- [ ] **Step 2: Lock layout**

One column, max width ~720px, mobile-first. Package cards: name, one Dutch sentence, euro price, one CTA. Footer: SovereignForge · OFFERTE/VOORBEELD · `KBO/BTW: nog niet toegekend` · not a Peppol Access Point.

Do not design a wallet QR, a network badge, or a “Pay USDC” button.

- [ ] **Step 3: Named-club demo rule**

The only public club demo is the **fake** ZWV De Golfbreker (`info@golfbreker.example`). Do not skin a real Geel club (ASV Geel, BBC Geel, ’t StAt, ZGeel, KST, …) on a public host this week. Later-list clubs are do-not-mail (see Task 5).

- [ ] **Step 4: Stripe chrome**

If a payment-button mock is needed, it is **not** Stripe live. Prefer no Stripe mark at all. If the existing test URL is kept, it must stay the `test_` URL and the sentence `Stripe sandbox / test only — geen live charge, geen factuur.` Reviewer fails a live `buy.stripe.com` URL that does not contain `/test_`.

- [ ] **Step 5: Hand design notes to builder as comments in the shop HTML, not a new kit**

No new `*-treasury.surge.sh` host. Shop stays `treasury-tools.surge.sh` plus repo `index.html`/`catalog.html`.

---

### Task 3: Builder — replace leftover public HTML + robots Allow

**Files:**
- Modify: `index.html`, `catalog.html`, `README.md`
- Create: `robots.txt`
- Do not modify: `solana-invoice.html`

**Interfaces:**
- Consumes: Task 2 copy/layout; EUR price list
- Produces: repo public face that matches the live Dutch shop intent, with Allow robots, no leftover USDC page as the homepage

- [ ] **Step 1: Write the failing leftover-HTML check**

```bash
python3 - << 'PY'
import pathlib, sys
banned = ("USDC", "Solana", "Phantom", "crypto", "wallet")
files = ["index.html", "catalog.html", "README.md"]
bad = []
for f in files:
    t = pathlib.Path(f).read_text(encoding="utf-8", errors="replace")
    for w in banned:
        if w.lower() in t.lower():
            bad.append(f"{f}:{w}")
if bad:
    print("FAIL leftover/crypto:", ", ".join(bad)); sys.exit(1)
print("PASS public files have no banned rail words")
PY
```

Expected **now on main:** `FAIL leftover/crypto` (because leftover HTML is still USDC). After this task: `PASS`.

- [ ] **Step 2: Confirm the test failed for the right reason**

Run the snippet in Step 1. Expected: exit code 1, `index.html:USDC` (and Solana) listed.

- [ ] **Step 3: Replace `index.html` with the Dutch EUR OFFERTE shop homepage**

`index.html` must be `lang="nl"`. Title example: `SovereignForge — OFFERTE`. Hero: packages for clubs and KMOs, price in euro, stamp OFFERTE/VOORBEELD, `KBO/BTW: nog niet toegekend`. List the EUR packages. CTA copy: `Bekijk pakket` / `Betaalgegevens na akkoord`. No copy-address, no QR, no transaction-signature unlock, no embedded `solana-invoice.html`.

- [ ] **Step 4: Replace `catalog.html` the same way (or make it a redirect/alias of the shop)**

If both files exist, they must tell the same EUR story. Do not keep a second “Treasury tools / USDC on Solana” catalog.

- [ ] **Step 5: Rewrite `README.md` as the shop readme (EUR, OFFERTE, no public rail)**

Public README may name the shop URL `https://treasury-tools.surge.sh/`. It must not publish the Phantom address or USDC mint. Operator rails stay out of the README.

- [ ] **Step 6: Add `robots.txt`**

```
User-agent: *
Allow: /
```

No `Disallow: /`. No empty file (Surge would restore default deny).

- [ ] **Step 7: Re-run Step 1 — must PASS**

Expected: `PASS public files have no banned rail words`

- [ ] **Step 8: robots + stamp + KBO checks**

```bash
grep -n "Allow: /" robots.txt
grep -n "Disallow: /" robots.txt || echo "NO_DISALLOW"
grep -E "FACTUUR" index.html catalog.html && echo FAIL_FACTUUR || echo PASS_NO_FACTUUR_STAMP
grep -E "KBO/BTW: nog niet toegekend" index.html
```

Expected: `Allow: /` present; `NO_DISALLOW` or no matching Disallow line; `PASS_NO_FACTUUR_STAMP` (the word may appear only in the legal sentence `geen factuur` / `geen FACTUUR-stempel`, not as the document stamp); KBO line present.

Legal-sentence exception: `geen wettelijke factuur` / `geen factuurstempel` is allowed. A heading or stamp `FACTUUR` is not.

- [ ] **Step 9: Do not deploy leftover HTML over the live shop**

When publishing, publish the **new** `index.html` + `robots.txt` to `treasury-tools.surge.sh`. Do not `surge` the old USDC `index.html`.

- [ ] **Step 10: Commit**

```bash
git add index.html catalog.html README.md robots.txt
git commit -m "feat: Dutch EUR OFFERTE shop face, robots Allow, leftover USDC HTML removed"
```

---

### Task 4: Builder — hide-the-coin without rewriting kits

**Files:**
- Modify: `index.html`, `catalog.html` (hrefs only)
- Create if needed: `shop/een-klus.html` (new file; €49 OFFERTE; no kit rewrite)
- Do not modify: any existing kit HTML on the verified hosts

**Interfaces:**
- Consumes: verified host table
- Produces: public CTAs that never land on a page that renders USDC/Solana/Phantom/wallet/crypto

- [ ] **Step 1: Write the link-leak scan**

```bash
python3 - << 'PY'
import pathlib, re, sys
html = pathlib.Path("index.html").read_text(encoding="utf-8", errors="replace")
html += "\n" + pathlib.Path("catalog.html").read_text(encoding="utf-8", errors="replace")
hrefs = re.findall(r'href="([^"]+)"', html)
banned_host = ("solana-invoice-treasury.surge.sh",)
banned_word = ("usdc", "solana", "phantom", "crypto", "wallet")
fail = []
for h in hrefs:
    low = h.lower()
    if any(b in low for b in banned_host):
        fail.append("host:"+h)
    if any(w in low for w in banned_word):
        fail.append("word:"+h)
    if "buy.stripe.com/" in low and "/test_" not in low:
        fail.append("live-stripe:"+h)
print("hrefs", len(hrefs))
if fail:
    print("FAIL", fail); sys.exit(1)
print("PASS no leaking hrefs")
PY
```

Expected after this task: `PASS no leaking hrefs`

- [ ] **Step 2: Unlink leaking kits from the public shop**

Keep the EUR **names and prices** on the shop. Change the CTA to an in-repo page or to `mailto:` **only if** the mailbox is `hello@studio.example` (demo) or to copy “Betaalgegevens na akkoord” with **no** personal Gmail.

Do **not** href: `solana-invoice-treasury.surge.sh`, `dual-invoice-treasury.surge.sh`, `club-site-kit-treasury.surge.sh`, `inbox-ops-treasury.surge.sh`, `peppol-chase-treasury.surge.sh`, `peppol-ready-treasury.surge.sh`, `menu-kit-treasury.surge.sh`, `vakman-kit-treasury.surge.sh`, or any leftover 9 USDC host, until a **new** EUR wrapper exists.

Kits that are EUR-word-clean **except PII** (`pipeline-treasury.surge.sh`) still cannot be public CTAs until web strips the Gmail (Task 5). Until then, describe “Lead tot offerte · €399” without the href.

- [ ] **Step 3: Eén klus €49 — new shop page, not a kit rewrite**

If `shop/een-klus.html` is created: Dutch OFFERTE, €49, `KBO/BTW: nog niet toegekend`, “Betaalgegevens na akkoord”, demo `hello@studio.example`. No unlock-by-signature. Do not embed `solana-invoice.html`.

- [ ] **Step 4: Stripe**

Remove `https://buy.stripe.com/test_dRmdR9gFd1Yt05D7E95os00` from the public shop unless design + reviewer explicitly keep it as sandbox. Default: **remove**. Never add a non-`test_` Stripe URL.

- [ ] **Step 5: leftover-toy ban**

`index.html` and `catalog.html` must not link `csv-cleaner-treasury`, `form-to-email-treasury`, `rss-to-webhook-treasury`, `tip-jar-treasury`, `receipt-treasury`, or other leftover 9 USDC hosts.

- [ ] **Step 6: Re-run Step 1 — PASS**

- [ ] **Step 7: Commit**

```bash
git add index.html catalog.html shop/een-klus.html
git commit -m "fix: unlink crypto kit hosts from public EUR shop"
```

---

### Task 5: Web — outreach law + strip public Gmail

**Files:**
- Modify: public shop files if they contain `gmail.com`
- Do not create a mail-merge tool
- Research already exists on branch `cursor/geel-club-mailtos-6be7` (`docs/geel-club-mailtos.md`) — cite it; do not invent extra inboxes

**Interfaces:**
- Consumes: Geel verenigingengids rules (public `info@` only; no personal Gmail; later-list do-not-mail)
- Produces: public pages with zero personal mailboxes; a send/no-send rule other seats can follow

- [ ] **Step 1: Fail if public files contain gmail.com**

```bash
grep -RIn "gmail.com" --include='*.html' --include='*.md' index.html catalog.html README.md shop 2>/dev/null && echo FAIL_GMAIL || echo PASS_NO_GMAIL
```

Expected after this task: `PASS_NO_GMAIL`

Live leak to close (do not copy the address into new files): `https://pipeline-treasury.surge.sh/` and `https://solana-invoice-treasury.surge.sh/` currently publish a personal Gmail. **Do not rewrite those kit hosts’ HTML this week** if they are kits. Instead: unlink them from the shop (Task 4). If builder already replaced `index.html` in-repo, that replacement must not include the Gmail.

- [ ] **Step 2: Outreach law (no send this week unless BOARD Sell/NOW explicitly says send — it does not)**

Allowed later: public `info@` from the Stad Geel listing, clubs **without** a modern site, not on the later-list.

Forbidden: personal Gmail/Telenet/Skynet/Hotmail; role inboxes (`secretaris@`, `bestuur@`); webmaster `info@webbyat.be`; later-list (ASV Geel, Valberta, Den Bruul, BBC Geel, ’t StAt, zwemclubkst); clubs with a modern site; applying the operator as a freelancer.

Mailto candidates already researched (do not mail this week): Aqua Ski, Defence Lab, Geelse Zaalvoetbal, Holvensche Hondenschool, Koninklijke Harmonie De Eendracht, Okinawa Goju-Ryu Karat-Do Geel-Ten Aard, TC Netevallei, ’t Geels Bieke. Source: `docs/geel-club-mailtos.md` on `cursor/geel-club-mailtos-6be7` / PR #103.

- [ ] **Step 3: Do not enroll X pay-per-use. Do not scrape personal mailboxes.**

- [ ] **Step 4: Commit only if shop files changed**

```bash
git add index.html catalog.html README.md shop
git commit -m "fix: strip personal mailboxes from public OFFERTE shop"
```

Skip the commit if `git diff` is empty because Task 4 already unlinked the leaking hosts.

---

### Task 6: Reviewer — shop rubric gate

**Files:**
- Test: run the commands in this task against the builder branch and against `https://treasury-tools.surge.sh/`
- Do not ship product HTML

**Interfaces:**
- Consumes: Tasks 3–5 outputs
- Produces: PASS/FAIL against the hard locks. A clean result is the review.

- [ ] **Step 1: Leftover HTML is gone from the public face**

```bash
python3 - << 'PY'
import pathlib, sys
text = pathlib.Path("index.html").read_text(encoding="utf-8", errors="replace")
needles = ["Solana Invoice — 9 USDC", "Paste your Solana transaction signature", "Treasury Solana USDC"]
hit = [n for n in needles if n in text]
print("FAIL leftover" if hit else "PASS no leftover pay page", hit)
sys.exit(1 if hit else 0)
PY
```

Expected: `PASS no leftover pay page []`

- [ ] **Step 2: Banned rail words on public files**

```bash
python3 - << 'PY'
import pathlib, sys
banned = ["usdc", "solana", "phantom", "crypto", "wallet"]
fail=[]
for f in ["index.html","catalog.html","README.md","robots.txt"]:
    p=pathlib.Path(f)
    if not p.exists():
        continue
    t=p.read_text(encoding="utf-8", errors="replace").lower()
    for w in banned:
        if w in t: fail.append(f"{f}:{w}")
print("FAIL" if fail else "PASS rail words", fail)
sys.exit(1 if fail else 0)
PY
```

Expected: `PASS rail words []`

- [ ] **Step 3: robots Allow**

```bash
python3 - << 'PY'
from pathlib import Path
t = Path("robots.txt").read_text(encoding="utf-8")
assert "User-agent: *" in t
assert "Allow: /" in t
assert "Disallow: /" not in t
print("PASS robots Allow")
PY
```

Expected: `PASS robots Allow`

After deploy, also:

```bash
curl -sS https://treasury-tools.surge.sh/robots.txt
```

Expected live body contains `Allow: /` and does not contain `Disallow: /`.

- [ ] **Step 4: OFFERTE only + no fake KBO**

```bash
python3 - << 'PY'
import pathlib, re, sys
text = pathlib.Path("index.html").read_text(encoding="utf-8", errors="replace")
if not re.search(r"KBO/BTW:\s*nog niet toegekend", text):
    print("FAIL missing pending KBO"); sys.exit(1)
if re.search(r"BE0\d{9}", text) or re.search(r"\b0\d{3}\.\d{3}\.\d{3}\b", text):
    print("FAIL invented KBO digits"); sys.exit(1)
if re.search(r"<[^>]*>\s*FACTUUR\s*<", text):
    print("FAIL FACTUUR stamp"); sys.exit(1)
print("PASS KBO pending, no FACTUUR stamp")
PY
```

Expected: `PASS KBO pending, no FACTUUR stamp`

- [ ] **Step 5: no live Stripe, no new connectors, no personal Gmail**

```bash
python3 - << 'PY'
import pathlib, re, sys
blob = ""
for f in ["index.html","catalog.html","README.md"]:
    blob += pathlib.Path(f).read_text(encoding="utf-8", errors="replace")
fail=[]
if "gmail.com" in blob.lower(): fail.append("gmail")
if re.search(r"buy\.stripe\.com/(?!test_)", blob): fail.append("live-stripe")
for w in ["wallet-connect", "phantom.com", "siwe", "x402", "hyperliquid"]:
    if w in blob.lower(): fail.append(w)
print("FAIL" if fail else "PASS connectors/PII", fail)
sys.exit(1 if fail else 0)
PY
```

Expected: `PASS connectors/PII []`

- [ ] **Step 6: Kit HTML was not rewritten**

```bash
git diff main -- solana-invoice.html
```

Expected: empty diff. Reviewer fails any patch to `solana-invoice.html` or to kit files whose only purpose is restyling USDC copy.

- [ ] **Step 7: Operator-is-not-freelancer check**

Public copy must not say the operator is available as a freelance developer / “ik code zelf”. Brand is SovereignForge delivering files. Fail bios that invite coding-job applications.

- [ ] **Step 8: Record PASS/FAIL on the PR.** A clean rubric is the review. Do not re-do a second manual pass of the same grep.

---

### Task 7: Planner — Paper / Rails week (no invert)

**Files:**
- Modify: `docs/ultra-2026-08-27/BOARD.md` only if status changes
- Do not add a shop card for the paper journal (no leftover HTML, no catalog card)

**Interfaces:**
- Consumes: invert-gate definition (Task 1)
- Produces: Kraken remains paper; Phantom remains receive-only internal

- [ ] **Step 1: Confirm invert gate is still closed**

```bash
grep -R "INVERT GATE ACK" docs || echo "NO_ACK"
```

Expected: `NO_ACK` (gate closed). If someone added an ACK without operator sign-off, treat it as invalid.

- [ ] **Step 2: Paper recipe lock (do not execute live)**

1. `dca-paper` — hold. Do not reset.
2. `fib-paper` — new spot workspace only.
3. `grid-paper` — new spot workspace only.
4. Long-term holds — do not sell the `dca-paper` stack unless CEO says.
5. Futures paper sleeve — cap 3x, kill switch; never mix that PnL into the DCA journal.

Kraken MCP in this environment may be disconnected; do not invent fills. Paper journal PR #110 (`dca-paper-journal/`) is operator-only VOORBEELD — not a shop kit, not a live host (404 on `dca-paper-journal-treasury.surge.sh`).

- [ ] **Step 3: Rails lock**

Phantom receive-only, two listed addresses max, no new key, no SIWE, no live Stripe, no x402/Helio/Request this week (those were Wallet **ideas**, not NOW). EUR receive-log pack (PR #91) is internal; it is not a live Surge host.

- [ ] **Step 4: Commit only if BOARD.md status cells changed**

```bash
git add docs/ultra-2026-08-27/BOARD.md
git commit -m "docs: mark invert gate still closed for 27 Aug week"
```

---

## Self-review

**Spec coverage:** EUR public face, no public crypto words, Phantom internal receive-only, Kraken paper until invert, operator ≠ freelancer, no fake KBO, OFFERTE/VOORBEELD only, no leftover HTML, no kit HTML rewrite, no new connectors, no live Stripe, robots Allow, verified kit URLs only — each maps to a task above.

**Placeholder scan:** no TBD / implement later.

**Type consistency:** invert gate phrase is `INVERT GATE ACK`; KBO phrase is `KBO/BTW: nog niet toegekend`; shop host is `https://treasury-tools.surge.sh/`.

## Execution handoff

Plan complete and saved to `docs/ultra-2026-08-27/PLAN.md`. Week board: `docs/ultra-2026-08-27/BOARD.md`.

Use superpowers:subagent-driven-development (one seat per task: planner, web, design, builder, reviewer) or superpowers:executing-plans inline. Builder must not rewrite kit HTML. Reviewer runs Task 6 as the gate.
