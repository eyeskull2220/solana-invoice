# Compliance adversarial plan — RGY 2026-08-27

**Seat:** COMPLIANCE  
**File:** `docs/rgy-2026-08-27/compliance/02-adv-plan.md`  
**Date:** 2026-08-27  
**Order:** adversarial first, RGY last. Skipping to Green is a failed read.

This file is a **plan**. It is **not a stamp**. It is not a lawyer. It is not a KBO extract, not a BTW-ID, not a Peppol participant, not a FACTUUR, not AVG-compliant, and not permission to send mail.

Sibling research (may land in parallel): `docs/rgy-2026-08-27/compliance/01-adv-research.md`.  
Baseline pack (open, not merged, not a stamp): [PR #116](https://github.com/eyeskull2220/solana-invoice/pull/116) `docs/ultra-seats/COMPLIANCE.md`.

---

## 0. Mandate (locked before color)

| Bucket | Items | Meaning in this plan |
|---|---|---|
| **WAIT** | KBO ~€111.50 · Stripe/Mollie **live** · FACTUUR · Peppol | Do **not** execute. Stay **R**. A later “we paid the loket in the doc” is still a stamp. |
| **NOW** | Privacy **no-coin** · Opt-out on **future CEO-gated** mail | Startable **copy and gates**. Still not a stamp. Still not a send. |

Hard bans (same as the COMPLIANCE seat):

- Do not invent KBO / `BE0…` / IBAN / Peppol ID (`0208:`).
- Do not print **FACTUUR**. Printed thirds stay **VOORBEELD** / **OFFERTE**.
- Do not file (e604, CAP, RSVZ, Intervat, MyMinfin).
- Do not send CS / Scout / government mail from this seat.
- Do not call this merge “already compliant.”

---

## 1. Adversarial pass (read this before the board)

A hostile reader (FPS Economy, RSVZ, GBA, a club’s lawyer, Stripe/Mollie onboarding, a later CEO) can already describe the operation. Coloring Green without answering these is theatre.

### 1.1 This plan-file as the stamp

Merging markdown is cheap. A later agent will quote the RGY table, drop the WAIT column, and write “compliance done 2026-08-27.” **Fail condition:** any sentence in a later PR that treats this file as a filing, a licence, or a Peppol ID.

### 1.2 Habitual selling while KBO is WAIT

Live catalog (`catalog.html`, https://treasury-tools.surge.sh/) and pay page (`index.html`) already price SKUs in USDC. WER III.49 §1 (law 9 Feb 2024, BS 21 Mar 2024) wants KBO **before** the activity starts. Putting KBO in WAIT does **not** freeze the catalog. “We only take USDC” is not an exemption. This plan does **not** solve that by inventing a number. It also does **not** pretend WAIT means “activity has not started.”

### 1.3 €111,50 as the whole start

Liantis (1 Jan 2026): statutory KBO inschrijvingsrecht **€111,50, vrij van btw** (indexed from €109). That is **one** vestigingseenheid at an *erkend ondernemingsloket*. It is **not**:

- VAT identification (e604 / loket service fee — Acerta/Liantis quote extra tens of euros, or free if the human files e604 themselves).
- Social-insurance fund affiliation.
- An ITAA engagement.
- A Peppol Access Point.
- Stripe or Mollie live.

Paying ~€111,50 from the Solana USDC treasury **in order to register because selling already started** is circular. This seat does not book that payment and does not pick a loket.

### 1.4 Stripe/Mollie **test** as live

Live charges need a real enterprise identity. There is no Belgian ondernemingsnummer to give them. Test-mode keys, Polar/Gumroad/Payhip fiat doors (older storefront research), and a Mollie **dashboard signup** are not Bancontact-in-production.

Mollie onboarding (third-party operator docs, e.g. Assist online help, fetched pattern 2026): **ondernemingsnummer** required; feitelijke vereniging / natural person without KBO is the usual refuse. Stripe live needs legal name, address, tax/enterprise identifiers, bank. **UNVERIFIED this fetch:** Stripe’s current Belgium field list (docs.stripe.com). The WAIT does not depend on that list: without KBO, live onboarding cannot complete honestly.

Crypto-asset / “trading in cryptocurrency” exclusions (Revolut Pro terms; processor MCC reviews) can still kill a USDC shop even **after** KBO. Do not plan Bancontact as a way to hide the rail.

### 1.5 FACTUUR leaking from sibling kits

Several 2026-08-26/27 PRs already had to strip placeholder `BE0…` and FACTUUR stamps. Club kits on this date (e.g. Harmonie VOORBEELD, SovereignForge shop) say **OFFERTE / VOORBEELD** and **KBO/BTW nog niet toegekend**. One leaked demo number on a live surge host is a false-identification problem. This plan’s WAIT on FACTUUR is a **ban**, not a “later this week” task.

PDF-by-email is **not** a 2026 Belgian **B2B** invoice between two VAT-taxable persons (Peppol BIS / EN 16931 since 1 Jan 2026). Selling invoice-adjacent HTML while unable to send a legal in-scope B2B invoice is a facts problem, not solved by a prettier PDF.

### 1.6 Peppol as if this repo were an Access Point

FPS e-factuur hub: Belgian VAT-taxable B2B = structured e-invoice. The **€25,000 vrijstelling still in scope**. B2C PDF remains allowed; even a B2C-only shop must **be able to receive** structured invoices from Belgian suppliers.

This operator / this repo / this seat **is not** a Peppol Access Point and will not become one. End-user software (after VAT identification) talks to a **certified** AP. Minting `0208:` + a fantasy enterprise number is a stamp. WAIT = after KBO + BTW-ID + a human pick of listed end-user software.

### 1.7 Privacy “no-coin” that is still a USDC product

Live `index.html` title: “Solana Invoice — 9 USDC.” Live `catalog.html` meta: “billed in USDC on Solana.” README opens with the treasury address. Builder’s EUR-first shop ([PR #119](https://github.com/eyeskull2220/solana-invoice/pull/119) `shop/sovereignforge/`, including a privacy page) is a **different face**. AVG art. 13 wants **controller identity first** at collection. A privacy fill-in that leads with USDC, Solana, Phantom, or `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3` fails NOW even if the rest of the page is Dutch.

**Adversarial split:** drafting no-coin fill-ins (this seat, NOW) does **not** restack the live treasury catalog (Builder). A buyer who only hits surge.sh still sees coin-first. Call that **Y** on the live catalog, not a fake Green on AVG.

Cookie theatre: GBA 17/11/2023 — no banner if zero non-necessary trackers. A banner “for compliance” on a tracker-free static page is noise and trains the team to ignore GBA. Analytics later = prior consent, not “gerechtvaardigd belang” as backup.

### 1.8 Opt-out line as a send licence

Scout already mailed **18** Tos on 2026-08-27; some omitted XII.13 §2 and used “antwoord ja of nee.” Playbook ([PR #117](https://github.com/eyeskull2220/solana-invoice/pull/117)): **do not second those Tos to patch opt-out.** CEO gates future mail ([PR #113](https://github.com/eyeskull2220/solana-invoice/pull/113)). NOW is: **when CEO later says yes, the draft must already contain a working electronic opt-out.** NOW is **not**: send, nudge, or “the 18 were CEO-gated so we are fine.”

WER XII.13 §1: prior consent default. B2B impersonal exception is **KB 4 Apr 2003, art. 1, 2°** (`info@`, `secretariaat@`, … to a **rechtspersoon**). Named humans, Hotmail/Gmail, eenmanszaak inboxes: **opt-in**, not this line. Sender proves consent (§4). Every advertising send still needs opt-out (§2 + KB art. 2).

Two different magic words already exist in sibling docs (`stop` in Scout playbook vs `UITSCHRIJVEN` in COMPLIANCE §12). Two words = one mail ships with neither, and the stop-list cannot match. This plan **picks one canonical token** (§3.2).

### 1.9 UNVERIFIED official pages treated as verified

COMPLIANCE.md marks FPS Economy / Finance / NBB CAP pages **UNVERIFIED** (captcha/Cloudflare on 2026-08-27). Citing those URLs as “fetched and confirmed” in a later Green cell is a stamp. Keep UNVERIFIED.

### 1.10 Rails and identity in the wrong order

Revolut Pro **before** Personal KYC (blocked by Pro Terms from 13 Jun 2025). Live Stripe/Mollie **before** KBO. Bijberoep hours untested. Social fund unfiled. Any one of these is enough for a processor or a fund to refuse. This plan does not open those rails.

---

## 2. WAIT — do not execute (stay R)

No task below is “book the loket,” “create a Stripe account,” “print FACTUUR,” or “register Peppol.”

### 2.1 KBO ~€111,50

| | |
|---|---|
| **What it is** | Statutory inschrijvingsrecht at an *erkend ondernemingsloket*: **€111,50 vrij van btw** from **1 Jan 2026** ([Liantis](https://www.liantis.be/nl/nieuws/nieuwe-kbo-tarieven-gekend)). Identical regulated tariff across loketten for that act. |
| **What it is not** | Self-service FPS form. A number this repo may invent. The full start cost. Permission to FACTUUR. |
| **Law** | WER III.49 §1 — register **before** the activity ([Justel, wet 9 Feb 2024](https://www.ejustice.just.fgov.be/eli/wet/2024/02/09/2024002118/justel)). |
| **This seat** | Does not book the counter. Does not pay €111,50. Writes `KBO/BTW: nog niet toegekend` until a human counter issues a number. |
| **Do not** | Paste a demo `0XXX.XXX.XXX` into shop/privacy/offerte. Pay the loket from Phantom “to get unblocked.” |

### 2.2 Stripe / Mollie **live**

| | |
|---|---|
| **What live means** | Charging Bancontact / cards / SEPA in **production**, with identity/business verification completed. |
| **Blocker** | No ondernemingsnummer. Mollie-class onboarding expects KBO details; natural-person / unregistered is the refuse. Stripe live needs the same class of identity. |
| **Not live** | Test keys. A created-but-restricted account. Polar/Gumroad/Payhip. A Bancontact logo on a VOORBEELD. |
| **This seat** | Does not create processor accounts. Does not mail Stripe/Mollie CS. Does not put IBAN or “betaal met Bancontact” as if live. |
| **After KBO (still not this plan)** | Human decision whether EUR processors sit beside Solana USDC. Crypto MCC / “trading” wording can still refuse. |

### 2.3 FACTUUR

| | |
|---|---|
| **Ban** | The word **FACTUUR** (and English **INVOICE** as a Belgian tax document) on anything this operator issues **before** KBO + VAT identification. |
| **Allowed** | **VOORBEELD**, **OFFERTE**, paper **journaal** (Coder). |
| **2026 B2B** | In-scope Belgian VAT-to-VAT = structured e-invoice, not PDF-mail ([efactuur.belgium.be](https://efactuur.belgium.be/nl/article/voor-wie-wordt-e-facturatie-verplicht)). |
| **This seat** | Grep/ban in later reviews. Does not “prepare a FACTUUR template for Friday.” |

### 2.4 Peppol

| | |
|---|---|
| **Mandate** | Since 1 Jan 2026, Belgian VAT-taxable B2B = Peppol BIS (unless a valid EN 16931 exception). Vrijstelling €25,000 **included**. B2C send still PDF-ok; **receive** from Belgian suppliers still required. |
| **This seat** | **Not an Access Point.** No participant ID. No AP application. |
| **WAIT until** | Real BTW-ID + listed **end-user** software. Humans pick the app. |
| **Do not** | Host a “Peppol kit” that claims to *be* the network. Mint `0208:` from a blank. |

---

## 3. NOW — startable (still not a stamp)

Two deliverables. Both are **docs and gates**. Neither restacks live surge.sh in this plan. Neither sends mail.

### 3.1 Privacy no-coin

**Goal:** a fill-in pack and review gate so any privacy surface (shop privacy page, later static `privacy.html`, mail footer that collects addresses) **does not lead with coin**.

**Lead (first screen / first paragraph):** who processes, what, why, legal bases. AVG art. 13 at collection ([GBA — recht op informatie](https://www.gegevensbeschermingsautoriteit.be/professioneel/avg/rechten-van-de-burgers/het-recht-op-informatie)).

**Below the fold, or a separate pay URL:** rails. No USDC / Solana / Phantom / treasury / mint in the **first** heading, meta description, or first paragraph of a privacy page.

**Leave blank — do not invent:**

```
Verwerkingsverantwoordelijke
  Naam: ______________________________
  Adres (Geel): ______________________
  KBO: nog niet toegekend
  Contact: (professional mailbox — not a personal Gmail in this repo)
  DPO: niet aangesteld (tenzij later verplicht)

Wat we verzamelen
  [ ] contactformulier  [ ] e-mail naar info@  [ ] niets (statische pagina)

Doeleinden + rechtsgrond (AVG art. 6): ____________________

Ontvangers / hosts
  Hosting: ______________  (name the processor: Surge / GitHub Pages / …)
  Buiten EU: [ ] nee  [ ] ja, waarborgen: ______________

Bewaartermijn of criteria: ____________________

Rechten: inzage, verbetering, wissing, beperking, bezwaar, overdraagbaarheid.
Klacht: Gegevensbeschermingsautoriteit — https://www.gegevensbeschermingsautoriteit.be/

Cookies / trackers
  Geen niet-strikte cookies, geen trackers → geen banner (GBA 17/11/2023).
  Analytics later = banner + prior consent. Not “gerechtvaardigd belang” as backup.

Betaling
  Aparte URL. Geen USDC in de eerste alinea van deze privacytekst.
```

**Gate (for later implementers / reviewers):**

- Files in scope when they exist: `shop/sovereignforge/privacy.html` (PR #119), any new `privacy.html` / `privacy.md` under `docs/` or `shop/`.
- **Out of scope for this seat’s NOW restack:** root `index.html`, `catalog.html`, `README.md`, `solana-invoice.html` (Builder hide-the-coin / EUR shop). Flag them as coin-first **Y**, do not rewrite them in a Compliance “privacy” PR unless CEO explicitly re-scopes.
- Grep fail if the **first 40 lines** of a privacy HTML, or the first heading + first `<p>` / lead paragraph, match `USDC|Solana|Phantom|spl-token|96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3|EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v`.
- Grep fail if privacy copy contains `FACTUUR`, `BE0`, `BE1`, a 10-digit KBO lookalike, or “AVG-compliant” / “GDPR-compliant” badge.
- Grep fail if a cookiebanner is added while the same tree has no tracker (`gtag`, pixels, analytics).
- Fill-ins stay fill-ins until a human writes a real name and a professional contact. Blank is honest. Invented identity is a stamp.

**Done when:** a later PR can land `docs/rgy-2026-08-27/compliance/03-privacy-fillins.md` (or equivalent shop privacy) that passes the grep gate, still says **not a stamped policy**, and still has `KBO: nog niet toegekend`.

### 3.2 Opt-out on future CEO-gated mail

**Goal:** one canonical opt-out **token and sentence** that Scout must paste into any future advertising draft **before** CEO may gate a send. This plan does **not** send. It does **not** second the 18. It does **not** invent mailtos.

**Canonical token:** `stop` (case-insensitive). Also honour `STOP`, `uitschrijven`, `UITSCHRIJVEN` on the stop-list so old drafts are not traps. **New drafts print `stop` only**, so matching is trivial.

**Canonical sentence (Dutch, unshortened):**

> Als u in de toekomst geen voorstellen van ons meer wilt ontvangen, antwoord dan **stop** op deze mail. Dat is kosteloos en zonder reden. Wij zetten u dan op onze stoplijst.

Electronic means = reply to the **same thread**. No tracking link. No phone-only. No “antwoord ja of nee” as a substitute (that is not XII.13 §2).

**CEO gate contract (future sends only):**

1. Scout draft exists.  
2. Checklist in `docs/ultra-seats/OUTREACH-PLAYBOOK.md` all pass (rechtspersoon, impersonal mailbox, not on the 18, not HOLD, ≥10 minutes since last send, euro only, no coin in the mail).  
3. The canonical opt-out sentence is in the body.  
4. **CEO says yes.**  
5. Human sends. This seat still does not send.

If step 3 is missing, CEO **must refuse**. A CEO yes without opt-out is an invalid gate.

**Not covered by this line (still BLOCKED / opt-in):**

- Named `voornaam.naam@`, Hotmail/Gmail/Telenet, eenmanszaak / natural-person traders.  
- Seconds to the 18 of 2026-08-27 (including “we forgot opt-out”).  
- Burst sends. CS mail from this seat.

**Stop-list (human, after a real send):** on `stop` / `uitschrijven`, acknowledge **non-promotional** within 24–48h, stop, log. Do not put the operator’s personal Gmail in the repo.

**Done when:** a later PR can land a short `docs/rgy-2026-08-27/compliance/04-ceo-mail-opt-out.md` (or a subsection in CEO.md / SCOUT.md) that quotes the canonical sentence, states “CEO yes without this sentence = invalid gate,” and still says **do not send from this file**.

---

## 4. RGY board (after the adversarial pass)

Legend: **R** = do not do / blocked / wait. **Y** = fact that stays thin; not this seat’s NOW restack, or depends on a human. **G** = startable copy/gate, **not** a legal stamp.

| Item | Color | Why |
|---|---|---|
| KBO ~€111,50 (loket act) | **R** | WAIT. Human counter. No invented number. Fee is not the whole start. |
| Stripe **live** | **R** | WAIT. No enterprise identity. Test ≠ live. |
| Mollie **live** | **R** | WAIT. Ondernemingsnummer expected. Same identity gap. |
| FACTUUR | **R** | Ban until KBO + BTW-ID. VOORBEELD / OFFERTE only. PDF ≠ 2026 B2B. |
| Peppol send/receive IDs | **R** | WAIT. Not an Access Point. After BTW-ID + end-user software. |
| File (e604, CAP, RSVZ, Intervat) | **R** | BLOCKED. Humans only. |
| Send mail / CS / seconds to the 18 | **R** | BLOCKED. Opt-out is not a licence. |
| Revolut Pro | **R** | BLOCKED until Personal KYC; Pro terms ≠ KBO. |
| Live treasury catalog / pay / README (coin-first) | **Y** | Already selling-shaped; Builder EUR-face is a different tree. Compliance does not restack surge.sh in this plan. Still legally thin (WER III.49). |
| Shop privacy.html (PR #119) vs fill-ins | **Y** | Shop may already hide coin; still blanks for controller identity. Align with §3.1 gate; do not badge “AVG-compliant.” |
| Cookie banner | **Y** | **No banner** while zero trackers (GBA). Banner without trackers = theatre (**R** if added). Banner **with** analytics = separate consent work, not NOW. |
| Bijberoep vs hoofdberoep | **Y** | Accountant + payslips. Do not code it here. |
| UNVERIFIED FPS/NBB URLs | **Y** | Keep the label. Do not promote to fetched-confirmed. |
| Kraken CAP / Vak XIII | **Y** | Separate file. Do not CAP paper. Do not CAP Phantom. Do not file from here. |
| Privacy no-coin fill-ins + grep gate | **G** | NOW. Draft only. Not a stamped policy. |
| Opt-out on **future** CEO-gated mail | **G** | NOW. Canonical `stop` sentence + invalid-gate rule. Not a send. |

**There is no Green cell that means “compliant.”** Green means “the next markdown/gate may be written.”

---

## 5. Implementation tasks (NOW only)

> For later workers: do **not** use this list to file, stamp, or send. WAIT rows have no implementer steps.

### Task 1: Privacy no-coin fill-ins

**Files:**

- Create: `docs/rgy-2026-08-27/compliance/03-privacy-fillins.md`
- Do **not** modify: `index.html`, `catalog.html`, `README.md`, `solana-invoice.html` (unless CEO re-scopes)
- Review against, do not silently overwrite: `shop/sovereignforge/privacy.html` if/when PR #119 exists in the tree

**Steps:**

- [ ] Copy the fill-in block from §3.1. Keep blanks. `KBO: nog niet toegekend`.
- [ ] State in the header: **not a stamped privacy policy**, not AVG-compliant, not a DPO appointment.
- [ ] Put any payment-rail mention **after** controller / purposes / rights — or omit rails and link “betaalpagina (aparte URL).”
- [ ] Run, from repo root, a first-40-lines check on that file (and on any privacy HTML in the same PR):

```bash
python3 - <<'PY'
from pathlib import Path
import re, sys
needles = re.compile(
    r"USDC|Solana|Phantom|spl-token|96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3|"
    r"EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v|FACTUUR|BE0\d|AVG-compliant|GDPR-compliant",
    re.I,
)
paths = list(Path("docs/rgy-2026-08-27/compliance").glob("03-privacy*.md"))
paths += list(Path("shop").glob("**/privacy.html")) if Path("shop").exists() else []
bad = []
for p in paths:
    head = "\n".join(p.read_text(encoding="utf-8").splitlines()[:40])
    if needles.search(head):
        bad.append(str(p))
if bad:
    sys.exit("coin/stamp in privacy lead:\n" + "\n".join(bad))
print("privacy lead gate: pass")
PY
```

Expected: `privacy lead gate: pass`

- [ ] Commit only the fill-ins file (+ gate note). Do not add a cookiebanner.

### Task 2: CEO-gated mail opt-out contract

**Files:**

- Create: `docs/rgy-2026-08-27/compliance/04-ceo-mail-opt-out.md`
- Point at, do not send from: `docs/ultra-seats/OUTREACH-PLAYBOOK.md`, `docs/ultra-seats/CEO.md` (when present)

**Steps:**

- [ ] Quote the canonical `stop` sentence from §3.2.
- [ ] Write the five-step gate. Explicit: **CEO yes + missing sentence = invalid.**
- [ ] List honour-on-receipt tokens: `stop`, `STOP`, `uitschrijven`, `UITSCHRIJVEN`.
- [ ] Ban seconds to the 18; ban this seat sending; ban personal Gmail in the file.
- [ ] Commit. Do not open Gmail. Do not add mailto: for a club.

### Task 3: WAIT freeze in the same folder

**Files:**

- Modify only if a later worker is tempted to add “KBO how-to” or “Mollie signup” under `docs/rgy-2026-08-27/compliance/`.

**Steps:**

- [ ] Do **not** create `05-kbo.md`, `05-stripe.md`, `05-mollie.md`, `05-factuur.md`, `05-peppol.md` as executable runbooks.
- [ ] If someone needs a pointer, one line: “WAIT — see `02-adv-plan.md` §2. Not this week’s implementer work.”

---

## 6. Failures that would make this a stamp

| Failure | What it looks like |
|---|---|
| Green = compliant | PR title “Compliance complete” / README badge. |
| Invented identity | Any `BE0`, Peppol `0208:`, IBAN, GSM, personal Gmail in these files. |
| FACTUUR | The word on an operator-issued PDF/HTML. |
| Live rails | Stripe/Mollie production keys, Bancontact button that charges. |
| Access Point cosplay | Repo claims to be Peppol / AP. |
| Send | Any mail from this seat; any second to the 18 “to add opt-out.” |
| Banner theatre | Cookie popup on a tracker-free page. |
| Coin-first privacy | USDC in the privacy lead. |
| Paying €111,50 in the doc | “Loket paid” without a human counter and a real number. |
| Promoting UNVERIFIED | Captcha-blocked FPS pages cited as confirmed. |

---

## 7. Sources (dated)

Fetched or confirmed **2026-08-27** unless marked UNVERIFIED.

| Topic | URL | Note |
|---|---|---|
| KBO tariff 2026 | https://www.liantis.be/nl/nieuws/nieuwe-kbo-tarieven-gekend | €111,50 vrij van btw from 1 Jan 2026 |
| WER III.49 §1 | https://www.ejustice.just.fgov.be/eli/wet/2024/02/09/2024002118/justel | KBO before activity |
| Peppol who-is-in-scope | https://efactuur.belgium.be/nl/article/voor-wie-wordt-e-facturatie-verplicht | page 09/10/2024; €25k vrijstelling in scope; fetched 2026-08-27 |
| Peppol mandate hub | https://efactuur.belgium.be/nl/article/gestructureerde-elektronische-facturen-tussen-ondernemingen-verplicht-sinds-2026 | since 1 Jan 2026 |
| Peppol software vs AP | https://efactuur.belgium.be/nl/article/softwareoplossingen-voor-het-verzenden-ontvangen-en-verwerken-van-elektronische-facturen | end-user, not AP |
| GBA cookies | https://www.gegevensbeschermingsautoriteit.be/cookies-en-andere-traceringsmiddelen | last update 17/11/2023 |
| GBA art. 13 | https://www.gegevensbeschermingsautoriteit.be/professioneel/avg/rechten-van-de-burgers/het-recht-op-informatie | information at collection |
| KB 4 Apr 2003 | https://www.ejustice.just.fgov.be/eli/besluit/2003/04/04/2003011238/staatsblad | impersonal B2B `info@` exception |
| FPS spam FAQ PDF | https://economie.fgov.be/nl/file/134162/download?token=maqS0JmV | XII.13 restatement |
| Baseline seat pack | https://github.com/eyeskull2220/solana-invoice/pull/116 | research only; nobody stamped |
| Scout playbook | https://github.com/eyeskull2220/solana-invoice/pull/117 | `stop` line; do not send |
| CEO seat | https://github.com/eyeskull2220/solana-invoice/pull/113 | gates mail; no send in that PR |
| EUR shop + privacy | https://github.com/eyeskull2220/solana-invoice/pull/119 | separate face; still not a stamp |

**UNVERIFIED this plan (do not upgrade):** Stripe Belgium live onboarding field list; FPS Finance VAT-exemption HTML (captcha in the seat pack); NBB CAP how-to (Cloudflare in the seat pack).

---

End of plan. **Nobody stamped.** WAIT stays WAIT. NOW is fill-ins and an opt-out gate, not a send and not a loket.
