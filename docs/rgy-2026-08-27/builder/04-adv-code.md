# 04 — Adversarial code (Builder leftover HTML)

**Seat:** Builder  
**Lens:** adversarial code, not design praise  
**Date:** 2026-08-27  
**HEAD:** `2170952` (`Merge pull request #27 … treasury-address-9594`)  
**Scope:** this working tree only. START FROM ZERO. Builder HTML/CSS is assumed a **bad layout**. Report-only. No mail.

Grep base (HEAD): `README.md`, `catalog.html`, `config.js`, `index.html`, `solana-invoice.html`. No `robots.txt`. No `betalen.js`. No `tools/`.

---

## Verdict: **RED**

The checkout is leftover one-file HTML. Inline CSS is the layout. USDC is the face. Live Surge `robots.txt` is `Disallow: /` with **no `Allow:`**. Paywall JS unlocks on failure. That is the product, not a side file.

| Probe | Result | Color |
|---|---|---|
| Leftover HTML / inline CSS | Entire tree: 3 HTML files, all `<style>` in `<head>`, one 50 KB pay page that also embeds the product file | **RED** |
| `FACTUUR` | 0 hits on HEAD | **GREEN** |
| `USDC` | 42 hits across all 5 files | **RED** |
| Google Fonts | 0 `fonts.googleapis` / `fonts.gstatic` | **GREEN** |
| Inline junk | `EMBEDDED_INVOICE` blob + minified QRCode + `innerHTML` + third-party QR URL | **RED** |
| `betalen.js` | file absent | **GREEN** |
| robots `Allow:` | file absent in git; live hosts `Disallow: /` only | **RED** |

---

## RED

### R1 — Leftover HTML *is* the app

HEAD file list:

| File | Lines | Bytes | Role |
|---|---:|---:|---|
| `index.html` | 344 | 50251 | pay / unlock landing |
| `solana-invoice.html` | 418 | 34267 | product invoice |
| `catalog.html` | 171 | 4882 | leftover storefront |
| `config.js` | 10 | 353 | treasury globals |
| `README.md` | 20 | 1070 | catalog copy |

There is no CSS module, no `src/`, no router. Layout lives in three competing `<style>` blocks.

- `index.html` lines 8–77: dark “crypto” skin (`--bg: #07090f`, Solana green `--accent: #14f195`).
- `catalog.html` lines 8–110 and `solana-invoice.html` lines 7–193: cream paper skin (`--paper: #f6f3ee`, `--accent: #0c4a36`).

Two palettes, two type stacks, two radii. A Belgian shop secretary hitting the catalog then the pay page gets a theme swap. That is leftover Builder HTML, not a system.

`catalog.html` still sells tools **not in this repo** (CSV Cleaner, Form to Email, RSS to Webhook) via hard-coded Surge URLs (lines 133–163). Dead inventory HTML.

### R2 — `index.html` embeds a second full copy of the invoice

```129:131:index.html
  <script src="config.js"></script>
  <script>
    var EMBEDDED_INVOICE = "\u003c!doctype html>\n\u003chtml lang=\"en\">\n...
```

Line 131 is one escaped HTML string: doctype, cream CSS, editor chrome, `INVOICE` stamp, mint footer, minified QRCode library, and the render IIFE. `downloadProduct()` (lines 279–297) `fetch("solana-invoice.html")` and on any failure falls back to that blob. Two sources of truth for the same file. Drift is guaranteed. This is the inline junk.

### R3 — USDC is the face (hide-the-coin miss)

Counts on HEAD: `index.html` 15, `catalog.html` 9, `README.md` 8, `solana-invoice.html` 7, `config.js` 3. **42.**

Cited, not exhaustive:

```6:7:index.html
  <title>Solana Invoice — 9 USDC</title>
  <meta name="description" content="Solana Invoice. One file. 9 USDC.">
```

```95:100:index.html
      <h2>Pay 9 USDC on Solana</h2>
      ...
      <p>Send exactly 9 USDC to:</p>
      ...
      <p class="net">Network: Solana · Token: USDC</p>
```

