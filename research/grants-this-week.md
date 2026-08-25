# Grants and RFPs a small team can apply to this week

**Checked:** 2026-08-25 (Tuesday). “This week” means 2026-08-25 through 2026-08-31.

**Method:** Official program pages and public APIs only. No aggregator copy, no invented amounts or deadlines. If a page did not state a field, this file says so.

**Filters:** Pay USD or USDC (not ETH, SOL, FIL-only, or project tokens). Not a token launch. Not a Superteam Earn bounty. Not a trading contest. Skip a program when KYC is the only stated path to get paid; note it.

---

## Verdict

**Hypothesis confirmed: nothing here pays this week.**

Several boards still accept applications this week (rolling). None of the official pages promise a decision or payout inside 2026-08-25–08-31. Typical clocks:

| Program | Official clock after you apply |
|---|---|
| Superteam regional grants | ~1 week average response, then KYC + payment form; Superteam FAQ says Superteam/Solana-sponsored payouts land within 7 days of that form |
| Solana Foundation standard/convertible grants | ~1 week review, then ~3 weeks to a decision, then a legal agreement |
| Filecoin Documentation Enhancement | Decision by the end of the month after you submit; pay only after signed contract + finished work + 30 days |
| Filecoin Open Grants | Preliminary review ~2 weeks, final decision ~4 weeks, then a contract |
| Ethereum Foundation ESP | 3–6 weeks; pays ETH by default; identity verification required |

**Main list below has one program** that is currently documented as open **and** officially pays USD or USDC. Everything else failed a filter or could not be verified as live.

---

## Currently open (USD or USDC)

### 1. Filecoin Documentation Enhancement Grants

| Field | Official source |
|---|---|
| Status | Documented as open on 2026-08-25. No closed banner on the program README. |
| Amount | Up to **$5,000 USD or USDC**, single payment after work is approved |
| Deadline | Rolling. Review decision “by the end of the month following the application submission date” (example: submit in August, notified by September 30) |
| Pay this week? | **No.** Pay happens after a signed agreement, completed work (including audience testing), Foundation approval, then **within 30 days** |
| Apply | Create a GitHub issue with the “Documentation Enhancement Grants” template: https://github.com/filecoin-project/devgrants/issues/new/choose |
| Docs | https://github.com/filecoin-project/devgrants/blob/master/Program%20Resources/Documentation%20Enhancement%20Grants%20README.md |
| Hub | https://fil.org/grants (points at the same GitHub repo) |
| Scope | Tutorials, developer guides, or interactive Filecoin docs. Dual-license / open-source. Finish within 3 months of signing. |
| KYC | Not labeled “KYC-only.” Selected applicants “need to provide additional information during the contracting and invoicing process.” |
| Fit | Small team can apply. Work must be Filecoin documentation, not a generic product. |

Filecoin’s main README also still advertises **Open Grants** (up to $50,000) and **FIL Builder Next Step Grants** ($5k–$10k). Those pages quote dollar budgets but **do not say the payout is USD or USDC**, so they are not in this list. Filecoin RFPs are not open: the official README says `OPEN RFPs: Stay tuned!` and the GitHub `label:RFP is:open` search returned **0** issues on 2026-08-25. FIL-ProPGF Batch 3 closed 2026-06-16.

---

## Checked, not listed

### Solana Foundation — standard and convertible grants

- **Page:** https://solana.org/grants-funding
- **Apply (form loaded 200):** https://share.hsforms.com/1GE1hYdApQGaDiCgaiWMXHA5lohw
- **RFP board:** https://airtable.com/apppDmK2Pin9WX8jV/shrR0uMKu4N57TGW7/tbli2ERM3sdhyHJYB (and apply-to-an-RFP share: https://airtable.com/apppDmK2Pin9WX8jV/shrDbfJ1wktQ7pB6f/tbli2ERM3sdhyHJYB)
- **Status:** Rolling. Official copy: “Anyone can apply” (individuals, teams, companies, universities).
- **Clock:** Application review ~1 week; decision and contact ~3 weeks; then Solana Foundation Legal finalizes an agreement.
- **Why not listed:** Official page **does not state USD or USDC**. Amount is applicant-proposed; no published cheque size. The Airtable RFP grid did not yield readable row data in this environment, so **no individual Foundation RFPs are claimed here**.
- **Too slow for this week:** Yes. Even a fast review still hits legal after the ~3-week decision window.

