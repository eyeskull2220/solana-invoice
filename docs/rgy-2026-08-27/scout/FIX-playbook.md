# FIX playbook — Scout send template

**Seat:** FIX (Scout)  
**Date of this page:** 2026-08-27  
**Status:** this file is the **only** send template. **No mail was sent from this PR.**  
**Operator:** Sasha · SovereignForge (Geel). The operator is not the freelancer. The team delivers.

This page designs out the Scout reds that made prior Gmail bursts fail review. It does not open a send queue. It does not authorise a blast. A later human may copy **this** template once, for **one** organisational mailbox, after a sourced hook exists. Nothing else is a send template.

---

## 0. Hard locks

| Lock | Meaning |
| --- | --- |
| **Do not send from this PR** | No Gmail send, no draft-and-send, no mailto click-through that leaves this repo. |
| **This file is the only send template** | Do not invent a second body. Do not reuse a prior blast. Do not paste a USDC catalog mail. |
| **u, Beste bestuur** | Formal Dutch **u**. Greeting is **Beste bestuur,** — not *Beste,* not *Hallo,* not *je/jij/jouw.* |
| **Hook = their date or their break** | First sentence and subject name a **date** or a **site-break** copied from a page opened for that club. No hook → no mail (and this PR still does not send). |
| **€ OFFERTE** | Price in euro. Stamp **OFFERTE**. Never FACTUUR. Never USDC, Solana, mint, Phantom, or a treasury string. |
| **Live kit URL** | The body must contain `https://club-site-kit-treasury.surge.sh/` — the live Dutch club-site kit (opened 2026-08-27). |
| **Mandatory opt-out, verbatim** | `Geen interesse? Eén antwoord volstaat — dan mailen wij u niet meer.` |
| **From-name** | Gmail display name **Sasha · SovereignForge (Geel)** — not `Sasha` alone. |
| **No Hotmail To** | Never To/Cc/Bcc `hotmail.com`, `live.com`, `outlook.com`, `msn.com`, `passport.com`. |
| **No seconds** | Cadence and copy never use seconds. No “in 30 seconds”, no delay of *n* seconds, no burst measured in seconds. |
| **No host-shame** | Do not mock Wix, Google Sites, Bootply, HTTP, “jaren 90”, or the current webmaster. State the break as a fact. |
| **No stencil** | The hook line is unique to that club. Merge fields for club name alone are not a hook. |

CEO lock still sits above this page: first real send waits for a human pick of **one** mailbox and **one** EUR OFFERTE. This file does not grant that yes.

---

## 1. Scout reds → designed out

| Scout red | What failed | Design-out in this template |
| --- | --- | --- |
| **Product-first subject** | Subjects led with the SKU (“Club-site kit”, “OFFERTE website”, “SovereignForge”). | Subject is the **date** or the **break**. The kit name does not appear in the subject. |
| **Stencil** | Same three paragraphs, only `{{club}}` swapped. Reads as a merge blast. | Opening sentence must quote **their** date or **their** break string from an opened page. If two mails could swap clubs and still read true, it is a stencil — do not send. |
| **Missing opt-out** | No stop line. Belgian B2B still needs an honest out. | Last body line before the signature is the verbatim opt-out. No paraphrase. |
| **Gmail from-name Sasha only** | Inbox shows a first name with no place or firm. Looks like a private Gmail. | Display name **Sasha · SovereignForge (Geel)**. Check the Gmail “Send mail as” field before any later human send. |
| **12/minute** | Same-hour burst; consumer Gmail at a bot rate. | Floor: **at most one outbound mail per ten minutes**. Default: **one mail, then stop**. Never a 12/minute window. Never a same-hour stack. |
| **Host-shame** | “Uw Wix is belabberd / uw site is uit 1998.” | Name the break without insulting the host or the secretaris. |
| **No demo URL** | Pitch with no clickable live kit. | Always include `https://club-site-kit-treasury.surge.sh/`. Do not substitute a USDC catalog, a Surge tool at 9/49, or `treasury-tools.surge.sh`. |

---

## 2. Envelope (before the body)

### From

| Field | Value |
| --- | --- |
| Display name | `Sasha · SovereignForge (Geel)` |
| Identity | SovereignForge, Geel. Not “freelance developer.” Not Eyeskull2220 on a job board. |

If Gmail still shows **Sasha** without the firm and the town, **do not send**.

### To

Allowed **only** if all of these hold:

1. Copied from a **public** page opened for that club (gids, club contact, gemeente).
2. Organisational role inbox: `info@`, `bestuur@`, `secretariaat@`, `secretaris@` on a **club/org domain**.
3. Not a named-person inbox (`jan@`, `voornaam.naam@`).
4. **No Hotmail To** — and the same ban for Live / Outlook / MSN.
5. Also skip personal ISP and free mail even when they are not Hotmail: `gmail.com`, `googlemail.com`, `telenet.be`, `skynet.be`, `scarlet.be`, `yahoo.com`. Those are not this template’s To.

