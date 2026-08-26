// Solana Pay transfer-request URLs. Recipient is the public pay-page address only.
// Same construction as solanaPayUrl in solana-invoice.html. USDC on Solana only.

(function (root, factory) {
  if (typeof module === "object" && module.exports) {
    module.exports = factory();
  } else {
    root.SolanaPayUrls = factory();
  }
})(typeof self !== "undefined" ? self : this, function () {
  var TREASURY_SOLANA_USDC = "96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3";
  var USDC_MINT = "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v";
  var INVOICE_DATE = "2026-08-26";

  // Wallet-drafted invoice list. Do not add amounts or a second address.
  var INVOICES = [
    { id: "199", amount: 199, memo: "" },
    { id: "249", amount: 249, memo: "" },
    { id: "299", amount: 299, memo: "" },
    { id: "399-pipeline", amount: 399, memo: "pipeline" },
    { id: "399-peppol-chase", amount: 399, memo: "peppol-chase" },
    { id: "490", amount: 490, memo: "" },
    { id: "900", amount: 900, memo: "" }
  ];

  function findInvoice(id) {
    var i;
    for (i = 0; i < INVOICES.length; i++) {
      if (INVOICES[i].id === id) return INVOICES[i];
    }
    return null;
  }

  function buildTransferUrl(amount, memo) {
    var q = [
      "amount=" + encodeURIComponent(String(amount)),
      "spl-token=" + encodeURIComponent(USDC_MINT)
    ];
    if (memo) q.push("memo=" + encodeURIComponent(memo));
    return "solana:" + TREASURY_SOLANA_USDC + "?" + q.join("&");
  }

  function buildUsdcInvoiceUrl(id) {
    var inv = findInvoice(String(id));
    if (!inv) {
      throw new Error("Unsupported invoice id. Wallet list only.");
    }
    return buildTransferUrl(inv.amount, inv.memo);
  }

  function buildAllInvoiceUrls() {
    var i;
    var out = {};
    for (i = 0; i < INVOICES.length; i++) {
      out[INVOICES[i].id] = buildTransferUrl(INVOICES[i].amount, INVOICES[i].memo);
    }
    return out;
  }

  var builders = {};
  INVOICES.forEach(function (inv) {
    builders[inv.id] = function () {
      return buildTransferUrl(inv.amount, inv.memo);
    };
  });

  var api = {
    TREASURY_SOLANA_USDC: TREASURY_SOLANA_USDC,
    USDC_MINT: USDC_MINT,
    INVOICE_DATE: INVOICE_DATE,
    INVOICES: INVOICES.slice(),
    buildUsdcInvoiceUrl: buildUsdcInvoiceUrl,
    buildAllInvoiceUrls: buildAllInvoiceUrls,
    builders: builders
  };

  if (typeof require !== "undefined" && require.main === module) {
    INVOICES.forEach(function (inv) {
      process.stdout.write(inv.id + "\t" + buildTransferUrl(inv.amount, inv.memo) + "\n");
    });
  }

  return api;
});
