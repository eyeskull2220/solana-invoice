# UTM Builder

One HTML file. 49 USDC. Offline campaign-link builder.

Open `index.html`. Type a page URL, source, medium, and campaign. Copy the tagged link. Optional: pull existing `utm_*` tags from a URL, or stamp the same tags onto a list of URLs and download a CSV.

No account. No wallet connect. Tags never leave the browser.

## Pay

Send **exactly 49 USDC** on Solana to:

```
96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3
```

- Network: Solana
- Token: USDC
- Mint: `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v`

Do not send SOL. Do not send USDC on another chain.

The page also shows a Solana Pay QR (`amount=49`, `spl-token` = that mint) and a copy-address button.

## Fields

| Field | Typical use |
| --- | --- |
| Website URL | Landing page. `https://` is added if you omit a scheme. |
| `utm_source` | Where the traffic comes from (`newsletter`, `google`) |
| `utm_medium` | Channel (`email`, `cpc`, `social`) |
| `utm_campaign` | Name of the push (`spring_sale`) |
| `utm_term` | Optional paid keyword |
| `utm_content` | Optional creative or A/B label |

Empty fields are omitted. Existing non-UTM query params and hash fragments stay. **Normalize tags** lowercases values and turns spaces into underscores; the page URL is left alone.

## Offline

Save `index.html` and open it from disk. The builder runs without a server. The pay QR image needs the network; copy-address still works offline.
