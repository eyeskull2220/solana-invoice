# Wallet FIX — File-1 inbound ledger

**Seat:** Wallet  
**Date (Brussels):** 2026-08-27  
**RED:** no File-1 inbound ledger  
**FIX:** this folder. Inbound-only. Receive-only.

This page does not send, swap, rebalance, or open perps. It does not invent a sale. It does not invent a third receive address. It does not print a seed. It does not print a full IBAN.

---

## Pay-tos (exactly two)

| Rail | Pay-to | Asset |
| --- | --- | --- |
| Solana | `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3` | native USDC mint `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v` |
| Base | `0x9eb954b567ef3616424a6e1bf42c63724930aa54` | native USDC `0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913` |

Never invent a third. A Solana Pay `reference`, a facilitator gas key, a CDP wallet, a Helio email-embedded wallet, or an MCP session address is **not** a treasury. Do not add it here. Do not put either string in a Peppol `PayeeFinancialAccount` / IBAN field.

Shop / mail copy stays EUR-first. These strings are Wallet rails, not the public face.

---

## FILE-1.csv

Path: `docs/rgy-2026-08-27/wallet/FILE-1.csv`

Inbound USDC ledger. **No spend column.** Outbound is out of scope.

| Column | Meaning |
| --- | --- |
| `date_brussels` | Calendar date in Europe/Brussels |
| `usdc_in` | Inbound USDC amount. `0` until a real inbound lands |
| `eur_note` | Operator note. **Not** a fetched FX mid. **Not** a tax figure. Do not invent a rate |
| `solana_sig` | Signature of the inbound SPL transfer, or `EXAMPLE` |
| `payer` | Paying address or short label. Not a third treasury |
| `what_sold` | What the inbound paid for. Empty/`EXAMPLE` if nothing sold |
| `offerte_id` | Offerte id if one exists. Empty/`EXAMPLE` if none |

### EXAMPLE row only (2026-08-27)

The file has **one** data row, marked `EXAMPLE` in `solana_sig`, `payer`, `what_sold`, and `offerte_id`:

- `usdc_in` = **0**
- `eur_note` = `EXAMPLE Phantom 0/0 no inbound USDC`
- Phantom **0/0** (SOL / USDC) on 2026-08-27 is a **stamp**, not a sale

Phantom MCP `wallet_balances` (Solana + Base, read-only) **timed out** on this run. Do **not** send “to test.” Do **not** call rebalance / buy / withdraw. If a later Wallet seat gets a live read, replace the stamp with that read — still `usdc_in=0` unless a real inbound exists.

This EXAMPLE row is **not** a customer, **not** an offerte, **not** a filled order. Do not rewrite it into a fake inbound.

### How to log a real inbound later

Append a **new** row only when USDC has actually landed on one of the two pay-tos:

1. `date_brussels` = Brussels date of the receive  
2. `usdc_in` = amount received (do not guess)  
3. `eur_note` = operator-entered note (Compliance books EUR on receipt **after** KBO; this file does not invent that number)  
4. `solana_sig` = real signature (or Base tx hash in this field only if the inbound was Base — still no third address)  
5. `payer` = the payer, not a new treasury  
6. `what_sold` / `offerte_id` = only if a real OFFERTE exists  

Missing inbound stays missing. **Do not invent.**

---

## Hard locks (this seat)

| Lock | Meaning |
| --- | --- |
| Receive-only | Read and record. No send, swap, rebalance, perps, new key |
| Two pay-tos | Solana + Base strings above. Never a third |
| No seeds | No mnemonic, no private key, no `CDP_WALLET_SECRET` |
| No full IBAN | Not in this CSV, not in this page. Peppol PaymentMeans is not a wallet string |
| No spend | FILE-1 is inbound. There is no outbound ledger in this FIX |
| EUR note is not FX | Do not fetch or bake a USDC→EUR rate |
| EXAMPLE is not income | 0 USDC. Phantom 0/0. Nothing sold |

---

## What this run did / did not do

| Did | Did not |
| --- | --- |
| Created `FILE-1.csv` with header + EXAMPLE row | Spend, swap, rebalance, perps |
| Created this FIX page | Invent a third pay-to |
| Recorded Phantom MCP timeout | Print a seed or full IBAN |
| Left `usdc_in` at 0 | Invent a payer, offerte, or signature |
| | Edit shop HTML / catalog / kit files |

---

End of Wallet FIX. Next Wallet work is a **real** inbound row, or nothing.