### Superteam grants (Grant listings, not Earn bounties)

Solana Foundation’s own funding page still points Superteam microgrants at Earn: https://earn.superteam.fun/grants/

Public API `GET https://superteam.fun/api/grants` returned 46 grant records on 2026-08-25. Individual listing pages were fetched to confirm **Open** vs **Applications Paused** vs **Closed**.

**Currency:** Almost every live Superteam grant is denominated **USDG**, not USDC. Superteam FAQ: Superteam / Solana-sponsored listings require **KYC to receive money**, then a payment form, then payout within 7 days of that form (https://docs.superteam.fun/the-superteam-handbook/community/faqs/superteam-earn-faq). That is a KYC-only payout path → **skipped from the main list**.

**The one USDC Superteam grant is not cash.** [Startup Accelerator Grant](https://superteam.fun/earn/grants/startup-accelerator-grant/) (DD.xyz / Webacy) shows **Open / Global / up to 10k USDC / 72h** but the API description is “up to $10,000 in DD.xyz **API credits**.” Recipients: 0. Not a USD/USDC cash grant.

**Agentic Engineering Grants** (global, Open): https://superteam.fun/earn/grants/agentic-engineering/ — **200 USDG**, 50% upfront / 50% on ship, ~1 week response, Superteam-sponsored → KYC to get paid.

**Touching Grass** regional funds (up to 500 USDG): marked Open but “You need to be a Superteam member to be able to apply.” Not a general small-team path.

**Solana Foundation regional grants on Superteam Earn** (up to 10k USDG, rolling, Apply Now on 2026-08-25 unless noted). Apply on the listing after a Superteam Earn talent profile. Regional only.

| Listing | Region | Response shown | URL |
|---|---|---|---|
| Solana Foundation USA Grants | United States | 1 week / avg grant $8,307 | https://superteam.fun/earn/grants/solana-foundation-usa-grants/ |
| Solana Foundation UK Grants | United Kingdom | 1 week / $4,613 | https://superteam.fun/earn/grants/solana-foundation-uk-grants/ |
| Solana Foundation Japan Grants | Japan | 1 week / $2,700 | https://superteam.fun/earn/grants/solana-foundation-japan-grants/ |
| Solana Foundation Brazil Grants | Brazil | 1 week / $5,518 | https://superteam.fun/earn/grants/solana-foundation-brazil-grants/ |
| Solana Foundation Turkey Grants | Turkey | 1 week / $3,452 | https://superteam.fun/earn/grants/solana-foundation-turkey-grants/ |
| Solana Foundation Korea Grants | South Korea | 1 week / $1,700 | https://superteam.fun/earn/grants/korea-grants/ |
| Solana Foundation Ireland Grants | Ireland | 1 week / $7,055 | https://superteam.fun/earn/grants/solana-foundation-ireland-grants/ |
| Solana Foundation Georgia Grants | Georgia | 1 week / $7,969 | https://superteam.fun/earn/grants/solana-foundation-georgia-grants/ |
| Solana Foundation Netherlands Grants | Netherlands | 1 week / $5,667 | https://superteam.fun/earn/grants/solana-foundation-netherlands-grants/ |
| Solana Foundation Singapore Grants | Singapore | 1 week / $9,450 | https://superteam.fun/earn/grants/solana-foundation-sg-grants/ |
| Solana Foundation Kazakhstan Grants | Kazakhstan | 1 week / $4,517 | https://superteam.fun/earn/grants/solana-foundation-kazakhstan-grants/ |
| Solana Foundation Canada Grants | Canada | 1 week / $5,586 | https://superteam.fun/earn/grants/solana-foundation-canada-grants/ |
| Solana Foundation Germany Grants | Germany | 1 week / $5,130 | https://superteam.fun/earn/grants/solana-foundation-germany-grants/ |
| Solana Foundation UAE Grants | United Arab Emirates | 1 month / $10,000 | https://superteam.fun/earn/grants/solana-foundation-UAE-grants/ |
| Solana Foundation Malaysia Grants | Malaysia | 1 week / $5,081 | https://superteam.fun/earn/grants/solana-foundation-malaysia-grants/ |
| Solana Foundation Balkan Grants | Balkan | 30 days / $3,331 | https://superteam.fun/earn/grants/solana-foundation-balkan-grants/ |
| Solana Foundation Poland Grants | Poland | 1 week / $6,317 | https://superteam.fun/earn/grants/Poland-grants/ |
| Solana Foundation Australia Grants | Australia | 1 week / $10,000 | https://superteam.fun/earn/grants/australia-grants/ |
| Solana Foundation Ukraine Grants | Ukraine | 1 week / $3,440 | https://superteam.fun/earn/grants/solana-foundation-ukraine-grants/ |
| La Familia Spain Grants | Spain | 1 week / $4,552 | https://superteam.fun/earn/grants/spain-grants/ |

USA listing copy (API): $1–$10,000; Foundation “hands out these grants typically once a month.”

**Paused (not apply-now):** [India](https://superteam.fun/earn/grants/solana-foundation-india-grants/), [Nigeria](https://superteam.fun/earn/grants/solana-foundation-nigeria-grants/) — pages say **Applications Paused**.

**Closed:** [ALLMIGHT Microgrants](https://superteam.fun/earn/grants/allmight-microgrants/) — **Closed**.

### Ethereum Foundation ESP

- Overview: https://esp.ethereum.foundation/applicants
- Wishlist: https://esp.ethereum.foundation/applicants/wishlist — **“There are currently no active wishlists available for application.”**
- Open rounds: https://esp.ethereum.foundation/applicants/open-rounds — **“There are no active grant rounds at this time.”**
- RFPs: https://esp.ethereum.foundation/applicants/rfp — two **Road to Devcon 8 India** items (Ecosystem up to **$300 USD** in support; University program, amount not stated on the listing). Official apply copy: **paid on-chain in ETH by default**. Recipients must complete **identity verification** and a grant letter.
- **Why not listed:** Pays ETH, not USD/USDC. KYC/identity verification is required. Wishlist and open rounds are empty.

### Circle Developer Grants

- Marketing: https://www.circle.com/grant — FAQ still says **$5,000–$100,000 in USDC**, milestone-based, apply via https://circle.questbook.app/
- Process includes “Finalists selected to proceed must complete applicable screenings.”
- **Questbook dashboard on 2026-08-25:** 0 proposals, 0 accepted, **$0k funds allocated, $0k paid out**.
- **Why not listed:** Official marketing still says apply; the live portal shows **no allocated funds**. That is not a confirmed paid-open program.

### Uniswap Foundation

- https://www.uniswapfoundation.org/grants and https://www.uniswapfoundation.org/grantee-toolkit
- Toolkit: **“We KYC all grantees.”** That is a KYC-only path → skipped.
- UFSF May 2026 cohort deadline was **2026-05-07** (closed).

### Other boards checked the same day

| Board | Result on 2026-08-25 |
|---|---|
| Web3 Foundation Grants | **Discontinued.** Repo banner: not accepting new applications. https://github.com/w3f/Grants-Program |
| Optimism Grants Council Season 9 | Applications closed **2026-05-20**. https://www.opgrants.io/seasons/current/season-9/ |
| Filecoin ProPGF Batch 3 | Final deadline **2026-06-16**. https://filpgf.io/propgf/ |
| Filecoin Open RFPs | **None.** https://github.com/filecoin-project/devgrants README: “Stay tuned!” |
| Base Builder Grants | Retroactive, **ETH**, no open application form. |
| Octant | Pays **ETH**; last cited epoch window ended **2026-06-30**. |
| Gitcoin RFP explainer | Mechanism page, not a live USD/USDC RFP board. https://gitcoin.co/mechanisms/requests-for-proposals |

---

## What a small team can actually do this week

1. **Apply now, get paid later (USD/USDC confirmed):** Filecoin Documentation Enhancement Grant — only if you will write Filecoin docs.
2. **Apply now, currency/KYC fail the brief:** Superteam regional grants (USDG + KYC) or Solana Foundation HubSpot form (currency unstated, weeks of legal).
3. **Do not expect a wallet credit before 2026-09-01** from any program above.

If the bar is “submit this week **and** receive USD/USDC this week,” the honest count is **zero**.
