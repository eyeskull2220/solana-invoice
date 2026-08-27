# Builder adversarial test — shop kill list

Date: 2026-08-27. Seat: Builder. File: this one only.

**Zero state.** This repo has no real tests. Walk of `main` at `2170952`: five files (`index.html`, `catalog.html`, `solana-invoice.html`, `config.js`, `README.md`). Zero `*test*`, zero `*spec*`, no `robots.txt`, no `privacy.html`, no `404.html`. Nothing in CI greps the shop face. Unmerged draft PRs and live Surge hosts are **not** tests. They are evidence to score against.

**Adversarial.** A check tries to fail the shop. One **RED** kill fails the shop. **YELLOW** is not a pass. **GREEN** is only a pass for that check on that surface. Do not average.

**Locks for this file.** Do not invent a KBO / BTW / `BE0` number. Do not mail anyone. Mailto on a page is not mail sent. Tests read pages and grep; they do not POST forms, do not click Stripe, do not open a mail client.

---

## What should fail a shop

These eight kills are the shop-face gate. A kit file (`solana-invoice.html`, a demo clubsite) is allowed to talk about payment rails **inside the product**. The **shop** is the public sales origin a secretaris opens first: home, catalogus/pakketten, betalen, contact, privacy, 404.

| ID | Kill | Fail if | Pass if |
| --- | --- | --- | --- |
| K1 | USDC-on-face grep | Visible text on shop marketing pages matches `\bUSDC\b`, `\bSolana\b`, or `\bPhantom\b` | Those tokens are absent from visible home / catalogus / pakketten. Charge copy is euro. Rails live only behind betalen-after-akkoord, never on the face. |
| K2 | Leftover FACTUUR | A document **stamp / heading / word-mark** is `FACTUUR` (all-caps or title), or a legal invoice is implied | Stamp is `OFFERTE` or `VOORBEELD`. “geen factuur” / “geen wettelijke factuur” denials are allowed. |
| K3 | No demo link | Shop has no working `voorbeeld` the buyer can open without paying | At least one HTTP 200 demo per offered kit, linked from the face, with `VOORBEELD` (or equivalent) on that demo. Unlock-after-signature is not a demo. |
| K4 | Contrast | Body or UI text vs its background is **&lt; 4.5:1** (WCAG 2.2 AA 1.4.3). Unknown oklch without a measured ratio is not green | Normal text ≥ 4.5:1; large text ≥ 3:1. Compute from used hex, or measure in-browser. |
| K5 | Tap 44 | A primary tap target (nav, CTA, copy, pay, demo) is **&lt; 44×44 CSS px** | `min-height: 44px` and `min-width: 44px` (or measured box ≥ 44) on those controls. WCAG 2.5.8’s 24px is too small for this shop. |
| K6 | robots Disallow | `GET /robots.txt` contains `Disallow: /` (any user-agent) | `Allow: /`, or no robots file. Public shop must be crawlable. |
| K7 | 404 | Missing path returns **200**, or returns **404 with the Surge default** (“page not found / powered by surge.sh”, Fira, `#b7b7b7` on `#e3e3df` = 1.56:1) | HTTP 404, shop-owned HTML, home + privacy links, same chrome as the shop. |
| K8 | Missing privacy | No `privacy.html` (or equivalent) at 200, or footer has no link, or the page invents a KBO | 200 page, linked from footer on every shop origin. Identity: natural-person / Geel is fine. **KBO/BTW: nog niet toegekend** — never a made-up `BE0`. No “GDPR-compliant” badge. |

Any other defect (cream-card slop, English-only face, cookie banner with zero trackers, fake IBAN) can be a later review item. It does **not** replace a kill.

---

## Proposed test list

No runner exists. These are the first tests to implement. Run them on **one origin at a time**. Record the URL and the git SHA or Surge stamp.

Face pages for a shop origin: `/`, `/catalog.html` or `/pakketten.html` if present, `/betalen.html` if present. Strip `<script>` and `<style>` before a “visible” grep. Do not count `USDC` inside a hostname in `href` unless that hostname is also link text.

### T1 — USDC-on-face (K1)

```bash
# Visible-ish: drop script/style, then grep. Fail on any hit.
python3 - <<'PY'
import re, sys, urllib.request
url = sys.argv[1]
html = urllib.request.urlopen(url, timeout=20).read().decode("utf-8", "replace")
vis = re.sub(r"<script[\s\S]*?</script>", "", html, flags=re.I)
vis = re.sub(r"<style[\s\S]*?</style>", "", vis, flags=re.I)
vis = re.sub(r"<[^>]+>", " ", vis)
hits = re.findall(r"\b(USDC|Solana|Phantom)\b", vis, re.I)
print("HITS", hits)
sys.exit(1 if hits else 0)
PY
https://ORIGIN/
```

Fail = RED. Zero hits = GREEN for that URL.

### T2 — leftover FACTUUR stamp (K2)

Grep source for `FACTUUR`. Then classify each hit:

