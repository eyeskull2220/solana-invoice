# REVIEW — Compliance PLAN-lock (03)

**Seat:** reviewer batch (docs only)
**Date:** 2026-08-27
**Artifact:** [PR #179](https://github.com/eyeskull2220/solana-invoice/pull/179) `docs/rgy-2026-08-27/compliance/PLAN-lock.md` (head `97b63a1`)
**Verdict:** **GREEN**
**Not a lawyer. Not a stamp.**

Old pack [PR #169](https://github.com/eyeskull2220/solana-invoice/pull/169) scored [PR #135](https://github.com/eyeskull2220/solana-invoice/pull/135) **YELLOW**. This batch scores the rewrite only. GREEN only if **this file** has **no** red and **no** yellow. It has neither.

The plan’s own RGY table is **not** the colour. This page does not grade itself GREEN. Copying “STORE Versie 3 copy = G” out of §7 would be a stamp.

---

## Mandate this batch scored

| Bucket | Locked items | Meaning for this review |
| --- | --- | --- |
| **WAIT** | KBO · live Stripe/Mollie · FACTUUR · Peppol | Plan must not execute, schedule, or “pay in the doc.” Stay R. Compliance **HOLDS**. |
| **NOW** | STORE **Versie 3** privacy **copy** (already **GREEN** in [PR #152](https://github.com/eyeskull2220/solana-invoice/pull/152)) · **one** opt-out on **future CEO-gated** mail | Whole copy / gate jobs. Still not a stamp. Still not a send. Still not a live-page PASS. |

Locks that stay locked (this run, not optional):

| Lock | Honoured on #179? |
| --- | --- |
| Privacy NOW = STORE Versie 3 fill-in (#152 GREEN as **copy**). Live `privacy.html` Versie 1 is world-state. Builder ships Versie 3. | **Yes.** §0, §2, §7. |
| Contact **is** `sasha.de.vree.rene@gmail.com` (Sasha, natuurlijke persoon, Geel). | **Yes.** §4 + prescribed fence. |
| Public face passes leftover-digit / USDC-grep. Payment line = **Betaalgegevens na akkoord** only. | **Yes.** §3 fence greps clean this run. |
| ONE opt-out, verbatim, including the em dash: `Geen interesse? Eén antwoord volstaat — dan mailen wij u niet meer.` | **Yes.** §5 fence. One send line. |
| WAIT stays WAIT. Nobody stamps. | **Yes.** §6. |

GREEN on this artifact only if **every** cell below is GREEN. Every cell is GREEN.

---

## What was scored

| Object | In this batch? |
| --- | --- |
| PR #179 `PLAN-lock.md` | **Yes — the only graded object.** One markdown file. |
| PR #169 `REVIEW-02-plan.md` | The YELLOW pack this rewrite answers. Bar, not re-scored. |
| PR #135 `02-adv-plan.md` | History. Wrong NOW jobs. **Not** the page a later agent follows. |
| PR #152 STORE Versie 3 fill-in (already GREEN as copy) | Lock for NOW privacy. **Not re-scored.** |
| Live `https://sovereignforge.surge.sh/privacy.html` | Context. Still Versie 1. **Not the score.** |
| HTML / catalog / pay / Gmail send | **No.** This review does not edit them and does not send. |

A later Compliance / Builder / Scout agent follows **#179**. Not #135 Task 1. Not #135 Task 2. Not #116 §12. Not #117 as a send template.

---

## This-run checks (2026-08-27)

| Check | Result |
| --- | --- |
| PR #179 files | **One** markdown file. No HTML. No CS mail. No seconds to the 18. |
| Plan executes KBO / Stripe live / FACTUUR / Peppol | **No.** §6 freeze. No `05-kbo.md` / `05-stripe.md` / `05-factuur.md` / `05-peppol.md` runbooks. |
| Invented `BE0` digits / Peppol `0208:` + digits / IBAN in the plan | **None.** Ban patterns only (`BE0…`, `0208:`). |
| Plan sends mail / CS / seconds to the 18 | **No.** Send count authorised: **zero.** |
| `03-privacy-fillins.md` / first-40-lines grep / Versie 4 | **Killed.** NOW is Versie 3. |
| Contact in §4 and in the prescribed fence | `sasha.de.vree.rene@gmail.com` · Sasha · natuurlijke persoon · Geel. |
| Prescribed public-face fence (`rg -i 'USDC\|Solana\|Phantom\|crypto\|wallet'`) | **Empty.** Also empty: IBAN, `BE0`, FACTUUR, AVG-compliant / GDPR-compliant. |
| leftover-digit on that fence (`9 USDC` / `49 USDC` / fake `BE0`) | **Empty.** Date `27` / `Versie 3` are not coin-price integers. |
| Payment line in that fence | **Betaalgegevens na akkoord.** One line. No “we do not take X” that writes X. |
| Opt-out verbatim (em dash) as the **send** fence | **Once**, in §5. §8 bar **cites** the same sentence. Not a second body. |
| `stop` / `UITSCHRIJVEN` as send templates | **Retired.** Quoted only as killed. Inbound tokens sit on Scout’s desk ([PR #170](https://github.com/eyeskull2220/solana-invoice/pull/170)), not as a Compliance body. |
| Liantis KBO inschrijvingsrecht 1 Jan 2026 | **€111,50 vrij van btw** ([Liantis](https://www.liantis.be/nl/nieuws/nieuwe-kbo-tarieven-gekend), fetched this run). Fee is one loket act, not the whole start. Plan matches. Does not book it. |
| Peppol who-is-in-scope | Fetched [efactuur.belgium.be](https://efactuur.belgium.be/nl/article/voor-wie-wordt-e-facturatie-verplicht): from 1 Jan 2026 Belgian VAT-to-VAT = structured e-invoice; **€25,000 vrijstelling still in scope**; B2C send PDF-ok; **receive** from Belgian suppliers still required. Plan WAIT matches. Not an Access Point. |
| GBA cookies | [GBA page](https://www.gegevensbeschermingsautoriteit.be/cookies-en-andere-traceringsmiddelen) last update **17/11/2023**. Analytics are not the strictly-necessary exception. Plan: **no banner** while first-party trackers are none. Pointer, not a stamp. |
| Live privacy Versie 1 | Still labelled **Versie 1**. Still: “Betaling is on-chain in USDC…”. Contact already that Gmail. Plan does **not** paint the URL green. |
| Git `main` pay/catalog | `index.html` title still “Solana Invoice — 9 USDC.” `catalog.html` meta still “billed in USDC on Solana.” World-state **Y**. Out of Compliance NOW restack. |
| ELI justel permalinks | This PLAN does not promote them to fetched-confirmed. This run did not upgrade them. Stripe Belgium field list stays **UNVERIFIED** (plan already does). |

Do **not** grep the PLAN markdown for coin tokens and call that a fail. This page names the gate. The prescribed fence is the copy that must pass. It passed.

---

## Closed from #169 (not copied as this grade)

| #169 attack | Was | Why #179 closes it |
| --- | --- | --- |
| Privacy NOW is blanks + 40-line grep, not Versie 3 | **YELLOW** | NOW **is** STORE Versie 3 (#152 GREEN as copy). `03-privacy-fillins.md` killed. First-40-lines grep killed. Live URL stays Versie 1 until Builder ships. |
| Contact ban vs Versie 3 GREEN | **YELLOW** | Contact **is** the operator Gmail already locked in Versie 3. #135 Task 1 / “professional mailbox” / invented `info@` retired. |
| Prescribed fill-in fails its own USDC grep | **YELLOW** | §3 fence has no leftover-digit / coin tokens. Payment is **Betaalgegevens na akkoord**. Gate is the whole public face, not the first 40 lines of a punch-list that wrote the forbidden word in order to forbid it. |
| Three opt-out templates | **YELLOW** | One sentence only. `stop` / `UITSCHRIJVEN` retired as send templates. #169 bar 5 (`stop` as the only sentence) is **overridden** by this batch’s operator lock. Future CEO-gated mail only. No send. |

WAIT freeze in #135 was already GREEN. Kept. That was not enough. NOW on this page is Versie 3 + one opt-out sentence.

---

## Scorecard

| # | Attack | Score | Why (this batch) |
| --- | --- | --- | --- |
| 1 | WAIT leak — KBO ~€111,50 booked or invented | **GREEN** | Human loket only. No demo number. Fee is not the whole start. Matches Liantis this run. Write `KBO/BTW: nog niet toegekend` until a counter issues a number. |
| 2 | WAIT leak — Stripe (or Mollie) **live** | **GREEN** | Test ≠ live. No processor account. No Bancontact-as-live. Mollie is the same identity gap. |
| 3 | WAIT leak — FACTUUR / Peppol ID / Access Point | **GREEN** | Ban until KBO + BTW-ID. VOORBEELD / OFFERTE only. End-user software after that. This seat is not an AP. €25k-in-scope confirmed this run. |
| 4 | Stamp / “Green = compliant” | **GREEN** | §0 + §7 + §9. Green means next markdown/gate / Builder may ship already-GREEN copy. Not AVG-conform. Not a filing. This file does not grade itself GREEN. |
| 5 | Send / CS / seconds to the 18 | **GREEN** | Future CEO-gated only. Human sends. This seat does not. Seconds forbidden, including “we forgot opt-out.” This review sent nothing. |
| 6 | Privacy NOW is blank fill-ins + 40-line grep, not Versie 3 | **GREEN** | Locked NOW is the Versie 3 **copy package** (PR #152). Parallel blank pack is killed. Live Versie 1 is world-state, not this score. Builder ships Versie 3. |
| 7 | Contact **is** the locked Gmail vs a mailbox ban | **GREEN** | §4 and the fence name `sasha.de.vree.rene@gmail.com` (Sasha, natuurlijke persoon, Geel). Versie 3 already: *Offerte-mail loopt via Gmail, een dienst buiten de EER. Alleen om uw vraag te beantwoorden.* |
| 8 | Prescribed copy fails leftover-digit / USDC-grep | **GREEN** | This-run grep of the §3 fence is empty for USDC / Solana / Phantom / crypto / wallet / IBAN / `BE0` / FACTUUR. Payment line is **Betaalgegevens na akkoord** only. |
| 9 | Three opt-out templates | **GREEN** | One allowed send line, verbatim, unshortened, em dash included. Extra bodies forbidden. Honour-on-receipt is Scout inbound, not a second Compliance template. |
| 10 | Invented identity / FACTUUR / Peppol in *this* file | **GREEN** | Review invents none. Plan invents none. |

**Overall: GREEN.**

RED rows on this file: **none.**
YELLOW rows on this file: **none.**

WAIT is frozen. NOW privacy is Versie 3. NOW opt-out is one sentence. Contact is the operator Gmail. The prescribed public-face copy can pass its own gate.

---

## Notes (not extra colours)

1. **Versie 3 GREEN is copy, not live.** PR #152 already said live `privacy.html` is still Versie 1 and still leads payment with USDC. This PLAN review does not paint that URL green. Builder still has to replace it. The plan is right to refuse a Compliance restack of `index.html` / `catalog.html`.

2. **Do not reopen Task 1.** Blanks + 40-line grep + “Geen USDC in de eerste alinea” was the #169 yellow. This page kills it. An “equivalent” Builder paste is allowed only if it still passes #152’s cells **and** the leftover-digit / USDC-grep. That is not a new punch-list.

3. **#169 bar 5 is not this batch’s bar.** That pack wanted the #117 `stop` line and called #127 invalid. This run’s operator lock is the opposite: the #127 sentence is the only send template. Scoring `stop` back in as a yellow would reopen the three-template hole. Scout [PR #170](https://github.com/eyeskull2220/solana-invoice/pull/170) already named the same sentence. Compliance does not fork a competing body.

4. **Habitual selling without KBO is still thin.** Git `main` still prices USDC. Live privacy still says on-chain USDC. Eighteen Tos already went out. Putting KBO in WAIT does not freeze the shop. The plan says that in §6.1. Keep it. Do not “pay €111,50 in the doc.”

5. **10% / 33% is not this PLAN.** Research (#140) is an accountant question. Omitting it here is scope, not a close.

6. **ELI 404s stay unpromoted.** Do not treat Justel/ELI rows as fetched-confirmed from this agent. Keep UNVERIFIED on Stripe Belgium field lists.

7. **GREEN on PLAN is not a send licence, not a live-page PASS, not AVG-conform.** Builder still ships Versie 3. Compliance HOLDS WAIT.

---

## Bar for GREEN (this artifact = this Compliance **plan**)

Operator lock for this rewrite, checked against #179 itself (not as a promise):

| # | Bar | After #179 |
| --- | --- | --- |
| 1 | WAIT still WAIT: no KBO booking, no live Stripe/Mollie, no FACTUUR, no Peppol ID / Access Point cosplay. | **Pass.** §6. Compliance HOLDS. |
| 2 | NOW privacy **is** the Versie 3 fill-in (PR #152) — not a blank `03-privacy-fillins.md` plus a first-40-lines grep. Live Versie 1 is world-state; Builder ships Versie 3. | **Pass.** §2–§3. |
| 3 | Contact **is** `sasha.de.vree.rene@gmail.com` (Sasha, natuurlijke persoon, Geel). | **Pass.** §4. Fence matches. |
| 4 | Grep/gate matches Versie 3: leftover-digit + no USDC / Solana / Phantom / crypto / wallet on the **public face**. Prescribed text can pass. Payment = **Betaalgegevens na akkoord**. | **Pass.** §3 fence this run. |
| 5 | **One** canonical opt-out sentence for future CEO-gated mail: `Geen interesse? Eén antwoord volstaat — dan mailen wij u niet meer.` Extra templates killed. No send. No seconds to the 18. | **Pass.** §5. |
| 6 | Green still does not mean compliant. No stamp. No CS mail. | **Pass.** §0, §7, §9. |

Until a later **Builder** ship of Versie 3 on the live shop, this PLAN is the lock. That ship is not this review. Do not treat a merge of #135 as “NOW done.” Follow #179.

---

## This run

| Did | Did not |
| --- | --- |
| Read #179 `PLAN-lock.md` as the only graded object | Send CS mail, open Gmail, second the 18 |
| Read #169 as the YELLOW bar | Re-score Versie 3 (#152 stays GREEN as copy) |
| Grepped the prescribed public-face fence (clean) | Grep the PLAN markdown and call coin-token *names of the gate* a fail |
| Fetched Liantis, efactuur.belgium.be, GBA cookies, live Versie 1 | Book a loket, invent `BE0` / `0208:`, print FACTUUR, create a processor account |
| Confirmed one opt-out sentence; `stop` / `UITSCHRIJVEN` retired as send templates | Write a second send template / `04-ceo-mail-opt-out.md` |
| Scored this PLAN **GREEN** (no red, no yellow) | Edit HTML / catalog / Surge; paint live Versie 1 green; stamp “compliant” |

**PLAN stage: GREEN.** Not a stamp. Not a send. Not a live-page PASS. Builder still ships Versie 3. Compliance HOLDS WAIT.

---

## This file is not

- Not legal advice. Not a GBA, FPS, RSVZ, or Peppol filing.
- Not a stamp that #179, #135, Versie 3, Surge, or Gmail is AVG-conform or “already registered.”
- Not a re-score of Versie 3 (that score stays in PR #152).
- Not a live-page PASS. Versie 1 on the URL is world-state.
- Not HTML. Not mail. Not a KBO. Not live Stripe. Not FACTUUR. Not Peppol.
- Not a second send template.

End. Docs only. No CS mail. No seconds to the 18. Nobody stamped.
