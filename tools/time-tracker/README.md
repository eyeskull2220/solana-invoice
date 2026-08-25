# Time Tracker

Offline, single-file time tracker. Open `index.html` in a browser — no server, no build, no network, no wallet.

## Price

| Field | Value |
|---|---|
| Amount | **49 USDC** |
| Pay to | `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3` |
| Network | Solana |
| Token | Circle USDC (`EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v`) |

Send exactly 49 USDC. Do not send SOL.

## Use

1. Open `tools/time-tracker/index.html`.
2. Type a task name.
3. Click **Start**. The clock runs until you click **Stop**.
4. Repeat for more sessions. Totals for today and all sessions update as you go.
5. Click **Export CSV** to download `time-tracker-YYYY-MM-DD.csv`.

**Copy address** copies the Solana USDC pay-to address.

Sessions are stored in this browser (`localStorage`). A running timer resumes if you reload the page.

## CSV columns

`Task,Started,Stopped,Duration seconds,Duration`

Started and Stopped are ISO-8601 timestamps. A still-running session is included with an empty Stopped cell.

## Notes

- No account. No wallet connect. The pay block is copy-address only.
- Delete a row, or **Clear all**, to drop logged sessions from this browser.
- Enter in the task field starts a timer when idle.