- **Denial** (pass): `geen FACTUUR`, `geen factuurstempel`, `geen wettelijke factuur`, `geen BTW-factuur`.
- **Stamp** (fail): heading, `.word`, watermark, `<title>`, or first-screen kicker that **is** `FACTUUR` without `geen`.

```bash
rg -n -i 'FACTUUR' index.html catalog.html pakketten.html betalen.html privacy.html
```

A kit **product** that prints `INVOICE` in English is not this kill (different audience). A Dutch shop face that ships `FACTUUR` as the document type is.

### T3 — demo link (K3)

From the shop face, collect every “Bekijk / Open het voorbeeld / Open het formulier” href. `GET` it.

Fail if: no such link, or the link 404s, or the only path is “paste a Solana signature to unlock”.

### T4 — contrast (K4)

For each used pair (body ink on bg, muted on bg, button ink on button fill, 404 ink on 404 bg):

```
ratio = (L1 + 0.05) / (L2 + 0.05)   # relative luminance, sRGB
fail if ratio < 4.5 for normal text
```

If the sheet uses `oklch(...)` and you did not convert or measure: **YELLOW**, not GREEN.

### T5 — tap 44 (K5)

In CSS: every `.btn`, `nav a`, `button`, copy-address control must declare `min-height: 44px` (and enough width). Padding-only estimates (`11px + 11px + 15px/1.2 line = 40px`) are a fail if they land under 44.

In browser (when a runner exists): getBoundingClientRect on 390px viewport. Not done today → CSS estimate only, mark YELLOW unless the math is clearly &lt; 44 (then RED).

### T6 — robots (K6)

```bash
curl -sS https://ORIGIN/robots.txt
# Fail if the body contains: Disallow: /
```

### T7 — 404 (K7)

```bash
curl -sS -o /tmp/404.html -w "%{http_code}\n" https://ORIGIN/this-page-does-not-exist-rgy-2026
# Need: 404
# Fail: 200; or body contains "powered by surge.sh"
# Pass: shop title/nav + link to / and /privacy.html
```

### T8 — privacy (K8)

```bash
curl -sS -o /dev/null -w "%{http_code}\n" https://ORIGIN/privacy.html
# Need: 200
# Face footer must href privacy.html
# Fail if page contains BE0\d or a 10-digit KBO stand-in
# Pass line: KBO/BTW: nog niet toegekend
```

### T9 — invented KBO (lock, not a shop-face kill by itself)

```bash
rg -n 'BE0[0-9. ]{8,}|BE 0[0-9. ]{8,}' INDEX_AND_SHOP_HTML
```

A hit on a shop or demo origin is RED for that origin (compliance lock). Do not “fix” by inventing a different number.

### T10 — mail (lock)

These tests do not send mail. A page may contain `mailto:` to a published address. Do not run `open mailto:` or SMTP from this suite.

---

## Scorecard — current evidence (2026-08-27 ~19:12 UTC)

Evidence sources, not tests:

- Git `main` `2170952` (this checkout).
- Live `GET` of `treasury-tools.surge.sh`, `sovereignforge.surge.sh`, `solana-invoice-treasury.surge.sh`, kit hosts, and their `/robots.txt`, `/privacy.html`, a missing path.
- Contrast math on hex pairs in those files. No Playwright measurement. No oklch→sRGB for the chalkboard sheet.

Live `treasury-tools.surge.sh` (10 899 B, title SovereignForge euro catalog) **does not match** repo `catalog.html` (4 882 B, “Treasury tools” / USDC chips). Score them as different surfaces.

### Kill × surface

