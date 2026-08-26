# Kilometervergoeding log

One HTML file. Log Belgian freelancer trips, apply the FOD forfait rate, total EUR, download a CSV.

No account. No wallet connect. Nothing leaves the browser after you open the file.

**Price: 9 USDC** on Solana.

## Pay

Send exactly **9 USDC** (not SOL) to:

```
96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3
```

- Network: Solana
- Token: USDC

Copy the address from this README or from the pay box on `index.html`.

## Rate

Default: **0.4440 EUR/km** — quarterly forfait 01.07.2026–30.09.2026 (FOD circulaire 2026/C/76 / omzendbrief 768).

Optional preset: **0.4761 EUR/km** — annual forfait 01.07.2026–30.06.2027.

The rate field is editable. Confirm the current FOD rate before you file. This is not tax advice.

## Use

1. Open `index.html` in a browser.
2. Check the rate (or pick a preset).
3. Fill date, from, to, km, purpose. Example places: Geel → Antwerpen.
4. Click **Add trip**. Repeat as needed.
5. Click **Download CSV**.

Trips stay in this browser until you clear them. Download before you clear.

CSV columns: `date,from,to,km,purpose,rate_eur_per_km,amount_eur`.
