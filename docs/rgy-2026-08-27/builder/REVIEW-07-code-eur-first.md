# REVIEWER — Builder CODE EUR-first (batch 07)

**Seat:** REVIEWER (new batch; **not** the author of [PR #213](https://github.com/eyeskull2220/solana-invoice/pull/213))
**Stage:** Builder **CODE** only
**Date:** 2026-08-27
**Artifact:** [PR #213](https://github.com/eyeskull2220/solana-invoice/pull/213) head `0f4f26b` (`cursor/eur-first-shop-code-6d16`)
**This file:** judgment only. **No implement.** No shop HTML edit. No kits edit. No mail. No Surge. No merge.

GREEN for this stage only if the scorecard has **no RED and no YELLOW**. One yellow fails GREEN. Start from zero. The PR body is not the tree.

---

## The machine (said back)

SovereignForge is **one** Belgian income machine. Success is **money in operator accounts** **and** a shop a Flanders vzw secretaris will forward: one light Dutch stuk, whole-euro integer. Kits / mails / paper / cloud are parts.

Live shop later: **https://sovereignforge.surge.sh/** from git **`shop/sovereignforge/`**. Leftover root `index.html` / `catalog.html` / `solana-invoice.html` is **not** the shop. Frozen six euro. **No USDC on the face.** Operator is **not** the freelancer. Still **OFFERTE**. `KBO/BTW: nog niet toegekend`. No FACTUUR. No Peppol claim. No invented `BE0`.

Live host stays **held** until CEO unlocks cutover **after** this review is GREEN **and** a preview exists. This CODE PR did not Surge. This review does not preview. **Do not surge `main`.**

[PR #208](https://github.com/eyeskull2220/solana-invoice/pull/208): a secretaris forwards a **stuk**, not a chalkboard, not leftover invoice HTML.

Implements DESIGN [#202](https://github.com/eyeskull2220/solana-invoice/pull/202) after DESIGN review GREEN [#204](https://github.com/eyeskull2220/solana-invoice/pull/204). PLAN GREEN [#195](https://github.com/eyeskull2220/solana-invoice/pull/195) does **not** substitute for this CODE score.

---

## Verdict

**CODE stage: RED.**

The shop origin `shop/sovereignforge/` is a real Dutch OFFERTE blad: euro prijsregel in the first viewport, stamp OFFERTE, Sasha · Geel, mailbox, Versie 3, robots `Allow: /`, no coin strings. That is **not** GREEN for the pack. GREEN requires no red and no yellow on this CODE tree. It has both.

Holes that remain:

1. **RED — club demo is not a clean VOORBEELD.** This CODE pass *landed* a kit **pay-box** and leftover **copy-address** rail on `kits/club/`. Operator Gmail sits on the public demo.
2. **YELLOW — inbox-ops wrap first viewport still reads Antwerpen.** Kicker `Studio Noord · demo KMO · Antwerpen` occupies the operator-identity slot. Demo freelancer / hire-me are gone. The hole is the slot.

Author of #213 (`bc-4744b394`) is not this seat (`bc-82aaa419`). This file does not ship HTML. This file does not publish. This file does not merge.

**After this reviewer: not preview, not cutover, not mail.** CODE must kill the club pay rail and the Antwerpen-as-seller kicker before GREEN is available. Preview Surge from `shop/sovereignforge/` only after a later CODE review is GREEN. **Do not surge `main`.**

---

## What was scored (and what was not)

| Object | Used as |
| --- | --- |
| PR #213 `shop/sovereignforge/` | **Shop origin.** Served locally from the CODE tree. First viewport measured at 390×844 and 1280×800. |
| PR #213 `kits/{menu,sponsor,vakman,inbox-ops,lid}/index.html` + `wrap.css` + `robots.txt` | **Sell wraps.** Same-pass as DESIGN §14 / PLAN §9. |
| PR #213 `kits/club/` | **Featured club host.** User lock: VOORBEELD, **no pay-box**. |
| PR #202 DESIGN + PR #204 REVIEW-05 | Locks this CODE must paint. **Not** this grade. |
| PR #188 PLAN §8 privacy HTML | Copy lock for `privacy.html`. Compared. |
| Live https://sovereignforge.surge.sh/ | **Out of scope.** Held USDC-first world-state. This PR did not Surge. This review did not fetch it as the score. |
| Leftover `main` `index.html` / `catalog.html` / `solana-invoice.html` | **Not the shop.** Not grepped as the face. |
| Inner kit artefacts (`menu.html`, `lid.html`, sponsor/vakman `offerte.html`, Golfbreker pages as *product documents*) | Unchanged-is-fine **except** where this CODE glued sell/pay chrome onto the club demo. |
| Mail, Surge, merge, KBO number | **Not done.** Not invented. |

The author’s “Locks honoured” list is **not** the colour.

---

## Frozen six (still locked)

| Kit | Face price | Shop post | Wrap face |
| --- | ---: | --- | --- |
| Menukaart + allergenen | **€199** | €199 | €199 |
| Sponsorblad vzw | **€199** | €199 | €199 |
| Vakman one-pager | **€249** | €249 | €249 |
| Inbox-ops | **€299** | €299 | €299 |
| Lid-inschrijving | **€349** | €349 | €349 |
| Club- of vzw-site | **€900** | €900 | €900 on the **pay-box**, not on a paper wrap |

Integers. No seventh chip. Order on the shop blad: menu → sponsor → vakman → inbox-ops → lid → club. Club is **€900**, not leftover **€774**.

---

## This-run checks (2026-08-27)

Served `shop/sovereignforge/` + `kits/` from head `0f4f26b` at `http://127.0.0.1:8765/` only. **Did not publish to Surge.**

| Check | Result |
| --- | --- |
| PR #213 origin vs leftover root | Shop files live under `shop/sovereignforge/`. Root invoice HTML is still the `main` leftover. Not surged. |
| Author of #213 vs this seat | Different agent (`bc-4744b394` wrote CODE; this batch is `bc-82aaa419`). |
| 390×844 home | Prijsregel `€199 · €199 · €249 · €299 · €349 · €900` in view (top 481). Both CTAs in view (bottom 683). Stamp `OFFERTE`. Kicker `Sasha · SovereignForge · Geel`. No horizontal scroll (`scrollWidth` 374 ≤ 390). Document height **2375px** (hard cap 2400; target 2200). |
| 1280×800 home | Same prijsregel in view (top 390). Both CTAs in view. Posten: name left / price right, same baseline. No dock. Radius 0. Type Source Sans 3 / Source Serif 4. Paper `#ffffff`, ink `#171717`. |
| Click walk | Home → `#pakketten` → Contact (`Alleen mail.`) → footer Betalen (`Betaalgegevens na akkoord.`). |
| Forbidden on shop HTML | `USDC` / `Solana` / `Phantom` / `crypto` / `wallet` / `chalkboard` / `€774` / `je` / `jouw` / invented `BE0` = **0**. |
| Kill list on shop | No leftover 9/49, Peppol Ready, dual-invoice, één-klus, pipeline/chase chips, hire-me, Demo freelancer, `SITE.md`, `editor.html`. |
| Privacy | Lede **Versie 3 — 27 augustus 2026**. Host/mailhost **niet geverifieerd**. Gmail buiten de EER, één zin, no SCC/adequacy *claim*. No AVG-conform badge. No cookie banner element. Matches PLAN §8. |
| Betalen | H1 **Betaalgegevens na akkoord.** No rekeningnummer, no ontvangstadres, no QR, no copy-address, no pay-to. Betalen is footer-only, not a primary tab. |
| robots | Shop + six kit folders: `User-agent: *` / `Allow: /`. |
| Club `kits/club/index.html` | VOORBEELD banner in first viewport. **`aside.paybox#kit-pay`** at y≈2874: `Deze kit · €900` + operator Gmail. |
| Club inner pages | `Kopieer adres` on agenda / contact / lidworden / over. Target `#pay-addr-foot` **missing**. `site.js` `PAY_TO = ""`. Click fails: “Kopieer handmatig: selecteer het adres.” |
| Inbox-ops wrap | First-viewport kicker **Studio Noord · demo KMO · Antwerpen**. Price €299. Footer Sasha · Geel is below the fold. |
| This review wrote HTML / sent mail / ran Surge / merged | **No.** |

---

## Scorecard

Worst row fails the stage. GREEN only if every row is GREEN.

| Gate | Score |
| --- | --- |
| First viewport euro only (frozen six; no USDC / Solana / Phantom / crypto / wallet / chalkboard / coin / €774) | **GREEN** on `shop/sovereignforge/` |
| Stamp OFFERTE; u/uw; Sasha · SovereignForge (Geel); mailbox; Betalen = Betaalgegevens na akkoord; no pay-to on first paint | **GREEN** on the shop |
| Privacy STORE Versie 3 (27 augustus 2026); host logs UNVERIFIED; Gmail buiten de EER, one true sentence; no SCC/adequacy claim; no AVG badge; no cookie banner | **GREEN** |
| robots `Allow: /` on shop + featured kits; no leftover 9/49, Peppol Ready, dual-invoice, één-klus, pipeline/chase chips, hire-me, Demo freelancer | **GREEN** |
| Inbox-ops wrap does not read as operator-as-freelancer | **YELLOW** |
| Club demo stays VOORBEELD, **no pay-box** | **RED** |
| Sell wraps match shop paint (inner artefacts may stay) | **YELLOW** (club host is 3-band + pay-box, not a paper wrap) |
| No Surge / no preview / no merge / no mail / no invented KBO in this seat | **GREEN** |
| **CODE stage** | **RED** |

**RED rows: 1.**
**YELLOW rows: 2.**
GREEN is therefore **not** available.

---

## 1. Shop first viewport — **GREEN** (origin only)

Hard-fail list on `shop/sovereignforge/{index,pakketten,betalen,contact,privacy}.html` plus `styles.css`: USDC, Solana, Phantom, crypto, wallet, chalkboard, coin, €774, wood PNG, brass CTA, freelancer-as-seller, Peppol Ready, dual-invoice, één-klus, pipeline, chase, leftover 9/49.

Measured on `index.html`:

- **390×844:** kicker, OFFERTE stamp, H1, lede (`u`), prijsregel, both CTAs, all inside 844px. First post starts at 683 — may peek; no phone PNG. Horizontal scroll **0**. No `overflow-x: hidden` lie.
- **1280×800:** prijsregel + CTA row in the first 800px. Frozen six on the blad. Name left / price right.

Title `SovereignForge — voorstel voor het bestuur`. Meta is euro OFFERTE, not coin. Favicon is ink `SF` on white.

This GREEN does **not** cover `kits/club/` first paint (3-band gold/navy). That is §6.

---

## 2. OFFERTE, u/uw, operator, Betalen — **GREEN** (shop)

Shop face:

- Stamp `OFFERTE` (outline, not a filled banner). Footer `OFFERTE / VOORBEELD · geen wettelijke factuur`. Negation `geen wettelijke factuur` / `geen BTW-factuur (OFFERTE)` is allowed. No FACTUUR as a document stamp.
- Address: `u` / `uw` on prescribed copy. `je` / `jouw` = 0 on shop HTML.
- From-name: `Sasha · SovereignForge · Geel` (kicker + footer). Contact colophon `SovereignForge · Geel / België · KBO/BTW: nog niet toegekend.`
- Mailbox: `sasha.de.vree.rene@gmail.com` only.
- Betalen H1 **`Betaalgegevens na akkoord.`** Lede: no rekeningnummer, no ontvangstadres, no kaartformulier. No pay-to on home first paint. No IBAN, no QR, no copy-address on the shop.

`KBO/BTW: nog niet toegekend` only. No invented number.

---

## 3. Privacy STORE Versie 3 — **GREEN**

`privacy.html` lede: **`Versie 3 — 27 augustus 2026. Geen keurmerk. Geen banner.`**

PLAN §8 copy is on disk: Wie in Geel; OFFERTE not FACTUUR-module; gegevens/rechtsgrond; geen kaart/IBAN; trackers **niet geverifieerd** (host logs UNVERIFIED); Gmail buiten de EER **alleen om uw vraag te beantwoorden**; **Deze pagina noemt geen SCC- of adequacy-claim**; no AVG-conform badge; no banner element. USDC = 0 on this page.

The words SCC / adequacy appear only as the locked negation. That is not a claim.

---

## 4. robots + kill list — **GREEN**

`robots.txt` on shop and on menu / sponsor / vakman / inbox-ops / lid / club:

```
User-agent: *
Allow: /
```

Shop pakketten is the same six posten. No 9/49 rows. No Peppol Ready. No dual-invoice. No één-klus SKU. No pipeline/chase chips. No hire-me. No Demo freelancer. `editor.html` is absent (STOP). No `SITE.md` under the shop.

Shop uitkomst line `Geen freelancer-desk.` is the PLAN/DESIGN negation of the freelancer line, not hire-me copy.

---

## 5. Inbox-ops Antwerpen kicker — **YELLOW**

DESIGN/PLAN allowed `Studio Noord · demo KMO · Antwerpen` as the kill of **Demo freelancer · Antwerpen**. This CODE used that string.

The hole is **where** it sits. Menu / sponsor / vakman / lid wraps put **`Sasha · SovereignForge · Geel`** in the kicker — the first-viewport identity slot. Inbox-ops puts **Studio Noord · Antwerpen** there. Operator Geel is only in the footer, below the fold.

A Flanders secretaris opening `inbox-ops-treasury` (shop “Open het voorbeeld”) sees Antwerpen in the same slot other kits use for the seller. “Studio Noord” is one rename from killed “Desk Noord.” Copy says `demo KMO` and `Wij solliciteren niet als menselijke developer`. That negation does not move the kicker.

Not RED: `Demo freelancer`, hire-me, USDC, pay-to, mint are gone. Price is **€299**. CTA is OFFERTE / Betaalgegevens na akkoord.

**Fix before GREEN:** drop the kicker, or make it the stencil (`demo KMO · VOORBEELD`) without Antwerpen in the seller slot, and put `Sasha · SovereignForge · Geel` where the other wraps put it.

---

## 6. Club demo pay-box — **RED**

User lock: club demo stays **VOORBEELD**, **no pay-box**. Inner artefacts unchanged is fine. This CODE pass did **not** leave Golfbreker untouched: it **added** `kits/club/` to git from empty `main` and glued sell/pay chrome onto the demo.

Evidence on head `0f4f26b`:

| Surface | What is there |
| --- | --- |
| `kits/club/index.html` | VOORBEELD banner (good). Then 3-band Golfbreker (product). Then **`<aside class="paybox" id="kit-pay">`**: `Deze kit · €900`, `Prijs €900. Betaalgegevens na akkoord.`, **`sasha.de.vree.rene@gmail.com`**. Footer `.foot-pay` repeats €900 + operator Gmail. |
| `agenda.html` / `contact.html` / `lidworden.html` / `over.html` | `.foot-pay` + **`<button data-copy="#pay-addr-foot">Kopieer adres</button>`**. `#pay-addr-foot` **does not exist**. |
| `site.js` | `var PAY_TO = ""` still runs clipboard copy. Empty target → fail copy: “Kopieer handmatig: selecteer het adres.” That sentence is leftover **wallet settlement** UX. |
| PLAN §9 | Demo mail inside kits stays RFC 2606 (`info@golfbreker.example`). **Never the operator Gmail on the public demo.** This tree puts the operator mailbox on the demo home pay-box and on four inner footers. |

First viewport of the club host is the gold/navy voorbeeld, not the pay-box (pay-box ≈ y 2874 at 390). That does **not** save the gate. The gate is **no pay-box**, not “pay-box below the fold.” A secretaris who clicks **Open het voorbeeld** on the shop blad lands on this host.

No USDC string on the club HTML grepped. The coin rail survived as **Kopieer adres** + empty `PAY_TO` + `.paybox`. Stripping the address and leaving the button is not a kill.

**Fix before GREEN:** delete `.paybox` / `#kit-pay` / `.foot-pay` sell chrome / `Kopieer adres` / copy + `PAY_TO` from `site.js`. Keep VOORBEELD banner and RFC 2606 club mail. If the kit needs a sell wrap, it is a **paper wrap in front of** Golfbreker (same paint as menu/sponsor), not a pay-box inside the demo.

---

## 7. Sell wraps vs shop paint — **YELLOW** (club)

Five wraps (`kits/menu|sponsor|vakman|inbox-ops|lid/index.html` + `wrap.css`) are the shop sheet: Source Serif 4 + Source Sans 3, white, ink, 0 radius, OFFERTE stamp, euro integer, Privacy → shop, Betaalgegevens na akkoord. Inner artefacts behind those wraps were not restyled. That match is real.

Club has **no** `wrap.css` sell wrap. The kit host index **is** the 3-band demo. DESIGN §14 required sell-wrap paint on the six live hosts. PLAN §9 said keep Golfbreker as VOORBEELD. This CODE followed PLAN for the costume and then failed the user lock by selling from inside it (§6).

Not a second RED for gold tape on Golfbreker itself (inner artefact). The yellow is: **Open het voorbeeld** for club is not the shop blad paint.

---

## Notes (not colour)

- Home length 2375px at 390 is inside the 2400 hard cap, above the 2200 target. Second commit tightened post padding to 12px on small viewports (DESIGN said 20px). Length trade, not a costume.
- Shop canonicals already name `https://sovereignforge.surge.sh/`. Live origin is still held USDC-first. That is world-state until a later preview/cutover. This review does not treat live Surge as this tree.
- Shop “Open het voorbeeld” points at existing treasury hosts. Git `kits/` is the CODE. Those hosts are **not** this tree until a later preview republish. This seat did not republish.
- Wordmark `href="/"` is correct when `shop/sovereignforge/` is the document root. It is wrong if someone serves the repo root. Do not surge `main`.
- `Geen freelancer-desk.` on the shop inbox-ops post is DESIGN uitkomst copy, not a freelancer line.
- Privacy heading `Geen kaart, geen IBAN` is PLAN §8, not a pay panel.

---

## What GREEN would require (not this PR)

1. Club host: no `.paybox`, no `Kopieer adres`, no `PAY_TO` copy rail, no operator Gmail on Golfbreker pages. VOORBEELD stays. Optional: paper sell wrap in front, same paint as the shop.
2. Inbox-ops wrap: Antwerpen out of the seller kicker. Operator Geel in the same slot as the other wraps.

Then a **different** CODE reviewer scores again. Preview is after that GREEN. Cutover later. Still OFFERTE. Still `KBO/BTW: nog niet toegekend`.

---

## This run

| Did | Did not |
| --- | --- |
| Scored PR #213 CODE tree from zero, adversarial | Rubber-stamp the PR body |
| Served origin locally; measured 390 and 1280; clicked Home → posten → Contact → Betalen | Publish to Surge; preview host; fetch live chalkboard as this grade |
| Named RED (club pay-box + copy-address) and YELLOW (inbox-ops Antwerpen kicker) | Edit shop HTML; edit kits; merge #213 |
| Kept leftover root invoice HTML as **not the shop** | Invent a KBO/BTW number; send mail; stamp FACTUUR |

**CODE stage after this file: RED.** Next seat is **CODE fix**, not preview, not cutover.

End. No shop HTML. No mail. No Surge. No merge.
