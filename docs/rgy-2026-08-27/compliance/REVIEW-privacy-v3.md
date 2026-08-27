# REVIEW — Privacy STORE Versie 3

**Seat:** reviewer batch (docs only)  
**Date:** 2026-08-27  
**Artifact:** STORE Versie 3 Dutch fill-in + CEO public design-out for the live sentence  
**Verdict:** **GREEN** (fill-in package only)  
**Not a lawyer. Not a stamp.**

Scored **from zero** against Versie 3. Versie 2 colours are not reused.

---

## What was scored

STORE Versie 3, as given in this batch:

- Trackers: `Wij zetten zelf geen cookies, pixels of analytics. Of Surge of de mailhost logs of cookies zet, is niet geverifieerd.`
- EER (fill-in): `Offerte-mail loopt via Gmail. Deze pagina noemt geen SCC- of adequacy-claim.`
- CEO public design-out (what Builder ships on the live page): `Offerte-mail loopt via Gmail, een dienst buiten de EER. Alleen om uw vraag te beantwoorden.` — no SCC / adequacy words on the live page.
- Fill-ins: Sasha, Geel, `sasha.de.vree.rene@gmail.com`.
- One privacy page on `sovereignforge.surge.sh`.
- No AVG badge, no banner, no USDC / IBAN / card.

Sections not restated in the Versie 3 delta (Wat / gegevens / OFFERTE / geen FACTUUR / bewaartermijn / no profiling / rechten / GBA) are treated as **still in STORE** unless a later batch drops them. This score does not invent their sentences.

Live `privacy.html` Versie 1 is **not** this artifact. It still contains “Betaling is on-chain in USDC”. That would fail USDC-lead if it were the object. It is not.

---

## Scorecard

| # | Cell | Score | Why (Versie 3 only) |
| --- | --- | --- | --- |
| 1 | USDC-lead | **GREEN** | No USDC / IBAN / card in the fill-in or the public design-out. |
| 2 | Who / contact | **GREEN** | Sasha, Geel, locked mail. Geen DPO was already the STORE shape. First name only is a note, not a yellow on this fill-in. |
| 3 | Trackers | **GREEN** | First-party claim is limited to “wij zetten zelf geen…”. Host / mailhost logs or cookies are **niet geverifieerd**, which matches this-run evidence (static HTML, no first-party script; one privacy GET without `Set-Cookie`; no Surge audit). |
| 4 | EER | **GREEN** | Placeholder is gone. Fill-in names Gmail and refuses SCC / adequacy theatre. Public sentence states Gmail is outside the EER and is only used to answer the question. |
| 5 | Badge / banner | **GREEN** | None. |
| 6 | One page | **GREEN** as a copy lock (the shop origin already has `/privacy.html` as the slot). |

**Overall: GREEN** for the STORE Versie 3 fill-in plus the locked public EER sentence.

GREEN here means: the **yellows this batch named** (USDC-lead, tracker overclaim, EER `[Invullen]`) are closed in the copy. It does **not** mean the live page is green. It does not mean AVG-conform.

---

## Notes (not colours)

1. **Live is still Versie 1.** Until Builder ships this copy to `sovereignforge.surge.sh/privacy.html`, the public text still leads with USDC. That is a ship task, not a leftover yellow **on this fill-in**.

2. **“Sasha” is not a civil-name stamp.** The fill-in uses a first name plus Geel plus the Gmail. A later human page may write a full name. This batch filled the blank it was given.

3. **“Een dienst buiten de EER” is the locked public sentence**, not a legal classification of Google Ireland vs onward US transfer. This seat does not stamp that wording. It scores that the page no longer ships `[Invullen]` or an SCC / adequacy claim.

4. **Kits** were not in the Versie 3 lock list. This run still saw kit hosts without a privacy link. Out of this fill-in’s scorecard.

5. **GBA URL** from STORE still points at `https://www.gegevensbeschermingsautoriteit.be/` (301 `/burger` this run).

---

## This file is not

- Not legal advice. Not a GBA filing. Not an AVG badge.
- Not a stamp that Surge, Gmail, or the operator is compliant.
- Not a live-page PASS. Not HTML. Not mail. Not a KBO.

End.