| Kill | `main` `index.html` | `main` `catalog.html` | Live treasury-tools | Live sovereignforge | Notes |
| --- | --- | --- | --- | --- | --- |
| K1 USDC-on-face | **RED** | **RED** | **GREEN** | **RED** | Repo: visible “9 USDC” / “Billed in USDC”. Live TT: visible USDC=0, Solana=0 (3 `Solana` hits are href hostnames only). SF: 12 visible `USDC` (“Charge blijft USDC op Solana”, “Betaal 900 USDC”). |
| K2 leftover FACTUUR | **GREEN** | **GREEN** | **GREEN** | **GREEN** | No `FACTUUR` stamp on these faces. Hits are denials: “geen factuur”, “geen FACTUUR”, “geen BTW-factuur (OFFERTE)”. Product `solana-invoice.html` stamps `INVOICE` (English kit, not this kill). |
| K3 no demo link | **RED** | **YELLOW** | **GREEN** | **GREEN** | Repo index: paywall unlock, no voorbeeld. Repo catalog: “Open …” to live tool hosts (product, not a Dutch VOORBEELD kit). Live TT: “Bekijk …” → kit hosts 200. SF: “Open het voorbeeld” → club/menu/sponsor/lid hosts 200. |
| K4 contrast | **GREEN** | **GREEN** | **GREEN** | **YELLOW** | Repo dark ink/bg 17.80; muted 8.17. Catalog ink 15.72; muted 6.19; accent 10.02. Live TT hex `#161513`/`#f4f1ea` and `#5c5850`/`#f4f1ea` are in the same band as catalog (AA). SF uses `oklch` chalkboard — not converted here. Surge **default 404** `#b7b7b7` on `#e3e3df` = **1.56** (used by TT, not by SF). |
| K5 tap 44 | **YELLOW** | **RED** | **YELLOW** | **GREEN** | Repo catalog `.btn` padding 11+11 + 15px/1.2 ≈ **40px**. Repo index `button` padding 11+11 + 16/1.5 ≈ 46, **unmeasured**. Live TT paddings `10px 13px` / `12px 14px`, no `min-height: 44px`. SF `.btn` and `nav a` declare `min-height: 44px`. |
| K6 robots Disallow | **RED** | **RED** | **RED** | **RED** | Repo: no `robots.txt` (shop origin would inherit Surge default). Live TT, SF, solana-invoice-treasury, csv/form/rss kits: `User-agent: *` / `Disallow: /` (26 bytes). |
| K7 404 | **RED** | **RED** | **RED** | **GREEN** | Repo: no `404.html`. Live TT + kit Surge hosts: HTTP 404 but Surge default HTML (Fira, “powered by surge.sh”). SF: HTTP 404, title “Pagina niet gevonden — SovereignForge”, links to `/` and `/privacy.html`. |
| K8 missing privacy | **RED** | **RED** | **RED** | **GREEN** | Repo: no page, no footer link. Live TT: `/privacy.html` 404, no href. SF: `/privacy.html` 200, footer link, “geen FACTUUR-module”, USDC mentioned **on privacy** (rails honesty; K1 still fails the **home** face). Club kit origin: `/privacy.html` 404. |

### Kit hosts (not the shop, still fail a public demo origin)

Probed: `solana-invoice-treasury`, `club-site-kit-treasury`, `menu-kit-treasury`, `lid-kit-treasury`, `csv-cleaner-treasury`, `form-to-email-treasury`, `rss-to-webhook-treasury`.

| Host | K1 | K2 | K3 | K6 | K7 | K8 |
| --- | --- | --- | --- | --- | --- | --- |
| solana-invoice-treasury | GREEN (euro OFFERTE face, USDC visible=0) | GREEN (denial) | GREEN (`offerte.html`) | **RED** Disallow | **RED** Surge 404 | **RED** |
| club-site-kit-treasury | **RED** (“900 USDC” on demo home) | GREEN | GREEN (ZWV De Golfbreker demo) | **RED** | **RED** | **RED** (no privacy on that origin) |
| menu-kit-treasury | **RED** (199 USDC on face) | GREEN (VOORBEELD, “geen wettelijke factuur”) | GREEN | **RED** | **RED** | **RED** |
| lid-kit-treasury | **RED** (349 USDC) | GREEN | GREEN (`lid.html`) | **RED** | **RED** | **RED** |
| csv / form / rss tools | form+rss **RED** (49 USDC); csv face has no USDC in visible copy | GREEN (no stamp) | they *are* the tool | **RED** | **RED** | **RED** |

### Overall

| Surface | Verdict | Why |
| --- | --- | --- |
| Repo `main` sales HTML | **RED** | K1, K3, K6, K7, K8. Catalog also K5. Not a Belgian shop. |
| Live treasury-tools | **RED** | Hid the coin (K1 GREEN) and has demos, but K6+K7+K8 still kill. Privacy 404. Surge 404. `Disallow: /`. |
| Live sovereignforge | **RED** | Best chrome (privacy, custom 404, tap 44 in CSS) and still **K1 + K6**. Home sells “Betaal 900 USDC”. |
| Shop as a shippable origin | **RED** | No surface is free of a kill. |

FACTUUR leftover is **not** the current failure mode on these faces. USDC-on-face, robots, 404, and privacy are.

---

## What this document does not do

- Does not add a test runner, Playwright, or CI job.
- Does not merge euro-face or hide-the-coin branches. Unmerged work is not evidence of `main` or of a host until it is live.
- Does not invent KBO. Does not mail. Does not treat `mailto:sasha.de.vree.rene@gmail.com` on a live footer as a send.
- Does not score cream-card / Inter / Google Fonts (reviewer extras). Those are out of this kill list.
- Does not claim sibling files `01`–`04` exist. This file stands alone.

## Builder follow-up (not this PR)

To take any shop origin to a kill-free GREEN:

1. Euro-only visible face (T1). USDC only after akkoord, not on home cards.
2. `robots.txt` = `Allow: /` on every public shop host (T6).
3. Shop-owned `404.html` and `privacy.html` on **that origin**, footer-linked (T7, T8). Phrase **KBO/BTW: nog niet toegekend**.
4. `min-height: 44px` on nav and CTAs (T5). Measure at 390px.
5. Keep OFFERTE/VOORBEELD; never stamp FACTUUR (T2).
6. Keep a 200 voorbeeld per kit (T3).

Until those are live **and** re-run, the shop stays RED.