```116:120:catalog.html
      <p class="lead">Small one-file tools. Open them, use them, keep them. Billed in USDC on Solana.</p>
    ...
    <p class="warn">Pay USDC on Solana only via the Solana Invoice page. Do not send XRP or any other chain.</p>
    <p class="warn">Treasury Solana USDC: <code>96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3</code><br>Mint: <code>EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v</code></p>
```

```200:247:solana-invoice.html
      <label for="amount">Amount (USDC)</label>
      ...
            <div class="label">Pay USDC on Solana to</div>
      ...
          <div>Network: Solana · Asset: USDC</div>
          <div>Mint: EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v</div>
```

Builder shop face is supposed to hide the coin. HEAD prints the coin in `<title>`, meta, H1-adjacent copy, price pills, mint, and the printed invoice footer.

### R4 — Paywall is adversarial-fail-open

```316:329:index.html
        if (pending) {
          honorUnlock();
          return;
        }
        ...
        verifyOnRpc(sig).then(function (tx) {
          ...
        }).catch(function () {
          return honorUnlock();
        })
```

- Empty treasury → unlock anyway.
- RPC error / parse miss / network fail → unlock anyway.
- `honorUnlock(why)` takes `why` and ignores it (line 300).

A signature-shaped string is enough. This is leftover “ship the file” JS, not a gate.

### R5 — Third-party QR with the treasury address in the query

```160:160:index.html
        img.src = "https://api.qrserver.com/v1/create-qr-code/?size=168x168&data=" + encodeURIComponent(addr);
```

Pay page phones `api.qrserver.com` with the receive address. Product file (`solana-invoice.html` line 254) instead inlines a minified QRCode library (Davidshimjs-era, includes `createMovieClip` / Flash and Android 2.1 `drawImage` hacks). Two QR strategies. One leaks the wallet to a third host. That is inline junk plus a data leak.

### R6 — Missing `robots.txt` in git; live `Allow:` absent

Repo: **no** `robots.txt`. `rg robots|noindex|nofollow` on HEAD → empty.

Live (2026-08-27, `curl`):

```
https://treasury-tools.surge.sh/robots.txt
https://solana-invoice-treasury.surge.sh/robots.txt
https://csv-cleaner-treasury.surge.sh/robots.txt

User-agent: *
Disallow: /
```

26 bytes. Surge default. **No `Allow:` line.** Catalog and pay page are globally disallowed. A Builder storefront that wants a secretary to find the shop via search cannot; a Builder storefront that wanted a precise `Allow: /` (or `Allow: /catalog.html`) never committed the file. Missing `Allow` is the live state, not a hypothetical.

---

## YELLOW

### Y1 — `INVOICE` stamp (not `FACTUUR`, still a legal-looking word)

```220:220:solana-invoice.html
            <div class="word">INVOICE</div>
```

HEAD has **zero** `FACTUUR`. It still prints a large `INVOICE` on the cream sheet. Same leftover paper layout as the Belgian BTW tools, English stamp. Demo vs legal document is not labeled `VOORBEELD` / `OFFERTE` here.

### Y2 — `innerHTML` on live fields

`solana-invoice.html` 335, 341, 358, 360, 362, 368 (and the copy inside `EMBEDDED_INVOICE`). Amount path is regex-gated before the USDC `<span>` write. Address empty-state uses a fixed string then switches to `textContent`. Residual XSS surface is small; still leftover DOM-string HTML instead of nodes.

QR fallback table builder injects `style="border:0;…"` on `<td>` (inside the minified blob, `solana-invoice.html` 254). Only `style=` hits in the tree.

### Y3 — Duplicate IDs / duplicate handlers

Pay page: `#qr`, `#copyBtn`, `#copyStatus` in `index.html`. Product file: same IDs. Harmless while they are separate documents; the embed means the downloaded file and the landing page share a namespace by construction.

`index.html` 167–184: two copy-button listeners, copy-paste twins, not a function.

### Y4 — Two SKUs, one address, one mint

