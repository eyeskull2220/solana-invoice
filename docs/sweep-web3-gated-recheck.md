# Sweep: Layer3 / Bountycaster / Questbook gated recheck

**Date:** 2026-08-26 (UTC). Checks ran ~00:46–00:49 UTC.

**Boards:** Layer3, Bountycaster, Questbook only.

**Question:** Does a **non-gated, non-trading, non-X task** exist on those boards today?

**Answer: ZERO.** Nothing is listed as a match. Prior finding (all gated / trading) still holds.

Not an application. Nothing was submitted. No exploits. No X tasks. No invented listings.

---

## Filters (hard)

A listing is a match only if **all** of these are true on a primary source checked today:

| Filter | Meaning here |
|---|---|
| Task | A complete-today (or complete-this-week) work item with a published deliverable. Multi-month grant *proposals* are not tasks. |
| Non-gated | No wallet/XP/level/stake lock, no whitelist, no FID/power-badge, no KYC/screening, no “Sign in to apply.” |
| Non-trading | No swap, bridge, stake, PnL, volume race, lending, FX, token launch, or DeFi protocol usage as the work. |
| Non-X | Completion or posting must not go through Twitter/X. |
| Source | Official page or live UI. No aggregator copy. If a field is missing, this file says so. |

Anything that fails a filter is recorded as **seen, excluded**. Closed, empty, or unverifiable boards are not matches.

---

## Verdict

| Board | Live surface today | Matching tasks |
|---|---|---|
| Layer3 | Marketing site up. `app.layer3.xyz/quests` blocked (Cloudflare 403). Product docs describe Activations as onchain finance + optional X/social gates. | **0** |
| Bountycaster | Homepage Open filter: **No posts found**. FAQ: listings come from Farcaster or Twitter/X. | **0** |
| Questbook | Explore Grants loaded. Open rows exist; all are grant programs that require Sign in. Funded Open rows are DeFi, token-launch, or screening-gated. | **0** |

**Count claimed as a match: 0.**

---

## Layer3

### What was reachable

| URL | Result (2026-08-26) |
|---|---|
| https://layer3.xyz/ | HTTP 200. Marketing copy: “Discover, trade, stake, and earn.” Curated Activations = “onchain tasks.” Staking is a first-class product. |
| https://app.layer3.xyz/quests | HTTP 403 Cloudflare challenge / block (`Just a moment…` in the browser; Ray ID `a30ed0101b1d8e10` on an earlier fetch). **Today’s per-quest catalog could not be inventoried.** |
| Guessed JSON APIs (`api.layer3.xyz/quests`, `app.layer3.xyz/api/quests`) | 403 or no public list. |
| Official docs | Loaded. Used as the product contract for gating and trading. |

No public quest list API was found. This file does **not** invent individual quest titles from third-party blogs or from a June 2026 Dune scrape.

### Why nothing matches (from official docs)

Sources:

- https://layer3xyz.gitbook.io/layer3-updated-docs/platform/activations.md
- https://layer3xyz.gitbook.io/layer3-updated-docs/platform/getting-started.md
- https://layer3xyz.gitbook.io/layer3-updated-docs/platform/rewards-and-progression.md
- https://layer3xyz.gitbook.io/layer3-updated-docs/platform/cubes.md
- https://layer3xyz.gitbook.io/layer3-updated-docs/platform/competitions.md
- https://layer3xyz.gitbook.io/layer3-updated-docs/platform/trade-and-stake.md
- https://layer3xyz.gitbook.io/layer3-updated-docs/platform/explore-more.md
- https://layer3xyz.gitbook.io/layer3-updated-docs/builder/guides/guides--action-types-reference.md
- https://layer3xyz.gitbook.io/layer3-updated-docs/builder/guides/guides--managing-activation-access.md

Facts on those pages:

