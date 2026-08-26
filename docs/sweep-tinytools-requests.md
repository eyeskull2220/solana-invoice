# tinytools.tools/requests sweep — 2026-08-26

Research only. Nothing was submitted to tinytools. No new HTML tool was added. No "I built this" click. No leftover clones.

**Board:** https://tinytools.tools/requests (also `?sort=recent`)  
**Catalog we would have listed:** https://treasury-tools.surge.sh/ (paid Solana USDC, 9 / 49 USDC)  
**Decision:** **do not fulfill, do not submit.**

## Verdict

There is **no new unfilled request** we can fulfill as a paid Surge tool this week.

1. The board still has the same **7 open** items, all from public profile `seedlessorange`, all stamped **19w ago**, all at **0 upvotes**. Sorting by recent does not surface anything newer.
2. The homepage copy "15 open requests" is stale. 7 open + 8 fulfilled = 15 rows on the board; only 7 are unfilled.
3. The invoice request is **already fulfilled** (Stellar Invoice). Skip it.
4. **HARD gate:** our catalog is paid USDC. tinytools markets itself as a directory of **free** in-browser tools. Do not submit a paywalled Surge page against this board.
5. None of the 7 open texts is an **exact match** for a tiny tool we already ship. Per the clone rule, do not drop extra HTML this week.

## HARD: paid USDC vs free-only

| Signal | What it says | Source |
| --- | --- | --- |
| Homepage | "572 free web tools" · "Free · No signup · Works in your browser" | https://tinytools.tools/ |
| Browse title | "Browse 600+ free web tools" | https://tinytools.tools/browse |
| Terms | No sentence that tools **must** be free. Tip jars (Ko-fi, BMC, Sponsors, Patreon, PayPal, Stripe) are allowed. Sandbox banner: never enter passwords, payment info, or personal info in the iframe. | https://tinytools.tools/terms §§5–6 |
| Live listings | Some cards are tagged **Paid** or **Freemium** (e.g. Shortform, Tana, Scrintal, MusicAura AI). Those are mostly known commercial products, often "Curated by tinytools". | /browse |
| Submit | `/submit` is behind sign-in. Reviewers can reject "for any reason" including off-topic. | /terms §4, /submit |
| Fulfill path | "Build one, click **I built this**, and the requester gets notified." | /requests |

**Call:** they do not publish a one-line "free-only" checkbox the way Tiny Tool Town does. They **do** present the directory as free, no-signup, in-browser tools, and they warn people not to type payment data into embeds. Our hub charges **9 USDC** (invoice / receipt / tip jar) or **49 USDC** (everything else) on Solana. Listing that as the fulfillment of a request-board item is likely to be rejected, and it would notify the requester with a paywall. **Do not submit.**

We also did not sign in, so we could not have submitted even if the gate were green.

## Already fulfilled — do not touch

