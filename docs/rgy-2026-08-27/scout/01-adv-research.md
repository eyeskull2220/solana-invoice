# 01 — Adversarial research (Scout first-mails)

**Seat:** Scout / RGY 01 (adv-research)
**Lens:** adversarial first, then RED / YELLOW / GREEN
**Date:** 2026-08-27
**Corpus:** 18 Dutch first-voorstellen, Gmail SENT, same UTC day. Inbox search for replies on those threads: **zero**.
**This file does not send mail.** It does not draft seconds. It does not invent mailtos. Face of any later voorstel stays **euro only** — no USDC, Solana, wallet, mint, or treasury address in outreach.

---

## Adversarial first

Scout did not research-then-mail. Scout paste-burst a stencil.

Eighteen Tos got a first Dutch voorstel on 2026-08-27. By 19:00 UTC none had answered. That is not “too early to judge.” It is the shape of the mail: a product on the subject line, a volunteer CMS named as a defect, no statutory opt-out, and twelve of the eighteen leaving the same consumer mailbox inside sixty-one seconds.

Call the two clocks what they are.

**Wave A (16:41–18:11 UTC, six Tos).** Older stencil. Opens “Wij zijn een klein team in Geel.” Quotes **USDC** and a Solana pay-to. Demo URLs go through Gmail’s `google.com/url` wrapper. Subjects are `Voorstel nieuwe clubwebsite …` / `Voorstel lid-inschrijving …` / `Voorstel nieuwe menukaart …` / `Voorstel sponsorblad …`. One of them tells Fanfare Sint-Niklaas their site “draait nog op Drupal.” One tells Gio's & Tavoli the menukaart “opent niet meer goed.” Belgian club secretarissen do not settle in USDC. Putting a mint-shaped string in a vzw inbox is not a euro face. It is a crypto pitch wearing Dutch.

**Wave B (18:47:13–18:48:14 UTC, twelve Tos).** Euro sticker on the same machine. Same five-block body:

1. `Beste bestuur van [naam],`
2. One scraped line (date, “info@”, “One.com”, “volzet”).
3. `Wij hebben een kant-en-klare Nederlandstalige [SKU] … Dit is een voorstel, geen factuur.`
4. `Prijs: €N (eenmalig, offerte).`
5. `Als dat past, antwoorden jullie ja of nee op deze mail.`

That last line is a close, not an opt-out. WER XII.13 § 2 still applies when the To is an impersonal `info@` of a rechtspersoon. FOD Economie, *Spam in 23 vragen* (Sept. 2019), vragen 13–14: every publicitaire mail must name the right to object and give an electronic means. “Ja of nee” is not that means. None of the eighteen carry the stop-line.

The twelve Wave B subjects are product-first without exception: `Voorstel lid-inschrijving voor …` / `Voorstel clubwebsite voor …` / `Voorstel sponsorblad voor …`. The one date that could have been the subject (Halle-Kempen kermisconcert 27 september, De Kelle volzet tot juni, Kampenhout open repetitie 4 september) is buried in sentence two so the inbox row still reads as vendor mail.

Host-shame is not a research finding. De Notengalm is told “Jullie site is nu een One.com-pagina.” Sint-Niklaas is told Drupal. The 26 August KWZC mail already ran the Drupal-7 version of this attack (“Dat CMS krijgt geen updates meer”) and got a polite no: the site was already being redeveloped. Naming the stack is how you teach a volunteer treasurer that you looked at the generator, not at the concert.

The Bancontact HOLD was written before Wave B and then ignored. Turnkring Oostakker’s own inschrijven page (fetched 2026-08-27) already takes **Bancontact**, credit card, KBC, or Belfius, and says membership is only final after that payment. `info@` on that page is waitlist, sociaal tarief, and questions. The 18:48:01 mail to `info@tkoostakker.be` claims the opposite: “Op jullie inschrijfpagina staat info@ voor wie wil starten. Die aanmeldingen komen nu als losse mail binnen.” That is a false brief. Pitching €349 lid-inschrijving to a club that already runs paid Bancontact enrollment is the HOLD miss: research said HOLD, the stencil said send.

