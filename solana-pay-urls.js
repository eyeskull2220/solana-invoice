// Solana Pay transfer-request URL builders for treasury USDC invoices.
// Recipient is the public pay-page address only. Do not invent or swap it.
// USDC on Solana only. Transfer request URLs — not a hosted checkout.

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
  var INVOICE_AMOUNTS = [249, 299, 399, 490, 900];
  var LABEL = "Solana Invoice";

  function isAllowedAmount(amountUsdc) {
    var n = Number(amountUsdc);
    var i;
    for (i = 0; i < INVOICE_AMOUNTS.length; i++) {
      if (INVOICE_AMOUNTS[i] === n) return true;
    }
    return false;
  }

  function memoFor(amountUsdc) {
    return "invoice-" + String(amountUsdc) + "-" + INVOICE_DATE;
  }

  function encodePair(key, value) {
    return encodeURIComponent(key) + "=" + encodeURIComponent(String(value));
  }

  // Transfer request (solana:<recipient>?…). Not an HTTPS checkout URL
  // and not a session URI.
  function buildUsdcInvoiceUrl(amountUsdc) {
    if (!isAllowedAmount(amountUsdc)) {
      throw new Error(
        "Unsupported invoice amount. Allowed USDC: " + INVOICE_AMOUNTS.join(", ")
      );
    }
    var amount = String(Number(amountUsdc));
    var query = [
      encodePair("amount", amount),
      encodePair("spl-token", USDC_MINT),
      encodePair("label", LABEL),
      encodePair("memo", memoFor(amount))
    ].join("&");
    return "solana:" + TREASURY_SOLANA_USDC + "?" + query;
  }

  function buildAllInvoiceUrls() {
    var i;
    var out = {};
    for (i = 0; i < INVOICE_AMOUNTS.length; i++) {
      out[INVOICE_AMOUNTS[i]] = buildUsdcInvoiceUrl(INVOICE_AMOUNTS[i]);
    }
    return out;
  }

  var builders = {
    249: function () { return buildUsdcInvoiceUrl(249); },
    299: function () { return buildUsdcInvoiceUrl(299); },
    399: function () { return buildUsdcInvoiceUrl(399); },
    490: function () { return buildUsdcInvoiceUrl(490); },
    900: function () { return buildUsdcInvoiceUrl(900); }
  };

  var api = {
    TREASURY_SOLANA_USDC: TREASURY_SOLANA_USDC,
    USDC_MINT: USDC_MINT,
    INVOICE_DATE: INVOICE_DATE,
    INVOICE_AMOUNTS: INVOICE_AMOUNTS.slice(),
    LABEL: LABEL,
    memoFor: memoFor,
    buildUsdcInvoiceUrl: buildUsdcInvoiceUrl,
    buildAllInvoiceUrls: buildAllInvoiceUrls,
    builders: builders
  };

  if (typeof require !== "undefined" && require.main === module) {
    INVOICE_AMOUNTS.forEach(function (amount) {
      process.stdout.write(String(amount) + " USDC\t" + buildUsdcInvoiceUrl(amount) + "\n");
    });
  }

  return api;
});
