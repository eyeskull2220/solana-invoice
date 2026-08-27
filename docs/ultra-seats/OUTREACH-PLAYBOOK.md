# Scout outreach playbook

**Date:** 2026-08-27  
**Seat:** [SCOUT.md](SCOUT.md)  
**Status:** how to write **one** first Dutch voorstel. **Do not send mail from this file.** **Do not invent mailtos.** **Do not second** the [18 already-mailed Tos](SCOUT.md#18-already-mailed--no-seconds).

This is the opposite of a spam run. Ten minutes on **their** site. One gevelnaam. One date or break. Five to seven sentences. Live kit URL. **€** offerte. Soft opt-out (WER XII.13 § 2). Then stop.

---

## Before anything is written

Walk this list. If any box fails, **do not draft**.

- [ ] To is **not** on the 18 of 2026-08-27, **not** on the 2026-08-26 wave, **not** on a stop-list, **not** Casa Conservas HOLD, **not** Oostakker Bancontact HOLD, **not** De Peesteker (later €199 seizoenskaart).  
- [ ] Ten minutes on the live site (and only that site + the municipal/federation page that published the mailbox).  
- [ ] Mailbox is on the **fetched public page**. Copy it. If it is not there, skip. Never guess `info@`.  
- [ ] Mailbox is organisational and impersonal (`info@`, `secretariaat@`, …). **Never** personal Hotmail / Live / Outlook / MSN / Gmail / Telenet / Skynet, and never `voornaam.naam@`.  
- [ ] KBO Public Search this session: the organisation is a **rechtspersoon**. If not found → **UNVERIFIED → skip**. ([kbopub.economie.fgov.be](https://kbopub.economie.fgov.be/kbopub/zoeknummerform.html))  
- [ ] Offer is for that rechtspersoon (club brochure), not a consumer product.  
- [ ] Last send was **≥ 10 minutes** ago. Never 12 per minute. Never a paste-burst.  
- [ ] You have **one** gevelnaam fact and **one** date or break from those ten minutes. If you cannot name either, you did not look long enough — skip or keep reading.  
- [ ] You will not mention USDC, Solana, wallet, mint, or a treasury address.

Legal background (cite, do not paraphrase into a loophole): [SCOUT.md — Belgian law](SCOUT.md#belgian-law-scout-actually-has-to-follow). Statute: [WER XII.13](https://www.ejustice.just.fgov.be/eli/wet/2013/12/15/2013011667/justel). Exceptions: [KB 4 April 2003, BS 28 May 2003, numac 2003011238](https://www.ejustice.just.fgov.be/cgi/article_body.pl?language=nl&caller=summary&pub_date=03-05-28&numac=2003011238). Opt-out always: FOD Economie, [*Spam in 23 vragen*](https://economie.fgov.be/nl/file/134162/download), vragen 13–14.

---

## The ten minutes

Stay on **their** pages. You are looking for two things only:

1. **One gevelnaam** — the name they put on the door / masthead / “over ons”, not a nickname you invent.  
2. **One date or break** — a concert, inschrijvingsdag, seizoensstart, repetitie, kermis, kamp, “lessen volzet tot …”, “open repetitie op …”. Written on **their** site this session.

Do **not** harvest a second fact to pad the mail. Do **not** audit their host, CMS, SSL, or “dead Drupal”. Host-shame is forbidden and it is not research.

If the site is a living WordPress/Twizzit rebuild and the only “break” you can find is “our site is fine”, they are probably not a kit buyer. Skip. Do not invent a wound.

---

## From-header

| Field | Value |
|---|---|
| **From-name** | `Sasha · SovereignForge (Geel)` |
| **From-mailbox** | The operator mailbox already used for first voorstellen. **Do not invent a new domain this week.** Do not print that mailbox in public repo files. |
| **SovereignForge KBO** | **UNVERIFIED** as a Belgian registered firm. Display name only. |

WER XII.13 § 3: do not hide origin. The from-name is the origin the bestuur sees.

---

## Subject — never product-first

The subject is **gevelnaam + the date/break**. It is not the product.

| Do | Do not |
|---|---|
| `Kermisconcert 27 september — Harmonie Sint-Martinus` | `Voorstel clubwebsite voor Harmonie Sint-Martinus Halle-Kempen` |
| `Open repetitie 4 september — De Eendracht Kampenhout` | `Voorstel lid-inschrijving voor …` |
| `Seizoen 2026–2027 — [gevelnaam]` | `Nieuwe clubwebsite KWZC — Drupal 7 vervangen` |

The last “do not” is both product-first **and** host-shame. Do not send that shape again (and do not send KWZC a second of any shape).

---

## Body — 5 to 7 sentences, u, euro, kit, opt-out

**Language:** **u** / **uw** on first contact. Not *je*. *Jullie* is still informal-plural; use **u** for the bestuur.

**Length:** 5–7 sentences. No attachment. No BCC list.

**Must contain, in this order:**

1. `Beste bestuur van [gevelnaam],`  
2. The **one** date/break, in one sentence, as it stands on **their** site.  
3. One sentence on what a readable clubpagina would hold around that date (agenda / contact / lid worden) — **without** insulting the current host.  
4. The live kit, as a demo of a **fictieve** club: <https://club-site-kit-treasury.surge.sh/>  
5. `Dit is een voorstel, geen factuur. Prijs: €900 (eenmalig, offerte).` — euro only.  
6. Soft opt-out (required).  
7. Sign-off: `Sasha · SovereignForge (Geel)`

### Soft opt-out (WER XII.13 § 2 + KB 2003 art. 2)

FOD Economie example shape (*Spam in 23 vragen*, vraag 14): tell them they may object, and give an **electronic** way.

Use this line, unshortened:

> Als u in de toekomst geen voorstellen van ons meer wilt ontvangen, antwoord dan **stop** op deze mail. Dat is kosteloos en zonder reden. Wij zetten u dan op onze stoplijst.

That **is** the suitable electronic means: reply to the same thread. Do not hide it under a tracking link. Do not require a phone call.

If they send **stop**: acknowledge within 24–48 hours (**non-promotional**), stop, update the stop-list. KB 2003 art. 2.

“Antwoord ja of nee” is **not** opt-out. Several 2026-08-27 mails used that and omitted XII.13 § 2. **Do not second those Tos to patch it.**

### Skeleton (placeholders only — not a mailto)

```
Subject: [DATUM OF BREUK] — [GEVELNAAM]

Beste bestuur van [GEVELNAAM],

Op uw site staat [één datum of breuk, letterlijk genoeg om herkenbaar te zijn, zonder de host te beoordelen].

Rond die datum is een eigen clubpagina met agenda, lid worden en contact eenvoudiger bij te houden dan losse berichten.

Wij hebben een Nederlandstalige clubkit klaar (home, over, agenda, lid worden, contact). Demo van een fictieve club, geen echte inbox: https://club-site-kit-treasury.surge.sh/

Dit is een voorstel, geen factuur. Prijs: €900 (eenmalig, offerte). Als het past, kunt u op deze mail antwoorden.

Als u in de toekomst geen voorstellen van ons meer wilt ontvangen, antwoord dan stop op deze mail. Dat is kosteloos en zonder reden. Wij zetten u dan op onze stoplijst.

Met vriendelijke groeten,
Sasha · SovereignForge (Geel)
```

Fill `[GEVELNAAM]` and `[DATUM OF BREUK]` from the ten minutes. **Do not** paste a To into this file. **Do not** send this skeleton to the 18.

€900 matches the euro offerte already used for the club kit (live demo above). Do not put 900 USDC in the body. A different product (€349 lid-inschrijving, €199 seizoenskaart) is **not** this first-mail kit. De Peesteker’s €199 seizoenskaart stays **later**.

---

## Never

| Rule | What it looks like when broken (already sent — do not repeat, do not “correct” with a second) |
|---|---|
| Never product-first subject | `Voorstel clubwebsite voor …`, `Voorstel lid-inschrijving voor …` |
| Never host-shame | KWZC: “draait nog op Drupal 7. Dat CMS krijgt geen updates”. Gio's & Tavoli: “De menukaart opent niet meer goed”. De Notengalm: “Jullie site is nu een One.com-pagina.” Name the **date**, not the stack. |
| Never 12 / minute | 2026-08-27 **18:47:13–18:48:14 UTC**: twelve Tos in about one minute. Hard floor now: **10 minutes between sends**. |
| Never personal Hotmail | Skip listing-page Hotmail / Live / Outlook / Gmail / Telenet / Skynet. Skip named `voornaam.naam@`. |
| Never USDC / crypto / wallet in the mail | Booischot 18:06 UTC quoted **900 USDC** and a Solana pay-to. Forbidden in every future first voorstel. |
| Never a second to those Tos | Including Oostakker **Bancontact** (they already take Bancontact on [inschrijven](https://www.tkoostakker.be/inschrijven); To already mailed). |
| Never Casa Conservas | HOLD. Live Geel site: <https://casaconservas.be/geel/>. |
| Never De Peesteker as a club-kit first mail | Later €199 seizoenskaart candidate. Site: <https://depeesteker.be/>. No mailto copied here. |

---

## After a send (human only — not this PR)

1. Log To, time, subject, gevelnaam, date/break, KBO number checked.  
2. Wait **≥ 10 minutes** before any other first voorstel.  
3. If **stop**: acknowledge, no pitch, update stop-list.  
4. If **yes**: hand to Builder. Scout does not code and does not send a second “just checking”.  
5. If silence: **stop**. No nudge. FOD vraag 8: do not keep asking.

---

## This PR does not send

No Gmail draft. No mailto: link for a new club. No proposed next-five list. Scout’s send list for this seat is **empty** until the operator names a new, unmailed rechtspersoon that survives the checklist.