Twelve mails in sixty-one seconds from one Gmail is a burst fingerprint. It is also how two Gymfed boards that talk to each other see the same paragraph twice. Zero replies is the campaign working as designed: spam-shaped, legally thin, product-first, and in six cases still asking a Flemish vzw to pay USDC.

Do not second any of the eighteen to “fix” this. A second is another publicitaire mail to a To that already got one, still without a working stop-history, and FOD vraag 8 is exactly about not asking again. Silence is the answer. Design the next first-mail. Do not send it from this file.

---

## Scorecard

| # | Attack | Score | Design-out (do not send from here) |
|---|---|---|---|
| S1 | Stencil wave | **RED** | One gevelnaam + one date/break from ten minutes on *their* site. No five-block paste. |
| S2 | Product-first subjects | **RED** | Subject is `[datum/breuk] — [gevelnaam]`. Never `Voorstel [SKU] voor …`. |
| S3 | Missing opt-out | **RED** | WER XII.13 § 2 stop-line on every first voorstel. “Ja of nee” is not opt-out. |
| S4 | Host-shame | **RED** | Name the concert / volzet / repetitie. Never Drupal, One.com, “site opent niet”, “CMS is dood”. |
| S5 | 12-in-60s | **RED** | Floor **10 minutes** between sends. Never a paste-burst. |
| S6 | Oostakker Bancontact HOLD miss | **RED** | HOLD = do not pitch geld-in / lid-inschrijving where Bancontact is already live. No second to that To. |

**Overall: RED.** 18 sent, 0 replies. Do not second. Do not mail from this file. EUR-only on any later first-contact face.

Adjacent (not in the named six, still scored):

| # | Attack | Score |
|---|---|---|
| A1 | USDC / Solana pay-to in Wave A bodies | **RED** |
| A2 | Impersonal organisational `info@` as To | **GREEN** |
| A3 | “Voorstel, geen factuur” (OFFERTE, not FACTUUR) | **GREEN** |
| A4 | No seconds sent yet to the 18 | **GREEN** (keep it) |
| A5 | Informal *jullie* / from-name only “Sasha” | **YELLOW** |
| A6 | Real dates used as *body* hooks, wasted on product subjects | **YELLOW** |

---

## S1 — Stencil wave — RED

Wave B is one template with a find-replace on the gevelnaam and the SKU noun.

Evidence, same UTC minute, same close, same missing opt-out:

- Fanfare Overmere 18:47:34 — “Die aanmeldingen komen nu als losse mail binnen.” → kant-en-klare lid-inschrijving → €349 → ja of nee.
- Turnkring Eikels Worden Bomen 18:48:00 — “Wie wil starten, mailt nu los naar info@.” → same lid-inschrijving paragraph → €349 → ja of nee.
- Turnkring Oostakker 18:48:01 — same “losse mail” claim (false; see S6) → same paragraph → €349 → ja of nee.
- Harmonie De Vriendenkring Berchem 18:47:58 — sponsors/ereleden → kant-en-klaar sponsorblad → €199 → ja of nee.
- De Notengalm 18:47:15 — One.com line → kant-en-klare clubwebsite → €900 → ja of nee.
- Halle-Kempen 18:48:14 — kermisconcert 27 september → same clubwebsite paragraph → €900 → ja of nee.

The SKU nouns rotate (`lid-inschrijving` / `clubwebsite` / `sponsorblad`). The machine does not. Wave A is the same machine with a Geel-team opener and a USDC footer.

A stencil wave is visible to anyone who sits on two boards, forwards to a federatie-secretariaat, or compares inboxes at a Gymfed / VLAMO table. It is also how Gmail classifies bulk: identical MIME length (~2.1–2.3 KB on Wave B), identical last two paragraphs, twelve hops from one From in one minute.

**Notes.** Personalisation that is only the club’s own name plus one scraped clause is not research. EWB’s “turnen je laat stralen” is homepage garnish, not a job. Overmere’s “zin om mee te spelen” is a real lid-in hook wasted on a paste.