**Simple invoice generator — no signup, just fill and download** (1 upvote). Built: [Stellar Invoice](https://tinytools.tools/t/stellar-invoice-ae20dc21) by Ritabanm (`/t/stellar-invoice-ae20dc21`). Catalog search `invoice` returns only that listing.

Our [Solana Invoice](https://solana-invoice-treasury.surge.sh/) is a different product (amount / QR / copy-address, 9 USDC). It is **not** a new unfilled request. Do not click "I built this" on this row.

The other seven fulfilled rows (NexusCSV, PomoLog, Spectrum, Texit, Qreative, PolicyBatch, Responsive Multiview) are also 19w-old `seedlessorange` posts. Out of scope.

## Open requests (7) — fit check

None of these is new this week. Each is checked for (a) exact match to a Surge catalog tool, (b) tinytools prior art, (c) whether a paid 9/49 USDC page would honestly fulfill the ask.

### 1. Side-by-side JSON diff viewer — skip

Paste two JSON objects; colored structural diff (not line text); ignore key order.

- Catalog: JSON Cleaner (pretty-print / minify) is **not** a structural diff. Not an exact match.
- tinytools search `json diff`: **0** tools. `json` hits JSONLint, NexusCSV, InstaIdea (formatter), not a side-by-side object diff.
- Ship this week? Possible as one HTML file, but it is a **new** tool, not a missing clone of something we already have. Clone rule: no.
- Paid USDC: request does not ask to pay. Do not submit.

### 2. Regex builder with plain-English explanations — skip

Pattern → English, English → pattern, live test against sample text.

- Catalog: none.
- tinytools search `regex`: **Regex101** (curated), plus InstaIdea's regex tester. Prior art exists; fulfilling with a 49 USDC clone would be a duplicate **and** a paywall.
- English→regex is not a one-file ship without an external model. Not this week.

### 3. Font pairing suggester — skip

Google Fonts or `.woff2` upload; 3–5 body suggestions; live article / landing / card preview.

- Catalog: none. tinytools `font pairing`: **0** tools.
- Needs a pairing corpus plus font loading. Not a missing catalog twin. Do not clone.

### 4. Meeting cost calculator — real-time dollar counter — skip

Attendees × hourly rate, start, tick dollars in real time, show total at end.

- Catalog: Quote Calc is **hours × rate → download a quote file**. Not a live meeting ticker. Not exact.
- tinytools `meeting cost`: **0** tools.
- Would be a small HTML page, but it is still a new product, not a missing twin. Paid USDC does not match "the kind of thing that makes people think twice about a quick sync." Do not submit.

### 5. Cron expression builder with human-readable preview — skip

Dropdowns → cron, paste cron → English + next 5 runs.

- Catalog: none. tinytools `cron`: **0** tools.
- Shippable as one file, but again a **new** tool. Clone rule: no. Paid: no.

### 6. Browser-based audio trimmer — skip

Waveform, drag start/end, MP3/WAV, client-side only, no upload.

- Catalog: none.
- tinytools `audio trim`: **AudioTrimmer** (curated) plus a local image/PDF/audio suite that includes trim. Request is already covered in-catalog. Do not paywall a duplicate.

### 7. Habit tracker with a GitHub-style contribution graph — skip

1–3 habits, year heatmap, localStorage, export image, no account.

- Catalog: Time Tracker is start/stop + CSV. Not a habit heatmap. Not exact.
- tinytools `habit tracker`: **0** tools.
- New product, not a missing twin. localStorage-only is compatible with "no account," but not with a 49 USDC honor-system wall. Do not submit.

## Exact-match / clone rule

**No leftover HTML clones** unless a request exactly matches a missing tiny tool we can ship this week.

| Open request | Closest thing we ship | Exact? |
| --- | --- | --- |
| JSON diff | JSON Cleaner (pretty / minify) | No |
| Regex builder | — | No |
| Font pairing | — | No |
| Meeting cost ticker | Quote Calc (static quote file) | No |
| Cron builder | — | No |
| Audio trimmer | — | No |
| Habit heatmap | Time Tracker (start/stop CSV) | No |
| Invoice (fulfilled) | Solana Invoice | Already fulfilled on tinytools |

No HTML files were added under `tools/` or as one-off clones.

## PII scan

Scanned: this note, the public request/fulfillment text, and (for "what would we submit") the live catalog pages we would have pointed at.

| Check | Result |
| --- | --- |
| This file | No email, phone, government ID, home address, or private handle. Public board names (`seedlessorange`, Ritabanm) and public URLs only. **Treasury wallet is not copied here.** |
| Open request bodies | No requester contact data. Habit tracker is localStorage-only. Audio trimmer is client-side files. JSON/regex/cron/meeting-cost are text or numbers. Font upload is a font file, not identity. |
| Fulfilled invoice text | Asks to store "my info, client info" in localStorage. That is **PII-adjacent**. We are not building or submitting an invoice clone. |
| If we had submitted a paid Surge URL | Pay page / invoice HTML collect a **Solana pay-to address** and amount. tinytools' own sandbox copy says not to enter payment info in the iframe. Extra reason not to embed the catalog there. |
| Submit / "I built this" | Not used. No account session. |

## What we did not do

- Did not sign in, submit a tool, or mark any request built.
- Did not post a new request.
- Did not upload HTML, zip, or a Surge URL to tinytools.
- Did not add catalog clones for JSON diff, cron, meeting cost, habit heatmap, regex, fonts, or audio trim.
- Did not treat homepage "15 open requests" as 15 unfilled items.

## Re-check next time

Open https://tinytools.tools/requests?sort=recent. If every open row is still `seedlessorange` / 19w / 0 upvotes, this sweep is unchanged. A **new** unfilled row is the only thing that should reopen the paid-USDC vs free-directory gate.