One To. No Cc blast. No Bcc list.

### Cadence (no seconds)

| Rule | Value |
| --- | --- |
| Default | One mail. Then stop. |
| Absolute floor if a human later sends more than one | At most **one outbound per ten minutes**. Never 12 per minute. Never a delay written in seconds. |
| Same-hour burst | Forbidden. |
| This PR | **Zero** outbound. |

### Price (EUR OFFERTE)

Pick **one** band from the opened-page need. Write it as euro. Stamp OFFERTE.

| Band | When the opened page shows |
| --- | --- |
| **€199** | One job: eetdag / spaghetti / mosselfestijn / QR for geld-in. Site already exists. |
| **€349** | Public site exists; lid in + geld in is still “mail us / walk in”; Bancontact/Twizzit pay is **not** already live. |
| **€900** | Site is placeholder, dead, dated static HTML, or “binnenkort terug online.” |

Do not print USDC. Do not print a Solana address. Do not mix two bands in one mail.

---

## 3. The only send template

Fill the **hook slots** from an opened page. Do not leave angle brackets in a real send. This PR does not send.

**Slots**

| Slot | Must be |
| --- | --- |
| `{HOOK_SUBJECT}` | Their date **or** their break. Not a product name. |
| `{HOOK_OPEN}` | One sentence that names that same date or break, in **u**-form. |
| `{NEED}` | Lid in / geld in / repetitie / sponsor — the secretaris job, not “een website.” |
| `{EUR}` | `199` or `349` or `900` |
| `{OFFERTE_LINE}` | One line what they get for that euro amount. |

### Subject

```
{HOOK_SUBJECT}
```

**Forbidden subjects (product-first):** `Club-site kit`, `Websitepakket €900`, `OFFERTE SovereignForge`, `Nieuwe clubsite`, `Gratis demo`.

**Allowed shape:** `Eetdagen 10 en 11 oktober` · `‘Binnenkort terug online’ op fanfaremolsluis.be` · `Vrijdagrepetitie in Oosterlo — lid worden zonder formulier`

### Body (plain text)

```
Beste bestuur,

{HOOK_OPEN}

{NEED} hoeft geen extra app en geen nieuw lidmaatschapssysteem. Wij maken een OFFERTE in euro voor dat ene stuk werk.

OFFERTE: €{EUR} — {OFFERTE_LINE}

Een live clubpagina (Nederlands, geen account):
https://club-site-kit-treasury.surge.sh/

Als dit nuttig is, antwoordt u op deze mail. Dan zetten wij de OFFERTE op uw naam. KBO vullen wij niet in tot u die zelf doorgeeft.

Geen interesse? Eén antwoord volstaat — dan mailen wij u niet meer.

Met vriendelijke groeten,
Sasha · SovereignForge (Geel)
```

**Signature name** matches the From display name. Do not sign `Sasha` alone. Do not sign a GitHub handle.

**Opt-out line** is mandatory and must match **exactly** (including the em dash):

`Geen interesse? Eén antwoord volstaat — dan mailen wij u niet meer.`

### What the body never contains

- USDC, Solana, Phantom, mint, treasury address, “crypto”
- FACTUUR / INVOICE / a Belgian ondernemingsnummer you invented
- Host-shame (Wix / Bootply / “amateuristisch” / “uit de vorige eeuw”)
- The word **seconden**, delays in seconds, or “in a few seconds”
- A second live URL that still bills in USDC (`treasury-tools.surge.sh`, `lid-kit-treasury.surge.sh`, `solana-invoice-treasury.surge.sh`, …)
- Twizzit-replacement language
- `je` / `jij` / `jouw`

---

## 4. How to fill a hook (examples — not a send list)

These rows show **shape**. They are **not** a queue. Do not mail them from this file.

### Date hook (eetdag)

Opened: Centrumharmonie Geel homepage — eetdagen **10–11 oktober 2026**, prices on the card, no checkout on that page.

| Slot | Fill |
| --- | --- |
| `{HOOK_SUBJECT}` | Eetdagen 10 en 11 oktober — inschrijving zonder kassa op de site |
| `{HOOK_OPEN}` | Op uw site staan de eetdagen van 10 en 11 oktober 2026 met prijzen, zonder een inschrijving die ter plaatse kan worden betaald. |
| `{NEED}` | Geld in voor die twee avonden |
| `{EUR}` | 199 |
| `{OFFERTE_LINE}` | één publieke inschrijf- en betaalpagina voor die eetdagen, naast de site die u al heeft |

No host-shame: the club already has a modern site. The hook is the **date**, not the CMS.

### Break hook (placeholder site)

