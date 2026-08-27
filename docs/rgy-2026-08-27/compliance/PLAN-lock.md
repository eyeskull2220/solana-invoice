# PLAN lock — Compliance (designs out #169 yellows)

**Seat:** FIX (Compliance PLAN)
**Date of this page:** 2026-08-27
**Stage:** PLAN only. **Docs only. No CS mail. No send. No seconds to the 18.**
**This file is the PLAN.** It is not a stamp. It is not a lawyer. It is not a KBO, not live Stripe, not FACTUUR, not Peppol, not AVG-conform.

YELLOW in [PR #169](https://github.com/eyeskull2220/solana-invoice/pull/169) (`REVIEW-02-plan.md`) because [PR #135](https://github.com/eyeskull2220/solana-invoice/pull/135) `02-adv-plan.md` planned the **wrong NOW jobs**. This page closes those four yellows in one pass. It does not licence a filing, a send, or a merge of #135 as “NOW done.”

A later Compliance / Builder / Scout agent follows **this page**. Not #135 Task 1 (blanks + 40-line grep). Not #135 Task 2 (`stop` body). Not #116 §12 (`UITSCHRIJVEN`). Not #117 as a send template.

---

## 0. Mandate (locked before colour)

| Bucket | Items | Meaning on this page |
| --- | --- | --- |
| **WAIT** | KBO · live Stripe/Mollie · FACTUUR · Peppol | Do **not** execute. Stay **R**. Compliance **HOLDS**. Nobody stamps. |
| **NOW** | STORE **Versie 3** privacy **copy** (already **GREEN** in [PR #152](https://github.com/eyeskull2220/solana-invoice/pull/152)) · **one** opt-out on **future CEO-gated** mail | Whole copy / gate jobs. Still not a stamp. Still not a send. Still not a live-page PASS. |

Hard bans (unchanged):

- Do not invent KBO / `BE0…` / IBAN / Peppol ID (`0208:`).
- Do not print **FACTUUR**. Printed thirds stay **VOORBEELD** / **OFFERTE**.
- Do not file (e604, CAP, RSVZ, Intervat, MyMinfin).
- Do not send CS / Scout / government mail from this seat.
- Do not second the 18 Tos of 2026-08-27.
- Do not call this merge “already compliant.”
- Do not restack live `index.html` / `catalog.html` / leftover invoice HTML from Compliance.

---

## 1. The four yellows — designed out

| #169 yellow | Design-out on this page |
| --- | --- |
| **Privacy NOW is blanks + 40-line grep, not Versie 3** | NOW **is** STORE Versie 3. Already GREEN as **copy** in #152. No `03-privacy-fillins.md`. No first-40-lines grep. Live `privacy.html` is still Versie 1 — world-state; Builder ships Versie 3 on the live shop. |
| **“Not a personal Gmail” vs Versie 3 GREEN** | Contact **is** `sasha.de.vree.rene@gmail.com` (Sasha, natuurlijke persoon, Geel). That sentence is **retired**. Do not write it. Versie 3 already names Gmail outside the EER. |
| **Prescribed fill-in fails its own grep** | Public-face copy in §3 has no leftover-digit / coin tokens. Payment line is **Betaalgegevens na akkoord** — not a sentence that names the forbidden words. Gate is whole public face, not the first 40 lines of a blank punch-list. |
| **Three opt-out templates** | One sentence only, in §5. `stop` / `UITSCHRIJVEN` / extra bodies are **retired as send templates**. Future CEO-gated mail only. No send. |

WAIT freeze in #135 was already GREEN. Keep it. That is not enough. NOW on this page is Versie 3 + one opt-out sentence.

This file does not grade itself GREEN. A later reviewer scores the stage.

---

## 2. NOW privacy = STORE Versie 3 (copy). Live is still Versie 1.

**Locked NOW:** the STORE Versie 3 fill-in scored GREEN as **copy** in [PR #152](https://github.com/eyeskull2220/solana-invoice/pull/152) `REVIEW-privacy-v3.md`.

That score is **not** reused here as a stamp. It is the artifact this PLAN cites. Do not open a parallel blank pack. Do not re-score Versie 3. Do not invent Versie 4.

### What Versie 3 is

| Line | Text (NOW copy) |
| --- | --- |
| Wie | Sasha · natuurlijke persoon · Geel · `sasha.de.vree.rene@gmail.com` |
| Trackers | Wij zetten zelf geen cookies, pixels of analytics. Of Surge of de mailhost logs of cookies zet, is niet geverifieerd. |
| EER | Offerte-mail loopt via Gmail, een dienst buiten de EER. Alleen om uw vraag te beantwoorden. |
| Host | One page on `sovereignforge.surge.sh` |
| Badge / banner | None. |
| Betaling (public face) | **Betaalgegevens na akkoord.** |

### What Versie 3 is not

- Not live `https://sovereignforge.surge.sh/privacy.html`. That URL is still **Versie 1**. World-state. Still a different document. This PLAN does not paint that URL green.
- Not a blank fill-in. #135 Task 1 (`03-privacy-fillins.md` with underscores and “professional mailbox”) is **killed**.
- Not a first-40-lines grep job. #135’s python lead-gate is **killed**.
- Not an AVG keurmerk. GREEN on #152 means the **copy package** closed tracker over-claim, empty EER, identity blanks, and coin-on-face. It does not mean AVG-conform.
- Not Builder’s shop restack. Compliance does not edit HTML. **Builder ships Versie 3 on the live shop.** Until that ship, the public URL stays Versie 1.

### Killed jobs (do not reopen)

| #135 job | Status after this lock |
| --- | --- |
| Create `docs/rgy-2026-08-27/compliance/03-privacy-fillins.md` with blanks | **Killed.** Versie 3 is already filled. |
| Keep blanks until a human writes a name | **Killed.** Name / town / mailbox are filled. |
| First 40 lines of that file must grep clean | **Killed.** The worker who copied “Geen USDC in de eerste alinea” could not pass it. |
| Align shop `privacy.html` by inventing a second pack | **Killed.** Builder ships **this** Versie 3. |

---

## 3. Prescribed public-face copy (must pass leftover-digit / USDC grep)

Builder pastes **this** (or an equivalent that still passes #152’s cells **and** the gate below). Do not add a sentence that names the forbidden tokens in order to forbid them.

```
Privacy — SovereignForge. Versie 3 — 27 augustus 2026.

Sasha, natuurlijke persoon, Geel (België), handelend onder de naam SovereignForge.
Geen vennootschap. KBO/BTW: nog niet toegekend. Geen functionaris voor gegevensbescherming.
Contact: sasha.de.vree.rene@gmail.com

Statische catalogus. Bestellen via OFFERTE. Geen account, geen formulier, geen checkout.

Als u mailt, verwerken wij wat u zelf stuurt. Doel: de vraag beantwoorden en een offerte opstellen.
Rechtsgrond: stappen op uw verzoek vóór een overeenkomst. Niet verplicht.

Wij zetten zelf geen cookies, pixels of analytics. Of Surge of de mailhost logs of cookies zet, is niet geverifieerd.
Daarom is er geen banner.

Offerte-mail loopt via Gmail, een dienst buiten de EER. Alleen om uw vraag te beantwoorden.
Deze pagina noemt geen SCC- of adequacy-claim.

Betaalgegevens na akkoord.

Rechten: inzage, verbetering, wissing, beperking, bezwaar, overdraagbaarheid.
Klacht: Gegevensbeschermingsautoriteit — https://www.gegevensbeschermingsautoriteit.be/
```

That block is the **prescribed fill-in**. It is copy. It is not a stamped policy. It is not live until Builder ships it.

### Gate (public face — shop privacy HTML, not this PLAN file)

When Builder ships Versie 3 onto the shop face (`shop/sovereignforge/**`, `shop/sovereignforge-builder/**`, live `privacy.html` on the shop origin):

| Gate | Must be empty / pass |
| --- | --- |
| leftover-digit ([PR #157](https://github.com/eyeskull2220/solana-invoice/pull/157)) | No leftover `9` / `49` coin-price integers. No fake `BE0` digits. |
| USDC-grep (whole public face, not first 40 lines) | No USDC, Solana, Phantom, crypto, or wallet **on the public face**. |
| Also empty on that face | No IBAN, no card numbers, no AVG-compliant / GDPR-compliant badge, no cookiebanner. |

**Betaalgegevens na akkoord only.** Rails, if any, live behind agreement — not in the privacy lead, not in the privacy body, not as a “we do not take X” sentence that writes X onto the page.

Do **not** grep this PLAN markdown for those tokens and call that a fail. This page names the gate. The prescribed block in the fence above is the copy that must pass.

Root leftover invoice HTML (`index.html`, `catalog.html`, `solana-invoice.html`) stays out of Compliance NOW restack (same as #135). Flag coin-first there as world-state **Y**. Builder’s EUR face is a different tree.

---

## 4. Contact IS the operator Gmail

**Contact:** `sasha.de.vree.rene@gmail.com`
**Wie:** Sasha, natuurlijke persoon, Geel.

#135 §3.1 / Task 1 / §6 (“not a personal Gmail in this repo”) is **retired**. Following that rule would reject the locked Versie 3 fill-in. Do not write it. Do not “professional mailbox” over it. Do not invent `info@`.

Versie 3 already states the transfer fact in public Dutch:

> Offerte-mail loopt via Gmail, een dienst buiten de EER. Alleen om uw vraag te beantwoorden.

That is the EER sentence. Do not add SCC / adequacy words to look complete. Do not omit the sentence to avoid naming Gmail.

This is operator contact for offerte and for this verklaring. It is not a DPO. It is not permission to send advertising from this seat.

---

## 5. ONE opt-out sentence — kill the extras

Mandatory, unshortened, including the em dash. **This is the only stop line for future CEO-gated mail:**

```
Geen interesse? Eén antwoord volstaat — dan mailen wij u niet meer.
```

No paraphrase. No second wording. Last body line before the signature, as in [PR #127](https://github.com/eyeskull2220/solana-invoice/pull/127).

### Retired as send templates (do not use)

| Source | Retired line / token | After this lock |
| --- | --- | --- |
| #135 §3.2 / #117 playbook | `Als u in de toekomst geen voorstellen van ons meer wilt ontvangen, antwoord dan **stop** …` | **Retired.** Not a send template. #169’s “pick `stop`” bar is **overridden**. |
| #116 COMPLIANCE §12 | `UITSCHRIJVEN` draft | **Retired.** Not a send template. |
| Any later extra body | A third wording | **Forbidden.** |

#169 said #127’s sentence was invalid for the CEO gate. **This PLAN locks the opposite:** #127 is the only body. Scout [PR #170](https://github.com/eyeskull2220/solana-invoice/pull/170) already named it the only send template. Compliance does not fork a competing sentence.

Do not create `docs/rgy-2026-08-27/compliance/04-ceo-mail-opt-out.md` as a second body. This section **is** the Compliance lock. #127 remains the mail body.

### Future CEO-gated mail only — no send

1. A Scout draft exists (the #127 body, including the sentence above).
2. CEO says **yes**.
3. A **human** sends. This seat does **not** send.

If step 1 is missing the verbatim sentence, CEO **must refuse**. A CEO yes without that sentence is an invalid gate.

**Not covered (still BLOCKED):**

- Seconds to the 18 of 2026-08-27 (including “we forgot opt-out”).
- CS mail from this seat.
- Burst sends.
- Honour-on-receipt tokens printed as extra templates. Inbound `stop` / `uitschrijven` at the desk is Scout’s inbound table ([PR #170](https://github.com/eyeskull2220/solana-invoice/pull/170)), not a second Compliance body.

**Send count authorised by this PLAN:** **zero.**

---

## 6. WAIT stays WAIT — Compliance HOLDS

No task below is “book the loket,” “create a Stripe account,” “print FACTUUR,” or “register Peppol.” Nobody stamps. A later “we paid the loket in the doc” is still a stamp.

### 6.1 KBO

Statutory inschrijvingsrecht at an *erkend ondernemingsloket*: **€111,50 vrij van btw** from **1 Jan 2026** ([Liantis](https://www.liantis.be/nl/nieuws/nieuwe-kbo-tarieven-gekend)). One vestigingseenheid. **Not** the whole start (VAT ID, social fund, ITAA, Peppol AP, live processor).

WER III.49 §1: register **before** the activity. Putting KBO in WAIT does **not** freeze the shop. This PLAN does **not** solve that by inventing a number. It also does **not** pretend WAIT means “activity has not started.” Write `KBO/BTW: nog niet toegekend` until a human counter issues a number.

This seat does not book the counter. Does not pay €111,50. Does not paste a demo `0XXX.XXX.XXX`.

### 6.2 Stripe / Mollie **live**

Live = charging Bancontact / cards / SEPA in **production** with identity completed. Blocker: no ondernemingsnummer. Test keys ≠ live. Polar / Gumroad / Payhip ≠ live. A Bancontact logo on a VOORBEELD ≠ live.

This seat does not create processor accounts. Does not mail Stripe/Mollie CS. Does not put IBAN or “betaal met Bancontact” as if live.

### 6.3 FACTUUR

Ban the word **FACTUUR** (and English **INVOICE** as a Belgian tax document) on anything this operator issues **before** KBO + VAT identification. Allowed: **VOORBEELD**, **OFFERTE**, paper journaal (Coder). PDF-mail is not a 2026 Belgian B2B invoice. Do not “prepare a FACTUUR template for Friday.”

### 6.4 Peppol

Belgian VAT-taxable B2B = structured e-invoice since 1 Jan 2026. The **€25,000 vrijstelling is still in scope**. B2C send still PDF-ok; **receive** from Belgian suppliers still required. This operator / this repo / this seat **is not** a Peppol Access Point. WAIT until real BTW-ID + listed **end-user** software. Humans pick the app. Do not mint `0208:` from a blank.

### 6.5 Do not create WAIT runbooks

Do **not** create `05-kbo.md`, `05-stripe.md`, `05-mollie.md`, `05-factuur.md`, `05-peppol.md` as executable runbooks. Pointer if needed: “WAIT — see this PLAN-lock §6. Not this week’s implementer work.”

---

## 7. RGY after the design-out

Legend: **R** = do not do / blocked / wait. **Y** = world-state; not this seat’s NOW restack. **G** = startable copy/gate, **not** a legal stamp.

| Item | Color | Why |
| --- | --- | --- |
| KBO ~€111,50 (loket act) | **R** | WAIT. Human counter. No invented number. Fee is not the whole start. |
| Stripe **live** | **R** | WAIT. No enterprise identity. Test ≠ live. |
| Mollie **live** | **R** | WAIT. Same identity gap. |
| FACTUUR | **R** | Ban until KBO + BTW-ID. VOORBEELD / OFFERTE only. |
| Peppol send/receive IDs | **R** | WAIT. Not an Access Point. After BTW-ID + end-user software. |
| File (e604, CAP, RSVZ, Intervat) | **R** | BLOCKED. Humans only. |
| Send mail / CS / seconds to the 18 | **R** | BLOCKED. Opt-out is not a licence. |
| Live Versie 1 `privacy.html` | **Y** | World-state. Builder ships Versie 3. Not this score. |
| Live treasury catalog / pay / README (coin-first) | **Y** | Builder EUR-face is a different tree. Still legally thin (WER III.49). |
| Cookie banner | **Y** | **No banner** while first-party trackers are none (GBA 17/11/2023 pointer, not a stamp). Banner without trackers = theatre. |
| Bijberoep vs hoofdberoep | **Y** | Accountant + payslips. Do not code it here. |
| STORE Versie 3 copy | **G** | NOW. Already filled. Already GREEN as copy in #152. Not a stamped policy. Not live until Builder ships. |
| One opt-out on **future** CEO-gated mail | **G** | NOW. The #127 sentence. Not a send. |

**There is no Green cell that means “compliant.”** Green means “the next markdown/gate may be written / Builder may ship the already-GREEN copy.”

---

## 8. Bar this PLAN meets (#169 acceptance, as locked by the operator)

#169 listed what a later Compliance plan must state. This page states each row. Operator lock **overrides** #169 bar 5 (`stop` as the only sentence).

| # | Bar | This page |
| --- | --- | --- |
| 1 | WAIT still WAIT: no KBO booking, no live Stripe/Mollie, no FACTUUR, no Peppol ID / Access Point cosplay. | §6. Compliance HOLDS. |
| 2 | NOW privacy **is** Versie 3 (#152) — not a blank `03-privacy-fillins.md` plus a first-40-lines grep. | §2–§3. |
| 3 | Contact rule does not ban the Gmail Versie 3 already locked. | §4. Contact **is** that Gmail. |
| 4 | Grep/gate matches Versie 3: leftover-digit + no USDC / Solana / Phantom / crypto / wallet on the **public face**. Prescribed text can pass. Payment = **Betaalgegevens na akkoord**. | §3. |
| 5 | **One** canonical opt-out sentence for future CEO-gated mail: `Geen interesse? Eén antwoord volstaat — dan mailen wij u niet meer.` `stop` / `UITSCHRIJVEN` / extra templates **killed**. No send. No seconds to the 18. | §5. |
| 6 | Green still does not mean compliant. No stamp. No CS mail. | §0, §7, §9. |

Until a later reviewer scores this page, treat #135 as **YELLOW** history. Do not treat a merge of #135 as “compliance planned, NOW done.”

---

## 9. Failures that would make this a stamp

| Failure | What it looks like |
| --- | --- |
| Green = compliant | PR title “Compliance complete” / README badge / “NOW done” on a merge of #135. |
| Invented identity | Any `BE0`, Peppol `0208:`, IBAN, GSM invented in these files. |
| Ban the locked mailbox | Writing “not a personal Gmail” as a gate against Versie 3. |
| Blank fork | A new `03-privacy-fillins.md` with underscores. |
| Coin on the public face | USDC / Solana / Phantom / crypto / wallet in shipped privacy HTML, including a “geen …” sentence that writes the token. |
| FACTUUR | The word on an operator-issued PDF/HTML as a tax document. |
| Live rails | Stripe/Mollie production keys, Bancontact button that charges. |
| Access Point cosplay | Repo claims to be Peppol / AP. |
| Send | Any mail from this seat; any second to the 18 “to add opt-out.” |
| Extra opt-out body | `stop` sentence or `UITSCHRIJVEN` shipped as a send template. |
| Banner theatre | Cookie popup on a tracker-free page. |
| Paying €111,50 in the doc | “Loket paid” without a human counter and a real number. |
| Live Versie 1 painted green | Scoring the URL instead of the Versie 3 copy. |

---

## 10. Sources (cite; do not reopen as a competing PLAN)

| Source | Use here |
| --- | --- |
| [PR #169](https://github.com/eyeskull2220/solana-invoice/pull/169) `REVIEW-02-plan.md` | Four yellows to close. WAIT freeze kept. `stop` bar overridden by operator lock. |
| [PR #135](https://github.com/eyeskull2220/solana-invoice/pull/135) `02-adv-plan.md` | History. WAIT still right. NOW jobs (blanks, 40-line grep, `stop`, “not a personal Gmail”) killed. |
| [PR #152](https://github.com/eyeskull2220/solana-invoice/pull/152) `REVIEW-privacy-v3.md` | Versie 3 copy already GREEN. Not re-scored. Live URL is still Versie 1. |
| [PR #127](https://github.com/eyeskull2220/solana-invoice/pull/127) `FIX-playbook.md` | The only send template. Opt-out sentence. |
| [PR #170](https://github.com/eyeskull2220/solana-invoice/pull/170) Scout `PLAN-lock.md` | Same one sentence. `stop` retired as a send template. Inbound desk owns replies. |
| [PR #157](https://github.com/eyeskull2220/solana-invoice/pull/157) | leftover-digit + USDC-grep on shop faces. Gate for shipped privacy HTML. |
| [PR #116](https://github.com/eyeskull2220/solana-invoice/pull/116) | Seat history. §12 `UITSCHRIJVEN` retired as a send template. Nobody stamped. |
| [PR #117](https://github.com/eyeskull2220/solana-invoice/pull/117) | Seat history. `stop` line retired as a send template. Do not second the 18. |
| Liantis KBO 1 Jan 2026 | €111,50 vrij van btw. Fee is not the whole start. |
| efactuur.belgium.be | €25k vrijstelling still in scope (as fetched in #169). |
| GBA cookies 17/11/2023 | Pointer: no banner if only strictly necessary cookies. Not a stamp. |

ELI justel permalinks 404’d the #169 agent; Staatsblad bodies were the this-run confirm. This PLAN does not promote those ELI URLs to fetched-confirmed. Stripe Belgium field list stays **UNVERIFIED**.

---

## 11. This run

| Did | Did not |
| --- | --- |
| Wrote this PLAN lock to close #169’s four yellows | Send CS mail, open Gmail, second the 18 |
| Cited Versie 3 (#152) as NOW privacy copy | Create `03-privacy-fillins.md` blanks or a 40-line grep |
| Locked contact **is** `sasha.de.vree.rene@gmail.com` (Sasha, natuurlijke persoon, Geel) | Write “not a personal Gmail” as a gate |
| Locked prescribed copy to **Betaalgegevens na akkoord**; public face must pass leftover-digit / USDC-grep | Ship HTML, restack live Versie 1, paint that URL green |
| Locked one opt-out sentence; retired `stop` / `UITSCHRIJVEN` | Write a second send template / `04-ceo-mail-opt-out.md` body |
| Held WAIT: KBO, live Stripe/Mollie, FACTUUR, Peppol | Book a loket, invent `BE0` / `0208:`, print FACTUUR, create a processor account |
| | Stamp “compliant.” Nobody stamped. |

**PLAN stage after this file:** the four #169 yellows are designed out on paper. **Do not send. Do not file. Do not stamp.** Builder still ships Versie 3 to the live shop. Compliance HOLDS WAIT.

---

## 12. This file is not

- Not legal advice. Not a GBA, FPS, RSVZ, or Peppol filing.
- Not a stamp that #135, Versie 3, Surge, or Gmail is AVG-conform or “already registered.”
- Not a re-score of Versie 3 (that score stays in #152).
- Not a live-page PASS. Versie 1 on the URL is world-state.
- Not HTML. Not mail. Not a KBO. Not live Stripe. Not FACTUUR. Not Peppol.
- Not a second send template.

End. Docs only. No CS mail. No seconds to the 18. Nobody stamped.
