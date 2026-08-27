# REVIEWER — Builder PLAN (batch 03)

**Seat:** REVIEWER (new batch)  
**Stage:** Builder **PLAN** only  
**Date:** 2026-08-27  
**Artifact:** [PR #172](https://github.com/eyeskull2220/solana-invoice/pull/172) `docs/rgy-2026-08-27/builder/PLAN-one-pass.md` (head `ab569b0`)  
**This file:** judgment only. **No implement.** No design review. No shop HTML, kits, CSS, mail, or Surge.

GREEN for this stage only if the scorecard has **no RED and no YELLOW**. One yellow fails GREEN.

---

## Verdict

**PLAN stage: YELLOW.** GREEN is refused. There is **no RED** on this rewrite.

[PR #161](https://github.com/eyeskull2220/solana-invoice/pull/161) scored the old pack **RED** because it was a **punch list**. This file is the rewrite. The five #161 content gates are now **GREEN**. The page is one complete EUR-first shop job.

It still **jumps to CODE** immediately after a plan reviewer. Operator stage order is research + plan reviewers first, **then DESIGN, then design review, then CODE**. That skip is **YELLOW**.

This batch does not score live [sovereignforge.surge.sh](https://sovereignforge.surge.sh/). Live USDC / `Disallow: /` is world-state, not a defect in this markdown. Leftover [PR #111](https://github.com/eyeskull2220/solana-invoice/pull/111) is **not the shop**.

---

## What was scored (and what was not)

| Object | Used as |
| --- | --- |
| PR #172 `PLAN-one-pass.md` | **The only graded object.** |
| PR #161 `REVIEW-02-plan.md` | Gates this rewrite must close. Exhibit, not re-scored as the plan. |
| PR #122 / #125 | Named as the punch-list pack #161 refused. Not re-opened. |
| PR #159 `03-adv-design.md` | Proof DESIGN has not closed. **Not** a design review in this batch. |
| Live shop, leftover `main` HTML, kit hosts | **Out of scope.** This file scores the PLAN page, not CODE. |

---

## Frozen six (still locked)

| Kit | Face price |
| --- | ---: |
| Menukaart + allergenen | **€199** |
| Sponsorblad vzw | **€199** |
| Vakman one-pager | **€249** |
| Inbox-ops | **€299** |
| Lid-inschrijving | **€349** |
| Club- of vzw-site | **€900** |

Integers. No seventh chip. A demo is a demo.

---

## Scorecard

Worst row fails the stage. GREEN is refused.

| Gate | Score |
| --- | --- |
| One complete EUR-first shop pass vs punch list | **GREEN** |
| EUR-first face (no USDC / Solana / Phantom / crypto / wallet on the public face) | **GREEN** |
| Six kits only (table above) | **GREEN** |
| robots `User-agent: *` / `Allow: /` on shop + six kit hosts | **GREEN** |
| No junk SKUs; leftover #111 is not the shop | **GREEN** |
| Privacy STORE **Versie 3** | **GREEN** |
| Betalen = **Betaalgegevens na akkoord** | **GREEN** |
| Kill freelancer line, leftover SKUs, junk chips | **GREEN** |
| Origin: `shop/sovereignforge/` → `https://sovereignforge.surge.sh/` only; do not surge `main` | **GREEN** |
| Operator stage order (plan reviewer → **DESIGN** → design review → CODE) | **YELLOW** |
| Adjacent: fake KBO / mail send / FACTUUR stamp / this review surged | **GREEN** (does not save the stage) |
| **PLAN stage** | **YELLOW** |

**RED rows: none.**  
**YELLOW rows: operator stage order.**  
GREEN is therefore refused.

---

## 1. One complete pass vs punch list — **GREEN**

#161 refused GREEN because the written plan was strip / Allow / hide-address / spawn the next FIX seat.

#172 is **one** later job, not that sequence. It names:

- Origin of record: git `shop/sovereignforge/` **is** what deploys to `https://sovereignforge.surge.sh/` (preview, then cutover).
- Closed file set: `index.html`, `pakketten.html`, `betalen.html`, `contact.html`, `privacy.html`, `robots.txt`, shared chrome, fonts from the live chalkboard **copied into that tree**.
- Closed six, each with a live demo host before akkoord.
- Featured kit euro wraps in the **same** CODE pass (inbox-ops drops USDC + freelancer line).
- Kill list: freelancer, live `SITE.md`, “elf live kits”, junk SKUs, #111.
- Secretary acceptance on the live origin after cutover.
- Explicit: leftover #111, root `index.html` / `catalog.html` / `solana-invoice.html`, and `treasury-tools.surge.sh` are **not** the shop. Do not surge from `.`.

That is the missing one-pass page #161 asked for. It is not a punch list.

Do not read the done-check `rg` block as a FIX-seat spawn. Those greps are acceptance for the **same** later CODE pass.

---

## 2. EUR-first face — **GREEN**

Face prices in the file are **€199 / €199 / €249 / €299 / €349 / €900**. Integers.

The page forbids `USDC`, `Solana`, `Phantom`, `crypto`, and the treasury address in `<title>`, `<h1>`, lede, chips, CTAs, and meta on shop pages. Home lede is euro OFFERTE copy. Pakketten kills “Charge blijft USDC.” Betalen is not a wallet panel (gate 7).

This is stricter than #161’s “USDC only on `/betalen`.” The lock for this rewrite is **no coin on the public face**. The file matches that lock.

---

## 3. Six kits only — **GREEN**

The closed-six table is the frozen six, in the locked order, with the locked euro integers. Uitkomst lines are six, not seven.

Drop-list is explicit: pipeline, Peppol chase, dual-invoice, Peppol Ready, één klus / 9 USDC invoice, CSV / form-to-email / RSS, #111 €9/€49 toys, km-log / freelance-contract / retainer / dagtarief / FAQ / UTM / waitlist / paywall / intake / link-in-bio as shop rows. Seizoenskaart and named-club stay **VOORBEELD demos**, not SKU #7.

ideas-builder #81 services stay off the shop table.

---

## 4. robots `Allow: /` — **GREEN**

The file writes, for the shop **and** each of the six kit hosts:

```
User-agent: *
Allow: /
```

`Disallow: /` is named a fail. Missing `robots.txt` is named as not Allow. CODE is told to land `shop/sovereignforge/robots.txt` and a `robots.txt` in each `kits/<slug>/` folder, then push Allow to the six existing treasury hosts in the same pass.

Allow on leftover #111 is **not** treated as the shop. The origin in this plan is `sovereignforge.surge.sh`.

---

## 5. No junk SKUs; #111 is not the shop — **GREEN**

Explicit forbid: do not merge #111, do not port €9/€49 cards, do not treat hide-the-coin as the EUR pass. Root leftover invoice HTML is not the deploy folder. `catalog.html` is not on the shop origin.

Junk hosts are grepped out of shop HTML in the done-check. That is the #161 gate, closed in writing.

---

## 6. Privacy STORE Versie 3 — **GREEN**

The file ships STORE **Versie 3 — 27 augustus 2026** as the shop `privacy.html` copy. Locks present:

- Wie: Sasha, natuurlijke persoon in Geel, `sasha.de.vree.rene@gmail.com`
- Host/mailhost logs **niet geverifieerd** → no cookie banner
- Gmail named as a dienst **buiten de EER**, alleen om te antwoorden; no SCC / adequacy claim
- No USDC / IBAN / kaartnummer on the page
- No AVG-conform badge
- One page on the shop origin; footer link required
- Do not restore Versie 1 “Betaling is on-chain in USDC”

This is the GREEN fill-in from [PR #152](https://github.com/eyeskull2220/solana-invoice/pull/152), not a blank grep card.

---

## 7. Betalen = Betaalgegevens na akkoord — **GREEN**

`betalen.html` H1 is **`Betaalgegevens na akkoord.`** Lede: no rekeningnummer, no ontvangstadres, no kaartformulier. Volgorde: kies kit → open voorbeeld → akkoord per mail → gegevens **apart, later**. Forbidden: treasury address `96BT6…buHk3`, mint, QR, copy-address, `USDC`, `Solana`, `Phantom`, radios that reveal a pay panel.

The page exists as a step, not a coin door. Charge copy is not on the face.

---

## 8. Kill freelancer / leftover SKUs / junk chips — **GREEN**

Shop copy must not say hire-me / freelancer / day-rate. Inbox-ops kicker is not “Demo freelancer · Antwerpen.” Root leftover “For freelancers…” is not deployed. `SITE.md` is not added to the git shop; live stub must 404 on cutover. No “Elf live kits” / “Alle 11 pakketten.”

Operator is not the freelancer. Team delivers.

---

## 9. Origin of record; do not surge `main` — **GREEN**

Live shop after cutover: **`https://sovereignforge.surge.sh/` only.** Git source: `shop/sovereignforge/`. CODE publishes that folder, never repo root. Do not surge `main`. Do not treat leftover #111 as the EUR pass.

This **PLAN** PR does not run Surge. That sentence is true of #172. It does not make the next-seat skip GREEN (gate 10).

---

## 10. Operator stage order — **YELLOW**

This file is **PLAN**. Operator order:

1. Research + plan reviewers  
2. **DESIGN**  
3. **Design review**  
4. **CODE** (preview, then cutover of `shop/sovereignforge/` onto `sovereignforge.surge.sh` only)

#172 writes a three-step sequence that **skips 2 and 3**:

1. This PR — merge this markdown only.  
2. A different reviewer scores this file against the #161 PLAN gates.  
3. **CODE** — one PR, six kit euro faces, preview, then cutover.

Same skip, verbatim, as the next-seat line: *“a **different** reviewer scores this file. Then CODE.”*

Same skip after GREEN: *“After a **different** reviewer marks **this** page GREEN”* → land the tree → `npx surge shop/sovereignforge/ sovereignforge-eur-preview.surge.sh` → cutover `sovereignforge.surge.sh`.

The chrome section is the same skip in another heading: *“Look and chrome (enough for CODE, **not a second DESIGN punch**).”* It tells CODE to reuse live chalkboard tokens (`--board` / `--chalk` / Young Serif + Atkinson) in **that same CODE pass**. That is DESIGN collapsed into CODE.

DESIGN has not closed. [PR #159](https://github.com/eyeskull2220/solana-invoice/pull/159) `03-adv-design.md` is an adversarial design pass on the live chalkboard (**overall RED**). This batch does **not** re-score that file. It only notes: a PLAN that says “enough for CODE, not a second DESIGN punch” is jumping the queue.

The heading *“Sequence (this file does not skip it)”* is false. It does not skip punch-list CODE. It **does** skip DESIGN and design review.

This is **YELLOW**, not RED. The shop job on the page is complete. The operator order is not.

---

## Adjacent GREEN (does not save PLAN)

- No invented KBO / `BE0`. Stamp remains `KBO/BTW: nog niet toegekend`.
- This PLAN does not send mail. This review did not send mail.
- Stamp is OFFERTE / VOORBEELD, not FACTUUR. Negation `geen wettelijke factuur` is allowed.
- This review did not write shop HTML, did not publish to Surge, did not surge `main`.

---

## Design-out (the yellow)

**After this reviewer: DESIGN. Not live Surge.**

Do not start CODE from this file. Do not treat this YELLOW as permission to land `shop/sovereignforge/` or to `npx surge` preview or cutover. Do not surge `main`. Do not merge leftover #111 as the shop.

Exact rewrite for GREEN on gate 10 (PLAN page only):

| Now in #172 | Required |
| --- | --- |
| This PR → plan reviewer → **CODE** (preview then cutover) | This PR → plan reviewer → **DESIGN** → **design review** → **CODE** |
| “Look and chrome (enough for CODE, not a second DESIGN punch)” | Chrome is **DESIGN**. CODE does not pick `--board` / cream / Inter from this PLAN. |
| Next seat: “Then CODE” | Next seat: **DESIGN** (docs, not a ship). Then a **different** reviewer scores DESIGN. Then CODE. |

CODE, when it eventually runs, remains the one pass already written: git `shop/sovereignforge/` onto **https://sovereignforge.surge.sh/** only, frozen six, Versie 3, Betaalgegevens na akkoord, robots Allow, no coin on the face, leftover #111 not the shop. That job is not in dispute. **When** it runs is.

This reviewer does not write the DESIGN page. This reviewer does not patch #172.

---

## GREEN looks like (this PLAN file only)

All of the following. Content gates 1–9 already hold in #172. Gate 10 does not.

1. **Keep** the one-pass shop job, frozen six, Versie 3, betalen lock, robots Allow, #111 forbid, do-not-surge-`main`.
2. **Rewrite Sequence** so it cannot be read as plan-reviewer → CODE. Insert DESIGN, then design review, before CODE.
3. **Kill** “enough for CODE, not a second DESIGN punch” and “Then CODE. Not this run.” Next seat after this reviewer is DESIGN, not live Surge.
4. **Do not** treat a later CODE GREEN, or a live cutover, as a PLAN GREEN. Live origin matching the job is Builder CODE, after design review.

Until 2–3 are in the PLAN page, this review stays **YELLOW**.

---

## This run

| Did | Did not |
| --- | --- |
| Read PR #172 `PLAN-one-pass.md` as the only graded object | Design review of chalkboard vs paper |
| Scored the rewrite against #161 PLAN gates | CODE review, shop HTML, kits, CSS |
| Locked origin, six kits, Versie 3, betalen, robots, kill list as GREEN in writing | Mail, KBO, reprice, rewrite live robots |
| Scored the plan-reviewer → CODE skip **YELLOW** | Surge publish, surge `main`, merge or “fix” #111 |
| Wrote the design-out: after this reviewer, **DESIGN** | Implement DESIGN or CODE |

**PLAN stage: YELLOW.** GREEN not available (yellow present; no reds).
