# SovereignForge shop — DESIGN

Seat: **DESIGN**. Bar: **impeccable Persuade / brand**. Not a template farm. Not Inter-on-cream.

This is the visual and rhetorical system for `shop/sovereignforge/`. Implement against it. Do not “improve” it into a SaaS landing.

## Persuade

A buyer from a kitchen, a vzw, or a van should know in **one thumb-scroll**:

1. **What it is** — a print-ready HTML pack, not a subscription.
2. **The euro price** — one number, large, with €.
3. **That it is an OFFERTE / VOORBEELD** — not a FACTUUR.
4. **The next move** — mail, or open the live demo.

Rules:

- Show the thing. Link the existing surge demos. Do not fake screenshots.
- Name the objection in the headline (account, subscription, agency month). Kill it in the next line.
- One primary action per screen. On a phone that action lives in the **dock**.
- Copy is Dutch, *u*-form, short sentences, specific nouns (menukaart, secretariaat, ontstopping). No “ontdek”, “naadloos”, “digitaal transformeren”.
- Prices are **€199 / €249 / €299 / €349 / €900**. Never a range. Never “vanaf”.

## Brand

**SovereignForge** is a small Kempen atelier that ships HTML you can host yourself. The shop should feel like a **night forge that also prints**: cold iron, one hot mark, brass stamps. Not a bakery. Not a fintech. Not a US start-up.

### Mark

Inline SVG only. Two slabs + a spark. No wordmark icon font. No external logo file.

### Colour (face)

| Token | Hex | Use |
| --- | --- | --- |
| Iron | `#07090c` | Page ground |
| Slate | `#12181f` | Cards, header |
| Mist | `#e8eef2` | Body ink |
| Mute | `#8b969e` | Secondary |
| Line | `#2c3640` | Hairlines |
| Ember | `#ff3d12` | Primary action only |
| Ember ink | `#140400` | Text on ember |
| Brass | `#e0b44a` | Stamps, prices, kicker |

No cream paper (`#f6f3ee` and kin). No sage-on-beige. No purple gradient. No glassmorphism.

### Type

**Bricolage Grotesque**, self-hosted `woff2` in `fonts/`. Weights 400 / 600 / 800. Latin + Latin-ext.

- Headlines: 800, tight tracking, slightly condensed via the face itself.
- UI / body: 400–600, 17px on a phone, 1.45 line-height.
- Prices: 800, `font-variant-numeric: tabular-nums`.

**Forbidden on the face:** Inter, Roboto, Open Sans, system-ui as the *designed* family, any `fonts.googleapis.com` / `fonts.gstatic.com` request, Adobe Fonts, Bunny, cdnfonts.

### Motion

Almost none. Header sticky. Dock sticky. Focus rings. `prefers-reduced-motion: reduce` kills the rest. No hero parallax, no count-up, no typed headline.

## Phone first

Design **320–430px** as the default stylesheet. Desktop is an override from `880px`.

- One column until 880px. Pack cards stack. Do not put price and CTA in a three-up grid on a phone.
- Tap targets **≥ 48px**. Dock buttons full-split.
- Sticky **dock** on small screens: `Pakketten` + `Mail`. Respect `env(safe-area-inset-bottom)`.
- Type that can be read at arm’s length in a kitchen. No 12px legal except the footer.
- Nav is a **Menu / Sluit** button until 880px. No hover-only information.
- Forms: large fields, `autocomplete`, Dutch labels, `mailto:` submit — nothing to a server.

## Pages

| File | Job |
| --- | --- |
| `index.html` | Promise + euro strip + three truths + path to packs |
| `pakketten.html` | All six packs, demos, mail-with-subject |
| `betalen.html` | How euro + OFFERTE works. No settlement strings |
| `contact.html` | Mailto form. RFC 2606 inbox |
| `privacy.html` | AVG for a static site. No trackers |

Shared chrome: skip link, header, dock, footer. `aria-current="page"` on the active item.

## Stamps

A visible **OFFERTE** or **VOORBEELD** chip on every pack and on Betalen. Brass on iron. Slight rotation is allowed; do not make it a joke sticker.

Legal lines that must appear (Dutch):

- Dit is een **OFFERTE** of een **VOORBEELD**, geen wettelijke **FACTUUR**.
- **KBO/BTW: nog niet toegekend.**

## Face blacklist (public HTML, CSS, JS)

Do not print, even to negate them:

- Settlement-asset tickers and names used on the kit pay pages
- Chain names
- Signing-app names
- The common word for on-chain money
- The word for a signing / receive app
- Any receive string or mint string
- Invented `BE0…` numbers, IBANs, GSM numbers, home streets, personal webmail

`robots.txt` is `Allow: /`. No analytics, no pixels, no tag managers, no third-party iframes, no QR-image CDNs.

## Accessibility

- `lang="nl"`.
- Contrast: mist on iron, ember-ink on ember, mute only for truly secondary text.
- Visible `:focus-visible` (brass ring).
- Demo links `rel="noopener noreferrer"` and say they leave the shop.

## What “impeccable” means here

If a secretary in Geel forwards the homepage to a chair, it should still look like **one maker** wrote it: same iron, same ember, same stamps, same prices. If it looks like a 2024 AI landing (cream, Inter, three rounded feature cards, “Welcome to the future”), it failed this seat.
