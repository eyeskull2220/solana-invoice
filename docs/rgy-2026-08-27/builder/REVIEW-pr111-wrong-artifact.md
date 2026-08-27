# REVIEW — PR #111 is the leftover catalog, not the shop

**Seat:** REVIEWER (new pass, 2026-08-27, after hide-the-coin)  
**Target:** [PR #111](https://github.com/eyeskull2220/solana-invoice/pull/111) `cursor/euro-shop-face-00e2` @ `8c5b820`  
**Verdict:** **RED**  
**GREEN on this PR:** **not available**

This file is judgment only. No shop HTML. No kit port. No mail. No spend. Notes below were taken on this pass against the PR files, `main`, and live Surge. They are not a rewrite of earlier RGY pages.

---

## Verdict in one paragraph

PR #111 titles itself a **shop** (“Euro-only sales face”, README `# SovereignForge shop`) and then prices the **leftover invoice catalog**: Offertebestand **€9**, studio-tools **€49**. The live Belgian shop is [`https://sovereignforge.surge.sh/`](https://sovereignforge.surge.sh/), whose featured kits are **€199 / €249 / €299 / €349 / €900** (today still printed as USDC). Those are different artifacts. Scoring #111 as a shop fix is a category error. **Do not merge it as the shop. Builder ports nothing from it. The only shop fix is a live Surge pass.**

---

## What this pass opened (from zero)

| Source | Opened | What it is |
| --- | --- | --- |
| PR #111 files | `index.html`, `catalog.html`, `pakketten.html`, `betalen.html`, `robots.txt`, `shop.css`, `README.md`, `config.js`, `kit-pay.html` | Euro resticker of this repo’s 9/49 catalog |
| `main` | `catalog.html`, `index.html` | Same SKUs, still `9 USDC` / `49 USDC` |
| Live shop | `https://sovereignforge.surge.sh/` home + `/pakketten.html` + `/robots.txt` | Chalkboard Belgian face. Featured kits 199 / 249 / 299 / 349 / 900. `Disallow: /` |
| PR #112 | `docs/ultra-2026-08-27/REVIEW-RUBRIC.md` | Live shop already **FAIL** (USDC on the face, robots Disallow). Independent of #111 |

PR #111 does not touch Surge. Merging it cannot change the live shop.

---

## Scorecard — PR #111 as shop

| Gate | Score | Evidence (this pass) |
| --- | --- | --- |
| Claims to be the shop | **yes → RED** | PR title “Euro-only **sales face**”. README: “# SovereignForge **shop**” / “Shop pages: `index.html` · `catalog.html` · `pakketten.html` · `betalen.html`”. Body: “Public **shop** copy”. |
| Priced leftover €9 / €49 toys | **yes → RED** | Home cards `€9` Offertebestand, `€49` Studio-tools (CSV, formulier naar e-mail, RSS-watcher). Catalog and pakketten repeat the same three tools. Betalen: “Kies een pakket (€9 of €49).” |
| Matches live featured kits | **no → RED** | Live home featured: Club **900 USDC**, Menukaart **199 USDC**, Sponsorblad **199 USDC**, Lid **349 USDC**. Pakketten also lists Vakman **249 USDC**, Inbox-ops **299 USDC**. None of €199 / €249 / €299 / €349 / €900 appear in #111. |
| Live shop closed by this PR | **no → RED** | Live `robots.txt` still `User-agent: *` / `Disallow: /`. Live lede still “Charge blijft USDC op Solana.” |
| **PR #111 as shop** | **RED** | Wrong artifact |

GREEN is not a polish of these four HTML files. GREEN is not available on this PR.

---

## Artifact map (why the euro sticker is still the toy catalog)

`main` `catalog.html` sells four leftover tools:

| Leftover (`main`) | Price on `main` | Same SKU on PR #111 |
| --- | --- | --- |
| Solana Invoice | `9 USDC` | Offertebestand **€9** |
| CSV Cleaner | `49 USDC` | CSV-opschoner **€49** |
| Form to Email | `49 USDC` | Formulier naar e-mail **€49** |
| RSS to Webhook | `49 USDC` | RSS naar webhook **€49** |

#111’s done-check is `rg -i 'USDC|Phantom|Solana' index.html catalog.html pakketten.html betalen.html` going empty. That can pass while the **inventory** is still the 9/49 toys.

Unchanged on the same branch:

- `config.js` still `priceLabel: "9 USDC"`, `priceUsdc: 9`
- `kit-pay.html` still `<title>Solana Invoice — 9 USDC</title>` (old `index.html` renamed, unlinked)
- `shop.css` cream `#f6f3ee` + sage `#0c4a36` rounded cards — leftover catalog skin, not the live chalkboard

Live shop featured kits (fetched 2026-08-27):

| Live kit | Face on Surge today | EUR list the shop is supposed to show |
| --- | --- | --- |
| Club- of vzw-site | `900 USDC · ±€774` | **€900** |
| Menukaart + allergenen | `199 USDC · ±€171` | **€199** |
| Sponsorblad vzw | `Kit 199 USDC · ±€171` | **€199** |
| Vakman one-pager | `249 USDC` (pakketten) | **€249** |
| Inbox-ops | `299 USDC` (pakketten) | **€299** |
| Lid-inschrijving | `349 USDC · ±€300` | **€349** |

#111’s home has **two** cards (€9, €49). It never names club / menu / sponsor / lid / vakman / inbox.

---

## What #111 did get right (does not save the PR)

These are true and **do not** make a shop:

- Stamp is **OFFERTE**, not FACTUUR.
- `KBO/BTW: nog niet toegekend` — no invented `BE0`.
- `betalen.html` copy is “Betaalgegevens na akkoord” — no receive address on that page.
- Repo `robots.txt` is `User-agent: *` / `Allow: /`.

`Allow: /` on the leftover tree does not index the live shop. Live `https://sovereignforge.surge.sh/robots.txt` remains:

```
User-agent: *
Disallow: /
```

PR #112 already failed the **live** shop on USDC-on-face and that Disallow. #111 does not reopen that score. It also does not close it.

---

## Design-out

1. **Do not merge #111 as the shop.** Closing it as “euro sales face” would put a second, wrong catalog on `main` and still leave Surge printing 900 USDC.
2. **Builder ports nothing from it.** Do not copy `index.html` / `catalog.html` / `pakketten.html` / `betalen.html` / `shop.css` / the €9/€49 SKUs / the cream card grid onto SovereignForge. The live chalkboard (Young Serif + Atkinson, demos, privacy, Geel footer) is the shop tree. This PR is not a source.
3. **The only shop fix is a live Surge pass** on `sovereignforge.surge.sh`: euro on the face for the featured kits (€199 / €249 / €299 / €349 / €900), USDC only after kit choice on betalen, `robots.txt` must not `Disallow: /`. That pass is a different PR against the live origin. It is not a follow-up commit on `cursor/euro-shop-face-00e2`.

---

## GREEN is not available on this PR

A later commit on #111 cannot turn this RED into GREEN. Reasons that stay true no matter how many USDC strings are stripped:

- The SKUs would still be the leftover 9/49 toys unless the PR **becomes a different artifact** (club/menu/sponsor/lid/vakman/inbox at shop prices). That would be a new PR, not #111.
- The live origin would still be Surge. Git `Allow: /` does not flip live `Disallow: /`.
- PR #112’s live FAIL (USDC on the chalkboard face) is out of this diff.

Reviewer does not ask Builder to “fix #111.” Reviewer asks Builder to **leave #111**. Shop work starts from the live host, not from this catalog.

---

## This run

| Did | Did not |
| --- | --- |
| Read PR #111 files and claim text | Merge, rebase, or “fix” #111 |
| Fetched live home, pakketten, `robots.txt` | Port HTML/CSS from #111 to Surge |
| Compared leftover `main` 9/49 catalog to #111 €9/€49 | Send mail |
| Recorded PR #112 live FAIL as already scored | Spend, reprice, or invent a KBO |

**PR #111: RED (wrong artifact). GREEN not available. Do not merge as shop.**
