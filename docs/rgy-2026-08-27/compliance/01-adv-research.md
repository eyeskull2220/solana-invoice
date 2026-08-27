# COMPLIANCE RESEARCH — adversarial first, then RGY

**Seat:** COMPLIANCE  
**Date:** 2026-08-27  
**File:** `docs/rgy-2026-08-27/compliance/01-adv-research.md`  
**Method:** adversarial read first; RED / YELLOW / GREEN after. Any RED makes the pack RED.

**This file is not legal, tax, social-security, or data-protection advice.** It is not a stamp. It is not a filing. It does not create a KBO number, a VAT number, a Peppol ID, an IBAN, or a FACTUUR. Confirm every figure with the cited official page, an *erkend ondernemingsloket*, a social insurance fund, and an ITAA accountant **before** any human filing.

Where a live official page was captcha- or bot-blocked on 2026-08-27, the row is **UNVERIFIED** (URL still given). Do not treat an UNVERIFIED row as a stamp.

---

## 0. Hard bans for this file

| Ban | Meaning |
|---|---|
| **Not a lawyer** | Research pointers. No advice. No “you are compliant.” |
| **Never stamp** | No FACTUUR, no “KBO active,” no “already classified as 10%,” no “opt-out cured.” |
| **Never file** | No e604, CAP, RSVZ, Intervat, MyMinfin, GBA, Revolut, or Stripe CS. |
| **Never invent KBO/VAT/IBAN** | Write `KBO/BTW: nog niet toegekend`. No placeholder `BE0…`. |
| **Never FACTUUR** | Third-party documents stay **OFFERTE** / **VOORBEELD**. |
| **No CS mail** | This file does not send. It does not “fix” already-sent mail with a second. |

---

## 1. Operator facts (this run)

Stated for this research. Not a completed start-up.

| Fact | State on 2026-08-27 |
|---|---|
| Track | Belgian **bijberoep** (intended). Hours test **UNVERIFIED** here. |
| KBO | **None.** `KBO/BTW: nog niet toegekend`. |
| Documents | **OFFERTE only.** No FACTUUR. |
| Revolut | **Personal KYC denied.** Revolut Pro is blocked until a Personal account exists. |
| IBAN | **None** (no Belgian EUR current account in this pack). |
| Stripe | **No live Stripe.** Test mode is not a shop. |
| Rails that *are* live on `main` | Public catalog + pay page lead with **USDC on Solana** and a treasury address. |

Live `main` (this checkout, 2026-08-27):

- `index.html` — first screen: “Solana Invoice. One file. **9 USDC**.” Pay card: “Pay 9 USDC on Solana.” Treasury address printed. Signature paste field.
- `catalog.html` — lead: “Billed in **USDC on Solana**.” Treasury address in a warning box.
- `README.md` — treasury address + USDC mint in the first lines.
- **No** privacy page, cookie notice, controller identity, or opt-out URL in this repo (`privacy`, `opt-out`, `UITSCHRIJVEN`, `persoonsgegevens`: zero hits).

An unmerged euro-only OFFERTE face exists on another branch (PR 111). It is **not** what `main` serves today. This file scores the live USDC-lead, not the unmerged face.

---

## 2. ADVERSARIAL FIRST

Read this section before the colour table. A hostile reader is FPS Finance, RSVZ, GBA, FOD Economie, a mailed club’s lawyer, or Revolut/Stripe KYC. They do not owe the operator a charitable gloss.

### 2.1 The operation already looks like an activity

WER art. III.49 §1 (wet 9 February 2024, BS 21 March 2024, numac `2024002118`): register in the KBO **before** activities start. A public catalog of priced SKUs, a live pay-to, “one-job automation,” and a burst of Dutch *voorstellen* is not a hobby drawer. “We only take USDC,” “Revolut said no,” and “OFFERTE not FACTUUR” do not move the start-date. The counter is still empty.

### 2.2 Privacy identity is a wallet

AVG art. 13 (GBA: information **at collection**) wants the **controller** first: who, contact, purposes, legal basis. Live pages open with a mint, a network, and `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3`. There is no `verwerkingsverantwoordelijke`. Personal data **already left the building**: organisational mailboxes were written to on 2026-08-26 and 2026-08-27; the pay page invites a Solana transaction signature (an on-chain identifier tied to a payer). A GBA file that starts “we take USDC” has already failed the first fact.

### 2.3 Already-sent advertising mail without XII.13 §2

WER XII.13 §1: electronic advertising needs prior, free, specific, informed consent, unless a KB exception applies. XII.13 §2: **every** advertising send must (1) explain the right to object to future advertising and (2) give a working electronic means. The B2B impersonal exception (KB 4 April 2003, art. 1, 2°) drops **opt-in**, not **opt-out**. The Verslag aan de Koning says the rechtspersoon must be told of the objection right **on every** advertising message.

