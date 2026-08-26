# PII / secrets scan — all open PRs

**Overall: 2 FAIL, 50 PASS** (52 open PRs)

| | |
|---|---|
| Repo | [eyeskull2220/solana-invoice](https://github.com/eyeskull2220/solana-invoice) |
| Snapshot | 2026-08-26 00:55 UTC |
| Base | `main` @ `2170952` |
| Scope | Every **open** pull request at snapshot (draft + ready). Diffs, added files, and PR description bodies. |
| Not scanned | Closed/merged PRs (#1, #10, #26, #27, #30). PRs opened after this snapshot. |
| Merge | **Do not merge** this report PR as a substitute for remediating FAIL findings. |

## What was flagged

A PR **FAIL**s if any of these appear as a real value (not a placeholder, prefix example, or public protocol id):

| Class | Examples |
|---|---|
| Keys | PEM/PKCS8 private keys, Solana secret-key byte arrays, 64-byte hex private keys, 87–88 char base58 secret keys |
| Seeds | BIP-39 mnemonics, “seed phrase” / “recovery phrase” with adjacent word lists |
| Tokens | GitHub (`ghp_` / `github_pat_`), Slack, Stripe live/test secrets, AWS `AKIA…`, OpenAI/Anthropic, Hugging Face, Telegram bot tokens, JWTs, Discord webhooks |
| Passwords | `password=` / `passwd=` assignments with a real secret |
| Phone | Personal or copied-out telephone numbers |
| Home address | Street-level postal addresses |
| Leaked `.env` | `.env` / `.env.*` files in the diff |
| Extra pay-to | This project’s receive address set to something other than the allowlist below |

A PR **PASS**es if none of those are present. Public business emails, RFC 2606 `.example` placeholders, public GitHub/Reddit handles, and on-chain program/mint ids are **not** FAILs.

## Allowlist (not findings)

These receive addresses are expected and are **not** secrets:

| Chain | Address |
|---|---|
| Solana | `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3` |
| Ethereum / EVM | `0x9eb954b567ef3616424a6e1bf42c63724930aa54` |

Circle USDC on Solana mainnet (`EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v`) is a public mint id, not a wallet. It appears in many tool PRs next to the allowlisted Solana pay-to. **Not flagged.**

## Method

1. Listed open PRs with `gh pr list --state open`.
2. Pulled each `gh pr diff` and PR body.
3. Regex + manual review for the classes above.
4. Discarded false positives: FNV hash `2166136261`, Greenhouse job ids, Cursor agent UUIDs, “Circle” (USDC issuer) vs street “Circle”, USDC mint, Solana **transaction signatures** (64-byte base58, same length as a secret key but used as `const SIG` fixtures), token-prefix examples in scan writeups (`sk_live_`, `ghp_`, … with no payload).

No `.env` files, PEM keys, mnemonics, password values, phone numbers, or street addresses were found in any open PR at snapshot.

## Summary

| Verdict | PRs |
|---|---|
| **FAIL** | [#2](https://github.com/eyeskull2220/solana-invoice/pull/2), [#56](https://github.com/eyeskull2220/solana-invoice/pull/56) |
| **PASS** | #3–#9, #11–#25, #28–#29, #31–#55, #57 (50 PRs) |

## FAIL details

Values below are redacted. See the cited files on the PR for the full string.

### PR #2 — FAIL

- **Title:** Listing research: 3 places we can submit this week
- **URL:** https://github.com/eyeskull2220/solana-invoice/pull/2
- **Files:** `LISTING-RESEARCH.md`

| Finding | Notes |
|---|---|
| Personal Gmail | Operational identity: a personal `@gmail.com` inbox is named as an account “we can actually use this week” and as the From address for a Console.dev submit. That is PII (personal email), not a public org mailbox. |
| Keys / seeds / tokens / passwords / phone / home address / `.env` | None |

**Remediation:** drop the personal inbox from the research file (use GitHub-only submit paths, or a role mailbox). Rotate the Gmail if it was only meant to stay private.

### PR #56 — FAIL

- **Title:** docs: 2026-08-26 BE/NL public-mailto website-klus sweep
- **URL:** https://github.com/eyeskull2220/solana-invoice/pull/56
- **Files:** `docs/sweep-be-public-mailto.md`

| Finding | Notes |
|---|---|
| Third-party personal Gmail | `docs/sweep-be-public-mailto.md` copies a real `@gmail.com` for “Josy Laumen, kinesitherapeut” in order to say *do not use it*. The address is still PII of a third party committed to git. |
| Phone / home address | None copied. First names and cities from public classifieds (Josy / Kasterlee, Alva / Antwerpen) are listing metadata, not street addresses. |
| Keys / seeds / tokens / passwords / `.env` | None |

**Remediation:** replace the third-party inbox with a non-identifying description (e.g. “a Gmail on josylaumen.be, different person”) without pasting the local-part.

## PASS (with reviewed-not-flagged notes)

Every PR below is **PASS** for keys, seeds, tokens, passwords, phone, home address, leaked `.env`, and non-allowlisted **project** pay-to.

### Tool / catalog PRs

These bake the allowlisted Solana pay-to (and usually the USDC mint) into HTML/README. That is intended public receive data.

| PR | Title | Files | Notes (not FAIL) |
|---|---|---|---|
| [#5](https://github.com/eyeskull2220/solana-invoice/pull/5) | Offline Solana USDC receipt generator | `tools/receipt/*` | Allowlisted pay-to. Integer `2166136261` is an FNV offset, not a phone. |
| [#6](https://github.com/eyeskull2220/solana-invoice/pull/6) | Webhook tester (49 USDC) | `tools/webhook-tester/*` | Allowlisted pay-to + USDC mint. |
| [#7](https://github.com/eyeskull2220/solana-invoice/pull/7) | JSON Cleaner | `tools/json-clean/*` | Same. |
| [#8](https://github.com/eyeskull2220/solana-invoice/pull/8) | Quote Calc | `tools/quote-calc/*` | Same. |
| [#9](https://github.com/eyeskull2220/solana-invoice/pull/9) | Expense CSV logger | `tools/expense-log/*` | Same. |
| [#11](https://github.com/eyeskull2220/solana-invoice/pull/11) | Markdown-to-HTML one-pager | `tools/md-page/*` | Same. |
| [#12](https://github.com/eyeskull2220/solana-invoice/pull/12) | Invoice Reminder | `tools/invoice-reminder/*` | Same. Optional “their pay-to” is user-typed at runtime, not committed. |
| [#13](https://github.com/eyeskull2220/solana-invoice/pull/13) | ICS Reminder | `tools/ics-reminder/*` | Same. |
| [#14](https://github.com/eyeskull2220/solana-invoice/pull/14) | UTM Builder | `tools/utm-builder/*` | Same. |
| [#15](https://github.com/eyeskull2220/solana-invoice/pull/15) | FAQ page generator | `tools/faq-page/*` | Same. |
| [#16](https://github.com/eyeskull2220/solana-invoice/pull/16) | Waitlist landing | `tools/waitlist/*` | Placeholder `you@studio.example` (RFC 2606). |
| [#17](https://github.com/eyeskull2220/solana-invoice/pull/17) | Scope Sheet | `tools/scope-sheet/*` | Same pay-to. |
| [#18](https://github.com/eyeskull2220/solana-invoice/pull/18) | Client intake form builder | `tools/intake/*` | `input type="tel"` with no sample number. Placeholder email `you@studio.example`. |
| [#19](https://github.com/eyeskull2220/solana-invoice/pull/19) | Link-in-bio builder | `tools/link-in-bio/*` | Placeholder `ada@example.com`. CSS class `.phone` is a layout frame, not a number. |
| [#20](https://github.com/eyeskull2220/solana-invoice/pull/20) | Tools catalog | `catalog/index.html` | Allowlisted Solana pay-to only. |
| [#21](https://github.com/eyeskull2220/solana-invoice/pull/21) | Solana USDC tip jar | `tools/tip-jar/*` | Allowlisted pay-to. User can type a different address at download time; nothing extra is committed. |
| [#22](https://github.com/eyeskull2220/solana-invoice/pull/22) | Honor-system paywall stub | `tools/paywall-stub/*` | `test-verify.mjs` `const SIG` is an 88-char base58 **transaction signature** used to test Solscan URL parse — not a secret key. |
| [#23](https://github.com/eyeskull2220/solana-invoice/pull/23) | Time tracker | `tools/time-tracker/*` | Allowlisted pay-to. |
| [#24](https://github.com/eyeskull2220/solana-invoice/pull/24) | Status-page stub | `tools/status-page/*` | Allowlisted pay-to. |

### Research / bounty / listing PRs

| PR | Title | Files | Notes (not FAIL) |
|---|---|---|---|
| [#3](https://github.com/eyeskull2220/solana-invoice/pull/3) | Fiat storefronts research | `research/fiat-storefronts.md` | Mentions email/password **signup** as a product feature. No credentials. |
| [#4](https://github.com/eyeskull2220/solana-invoice/pull/4) | Grants/RFP this week | `research/grants-this-week.md` | Public grant URLs only. |
| [#25](https://github.com/eyeskull2220/solana-invoice/pull/25) | USDC bounty research | `USDC-BOUNTIES.md` | Extra base58 strings are **public**: GMTrade protocol treasury, OnRe program id, Agent Overflow **devnet** mint. Not this repo’s pay-to. Org email `hello@drift.trade`. |
| [#28](https://github.com/eyeskull2220/solana-invoice/pull/28) | Solution for #25 | `submission_25.md` | Allowlisted Solana address only (verification column). |
| [#29](https://github.com/eyeskull2220/solana-invoice/pull/29) | Grants research (rafaio1) | `research/grants-this-week.md` | Public boards. |
| [#31](https://github.com/eyeskull2220/solana-invoice/pull/31) | Grants research (rafaio1, second) | `research/grants-this-week.md` | Same class as #4/#29. |
| [#32](https://github.com/eyeskull2220/solana-invoice/pull/32) | Toolify.ai sweep | `docs/sweep-toolify.md` | Allowlisted Solana + EVM. |
| [#33](https://github.com/eyeskull2220/solana-invoice/pull/33) | Gitcoin + OnlyDust sweep | `docs/sweep-gitcoin-onlydust-today.md` | No wallets/PII. |
| [#34](https://github.com/eyeskull2220/solana-invoice/pull/34) | DeskCrew Solana-USDC sweep | `docs/sweep-deskcrew-solana.md` | Extra Solana pubkeys are DeskCrew’s **public** x402 tool-fee `payTo`, fee-payer, and advertised payout sender — not this project’s receive address, not keys. |
| [#35](https://github.com/eyeskull2220/solana-invoice/pull/35) | Collaborators.build sweep | `docs/sweep-collaborators.md` | Privy `appId` is a **public frontend client id** from their JS bundle, not a bearer secret. GitHub usernames are public PR authors. Allowlisted EVM mentioned as unused. |
| [#36](https://github.com/eyeskull2220/solana-invoice/pull/36) | r/smallbusiness buyer sweep | `docs/sweep-smallbusiness-buyers.md` | Public Reddit handles + permalinks only. No emails/phones copied. Allowlisted pay-tos. |
| [#37](https://github.com/eyeskull2220/solana-invoice/pull/37) | Wellfound/Contra sweep | `docs/sweep-wellfound-contra-team.md` | Public job URLs. No inboxes/phones. |
| [#38](https://github.com/eyeskull2220/solana-invoice/pull/38) | PeoplePerHour sweep | `docs/sweep-pph.md` | Job ids/titles only; no harvested mailboxes. |
| [#39](https://github.com/eyeskull2220/solana-invoice/pull/39) | Lemmy/Fosstodon sweep | `docs/sweep-lemmy-fosstodon.md` | Allowlisted pay-tos. Login **field labels** (`Password`) with no values. Unauthenticated 401 bodies (`incorrect_login`, `invalid_token`) are error strings, not tokens. |
| [#40](https://github.com/eyeskull2220/solana-invoice/pull/40) | Codementor / Q&A-for-pay sweep | `docs/sweep-codementor.md` | Mentions that JustAnswer apply forms ask for name/email/phone; **no values**. |
| [#41](https://github.com/eyeskull2220/solana-invoice/pull/41) | SideProject sweep | `docs/sweep-sideproject.md` | Allowlisted pay-tos. Placeholder emails only. |
| [#42](https://github.com/eyeskull2220/solana-invoice/pull/42) | Algora/Polar today sweep | `docs/sweep-algora-polar-today.md` | No secrets/PII. |
| [#43](https://github.com/eyeskull2220/solana-invoice/pull/43) | r/slavelabour sweep | `docs/sweep-slavelabour.md` | Public subreddit posts; no phones/emails. |
| [#44](https://github.com/eyeskull2220/solana-invoice/pull/44) | Replit sweep | `docs/sweep-replit-today.md` | No secrets/PII. |
| [#45](https://github.com/eyeskull2220/solana-invoice/pull/45) | Farcaster buyer sweep | `docs/sweep-farcaster-buyers.md` | No secrets/PII. |
| [#46](https://github.com/eyeskull2220/solana-invoice/pull/46) | Solana request-thread sweep | `docs/sweep-solana-requests.md` | Allowlisted pay-to + USDC mint. |
| [#47](https://github.com/eyeskull2220/solana-invoice/pull/47) | Live Surge PII/secrets scan | `docs/pii-scan-surge.md` | Token **prefixes** listed in a methodology table (`sk_live_`, `ghp_`, `xoxb-`, `AKIA`) with no payloads. Allowlisted pay-tos. SHA-256 of public HTML is not a secret. |
| [#48](https://github.com/eyeskull2220/solana-invoice/pull/48) | Dev.to/Hashnode sweep | `docs/sweep-devto-hashnode.md` | Placeholder `you@company.com` on a form that was not submitted. |
| [#49](https://github.com/eyeskull2220/solana-invoice/pull/49) | Fast-directory sweep | `docs/sweep-fast-directories.md` | Allowlisted Solana + mint. `.example` placeholders. |
| [#50](https://github.com/eyeskull2220/solana-invoice/pull/50) | GetApp / Crozdesk sweep | `docs/sweep-getapp-crozdesk.md` | Allowlisted Solana + EVM. |
| [#51](https://github.com/eyeskull2220/solana-invoice/pull/51) | r/selfemployed + r/Accounting sweep | `docs/sweep-selfemployed-accounting.md` | Explicitly copied no emails. |
| [#52](https://github.com/eyeskull2220/solana-invoice/pull/52) | Product Hunt alts sweep | `docs/sweep-ph-alts.md` | Login/password **fields** described; none filled. |
| [#53](https://github.com/eyeskull2220/solana-invoice/pull/53) | Newsletter sweep | `docs/sweep-newsletters.md` | Public editorial inboxes (`editor@cooperpress.com`, `new@densediscovery.com`, `hello@console.dev`). Not personal Gmail. |
| [#54](https://github.com/eyeskull2220/solana-invoice/pull/54) | Layer3/Bountycaster/Questbook recheck | `docs/sweep-web3-gated-recheck.md` | No keys/PII. |
| [#55](https://github.com/eyeskull2220/solana-invoice/pull/55) | Dework this-week sweep | `docs/sweep-dework-today.md` | Allowlisted pay-tos listed as unused. |
| [#57](https://github.com/eyeskull2220/solana-invoice/pull/57) | ComeOn.be sweep | `docs/sweep-comeon-be.md` | States personal phones on Vivastreet were **not copied**. Allowlisted EVM. |

## Out of scope / not findings

- **This report PR** (the file you are reading) only documents findings; it does not add new secrets.
- GitHub username `eyeskull2220` is the public repo owner.
- Surge/product URLs (`*.surge.sh`) are public hosts.
- Closed PRs that previously held similar research PII (#10, #26, #30) are **not** in this open-PR table.

## Recheck

Re-run this scan if new open PRs land after 2026-08-26 00:55 UTC, or after FAIL PRs #2 / #56 are edited.
