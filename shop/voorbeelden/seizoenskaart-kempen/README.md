# Seizoenskaart + QR (Kempen) — VOORBEELD

Printklare Nederlandse seizoenskaart, telefoonpagina als QR-doel, allergenenmatrix. **OFFERTE €199.**

Map: `shop/voorbeelden/seizoenskaart-kempen/`

## Openen

Serveer deze map (niet `file://` — dan kan een telefoon de QR niet volgen):

```bash
python3 -m http.server 8765 --bind 127.0.0.1
```

Daarna:

- Offerte: `/` of `index.html` — stempel **OFFERTE**, bedrag **€199**
- Kaart (print + telefoon): `kaart.html`
- Allergenenmatrix: `allergenen.html`
- Printstylesheet: `print.css` (gekoppeld op kaart en matrix)

Print de kaart vanuit de browser. De QR codeert de http(s)-URL van `kaart.html`. Een telefoon opent diezelfde ronde.

## Wat dit is

Voor een houtgestookte Kempen-bistro waarvan de **kaart elke 2–3 weken wisselt** en die **geen menu op de site** heeft. De voorbeeldzaak op de kaart is fictief (**Bistro De Houthaard**). Geen opdracht van een bestaande zaak.

## Wat dit niet is

- Geen factuur. Document op het gezicht: **OFFERTE**.
- **KBO/BTW: nog niet toegekend** — geen verzonnen ondernemingsnummer.
- Geen FAVV-document, geen wettelijke allergeneninformatie, geen attest. De matrix is een intern werkblad; de keuken vult het echte blad in.
- Geen restack van de root HTML-tools. Deze map is nieuw.

## Prijzen op de offerte

**€199** voor de eerste ronde: printkaart + telefoonpagina + matrix. Extra wissel na deze ronde zit daar niet in. Betaling: overschrijving in euro na akkoord; IBAN volgt na KBO.

## Bestanden

| Bestand | Rol |
| --- | --- |
| `index.html` | Offerte €199 |
| `kaart.html` | Printklare kaart én telefoon-QR-doel |
| `allergenen.html` | Matrix, veertien EU-allergenen |
| `print.css` | `@page` A4 + `@media print` |
| `screen.css` | Scherm, ook smalle telefoon |
| `qrcode.min.js` | QR (MIT, Kazuhiko Arase) |
| `qr-draw.js` | Tekent QR van `location.href` |
| `scan-pii.sh` | Weigert o.a. verzonnen KBO-cijfers |

```bash
sh scan-pii.sh
```