The Scout pack (same calendar day) records **18** Tos mailed on 2026-08-27 plus a 2026-08-26 wave. Several 2026-08-27 bodies used “antwoord ja of nee” and **omitted** XII.13 §2. At least one quoted **900 USDC** and a Solana pay-to. Twelve Tos left in about one minute (18:47–18:48 UTC). That is a completed send log, not a hypothetical. A second mail “to add the opt-out” is another advertising message to the same To — FOD *Spam in 23 vragen* vraag 8 plus the operator’s own no-seconds rule. You cannot unsend. You cannot stamp the gap closed from this seat.

### 2.4 10% / 33% is the wrong cupboard for fees

A hostile tax reader will not let the operator park **fees for work** in the new 10% *meerwaardebelasting* or the old 33% miscellaneous bucket.

- **10%** (wet 6 April 2026, BS 21 April 2026, numac `2026002780`, inwerkingtreding 1 January 2026) sits in WIB 92 art. 90, first lid, **9°**: gains realised **“buiten het uitoefenen van een beroepswerkzaamheid”** and in the **normal management of private assets**, on transfer for consideration of financial assets. Art. 92 §1 c) includes **cryptoactiva** (digital representation of a value or right, DLT, including tokens usable for payment). Art. 171, 2°, e) + art. 269 §1, 5°: **10%**. Art. 96/2, 6°: those 9° c) amounts are **exempt from this tax to the extent they are already taxable as movable or professional income**.
- **33%** remains the miscellaneous / abnormal-management line (WIB 92 art. 90, 1° as cross-referenced by the same 2026 law; municipal surcharge on top). Still **not** a fee for a delivered job.
- **USDC received for a priced tool or a one-job automation** is consideration for a supply. That is **beroepsinkomen** (WIB 92 art. 23 — Justel coordination of WIB 92 is **stale**; confirm on Fisconetplus / with the accountant). Holding the token does not defer the fee. “Stablecoin so not a gain” is a different question from “I was paid.”

Nobody in this pack (ITAA, ruling, FPS) has **stamped** which cupboard each euro sits in. A mixed personal Phantom that later shows both (a) private USDC lots and (b) customer payments is how 10%/33% and Vak IV get argued into the same signature. Unstamped is not “probably 10%.” Unstamped is “FPS can pick the worst coherent story.”

### 2.5 Rails closed, shop open

Revolut Personal KYC **denied** → no Pro, no IBAN from that path. Live Stripe **WAIT** (no enterprise identity to verify). That does **not** freeze the Solana pay-to already printed on `main`. A KYC refusal is a bank’s risk decision. It is not a Belgian exemption from KBO, VAT identification, or books.

### 2.6 What a hostile one-liner sounds like

> Unregistered natural person in Geel, no KBO, no IBAN, Revolut Personal refused, no live Stripe, public USDC catalog, advertising mail already sent without a working opt-out, and no accountant stamp that USDC-for-work is Vak IV rather than 10% or 33%.

That sentence does not need a FACTUUR to be usable.

---

## 3. RGY scores

Adversarial section first. Colours second. **GREEN** would mean: fact pattern matches a cited duty, and the live artefact already does the duty. None of the three scored items are GREEN.

| Item | Score | One-line note |
|---|---|---|
| **Privacy USDC-lead** | **RED** | Live identity is a mint and a treasury address. No controller. Collection already happened (mail + signature field). Art. 13 wants who/why first. |
| **Missing opt-out on already-sent mails** | **RED** | XII.13 §2 is mandatory on every advertising send, including the B2B `info@` exception. The send already happened. A second is not a cure. |
| **10% / 33% unstamped** | **YELLOW** | Statute puts **fees for work** outside 10% and outside 33%. No ITAA stamp yet. Turns **RED** the moment anyone books a service fee as 10% or 33%. |

**Pack score: RED.** Two completed RED artefacts (USDC-lead on `main`; already-sent mail without §2). The yellow item is a classification gap, not a free pass.

---

## 4. Notes per scored item

### 4.1 Privacy USDC-lead — **RED**

**Duty (research, not a stamp).** GBA, *Het recht op informatie* (fetched 2026-08-27): when personal data are collected from the person, give identity and contact of the controller, purposes and legal basis, recipients, retention, rights, GBA complaint — **at collection**. Layered is allowed. Leading with a pay-to is the wrong first layer.

**Live artefact.** `index.html` / `catalog.html` / `README.md` lead with USDC, Solana, and the treasury address. Zero privacy copy in this repo. The pay page collects a transaction signature. Outreach already processed organisational (and, on some waves, whatever Tos were in SENT) contact data.

**Why not YELLOW.** A static page with **no** collection can wait on a thin “we don’t collect” line. This operator already mailed, and the pay page is a collection surface. The missing page is not the only problem: the **lead** of every public surface is the rail.

