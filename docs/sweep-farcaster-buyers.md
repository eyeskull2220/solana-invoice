# Farcaster / Warpcast buyer sweep

**Date:** 2026-08-26  
**Scope:** public casts asking for invoice or CSV tools that we can reply to without an X account.  
**Result: ZERO.** No handles. Nothing was posted.

This is research only. No replies were sent. X/Twitter was not used.

---

## Verdict

**0 replyable buyer casts.**

Searchcaster — the designated public, no-login Farcaster search used in the prior seller sweep — is still dead. Per the hard rule for this run (`If still dead: ZERO. No invent handles.`), this file lists **no** Farcaster usernames, FIDs, cast hashes, or permalinks.

| Count | Meaning |
| --- | --- |
| Replyable buyer casts | **0** |
| Handles invented | **0** |
| Replies posted | **0** |

---

## What we were looking for

Public Warpcast / Farcaster casts where someone asks for a small invoice tool or a CSV cleaner (or close: generate an invoice, clean a spreadsheet, drop empty rows). We would reply from Farcaster itself, not from X.

Live tools we would have pointed at, if a cast had qualified (do not invent others):

- Invoice: https://solana-invoice-treasury.surge.sh/
- CSV Cleaner: https://csv-cleaner-treasury.surge.sh/
- Catalog: https://treasury-tools.surge.sh/

A cast only counts if all of these are true:

1. It is a public Farcaster/Warpcast cast (not an X post).
2. The text is a real ask for an invoice or CSV tool, not a guess from an old handle.
3. The handle and permalink come from a live public search index we actually queried, not memory.

None of that is possible while Searchcaster returns 410, so the count stays at zero.

---

## Searchcaster probe (2026-08-26)

Prior seller sweep: Searchcaster API **HTTP 410**. Re-probed the same day as this buyer sweep. Still 410.

Homepage (HTTP 200): [searchcaster.xyz](https://searchcaster.xyz/) — copy: “Searchcaster has been deprecated. Try Buoy instead.” Docs (`/docs`) **307** to `/`.

| URL | HTTP | Body / note |
| --- | --- | --- |
| `GET https://searchcaster.xyz/api/search?text=invoice` | **410** | `{"error":"The Searchcaster API has been deprecated. Try neynar.com instead."}` · `x-matched-path: /api/deprecated` |
| `GET https://searchcaster.xyz/api/search?q=invoice` | **410** | Same JSON |
| `GET https://searchcaster.xyz/api/search?text=csv` | **410** | Same JSON |
| `GET https://searchcaster.xyz/api/profiles?username=greg` | **410** | Same JSON |
| `https://www.searchcaster.xyz/api/search?text=invoice` | **308** | Canonicalizes to the 410 path above |
| `https://searchcaster.xyz/search?text=invoice` | **307** | To `/?text=invoice` (deprecated homepage, not a live result set) |
| `https://api.searchcaster.xyz/search?text=invoice` | DNS fail | Host does not resolve |

410 is Gone, not a transient 5xx. The API path is wired to `/api/deprecated`. There are no casts to parse.

---

## Other endpoints (status only — not a substitute index)

These were hit only to record whether anything else was a drop-in public search. **Bodies were not parsed for handles.** No names from them appear below.

| URL | HTTP | Why it is not this sweep’s index |
| --- | --- | --- |
| Warpcast `~/search` | **301** → `farcaster.xyz` | Client UI, not Searchcaster. |
| `https://farcaster.xyz/~/search?q=invoice` | **200** HTML | UI page. Not used as a handle source. |
| `client.warpcast.com` / `api.warpcast.com` / `api.farcaster.xyz` `v2/search-casts` | **200** JSON | Unofficial client search. Not Searchcaster. Not used. |
| `https://api.neynar.com/v2/farcaster/cast/search?q=invoice` | **402** | Needs an API key or x402 payment. Out of scope. |
| `https://buoy.club/` | **200** HTML | Searchcaster homepage’s suggested replacement. Not queried for buyers in this sweep. |

If those JSON bodies contain casts, they are irrelevant to this file. Copying them would be inventing a Searchcaster result set we do not have.

---

## Buyer table

Empty on purpose.

| # | Handle | FID | Cast permalink | Ask | Reply without X? |
| --- | --- | --- | --- | --- | --- |
| — | — | — | — | — | — |

No rows.

---

## PII scan

Scanned this file after writing it. Patterns: email (`@` domains), phone numbers, physical addresses, government IDs, crypto wallets, buyer handles / FIDs, real names harvested from casts.

| Class | Hits in this file |
| --- | --- |
| Email addresses | **0** |
| Phone numbers | **0** (a naive digit regex matched the date `2026-08-26` twice; those are dates, not phones) |
| Physical / mailing addresses | **0** |
| Government IDs | **0** |
| Wallet addresses | **0** (none copied from README or elsewhere) |
| `@handle` tokens | **0** |
| Buyer Farcaster handles | **0** |
| Buyer FIDs / cast hashes | **0** |
| Real names of people asking | **0** |

Non-PII strings that do appear: product Surge URLs, Searchcaster / Warpcast / Neynar / Buoy hostnames, and the public error JSON from Searchcaster. The username `greg` appears only as the documented Searchcaster profile-API probe path (HTTP 410; no profile body). It is not a buyer and was not used as a reply target.

---

## What we did not do

- Did not invent Farcaster handles, FIDs, or permalinks.
- Did not treat memory, training data, or the Warpcast client search body as a live buyer list.
- Did not open Neynar (402) or Buoy as a replacement index for this dated sweep.
- Did not post, like, recast, or DM anyone.
- Did not use an X account.

---

## If Searchcaster (or a designated public index) comes back

Re-run with the same buyer queries (`invoice`, `csv`, and close variants). Only then fill the table from that index’s JSON. Until the 410 is gone, keep this file at **ZERO**.