`#pay` (9 USDC) and `#job` (49 USDC, memo `one-job-automation`) share `TREASURY.solanaAddress`. Unlock logic only checks **9** USDC (`EXPECTED_RAW = "9000000"`, line 136). The 49 card is leftover catalog HTML glued onto the invoice landing.

### Y5 — `lang="en"` on a Builder seat that sells Belgian paper

`index.html` 2, `catalog.html` 2, `solana-invoice.html` 2. No `nl`. Cream invoice copy is English (“Amount due”, “Issued”). Leftover from the English one-file prototype.

### Y6 — `config.js` is a writable global

```1:10:config.js
window.TREASURY = {
  solanaAddress: "96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3",
  usdcMint: "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v",
  ...
  asset: "USDC"
};
```

No SRI, no CSP, no freeze. Any later script on the same origin overwrites pay-to.

### Y7 — Type / CSS junk in the “layout”

- `font-weight: 650` (`catalog.html` 90, 96; invoice buttons). Not a CSS2 keyword; browsers clamp. Leftover design token.
- `index.html` body: stacked radial gradients + 16px `ui-sans-serif`. Invoice body: `"Iowan Old Style", Palatino, … serif`. Catalog: system UI on cream. Three type systems.
- `#qr { display: none; place-items: center; }` then `#qr.show { display: grid; }` — grid properties while `display:none`. Harmless, sloppy.
- No skip link, no `main` landmark on `solana-invoice.html` (uses `.app` / `<aside>` / `<article>` only).

---

## GREEN

### G1 — `FACTUUR`

```
rg FACTUUR .
→ 0 matches on HEAD
```

The banned Belgian stamp is not in this checkout. (Unmerged branches still have it — Notes.)

### G2 — Google Fonts

```
rg fonts.googleapis|fonts.gstatic|Google Fonts
→ 0 matches on HEAD
```

Stacks are local / system (`ui-sans-serif`, `Iowan Old Style`, Palatino, Georgia). No stylesheet hop to Google. No privacy leak via fonts.

### G3 — `betalen.js`

```
ls betalen.js
→ no such file
```

`rg betalen` on HEAD → 0. Dutch pay script is not left in this tree. (Unmerged kit copy uses the *word* “betalen” in reminder HTML, not a `betalen.js` asset.)

### G4 — No `style=` in authored markup

Authored HTML uses classes. The only inline `style=` is inside the vendored QRCode table fallback.

---

## NOTES

- **Report-only.** No proof patch. Lines above are already on `2170952`.
- **Do not mail.** This file is the deliverable.
- **Unmerged Builder HTML (not HEAD, do not treat as shipped):** `tools/btw-invoice/index.html` still concatenates `class="word">FACTUUR` (commit `bdec9d9`). Older `tools/inbox-ops/invoice.html` same stamp (`9b74ef3`). Later `inbox-ops-pack` switched print word to `VOORBEELD`. Those trees are not in this checkout; they are leftover on remote branches if anyone merges them onto the shop.
- **Live robots** match the earlier surge PII note (`docs/pii-scan-surge.md` on `490c3c7`): `User-agent: *` / `Disallow: /`. Git never grew an `Allow:`. Surge will keep serving the 26-byte deny-all until a `robots.txt` is committed **and** deployed.
- **Concurrent FIX** (“Builder hide-coin + robots”) may add `robots.txt` / strip USDC after this scan. Re-grep HEAD before treating G1–G3 as still true.
- Unlock-fail-open (R4) and qrserver leak (R5) are code defects, not layout. They sit in the same leftover file as the bad CSS.
- Catalog “Do not send XRP” (`catalog.html` 119) is leftover chain-warning copy from an older treasury page. Fine as a warn; still USDC-faced.

---

## Re-grep (copy/paste)

```bash
rg -n 'FACTUUR|USDC|fonts\.googleapis|fonts\.gstatic|betalen\.js|Allow:|robots' \
  README.md catalog.html config.js index.html solana-invoice.html
ls robots.txt betalen.js 2>/dev/null || true
curl -sS https://treasury-tools.surge.sh/robots.txt
```
