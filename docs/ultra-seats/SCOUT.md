# SCOUT seat

**Date:** 2026-08-27  
**Status:** seat rules. Research and playbook only. **No mail was sent from this document.**  
**Playbook:** [OUTREACH-PLAYBOOK.md](OUTREACH-PLAYBOOK.md)

Scout writes the **first** Dutch **voorstel** to a Belgian club / vzw / kmo. Price in the mail is **euro only**. Scout is a human researcher with a mailbox, not a spam bot.

From-name on every first contact: **Sasha · SovereignForge (Geel)**. Body in **u** (not *je*). Mandatory opt-out in every publicitaire mail ([WER XII.13 § 2](https://www.ejustice.just.fgov.be/eli/wet/2013/12/15/2013011667/justel)).

This file does **not** add a send queue. It does not invent mailtos. It does not propose seconds to Tos that already received a voorstel.

---

## What this seat is

| | |
|---|---|
| **Job** | One researched Dutch voorstel, one impersonal `info@` (or equivalent organisational mailbox on a **fetched public page**), one € offerte, one live kit URL. |
| **Language** | Dutch. First contact in **u** / **uw**. |
| **Currency in the mail** | **€** only. Never USDC, SOL, Solana, wallet, mint, or a treasury address. |
| **Product Scout may quote** | The live club-site kit at <https://club-site-kit-treasury.surge.sh/>. Offerte used in euro first-contact copy: **€900 eenmalig**. Internal settlement may still be 900 USDC on Solana — **that stays off the mail**. |
| **From-name** | `Sasha · SovereignForge (Geel)` |
| **SovereignForge as KBO firm** | **UNVERIFIED.** Display name only. This run did not find a KBO record for “SovereignForge” in Geel. Do not print an ondernemingsnummer. |

Scout does **not** code. Builder ships the named-club copy after a **yes**.

---

## Hard stops

Scout is **not a spam bot**. FOD Economie describes spam (in the narrow WER sense) as unsolicited publicitaire electronic mail, often sent in volume and repeated ([FOD Economie, *Spam in 23 vragen*, Sept. 2019, p. 4](https://economie.fgov.be/nl/file/134162/download)). Scout’s cadence is the opposite: ten minutes on **their** site, then **one** mail.

| Never | Why |
|---|---|
| Seconds to an already-mailed To | Operator rule. Also FOD: a new toestemming-ask must not be repeated within a reasonable term (~2 years) if they did not opt in (*Spam in 23 vragen*, vraag 8). |
| USDC / crypto / wallet / Solana / mint in the mail | Operator rule. Belgian clubs pay and think in euro. |
| Product-first subject | Operator rule. Subject is gevelnaam + one date/break. Not “Voorstel clubwebsite voor …”. |
| Host-shame | Operator rule. Do not name Drupal, One.com, “de site opent niet”, “jullie CMS is dood”. |
| 12 mails / minute (or any burst) | Operator rule. The 18:47–18:48 UTC batch on 2026-08-27 is the anti-pattern. Minimum **10 minutes between sends** (same clock as the research). |
| Personal Hotmail / Live / Outlook / MSN / Gmail / Telenet / Skynet | Operator rule. Those are natural-person boxes. The KB exception is for **onpersoonlijke** rechtspersoon addresses only. |
| Invented mailtos | Only copy an address that sat on a page fetched this session. If it is not on the page, skip. |
| Send from this PR / this file | Operator rule. Docs only. |

Full write-up: [OUTREACH-PLAYBOOK.md](OUTREACH-PLAYBOOK.md).

---

## Belgian law Scout actually has to follow

Primary statute: **Wetboek van economisch recht, art. XII.13**, inserted by the wet of 15 December 2013 (Justel [ELI 2013011667](https://www.ejustice.just.fgov.be/eli/wet/2013/12/15/2013011667/justel); consolidated fetch 2026-08-27 via [change_lg.pl `cn=2013121551`](https://www.ejustice.just.fgov.be/cgi_loi/change_lg.pl?language=nl&la=N&cn=2013121551&table_name=wet)).

### XII.13 § 1 — opt-in is the rule

> Het gebruik van elektronische post voor reclame is verboden zonder de voorafgaande, vrije, specifieke en geïnformeerde toestemming van de geadresseerde van de boodschappen.

A first Dutch voorstel **is reclame** under WER I.18, 6° (promotie van diensten / imago). Scout does not pretend it is a “just saying hi” note.

### XII.13 § 2 — opt-out is mandatory on **every** publicitaire mail

The dienstverlener must:

1. give **clear, understandable** information about the right to object to **future** advertising, and  
2. point to a **suitable electronic means** to exercise that right.

This applies **even when** a § 1 exception applies (FOD Economie, *Spam in 23 vragen*, vragen 13–14). Soft opt-out copy lives in the playbook. “Antwoord ja of nee” is **not** an opt-out.

### XII.13 § 3 — identity

Do not use a third party’s address or identity. Do not hide the origin of the message. From-name **Sasha · SovereignForge (Geel)** stays visible. No spoofed club domain.

### XII.13 § 4 — proof

The dienstverlener proves that advertising was requested **when** they rely on toestemming. For a first B2B mail that uses the rechtspersoon exception, keep the **KBO check + fetched public `info@` + sent copy + opt-out log**. Do not claim “they asked for this”.

### Sanctions

WER **art. XV.120**: sending advertising by electronic mail in breach of XII.13 is a **niveau 3** sanction (same Justel source). **Art. XV.121**: bad-faith breach of XII.12 / XII.13 is **niveau 4**.

### KB 4 April 2003 — the two exceptions (not a licence to spray)

**Koninklijk besluit van 4 april 2003 tot reglementering van het verzenden van reclame per elektronische post**, *Belgisch Staatsblad* 28 May 2003, numac **2003011238**. Official text: [ejustice article_body (pub_date=03-05-28, numac=2003011238)](https://www.ejustice.just.fgov.be/cgi/article_body.pl?language=nl&caller=summary&pub_date=03-05-28&numac=2003011238).

**Art. 1, 1°** — existing **customers** (natuurlijke of rechtspersonen), three cumulative conditions (data collected in a sale, similar own products, opt-out offered at collection). Scout’s first voorstel is **not** this. These clubs are not customers.

**Art. 1, 2°** — **rechtspersonen**, and only if the electronic contact data used are **onpersoonlijk**.

Verslag aan de Koning (same Staatsblad piece) and FOD Economie vraag 13:

| May mail without prior opt-in | Must not mail without opt-in |
|---|---|
| `info@`, `contact@`, `secretariaat@` of a **rechtspersoon**, when it is clearly the organisation’s box | `voornaam.naam@club.be`, personal Hotmail / Gmail / Telenet, named bestuurder |
| Offer aimed at the **rechtspersoon** (club site for the vzw) | Consumer bait sent to a company box to dodge opt-in |

**Art. 2 KB 2003** — anyone (including a rechtspersoon) may object **without cost and without giving a reason**. Scout must: (1) acknowledge within a reasonable term (FOD: do not exceed 24–48 hours), (2) stop, (3) keep an internal stop-list. The acknowledgement mail itself must **not** be promotional.

### How Scout uses this (narrow)

A first voorstel is only on the table when **all** of the following hold:

1. The target is a **rechtspersoon** (typically a vzw). Confirm on [KBO Public Search](https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html) **this session**. If the KBO hit is missing or ambiguous → **UNVERIFIED → skip**.  
2. The mailbox is **onpersoonlijk** and copied from a **fetched public page** (not a PDF of a named volunteer, not a guessed `info@`).  
3. The offer is for that organisation (club brochure site), not for a natural person.  
4. The mail contains XII.13 § 2 opt-out.  
5. The To is **not** on the already-mailed list, the HOLD list, or a stop-list.

This is still **not** “mail every Flemish `info@`”. Volume, repetition, and harvested lists are what FOD calls spam. Scout’s 10-minute gevelnaam pass is the operational control.

FOD Economie theme page (captcha from this environment on 2026-08-27; URL is official): <https://economie.fgov.be/nl/themas/online/elektronische-handel/spam>. Interpretative brochure: [*Spam in 23 vragen*, September 2019](https://economie.fgov.be/nl/file/134162/download) (FOD Economie, ondernemingsnr. 0314.595.348).

This file is **not legal advice**. It cites the statute and the FOD brochure so Scout does not improvise.

---

## 18 already mailed — no seconds

These **18** Tos received a Dutch voorstel on **2026-08-27** (Gmail SENT, operator mailbox). **Do not mail them again.** Do not “fix” missing opt-out, USDC, or host-shame with a second. Do not pitch Bancontact, a seizoenskaart, or a different kit to the same To.

| # | Gevelnaam | To (already sent — not a new mailto) | UTC |
|---|---|---|---|
| 1 | KZK Spurs | `info@kzk.be` | 16:41 |
| 2 | Koninklijke Fanfare Sint-Niklaas (Putte) | `info@fanfaresintniklaas.be` | 16:47 |
| 3 | Gio's & Tavoli | `info@giostavoli.be` | 16:53 |
| 4 | KF De Eendracht Kampenhout | `info@eendrachtkampenhout.be` | 16:55 |
| 5 | Fanfare Sint-Cecilia Booischot | `info@fanfarebooischot.be` | 18:06 |
| 6 | Genker Zwemvereniging Neptunus | `info@gzvneptunus.be` | 18:11 |
| 7 | d'Harmonie Sint-Amands | `info@dharmonie-sint-amands.be` | 18:47 |
| 8 | De Notengalm | `info@notengalm.be` | 18:47 |
| 9 | Koninklijke Harmonie Concordia Maaseik | `info@harmonieconcordia.be` | 18:47 |
| 10 | KH De Verbroedering Wommelgem | `info@khdv.be` | 18:47 |
| 11 | Kempisch Swimming Team | `info@zwemclubkst.be` | 18:47 |
| 12 | Turnkring De Kelle | `info@turnkringdekelle.be` | 18:47 |
| 13 | Brass-aux-Saxes | `info@brass-aux-saxes.be` | 18:47 |
| 14 | Fanfare Overmere | `info@fanfare-overmere.be` | 18:47 |
| 15 | Harmonie De Vriendenkring Berchem | `info@harmoniedevriendenkring.be` | 18:47 |
| 16 | Turnkring Eikels Worden Bomen | `info@turnkringewb.be` | 18:48 |
| 17 | **Turnkring Oostakker** | `info@tkoostakker.be` | 18:48 |
| 18 | Koninklijke Harmonie Sint-Martinus Halle-Kempen | `info@harmoniehalle.be` | 18:48 |

Rows 7–18 left within **about one minute**. That burst is forbidden going forward.

**Also already mailed (2026-08-26, same rule — no seconds):** Dolfijnen Middelkerke `info@dolfijnenmiddelkerke.be`; KWZC De Waterratten `info@kwzc.be` (they replied: site already being redeveloped — **stop**); Harmonie De Eendracht Oosterlo `info@harmonie-oosterlo.be`; KH De Broedermin `info@debroedermin.be`; plus kmo Tos `info@ingemeeussen.be`, `info@studio84antwerp.be`, `info@atelier-k.be`, `info@fiboro.be`, `info@carsdemeutter.be`. KWZC and Studio 84 already answered; still no second pitch.

Addresses in the tables above are **not invented**: they are the Tos on SENT messages. They are listed so Scout does not write them again. They are **not** a mail-merge file.

---

## HOLD (do not mail)

### Casa Conservas — HOLD

[casaconservas.be/geel/](https://casaconservas.be/geel/) (fetched 2026-08-27): live WordPress, Geel room at Peperstraat 21, menu, webshop, reservatie. Operator instruction: **HOLD**. Do not send a first voorstel. Do not copy the page mailbox into a send queue.

### Oostakker Bancontact — HOLD

Turnkring Oostakker is **already mailed** (row 17). [tkoostakker.be/inschrijven](https://www.tkoostakker.be/inschrijven) (fetched 2026-08-27) already tells new members they can pay with **Bancontact** (plus credit card / KBC / Belfius). A Bancontact pitch would be a **second** to the same To **and** would talk past a payment flow they already run. **HOLD.** No Bancontact mail.

---

## Later — not a Scout first voorstel

### De Peesteker — later €199 seizoenskaart candidate

[depeesteker.be](https://depeesteker.be/) (fetched 2026-08-27): houtgestookte bistro, Zandstraat 82/B, 2200 Herentals. KBO **BE 1021.176.804** is printed in the site footer (rechtspersoon: BV De Peesteker; Staatsblad oprichting cited via [busibee publication](https://busibee.be/en/1021176804-de-peesteker/publications/1cALhWhXff1cHDG3sCnGEk/25319796.pdf)).

Operator instruction: **later €199 seizoenskaart** — Builder / a later seat, **not** Scout’s first Dutch club-kit voorstel. Do not mail a clubwebsite offerte. Do not invent a seizoenskaart live URL in this file (**UNVERIFIED** that a €199 kit page exists today). No mailto is copied here.

---

## What Scout does next (without mailing)

1. Keep the 18 + 26 Aug Tos on a stop-list.  
2. Honour HOLD and the Peesteker later-bucket.  
3. If a human later wants a **new** first contact: playbook, KBO check, public `info@` on a fetched page, 10 minutes, one mail, €, opt-out.  
4. Do not compile a fresh To list in this seat until the operator asks. This PR does not contain one.

---

## PII / identity

| Field | In this file |
|---|---|
| Operator personal Gmail | **Absent** (existing from-mailbox is not reprinted). |
| Invented from-domain | **Absent**. |
| Named-person inboxes | **Not used as mail targets.** |
| Already-mailed organisational Tos | Listed so they are not mailed **again**. |
| Casa Conservas / Peesteker mailboxes | **Not copied** into a send list. |

---

## Sources

- WER art. XII.13, XII.12, XV.120, XV.121 — [Justel ELI 2013011667](https://www.ejustice.just.fgov.be/eli/wet/2013/12/15/2013011667/justel)  
- KB 4 April 2003 — [BS 28 May 2003, numac 2003011238](https://www.ejustice.just.fgov.be/cgi/article_body.pl?language=nl&caller=summary&pub_date=03-05-28&numac=2003011238)  
- FOD Economie, *Spam in 23 vragen* (Sept. 2019) — [economie.fgov.be file 134162](https://economie.fgov.be/nl/file/134162/download)  
- KBO Public Search — [kbopub.economie.fgov.be](https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html)  
- Live kit — <https://club-site-kit-treasury.surge.sh/> (fetched 2026-08-27; demo “Voorbeeldclub”, Openwater 7 september)  
- Casa Conservas Geel — <https://casaconservas.be/geel/>  
- Turnkring Oostakker inschrijven — <https://www.tkoostakker.be/inschrijven>  
- De Peesteker — <https://depeesteker.be/>  
- Gmail SENT 2026-08-26 and 2026-08-27 (already-mailed Tos; not reproduced as new mailtos)
