# REVIEW — Privacy STORE Versie 2

**Seat:** reviewer batch (docs only)  
**Date:** 2026-08-27  
**Artifact:** STORE Versie 2 Dutch fill-in, **not yet live**, plus CEO design-outs locked in this batch  
**Verdict:** **YELLOW**  
**Not a lawyer. Not a stamp.**

This file scores **this batch from zero**. It does not copy an older privacy note as the colour.

---

## What was scored

| Object | In this batch? |
| --- | --- |
| STORE Versie 2 fill-in (text in the batch) | **Yes — the artifact** |
| CEO design-outs locked with that fill-in | **Yes — applied on top of the fill-in** |
| Live `https://sovereignforge.surge.sh/privacy.html` (Versie 1) | Context only. Not the score. |
| PR #124 `shop/sovereignforge/privacy.html` / `privacy-nl.md` | Not this artifact. Not the score. |

**STORE Versie 2 fill-in (as given):**

- Title / version: Privacy — SovereignForge. Versie 2 — 27 augustus 2026.
- Wie: `[voornaam + achternaam]`, natuurlijke persoon, Geel (België). Handelsnaam SovereignForge. Geen KBO, geen vennootschap. Contact `[e-mail]` (geen DPO).
- Wat: statische catalogus. Bestellen via OFFERTE. Geen FACTUUR-module.
- Gegevens: wat u zelf mailt. Doeleinde offerte. Rechtsgrond maatregelen op verzoek vóór overeenkomst. Niet verplicht.
- Trackers (fill-in line): `Deze site plaatst geen cookies, local storage, pixels, beacons of analytics.` (CEO already marked UNVERIFIED for Surge.)
- Ontvangers: geen verkoop. Controller + mailhost + static host.
- EER: still `[Invullen]`.
- Also present as blocks: bewaartermijn, no profiling, rechten, GBA klacht URL.

**CEO design-outs (locked, this batch):**

1. Ship contact `sasha.de.vree.rene@gmail.com`.
2. Tracker line becomes: `Wij plaatsen zelf geen cookies, pixels of analytics. De host kan technische logs bijhouden.`
3. Omit the EER heading unless there is **one true sentence**.
4. One privacy page on `sovereignforge.surge.sh`.
5. Kits link to it.
6. No AVG badge.
7. No banner.
8. No USDC / IBAN / card.

**This-run checks (2026-08-27), not reused notes:**

- Live privacy Versie 1 still has a **Betaling** paragraph: “Betaling is on-chain in USDC…”. That is the USDC-lead this fill-in is meant to close. It is **not** in STORE v2.
- Live privacy HTML: no `<script>`, no `gtag` / analytics / pixel hosts in the page body.
- `GET https://sovereignforge.surge.sh/privacy.html` this run: **no `Set-Cookie`**. That is not a stamp that Surge never sets cookies or never logs.
- Shop home already links to `/privacy.html`. Kit hosts checked this run (`club-site-kit`, `inbox-ops`, `menu-kit`, `sponsor-kit`, `lid-kit`, `vakman-kit`, `pipeline`, `peppol-chase`, `peppol-ready`, `dual-invoice`) had **no** link to that page.
- GBA URL `https://www.gegevensbeschermingsautoriteit.be/` responds (301 to `/burger`).

---

## Scorecard

| # | Cell | Score | Why (this batch) |
| --- | --- | --- | --- |
| 1 | USDC-lead | **GREEN** | Fill-in has no USDC / Solana / Phantom. Design-out forbids USDC / IBAN / card. The live Versie 1 payment paragraph does not ship in this package. |
| 2 | Who / contact | **YELLOW** | Email is locked. `[voornaam + achternaam]` is still a bracket. A natuurlijke persoon without a name on the page is still an identity blank. |
| 3 | Wat / OFFERTE | **GREEN** | Static catalog, order by OFFERTE, geen FACTUUR-module. |
| 4 | Gegevens / doel / grond | **GREEN** | Mail you send; offerte; measures on request before a contract; not required. |
| 5 | Trackers (fill-in line alone) | **YELLOW** | Absolute “deze site plaatst geen cookies…”. CEO already marked that UNVERIFIED for Surge. |
| 6 | Trackers (after design-out) | **GREEN** | Locked line splits “wij” vs host logs. Matches this-run page (no first-party script). Does not stamp the host. No banner, which fits a no-first-party-tracker claim (GBA 17/11/2023 is a pointer, not a stamp). |
| 7 | Ontvangers | **GREEN** | No sale. Categories: controller, mailhost, static host. |
| 8 | EER | **YELLOW** | Fill-in is still `[Invullen]`. Design-out is a rule, not a sentence. Contact is Gmail. Omitting the heading **without** one true sentence about that mail path leaves an Art. 13 hole. |
| 9 | Bewaartermijn / no profiling / rechten / GBA | **GREEN** | Blocks are in the fill-in. GBA URL resolves this run. Not a stamp that the unquoted retention sentence is complete. |
| 10 | AVG badge / cookie banner | **GREEN** | Design-out omits both. Fill-in does not add them. |
| 11 | One page + kits link | **YELLOW** | One page on the shop origin is the lock. Kits **do not** link this run. Design-out is not done. |

**Overall: YELLOW.**

USDC-lead is closed in this fill-in + design-out package. That is not enough for GREEN. Leftover yellow: identity brackets, EER placeholder / missing true sentence, kits not linked. Trackers are GREEN **only** if the locked design-out line ships instead of the STORE absolute line.

---

## Notes

1. **USDC-lead is a copy problem, not a rail problem.** Live Versie 1 puts on-chain USDC under **Betaling**. STORE v2 + “no USDC/IBAN/card” removes that lead. This batch does not score how settlement actually happens.

2. **Do not ship the STORE tracker line.** The fill-in sentence is the UNVERIFIED overclaim. The locked replacement is the line that can go GREEN.

3. **Do not omit EER as a way to delete `[Invullen]`.** The contact lock is Gmail. A true sentence exists as an operational fact (mail you send goes to Gmail). The design-out says keep the heading only if that sentence is written. Writing nothing is not a close.

4. **`[voornaam + achternaam]` is not filled by locking the email.** Contact ≠ identity.

5. **Host cookies vs host logs.** This run saw no `Set-Cookie` on the privacy URL. That is one response, not a Surge audit. The design-out’s “technische logs” is honest; it is not a cookie inventory.

6. **Not live.** Scoring the fill-in does not paint live Versie 1 green. Until Builder ships this copy, the public page still leads with USDC.

---

## Bar for GREEN (this artifact)

A later batch is GREEN only if **all** of these are true in the scored copy (not as a promise):

1. No USDC / IBAN / card on the privacy page (already true here).
2. Voornaam **and** achternaam in the Wie line. No brackets.
3. Tracker line is the locked self/host sentence, not “deze site plaatst geen cookies…”.
4. One true EER sentence in the copy, or no EER heading **and** that same fact stated elsewhere. No `[Invullen]`.
5. No AVG badge. No banner.
6. Kits that sell off this shop actually link the one `sovereignforge.surge.sh` privacy page (checked live, not asserted).

Until then: **YELLOW**.

---

## This file is not

- Not legal advice. Not a GBA filing. Not an AVG-conform keurmerk.
- Not a stamp that STORE, Surge, or Gmail is “compliant”.
- Not an implementation. No HTML. No mail. No KBO.

End.