1. **Getting started is wallet-gated.** Sign in at `app.layer3.xyz` by connecting an EVM or Solana wallet.
2. **Activations are onchain finance.** Docs: “real actions on real protocols (**swaps, deposits, mints, bridges**)” verified onchain before reward. That is trading / protocol usage, not a non-trading task.
3. **Social / X steps are a first-class action type.** Activations may include “connect your X, Discord, or other accounts for community-gated steps.” Action types include `Social Connections` (Twitter, Discord, Telegram, Email, Github). X is excluded by the brief even when mixed with other steps.
4. **XP gates access.** “XP drives your Level … and access to **gated experiences**.” CUBEs “determine … which **gated Activations** you can enter.” Builder access types include whitelist CSV and private link-only Activations.
5. **Liquid Rewards / extra quests are stake-gated.** Rate tables require locked L3 (or League + smaller lock). Marketing and web-search snippets of `app.layer3.xyz/collections/quest-and-earn` still show **Level Locked** / **Stake Exclusive** labels; those pages were not independently readable here because of the 403.
6. **Competitions are trading contests.** Docs: “trading contests, volume races, and PnL battles.” Arena is “Telegram-native trading on Hyperliquid.” Excluded.
7. **CUBE mint is an onchain fee.** FAQ: minting writes to the chain and carries a network fee. Not a free ungated claim.

### Learn (not claimed)

