# Club-site kit (Belgische club / vzw)

Reusable static site for a Belgian club or vzw. Dutch pages only. No backend, no account, no wallet connect, no identity login.

**Price:** exactly **900 USDC** on **Solana** (USDC only — not SOL, not another chain).

**Pay-to:** `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3`

**USDC mint:** `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v`

Copy-address on the demo (home pay box and every footer). Do not send other assets.

This folder is the public kit plus a **generic demo**. Catalog, pay page, and leftover HTML in the repo root are untouched.

## Demo (generic only)

Open `index.html`. Fake club:

- **Voorbeeldclub vzw** — sport en ontspanning, Voorbeeldstad
- Contact: `info@voorbeeldclub.example` (RFC 2606, not a real inbox)
- Pages: home, over, agenda, lid worden, contact, privacy

Not a live club mailbox. Not a personal webmail. No phone, no home address, no keys.

## Pages

| File | Role |
| --- | --- |
| `index.html` | Home + kit pay box (900 USDC) |
| `over.html` | Over de (fictieve) vzw |
| `agenda.html` | Vier events + trainingstijden |
| `lidworden.html` | Lidgeld + mailto |
| `contact.html` | Mailto-formulier (geen server) |
| `privacy.html` | AVG-demo voor een statische clubsite |
| `club.js` | **Identity file** — name, city, sport, email, fees, colors |
| `styles.css` / `site.js` | Layout, menu, copy-address |
| `scan-pii.sh` | Guard for this public folder |

## How Builder customizes one named club (private, later)

Do this in a **private** copy. Do **not** commit a named real club, a live inbox, or member PII back to this public treasury repo.

1. Copy `tools/club-site-kit/` to a private folder or private repo.
2. Edit `club.js`: club name, city, sport, **club mailbox** (never personal webmail), lidgeld, colors.
3. Rewrite Over / Agenda / Lid worden / Contact / Privacy prose for that club. On privacy, the vzw is the controller.
4. Replace the four agenda cards and the training table.
5. Remove the yellow demo banner and every kit pay box (`.demo-banner`, `.paybox`, `.foot-pay`) from the delivered site.
6. Host the folder on any static host. No build step. No identity login.

The public demo stays Voorbeeldclub. The named club lives only in that private copy.

## What we refuse

- Identity-tenant jobs (directory login, SSO, members area)
- Restacking leftover 9 USDC HTML toys as this kit
- Putting a real club inbox or personal webmail in this public repo
- Applying the operator to coding seats

## PII scan

From this folder:

```bash
./scan-pii.sh
```

Must exit 0 before merge. Allowed pay-to is the treasury Solana address above. Allowed mail is the RFC 2606 demo address.

## Use

Open `index.html`. Mobile menu is Menu / Sluit. Desktop (from 880px) shows the six links in a row. Pay 900 USDC on Solana, then Builder ships one private named-club copy as above.
