# Fiat storefronts for offline HTML tools

Checked **2026-08-25** against live official pages (HTTP status + help docs). No product listings were created. Scope: sell existing single-file HTML tools (Solana Invoice, CSV Cleaner, Form-to-Email, RSS-to-Webhook) for **fiat this week**, without Phantom, X-required signup, trading venues, or a fake identity.

**Hypothesis:** Payhip or Gumroad is the fastest fiat door. **Confirmed for the named four.** Both accept a free email signup today and let you publish a digital download after connecting a real PayPal or bank/Stripe payout. Lemon Squeezy is open but is **not** the fastest: new stores start in test mode and need a compliance review before live checkout.

## Currently open (this week)

| Storefront | Seller URL | Signup required | Payout currency | List one HTML file this week? |
|---|---|---|---|---|
| **Payhip** | [payhip.com](https://payhip.com/) · [register](https://payhip.com/auth/register) | Yes (free email; no card). Homepage 200, register 200. | Not held by Payhip. Stripe → bank in the Stripe account currency. PayPal → PayPal balance (100+ currencies / 200+ markets). | **Yes.** Digital Product upload; most types allowed (blocked: EXE, ISO, DMG, VBS, SCR, JAR). HTML is not blocked. ZIP if a host is picky. |
| **Gumroad** | [gumroad.com](https://gumroad.com/) · [signup](https://gumroad.com/signup) | Yes (email/password; social logins optional — X is not required). Homepage + signup 200. | Display currency is seller-chosen. Card charges settle in USD or the buyer’s local currency. **Bank payout = local currency** of a supported country. **PayPal-only countries = USD.** | **Yes.** Digital product Content tab accepts uploaded files. First **payout** is separate: $100 USD minimum (some countries higher) and a 1–3 week first-account review. |
| **itch.io** | [itch.io](https://itch.io/) · [tools catalog](https://itch.io/tools) · [payments docs](https://itch.io/docs/creators/payments) | Yes (free account). Homepage 200. `/register` is Cloudflare-challenged from this IP; docs + catalog are live. | **Collected by itch.io:** USD in, USD out (PayPal or Payoneer). **Direct to you:** seller-picked currency — PayPal USD/CAD/GBP/EUR/JPY/AUD; Stripe USD/CAD/EUR/GBP (US, CA, IE, UK). | **Yes.** Classification **Tools** is a first-class catalog (31,056 results today, including paid tools). Upload a downloadable `.html` / `.zip`, or HTML5 embed. Need Seller settings + PayPal/Stripe or itch payouts. |
| **Ko-fi Shop** | [ko-fi.com/shop](https://ko-fi.com/shop) · [shop help](https://help.ko-fi.com/hc/en-us/articles/360009712917-Ko-fi-Shop-Sell-digital-physical-products) · [payouts](https://help.ko-fi.com/hc/en-us/articles/115003980093-How-do-I-get-paid) | Yes (free creator page). Homepage Cloudflare-challenged from this IP; official shop/help docs are current. | Instant to connected **PayPal or Stripe** (processor currency). Page currency is seller-chosen (USD, EUR, GBP, and others listed in fee docs). | **Yes.** Shop item type “digital file”; upload or link the HTML. 5% Ko-fi fee on shop sales + processor fees. |
| **Polar** | [polar.sh](https://polar.sh/) · [signup](https://polar.sh/signup) → `/auth` 200 · [file downloads](https://polar.sh/docs/features/benefits/file-downloads) | Yes (GitHub, Google, or email; no card). | MoR. Balance settles in **USD**. Payout via Stripe Connect Express to a **same-country local-currency bank**. Wise/Revolut-style accounts usually fail. | **Yes, after payout account is connected.** Docs: Polar will not take live money until Stripe Connect is set up. File Downloads accept any file type (up to 10GB). |
| **Lemon Squeezy** | [lemonsqueezy.com](https://www.lemonsqueezy.com/) 200 · register → [auth signup](https://auth.lemonsqueezy.com/signup/business-intent) 200 | Yes (email/password or Google; Twitter optional — X is not required). No card to start. | Transactions processed in **USD**. PayPal payouts **USD**. Bank payouts USD, convertible to a chosen local currency at payout. $50 minimum; 1st/15th schedule. | **Draft this week; live checkout not guaranteed.** Official: new stores are test-mode until activation review, “typically 1–2 business days.” File upload is supported. Stripe is folding LS into Managed Payments; standalone signup is still open today. |
| **Sellfy** | [sellfy.com](https://sellfy.com/) 200 · [signup](https://sellfy.com/signup) | Yes. 14-day trial exists. | Instant to connected **PayPal or Stripe** (processor currency). | **Only after a paid plan.** Official help (updated 2026-07-22): checkout is **disabled** on the trial. Starter is **$39/mo**. Any digital file type once paid. Skip unless paying this week. |

## Fastest door this week

1. **Payhip** — free plan (5% + processor), email signup, upload HTML today, go live after connecting an existing PayPal or Stripe account. First Stripe/PayPal sale can sit pending a few days; the listing itself is immediate.
2. **Gumroad** — equally fast to **list**. Getting **paid** is slower ($100 floor + first-account review). Use if you already want a Gumroad permalink and can wait on the first payout.
3. **itch.io or Ko-fi** — same-week listing if you already have PayPal/Stripe. itch.io is a real tools marketplace, not only games.
4. **Polar** — same-week if Stripe Connect KYC finishes (real identity, domestic bank). Strong MoR; not faster than Payhip if you already have PayPal.
5. **Lemon Squeezy** — do not treat as this-week live checkout. Review gate plus $50 / twice-monthly payouts.

**Do not create fake storefront identities.** Every option above eventually needs a real legal name plus PayPal, Stripe, or bank KYC to receive money. That is ordinary payout verification, not a reason to skip the store.

## Checked and left out

- **Paddle** ([paddle.com](https://www.paddle.com/) 200) — live company site. New merchant onboarding is a sales/compliance process, not a same-day HTML download listing. Not verified as this-week.
- **Etsy** — marketplace exists; this environment got a bot-challenge 403, so seller-onboarding-this-week was **not** confirmed. Not listed as open here.
- **X-only, trading, or invented shops** — skipped as requested. No Phantom / crypto checkout researched.

## Sources (official, fetched 2026-08-25)

- Payhip homepage + `/auth/register` (200); [Add Digital Products](https://help.payhip.com/article/59-adding-a-digital-product) (updated 2026-03-17); [first product](https://help.payhip.com/article/164-how-to-sell-your-first-product-on-payhip); [Stripe](https://help.payhip.com/article/65-connecting-your-stripe-account); [PayPal](https://help.payhip.com/article/64-connecting-your-paypal-account)
- Gumroad homepage + `/signup` (200); [Adding a product](https://gumroad.com/help/article/149-adding-a-product); [Currency](https://gumroad.com/help/article/46-what-currency-does-gumroad-use); [Getting paid](https://gumroad.com/help/article/13-getting-paid)
- itch.io homepage + [tools](https://itch.io/tools) (200, 31,056 tools); [Getting started](https://itch.io/docs/creators/getting-started); [Payments](https://itch.io/docs/creators/payments)
- Ko-fi [Shop](https://ko-fi.com/shop); [Shop help](https://help.ko-fi.com/hc/en-us/articles/360009712917-Ko-fi-Shop-Sell-digital-physical-products); [How do I get paid](https://help.ko-fi.com/hc/en-us/articles/115003980093-How-do-I-get-paid)
- Polar homepage + `/signup`→`/auth` (200); [Introduction](https://polar.sh/docs/introduction); [File downloads](https://polar.sh/docs/features/benefits/file-downloads); [Payout accounts](https://polar.sh/docs/features/finance/accounts)
- Lemon Squeezy homepage (200); [Getting started](https://docs.lemonsqueezy.com/guides/getting-started); [Getting paid](https://docs.lemonsqueezy.com/help/getting-started/getting-paid); [Currencies](https://docs.lemonsqueezy.com/help/payments/currencies); [2026 Stripe update](https://www.lemonsqueezy.com/blog/2026-update)
- Sellfy homepage (200); [How much does Sellfy cost?](https://docs.sellfy.com/article/211-how-much-does-sellfy-cost) (updated 2026-07-22)
