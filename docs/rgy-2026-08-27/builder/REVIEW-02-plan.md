# REVIEWER — Builder PLAN (batch 02)

**Seat:** REVIEWER (new batch)  
**Stage:** Builder **PLAN** only  
**Date:** 2026-08-27  
**This file:** judgment only. **No implement.** No design review. No shop HTML, kits, or CSS.

GREEN for this stage only if the scorecard has **no RED and no YELLOW**. One yellow fails GREEN.

---

## Verdict

**PLAN stage: RED.** The written Builder plan is a **punch list**, not **one complete EUR-first shop pass**.

Artifacts for this batch are only:

| Artifact | File | Their verdict |
| --- | --- | --- |
| [PR #122](https://github.com/eyeskull2220/solana-invoice/pull/122) | `docs/rgy-2026-08-27/builder/02-adv-plan.md` | **RED** — punch-list rebuilds; no one-pass shop plan; junk SKUs on home |
| [PR #125](https://github.com/eyeskull2220/solana-invoice/pull/125) | `docs/rgy-2026-08-27/builder/08-rgy-plan.md` | **RED** — all five PLAN gates RED; live “elf live kits”; #111 is toys |

This batch does not reopen DESIGN or CODE. It does not score fonts, privacy Versie 3, or unpublished shop trees. Leftover [PR #111](https://github.com/eyeskull2220/solana-invoice/pull/111) is **not the shop** and is not a PLAN substitute.

---

## Frozen six (EUR-first shop)

A complete PLAN names these six kits and these euro face prices. Nothing else on home or pakketten.

| Kit | Face price |
| --- | ---: |
| Menukaart + allergenen | **€199** |
| Sponsorblad vzw | **€199** |
| Vakman one-pager | **€249** |
| Inbox-ops | **€299** |
| Lid-inschrijving | **€349** |
| Club- of vzw-site | **€900** |

USDC, if it exists at all, is only on `/betalen` after a kit is chosen. Not in `<title>`, `<h1>`, lede, or chips.

---

## Scorecard

Worst row fails the stage. GREEN is refused.

| Gate | Score |
| --- | --- |
| One complete EUR-first shop pass vs punch list | **RED** |
| EUR-first face | **RED** |
| Six kits only (table above) | **RED** |
| robots `Allow: /` in the plan | **RED** |
| No junk SKUs; #111 is not the shop | **RED** |
| Adjacent: fake KBO / mail send / FACTUUR stamp in the plan | **GREEN** (does not save the stage) |
| **PLAN stage** | **RED** |

Yellows in #122 (reviewer-as-gate, week-scale research #81, robots Allow only on the leftover tree) also refuse GREEN. They are not promoted to save any red row.

---

## 1. One complete pass vs punch list — **RED**

A complete PLAN is one page that, in a **single** later CODE pass, ships a closed shop together:

- `index.html` (home)
- `pakketten.html`
- `betalen.html`
- `privacy.html` (footer link)
- `contact.html`
- `robots.txt` → `User-agent: *` / `Allow: /`
- the frozen six, each with a live demo before pay
- one host of record (git tree = live shop)

#122 A1 / A3 and #125 gate 1 agree: that page does not exist. What exists is a sequence of strips:

1. Live Surge chalkboard already has surfaces — then eleven kits, USDC on the face, `Disallow: /`.
2. Live `SITE.md` is a stub that points at those USDC faces (#122 A2).
3. [PR #111](https://github.com/eyeskull2220/solana-invoice/pull/111) rebuilds a **different** tree: euro labels on the 9/49 leftover catalog.
4. FIX seats (hide-coin + robots, named-club, seizoenskaart) spawned because PLAN never froze the shop.

Punch-list tells CODE to strip strings, Allow robots on the leftover repo, hide an address. It does not say which origin is canonical, which six SKUs live, or what a secretary sees after one merge. #111 can merge and live sovereignforge still says 900 USDC. That is not one pass.

**#122 vs #125 on “how many offers.”** Adversarial #122 still talks CEO “one week-scale offer.” Reviewer #125 freezes **six kits**. This batch locks the six-kit table above as the shop PLAN. The disagreement is more evidence there is no single complete plan — not a license to ship eleven, five, or three.

---

## 2. EUR-first — **RED**

Face price is `€N`. Euro in a second clause next to USDC is FAIL.

From the artifacts (not a new CODE audit):

| Surface they opened | Face |
| --- | --- |
| ideas-builder #81 | USDC (1,500 / 1,800 / 2,500 / 3,500 / 2,000) |
| Live `sovereignforge.surge.sh` | **900 USDC** · ±€774; lede “Charge blijft USDC.” |
| Live pakketten | USDC column first; “Elf live kits.” |
| #111 “euro shop” | €9 / €49 on leftover toys — euro sticker, wrong catalog |
| `main` catalog | `9 USDC` / `49 USDC` |

#122 A2: live `SITE.md` still says USDC-on-face **by reference**. #125 gate 2: partial euro on `treasury-tools.surge.sh` does not make PLAN green.

There is no Builder PLAN sentence that says: every shop/catalog chip is `€199` / `€249` / `€299` / `€349` / `€900` with no USDC in title, h1, lede, or card.

---

## 3. Six kits only — **RED**

Required: the frozen six. Not eleven. Not five services. Not three toys.

#125 lists live pakketten as **eleven** rows and names the drop-list. #122 A4: neither live home nor #111 home matches the board.

| Count | Whose plan | What it sells |
| ---: | --- | --- |
| 11 | Live pakketten | Club / menu / sponsor / lid / vakman / inbox **plus** pipeline, Peppol chase, dual-invoice, Peppol Ready, één klus |
| 5 | ideas-builder #81 | Week-scale **services** in USDC — not shop kits |
| 3 | #111 | Offertebestand €9, studio-tools €49, één opdracht €49 |
| 6 | **this batch** | Menu €199, sponsor €199, vakman €249, inbox-ops €299, lid €349, club €900 |

No PLAN document in the artifacts freezes those six names **and** those euro integers together. A later PLAN rewrite that adds seizoenskaart or named-club VOORBEELD as SKU #7 stays RED. A demo is a demo, not a seventh chip.

---

## 4. robots `Allow: /` — **RED**

PLAN must put `User-agent: *` then `Allow: /` on the public shop (and the six kit hosts). `Disallow: /` is a hard fail.

#122 B6 is **YELLOW** only because #111 wrote Allow on the leftover tree while live shop stays Disallow. For PLAN, that is still **RED**: the plan never states Allow on the origin REVIEWER scores. #125 gate 4: both public hosts `Disallow: /`; missing `robots.txt` on `main` is not Allow; a later FIX seat for robots is proof PLAN omitted it.

Allow on #111 does not index the shop. The shop is not #111.

---

## 5. No junk SKUs; leftover #111 is not the shop — **RED**

Junk = 9/49 leftover HTML, dual-invoice as a price row, Peppol Ready, één klus, and any SKU that exists because a PR needed to ship something.

#122 A4 and #125 gate 5: live pakketten still dumps dual-invoice / Peppol Ready / één klus; English toys (CSV / form-to-email / RSS / Solana Invoice 9 USDC) still exist as SKUs. #111 **re-centres** those toys as the shop face.

**PR #111 is leftover catalog, not the shop.** Do not merge it as SovereignForge. Do not port its €9/€49 cards, cream catalog, or `rg` four-file done-check. Builder PLAN that treats #111 as the EUR pass stays RED even if every USDC string on those four files is gone.

Drop-list (off home and off pakketten): dual-invoice, Peppol Ready, één klus, pipeline/chase as shop chips, CSV / form-to-email / RSS, Solana Invoice 9 USDC, retainer/km-log/FAQ/UTM/waitlist/paywall/intake as shop rows.

---

## Adjacent GREEN (does not save PLAN)

These are true in the artifacts and stay locks. They are not GREEN for the **stage**:

- Plans do not invent a KBO / `BE0`. Stamp remains `KBO/BTW: nog niet toegekend`.
- Plans scored here do not send mail.
- Stamp is OFFERTE / VOORBEELD, not FACTUUR.

---

## GREEN looks like (PLAN rewrite only)

A **single** Builder PLAN page, merged before CODE, with **zero** red or yellow on the scorecard:

1. **One pass:** home, pakketten, betalen, privacy, contact, `robots.txt` Allow — one PR, one host of record. Git shop HTML **is** what deploys. No parallel leftover catalog. Rewrite or remove live `SITE.md` so it no longer points at USDC faces.
2. **EUR-first:** frozen six at **€199 / €199 / €249 / €299 / €349 / €900**. No `USDC` / Solana / crypto in title, h1, lede, or chips. Charge copy only on betalen after kit choice. Pakketten does not say “Charge blijft USDC.”
3. **Six kits only.** Drop-list explicit. No seventh chip. #81 services stay off the shop table unless they **are** one of the six.
4. **robots Allow** on shop + six kit hosts, in the plan, matching the file that will go live.
5. **#111 is not the shop.** Explicit forbid: do not merge, port, or treat hide-the-coin as the EUR pass.

Until that page exists, Builder PLAN stays **RED**. This file does not write it.

---

## This run

| Did | Did not |
| --- | --- |
| Read PR #122 `02-adv-plan.md` and PR #125 `08-rgy-plan.md` | Design review |
| Scored PLAN: one complete EUR-first pass vs punch list | CODE review, shop HTML, kits, CSS, Surge |
| Locked the six kits and euro prices | Merge or “fix” #111 |
| Recorded leftover #111 as not the shop | Mail, KBO, reprice, rewrite robots live |

**PLAN stage: RED.** GREEN not available (reds present; #122 yellows would also refuse GREEN).
