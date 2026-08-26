# Nostr buyer sweep — invoice / CSV tools

**Date:** 2026-08-26  
**Buyers found:** **0**  
**nsec used:** none (none invented, none loaded, none sent)

Public kind-1 notes were searched for people *asking* for an invoice generator or a CSV cleaner. This catalog sells those as one-file HTML tools (Solana Invoice, CSV Cleaner). The sweep is read-only.

## Hard rules

- **Do not invent an nsec.** Relays that sent `AUTH` were closed. No `EVENT` was published. No Stacker News leftover-sat bounty was claimed.
- **Stacker News leftover sat bounties need nsec — skip those.** SN links and leftover-sat posts were dropped, not replied to.
- **If TLS/search is dead: ZERO.** Primary NIP-50 index `relay.nostr.band` / `api.nostr.band` timed out. Other public search relays answered, so this is not a TLS-dead zero — it is a **no-buyer** zero after filtering.

## Method

Read-only NIP-50 `REQ` over WebSocket (Node built-in `WebSocket`). Filter shape:

```json
["REQ", "<id>", { "kinds": [1], "search": "<query>", "limit": 50 }]
```

No API keys. No Bearer tokens. No `AUTH` responses signed.

### Relays probed 2026-08-26

| Endpoint | TLS / WS | NIP-50 | Used |
|---|---|---|---|
| `wss://relay.nostr.band` | TLS + WS timeout | (primary search index) | **no — dead** |
| `https://api.nostr.band/v0/search` | connect timeout | HTTP search | **no — dead** |
| `wss://cache.primal.net/v1` | WS error | Primal cache | **no — dead** |
| `wss://relay.vertexlab.io` | open, then `AUTH` | yes | **no — would need nsec** |
| `wss://filter.nostr.wine` | NIP-11 `auth_required: true` | yes | **no — would need nsec** |
| `wss://search.nos.today` | live | yes | yes |
| `wss://nostr.wine` | live | yes | yes |
| `wss://relay.ditto.pub` | live | yes | yes |
| `wss://nostrja-kari-nip50.heguro.com` | live | yes | yes |
| `wss://relay.noswhere.com` | live | yes | probed; 0 events for these queries |

`wss://relay.damus.io` and `wss://nos.lol` are up but do **not** advertise NIP-50. They were not used as search.

### Query strings

`invoice generator`, `invoice tool`, `need invoice`, `looking for invoice`, `csv tool`, `csv cleaner`, `clean csv`, `solana invoice`, `usdc invoice`, `invoice html`, `invoice pdf`, `invoice qr`, `csv duplicate`, `need a csv`, `csv spreadsheet`, `simple invoice`, `offline invoice`, `generate invoice`, `invoice template`, `csv columns`, `dedupe csv`, `trim csv`, `invoice usdc`, `crypto invoice`, `one file invoice`, `no wallet invoice`, plus a second pass of `#asknostr invoice`, `#asknostr csv`, `looking for invoice generator`, `looking for csv cleaner`, `need an invoice generator`, `need a csv cleaner`, `recommend invoice tool`, `simple html invoice`, `offline invoice generator`, `csv trim duplicates`.

### What counted as a buyer

A kind-1 note counted only if **all** were true:

1. Public note (kind 1) from a search relay above.
2. Asks for a **tool** (generator / cleaner / template / HTML / PDF), not a Lightning `bolt11` / zap invoice.
3. Ask language (`looking for`, `does anyone`, `#asknostr`, `need a/an`, `recommend`, …).
4. **Not** a seller pitch (price, pay address, Fiverr, “I built/sell”).
5. **Not** Stacker News leftover sats / SN bounty copy.

## Result

**ZERO notes met the buyer bar.**

Raw volume (first pass, five search relays, 32 queries):

| Bucket | Count |
|---|---|
| Unique kind-1 events returned | 1467 |
| Mentions of invoice/CSV after a loose keyword pass | ~1000 |
| Lightning-invoice noise | 291 |
| Seller / promo copy | 239 |
| Stacker News / leftover-sat related (skipped) | 14 |
| Strict ask + tool, not LN, not SN, not seller | **0** |

Second targeted pass (`#asknostr invoice/csv`, “looking for invoice generator”, …): 94 unique events, **0** after the same filters.

## What was skipped on purpose

### AUTH / nsec

`relay.vertexlab.io` sent an `AUTH` challenge. `filter.nostr.wine` advertises `auth_required`. Both were dropped. Inventing an nsec to satisfy AUTH would violate the hard rule and would not make the notes more public than they already are on unauthenticated search relays.

### Stacker News leftover sats

Example of the class that was skipped, not claimed:

- Event `6eb704af78a6e4b7fd629626f322994ef71236859758f94ebb4b58e4cc9668e2` (2026-02-02) — “LN Invoice Generator by cointastical … 440 sats … https://stacker.news/items/1424511”
- Other SN-balance / leftover-sat notes in the same skip set (claiming those sats needs an nsec / SN session).

### Seller noise (not buyers)

These matched invoice/CSV *keywords* and were excluded:

- CobroClaro overdue-invoice / payment-request pages (`19dd578e70d19d7c…`, 2026-08-13).
- Repeated “Micro Freelance Toolkit $10 Solana” invoice-generator spam (many near-duplicate notes on 2026-08-09).
- Fiverr “Need a messy CSV or Excel file cleaned today?” (`7d0a648b7faeb1a1…`, 2026-06-15).
- `#asknostr` pitches selling a “quote/invoice tool” for 7900 sats (`cbf7bd4ca18a7860…`, 2026-06-05).

## Near misses (not counted)

Pain adjacent to the catalog, but **not** an ask for these tools:

- Event `03caf607518269f4…` (2026-08-18) — CSV block-list upload formatted wrong; asks how to delete list entries, not for a CSV cleaner product.
- Event `3ce5aa75a9ce5e4a…` (2026-07-15) — partner needs text parsed into spreadsheet columns; constraint is Excel-at-work, not a public tool request.
- Event `4e9464786a12f352…` (2026-07-18) — `#asknostr` wallet that “won't generate receive invoices” — Lightning receive invoices, not a business invoice HTML tool.

## Implication for this catalog

No public Nostr note from this sweep is a live inbound lead for Solana Invoice or CSV Cleaner. Re-run later with the same no-nsec method. If `relay.nostr.band` is still dead and every remaining NIP-50 relay also fails, record **ZERO** and stop — do not invent keys or scrape SN leftover bounties to fill the list.