**Do not do from this seat.** Invent a controller name, a personal Gmail, a KBO, or a USDC-first “privacy” blurb. Do not add a cookie banner for theatre (GBA 17/11/2023: no banner if zero non-necessary trackers — in-repo HTML has no `gtag`/pixels on this fetch).

**STARTABLE (human copy, still unstamped):** a privacy fill-in that opens with **who processes what and why**, KBO left blank (`nog niet toegekend`), payment rails **below** or on a separate pay URL. Euro shop face (PR 111) is a related STARTABLE for marketing pages — it does not by itself satisfy art. 13.

### 4.2 Missing opt-out on already-sent mails — **RED**

**Duty.** WER XII.13 §2 (wet 15 December 2013, ELI `2013011667`) + KB 4 April 2003 art. 2 (numac `2003011238`). Opt-out is not optional on the rechtspersoon exception. “Antwoord ja of nee” is a prompt, not an objection right plus an electronic means.

**Live artefact.** Operator-stated / Scout-recorded: 18 Tos on 2026-08-27 + 2026-08-26 wave. Several 2026-08-27 mails omitted §2. Burst cadence. At least one USDC/pay-to body. This file does **not** reprint Tos (they are already on a stop-list in the Scout seat). They are listed there so they are **not** mailed again.

**Why not YELLOW.** The breach, if the messages were *reclame* (WER I.18, 6° — promotion of services/image), is in SENT, not in a draft.

**Do not do from this seat.**

- Do **not** send a second to “add UITSCHRIJVEN.” That is another advertising send to the same To.
- Do **not** mail named natural-person boxes, Hotmail/Gmail/Telenet, or guessed `info@`.
- Do **not** claim the KB exception for an *eenmanszaak* / natural-person trader.

**STARTABLE:** keep the already-mailed Tos on a stop-list; honour any **stop** with a non-promotional ack (KB art. 2); future first voorstel only with §2 on the body, euro-only, impersonal rechtspersoon mailbox copied from a fetched public page, KBO Public Search the same session. **BLOCKED to send** from this research file.

Sanctions research pointer (not a prediction): WER XV.120 (niveau 3) / XV.121 (niveau 4 in bad faith) — confirm on the same Justel consolidation as XII.13.

### 4.3 10% / 33% unstamped — **YELLOW**

**What the 2026 law actually gates (fetched Justel 2026-08-27).**

| Cupboard | Hook | Fits USDC **fee for a job**? |
|---|---|---|
| **10%** *meerwaarde* | Wet 6 April 2026 → WIB 92 art. 90, first lid, **9° c)** + art. 171, 2°, e) / art. 269 §1, 5°. Only **outside** a professional activity, **normal** private management, on a **transfer for consideration** of financial assets (crypto included: art. 92 §1 c)). | **No** — the fee is the professional supply, not a private disposal. Art. 96/2, 6° typedwang: already-professional amounts are out of this tax. |
| **33%** miscellaneous / abnormal | WIB 92 art. 90, **1°** (abnormal management / speculation); municipal surcharge. The 2026 law did **not** abolish this line. | **No** — still not a customer payment for work. |
| **Beroepsinkomen** | WIB 92 art. 23 (profits / proceeds / remunerations from a professional activity). Progressive PB + Geel municipal + RSVZ on net profit (bijberoep floors are a **separate** stamp). | **This is the cupboard the hostile reader will try first** for priced tools / one-job automation. **Unstamped** until an ITAA writes it. |

Exemption slice in art. 96/2, first lid, 2° is **€4,855** (indexable under art. 178). Secondary write-ups quote ~**€10,000** for income year 2026. **UNVERIFIED** exact indexed 2026 euro without the FPS index table. Irrelevant to a service fee: the fee is not in art. 90, 9°.

Self-reporting: art. 313, first lid, 7° (as amended) — 9° c)/d) crypto and currency gains are **not** covered by the withholding-liberatory shortcut in the same way as banked 9° c) instruments. Crypto **gains** (if they ever are gains) are self-reported. That is still not a licence to call a **fee** a gain.

**Why YELLOW, not RED, not GREEN.**

- **Not GREEN:** no accountant, no ruling, no books, no KBO. Unstamped means unstamped.
- **Not RED (yet):** this file has **no** evidence of a filed return that put service fees in 10% or 33%. The gap is classification, not a completed wrong box.
- **RED trigger:** any invoice, OFFERTE footnote, mail, or later return that treats USDC-for-work as “just the 10% crypto tax” or “33% diverse inkomsten.” Same for mixing customer receipts into a private-lot FIFO until an ITAA draws the line.

**Wallet hygiene (still a gap).** Personal Phantom + professional receipts in one pile is how 10%/33% (later disposal of private lots) and Vak IV (fees) get argued together. Dedicated receiving address after KBO is bookkeeping, not a registration.

