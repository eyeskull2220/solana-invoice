# PII / secrets scan — live Surge pages

**Overall: PASS**

Live sites were read-only. Nothing on these hosts was edited, redeployed, or requested to change.

| | |
|---|---|
| Scanned | 2026-08-26 00:44–00:49 UTC |
| Method | HTTP GET of HTML + linked assets; leak-path probe; regex for keys / seeds / tokens / passwords / emails / phones / street addresses; browser runtime check (DOM, cookies, `localStorage`, network) |
| Verdict | **PASS** — no keys, seeds, tokens, passwords, phone numbers, home addresses, or unexpected emails |

## Allowlist (pay-to)

These receive addresses are expected and **not** findings:

| Chain | Address | Seen on scanned hosts? |
|---|---|---|
| Solana | `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3` | Yes — pay page `config.js`, rendered DOM, QR URL |
| Ethereum | `0x9eb954b567ef3616424a6e1bf42c63724930aa54` | No (these pages are Solana USDC only) |

Circle mainnet USDC mint `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v` also appears. That is a public mint id, not a secret.

## Results by host

### https://solana-invoice-treasury.surge.sh/ — PASS

Published files that are **not** the Surge index fallback:

| Path | Role |
|---|---|
| `/` (`index.html`, 50279 B) | Pay / unlock landing |
| `/config.js` (369 B) | Treasury receive address + price |
| `/solana-invoice.html` (34267 B) | Product invoice file (empty address field) |
| `/README.md` | Setup notes |
| `/robots.txt` | `User-agent: *` / `Disallow: /` |
| `/CNAME` | Host name only |

**Flagged:** none.

**Reviewed, not flagged:**

- `window.TREASURY.solanaAddress` is the allowlisted Solana pay-to. After `config.js` loads, `#addr` and `#addr49` show that address; the “do not send yet” banners are hidden.
- QR image: `https://api.qrserver.com/v1/create-qr-code/?size=168x168&data=96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3` (same allowlisted address).
- Product file has placeholder `Your USDC receive address` and no baked-in wallet, email, or phone.
- README mentions `127.0.0.1:4173` as a local-dev URL only.

### https://treasury-tools.surge.sh/ — PASS

Catalog HTML only (plus `/README.md`, `/robots.txt`, `/CNAME`). No scripts, no pay-to, no emails, no phones, no home address. Links out to other `*.surge.sh` tools (those extra hosts were **not** in this scan’s scope).

### https://csv-cleaner-treasury.surge.sh/ — PASS

Single-file cleaner. No sample CSV, no pay-to, no emails, no phones, no home address. File input starts empty. Footer states the spreadsheet never leaves the browser.

### https://form-to-email-treasury.surge.sh/ — PASS

Destination email input is **empty** at load. The only email string in source is the placeholder `you@studio.example` (reserved `.example` TLD, RFC 2606) — not a real inbox.

Default field labels are generic (`Name`, `Email`, `Message`). Subject default is `Website inquiry`. No pay-to in this file. No phone or street address.

### https://rss-to-webhook-treasury.surge.sh/ — PASS

Feed URL and webhook URL inputs are **empty**. Placeholders are `https://example.com/feed.xml` and `https://hooks.example.com/incoming/` (reserved example hosts). No Discord / Slack / Telegram webhook, no bot token, no pay-to, no email, no phone.

## What was searched for

| Class | Result |
|---|---|
| PEM / PKCS8 private keys, Solana secret-key arrays, 64-byte hex privkeys | None |
| BIP-39 / “seed phrase” / “mnemonic” / “recovery phrase” | None |
| API tokens (`sk-`, `sk_live_`, `ghp_`, `xoxb-`, `AKIA…`, JWTs, SendGrid `SG.`, Stripe, OpenAI, Anthropic, Telegram `bot:token`) | None |
| Passwords / `password=` assignments | None |
| Unexpected emails (anything other than `you@studio.example`) | None |
| Phone numbers / `tel:` | None |
| Street / home addresses | None |
| Unexpected wallets (base58 32–44 or `0x` + 40 hex other than allowlist + USDC mint) | None |
| Source maps | None |
| Cookies / `localStorage` / `sessionStorage` at runtime | Empty on all five |

## Leak-path probe (all five hosts)

Requested and **not** present (HTTP 404 Surge error page, no PII in the body):

`.env`, `.env.local`, `.git/HEAD`, `.git/config`, `wallet.json`, `keypair.json`, `id.json`, `secrets.json`, `credentials.json`, `package.json`, `*.map`, `auth.json`, `token.json`, `keys.js`, and sibling product files that are generated in-browser only (`contact-form.html`, `watcher.js`, `sample.csv`, …).

`config.js` exists **only** on the pay host (expected). Other hosts 404 it.

## Runtime notes (not FAIL)

- Missing `/favicon.ico` on each host (404). No secret in the 404 body.
- Browser mixed-content warning on Form to Email because a preview `<form action="mailto:">` is empty-target until the user types an inbox. Not a credential leak.
- `/solana-invoice.html` is fetchable without going through the unlock UI. The file has no treasury key or personal data; it is the product HTML. Recorded here so the unlock story is honest, not as a PII fail.
- Each host also publishes `/README.md`. Those files contain no emails, phones, or secrets.

## Out of scope

Catalog links to other Surge tools (Quote Calc, ICS Reminder, tip jar, …) were **not** scanned. Re-run this checklist against those hosts if they go live with their own copy.

## SHA-256 of scanned primary files

| File | SHA-256 |
|---|---|
| solana-invoice-treasury `index.html` | `c3edc298cc50a99455ae0767c79b832c472c46f0a8753fda7a77c4afba576c11` |
| solana-invoice-treasury `config.js` | `21867d7193984f1b952342a62825047ca5bf6cebdccfc9db64a0b38f3cc58713` |
| solana-invoice-treasury `solana-invoice.html` | `22fd5fff03c20588d16baed0e5b5b929dc3faa4cc149de1d4033e94671211ac5` |
| treasury-tools `index.html` | `1da6bb55958216a6530e4f406155e6228a328118cec208c3517ca636e5ff3de1` |
| csv-cleaner-treasury `index.html` | `db61beb2811f63df0ea4c3a7ce073e044ddc17a73a90cc0fc8c07e49b4c470c6` |
| form-to-email-treasury `index.html` | `8fde2344085b04f60a4b6cf1b9e0e243b3a6a157ded16ef665d9e102420af0ad` |
| rss-to-webhook-treasury `index.html` | `34bb667d0d016cc6f548868c0e4addc77db56ff6adb390bc3a9f9592a5ebb32c` |
