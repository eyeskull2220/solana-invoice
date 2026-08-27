# REVIEW — Compliance PLAN (02-adv-plan)

**Seat:** reviewer batch (docs only)
**Date:** 2026-08-27
**Artifact:** [PR #135](https://github.com/eyeskull2220/solana-invoice/pull/135) `docs/rgy-2026-08-27/compliance/02-adv-plan.md`
**Verdict:** **YELLOW**
**Not a lawyer. Not a stamp.**

Scored from zero against the plan file, the locked NOW/WAIT mandate for this batch, and this-run fetches. The plan’s own RGY table is **not** the colour. Copying “privacy = G” out of §4 would be a stamp.

---

## Mandate this batch scored

| Bucket | Locked items | Meaning for this review |
| --- | --- | --- |
| **WAIT** | KBO · live Stripe · FACTUUR · Peppol | Plan must not execute, schedule, or “pay in the doc.” Stay R. |
| **NOW** | Versie 3 privacy **copy** (fill-in already **GREEN** in [PR #152](https://github.com/eyeskull2220/solana-invoice/pull/152)) · opt-out on **future CEO-gated** mail | Whole copy/gate jobs. Still not a stamp. Still not a send. |

GREEN on this artifact only if **every** cell below is GREEN (no red, no yellow). This file is not GREEN.

---

## What was scored

| Object | In this batch? |
| --- | --- |
| PR #135 `02-adv-plan.md` | **Yes — the artifact** |
| PR #152 STORE Versie 3 fill-in (already GREEN as copy) | Lock for NOW privacy. Not re-scored. |
| Live `https://sovereignforge.surge.sh/privacy.html` | Context. Still Versie 1. Not the score. |
| [PR #140](https://github.com/eyeskull2220/solana-invoice/pull/140) research pack | Context. 10%/33% is **not** this PLAN’s NOW. |
| HTML / catalog / pay / Gmail send | **No.** This review does not edit them and does not send. |

---

## This-run checks (2026-08-27)

| Check | Result |
| --- | --- |
| Plan executes KBO / Stripe live / FACTUUR / Peppol | **No.** §2 + Task 3 freeze. No `05-kbo.md` runbook. |
| Invented `BE0` / Peppol `0208:` / IBAN in the plan | **None.** |
| Plan sends mail / CS / seconds to the 18 | **No.** |
| Liantis KBO inschrijvingsrecht 1 Jan 2026 | **€111,50 vrij van btw** ([Liantis](https://www.liantis.be/nl/nieuws/nieuwe-kbo-tarieven-gekend), fetched this run). Fee is one loket act, not the whole start. |
| WER III.49 §1 | ELI justel URL in the plan **404 this run**. Staatsblad body numac `2024002118` (21 Mar 2024) **did** fetch: register **before** activities start, via an *ondernemingsloket*. |
| Peppol who-is-in-scope | Fetched [efactuur.belgium.be](https://efactuur.belgium.be/nl/article/voor-wie-wordt-e-facturatie-verplicht): from 1 Jan 2026 Belgian VAT-to-VAT = structured e-invoice; **€25,000 vrijstelling still in scope**; B2C send PDF-ok; **receive** from Belgian suppliers still required. |
| GBA cookies | [GBA page](https://www.gegevensbeschermingsautoriteit.be/cookies-en-andere-traceringsmiddelen) last update **17/11/2023**. FAQ: banner not required if only strictly necessary cookies. Analytics are not that exception. |
| GBA art. 13 | Identity/contact of the controller **at collection** ([GBA — recht op informatie](https://www.gegevensbeschermingsautoriteit.be/professioneel/avg/rechten-van-de-burgers/het-recht-op-informatie)). |
| KB 4 Apr 2003 | ELI staatsblad URL in the plan **404 this run**. `article_body` numac `2003011238` (28 May 2003) **did** fetch: impersonal `info@` of a **rechtspersoon** (Verslag); art. 2 object **zonder kosten en zonder een reden**. |
| Live privacy Versie 1 | Still labelled Versie 1. Still: “Betaling is on-chain in USDC…”. Contact already `sasha.de.vree.rene@gmail.com`. |
| Git `main` pay/catalog | `index.html` title still “Solana Invoice — 9 USDC.” `catalog.html` meta still “billed in USDC on Solana.” |
| Live Surge pairing in the plan | `treasury-tools.surge.sh/catalog.html` **404** this run. Host home shows a **€900** club kit. `solana-invoice-treasury.surge.sh` this run is **€49 OFFERTE**, not 9 USDC. Plan’s specific USDC-host pairing is **stale**; git `main` and live privacy payment paragraph are not. |
| Versie 3 fill-in (PR #152) | GREEN copy package: Sasha · Geel · that Gmail; tracker line splits “wij” vs unverified host/mailhost; EER names Gmail outside the EER, only to answer; no USDC/IBAN/card; no AVG badge; no banner. Live URL is a different document. |
| Competing opt-out lines | Plan quotes the [PR #117](https://github.com/eyeskull2220/solana-invoice/pull/117) `stop` sentence. [PR #116](https://github.com/eyeskull2220/solana-invoice/pull/116) COMPLIANCE §12 still drafts `UITSCHRIJVEN`. [PR #127](https://github.com/eyeskull2220/solana-invoice/pull/127) FIX playbook locks a **different** verbatim line as “the only send template”: `Geen interesse? Eén antwoord volstaat — dan mailen wij u niet meer.` |

A 404 on an ELI permalink is not a finding that the law is gone. It is a finding that the plan must not treat those ELI URLs as “fetched-confirmed” if this run cannot open them. Staatsblad bodies above are the this-run confirm.

---

## Scorecard

| # | Attack | Score | Why (this batch) |
| --- | --- | --- | --- |
| 1 | WAIT leak — KBO ~€111,50 booked or invented | **GREEN** | Human loket only. No demo number. Fee is not the whole start. Matches Liantis this run. |
| 2 | WAIT leak — Stripe (or Mollie) **live** | **GREEN** | Test ≠ live. No processor account. Mollie is the same identity gap; adding it to WAIT is not a leak. |
| 3 | WAIT leak — FACTUUR / Peppol ID / Access Point | **GREEN** | Ban until KBO + BTW-ID. End-user software after that. This seat is not an AP. Peppol €25k-in-scope confirmed this run. |
| 4 | Stamp / “Green = compliant” | **GREEN** | §1.1 + §6 fail table. Green in the plan means “next markdown/gate may be written,” not a filing. |
| 5 | Send / CS / seconds to the 18 | **GREEN** | Future CEO-gated only. Seconds forbidden. This review sent nothing. |
| 6 | Privacy NOW is blank fill-ins + 40-line grep, not Versie 3 | **YELLOW** | Locked NOW is the Versie 3 **copy package** (PR #152 GREEN). The plan’s Task 1 still creates `03-privacy-fillins.md` with blanks and a first-40-lines grep. That is a second artifact, not the job already scored GREEN. |
| 7 | “Not a personal Gmail” vs Versie 3 GREEN | **YELLOW** | §3.1 / Task 1 forbid a personal Gmail in the repo. Versie 3 GREEN (and live Versie 1) already name `sasha.de.vree.rene@gmail.com`. Following Task 1 would reject the locked fill-in. |
| 8 | Prescribed copy fails its own gate | **YELLOW** | Task 1: copy the §3.1 block, then grep `USDC` in the first 40 lines. The block itself says “Geen USDC in de eerste alinea…”. That line is inside a short fill-in. The worker who follows the steps cannot pass the script as written. |
| 9 | Three opt-out templates | **YELLOW** | Canonical `stop` sentence matches PR #117 and KB art. 2 (kosteloos / zonder reden / electronic reply). Plan does **not** retire PR #127’s “Eén antwoord volstaat” line, which names no token and omits cost-free/no-reason. COMPLIANCE §12 `UITSCHRIJVEN` is honour-on-receipt in the plan, but still a third draft. CEO can still gate the FIX playbook and think opt-out is done. |
| 10 | Invented identity / FACTUUR / Peppol in *this* file | **GREEN** | Review invents none. Plan invents none. |

**Overall: YELLOW.**

WAIT is frozen. That is not enough for GREEN. NOW privacy in the plan is the wrong job (blanks + grep) next to a fill-in that is already GREEN. NOW opt-out picks a good sentence and then leaves two other sentences live.

---

## Notes (not extra colours)

1. **Versie 3 GREEN is copy, not live.** PR #152 already said live `privacy.html` is still Versie 1 and still leads payment with USDC. This PLAN review does not paint that URL green. Builder still has to replace it. The plan was right to refuse a Compliance restack of `index.html` / `catalog.html`.

2. **Do not implement Task 1 as written.** It forks blanks against Versie 3 and cannot pass its own grep. A later plan that is GREEN names Versie 3 as the NOW privacy artifact (or an equivalent that still passes PR #152’s cells) and drops the parallel `03-privacy-fillins.md` punch-list.

3. **`stop` is the right token if one must be picked.** The sentence in §3.2 is the PR #117 line. KB art. 2 this run wants an objection **zonder kosten en zonder een reden** and an electronic ack. PR #127’s line is not that sentence. The plan’s “CEO yes without this sentence = invalid” is the right gate **if** CEO actually uses it. Naming PR #127 as invalid is missing.

4. **Habitual selling without KBO is still thin.** Git `main` still prices USDC. Live privacy still says on-chain USDC. Eighteen Tos already went out. WER III.49 §1 (Staatsblad this run) wants the loket **before** the activity. Putting KBO in WAIT does not freeze the shop. The plan says that in §1.2. Keep it. Do not “pay €111,50 in the doc.”

5. **10% / 33% is not this PLAN.** Research (#140) scored unstamped classification **YELLOW** and STARTABLE as an accountant question. This batch’s NOW/WAIT list does not include it. Omitting it here is scope, not a close.

6. **ELI 404s this run.** Do not promote the plan’s Justel/ELI rows to “fetched-confirmed” from this agent. Staatsblad bodies for III.49 and KB 2003 were readable. Keep UNVERIFIED on Stripe Belgium field lists (plan already does).

---

## Bar for GREEN (this artifact = a later Compliance **plan**)

A later plan file is GREEN only if **all** of these are true in the plan itself (not as a promise):

1. WAIT still WAIT: no KBO booking, no live Stripe/Mollie, no FACTUUR, no Peppol ID / Access Point cosplay.
2. NOW privacy **is** the Versie 3 fill-in (PR #152) — or a successor that still passes those cells — not a blank `03-privacy-fillins.md` plus a first-40-lines grep.
3. Contact rule does not ban the Gmail Versie 3 already locked (or it explicitly defers to that fill-in).
4. Any grep/gate matches Versie 3: no USDC / IBAN / card / FACTUUR / AVG-compliant badge **anywhere** in the privacy copy, not only the first 40 lines. Prescribed text must be able to pass the gate.
5. One canonical opt-out sentence for future CEO-gated mail (the `stop` line). PR #127’s “Eén antwoord volstaat” is **invalid** for the CEO gate. `UITSCHRIJVEN` is honour-on-receipt only. No send. No seconds to the 18.
6. Green still does not mean compliant. No stamp. No CS mail.

Until then: **YELLOW.** Do not treat a merge of #135 as “compliance planned, NOW done.”

---

## This file is not

- Not legal advice. Not a GBA, FPS, RSVZ, or Peppol filing.
- Not a stamp that #135, Versie 3, Surge, or Gmail is AVG-conform or “already registered.”
- Not a re-score of Versie 3 (that score stays in PR #152).
- Not HTML. Not mail. Not a KBO. Not live Stripe. Not FACTUUR. Not Peppol.

End.
