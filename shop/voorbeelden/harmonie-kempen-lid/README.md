# VOORBEELD — Koninklijke Harmonie De Kempische Leeuw

Named-club Dutch preview for the **lid-inschrijving** kit. The face is a Flemish harmony membership page, not a generic Voorbeeldharmonie and not a freelancer studio.

Open [`index.html`](index.html). Phone-first. No account. No wallet connect.

## What this is

- **Club:** Koninklijke Harmonie De Kempische Leeuw, Lille (Antwerpse Kempen)
- **Season:** 2026–2027
- **Winterconcert:** Saturday 19 December 2026, 20:00, parochiezaal Lille
- **Form:** lidmaatschap seizoen 2026–2027 (not 2023)
- **Stamp:** **VOORBEELD**. An offer to a club is **OFFERTE**. Never **FACTUUR**.
- **Mailbox:** `secretariaat@kempischeleeuw.example` (RFC 2606). Club-style, not `hello@studio.example`.

This club is invented for the preview. It is not a live vzw. Do not mail anyone. Do not apply the Geel operator as the freelancer.

## What stays off the face

- No USDC, Solana, mint, or treasury address on the membership page
- No fake KBO / BTW / IBAN
- No leftover 9 USDC HTML toys
- No “GDPR-compliant” badge (plain Dutch privacy sentence only)

## Builder notes

Copy this folder privately when a real harmony pays. Replace the club name, Lille, dates, lidgeld, and the `.example` mailbox. Leave KBO empty until they hand you the real number. Keep VOORBEELD until it is their live page.

Kit settlement stays on the shop pay page, not on this preview.

```bash
sh scan-pii.sh
```
