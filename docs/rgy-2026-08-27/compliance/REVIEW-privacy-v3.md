# REVIEW — Privacy STORE Versie 3

**Seat:** reviewer batch (docs only)  
**Date:** 2026-08-27 (re-score)  
**Artifact:** STORE Versie 3 Dutch fill-in + CEO public EER sentence  
**Verdict:** **GREEN**  
**Not a lawyer. Not a stamp.**

Scored from the Versie 3 text in this batch only. No earlier fill-in is the score.

---

## Artifact (this batch)

| Line | Text |
| --- | --- |
| Trackers | Wij zetten zelf geen cookies, pixels of analytics. Of Surge of de mailhost logs of cookies zet, is niet geverifieerd. |
| EER (STORE) | Offerte-mail loopt via Gmail. Deze pagina noemt geen SCC- of adequacy-claim. |
| EER (live, Builder) | Offerte-mail loopt via Gmail, een dienst buiten de EER. Alleen om uw vraag te beantwoorden. |
| Wie | Sasha · Geel · sasha.de.vree.rene@gmail.com |
| Host | one page on sovereignforge.surge.sh |
| Locks | no AVG badge · no banner · no USDC / IBAN / card |

Live `https://sovereignforge.surge.sh/privacy.html` this run is still labelled **Versie 1** and still contains “Betaling is on-chain in USDC”. That page is **not** this artifact.

---

## This-run checks (2026-08-27)

| Check | Result |
| --- | --- |
| Privacy HTML `<script>` / gtag / analytics hosts | none in the live file |
| `Set-Cookie` on `GET /privacy.html` | none |
| Live privacy copy vs this fill-in | different document (Versie 1) |
| Shop home link to `/privacy.html` | present |
| First-party USDC / IBAN / card in **this fill-in** | none |

A quiet `Set-Cookie` on one GET is not a Surge or Gmail audit. The tracker line already says that is unverified.

---

## Scorecard

| Cell | Score | Why |
| --- | --- | --- |
| Trackers | **GREEN** | First-party claim is only “wij zetten zelf geen cookies, pixels of analytics.” Host and mailhost are explicitly **niet geverifieerd**. No banner. |
| EER | **GREEN** | STORE names Gmail and refuses SCC / adequacy words. Live sentence adds that Gmail is outside the EER and is only used to answer the question. No empty heading. |
| Wie / contact | **GREEN** | Sasha, Geel, and the Gmail are filled. |
| USDC / IBAN / card | **GREEN** | None in the fill-in or the public sentence. |
| Badge / banner | **GREEN** | None. |
| One page | **GREEN** | Lock is a single page on the shop origin. |

**Overall: GREEN.**

GREEN means this copy no longer over-claims trackers, no longer ships an empty EER line, names who to mail, and does not put USDC / IBAN / card on the privacy page. It does not mean the live Versie 1 page is green. It does not mean AVG-conform.

---

## Notes (not colours)

- Builder still has to **replace** live Versie 1. Until that ship, the public URL is a different text.
- “Sasha” plus Geel plus the Gmail is what this batch filled. Not a civil-name stamp.
- “Een dienst buiten de EER” is the locked public sentence, not a classification of Google Ireland vs onward transfer. This seat does not stamp it.
- No SCC / adequacy words on the live page is the lock. Do not add them to look complete.

---

## This file is not

Not legal advice. Not a GBA filing. Not an AVG keurmerk. Not a live-page PASS. Not HTML. Not mail. Not a KBO.

End.
