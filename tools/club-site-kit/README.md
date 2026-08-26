# Club-site kit (Belgische club / vzw)

Reusable static website kit for a Belgian club or vzw. One folder: HTML, CSS, JS. No backend, no account, no wallet connect. Agents ship a rebranded copy after payment; this folder is the kit plus a public demo.

**Price:** 900 USDC on Solana (USDC only — not SOL, not another chain).

**Pay-to:** `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3`

**USDC mint:** `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v`

Copy-address on the demo (home pay box and footer). Do not send other assets.

## Demo

Open `index.html`. Fake club only:

- **ZWV De Golfbreker** — zwemclub, Geel
- Contact: `info@golfbreker.example` (RFC 2606, not a real inbox)
- Extra pages: `over.html`, `agenda.html`, `lidworden.html`, `contact.html`
- Banner and footer state this is a demo, not a real vzw

Not Dolfijnen Middelkerke. Not any real club. No personal Gmail, phone, or home address.

## Rebrand

1. **Club name / city / sport** — header and hero copy in each HTML file (or fill `editor.html` and download).
2. **Colors** — in `styles.css`, `:root`:
   - `--water` primary (header, buttons, date blocks)
   - `--lane` accent (rules, chips, copy-button)
   - `--ink` / `--paper` body
3. **Agenda rows** — the four `.event` cards on `index.html` and `agenda.html` (day, month, title, detail). Training table on `agenda.html`.
4. **Mailto / lidgeld** — `lidworden.html` and the lid-worden block on home. Replace the fee and `mailto:info@golfbreker.example`.
5. **Editor** — `editor.html` (offline after open): club name, city, sport, next 4 events, membership fee, contact email, two colors. Download one self-contained HTML, or a zip of the multi-page pack.

The generated club files do not include the kit pay box. Keep the demo disclaimer off the paid copy.

## Host

Upload the folder (or the single HTML from the editor) to any static host. Works from `file://` after download. No build step.

## Files

| File | Role |
|---|---|
| `index.html` | Public demo (all sections + kit pay box) |
| `over.html` / `agenda.html` / `lidworden.html` / `contact.html` | Extra demo pages |
| `styles.css` | Shared layout, mobile-first |
| `site.js` | Menu + copy-address |
| `editor.html` | Rebrand → download |
