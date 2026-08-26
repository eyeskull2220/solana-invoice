// Checks Wallet-drafted Solana Pay URLs: amounts, treasury, no Helio / wallet-connect / PII.
var fs = require("fs");
var path = require("path");
var pay = require("./solana-pay-urls.js");

var failures = [];
function assert(cond, msg) {
  if (!cond) failures.push(msg);
}

var TREASURY = "96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3";
var USDC = "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v";

function urlFor(amount, memo) {
  var u = "solana:" + TREASURY + "?amount=" + amount + "&spl-token=" + USDC;
  if (memo) u += "&memo=" + memo;
  return u;
}

var expected = {
  "199": urlFor(199, ""),
  "249": urlFor(249, ""),
  "299": urlFor(299, ""),
  "399-pipeline": urlFor(399, "pipeline"),
  "399-peppol-chase": urlFor(399, "peppol-chase"),
  "490": urlFor(490, ""),
  "900": urlFor(900, "")
};

assert(pay.TREASURY_SOLANA_USDC === TREASURY, "treasury address must match pay page");
assert(pay.USDC_MINT === USDC, "USDC mint must be Circle Solana USDC");

var all = pay.buildAllInvoiceUrls();
Object.keys(expected).forEach(function (id) {
  var url = pay.buildUsdcInvoiceUrl(id);
  assert(url === expected[id], "builder mismatch for " + id + ": " + url);
  assert(pay.builders[id]() === expected[id], "named builder mismatch for " + id);
  assert(all[id] === expected[id], "buildAll mismatch for " + id);
  assert(url.indexOf("solana:" + TREASURY) === 0, id + " must start with solana: + treasury");
  assert(url.indexOf("https://") === -1, id + " must not be HTTPS checkout");
  assert(!/helio|hel\.io|moonpay/i.test(url), id + " must not mention Helio");
  assert(!/wallet.?connect|^wc:/i.test(url), id + " must not be wallet-connect");
  assert(url.indexOf("spl-token=" + USDC) !== -1, id + " must request USDC");
});

var threw = false;
try { pay.buildUsdcInvoiceUrl("1000"); } catch (e) { threw = true; }
assert(threw, "invented amounts must throw");

var NEW_FILES = [
  "solana-pay-urls.js",
  "solana-pay-urls.test.js",
  "docs/solana-pay-urls.md",
  "README.md"
];

var PII = [
  { name: "email", re: /[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}/i },
  { name: "gmail", re: /gmail\.com/i },
  { name: "phone", re: /\+\d{8,15}\b/ },
  { name: "evm-address", re: /0x[a-fA-F0-9]{40}/ },
  { name: "helio", re: /helio|hel\.io/i },
  { name: "wallet-connect", re: /wallet.?connect|wc:/i }
];

var ALLOWED_BASE58 = {};
ALLOWED_BASE58[TREASURY] = true;
ALLOWED_BASE58[USDC] = true;

NEW_FILES.forEach(function (rel) {
  var text = fs.readFileSync(path.join(__dirname, rel), "utf8");
  PII.forEach(function (rule) {
    if (rel === "solana-pay-urls.test.js" && (rule.name === "helio" || rule.name === "wallet-connect" || rule.name === "email")) return;
    if ((rel === "docs/solana-pay-urls.md" || rel === "README.md") && (rule.name === "helio" || rule.name === "wallet-connect")) return;
    var m = text.match(rule.re);
    assert(!m, rel + " PII/forbidden hit (" + rule.name + "): " + (m && m[0]));
  });
  var base58 = text.match(/\b[1-9A-HJ-NP-Za-km-z]{32,44}\b/g) || [];
  base58.forEach(function (token) {
    if (!ALLOWED_BASE58[token]) {
      assert(false, rel + " invented or extra Solana address: " + token);
    }
  });
  if (rel === "docs/solana-pay-urls.md") {
    Object.keys(expected).forEach(function (id) {
      assert(text.indexOf(expected[id]) !== -1, "docs must include URL for " + id);
    });
  }
});

if (failures.length) {
  process.stderr.write(failures.map(function (f) { return "FAIL: " + f; }).join("\n") + "\n");
  process.exit(1);
}
process.stdout.write("ok " + Object.keys(expected).length + " Wallet invoice URLs; PII scan clean\n");