Opened: `fanfaremolsluis.be` — “We werken momenteel aan onze website, binnenkort terug online.” Gemeente Mol still lists the club.

| Slot | Fill |
| --- | --- |
| `{HOOK_SUBJECT}` | ‘Binnenkort terug online’ op fanfaremolsluis.be |
| `{HOOK_OPEN}` | Op fanfaremolsluis.be staat nog dat de site ‘binnenkort terug online’ komt; de gemeente houdt de club intussen bij. |
| `{NEED}` | Een publieke clubpagina die het bestuur zelf kan laten staan |
| `{EUR}` | 900 |
| `{OFFERTE_LINE}` | vijf Nederlandstalige pagina’s (home, over, agenda, lid worden, contact) die bij u blijven |

No host-shame: do not add “uw huidige host is waardeloos.” The break string **is** the hook.

### Date hook that is still a walk-in

Opened: Harmonie De Eendracht Geel-Oosterlo — Friday repetitie 20:00–22:00, lid in = “kom gerust ’s vrijdags langs.”

| Slot | Fill |
| --- | --- |
| `{HOOK_SUBJECT}` | Vrijdag 20:00 in Oosterlo — lid worden staat nog niet op de pagina |
| `{HOOK_OPEN}` | U nodigt mensen uit op de vrijdagrepetitie van 20:00 tot 22:00 in het Ontmoetingscentrum Bonten Hannen; op de pagina is lid worden nog een langs-komen. |
| `{NEED}` | Lid in (en later geld in) zonder de repetitie te vervangen |
| `{EUR}` | 349 |
| `{OFFERTE_LINE}` | een lid-wordenpagina op naam van De Eendracht, naast de vrijdag die u al heeft |

If Bancontact or Twizzit pay is already on an opened page: **do not use this template** for that club (HOLD — not a Scout send).

---

## 5. Pre-send checklist (human, later)

A later human may send **only** if every line is true. This PR still sends nothing.

1. Display name is **Sasha · SovereignForge (Geel)**, not Sasha only.  
2. To is one organisational mailbox; **not** Hotmail / Live / Outlook / MSN; not Gmail/Telenet/Skynet.  
3. Greeting is **Beste bestuur,** and the body uses **u**.  
4. Subject is `{HOOK_SUBJECT}` — date or break — **not** a product name.  
5. `{HOOK_OPEN}` quotes a fact from a page opened for **this** club. Swapping the club name would make the sentence false.  
6. Price is **€199 / €349 / €900** as OFFERTE. No USDC.  
7. Body contains `https://club-site-kit-treasury.surge.sh/` and no other pay/catalog host.  
8. Opt-out line is verbatim: `Geen interesse? Eén antwoord volstaat — dan mailen wij u niet meer.`  
9. No host-shame. No seconds. No invented KBO. No FACTUUR.  
10. Cadence: this send is alone, or at least ten minutes after the previous outbound.  
11. Operator / CEO has picked **this** mailbox. No blast.

If any line fails: **do not send.** Fix the copy against this file. Do not write a second template.

---

## 6. What this run did / did not do

| Did | Did not |
| --- | --- |
| Wrote this page as the **only** send template | Send mail, open a Gmail draft for send, or click mailto |
| Designed out the seven Scout reds in §1 | Authorise 12/minute or a same-hour burst |
| Locked from-name **Sasha · SovereignForge (Geel)** | Leave From as `Sasha` |
| Locked live kit URL to the Dutch club-site kit | Link a USDC catalog or a 9/49 Surge toy |
| Locked opt-out verbatim | Paraphrase the stop line |
| Showed date/break fill **examples** | Turn those clubs into a send queue |
| Banned Hotmail To and seconds in copy/cadence | Harvest personal ISP mailboxes |

---

## 7. Sources

- Live kit (opened this seat): [https://club-site-kit-treasury.surge.sh/](https://club-site-kit-treasury.surge.sh/) — Dutch club pages, labelled demo, no account.  
- Buyer facts used only as **hook-shape** examples: `docs/ultra-2026-08-27/BUYERS.md` on `cursor/ultra-belgian-buyers-44c6` (Centrumharmonie eetdagen 10–11 Oct 2026; Fanfare Mol-Sluis placeholder; Harmonie Oosterlo Friday repetitie). Those rows stay research.  
- CEO send law: `docs/ultra-seats/CEO.md` on `cursor/ceo-ultra-seat-c448` — no blast; EUR OFFERTE; operator is not the freelancer.  
- Club mailbox hygiene: `docs/geel-club-mailtos.md` on `cursor/geel-club-mailtos-6be7` — no Hotmail/Gmail/Telenet To.

**PII:** No personal mailbox, phone, or home street is copied here. No treasury string is copied here.

---

End of FIX playbook. The next Scout action is a **human** picking one mailbox against this template, or nothing. This PR does not send.
