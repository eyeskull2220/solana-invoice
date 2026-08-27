# REVIEWER — Scout RESEARCH stage RGY

Seat: **REVIEWER**. Stage: **Scout RESEARCH only**. Date: **2026-08-27**.

Score **starts at 0**. GREEN only if the research pack is clean: sourced from this session’s SENT/INBOX, internally consistent, no invented mailto, no second, no send queue. This file does not implement. **No mail was sent. No seconds. No drafts created.**

Judged from: Gmail SENT + INBOX this run, live [tkoostakker.be/inschrijven](https://www.tkoostakker.be/inschrijven), PR [#133](https://github.com/eyeskull2220/solana-invoice/pull/133) (`docs/rgy-2026-08-27/scout/01-adv-research.md`), PR [#117](https://github.com/eyeskull2220/solana-invoice/pull/117) (`docs/ultra-seats/SCOUT.md`), PR [#115](https://github.com/eyeskull2220/solana-invoice/pull/115) (`docs/ultra-2026-08-27/BUYERS.md`).

The **18 first-mails** stay **RED**. That is not a GREEN stamp on the pack. The pack is the evidence that those mails are RED.

**GREEN count: 12 / 16. Stage: not closed. Overall: YELLOW.**

---

## Table

| item | RED/YELLOW/GREEN | note | fix-if-not-green |
| --- | --- | --- | --- |
| corpus 18 SENT / 0 replies | GREEN | This run: `in:sent after:2026/08/27 before:2026/08/28` → **18** threads, each **1** outbound, all `Label_2` + SENT. Last clock **18:48:14Z** (Halle-Kempen). Inbox domain search of the 18 organisational boxes → **empty**. KWZC 26 Aug reply exists and is **stop** (rebuild in flight) — outside the 18. | — |
| S1 stencil wave | GREEN | Wave B bodies are the same five-block paste. Live: Oostakker, Concordia, Wommelgem, KST, Notengalm, Brass — `Beste bestuur` → one scraped line → `kant-en-klare Nederlandstalige [SKU]` → `voorstel, geen factuur` → `Prijs: €N` → `ja of nee`. SizeEstimate Wave B ~2111–2346 B. Wave A is the other machine (Geel opener + USDC + `google.com/url`). | — |
| S2 product-first subjects | GREEN | All **18** SENT subjects lead with `Voorstel` + SKU. Count this run: clubwebsite 6, lid-inschrijving 9 (8 Wave B + Kampenhout), sponsorblad 2, menukaart 1. Matches #133’s 6+8+2+1+1 split. | — |
| S3 missing opt-out | GREEN | Live bodies (Oostakker, Notengalm, Concordia, Wommelgem, KST, Brass, KZK, Gio’s): no `stop`, no bezwaar, no unsubscribe. Wave B close is `ja of nee`. Wave A close is `antwoorden jullie op deze mail`. WER XII.13 § 2 cite in #133 matches #117 (Justel ELI 2013011667). “Ja of nee” is not § 2. | — |
| S4 host-shame | GREEN | Live snippets: Notengalm “One.com-pagina”; Sint-Niklaas “draait nog op Drupal”; Gio’s “opent niet meer goed”; KWZC 26 Aug Drupal 7 → they already had a rebuild. Enough for a pattern. Pack correctly says not all 18 contain it. | — |
| S5 12-in-60s | GREEN | Wave B internalDate this run: 18:47:13, :15, :18, :20, :27, :30, :32, :34, :58, 18:48:00, :01, :14. **12 Tos, 61 seconds.** Gaps of 1–3 s. Title “60s” vs body “61 seconds” is the same burst. | — |
| S6 Oostakker Bancontact HOLD miss | GREEN | Live page this run still: lidgeld immediately via **bankcontact**, kredietkaart, KBC of Belfius; `info@` is sociaal tarief, volzet/wachtlijst, vragen. SENT 18:48:01Z still claims “info@ voor wie wil starten” / “losse mail”. False brief + €349 lid-in. HOLD was already in #115 §5 and #117. | — |
| A1 USDC Wave A | GREEN | Live KZK: `900 USDC` + Solana pay-to. Live Gio’s: `199 USDC` + same pay-to. Demo URLs wrapped in Gmail `google.com/url`. Pack’s six-To Wave A map matches SENT. | — |
| A2 impersonal `info@` | GREEN | All 18 SENT Tos are organisational `info@`, not harvested personal boxes. | — |
| A3 OFFERTE not FACTUUR | GREEN | Live bodies stamp `voorstel, geen factuur` / `offerte`. No FACTUUR. | — |
| A4 no seconds | GREEN | 18 threads, 1 message each. Inbox empty. Gmail drafts this run: two leftover 26 Aug directory pitches (densediscovery / cooperpress), **not** club seconds. Pack forbids patching the 18. Keep it. | — |
| A5 *jullie* / from-name | GREEN | Finding is correctly **YELLOW on the mail**. Wave B is *jullie* + from-name “Sasha”. Playbook wants **u** and `Sasha · SovereignForge (Geel)`. Origin was not spoofed as the club. | — |
| A6 wasted date/break hooks | YELLOW | Pack names Halle-Kempen 27 sep, De Kelle volzet tot juni, Kampenhout 4 sep, Sint-Amands LUMEN / 250 jaar. It **omits** the first Wave A body: KZK “test- en inschrijvingsdag is **morgen 28 augustus om 17u**”. Also omits Sint-Niklaas mosselfeest 29 augustus / concert 24 oktober (in the SENT snippet). A6 is not an exhaustive hook ledger. | Name every date/break that already sat in a Watch-18 body. Do not turn those names into seconds. |
| 18-table face integers | YELLOW | #133 table leaves rows 9–11 and 13 as `€ (… stencil)` without the integer. This run: Concordia **€349**, Wommelgem **€349**, KST **€349**, Brass **€900**. S1 already quotes €349 for the lid-in paste, so the SKU is recoverable — the corpus ledger is still incomplete. | Fill face integers from SENT. Still not a merge file. |
| no send queue / no 13th from pack | GREEN | Design-outs are constraints for a **later unmailed** rechtspersoon. Explicit: do not second the 18, do not mail from the file, EUR-only face. Example subjects use already-mailed gevelnamen marked **do not send**. | — |
| Tos table as merge-bait | YELLOW | #133 reprints all 18 organisational mailboxes in a public markdown table (same list as #117). Intent is stop-list. Adversarial read is a CSV. #105 is still the same 18 as a buyer list. | Subsequent Scout files name gevelnaam + UTC only. Operational copy is `Label_2` on SENT. Do not merge #105. This review does not reprint Tos. |

---

## What was live-checked (this run)

| Check | Result |
| --- | --- |
| SENT 27 Aug | Exactly 18 `Voorstel` threads. No 19th. |
| Wave B clock | 18:47:13Z → 18:48:14Z |
| Replies on the 18 | 0 |
| KWZC 26 Aug | Human reply: site already being redeveloped — **stop** |
| Oostakker `/inschrijven` | Bancontact / KBC / Belfius live; `info@` is not “start here” |
| Oostakker SENT body | False “losse mail” + €349 lid-inschrijving + `ja of nee` |
| Wave A USDC | KZK 900 + Gio’s 199 + treasury pay-to |
| Host-shame lines | Notengalm One.com; Sint-Niklaas Drupal; Gio’s opent niet |
| Club drafts | None. Two unrelated 26 Aug directory drafts only. |
| Mail from this review | None. `send_message` not used. No draft created. |

This review does **not** reprint SENT Tos or the operator from-mailbox.

---

## The 18 mails (still RED — not a new queue)

Confirmed RED this run, same six attacks as #133:

| # | Attack on the mail | Mail score |
| --- | --- | --- |
| S1 | Stencil wave (Wave B five-block paste) | **RED** |
| S2 | Product-first subjects (`Voorstel [SKU] …` × 18) | **RED** |
| S3 | Missing WER XII.13 § 2 opt-out (“ja of nee” is not STOP) | **RED** |
| S4 | Host-shame (One.com, Drupal, “opent niet”; KWZC already said no) | **RED** |
| S5 | 12-in-60s (18:47:13–18:48:14Z) | **RED** |
| S6 | Oostakker Bancontact HOLD miss (€349 lid-in; Bancontact already live) | **RED** |

Do not second any of the 18 to patch opt-out, euro, host-shame, or the false Oostakker brief. Silence is the answer.

Adjacent on the mail, as in #133 and re-checked: A1 USDC Wave A **RED**; A2 `info@` **GREEN**; A3 OFFERTE **GREEN**; A4 no seconds **GREEN** (keep it); A5 *jullie* / from-name **YELLOW**; A6 wasted hooks **YELLOW** (and the pack’s A6 list is incomplete — see table).

---

## Design-out (every YELLOW on the **pack**)

Until the matching research row is GREEN, a later Scout file **must not**:

1. **Treat A6 as exhaustive.** The strongest Wave A date/break (KZK 28 augustus 17u) is missing from #133’s A6 list. Completing A6 is research, not a reason to write a second.
2. **Leave face integers as “€ (stencil)”.** The 18-table is the corpus ledger. Fill Concordia / Wommelgem / KST / Brass from SENT (€349 / €349 / €349 / €900). Still not a mail-merge.
3. **Reprint the 18 Tos** in new markdown. #117 and #133 already have the stop-list. Next files: gevelnaam + UTC. `Label_2` is the operational copy. Do not merge #105.
4. **Send, second, or draft** from research or from this review. Design-outs for a later first are constraints, not a tonight queue. Example subjects in #133 that reuse already-mailed gevelnamen stay unsent.

GREEN locks on the **mails** that design must still honour (the research of these is closed even though the pack is YELLOW): no five-block paste; no `Voorstel [SKU]` subject; WER XII.13 § 2 stop-line on every future first; no Drupal / One.com / “opent niet”; floor 10 minutes between sends; HOLD where Bancontact / KBC / Belfius / Payconiq / Twizzit pay / Mollie is already live; EUR-only face; no USDC / Solana / wallet / mint / treasury address in outreach; no seconds to the 18 or the 26 Aug set; KWZC stays stop.

---

## Verdict

Scout RESEARCH is **not GREEN**.

The named six attacks are **sourced and live-checked**. The 18 first-mails are **RED**. Zero replies. No seconds. The pack did not send, did not invent a 13th, and did not draft a club voorstel.

The pack is still **YELLOW**: A6 is an incomplete hook ledger (misses KZK 28 Aug and Sint-Niklaas mossel/concert), four Wave B face integers are blank, and the 18-table reprints mailboxes that a later agent can merge. GREEN only when those three hygiene rows close — still without mailing.

No implementation in this PR. No mail. No seconds.
