// Checks Solana Pay builders: amounts, treasury address, no Helio / wallet-connect / PII.
var fs = require("fs");
var path = require("path");
var pay = require("./solana-pay-urls.js");

var failures = [];

function assert(cond, msg) {
  if (!cond) failures.push(msg);
}

var TREASURY = "96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3";
var USDC = "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v";
var AMOUNTS = [249, 299, 399, 490, 900];
var DATE = "2026-08-26";

assert(pay.TREASURY_SOLANA_USDC === TREASURY, "treasury address must match config.js / pay page");
assert(pay.USDC_MINT === USDC, "USDC mint must be Circle Solana USDC");
assert(pay.INVOICE_DATE === DATE, "invoice date must be 2026-08-26");
assert(JSON.stringify(pay.INVOICE_AMOUNTS) === JSON.stringify(AMOUNTS), "amount allowlist");

var expected = {};
AMOUNTS.forEach(function (amount) {
  expected[amount] =
    "solana:" + TREASURY +
    "?amount=" + amount +
    "&spl-token=" + USDC +
    "&label=Solana%20Invoice" +
    "&memo=invoice-" + amount + "-" + DATE;
});

var all = pay.buildAllInvoiceUrls();
AMOUNTS.forEach(function (amount) {
  var url = pay.buildUsdcInvoiceUrl(amount);
  var named = pay.builders[amount]();
  assert(url === expected[amount], "builder URL mismatch for " + amount + ": " + url);
  assert(named === expected[amount], "named builder mismatch for " + amount);
  assert(all[amount] === expected[amount], "buildAllInvoiceUrls mismatch for " + amount);
  assert(url.indexOf("solana:" + TREASURY) === 0, amount + " must start with solana: + treasury");
  assert(url.indexOf("https://") === -1, amount + " must not be an HTTPS Helio/checkout URL");
  assert(!/helio|hel\.io|moonpay/i.test(url), amount + " must not mention Helio/MoonPay");
  assert(!/wallet.?connect|^wc:/i.test(url), amount + " must not be wallet-connect");
  assert(url.indexOf("spl-token=" + USDC) !== -1, amount + " must request USDC, not SOL");
});

var threw = false;
try {
  pay.buildUsdcInvoiceUrl(9);
} catch (e) {
  threw = true;
}
assert(threw, "unsupported amounts must throw");

threw = false;
try {
  pay.buildUsdcInvoiceUrl(1000);
} catch (e) {
  threw = true;
}
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
  { name: "wallet-connect", re: /wallet.?connect|wc:/i },
  { name: "seed-phrase", re: /\b([a-z]+ ){11,23}[a-z]+\b/ },
  { name: "private-key-hex", re: /\b[a-f0-9]{64}\b/i }
];

var ALLOWED_BASE58 = {};
ALLOWED_BASE58[TREASURY] = true;
ALLOWED_BASE58[USDC] = true;

NEW_FILES.forEach(function (rel) {
  var full = path.join(__dirname, rel);
  var text = fs.readFileSync(full, "utf8");
  PII.forEach(function (rule) {
    if (rel === "solana-pay-urls.test.js" && (rule.name === "helio" || rule.name === "wallet-connect" || rule.name === "email")) {
      return;
    }
    if ((rel === "docs/solana-pay-urls.md" || rel === "README.md") && (rule.name === "helio" || rule.name === "wallet-connect")) {
      return;
    }
    var m = text.match(rule.re);
    assert(!m, rel + " PII/forbidden hit (" + rule.name + "): " + (m && m[0]));
  });
  var base58 = text.match(/\b[1-9A-HJ-NP-Za-km-z]{32,44}\b/g) || [];
  base58.forEach(function (token) {
    if (!ALLOWED_BASE58[token]) {
      assert(false, rel + " invented or extra Solana address: " + token);
    }
  });
  AMOUNTS.forEach(function (amount) {
    if (rel === "docs/solana-pay-urls.md") {
      assert(text.indexOf(expected[amount]) !== -1, "docs must include URL for " + amount);
    }
  });
  if (rel === "README.md") {
    assert(text.indexOf(TREASURY) !== -1, "README must keep the treasury address");
    assert(text.indexOf("docs/solana-pay-urls.md") !== -1, "README must point at the URL doc");
  }
});

var config = fs.readFileSync(path.join(__dirname, "config.js"), "utf8");
assert(config.indexOf(TREASURY) !== -1, "config.js still holds the treasury address");

if (failures.length) {
  process.stderr.write(failures.map(function (f) { return "FAIL: " + f; }).join("\n") + "\n");
  process.exit(1);
}
process.stdout.write("ok " + AMOUNTS.length + " invoice URLs; PII scan clean\n");