**STARTABLE:** accountant one-pager question: “Confirm in writing that USDC received as consideration for tools/services is Vak IV *beroepsinkomen* at EUR-on-receipt (ECB USD/EUR; document 1 USDC ≈ 1 USD), and is **not** art. 90, 9° (10%) and **not** art. 90, 1° (33%).” **BLOCKED:** this seat does not pick the box on a return.

---

## 5. STARTABLE / BLOCKED / WAIT (this pack)

| Bucket | What | Why |
|---|---|---|
| **STARTABLE** | Privacy fill-ins that **do not** lead with USDC | Art. 13. Blanks for name/address. No invented KBO. |
| **STARTABLE** | Stop-list + future Scout line **with** XII.13 §2 | Draft only. Do not send. Do not second the already-mailed Tos. |
| **STARTABLE** | Accountant question on Vak IV vs 10%/33% | One-pager. Not a return. |
| **BLOCKED** | File / stamp / CS mail | KBO, e604, CAP, FACTUUR, Revolut/Stripe support, “opt-out cured” seconds. |
| **WAIT** | KBO day | WER III.49. Counter only. |
| **WAIT** | Live Stripe | No enterprise identity. |
| **WAIT** | Revolut Pro / IBAN | Personal KYC denied. Pro Terms require an existing Personal account. |
| **WAIT** | Peppol | After VAT identification. End-user software. Not an Access Point. |

---

## 6. Sources (official, dated)

Fetched or attempted **2026-08-27**.

| Topic | URL | Note |
|---|---|---|
| WER III.49 §1 | https://www.ejustice.just.fgov.be/eli/wet/2024/02/09/2024002118/justel | KBO before start; BS 21 Mar 2024 |
| AVG art. 13 / GBA information duty | https://www.gegevensbeschermingsautoriteit.be/professioneel/avg/rechten-van-de-burgers/het-recht-op-informatie | Fetched 2026-08-27; at collection; identity first |
| GBA cookies | https://www.gegevensbeschermingsautoriteit.be/cookies-en-andere-traceringsmiddelen | Last update 17/11/2023; no banner if only strictly necessary |
| WER XII.13 | https://www.ejustice.just.fgov.be/eli/wet/2013/12/15/2013011667/justel | Opt-in default; §2 opt-out always |
| KB 4 Apr 2003 | https://www.ejustice.just.fgov.be/eli/besluit/2003/04/04/2003011238/justel | Art. 1, 2° impersonal rechtspersoon; art. 2 objection; Verslag: tell them **every** send |
| Same, Staatsblad body | https://www.ejustice.just.fgov.be/cgi/article_body.pl?language=nl&caller=summary&pub_date=03-05-28&numac=2003011238 | pub. 28 May 2003 |
| FOD Economie *Spam in 23 vragen* | https://economie.fgov.be/nl/file/134162/download?token=maqS0JmV | Official PDF; vragen 13–14 opt-out on exception |
| Meerwaarde 10% (primary) | https://www.ejustice.just.fgov.be/eli/wet/2026/04/06/2026002780/justel | Wet 6 Apr 2026; BS 21 Apr 2026; numac `2026002780`; fetched 2026-08-27 |
| Same, Staatsblad | https://www.ejustice.just.fgov.be/eli/wet/2026/04/06/2026002780/staatsblad | ELI listing fetched 2026-08-27 |
| WIB 92 (code identity) | https://www.ejustice.just.fgov.be/eli/wet/1992/04/10/1992041050/justel | **Stale coordination** — use Fisconetplus / accountant for art. 23 / 90, 1° |
| ECB USD/EUR | https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html | Booking method for an accountant, not a stamp |
| Revolut BE Pro Terms | https://www.revolut.com/en-BE/legal/pro/ | From 13 June 2025; Personal account required |
| ITAA directory | https://www.itaa.be/ | Find a practitioner; this seat does not engage one |
| Indexed €10,000 exemption | FPS Finance index table for art. 96/2, 2° / art. 178 | **UNVERIFIED** this fetch (law’s unindexed slice is €4,855) |

---

## 7. What this file is not

- Not a lawyer. Not a stamp. Not a FACTUUR.
- Not a KBO, VAT, Peppol, CAP, or RSVZ filing.
- Not a cure for already-sent mail.
- Not a classification of any USDC lot as 10% or 33% or Vak IV.
- Not CS mail and not a second to the already-mailed Tos.
- Not an Access Point. Not live Stripe. Not a Revolut IBAN.

Next human move is an *ondernemingsloket* + social insurance fund + ITAA conversation — **WAIT / BLOCKED** for this seat — not an edit that inserts a made-up number or a retroactive opt-out.

**Nobody stamped.**
