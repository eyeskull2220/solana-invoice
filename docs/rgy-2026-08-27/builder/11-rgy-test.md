# Builder TEST — RGY 2026-08-27

Seat: **Builder TEST**. Date: **2026-08-27**. Run: live shop, then this file.

This seat invents the test bar the REVIEWER rubric ([PR #112](https://github.com/eyeskull2220/solana-invoice/pull/112), `docs/ultra-2026-08-27/REVIEW-RUBRIC.md`) never made mechanical. The rubric is a human PASS/FAIL sheet. It can (and did) call a cream catalog “euro-first” while every chip is a leftover USDC integer with a `€` glued on.

**This PR only adds the TEST instrument and the live score. No shop HTML, no CSS, no deploy.**

Overall live verdict: **RED**.

---

## 0. Adversarial pass (before the score)

Pressure rules: score **live Surge**, not git. A green PR that is not the host is not a green shop. `rg` that cannot see leftover digits is not a test. Two public faces that disagree are a fail even if each face has a story.

### Attacks that landed

1. **`no USDC grep` is not hide-the-coin.**  
   `https://treasury-tools.surge.sh/` has **zero** visible `USDC` / `Phantom` / `Solana` in the body. Chips are `€900`, `€199`, `€349`, `€490`, `€49`. Those integers are the kit **USDC** amounts from the chalkboard (`900 USDC · ±€774`, Kraken 1 USDC ≈ €0,86 on 27 aug 2026). The grep is clean. The digits are not. REVIEWER row 1 can be gamed by renaming the unit.

2. **The chalkboard actually converted; the catalog did not.**  
   `https://sovereignforge.surge.sh/` prints both `900 USDC` and `±€774`. That is a shop-face USDC fail, but the euro column is honest. The catalog prints `€900` as if 900 were euros. A secretary comparing the two hosts is looking at two different prices for the same kit.

3. **`robots.txt` is `Disallow: /` on every public host**, including the shop. Treasury-tools also sends `<meta name="robots" content="index,follow">`. The meta tag is a lie: crawlers obey `robots.txt`. REVIEWER already failed Disallow. TEST adds the missing **positive** bar: public shop hosts must serve `Allow: /`.

4. **Git is a third face, not the live shop.**  
   [PR #111](https://github.com/eyeskull2220/solana-invoice/pull/111) (`cursor/euro-shop-face-00e2`) has `robots.txt` `Allow: /` and `rg -i 'USDC|Phantom|Solana'` clean on `index.html` / `catalog.html` / `pakketten.html` / `betalen.html`. Live `sovereignforge.surge.sh` still charges USDC on the home. Live `treasury-tools.surge.sh` still leftover-digits. Scoring git would fake GREEN.

5. **Even PR #111 leftover-digits the small kits.**  
   Unpublished home chips are `€9` and `€49`. Those are the USDC integers again (`9 USDC` / `49 USDC`), not the Kraken euros (`±€8` / `±€42`). `no USDC grep` would pass. Leftover-digit scan would still fail.

6. **Sponsorblad `€900` is a trap for a naive digit grep.**  
   On the chalkboard home, the mini-table is captioned “voorbeeldbedragen van de club, niet de kitprijs” (`€150` / `€400` / `€900`). That `€900` is allowed. The catalog chip `€900` for “Club- of vzw-site” is not. The scan has to bind digits to **role**, not to “a 900 exists somewhere”.

7. **Pakketten on a phone is a 936 px table in a 333 px pan.**  
   Body `overflow-x` is false (`overflow-x: auto` on `.table-wrap`). Nav still hits. A secretary still cannot see euro and voorbeeld without sideways pan, and the first money column is `900 USDC`. Desktop+phone is not “page didn’t explode”.

8. **`FACTUUR` and fake `BE0` are the rows people already watch.**  
   Live shop and kits did **not** stamp FACTUUR or invent `BE0…`. Adversarial did not invent a fail here. The missing bar is the other four checks, plus leftover-digit.

### Attacks that did not land

- No invented KBO/BTW number on shop or kit hosts (`KBO/BTW: nog niet toegekend`).
- No FACTUUR document stamp. Hits are negations (`geen FACTUUR`, `geen wettelijke factuur`, `geen BTW-factuur`).
- Chalkboard home at 1280 and 390: no body overflow, nav links have 44 px height.
- Betalen QR is 225×225 at 390 px; address `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3` fits the column (page `scrollWidth` 374 < 390). `word-break: normal` is still a yellow, not a red overflow.
- No Google Fonts / Inter on the live chalkboard (out of this TEST bar; already in REVIEWER).

---

## 1. The missing TEST bar (invented here)

Six mechanical checks. Binary. No “disclaimer nearby”. Shop-face pages: **home**, **catalog** (if it is a public face), **pakketten**. **Betalen** is the pay surface: leftover-digit and USDC grep are scored there only as notes, except robots / FACTUUR / BE0 / viewport still apply.

Kit hosts inherit leftover-digit, FACTUUR, BE0, robots. They do not have to hide USDC until the shop face does — but a kit **landing** linked as the public voorbeeld still fails leftover-digit if it sells `€900` meaning 900 USDC.

### T1 — Leftover-digit scan

**What it is.** After hide-the-coin or hide-the-KBO, numeric tokens that kept their old meaning.

**Kit-charge integer set** (current chalkboard): `{9, 49, 199, 249, 299, 349, 399, 490, 900}`.

**Published conversion** (shop copy, 27 aug 2026, Kraken, not FOD): `1 USDC ≈ €0,86`. Honest euros for that set: `9→±€8`, `49→±€42`, `199→±€171`, `249→±€214`, `299→±€257`, `349→±€300`, `399→±€343`, `490→±€421`, `900→±€774`.

**RED if** any shop-face HTML/CSS/visible text contains:

| Leftover | Pattern | Why |
| --- | --- | --- |
| USDC amount sold as euro | chip/price `€900` (etc.) for a **kit** | Digits survived; unit was renamed |
| Orphan charge | `\b(9\|49\|199\|249\|299\|349\|399\|490\|900)\b` with neither `€` nor `USDC` in the same price node | Search-replace dropped the unit |
| Fake or leftover VAT | `BE0` + 9 digits, `0xxx.xxx.xxx`, `0xxx xxx xxx` | Hide-the-KBO left the digits |
| Leftover IBAN | `BE\d{2}\s?\d{4}\s?\d{4}\s?\d{4}` | Same class of leftover |
| Face `data-usdc` / `qr/{usdc}.svg` | attributes or filenames on **home/catalog/pakketten** | Machine leftover after copy rewrite |

**Allowed (not leftover):**

- Demo-club voorbeeldbedragen **labeled as not the kit price** (sponsorblad `€150` / `€400` / `€900` under that caption).
- Honest converted euro (`±€774`) on **betalen**, or on shop face **only if** USDC is also allowed there by product policy (today it is not — see T3).
- Dates (`27 aug 2026`), image width/height (`390`×`844`), CSS (`16px`).
- Negation copy that contains no charge integer.

**How to run:** parse price nodes (`.price`, `.feat-price`, `[class*=price]`, table cells under a USDC/`€` column). Do not `rg 900` the whole file.

### T2 — Desktop + phone

Viewports: **1280×800** and **390×844**. Routes: `/`, `/pakketten.html`, `/betalen.html`, `/contact.html`, `/privacy.html` on `sovereignforge.surge.sh`; `/` on `treasury-tools.surge.sh`.

**RED if** at either viewport:

- `document.documentElement.scrollWidth > innerWidth + 2` (body sideways scroll), or
- a header nav link has width or height `0`, or
- the OFFERTE/identity footer is not in the accessibility tree.

**YELLOW if** a primary money table is wider than the viewport and only reachable by `overflow-x: auto` pan (pakketten 9-column). Not RED: the page did not break. Not GREEN: a phone buyer cannot read the row.

**GREEN only if** both viewports show the same prices and stamps without pan, and nav hit targets stay ≥ 44 px on the short side.

### T3 — No USDC grep

Shop-face files / live HTML for home, catalog, pakketten:

```bash
rg -i 'USDC|Phantom|Solana' <face-files>
# expected: no matches
```

**RED if** any match in visible copy, `<title>`, meta description, `h1`, price chips, or CTA (`Betaal 900 USDC`).

**YELLOW if** the only hits are host slugs (`solana-invoice-treasury.surge.sh`) or privacy settlement sentences. Privacy may say USDC; that page is not the shop face. Betalen may say USDC **after** T1/T3 pass on the face.

Live chalkboard home is RED on this row today. Live treasury-tools body is GREEN on the grep and RED on T1.

### T4 — robots Allow

For each **public shop** origin (`sovereignforge.surge.sh`, `treasury-tools.surge.sh`):

```
User-agent: *
Allow: /
```

**RED if** `Disallow: /` is present for `User-agent: *` (or equivalent block-everything).

**YELLOW if** `robots.txt` is missing (crawlers default-allow, but this bar asked for an explicit Allow) or if `Allow: /` is present **and** a `Disallow: /` also is.

**GREEN only if** Allow is present and Disallow-all is absent.

Kit hosts with `Disallow: /` fail T4 for that host. They do not by themselves fail the shop if the shop origin Allows — except today the shop origin also Disallows.

### T5 — No FACTUUR

**RED if** a page stamps, titles, watermarks, or filenames a document `FACTUUR` (heading, `.stamp`, `.word`, download name).

**Allowed:** negation in running text when the visible stamp is `OFFERTE` or `VOORBEELD` (`geen FACTUUR`, `nooit FACTUUR`, `geen wettelijke factuur`, `geen BTW-factuur`).

`dual-invoice` as a slug is leftover naming, not a FACTUUR stamp.

### T6 — No fake BE0

**RED if** any Belgian KBO/BTW number is invented: `BE0` + digits, `0xxx.xxx.xxx`, or any made-up ondernemingsnummer.

**GREEN:** `KBO/BTW: nog niet toegekend` with no number. Demo mail like `hello@studio.example` is not a BE0 fail.

---

## 2. Live score — 2026-08-27

Fetched HTML + `robots.txt`. Browser: chalkboard home/pakketten/betalen and treasury-tools at **1280×800** and **390×844**.

Repo `main` (`index.html`, `catalog.html`) is still the English 9 USDC pay page. It is not the live Belgian shop. It is scored in the notes so nobody pretends git is Surge.

### Scorecard

| # | Check | `sovereignforge.surge.sh` | `treasury-tools.surge.sh` | `main` repo pay/catalog | Kit hosts (spot) |
| --- | --- | --- | --- | --- | --- |
| T1 | Leftover-digit | **YELLOW** — euro converted (`±€774`) but USDC integers still on the face; sponsor `€900` is labeled demo | **RED** — every chip is the USDC integer with `€` (`€900` … `€49`) | **RED** — `9 USDC` / `49 USDC` are the product | Kit landings still print `199 USDC` etc. (unit not renamed; T1 kit-as-euro does not fire; T3 would) |
| T2 | Desktop+phone | **YELLOW** — home/contact/betalen no body overflow; pakketten table 936 px in 333 px pan | **GREEN** — 390 and 1280, no body overflow, cards stack | n/a as Belgian shop | not scored this run |
| T3 | No USDC grep | **RED** — lede “Charge blijft USDC op Solana”; CTAs `Betaal 900 USDC`; pakketten column `USDC` | **GREEN** body — no `USDC`/`Phantom`/`Solana` in visible copy. **YELLOW** slugs `solana-invoice-treasury` | **RED** | **RED** on most kit wraps (`199 USDC`) |
| T4 | robots Allow | **RED** — `User-agent: *` / `Disallow: /` | **RED** — same; meta `index,follow` contradicted | n/a (no `robots.txt` on `main`) | **RED** — every listed kit host Disallow-all |
| T5 | No FACTUUR | **GREEN** — stamp OFFERTE; “geen BTW-factuur”; privacy “geen FACTUUR-module” | **GREEN** — “Stempel OFFERTE, geen FACTUUR” (negation) | **GREEN** — English `INVOICE`, not `FACTUUR` | **GREEN** — negations only (`nooit FACTUUR`, `geen wettelijke factuur`) |
| T6 | No fake BE0 | **GREEN** — `KBO/BTW: nog niet toegekend` | **GREEN** — same | **GREEN** — none | **GREEN** — none |

### Surface verdicts

| Surface | RGY | One-line |
| --- | --- | --- |
| Live shop home `sovereignforge.surge.sh/` | **RED** | T3 USDC on the face; T4 Disallow; T1 yellow (honest euro beside leftover USDC) |
| Live pakketten | **RED** | T3 USDC column + T4; T2 yellow pan-table |
| Live betalen | **YELLOW** | USDC allowed here **if** the face were clean; face is not. T4 still RED for the host. QR+address readable at 390 |
| Live privacy/contact | **YELLOW** | T5/T6 green; host T4 still Disallow; privacy correctly names USDC settlement |
| Live catalog `treasury-tools.surge.sh/` | **RED** | T1 leftover `€900`; T4 Disallow; T3 grep green (the trap) |
| Git PR #111 euro face (not live) | **YELLOW** | Would pass T3+T4; would still fail T1 on `€9`/`€49` |
| Repo `main` pay page | **RED** | Not a Belgian shop face; still `9 USDC` |

**Shop as a whole: RED.** One RED on a shop face fails the shop. T1 on treasury-tools, T3 on chalkboard, T4 on both.

---

## 3. Notes (evidence)

### T1 leftover-digit

Chalkboard home price nodes:

- `900 USDC · ±€774 · geen BTW-factuur (OFFERTE)`
- `199 USDC · ±€171 · …`
- `Kit 199 USDC · ±€171 · …`
- `349 USDC · ±€300 · …`

Treasury-tools `.price` nodes at 390 px: `€900`, `€199`, `€199`, `€349`, `€249`, `€299`, `€399`, `€399`, `€490`, `€249`, `€49`. **11/11 match the kit-charge integer set.** None match the Kraken euro column.

Sponsorblad mini-table on chalkboard (allowed leftover-lookalike): caption “voorbeeldbedragen van de club, niet de kitprijs”; `Hoofdsponsor €900`. A scan that `rg €900` without role will false-RED this.

Betalen leftover machine state (out of shop-face T1, logged): `data-usdc="900"`, `src="qr/900.svg"`, mailto subject `900 USDC`.

### T3 USDC grep

Chalkboard home meta: `Charge in USDC, euro is omrekening.` Lede: `Charge blijft USDC op Solana.` Pakketten `<th>USDC</th>` and CTAs `Betaal 900 USDC`.

Treasury-tools visible body: no `USDC`. Footer still links `https://solana-invoice-treasury.surge.sh/` (slug leftover = YELLOW).

### T4 robots

Every fetched host on this run:

```
User-agent: *
Disallow: /
```

Including `sovereignforge.surge.sh/robots.txt` and `treasury-tools.surge.sh/robots.txt` (25 bytes). Git PR #111 file is `Allow: /` and is not what Surge serves.

### T2 viewports

| Route | 1280 | 390 |
| --- | --- | --- |
| SF home | scrollWidth 1264, nav visible, prices as above | scrollWidth 374, nav Pakketten/Betalen/Contact height 44, header 107 px wrap, no overflow |
| SF pakketten | wide table ok | table width 936, wrap 333, `overflow-x: auto`; first money cell `900 USDC` |
| SF betalen | kit radios + QR | QR 225×225, address 333 px wide, no page overflow |
| TT home | cards | cards stack, leftover chips still `€900` |

Console on TT: favicon 404 only.

### T5 / T6

No `BE0` + digits. No FACTUUR stamp. Dual-invoice card text: `Stempel OFFERTE, geen FACTUUR`.

### Extra adversarial notes (not extra bar rows)

- TT still exposes a Stripe **test** link (`buy.stripe.com/test_…`) on the menukaart card. Not T1–T6; still a live-shop lie next to “geen factuur”.
- TT `/privacy.html` is 404; chalkboard `/privacy.html` is 200. REVIEWER already failed TT privacy. Not re-litigated as a seventh bar.
- Three faces: Surge chalkboard, Surge cream catalog, unpublished PR #111 cream `€9` shop. TEST scores the two live ones.

---

## 4. Tests that would design the yellows out

These are the tests to add so the yellows cannot ship. Until they exist and pass on **the deployed origin**, TEST stays RED/YELLOW.

### 4.1 Leftover-digit vs conversion table (kills T1 yellow + TT red + PR #111 yellow)

```bash
# tests/test_leftover_digits.py — fail if a shop-face price node
# is in KIT_USDC and the text is "€{usdc}" rather than "€{eur}".
KIT = {
  9: 8, 49: 42, 199: 171, 249: 214, 299: 257,
  349: 300, 399: 343, 490: 421, 900: 774,
}
# Parse .price / .feat-price / pakketten money cells.
# Allow demo tables with caption containing "niet de kitprijs".
# Fail: text matches r"^€(9|49|199|249|299|349|399|490|900)$" on a kit card.
```

Until this exists, hide-the-coin PRs will keep shipping `€900`.

### 4.2 Host agreement (kills SF vs TT yellow)

Same kit, same euro, same unit, on every public face:

```bash
# curl both homes, extract Club-site price node, assert equal.
# Today: SF "900 USDC · ±€774" vs TT "€900" → fail.
```

One shop origin, or two origins with one price function. No second catalog with a different digit story.

### 4.3 `rg` on the face glob (kills T3; does not replace 4.1)

```bash
rg -i 'USDC|Phantom|Solana' index.html catalog.html pakketten.html
# live: curl -s https://sovereignforge.surge.sh/ | rg -i 'USDC|Phantom|Solana'
test $? -eq 1
```

CI must curl **Surge**, not only git, or T3 stays a theater passing on PR #111 while production prints `Betaal 900 USDC`.

### 4.4 robots Allow on deploy (kills T4)

```bash
for h in https://sovereignforge.surge.sh https://treasury-tools.surge.sh; do
  body=$(curl -fsS "$h/robots.txt")
  printf '%s\n' "$body" | grep -qx 'User-agent: *'
  printf '%s\n' "$body" | grep -qx 'Allow: /'
  printf '%s\n' "$body" | grep -q 'Disallow: /' && exit 1
done
```

Wire this to the Surge publish step. A host that still serves the 25-byte Disallow file cannot be called shipped.

### 4.5 Playwright 1280 + 390 (kills T2 yellow)

```js
// tests/shop.viewport.spec.js
for (const size of [[1280, 800], [390, 844]]) {
  // / /pakketten.html /betalen.html
  // expect(scrollWidth).toBeLessThanOrEqual(innerWidth + 2)
  // expect(nav links). each height >= 44
  // pakketten: no horizontal pan required to read euro
  //   → stacked cards on 390, not a 9-col table
}
```

Design the yellow out: **do not ship a 9-column USDC table as the phone pakketten view**. Cards with one euro price pass; a pan-table is a permanent yellow.

### 4.6 Betalen address wrap (kills word-break yellow)

```js
// at 390: address element overflow-wrap/anywhere or word-break:break-all
// getBoundingClientRect().right <= innerWidth
// no page scrollWidth overflow after selecting the longest kit label
```

### 4.7 FACTUUR / BE0 as grep CI (keeps T5/T6 green)

```bash
# Stamp fail: FACTUUR as its own heading/stamp, not "geen FACTUUR"
rg -n 'FACTUUR' live.html | rg -v -i 'geen FACTUUR|nooit FACTUUR|geen wettelijke factuur|geen BTW-factuur|geen FACTUUR-module'
rg -n -i 'BE0[0-9]|0[0-9]{3}[.\s][0-9]{3}[.\s][0-9]{3}' live.html
```

These two are GREEN today. Put them in CI so a later “fill in KBO” PR cannot invent `BE0123.456.789`.

### 4.8 Deploy parity (kills git-vs-Surge yellow)

After publish: `sha256` of live `/`, `/pakketten.html`, `/robots.txt` equals the git tree that TEST scored — or TEST re-runs on live and stays RED. PR #111 must not be counted as T3/T4 green until those bytes are what curl returns.

---

## 5. What GREEN would look like

Live `sovereignforge.surge.sh` (and any remaining catalog origin):

1. Price nodes are honest euros (`€774`, not `€900`), no kit-charge integer sold as euro. Demo `€900` only under “niet de kitprijs”.
2. Home and pakketten readable at 1280 and 390 without pan; pakketten is cards or a short table.
3. `rg -i 'USDC|Phantom|Solana'` on those faces is empty. USDC lives on betalen and privacy.
4. `robots.txt` is `Allow: /`, not `Disallow: /`.
5. Stamp OFFERTE/VOORBEELD, never FACTUUR.
6. `KBO/BTW: nog niet toegekend`, never `BE0…`.

Until 4.1–4.8 exist, a later builder can “fix copy” and still fail this seat. That is the point of inventing the bar.

---

## 6. Out of scope

- Shop HTML/CSS fixes (other builder seats / PR #111).
- REVIEWER cream/Inter/Google Fonts/privacy/cookie rows (already instrumented in PR #112).
- Paper-bot, Kraken journal, Peppol kits as products.
- Changing the treasury address.
