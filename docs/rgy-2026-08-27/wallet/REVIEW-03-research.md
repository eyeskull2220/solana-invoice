# REVIEW — Wallet RESEARCH lock (03)

**Seat:** REVIEWER
**Batch:** NEW (RESEARCH-lock only; old pack `#176` is context, not this grade)
**Date:** 2026-08-27
**Artifact:** PR [#184](https://github.com/eyeskull2220/solana-invoice/pull/184) `docs/rgy-2026-08-27/wallet/RESEARCH-lock.md` (head `991964fa63277ff5fce5a729079079251054102d`)
**This file:** judgment only. **No implement.** No spend. No extra snap. No extra RPC.

Verdict for the stage is the worst row. **GREEN only if this file has no RED and no YELLOW.** It has neither.

| Gate | Score |
| --- | --- |
| File-1 SSOT is operator `receive-log.csv`, **not** header-only | **GREEN** |
| Opening `2026-08-27,0,,0.00,,,,opening 0/0` stays; empty inbound valid | **GREEN** |
| Columns `date,usdc,eur_mid,eur_value,payer,memo,tx,notes`; `#128` EXAMPLE never imported | **GREEN** |
| Exactly two pay-tos | **GREEN** |
| No spend in STARTABLE | **GREEN** |
| 08:00-only snap; no extra RPC this sitting | **GREEN** |
| GREEN = pack cleanliness, not inbound | **GREEN** |
| Cite [#171](https://github.com/eyeskull2220/solana-invoice/pull/171); do not fork a second book | **GREEN** |
| This review extra-snapped or spent | **GREEN** (neither) |
| **RESEARCH-lock pack hygiene** | **GREEN** |

Old pack PR [#176](https://github.com/eyeskull2220/solana-invoice/pull/176) scored advocate `#149` **YELLOW** (GREEN count **10 / 12**). This batch scores **this rewrite only**. A later Wallet agent follows `#184` for File-1 current-state and columns. Not `#149`. Not `#128`. PLAN-stage SSOT / 08:00 snap already live on `#171` — cite, do not reopen as a second book.

**GREEN here is pack cleanliness, not inbound. There is no inbound.**

---

## Locks for this batch (honoured)

| Lock | Meaning this run |
| --- | --- |
| **SSOT** | Operator box `/home/box/agent-data/projects/agent-treasury/receive-log.csv`. **Not** header-only. Opening `2026-08-27,0,,0.00,,,,opening 0/0` stays. Empty inbound is valid. Not a parse fail. Not a sale. This VM cannot open the box; CEO-read bytes in PR [#141](https://github.com/eyeskull2220/solana-invoice/pull/141) are the stamp. |
| **Columns** | `date,usdc,eur_mid,eur_value,payer,memo,tx,notes`. PR [#128](https://github.com/eyeskull2220/solana-invoice/pull/128) `date_brussels,usdc_in,eur_note,solana_sig,payer,what_sold,offerte_id` is **EXAMPLE docs, never imported**. Do not prescribe `#128` columns. |
| **Pay-tos (exactly two)** | Solana `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3`. Base `0x9eb954b567ef3616424a6e1bf42c63724930aa54`. Never a third. No IBAN. No seeds. |
| **No spend** | No send, swap, rebalance, perps, Helio, Kraken USDC out, ATA-create, rent-fund, test tx. |
| **08:00 only snap** | Stamp is **2026-08-27 08:00** Europe/Brussels. SOL 0 / USDC ATA empty on `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3`. **This run did not re-query Phantom MCP, did not re-query public RPC, did not take an environment snapshot.** |
| **Cite PLAN-lock `#171`** | Same SSOT, same 8-col header, same opening 0/0, same two pay-tos, same 08:00-only snap. Do not fork a second book. Do not re-score PLAN. |

Mints (not pay-tos): Solana USDC `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v`. Base USDC `0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913`.

---

## What was judged (this file, not a CODE audit)

RESEARCH-lock means: the written close of the two File-1 hygiene holes. It is not a GREEN stamp on inbound. There is no inbound. Scored from zero against **this file**:

| Source | Role this batch |
| --- | --- |
| PR [#184](https://github.com/eyeskull2220/solana-invoice/pull/184) `RESEARCH-lock.md` | **The artifact.** Rewrite that claims to close `#176`. |
| PR [#176](https://github.com/eyeskull2220/solana-invoice/pull/176) `REVIEW-01-research.md` | Prior YELLOW pack. Context. Bar for the two hygiene rows. Not this grade. |
| PR [#171](https://github.com/eyeskull2220/solana-invoice/pull/171) `PLAN-lock.md` | PLAN already locked the same SSOT / 08:00 snap / two pay-tos. **Cite only.** Not re-scored. Do not fork. |
| PR [#149](https://github.com/eyeskull2220/solana-invoice/pull/149) `01-adv-research.md` | Advocate RESEARCH. YELLOW. Not the page a later agent follows. |
| PR [#141](https://github.com/eyeskull2220/solana-invoice/pull/141) File-1 after-fix | Operator File-1 **GREEN** as a ledger artifact. Stamp for 0/0. |
| PR [#128](https://github.com/eyeskull2220/solana-invoice/pull/128) `FILE-1.csv` | EXAMPLE docs. Wrong columns. Must stay never-imported. Not a FIX recipe. |
| PR [#91](https://github.com/eyeskull2220/solana-invoice/pull/91) `tools/eur-receive-log/` | Kit. Not File-1. Must stay import/export-blocked. |
| leftover `main` `README.md` / `config.js` / `index.html` / `catalog.html` | Solana treasury + mint only. Base string is **not** on `main`. Shop leftover, not a third treasury. |

No Phantom `wallet_balances`. No public RPC re-query. No Helio. No Kraken USDC sale. No shop HTML. No mail. No environment snapshot.

`#184` does not grade itself GREEN. This file does.

---

## Closed from `#176` (not copied as this grade)

| `#176` gate | Was | Why this file closes it |
| --- | --- | --- |
| File-1 current-state vs book | **YELLOW** | SSOT is operator `receive-log.csv`. **Not** header-only. Opening 0/0 left intact. `#149` “Header only. No inbound row.” named as a stale shape. |
| File-1 later-FIX columns | **YELLOW** | Canonical header is the operator 8-col. `#128` `date_brussels,usdc_in,…` is EXAMPLE, never imported. `#149` NOTES prescription is **killed**. |
| File-1 0/0 valid | GREEN | Kept. Empty inbound is not a parse fail, not a sale. |
| Two pay-tos only | GREEN | Kept. Exact strings. Never a third. |
| No spend | GREEN | Kept. No send / swap / rebalance / ATA-create. |
| 08:00-only snap | GREEN | Kept. Cite `#171`. No extra RPC this sitting. |
| mints ≠ pay-tos | GREEN | Kept. Circle native USDC cited as mints. Ethereum USDC named as wrong token. |
| no invented inbound | GREEN | Kept. There is no inbound. |
| no IBAN / seeds | GREEN | Kept. |
| shop leftover Solana-only | GREEN | Kept. Documented, **not** patched from Wallet. |
| this sitting extra-snap | GREEN | Kept on `#184`. Independently kept on this review. |
| scope hygiene | GREEN | Single new markdown under `docs/rgy-2026-08-27/wallet/`. No CSV. No shop edit. |

Leftover open PRs `#128` / `#149` / `#91` still exist as git objects. They do **not** un-GREEN this page. A later agent that follows those pages instead of `#184` (File-1 current-state / columns) or `#171` (PLAN) is off-lock.

---

## Scores

### 1. File-1 SSOT is operator `receive-log.csv`, not header-only — **GREEN**

**Lock.** SSOT is operator `receive-log.csv`. Not header-only. Opening `2026-08-27,0,,0.00,,,,opening 0/0` stays. Empty inbound is valid. Not a parse fail. Not a sale.

**`#176` yellow.** Pack live-desk: **“Header only. No inbound row.”** Book (`#141` GREEN): eight-column header **plus** opening `2026-08-27,0,,0.00,,,,opening 0/0`. Header-only was the old RED `#141` closed. Empty inbound is still true. The **shape** of File-1 in `#149` was stale.

**Closed on `#184`.** Canonical File-1 is the operator box:

```
/home/box/agent-data/projects/agent-treasury/receive-log.csv
```

It is **not** header-only. `#149` live-desk “Header only. No inbound row.” is a **stale shape**. Empty inbound is still true. The file already has a first data row. BLOCKED: describe File-1 as header-only — **never**. Do not describe a first-row 0/0 as “missing, so write a header-only git stub.” This VM cannot open the box. Do not patch the box CSV from a RESEARCH page. Do not invent a second opening row in git.

**Fix-if-not-green.** — (closed as a gate). Name the book. Do not describe File-1 as header-only.

### 2. Opening 0/0 stays; empty inbound valid — **GREEN**

**Lock.** Opening row left intact:

```
2026-08-27,0,,0.00,,,,opening 0/0
```

Empty inbound is **valid**. Not a parse fail. Not a sale. Not a fill. Not a filing.

**Closed on `#184`.** Field map matches the book: `date=2026-08-27`, `usdc=0`, `eur_mid` **empty** (valid on a zero row), `eur_value=0.00` (zero-of-zero, **not** 1 USDC = 1 EUR), `payer` / `memo` / `tx` empty, `notes` = `opening 0/0` (and any CEO-read suffix from `#141`). Inbound: **none**.

CEO-read bytes in `#141` may continue the `notes` field after `opening 0/0`. Leave that row. Do not truncate it. Do not invent a payer, offerte, signature, or positive `usdc` so the CSV “looks used.” STARTABLE: keep the opening row. WAIT: first real inbound row until actual USDC on a listed pay-to **and** pay-proof **and** operator `eur_mid`.

`#176` already scored 0/0-valid GREEN on `#149`. This rewrite does not reopen it. It stops treating the opening row as missing.

**Fix-if-not-green.** — (closed as a gate). Leave the opening row intact.

### 3. Columns; `#128` EXAMPLE never imported — **GREEN**

**Lock.** Canonical columns are `date,usdc,eur_mid,eur_value,payer,memo,tx,notes`. PR `#128` columns are **EXAMPLE, never imported**.

**`#176` yellow.** `#149` NOTES: “if a later FIX writes the CSV” use `date_brussels, usdc_in, eur_note, solana_sig, payer, what_sold, offerte_id` — the `#128` map. Pack Y3 called `#128` EXAMPLE not income (correct) then **prescribed those columns**. `eur_note` is not `eur_mid`/`eur_value`. `solana_sig` is not full `tx` after pay-proof and ignores Base. A later FIX that followed `#149` NOTES would split the books.

**Closed on `#184`.** Exact columns (8):

```
date,usdc,eur_mid,eur_value,payer,memo,tx,notes
```

That is the only File-1 header. `#128` `docs/rgy-2026-08-27/wallet/FILE-1.csv` uses the EXAMPLE names. That file is **not** SSOT. It is **never imported** into operator File-1. It is never exported over operator File-1. Live inbound is **never appended** there. **Do not prescribe `#128` columns.** The `#149` prescription is **killed**.

Wrong map is named so a later FIX cannot “helpfully” rename:

| Operator (SSOT) | `#128` EXAMPLE | Do not |
| --- | --- | --- |
| `date` | `date_brussels` | Do not rename the SSOT |
| `usdc` | `usdc_in` | Do not dual-book |
| `eur_mid` / `eur_value` | `eur_note` (explicitly not FX) | Do not treat `eur_note` as a mid; do not fetch ECB onto the 0/0 row |
| `tx` (full sig after pay-proof) | `solana_sig` | Do not copy EXAMPLE into `tx`; do not ignore Base |
| `memo` (what sold) | `what_sold` + `offerte_id` | Do not grow a ninth column on the box |

Kit `#91` is a **kit, not File-1** (six columns; `parseAmount` would skip 0/0). RESEARCH does not import/export across it. That matches PLAN-lock `#171`. It is not a second schema.

**Fix-if-not-green.** — (closed as a gate). Canonical File-1 = operator 8-col header. `#128` stays a stub, not SSOT.

### 4. Exactly two pay-tos — **GREEN**

**Lock.** The two strings. Never a third.

- Solana `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3`
- Base `0x9eb954b567ef3616424a6e1bf42c63724930aa54`

**Closed on `#184`.** Those two appear as receive addresses. Mints are labeled **not** a pay-to. Ethereum-mainnet USDC `0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48`, bridged USDC.e, Phantom MCP session, Solana Pay `reference`, facilitator gas key, CDP wallet, Helio email-embedded wallet, explorer “token account,” EIP-55 recase, leftover shop HTML: **not** treasury.

This checkout confirms leftover `README.md` / `config.js` / `index.html` / `catalog.html` list the Solana string only. Base is absent on `main`. `#184` documents that leftover and **does not** patch the shop and **does not** drop Base. Builder / CEO own the face.

**No IBAN.** No full IBAN. No Revolut last-4. Do not stuff either wallet string into Peppol PaymentMeans. **No seeds.**

`#176` already scored this GREEN. This rewrite does not reopen it. No third string invented in the file.

**Fix-if-not-green.** — (closed as a gate). Never a third.

### 5. No spend in STARTABLE — **GREEN**

**Lock.** No spend. Timeout, null account, empty ATA, and `#176` YELLOW are **not** licenses to send.

**Closed on `#184`.** STARTABLE is name operator File-1 as SSOT, keep opening 0/0, cite `#128` as EXAMPLE, cite `#171` PLAN-lock, refuse third-address / spend / IBAN PRs. None of those is send, swap, rebalance, perps, Helio, Kraken USDC out, ATA-create, rent-fund, or “tiny USDC to ourselves so File-1 has a tx.”

BLOCKED: spend, swap, rebalance, ATA-create, test tx — **never on this RESEARCH**. File-1 has **no outbound column**. Do not add one.

This reviewer run did not send either.

**Fix-if-not-green.** — (closed as a gate). Do not spend this GREEN.

### 6. 08:00-only snap; no extra RPC this sitting — **GREEN**

**Lock.** 08:00 is the only scheduled snap. No extra RPC. Extra RPC only after a pasted sig.

**Closed on `#184`.** Stamp **2026-08-27 08:00** Europe/Brussels. SOL **0**. USDC ATA **empty / 0**. File-1 `usdc` **0**. Inbound txs **none**. Extra snap this RESEARCH **none**. Numbers already taken / CEO-verified. **Do not refresh.** This run did **not** call Phantom `wallet_balances`, did **not** re-query public RPC, did **not** take an environment snapshot. `#128` “replace the stamp” stays killed — cited from `#171`, not re-opened.

Extra RPC only after a **pasted** signature (or Base tx hash), then one `getTransaction` / Base receipt against **one of the two pay-tos**, the native USDC mint on that chain, and the claimed amount. MCP session wallet is not proof. No pay-proof was presented. **Do not snap “just to see.”**

WAIT: Phantom MCP live read is **not required**. Timeout was already WAIT. Do not send to test.

**Fix-if-not-green.** — (closed as a gate). Do not replace the 08:00 stamp. Do not retry `wallet_balances` until a pasted sig exists.

### 7. GREEN = pack cleanliness, not inbound — **GREEN**

**Lock.** GREEN on this page means the pack is clean. It does not mean USDC landed. There is no inbound.

**Closed on `#184`.** Lead, GREENS-kept table, next-inbound section, bar, and close all state it. “Next inbound (one ledger — still none)” starts **There is no inbound. Do not invent one to exercise this recipe.** Clean pack ≠ funded treasury. This file does not grade itself GREEN.

A later FIX that “writes a sale so the CSV looks used” would spend this GREEN. That is BLOCKED: invent inbound — **never**.

**Fix-if-not-green.** — (closed as a gate). Do not treat pack GREEN as inbound.

### 8. Cite `#171`; do not fork a second book — **GREEN**

**Lock.** PLAN-stage SSOT / 08:00 snap already live on [PR #171](https://github.com/eyeskull2220/solana-invoice/pull/171) `PLAN-lock.md`. Cite. Do not fork a second book.

**Closed on `#184`.** The page cites `#171` in the lead, in GREENS kept, in the columns section, in 08:00-only snap (`#128` replace-the-stamp stays killed), in STARTABLE, in sources, and in the did/did-not table. RESEARCH names the operator 8-col header **again** so a later FIX cannot follow `#149` NOTES instead. That is restating the **same** book, not a second one.

Checked against `#171` (not re-scored):

| Fact | `#171` PLAN-lock | `#184` RESEARCH-lock |
| --- | --- | --- |
| Path | `/home/box/agent-data/projects/agent-treasury/receive-log.csv` | same |
| Header | `date,usdc,eur_mid,eur_value,payer,memo,tx,notes` | same |
| Opening | `2026-08-27,0,,0.00,,,,opening 0/0` | same |
| `#128` | EXAMPLE, never imported | EXAMPLE, never imported; `#149` prescription killed |
| `#91` | kit, not File-1; no import/export | kit, not File-1; no import/export |
| Pay-tos | the two strings | the two strings |
| Stamp | 2026-08-27 08:00; SOL 0; ATA empty | same; do not re-read |
| Next inbound | operator File-1 only, after pay-proof | same recipe; **still none** |

No competing SSOT. No git stub promoted. STARTABLE “Cite `#171`” is PLAN-cite, not a second PLAN. Did-not: re-score PLAN; implement `#150` / `#128` / `#91`.

**Fix-if-not-green.** — (closed as a gate). Follow `#184` for RESEARCH File-1 current-state / columns. Follow `#171` for PLAN. Do not invent a third book.

### 9. This review extra-snapped or spent — **GREEN**

**Notes.** No Phantom MCP balance call. No public RPC re-query. No send. No Helio. No shop HTML. No mail. No environment snapshot. `#141` G5 chain corroboration was a **prior** batch; this batch does not repeat it. `#184` claimed it did not extra-snap; this review independently did not either. Diff judged: one new markdown file.

---

## RED

None on this artifact.

## YELLOW

None on this artifact.

---

## What is already true (does not un-GREEN this page)

These are scars so a later agent does not “fix” the wrong thing:

- Operator File-1 0/0 is valid (`#141`). Do not invent inbound. GREEN is pack cleanliness, not a funded treasury.
- Two pay-to strings are frozen. Do not add a third “for completeness.”
- `#128` remains an open EXAMPLE stub with the wrong columns. Do not import it. Do not prescribe its columns. Do not merge it over the box.
- `#149` remains the advocate YELLOW corpus. A later agent follows `#184`, not `#149` NOTES.
- `#91` may stay an unmerged operator pack. Do not import/export across it (`parseAmount` would skip 0/0).
- `#171` is the PLAN lock. This RESEARCH does not re-open PLAN and does not fork it.
- Shop face still lists Solana only (`main` README / `config.js` / `index.html` / `catalog.html`). Wallet still has Base. Do not patch leftover shop HTML from Wallet.
- Copying this GREEN into an extra `wallet_balances` tonight would spend it.

---

## STARTABLE / BLOCKED / WAIT (this judgment)

### STARTABLE

| Item | Note |
| --- | --- |
| Keep File-1 opening 0/0 | Valid empty inbound. Not a parse fail. Not a sale. |
| Follow `#184` for File-1 current-state and columns | Not `#149`. Not `#128`. |
| Cite `#171` PLAN-lock | Same SSOT / two pay-tos / 08:00-only snap. Do not fork. |
| Cite `#128` as EXAMPLE, never imported | Do not prescribe its columns. |
| Refuse third-address / spend / IBAN PRs | Wallet yes/no. |
| 08:00 stamp as the day’s snap | Already taken / CEO-verified. Use it. Do not refresh it tonight. |

### BLOCKED

| Item | Until |
| --- | --- |
| Describe File-1 as header-only | Never — that RED is closed |
| Prescribe `#128` `date_brussels,usdc_in,…` for a later FIX | Never |
| Import `#128` FILE-1.csv into the box | Never |
| Extra snap / Phantom MCP / public RPC re-query / “replace the stamp” | A pasted pay-proof sig |
| Spend, swap, rebalance, ATA-create, test tx | Never on this RESEARCH |
| Third pay-to / IBAN / seed | Never |
| Invent inbound so the CSV looks used | Never |
| Book 1 USDC = 1 EUR | Never |
| Patch leftover shop HTML from Wallet | Never (Builder / CEO own the face) |
| Fork a second File-1 book apart from `#171` / `#184` | Never |
| Import/export operator File-1 through kit `#91` | Never (0/0 would be skipped) |

### WAIT

| Item | Waiting on |
| --- | --- |
| First real File-1 inbound row | Actual USDC on a listed pay-to **and** pay-proof **and** operator `eur_mid` |
| Phantom MCP live read | Not required. Timeout was already WAIT. Do not send to test |

---

## This run

| Did | Did not |
| --- | --- |
| Read `#184` `RESEARCH-lock.md` as the RESEARCH artifact | Extra snap / Phantom `wallet_balances` / public RPC re-query |
| Scored RESEARCH gates from zero against this file | Spend, swap, rebalance, perps, Helio |
| Used 08:00 / File-1 0/0 as the stamp | Invent a third pay-to, inbound, IBAN, or seed |
| Checked `#171` as the same book (cite, not a re-score) | Fork a second SSOT; re-score PLAN; implement `#150` / `#128` / `#91` |
| Confirmed leftover `main` shop is Solana-only (not patched) | Edit shop HTML, catalog, kit files, mail, patch box CSV |
| Wrote this REVIEW | Treat leftover open PRs as this grade; treat pack GREEN as inbound |

**RESEARCH-lock pack hygiene: GREEN.** Reviewer does not implement it. No shop HTML. No spend. No snap.

GREEN here is pack cleanliness, not inbound. There is no inbound.

---

End. Docs only. No spend. No snap. No RPC. No IBAN. Two pay-tos. Empty inbound valid.
