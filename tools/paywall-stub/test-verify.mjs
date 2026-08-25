import fs from "node:fs";
import path from "node:path";
import vm from "node:vm";
import { fileURLToPath } from "node:url";
import assert from "node:assert/strict";

const dir = path.dirname(fileURLToPath(import.meta.url));
const html = fs.readFileSync(path.join(dir, "index.html"), "utf8");

function grab(re, label) {
  const m = html.match(re);
  assert.ok(m, "missing " + label);
  return m[1];
}

const coreSrc = grab(/<script id="paywall-core">([\s\S]*?)<\/script>/, "paywall-core");
const ctx = {};
vm.runInNewContext(coreSrc, ctx);
const C = ctx.PaywallCore;

const PAY_TO = "96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3";
const MINT = "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v";
const RAW = "9000000";
const SIG = "5VERv8NMvzbJMEkV8xatZkSjcDmdDhEqaM9BhBmdVJNW8LgPH4qsGWxFH5d8wb2n8wz9gxKh8kjKhHs9N5nKjN5n";

assert.equal(html.includes(PAY_TO), true);
assert.equal(html.includes("priceUsdc: 9"), true);
assert.equal(html.includes(MINT), true);
assert.equal(C.looksLikeAddress(PAY_TO), true);
assert.equal(C.looksLikeSig(""), false);
assert.equal(C.looksLikeSig("asdf"), false);
assert.equal(C.looksLikeSig("short"), false);
assert.equal(C.looksLikeSig(SIG), true);
assert.equal(C.extractSig("  " + SIG + "  "), SIG);
assert.equal(C.extractSig("https://solscan.io/tx/" + SIG), SIG);
assert.equal(C.extractSig("https://explorer.solana.com/tx/" + SIG + "?cluster=mainnet"), SIG);

assert.equal(C.isPayment(null, PAY_TO, MINT, RAW), false);
assert.equal(C.isPayment({ meta: { err: { InstructionError: [] } } }, PAY_TO, MINT, RAW), false);

const paidByDelta = {
  meta: {
    err: null,
    preTokenBalances: [{
      accountIndex: 2,
      mint: MINT,
      owner: PAY_TO,
      uiTokenAmount: { amount: "1000" }
    }],
    postTokenBalances: [{
      accountIndex: 2,
      mint: MINT,
      owner: PAY_TO,
      uiTokenAmount: { amount: "9001000" }
    }]
  }
};
assert.equal(C.isPayment(paidByDelta, PAY_TO, MINT, RAW), true);

const wrongAmount = {
  meta: {
    err: null,
    preTokenBalances: [{
      accountIndex: 2,
      mint: MINT,
      owner: PAY_TO,
      uiTokenAmount: { amount: "0" }
    }],
    postTokenBalances: [{
      accountIndex: 2,
      mint: MINT,
      owner: PAY_TO,
      uiTokenAmount: { amount: "1000000" }
    }]
  }
};
assert.equal(C.isPayment(wrongAmount, PAY_TO, MINT, RAW), false);

const paidByParsed = {
  meta: { err: null, preTokenBalances: [], postTokenBalances: [], innerInstructions: [] },
  transaction: {
    message: {
      instructions: [{
        parsed: {
          info: {
            mint: MINT,
            destinationOwner: PAY_TO,
            tokenAmount: { amount: RAW }
          }
        }
      }]
    }
  }
};
assert.equal(C.isPayment(paidByParsed, PAY_TO, MINT, RAW), true);

const payUrl = C.solanaPayUrl(PAY_TO, 9, MINT, "Treasury tools");
assert.equal(payUrl.startsWith("solana:" + PAY_TO), true);
assert.equal(payUrl.includes("amount=9"), true);
assert.equal(payUrl.includes("spl-token=" + MINT), true);

console.log("ok " + 14 + " checks");