**Design-out.** Ten minutes on the live site. One gevelnaam. One date or break written on *that* site this session. Five to seven sentences in **u**. If you cannot name the date/break, skip — do not fall back to the stencil. Do not mail-merge the 18. Do not “A/B” the stencil on new Tos in a burst.

---

## S2 — Product-first subjects — RED

All **18** inbox rows lead with the SKU.

| Wave | Subject shape | Count |
|---|---|---|
| A+B | `Voorstel … clubwebsite …` | 6 |
| A+B | `Voorstel … lid-inschrijving …` | 8 |
| A+B | `Voorstel … sponsorblad …` | 2 |
| A | `Voorstel nieuwe menukaart …` | 1 |
| A | `Voorstel lid-inschrijving De Eendracht Kampenhout` (SKU still first) | 1 |

A secretaris scanning mail on a phone sees vendor. They do not see “kermisconcert 27 september”, “open repetitie 4 september”, or “lessen volzet tot juni 2026”. Those facts exist in the bodies of Halle-Kempen, Kampenhout, and De Kelle and were demoted under `Voorstel`.

KWZC (26 Aug, not in the 18) already showed the other failure mode of a product subject: `Nieuwe clubwebsite KWZC — Drupal 7 vervangen` is both product-first and host-shame. They replied that a rebuild was already underway.

**Notes.** “Voorstel” is honest (not a fake invoice subject). Honesty about it being a pitch does not require the SKU in the subject. The playbook subject rule is gevelnaam + date/break.

**Design-out.** Subject = `[datum of breuk] — [gevelnaam]`. Examples that were available on 27 Aug and were **not** used: `Kermisconcert 27 september — Harmonie Sint-Martinus`; `Open repetitie 4 september — De Eendracht Kampenhout`; `Lessen volzet tot juni — Turnkring De Kelle`. Do not send those now. Those Tos already have a first mail. The design-out is for **unmailed** rechtspersonen only.

---

## S3 — Missing opt-out — RED

