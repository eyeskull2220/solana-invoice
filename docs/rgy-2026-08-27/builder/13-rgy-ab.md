# 13 — Builder A/B red-green deploy

Seat: **ADVERSARIAL**, then **RGY REVIEWER**.  
Date: **2026-08-27**.  
Surface: Builder shop faces (`sovereignforge.surge.sh`, `treasury-tools.surge.sh`, repo `main`, PR #111).  
This file is a score. It does not ship HTML.

## Score: **RED**

There is **no real A/B**. Two Surge hostnames with different HTML is not an experiment, not a traffic split, and not a red-green slot.

Live is the **losing mix**:

| Host | Look | Face currency | Verdict vs winning face |
| --- | --- | --- | --- |
| [`sovereignforge.surge.sh`](https://sovereignforge.surge.sh/) | chalkboard (Young Serif + Atkinson, `--board`) | **USDC on the home** | Losing — coin on the sales face |
| [`treasury-tools.surge.sh`](https://treasury-tools.surge.sh/) | keukentafel cream (`#f4f1ea` + sage cards) | **EUR-first** | Losing — cream catalog, not chalkboard |
| repo `main` (`index.html` / `catalog.html`) | dark-crypto / cream catalog | **USDC-first** | Losing — not the shop |
| PR [#111](https://github.com/eyeskull2220/solana-invoice/pull/111) (unmerged) | keukentafel (`#f6f3ee` + sage `#0c4a36`) | EUR-first | Losing look even if merged |

The designated winner (chalkboard + euro on the face + coin only on betalen) is **not live on any host**. Both public shops also `Disallow: /`. There is no switch to cut over.

Rule used: **RED if no A/B and live is the losing variant.** Both clauses hold.

---

## 1. Adversarial — claims that would fake a GREEN

These are the ways a Builder seat can report “A/B is running” without having one. Each claim is scored against a fetch from **2026-08-27 ~19:17 UTC**.

### 1.1 “Two hosts = A/B”

**False.** A real A/B needs all of:

1. Two named variants with a single variable (EUR-first vs USDC-face, **or** keukentafel vs chalkboard — not both at once).
2. An assignment mechanism (cookie, hash, query, weighted DNS, edge rule).
3. A metric and a sample rule (who counts, when to stop).
4. A cutover: red slot holds the loser, green slot holds the winner, traffic moves after the call.

Fetched reality:

- No `Set-Cookie`, no variant query, no experiment id, no `split` / `ab-test` / `feature-flag` string on either home.
- Response headers are Surge cache only (`server: Surge`, `vary: Accept-Encoding`).
- The two hosts differ on **two axes at once** (look **and** currency). That is two drifted deploys, not a controlled test.
- Surge overwrites a hostname. There is no red slot / green slot. Redeploy is smash-and-replace.

### 1.2 “treasury-tools is already the EUR-first winner”

**False.** Face prices are euro (`€900`, `€199`, …; lead “Prijs in euro”). That wins the **currency** axis. It loses the **look** axis: cream `#f4f1ea`, sage `#123c2e`, Iowan/Palatino card grid — the keukentafel template REVIEWER already fails as Inter/cream slop. `/privacy.html` is **404**. `robots.txt` is `Disallow: /`. A secretary who lands here never sees the chalkboard board.

### 1.3 “sovereignforge is chalkboard, so ship that”

**False.** CSS is the winning look (`/* SovereignForge — chalkboard. Self-hosted Young Serif + Atkinson. */`, `--board`). Copy is the losing coin:

- `<meta name="description">`: “Charge in USDC, euro is omrekening.”
- Home lede: “Charge blijft USDC op Solana.”
- Price rows: `900 USDC · ±€774`, CTAs `Betaal 900 USDC`.
- Rate line: “Charge blijft USDC.”

Euro is a footnote next to the coin. Rubric: **FAIL if USDC is the face price or appears in the first viewport.** Home is that viewport. `/betalen.html` is allowed to say USDC; home is not.

### 1.4 “PR 111 is the green slot waiting to flip”

**False.** PR #111 hides the coin on marketing HTML (`€9` / `€49`, “betaalgegevens na akkoord”). `shop.css` is still keukentafel:

```css
--bg: #f6f3ee;
--accent: #0c4a36;
--radius: 14px;
```

That is the cream-paper + sage-card template. Merging #111 and deploying it to either host would **replace chalkboard with keukentafel**. Euro-only cream is not the winning face. The PR is also unmerged and was not deployed.

### 1.5 “Red-green is the two Surge names”

**False.** Red-green deploy means: green is the candidate you can fail back from; red is live; you flip a pointer. Here both names are live, both are index-blocked, both fail the shop rubric, and neither is a standby of the other. A visitor who bookmarks `treasury-tools.surge.sh` never sees chalkboard. A visitor who bookmarks `sovereignforge.surge.sh` never sees euro-first. There is no pointer to flip.

### 1.6 “Kits behind the shops are the test”

**False.** Kit hosts (`club-site-kit-treasury.surge.sh`, `menu-kit-treasury.surge.sh`, …) are deliverable demos, not shop-face variants. Most still print USDC on the wrap. They do not assign traffic between chalkboard and keukentafel.

### 1.7 “main is dark, so we already picked chalkboard”

**False.** Repo `main` `index.html` is a dark **crypto paywall** (`Solana Invoice — 9 USDC`, `#07090f`). That is not chalkboard (no `--board`, no Young Serif, coin on the title). `catalog.html` is cream keukentafel with `9 USDC` / `49 USDC` chips. Git does not contain the live chalkboard tree.

---

## 2. What a real A/B would look like (and is missing)

| Required | Present? | Evidence |
| --- | --- | --- |
| Named variants | Partial | Informal: SF chalkboard vs TT cream; USDC-face vs EUR-first. Not documented as A/B. |
| One variable | **No** | Hosts differ on look **and** currency **and** privacy **and** nav. Confounded. |
| Assignment | **No** | No cookie, no hash, no query, no edge rule. |
| Metric | **No** | No event, no mail-tag, no “voorstel doorgestuurd” count per host. |
| Sample / stop rule | **No** | No n, no date, no kill criterion. |
| Red-green slots | **No** | Two production hostnames, smash-deploy, no standby. |
| Winner already coded in git | **No** | Chalkboard tree is live-only. Euro-only tree in PR #111 is cream. Intersection (chalkboard + no coin) is not in `main`. |

GREEN would require: one variable live under assignment, or the experiment already **closed** onto the winning face with the loser taken down. Neither is true.

YELLOW would require: a real split with a documented winner pending cutover, **or** live already showing chalkboard + euro-first with only a leftover host. Neither is true.

RED is the only honest score.

---

## 3. Evidence — live fetch 2026-08-27 ~19:17 UTC

### 3.1 `https://sovereignforge.surge.sh/` — chalkboard, USDC-face

- Title: `SovereignForge — voorstel voor het bestuur`
- Lede: `Charge blijft USDC op Solana. Euro is omrekening, geen checkout.`
- Featured price: `900 USDC · ±€774 · geen BTW-factuur (OFFERTE)`
- CTA: `Betaal 900 USDC`
- CSS: `styles.css` opens `/* SovereignForge — chalkboard. Self-hosted Young Serif + Atkinson. */` with `--board: oklch(0.20 0.025 145)`
- `robots.txt`: `User-agent: *` / `Disallow: /`
- Privacy: `/privacy.html` linked from footer (exists; not the fail on this host)
- `/betalen.html` h1: `Kies het pakket. Betaal dat USDC-bedrag.` — allowed **if** home were euro-first. Home is not.

### 3.2 `https://treasury-tools.surge.sh/` — keukentafel, EUR-first

- Title: `SovereignForge — clubsite, inbox-ops, Peppol en menukaart voor clubs en KMO’s`
- Lead: `Wij leveren het bestand. Prijs in euro.`
- Chips: `€900`, `€199`, `€349`, `€49` — no `USDC` in the home HTML body
- Palette: `--bg: #f4f1ea; --card: #fffdf8; --accent: #123c2e;` Iowan Old Style / Palatino
- `robots.txt`: `User-agent: *` / `Disallow: /` (contradicts `<meta name="robots" content="index,follow">`)
- `/privacy.html`: **404**
- Stripe sandbox link on the menukaart card (test only) — extra surface, still not an A/B

### 3.3 `https://solana-invoice-treasury.surge.sh/` — cream “één klus”, euro

- Title: `Eén klus — €49 · OFFERTE`
- Same cream tokens as treasury-tools (`#f4f1ea`)
- `robots.txt`: `Disallow: /`
- Not a chalkboard variant. A kit wrap.

### 3.4 Repo `main` (this checkout)

- `index.html` title `Solana Invoice — 9 USDC`; pay card on the face
- `catalog.html` cream `#f6f3ee` + chips `9 USDC` / `49 USDC`
- README still lists `https://treasury-tools.surge.sh/` as “Live catalog”
- No shop chalkboard files in git

### 3.5 Assignment / red-green signals

Grepped both homes for `variant`, `ab-test`, `experiment`, `feature-flag`, `?v=`, `utm_`, `split`: **zero hits**.  
Headers: no experiment cookie.  
Repo grep for `keukentafel` / `chalkboard` / `a/b` / `red-green`: **zero hits** on `main`.

---

## 4. Which face wins (design-out — no coin)

Do not run an A/B. Do not keep both hosts. Pick **one** face and delete the other.

**Winning face**

1. **Look:** chalkboard — `--board` dark green, Young Serif + Atkinson self-hosted, no Inter, no cream card grid, no `#f4f1ea` / `#f6f3ee` shop home.
2. **Currency:** euro on the sales face (`€…` / `Prijs €…` in title, h1, lede, chips). USDC does not appear in the first viewport.
3. **Coin:** only on `/betalen.html` (or a pay panel **after** a kit is chosen). Copy: “betaalgegevens na akkoord” on marketing pages. No address, no mint, no Phantom, no Solana in home/catalog/pakketten.
4. **Host:** one public shop origin. The other Surge name 301s to it, or is taken down.
5. **Index:** `robots.txt` must not `Disallow: /`.
6. **Privacy:** `/privacy.html` on that origin, linked in the footer.

**Losing faces to kill**

| Face | Why it loses |
| --- | --- |
| Live sovereignforge home | Coin on the board. Secretary sees USDC before the kit. |
| Live treasury-tools home | Keukentafel cream catalog. Wrong room. |
| PR #111 `shop.css` | Euro copy on cream cards. Hides the coin, keeps the kitchen table. |
| repo `index.html` / `catalog.html` | USDC paywall + cream catalog. Not the Belgian shop. |

**Not a test:** chalkboard-with-coin vs cream-with-euro. Those are two different products. Combining the winners (board + euro, coin off-stage) is a **design decision already made** by REVIEWER rubric + hide-the-coin brief. Measuring it would only delay taking the loser down.

---

## 5. Builder follow-up (not this PR)

This review does not implement the face. Builder / FIX seats:

1. Put the live chalkboard tree in git.
2. Strip USDC/Solana/Phantom from home, pakketten (euro column only), catalog. Leave coin on betalen.
3. Do **not** restyle chalkboard into `#f6f3ee`.
4. Point one hostname at that tree. Redirect or delete the other.
5. `Allow: /`. Privacy on the shop origin.
6. Close PR #111 or restyle it onto `--board` before merge — cream euro is still the losing look.

Until that cutover, A/B / red-green stays **RED**.

---

## 6. Sources

- Live HTML/CSS/`robots.txt`: `sovereignforge.surge.sh`, `treasury-tools.surge.sh`, `solana-invoice-treasury.surge.sh` (fetched 2026-08-27 ~19:17 UTC)
- REVIEWER rubric: `docs/ultra-2026-08-27/REVIEW-RUBRIC.md` on PR [#112](https://github.com/eyeskull2220/solana-invoice/pull/112)
- Hide-the-coin euro face: PR [#111](https://github.com/eyeskull2220/solana-invoice/pull/111) (`shop.css` `--bg: #f6f3ee`)
- This checkout: `index.html`, `catalog.html`, `README.md` on `main`