Docs describe [Learn](https://app.layer3.xyz/learn) as “free, structured educational content.” That page was behind the same `app.layer3.xyz` 403, so today’s lesson list was **not** verified. Even if Learn is unpaid reading, Getting Started still requires a wallet, CUBEs still cost a mint fee, and docs say Learn “pairs naturally with live Activations.” That is not enough to claim a non-gated payable **task**. It is left unclaimed.

---

## Bountycaster

### Live UI (browser, 2026-08-26 ~00:46 UTC)

https://www.bountycaster.xyz/

- Lifetime stats on the page: **$1.5 million** posted, **2,967** bounties posted.
- Filter defaulted to **Open**.
- Result: **No posts found.**
- Trending / Beginner friendly / Highest value / Ending soon links did not surface a row in this session.

There is no open bounty to classify. Empty is not a match.

### Platform gates (FAQ, live)

https://www.bountycaster.xyz/faq  
https://www.bountycaster.xyz/start/bounty

- “We currently support **Farcaster and Twitter/X**.”
- “Bountycaster currently lists bounties that are published on Farcaster or Twitter/X. **Posting a bounty directly from this website is disabled.**”
- Who can **post**: Farcaster power badge **or** FID at/before **#20939**; Twitter/X **verified badge** (cap $1000 unless manually reviewed).
- How to **complete**: reply in the original Farcaster/X thread with proof. Payments are peer-to-peer (guided flow on Base USDC when used).

Any listing that appeared would fail **non-X** if it originated on X, and would fail **non-gated** because fulfillment is a Farcaster or X thread (power-badge / FID / verified-badge gates on the posting side; account required to reply). None appeared on Open today, so none are listed.

No exploit research. No X-task enumeration.

---

## Questbook

### Live UI (browser, 2026-08-26 ~00:47 UTC)

https://questbook.app/ — Explore Grants loaded after the featured-logo strip.

Every program card that accepts work uses **Sign in** / **Submit new**. That is gated. Grant programs are proposal + review + milestone payout, not same-day tasks.

### Open rows seen (excluded, not matches)

Recorded so the inventory is not silently incomplete. **None** of these are claimed.

| Program | UI status | Money shown on card | Why excluded |
|---|---|---|---|
| Fetch.AI **Agent Launch Flash Grants** | Open | **$177** left in multisig; $10k allocated / $10k paid; 5 accepted / 44 proposals | Sign in required. Token launchpad (Agent Launch graduates tokens to PancakeSwap). Opened program info: “grants related to the Agent Launch Flash Grants Ecosystem.” Recent proposals (25 Aug 2026) are multi-week milestones (example Equxi ask **2,500 USD**, deadline **25 Sep 2026**). Not a non-trading task. |
| Compound **Dapps and Ideas Domain** | Open | $70k available / $499k paid | Sign in. Compound is onchain lending. DeFi / trading-adjacent. Grant, not a task. |
| Compound **Security Tooling Domain** | Open | $6573 available / $143k paid | Sign in. Compound DeFi. Grant. |
| Compound **Multichain and Cross Chain Domain** | Open | $8903 available / $53k paid | Sign in. Compound DeFi. Grant. |
| Compound **DAO Expenses Domain** | Open | $12k available / $28k paid | Sign in. Compound DAO internals, not a public ungated task. |
| **Alchemix DAO** | Open | $9575 available / $119k paid | Sign in. Alchemix is DeFi yield. Trading-adjacent. Grant. |
| Axelar collectives (Researchers, Research Collective, Artist Collective, Community Contributors, Builders Collective, General/Admin/Technical Moderators, Developer Experience, Technical Integrations, Bounty Winners, Amplifier Advisory Committee, ARC Korea, …) | Many labeled Open | Several show **No multisig** and only historical “paid out”; some $0 paid / $0 accepted | Sign in. Not same-day tasks. Artist/moderator tracks are still grant membership, not ungated tasks. |
| **Shido** GameFi / AI / DeFi / Cross-Chain Grants (and siblings on the same strip) | Open | **No multisig**, **$0 paid**, **0 accepted** | Sign in. Unfunded on the card. DeFi/GameFi tracks fail non-trading even if they were funded. |
| **Circle 2026 Cohort 2** (https://circle.questbook.app/) | Open | $300k available; **$0 paid**; 3 accepted / **649** proposals | Sign in. Marketing: finalists “must complete applicable **screenings**.” About copy prioritizes **onchain lending, capital markets, FX**, agentic commerce, payments. Grant, gated, trading-adjacent. |
| Circle **2026 Cohort 1** | **Closed** | $300k available / $120k paid; 19 accepted | Closed. |

Circle marketing still points apply at https://www.circle.com/grant → https://circle.questbook.app/. Portal totals today: **668** proposals, **22** accepted, **$245k** allocated, **$120k** paid out. A prior 2026-08-25 check of this portal (in-repo `research/grants-this-week.md` on another branch) saw **$0 allocated**. Cohort 2 is now labeled Open with funds on the card, but it still fails the filters above. It is **not** a match.

### Closed (not matches)

Seen on the same Explore Grants page, among others:

- Polygon Community Grants - Direct Track (Closed; $0 paid; 179 proposals)
- Reclaim Builders (Closed)
- AI Research Grants : Proof.fun (Closed)
- Reclaim App Builders - India (Closed)
- Arbitrum New Protocols / Education / Developer Tooling / Gaming 3.0, Stylus Sprint, Orbit (Closed)
- Compound CGP 2.0 / Multichain / III Dev Tooling / III Security Tooling (Closed)
- **TON Grants** (Closed; $0 in multisig; $2M paid; 103 accepted / 2132 proposals)
- TON **Education & Resources Bounties** (Closed)
- TON **Developers & Community Tools Bounties** (Closed)
- ENS Public Goods Large Grants Q3 2024 (historical card; $1 available / $267k paid)

TON’s own bounty guidelines still send assigned GitHub issues to Questbook for payout. Those Questbook programs are **Closed** on the live board today.

Polygon’s own FAQ still says KYC is mandatory for received grants, and the last direct-grant date cited on https://polygon.questbook.xyz/ was **15 April 2025**. The live card is Closed.

---

## What was not done

- No wallet connect, no Sign in, no proposal submitted.
- No Layer3 Activation completed (app blocked; would have been trading/gated anyway).
- No Bountycaster reply (Open list empty; platform is Farcaster/X).
- No exploit, CTF, or unauthorized-access work.
- No Twitter/X tasks enumerated or recommended.
- Individual Layer3 quest titles were **not** guessed from Cloudflare-blocked HTML.

---

## Recheck later

If the bar is still “non-gated + non-trading + non-X **task** today,” re-hit:

1. https://app.layer3.xyz/quests and https://app.layer3.xyz/learn (need an unblocked client).
2. https://www.bountycaster.xyz/ with filter **Open**.
3. https://questbook.app/ Explore Grants + https://circle.questbook.app/ Open badges.

Until a listing clears every filter on a primary page, the honest count stays **zero**.