Statute: **WER art. XII.13 § 2** (Wet 15 Dec 2013, Justel [ELI 2013011667](https://www.ejustice.just.fgov.be/eli/wet/2013/12/15/2013011667/justel)). Every advertising electronic mail must (1) state the right to object to **future** advertising, clearly, and (2) point to a **suitable electronic means**. This holds even when § 1 opt-in is displaced by the rechtspersoon exception in **KB 4 April 2003** art. 1, 2° ([BS 28 May 2003, numac 2003011238](https://www.ejustice.just.fgov.be/cgi/article_body.pl?language=nl&caller=summary&pub_date=03-05-28&numac=2003011238)). FOD Economie, *Spam in 23 vragen*, vragen 13–14, same reading. KB 2003 art. 2: objection is free and without reason; acknowledge, stop, keep a stop-list.

**Count:** 18 / 18 Wave A+B bodies have no stop-line, no “antwoord stop”, no unsubscribe URL, no “u mag bezwaar maken”. Wave B’s `Als dat past, antwoorden jullie ja of nee` is a sales close. A “nee” is not logged as XII.13 objection unless Scout treats every nee as STOP and says so in the mail. It does not.

Sanctions sit at WER **XV.120** (niveau 3) for XII.13 breach. This file is not legal advice. It is the reason the next design does not ship without § 2.

**Notes.** Tos were impersonal `info@` of clubs (A2 GREEN). That may satisfy the KB 2003 *opt-in* carve-out. It does **not** waive opt-out. Do not “patch” the 18 with a second mail whose only new sentence is the stop-line. That second is more reclame.

**Design-out.** Unshortened line on every future first voorstel:

> Als u in de toekomst geen voorstellen van ons meer wilt ontvangen, antwoord dan **stop** op deze mail. Dat is kosteloos en zonder reden. Wij zetten u dan op onze stoplijst.

Reply-to-thread is the electronic means. No tracking link. If **stop**: non-promotional ack within 24–48 hours, stop, list. Do not send that line to the 18 now.

---

## S4 — Host-shame — RED

Naming the volunteer’s host or CMS as the wound.

| To (already mailed — not a new mailto) | UTC | Shame line |
|---|---|---|
| `info@notengalm.be` | 18:47:15 | “Jullie site is nu een One.com-pagina.” |
| `info@fanfaresintniklaas.be` | 16:47:23 | “Jullie site draait nog op Drupal.” |
| `info@giostavoli.be` | 16:53:37 | “De menukaart op jullie site opent niet meer goed.” |
| `info@kwzc.be` (26 Aug, outside the 18) | 03:01 | Drupal 7 “krijgt geen updates meer” → they already had a rebuild in flight |

The 26 Aug KWZC reply is the empirical cost: host-shame invites “we already fixed that, thanks.” It also tells the treasurer you ranked their stack, not their kermis or lid-in.

Research docs that treated One.com / Drupal / “thin volunteer homepage” as a *buying signal* leaked into the mail as an insult. Buying-signal research stays in the repo. The mail names the date or the break.

**Notes.** Not every one of the 18 contains host-shame. Enough do that it is a pattern, not an accident. Wave B still shipped Notengalm’s One.com line after Wave A had already run Drupal and “opent niet”.

**Design-out.** Forbidden strings in voorstellen: Drupal, Joomla, One.com, Webhero, Google Sites, Hostnet, “CMS”, “generator”, “opent niet”, “krijgt geen updates”, “dode site”. Allowed: the concert date, volzet tot, open repetitie, inschrijvingsdag — copied from their page this session. KWZC gets nothing further.

---

## S5 — 12-in-60s — RED

Wave B clock (Gmail `internalDate`, UTC):

| # | To | Time |
|---|---|---|
| 7 | `info@dharmonie-sint-amands.be` | 18:47:13 |
| 8 | `info@notengalm.be` | 18:47:15 |
| 9 | `info@harmonieconcordia.be` | 18:47:18 |
| 10 | `info@khdv.be` | 18:47:20 |
| 11 | `info@zwemclubkst.be` | 18:47:27 |
| 12 | `info@turnkringdekelle.be` | 18:47:30 |
| 13 | `info@brass-aux-saxes.be` | 18:47:32 |
| 14 | `info@fanfare-overmere.be` | 18:47:34 |
| 15 | `info@harmoniedevriendenkring.be` | 18:47:58 |
| 16 | `info@turnkringewb.be` | 18:48:00 |
| 17 | `info@tkoostakker.be` | 18:48:01 |
| 18 | `info@harmoniehalle.be` | 18:48:14 |

**12 Tos, 18:47:13 → 18:48:14 = 61 seconds.** Several gaps are 1–3 seconds. That is not “one researched mail.” That is a paste-burst from a consumer Gmail. Deliverability, domain reputation, and the legal “volume / repetition” picture FOD uses for spam all move the wrong way together.

Wave A was slower (16:41, 16:47, 16:53, 16:55, 18:06, 18:11) and still a stencil. The crime to design out is the minute-burst, not the fact of six mails in a day.

**Notes.** Operator rule already written into the SCOUT seat: minimum **10 minutes** between sends, matching the ten-minute site pass. The burst proves the pass did not happen per To.

**Design-out.** Hard floor: last send ≥ 10 minutes ago, else do not draft. Max cadence is the research clock, not the SMTP clock. Never 12 per minute. Never a queue “send these twelve now.” This file contains **no** next-twelve.

---

## S6 — Oostakker Bancontact HOLD miss — RED

**HOLD (research, opened 2026-08-27):** [tkoostakker.be/inschrijven](https://www.tkoostakker.be/inschrijven)

> Bij inschrijving dient u onmiddellijk het lidgeld te betalen. Dit is mogelijk via **bankcontact**, kredietkaart, KBC of Belfius. U ontvangt een bevestigingsmail van inschrijving na betaling. Na de betaling ben je officieel lid en dus ook verzekerd.

`info@` on that page is for: sociaal tarief, volzet/wachtlijst, “nog vragen”. Lid in + geld in is already a pay-first Bancontact flow. Buyer research (PR #115) marked this row **HOLD**. SCOUT seat (PR #117) repeats the HOLD and forbids a Bancontact / lid-inschrijving pitch to this To.

**What went out, 18:48:01 UTC, to `info@tkoostakker.be`:**

> Op jullie inschrijfpagina staat info@ voor wie wil starten. Die aanmeldingen komen nu als losse mail binnen.
>
> Wij hebben een kant-en-klare Nederlandstalige lid-inschrijving … Prijs: €349 …

That paragraph is false on the opened page. It is also a **second kind of miss**: even a true waitlist-form pitch would still be a first mail to a To that research said do not geld-in. Scout sent the SKU that HOLD exists to block.

**Notes.** Adjacent Oostakker HOLD (Lunch Garden Bancontact on resto.be) was not mailed — good. Casa Conservas Bancontact webshop was not mailed — good. The miss is specifically Turnkring Oostakker row 17 of the 18. Do not “correct” with a Bancontact-aware second. Do not pitch seizoenskaart, webshop, or waitlist to the same To.

**Design-out.** Before any lid-in / geld-in SKU: open inschrijven / lid worden / webshop this session. If Bancontact / KBC / Belfius / Payconiq / Twizzit pay / Mollie is already named, **HOLD**. Skip. The 18 including Oostakker stay on the already-mailed list. No seconds.

---

## Adjacent scores

### A1 — USDC in Wave A — RED

Six Tos already have 199 / 349 / 900 **USDC** and the treasury pay-to in the body (KZK Spurs, Fanfare Sint-Niklaas Putte, Gio's & Tavoli, Kampenhout, Booischot, GZVN). Wave B switched to €349 / €199 / €900 without USDC. The switch does not unsend Wave A. EUR-only face means: never again in outreach. Internal settlement may stay USDC; it stays **off the mail**. Do not second Wave A with a euro restatement.

### A2 — Impersonal `info@` — GREEN

All 18 Tos are organisational `info@` copied onto SENT messages, not harvested Hotmail / `voornaam.naam@`. That is the KB 2003 art. 1, 2° mailbox class. Keep it. Still not a licence to burst.

### A3 — OFFERTE, not FACTUUR — GREEN

Bodies say “Dit is een voorstel, geen factuur” / “eenmalig, offerte.” No FACTUUR stamp in the 18.

### A4 — No seconds yet — GREEN

Inbox check 2026-08-27: no replies on the 18; Scout has not nudged. **Keep this GREEN.** Operator rule: no seconds, including “just adding opt-out.”

### A5 — *jullie* / from-name — YELLOW

Wave B uses *jullie* (informal plural) to a bestuur. Playbook wants **u** / **uw** on first contact. From-name on the wire is “Sasha”, not `Sasha · SovereignForge (Geel)`. WER XII.13 § 3 is about not hiding origin; a stable from-name is the operational control. YELLOW, not RED: identity was not spoofed as the club.

### A6 — Wasted real hooks — YELLOW

De Kelle volzet, Halle-Kempen kermisconcert, Kampenhout 4 september, Sint-Amands LUMEN / 250 jaar — those are date/break facts. They were used as sentence two under a `Voorstel` subject. The research muscle exists. The stencil sat on it. Do not recycle those hooks as seconds.

---

## The 18 (already mailed — do not write again)

| # | Gevelnaam | To | UTC | Face in body |
|---|---|---|---|---|
| 1 | KZK Spurs | `info@kzk.be` | 16:41 | 900 USDC |
| 2 | Koninklijke Fanfare Sint-Niklaas (Putte) | `info@fanfaresintniklaas.be` | 16:47 | 900 USDC + Drupal |
| 3 | Gio's & Tavoli | `info@giostavoli.be` | 16:53 | 199 USDC + “opent niet” |
| 4 | KF De Eendracht Kampenhout | `info@eendrachtkampenhout.be` | 16:55 | 349 USDC |
| 5 | Fanfare Sint-Cecilia Booischot | `info@fanfarebooischot.be` | 18:06 | 900 USDC |
| 6 | Genker Zwemvereniging Neptunus | `info@gzvneptunus.be` | 18:11 | 199 USDC |
| 7 | d'Harmonie Sint-Amands | `info@dharmonie-sint-amands.be` | 18:47 | €349 |
| 8 | De Notengalm | `info@notengalm.be` | 18:47 | €900 + One.com |
| 9 | Koninklijke Harmonie Concordia Maaseik | `info@harmonieconcordia.be` | 18:47 | € (lid-inschrijving stencil) |
| 10 | KH De Verbroedering Wommelgem | `info@khdv.be` | 18:47 | € (lid-inschrijving stencil) |
| 11 | Kempisch Swimming Team | `info@zwemclubkst.be` | 18:47 | € (lid-inschrijving stencil) |
| 12 | Turnkring De Kelle | `info@turnkringdekelle.be` | 18:47 | €349 |
| 13 | Brass-aux-Saxes | `info@brass-aux-saxes.be` | 18:47 | € (clubwebsite stencil) |
| 14 | Fanfare Overmere | `info@fanfare-overmere.be` | 18:47 | €349 |
| 15 | Harmonie De Vriendenkring Berchem | `info@harmoniedevriendenkring.be` | 18:47 | €199 |
| 16 | Turnkring Eikels Worden Bomen | `info@turnkringewb.be` | 18:48 | €349 |
| 17 | **Turnkring Oostakker** | `info@tkoostakker.be` | 18:48 | €349 — Bancontact HOLD miss |
| 18 | Koninklijke Harmonie Sint-Martinus Halle-Kempen | `info@harmoniehalle.be` | 18:48 | €900 |

Addresses above are SENT Tos, listed so they are not mailed again. They are **not** a mail-merge file. Operator from-mailbox is **not** reprinted here.

Also already mailed 2026-08-26 (same no-seconds rule, not in the 18): Dolfijnen Middelkerke, KWZC De Waterratten (replied: rebuild in flight — **stop**), Harmonie Oosterlo, KH De Broedermin, plus kmo Tos Inge Meeussen, Studio 84 Antwerp (auto-ack), Atelier-K, Fiboro, Cars De Meutter.

---

## NOTES

1. **Report-only.** No Gmail draft, no send, no second, no new To list.
2. **Reply zero** is measured on 2026-08-27 the same evening as Wave B. Clubs do not sit on info@ at 20:48 Belgian time in August the way a vendor does. That caveat does not rescue stencil + no opt-out + burst + USDC + false Oostakker brief. It only says: do not send a “checking in” mail tomorrow to harvest a late reply.
3. **EUR-only face.** Wave B price tokens (€199 / €349 / €900) are the correct *unit*. Wave A USDC is not. Outreach copy never names USDC, Solana, Phantom, mint, or a treasury address.
4. **HOLD list stays closed:** Turnkring Oostakker Bancontact; Casa Conservas webshop Bancontact; Lunch Garden Oostakker Bancontact; KLJ Twizzit-mandate; KWZC (already answered). De Peesteker stays a **later** €199 candidate, not a Scout first club-kit voorstel, and is not mailed from this file.
5. **Concurrent SCOUT playbook (PR #117)** already encodes S1–S6 as never-rules. This RGY file is the evidence pack those rules rest on. It does not replace the playbook and it does not authorise a send queue.
6. Inbox search used Gmail `in:inbox` against the 27 Aug `Voorstel` / lid-inschrijving / clubwebsite / menukaart subjects: empty. SENT snippets for the 18 show no `Re:` from the clubs.

---

## Design-outs (next first-mail, not these Tos)

A later **first** voorstel to a **new**, unmailed rechtspersoon is still RED to implement until it satisfies all of:

1. Subject = date/break — gevelnaam (S2).
2. Body 5–7 sentences in **u**, one gevelnaam fact, one date/break, no host-shame (S1, S4, A5).
3. WER XII.13 § 2 stop-line verbatim (S3).
4. € offerte only. No USDC / chain / wallet (A1).
5. ≥ 10 minutes since last send; no burst (S5).
6. KBO rechtspersoon this session; impersonal mailbox copied from a fetched public page (A2).
7. Inschrijven/pay page opened this session; Bancontact-already-live → HOLD (S6).
8. To not in the 18, not in the 26 Aug set, not on a stop-list, not Casa Conservas, not Oostakker.

Until then Scout research stays **RED**. This PR does not send.

---

End. No seconds. No mail. EUR-only face.
