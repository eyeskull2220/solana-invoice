# Startup Buffer and BetaPage check

**Date:** 2026-08-26  
**Catalog checked:** https://treasury-tools.surge.sh/  
**Result: ZERO listings sent.** Nothing was posted on either site.

This note is for a person who does not write code. It is a record of what was opened, what was already listed, and why nothing was submitted.

Pay-to addresses below are public receive addresses. They are not passwords.

- Solana USDC: `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3`
- EVM: `0x9eb954b567ef3616424a6e1bf42c63724930aa54`

---

## What this sweep was allowed to do

- Look at Startup Buffer and BetaPage only.
- Send a listing **once** if the form did **not** ask for a login. If a login was required, send **nothing**.
- Scan the catalog for personal details and secrets. Do not publish those.
- Leave the HTML pages alone. No restack.
- Do **not** send again to Launching Next, FSL, or Tarkle.

---

## Bottom line

| Site | Can we list the catalog today without logging in? | Already listed? | Sent this sweep? |
| --- | --- | --- | --- |
| Startup Buffer | Form exists, but this sweep could not reach it (robot check). Public pages also say it asks for a contact email, city, and a screenshot. | No public hit found for this catalog. Site search was blocked by the same robot check. | **ZERO** |
| BetaPage | No. The old BetaPage address now sends you to PitchWall, and PitchWall makes you sign in before the free listing form. | No. Search for “Treasury tools” and `treasury-tools.surge.sh` both returned **No matching data**. | **ZERO** |

---

## Startup Buffer

- Home: https://startupbuffer.com/
- Submit page: https://startupbuffer.com/site/submit

On 2026-08-26 the submit page, the search page, and a guessed listing URL (`/startup/treasury-tools`) all stopped on a “verify you are human” screen. That screen never opened the real form, so nothing was typed and nothing was sent.

Public write-ups of that same form (including the site’s own FAQ) say you do **not** need an account. They also say you **must** fill:

- Startup name
- Website
- Business email
- One-sentence pitch
- Longer description (several sentences)
- Country and city
- A screenshot (under 500 KB)

A contact email and a person’s city are personal details. This sweep does not put those on a public listing. Even if the robot check had cleared, the email and city fields would have stopped a clean send.

Free vs paid: the site advertises a free submit plus paid “promote” plans. This sweep did not buy a plan.

If you later want this listing yourself: open https://startupbuffer.com/site/submit in your own browser, pass the human check, and fill the form. Use https://treasury-tools.surge.sh/ as the website. Do not send this sweep again from an automated browser.

---

## BetaPage (now PitchWall)

- Old address: https://betapage.co/
- Old submit addresses: https://betapage.co/product/submit and https://betapage.co/submit
- All of those opened **PitchWall** instead: https://pitchwall.co/ and https://pitchwall.co/submit

PitchWall still lets you **look** at plans while signed out. There is a **Free Launch** plan. Clicking **Select Plan** on Free Launch goes to a **Login** page:

https://pitchwall.co/auth/login?redirect=/product/submit?plan=free

Sign-in buttons on that page: Google, GitHub, Microsoft, Discord. There is also **Login** and **Register** in the top bar. Rule for this sweep: login required → **ZERO**. The form was not filled.

Search on PitchWall (2026-08-26):

- “Treasury tools” → No matching data
- `treasury-tools.surge.sh` → No matching data

Paid PitchWall plans ($49 / $99) were not used.

If you later want this listing yourself: sign in on PitchWall, pick Free Launch, and point it at https://treasury-tools.surge.sh/. This sweep will not do that login.

---

## Personal-details scan (catalog and pay page)

Opened https://treasury-tools.surge.sh/ and the live Solana Invoice page it bills through.

**Not found on the catalog page**

- No personal email
- No phone number
- No person’s name
- No home or street address
- No password, API key, or seed phrase

**Pay-to**

- Allowed Solana USDC and EVM addresses are listed at the top of this note.
- The live catalog page itself did not print those addresses on 2026-08-26. It tells visitors to pay USDC on Solana through the Solana Invoice page, and it already mentions a listing on [Twelve.tools](https://twelve.tools/).
- The live invoice config file does include the Solana USDC address above. That is a public receive address, not a secret.

Nothing in this note copies a personal inbox, a person’s city, or a login.

---

## What was not done

- No HTML files were edited.
- No second send to Launching Next, FSL, or Tarkle.
- No PitchWall account was created.
- No Startup Buffer form was submitted.
- No paid upgrade was bought.

---

## Copy you can paste later (no personal fields)

Use this only if **you** open one of the forms above.

**Name:** Treasury tools

**Website:** https://treasury-tools.surge.sh/

**One sentence:** Small one-file tools. Open them, use them, keep them. Billed in USDC on Solana.

**Longer text:** Treasury tools is a catalog of small one-file HTML tools. There is no account and no wallet on these pages. You open a tool, use it, and keep the file. Tools include an invoice page, a CSV cleaner, a form-to-email builder, and other one-page utilities. Billing is USDC on Solana only. Do not send other coins or other chains.

Leave email, name, and city blank in this repo. Fill those only in the live form if you choose to list.
