# CEO RESEARCH — SovereignForge as one Belgian income machine

**Date:** 2026-08-27  
**Seat:** CEO  
**Mode:** adversarial first, then RGY  
**Start:** 0  
**Success (only):** money in operator accounts **and** a shop a secretaris forwards  
**This turn:** no mail, no spend, no Phantom send, no Kraken live, no fake KBO  

This file is research. It is not a punch-list, not a seventh seat, and not shop HTML.

---

## 0. Start from 0

SovereignForge is **one** income machine for **one** operator in Geel, Belgium (Sasha De Vree / `eyeskull2220`). It is not a company with a floor of engineers. It is not a trading-desk product company. It is not this git repository.

What is **not** the machine (do not count as progress):

| Object | What it actually is | Why it is not the machine |
|---|---|---|
| `eyeskull2220/solana-invoice` (this checkout) | Leftover English invoice HTML + catalog. Paywall honors unlock on RPC failure. | Live shop is [sovereignforge.surge.sh](https://sovereignforge.surge.sh/). This repo is residue. |
| Linear team "SovereignForge" | One human + two bots. Issues name a fake org. | Headcount is 1. Roles are labels. |
| `SovereignForgeV1` (~646 MB, Bybit OFG-DCA) | Personal trading bot + Tauri terminal. Soft-launch still Backlog. Belgian tax memo **canceled**. | No proven fills that put euros in the operator account. Not the shop. |
| `SovereignForgeGrokbot` | Desktop trading app fork. Open PRs on MON-LOOP peels and a ccxt `gate` rename. | Same class as V1. Not Sell. |
| 100+ Ultra PRs into this leftover repo on 2026-08-26/27 | Agent swarm writing kits, playbooks, privacy pages, "EUR-first" shops, FIX boards. | PRs against leftover HTML do not move the live host. |

What **is** the machine, from zero:

1. **Sell** — a Dutch OFFERTE shop a club/vzw secretaris can forward tonight, that can take USDC into an address the operator controls.
2. **Paper** — Kraken paper only, until the invert gate is actually met (not narrated).
3. **Rails** — legal + payment identity that does not invent a KBO and does not enroll the operator as a freelancer.
4. **Capabilities** — what this agent stack can do **without** mailing, spending, or sending.

If a lane does not put money in or make a page forwardable, it is theater.

---

## 1. Adversarial (read this before any GREEN)

### 1.1 The shop does not convert. The pay address is empty.

Live shop pay address (printed on [betalen.html](https://sovereignforge.surge.sh/betalen.html) and in this leftover repo):

`96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3`

Solana mainnet probe 2026-08-27 (public RPC):

- `getSignaturesForAddress` → **[]**
- `getTokenAccountsByOwner` for USDC mint `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v` → **[]**
- `getBalance` (SOL) → **0**

No USDC token account has ever been created. No SOL to pay rent. **Zero inbound.** Success criterion 1 (money in operator accounts) is false on the only public pay rail the shop publishes.

### 1.2 A secretaris cannot pay this, so the board cannot approve it.

Shop copy is aimed at "de secretaris die vanavond nog een voorstel naar het bestuur stuurt." That sentence is the right buyer. The checkout is the kill:

- Charge is **USDC on Solana only**. No IBAN, no kaart, no Bancontact, no cash.
- Footer: **KBO/BTW: nog niet toegekend**. Privacy: natuurlijke persoon, geen vennootschap, geen ondernemingsnummer.
- Every SKU is stamped **geen BTW-factuur (OFFERTE)**.
- Club kit is **900 USDC (~€774 at Kraken USDCEUR 0.8587, 27 Aug 2026, not a FOD rate)**.

A Geel vzw bestuur that forwards this is being asked to send ~€774 of crypto to a nameless Solana key with no invoice. That is not how a secretaris spends club money. **The page can be forwarded as a demo. The offer cannot be executed by the buyer it names.**

### 1.3 The maatstaf is a fake club.

Hero maatstaf: "ZWV De Golfbreker." The live demo ([club-site-kit-treasury.surge.sh](https://club-site-kit-treasury.surge.sh/)) says in the title and banner: **verzonnen zwemclub**, **geen echte vzw**, example.com mail, no address, no ondernemingsnummer. A secretaris who opens "het voorbeeld" learns the reference club does not exist. That is the opposite of "zo ziet een clubsite eruit die je vanavond kunt doorsturen."

### 1.4 Search cannot find the shop.

`https://sovereignforge.surge.sh/robots.txt`:

```
User-agent: *
Disallow: /
```

No organic discovery. No cookiebanner (good). Also no way a secretaris Googles "clubsites Geel" and lands here. Forwarding is the only distribution. Nothing has been forwarded that produced a payment (see 1.1).

### 1.5 This leftover repo is a trap for agents.

`index.html` here is still English "Solana Invoice — 9 USDC" with an unlock that **downloads the product when RPC verification fails** (`honorUnlock` on catch). `catalog.html` points at `treasury-tools.surge.sh` and English 9/49 USDC tools. README still says "Treasury tools."

The live SKU "Eén klus" on shop is 49 USDC / ±€42 and the live `solana-invoice-treasury.surge.sh` title is already `Eén klus — €49 · OFFERTE`. **This git tree is not that host.** Editing this repo as if it were the shop is how you get 100 open PRs and zero USDC.

### 1.6 The trading bot is not an income machine.

`SovereignForgeV1` README: one operator, Bybit USDC alts, OFG-DCA, drawdown is the strategy, halt never sells. Linear:

- **SOV-55** G32 Belgian tax classification + accountant sig — **Canceled**
- **SOV-63** G40 five pre-live gates with $300 — **Canceled**
- **SOV-78** soft launch 2026-10-10, $100–$300 MICRO — **Backlog**, blocked by SOV-77 soak GNG
- Safety policy: drawdown / daily-loss / inversion are **alert-only** (they never halt)

That is a bag-holder executor with a canceled tax memo. It does not satisfy "money in operator accounts." It is also **Bybit**, not the Kraken paper lock below. Do not revive it as lane Paper.

### 1.7 The team layout is fake. Treat it as BAD. (see §2)

### 1.8 Phantom send would be a lock break. Kraken live would be a lock break. Mail would be a lock break. Inventing a KBO would be a lock break.

This session: Phantom MCP `wallet_addresses` / `wallet_balances` **timed out**. Kraken MCP **failed tool discovery**. Gmail was not used. No KBO was written. Those are constraints, not TODOs for this file.

### 1.9 Selling Peppol kits while unable to issue a Belgian invoice is a joke the buyer will notice.

Pakketten include "Peppol Client-Chase" (399 USDC) and "Peppol Ready" (249 USDC). Footer: **geen Peppol Access Point**. Seller cannot Peppol. Seller cannot FACTUUR. Seller is teaching B2B PDF→Peppol while charging USDC on Solana. Adversarial read: the SKU exists to look like a KMO product line, not because a Kempen boekhouder can buy it.

---

## 2. Team layout — verdict: BAD

**Verdict: BAD.** Not "needs a shuffle." Bad as in: the org chart is the main way the machine avoids selling.

### Facts (not roles)

Linear workspace [SovereignForge](https://linear.app/sovereignforge), one team, users:

| Linear user | What they are |
|---|---|
| Sasha De Vree (`eyeskull2220@gmail.com`) | **Only human.** Admin. Operator. |
| Cursor OAuth app | Agent identity, last seen 2026-08-12 |
| Linear app user | Workspace bot |

Issue bodies still assign **Manager / Working** seats that have no Linear users: Release Manager, Orchestrator, QA Engineer, OFG Core, Risk Halt, Release Ops, Terminal Frontend, Chaos Engineer, Platform Engineer, CTO, Kind-A. Assignees are always Sasha with the note "agents named here; no Linear seats."

GitHub this afternoon: a **seat factory** dumping PRs into leftover `solana-invoice` — CEO, BUILDER, REVIEWER, SCOUT, COMPLIANCE, CODER, FIX, DESIGN, WALLET, plus kit HTML. That is a seventh-seat explosion on a repo the shop does not live in.

### Why it is bad for an income machine

1. **One operator cannot staff a Release Manager.** Every "Manager:" line is the same person talking to a model.
2. **Roles multiply work that cannot ship.** SOV-71…78 are week-slices on a Grokbot monolith. None of them are "secretaris forwards" or "USDC arrived."
3. **Canceled operator-only gates** (tax memo, $300 walk, DR drill) show the org can mark G1–G47 Done in a day and cancel the only items that touch Belgian money.
4. **This leftover repo is being used as a shared whiteboard** because it is the public checkout agents can push to. That is not a team. That is a collision.

### The only layout that matches the machine

| Seat | Job | Not |
|---|---|---|
| **Operator (human)** | Keys, PIN, capital, GNG, mail, KBO decision, live Kraken if-and-only-if invert gate | Freelancer invoice to himself |
| **CEO research (this file)** | Kill theater; name RED | Another org chart |
| **Sell** | Live host `sovereignforge.surge.sh` only | PRs to leftover HTML |
| **Paper** | Kraken invert-paper until gate | Bybit live, Grokbot ARM |
| **Rails** | True KBO or none; Phantom receive-only | Invented BE0… numbers |
| **Capabilities** | Tools that work without spend/mail | Seat factory |

Six named functions, one human. No Reviewer/Planner/Web/Design factory. Agents may write; they do not become a team.

---

## 3. Hard locks (non-negotiable)

These are locks, not backlog.

| Lock | Meaning | Observed 2026-08-27 |
|---|---|---|
| **Operator, not freelancer** | Do not enroll Sasha as zelfstandige / bijberoep to "make the shop legal." Do not invoice as a contractor to a paper company. | Privacy already: natuurlijke persoon, geen vennootschap. Keep it. |
| **No fake KBO** | Do not print a BE number, vestiging, or Peppol participant ID that FOD/KBO cannot show. Footer "nog niet toegekend" is the honest state. | Shop footer and privacy match. Do not "fix" this with a made-up number. |
| **Phantom receive-only** | Read addresses/balances. No `transfer`, no swap, no perps, no rebalance. | Addresses/balances timed out this run. **Did not send.** |
| **Kraken paper until invert gate** | Stay on `kraken paper` / `kraken futures paper` (invert). Live is forbidden until **all three** are true on invert-paper: **return > 0 after fees** AND **≥ 8 fills** AND **maxDD ≤ 8%**. | Kraken MCP down. No paper journal in *this* tree on `main`. **Did not live-trade. Did not spend.** |
| **No mail this turn** | Do not Gmail-send, do not mailto blast, do not "just introduce." | Not used. |
| **No spend this turn** | No USDC, no SOL, no Kraken live, no ads. | Not used. |

**Legal tension (do not paper over):** Belgian KBO rules require registration before a natuurlijke persoon **habitually** exercises an independent economic activity. A working club-site product line would be that activity. The lock is: **do not fake the number and do not freelancer-register to dodge it.** Until a real KBO exists, Sell stays OFFERTE, not FACTUUR, and volume must stay non-habitual. That is a ceiling, not a loophole.

---

## 4. Four lanes — RED / YELLOW / GREEN

Scoring: **RED** = blocks success; **YELLOW** = real but not success; **GREEN** = actually moves money-in or forwardable shop. Notes sit under each cell.

### 4.1 Sell

**RGY: RED**

| Item | Color | Notes |
|---|---|---|
| Live host exists | YELLOW | [sovereignforge.surge.sh](https://sovereignforge.surge.sh/) is a Dutch catalog. 11 SKUs. Secretaris-shaped H1. That is more shop than this repo. It is not a sale. |
| Forwardable tonight | YELLOW | Static HTML, NL, Geel, screenshots. A secretaris *could* mail the URL. `robots.txt` Disallow and fake Golfbreker demo cut the chance. |
| Board-executable offer | RED | USDC-only, no IBAN, no FACTUUR, no KBO. 900 USDC club kit is unpayable by a vzw treasurer. |
| Money in | RED | Pay address: 0 signatures, 0 USDC ATA, 0 SOL. |
| This git repo as shop | RED | Leftover English 9 USDC invoice. Honor-unlock on RPC fail. Not the live host. |
| SKU count (11) | RED as progress | More SKUs without a first inbound is a catalog, not a machine. Peppol SKUs are worse (see 1.9). |

**Sell notes**

- Do not merge Ultra PRs that rewrite shop HTML **in this leftover repo** and call that a deploy. Deploy is the Surge host.
- Do not add IBAN/Bancontact this turn (spend/rails). Do not add a fake KBO to "look serious."
- The only Sell proof that counts: a secretaris-forwarded URL **and** a USDC credit on the printed address (or a later operator-owned receive address that is actually published).

### 4.2 Paper

**RGY: RED**

| Item | Color | Notes |
|---|---|---|
| Invert gate definition | GREEN | Clear: return>0 after fees ∧ fills≥8 ∧ maxDD≤8% on invert-paper. Do not soften. |
| Gate met | RED | No evidence in this checkout. Kraken MCP unavailable. Did not run a paper session (would be allowed; was not the job of this file). |
| Kraken live | RED (locked off) | Forbidden until gate. |
| Bybit / Grokbot / OFG-DCA as Paper | RED | Wrong venue, canceled tax gate, alert-only drawdown. Start from 0 = do not carry it. |
| Paper vs success | RED | Paper cannot put money in operator accounts. It can only *unlock later* live. Until gate, Paper is a brake, not an engine. |

**Paper notes**

- Kraken CLI paper needs **no auth and no spend**. That is the allowed experiment. This research did not run it.
- Invert-paper = Kraken inverse (and/or the named invert strategy) **on paper**. Not "we inverted a dashboard flag."
- After-fees is mandatory. Kraken spot paper already applies 0.26% taker. A strategy that only looks green before fees is a fail.
- ≥8 fills blocks one-lucky-print theater. maxDD≤8% blocks the old OFG thesis ("drawdown is the strategy").

### 4.3 Rails

**RGY: RED** (honest identity is YELLOW; usable rails are RED)

| Item | Color | Notes |
|---|---|---|
| No fake KBO on live shop | YELLOW | Footer + privacy tell the truth. That is compliance hygiene, not a rail a secretaris can pay. |
| Operator ≠ freelancer | YELLOW | Lock held. Also means there is **no** lawful habitual invoicing path until a real KBO decision (operator-only, not this agent). |
| Pay rail | RED | Solana USDC to an unused key. Buyer must already have USDC. Shop refuses card/IBAN. |
| Phantom receive-only | YELLOW | Lock held (no send). Wallet read **timed out** — cannot even confirm the printed address is the Phantom account. |
| Identity vs shop | RED | Published receive key has never been funded, so it may be a generated treasury string, not a wallet the operator opens daily. Untested. |
| Belgian tax / DAC8 / FIFO bot | RED | SOV-55 canceled. Bot ledger ≠ FOD. Irrelevant until there is income. |
| Peppol | RED | Not an Access Point. Selling Peppol kits is not a rail. |

**Rails notes**

- A real KBO is an **operator** act (ondernemingsloket, social-insurance fund, possible BTW). Agents must not "help" by inventing one.
- Until that act, keep OFFERTE language. Do not ship FACTUUR modules.
- Receive-only Phantom is the inbound crypto rail **if** the shop address matches a wallet the operator actually holds. That match was not proven this run.

### 4.4 Capabilities

**RGY: YELLOW** (tools exist; they are pointed at the wrong object)

| Item | Color | Notes |
|---|---|---|
| Cursor cloud agents | YELLOW | Can write. This afternoon they wrote **into leftover HTML**. Capability without aim is a cost. |
| Linear | YELLOW | Readable. Org chart is fiction. Useful as a museum of what not to staff. |
| GitHub | YELLOW | Three repos. Public leftover repo is the only easy PR surface — hence the swarm. |
| Live shop HTTP | GREEN as a probe | Shop, pakketten, betalen, contact, privacy, kits, robots.txt all fetched. Enough to score Sell without deploying. |
| On-chain read | GREEN as a probe | Empty treasury is a fact, not a vibe. |
| Phantom MCP | RED this run | Timeouts. Receive-only still holds because nothing was sent. |
| Kraken MCP | RED this run | Discovery failed. Paper CLI may still work locally; not used. |
| Gmail | GREEN as a lock | Exists. **Must not send.** Capability to mail is a temptation, not a lane. |
| eToro / Bybit bot stack | RED for this machine | Wrong product. Start from 0. |

**Capabilities notes**

- Allowed this seat: read, write research in git, open a PR, probe public HTTP and chain.
- Forbidden: mail, spend, Phantom transfer, Kraken live, fake KBO, claiming leftover PRs are shop deploys.

---

## 5. Scoreboard vs success

| Success test | Result | Color |
|---|---|---|
| Money in operator accounts | 0 USDC / 0 SOL / 0 signatures on the shop address | **RED** |
| Shop a secretaris forwards | Live Dutch shop exists; demo is fake; robots Disallow; offer is unpayable by a vzw | **RED** (page YELLOW, deal RED) |
| One machine, four lanes | Lanes named. Team layout still fights them. | **RED** until seats collapse |
| Hard locks held this turn | Yes: no mail, no spend, no fake KBO, no freelancer enroll, no Phantom send, no Kraken live | **GREEN** (locks only) |

**Machine RGY: RED.** Locks held is not income.

---

## 6. What would flip a cell (not a plan, not mail, not spend)

These are **tests**, not a sprint board. None of them are authorized as work in this file.

- **Sell → YELLOW:** shop address shows ≥1 real USDC inbound **or** a documented secretaris forward (screenshot/thread) without this agent mailing. Still not GREEN until both.
- **Sell → GREEN:** both success tests true.
- **Paper → YELLOW:** invert-paper journal with the three numbers printed from Kraken paper (not a screenshot of a dashboard).
- **Paper → GREEN:** gate met; still no live until operator GNG. GREEN on Paper means "gate passed," not "money in."
- **Rails → YELLOW:** Phantom receive address **read** and shown equal to the shop print (or shop updated to the real receive address by the operator). Still no send.
- **Rails → GREEN:** requires a real KBO **or** an operator decision that habitual Sell is refused. Agents cannot GREEN this.
- **Capabilities → GREEN:** Phantom read works, Kraken paper CLI works, agents stop opening shop PRs against leftover HTML.

---

## 7. Evidence log (this run)

| Probe | Result |
|---|---|
| `https://sovereignforge.surge.sh/` | Dutch shop, secretaris H1, 4 featured kits, 11 on pakketten |
| `/pakketten.html` `/betalen.html` `/contact.html` `/privacy.html` | 200. USDC charge, euro as omrekening, KBO not assigned, Gmail only |
| `/robots.txt` | `Disallow: /` |
| `/club.html` | 404 ("shop zit op home en pakketten") |
| Club demo | Fake ZWV De Golfbreker, Geel, NL |
| Kraken public `USDCEUR` | last 0.8587 (shop ≈ €0,86 is in-range, not FOD) |
| Solana pay address | empty (sigs/ATA/SOL) |
| This repo `main` | `2170952` leftover treasury HTML; no `docs/` on main |
| Linear users | 1 human (Sasha), Cursor OAuth, Linear bot |
| Linear SOV-55 / 63 / 78 | tax canceled; $300 walk canceled; soft launch backlog |
| GitHub repos | `solana-invoice` public leftover; `SovereignForgeV1` private bot; `SovereignForgeGrokbot` private fork |
| Phantom MCP | timeout (no send attempted) |
| Kraken MCP | discovery error (no live attempted) |
| Gmail | not called |

---

## 8. CEO close

The leftover invoice repo is full of agents. The live shop is a Dutch catalog on Surge that nobody has paid. The Linear org is a costume. The trading bot is a second machine that has not been allowed to be first.

From 0, SovereignForge is: **one operator, four lanes, two success tests.** Today both tests fail. Team layout is **BAD**. Locks held. Do not mail. Do not spend. Do not invent a KBO. Do not touch Kraken live. Do not send on Phantom.

Next writing that matters is not another seat. It is a fact that USDC arrived, or a fact that a real secretaris forwarded the live URL — neither of which this file can produce.
