(function (global) {
  "use strict";

  var PAY_TO = "96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3";
  var USDC_MINT = "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v";
  var PRICE = 399;
  var STORAGE_KEY = "treasury-pipeline-kit-v1";
  var MONTHS_NL = [
    "januari", "februari", "maart", "april", "mei", "juni",
    "juli", "augustus", "september", "oktober", "november", "december"
  ];

  var DEMO = {
    sellerName: "Studio Noord",
    sellerAddress: "Voorbeeldlaan 1\n2000 Antwerpen",
    sellerVat: "BE 0999.999.992",
    sellerMail: "hello@studio.example",
    leadName: "Alex Example",
    leadCompany: "Client BV",
    leadEmail: "alex@client.example",
    leadPhone: "",
    leadJob: "Website herwerking: homepage en contactpagina, inclusief mobiele layout.",
    leadDeadline: "2026-09-15",
    leadBudget: "726",
    leadNotes: "Demo lead. Geen echte inbox.",
    clientName: "Client BV",
    clientAddress: "Klantplein 8\n1000 Brussel",
    clientVat: "BE 0888.888.888",
    clientMail: "billing@client.example",
    offerteNo: "OFF-202608-001",
    offerteDate: "2026-08-12",
    offerteValid: "2026-09-12",
    offerteIntro: "Offerte voor de herwerking van de website, op basis van de intake.",
    invoiceNo: "F-202608-001",
    invoiceDate: "2026-08-12",
    dueDate: "2026-08-26",
    vatRate: "21",
    lineDesc: "Website herwerking — homepage + contact",
    lineQty: "8",
    linePrice: "75,00"
  };

  function $(id) {
    return document.getElementById(id);
  }

  function escapeHtml(value) {
    return String(value)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#39;");
  }

  function parseDecimal(raw) {
    var s = String(raw == null ? "" : raw).trim().replace(/\s/g, "").replace(",", ".");
    if (!s) return null;
    if (!/^\d+(\.\d+)?$/.test(s)) return null;
    var n = Number(s);
    if (!isFinite(n) || n < 0) return null;
    return n;
  }

  function toCents(n) {
    return Math.round(n * 100);
  }

  function formatEur(cents) {
    var neg = cents < 0;
    var abs = Math.abs(cents);
    var euro = Math.floor(abs / 100);
    var ct = String(abs % 100);
    if (ct.length < 2) ct = "0" + ct;
    var intStr = String(euro).replace(/\B(?=(\d{3})+(?!\d))/g, ".");
    return (neg ? "−" : "") + intStr + "," + ct + " €";
  }

  function formatDateNl(iso) {
    if (!iso) return "";
    var p = String(iso).split("-");
    if (p.length !== 3) return iso;
    var mi = parseInt(p[1], 10) - 1;
    var month = MONTHS_NL[mi] || p[1];
    return parseInt(p[2], 10) + " " + month + " " + p[0];
  }

  function qtyLabel(n) {
    if (Math.abs(n - Math.round(n)) < 1e-9) return String(Math.round(n));
    return String(n).replace(".", ",");
  }

  function looksLikeEmail(value) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value);
  }

  function slug(name) {
    var s = String(name || "").toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");
    return s || "document";
  }

  function defaultState() {
    return {
      sellerName: DEMO.sellerName,
      sellerAddress: DEMO.sellerAddress,
      sellerVat: DEMO.sellerVat,
      sellerMail: DEMO.sellerMail,
      leadName: DEMO.leadName,
      leadCompany: DEMO.leadCompany,
      leadEmail: DEMO.leadEmail,
      leadPhone: DEMO.leadPhone,
      leadJob: DEMO.leadJob,
      leadDeadline: DEMO.leadDeadline,
      leadBudget: DEMO.leadBudget,
      leadNotes: DEMO.leadNotes,
      clientName: DEMO.clientName,
      clientAddress: DEMO.clientAddress,
      clientVat: DEMO.clientVat,
      clientMail: DEMO.clientMail,
      offerteNo: DEMO.offerteNo,
      offerteDate: DEMO.offerteDate,
      offerteValid: DEMO.offerteValid,
      offerteIntro: DEMO.offerteIntro,
      invoiceNo: DEMO.invoiceNo,
      invoiceDate: DEMO.invoiceDate,
      dueDate: DEMO.dueDate,
      vatRate: DEMO.vatRate,
      lines: [{ desc: DEMO.lineDesc, qty: DEMO.lineQty, price: DEMO.linePrice }],
      reminderBody: reminderBodyFrom(DEMO)
    };
  }

  function reminderBodyFrom(d) {
    return (
      "Beste " + (d.clientName || "Client BV") + ",\n\n" +
      "Onze factuur " + (d.invoiceNo || "F-202608-001") +
      " van " + formatDateNl(d.invoiceDate || "2026-08-12") +
      " is vervallen op " + formatDateNl(d.dueDate || "2026-08-26") +
      ". Het openstaande bedrag is 726,00 € incl. 21% BTW.\n\n" +
      "Gelieve te betalen met vermelding van het factuurnummer. Vragen? Antwoord op dit bericht of gebruik " +
      (d.sellerMail || "hello@studio.example") + ".\n\n" +
      "Met vriendelijke groeten,\n" +
      (d.sellerName || "Studio Noord")
    );
  }

  function loadState() {
    try {
      var raw = localStorage.getItem(STORAGE_KEY);
      if (!raw) return defaultState();
      var parsed = JSON.parse(raw);
      var base = defaultState();
      var key;
      for (key in parsed) {
        if (Object.prototype.hasOwnProperty.call(parsed, key)) base[key] = parsed[key];
      }
      if (!base.lines || !base.lines.length) {
        base.lines = defaultState().lines;
      }
      return base;
    } catch (e) {
      return defaultState();
    }
  }

  function saveState(state) {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
    } catch (e) {}
  }

  function resetState() {
    var state = defaultState();
    saveState(state);
    return state;
  }

  function readLinesFrom(container) {
    var nodes = container.querySelectorAll(".line");
    var out = [];
    var i, el, desc, qty, price, unitCents;
    for (i = 0; i < nodes.length; i++) {
      el = nodes[i];
      desc = el.querySelector(".desc").value.trim();
      qty = parseDecimal(el.querySelector(".qty").value);
      price = parseDecimal(el.querySelector(".price").value);
      if (!desc && qty === null && price === null) continue;
      if (qty === null || price === null) {
        out.push({ desc: desc, qty: qty, price: price, exclCents: null, invalid: true });
        continue;
      }
      unitCents = toCents(price);
      out.push({
        desc: desc,
        qty: qty,
        price: price,
        unitCents: unitCents,
        exclCents: Math.round(qty * unitCents),
        invalid: false
      });
    }
    return out;
  }

  function linesForSave(container) {
    var nodes = container.querySelectorAll(".line");
    var out = [];
    var i, el;
    for (i = 0; i < nodes.length; i++) {
      el = nodes[i];
      out.push({
        desc: el.querySelector(".desc").value,
        qty: el.querySelector(".qty").value,
        price: el.querySelector(".price").value
      });
    }
    if (!out.length) out.push({ desc: "", qty: "", price: "" });
    return out;
  }

  function totalsOf(lines, vatRate) {
    var excl = 0;
    var i;
    for (i = 0; i < lines.length; i++) {
      if (!lines[i].invalid && lines[i].exclCents != null) excl += lines[i].exclCents;
    }
    var vat = Math.round(excl * vatRate / 100);
    return { exclCents: excl, vatCents: vat, inclCents: excl + vat };
  }

  function usableLines(lines) {
    var out = [];
    var i;
    for (i = 0; i < lines.length; i++) {
      if (!lines[i].invalid) out.push(lines[i]);
    }
    return out;
  }

  function linesTableHtml(lines) {
    var usable = usableLines(lines);
    var rows = "";
    var i, line;
    if (!usable.length) {
      rows = "<tr><td colspan=\"4\" class=\"empty\">Nog geen lijnen</td></tr>";
    } else {
      for (i = 0; i < usable.length; i++) {
        line = usable[i];
        rows += "<tr>" +
          "<td>" + (line.desc ? escapeHtml(line.desc) : "—") + "</td>" +
          "<td class=\"num\">" + escapeHtml(qtyLabel(line.qty)) + "</td>" +
          "<td class=\"num\">" + escapeHtml(formatEur(line.unitCents)) + "</td>" +
          "<td class=\"num\">" + escapeHtml(formatEur(line.exclCents)) + "</td>" +
          "</tr>";
      }
    }
    return "<table class=\"items\">" +
      "<thead><tr><th>Omschrijving</th><th class=\"num\">Aantal</th>" +
      "<th class=\"num\">Prijs excl.</th><th class=\"num\">Totaal excl.</th></tr></thead>" +
      "<tbody>" + rows + "</tbody></table>";
  }

  function partyHtml(name, address, vat, mail, emptyName) {
    var parts = [];
    parts.push(name ? escapeHtml(name) : "<span class=\"empty\">" + emptyName + "</span>");
    if (address) parts.push(escapeHtml(address));
    if (vat) parts.push("BTW/KBO " + escapeHtml(vat));
    if (mail) parts.push(escapeHtml(mail));
    return parts.join("\n");
  }

  function downloadCss() {
    return "html,body{margin:0;padding:0}body{min-height:100vh;background:#f3efe6;color:#1c1814;font:16px/1.5 \"Iowan Old Style\",Palatino,\"Palatino Linotype\",Georgia,serif}main{width:min(760px,100%);margin:0 auto;padding:28px 16px 64px}.sheet{background:#fffcf7;border:1px solid #d9d0c3;border-radius:4px;padding:32px 28px 24px}.top{display:flex;justify-content:space-between;gap:16px;align-items:flex-start;border-bottom:2px solid #1c1814;padding-bottom:14px;margin-bottom:18px}.kicker{font-family:ui-sans-serif,system-ui,sans-serif;font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:#6a6258}.word{font-size:1.85rem;letter-spacing:.1em;margin-top:2px}.meta{text-align:right;font-family:ui-sans-serif,system-ui,sans-serif;font-size:13px;color:#6a6258}.meta strong{display:block;color:#1c1814;font-weight:650}.parties{display:grid;gap:16px;margin-bottom:20px}@media(min-width:560px){.parties{grid-template-columns:1fr 1fr}}.k{font-family:ui-sans-serif,system-ui,sans-serif;font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:#6a6258;margin-bottom:4px}.v{white-space:pre-wrap;word-break:break-word}table{width:100%;border-collapse:collapse;font:14px/1.4 ui-sans-serif,system-ui,sans-serif;margin:0 0 16px}th,td{text-align:left;padding:8px 0;border-bottom:1px solid #d9d0c3;vertical-align:top}th{font-size:11px;text-transform:uppercase;letter-spacing:.05em;color:#6a6258}td.num,th.num{text-align:right;font-variant-numeric:tabular-nums}.sum{margin-left:auto;width:min(280px,100%);font:14px/1.4 ui-sans-serif,system-ui,sans-serif}.sum div{display:flex;justify-content:space-between;gap:12px;padding:6px 0;font-variant-numeric:tabular-nums}.sum .grand{border-top:2px solid #1c1814;margin-top:4px;padding-top:10px;font-weight:750;font-size:1.05rem}.note{margin-top:22px;color:#6a6258;font-family:ui-sans-serif,system-ui,sans-serif;font-size:12px}.intro{margin:0 0 16px}.badge{display:inline-block;font-size:12px;font-weight:650;padding:4px 8px;border-radius:999px;background:#f8eadc;color:#8a4b12;margin:0 0 14px}.lmeta{display:grid;gap:10px;margin:0 0 18px;grid-template-columns:repeat(auto-fit,minmax(140px,1fr))}.lmeta div{border:1px solid #d9d0c3;border-radius:10px;padding:10px 12px;background:#fff}.lmeta span{display:block;font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:#6a6258;margin:0 0 4px}.amount{font-size:2rem;letter-spacing:-.03em;margin:0 0 14px}.body p{margin:0 0 12px}@media print{body{background:#fff}main{padding:0}.sheet{border:0;width:100%;padding:12mm}}";
  }

  function wrapDownload(title, inner) {
    return "<!doctype html>\n<html lang=\"nl\">\n<head>\n<meta charset=\"utf-8\">\n" +
      "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n" +
      "<title>" + escapeHtml(title) + "</title>\n<style>\n" + downloadCss() + "\n</style>\n" +
      "</head>\n<body>\n<main>\n" + inner + "\n</main>\n</body>\n</html>\n";
  }

  function downloadFile(filename, html) {
    var blob = new Blob([html], { type: "text/html;charset=utf-8" });
    var url = URL.createObjectURL(blob);
    var a = document.createElement("a");
    a.href = url;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    a.remove();
    URL.revokeObjectURL(url);
  }

  function copyPayTo(statusEl) {
    function ok() {
      statusEl.textContent = "Copied. Send exactly 399 USDC on Solana.";
    }
    function fail() {
      statusEl.textContent = "Copy failed. Select the address.";
    }
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(PAY_TO).then(ok, fail);
    } else {
      fail();
    }
  }

  function setStatus(el, msg) {
    if (!el) return;
    if (msg) {
      el.textContent = msg;
      el.classList.remove("hidden");
    } else {
      el.textContent = "";
      el.classList.add("hidden");
    }
  }

  function setError(el, msg) {
    if (!el) return;
    if (msg) {
      el.textContent = msg;
      el.classList.remove("hidden");
    } else {
      el.textContent = "";
      el.classList.add("hidden");
    }
  }

  function addLineRow(container, desc, qty, price, onChange) {
    var wrap = document.createElement("div");
    wrap.className = "line";
    wrap.innerHTML =
      "<div class=\"line-head\"><span>Item</span>" +
      "<button type=\"button\" class=\"danger remove\">Remove</button></div>" +
      "<label class=\"field\"><span>Omschrijving</span>" +
      "<input class=\"desc\" type=\"text\" autocomplete=\"off\"></label>" +
      "<div class=\"row two\">" +
      "<label class=\"field\"><span>Aantal</span>" +
      "<input class=\"qty\" type=\"text\" inputmode=\"decimal\" autocomplete=\"off\"></label>" +
      "<label class=\"field\"><span>Prijs excl. BTW</span>" +
      "<input class=\"price\" type=\"text\" inputmode=\"decimal\" autocomplete=\"off\"></label>" +
      "</div>";
    wrap.querySelector(".desc").value = desc || "";
    wrap.querySelector(".qty").value = qty || "";
    wrap.querySelector(".price").value = price || "";
    wrap.querySelector(".remove").addEventListener("click", function () {
      if (container.querySelectorAll(".line").length <= 1) {
        wrap.querySelector(".desc").value = "";
        wrap.querySelector(".qty").value = "";
        wrap.querySelector(".price").value = "";
        onChange();
        return;
      }
      wrap.remove();
      onChange();
    });
    wrap.querySelector(".desc").addEventListener("input", onChange);
    wrap.querySelector(".qty").addEventListener("input", onChange);
    wrap.querySelector(".price").addEventListener("input", onChange);
    container.appendChild(wrap);
  }

  function renderLineRows(container, lines, onChange) {
    container.innerHTML = "";
    var list = lines && lines.length ? lines : [{ desc: "", qty: "", price: "" }];
    var i;
    for (i = 0; i < list.length; i++) {
      addLineRow(container, list[i].desc, list[i].qty, list[i].price, onChange);
    }
  }

  function validateForm(d) {
    if (!d.leadName) return "Vul een naam in.";
    if (!d.leadEmail) return "Vul een e-mail in.";
    if (!looksLikeEmail(d.leadEmail)) return "E-mail ziet er niet geldig uit.";
    if (!d.leadJob) return "Beschrijf de job.";
    return "";
  }

  function validateQuoteOrInvoice(d, kind) {
    if (!d.sellerName) return "Enter the seller name.";
    if (!d.clientName) return "Enter the client name.";
    if (kind === "offerte" && !d.offerteNo) return "Enter an offerte number.";
    if (kind === "offerte" && !d.offerteDate) return "Enter an offerte date.";
    if (kind === "invoice" && !d.invoiceNo) return "Enter an invoice number.";
    if (kind === "invoice" && !d.invoiceDate) return "Enter an invoice date.";
    if (d.vatRate === null) return "BTW rate must be a number 0 or greater.";
    if (d.vatRate > 100) return "BTW rate must be 100 or less.";
    var i, filled = 0;
    for (i = 0; i < d.lines.length; i++) {
      if (d.lines[i].invalid) return "Each line needs a quantity and a unit price (use 0 or more).";
      if (!d.lines[i].desc) return "Each filled line needs a description.";
      filled += 1;
    }
    if (filled < 1) return "Add at least one line item.";
    return "";
  }

  function validateReminder(d) {
    if (!d.sellerName) return "Vul de afzender in.";
    if (!d.clientName) return "Vul de klant in.";
    if (!d.clientMail) return "Vul het klant-mailadres in.";
    if (!looksLikeEmail(d.clientMail)) return "Klant-mail ziet er niet geldig uit.";
    if (d.sellerMail && !looksLikeEmail(d.sellerMail)) return "Afzender-mail ziet er niet geldig uit.";
    if (!d.invoiceNo) return "Vul een factuurnummer in.";
    if (!d.dueDate) return "Vul een vervaldatum in.";
    if (d.amount === null) return "Bedrag moet een getal 0 of groter zijn.";
    if (!d.reminderBody) return "Schrijf de brief.";
    return "";
  }

  function daysOverdue(iso) {
    if (!iso) return null;
    var due = new Date(iso + "T00:00:00");
    if (isNaN(due.getTime())) return null;
    var now = new Date();
    var today = new Date(now.getFullYear(), now.getMonth(), now.getDate());
    return Math.round((today - due) / 86400000);
  }

  function offerteInner(d, tot) {
    var rateLabel = (d.vatRate == null ? "—" : String(d.vatRate).replace(".", ",")) + "%";
    return "<article class=\"sheet\">" +
      "<header class=\"sheet-top top\">" +
      "<div><div class=\"kicker\">" + escapeHtml(d.sellerName || "Studio Noord") + "</div>" +
      "<div class=\"word\">OFFERTE</div></div>" +
      "<div class=\"meta\">Nr. <strong>" + escapeHtml(d.offerteNo || "—") + "</strong>" +
      "Datum <strong>" + escapeHtml(formatDateNl(d.offerteDate) || "—") + "</strong>" +
      (d.offerteValid ? "Geldig tot <strong>" + escapeHtml(formatDateNl(d.offerteValid)) + "</strong>" : "") +
      "</div></header>" +
      (d.offerteIntro ? "<p class=\"intro\">" + escapeHtml(d.offerteIntro) + "</p>" : "") +
      "<div class=\"parties\">" +
      "<div><div class=\"k\">Van</div><div class=\"v\">" +
      partyHtml(d.sellerName, d.sellerAddress, d.sellerVat, d.sellerMail, "Studio Noord") +
      "</div></div>" +
      "<div><div class=\"k\">Voor</div><div class=\"v\">" +
      partyHtml(d.clientName, d.clientAddress, d.clientVat, d.clientMail, "Client BV") +
      "</div></div></div>" +
      linesTableHtml(d.lines) +
      "<div class=\"sum-box sum\">" +
      "<div><span>Totaal excl. BTW</span><span>" + escapeHtml(formatEur(tot.exclCents)) + "</span></div>" +
      "<div><span>BTW " + escapeHtml(rateLabel) + "</span><span>" + escapeHtml(formatEur(tot.vatCents)) + "</span></div>" +
      "<div class=\"grand\"><span>Totaal incl. BTW</span><span>" + escapeHtml(formatEur(tot.inclCents)) + "</span></div>" +
      "</div>" +
      "<p class=\"pay-note note\">Dit is een offerte, geen factuur. Bedragen in euro. 21% is het standaard Belgische BTW-tarief tenzij anders afgesproken.</p>" +
      "</article>";
  }

  function invoiceInner(d, tot) {
    var rateLabel = (d.vatRate == null ? "—" : String(d.vatRate).replace(".", ",")) + "%";
    return "<article class=\"sheet\">" +
      "<header class=\"sheet-top top\">" +
      "<div><div class=\"kicker\">" + escapeHtml(d.sellerName || "Studio Noord") + "</div>" +
      "<div class=\"word\">FACTUUR</div></div>" +
      "<div class=\"meta\">Nr. <strong>" + escapeHtml(d.invoiceNo || "—") + "</strong>" +
      "Datum <strong>" + escapeHtml(formatDateNl(d.invoiceDate) || "—") + "</strong>" +
      (d.dueDate ? "Vervaldatum <strong>" + escapeHtml(formatDateNl(d.dueDate)) + "</strong>" : "") +
      "</div></header>" +
      "<div class=\"parties\">" +
      "<div><div class=\"k\">Verkoper</div><div class=\"v\">" +
      partyHtml(d.sellerName, d.sellerAddress, d.sellerVat, d.sellerMail, "Studio Noord") +
      "</div></div>" +
      "<div><div class=\"k\">Klant</div><div class=\"v\">" +
      partyHtml(d.clientName, d.clientAddress, d.clientVat, "", "Client BV") +
      "</div></div></div>" +
      linesTableHtml(d.lines) +
      "<div class=\"sum-box sum\">" +
      "<div><span>Totaal excl. BTW</span><span>" + escapeHtml(formatEur(tot.exclCents)) + "</span></div>" +
      "<div><span>BTW " + escapeHtml(rateLabel) + "</span><span>" + escapeHtml(formatEur(tot.vatCents)) + "</span></div>" +
      "<div class=\"grand\"><span>Totaal incl. BTW</span><span>" + escapeHtml(formatEur(tot.inclCents)) + "</span></div>" +
      "</div>" +
      "<p class=\"pay-note note\">Betaal binnen de vermelde termijn. Vermeld factuurnummer " +
      escapeHtml(d.invoiceNo || "—") + " als mededeling. Bedragen in euro. B2C: PDF per mail blijft toegelaten. B2B: sinds 1 januari 2026 is een PDF geen wettelijke factuur in België (Peppol). Dit bestand is geen Peppol-document.</p>" +
      "</article>";
  }

  function reminderInner(d) {
    var overdue = daysOverdue(d.dueDate);
    var badge = (overdue != null && overdue > 0)
      ? "<div class=\"badge\">Achterstallig · " + overdue + " dagen</div>"
      : "<div class=\"badge\">Herinnering</div>";
    var amt = d.amount === null ? "—" : formatEur(toCents(d.amount));
    var paras = escapeHtml(d.reminderBody || "").split(/\n\n+/).map(function (p) {
      return "<p>" + p.replace(/\n/g, "<br>") + "</p>";
    }).join("");
    return "<article class=\"sheet letter\">" +
      "<div class=\"kicker\">" + escapeHtml(d.sellerName || "Studio Noord") + "</div>" +
      "<h3>BETALINGSHERINNERING</h3>" +
      badge +
      "<div class=\"letter-meta lmeta\">" +
      "<div><span>Aan</span><strong>" + escapeHtml(d.clientName || "—") + "</strong></div>" +
      "<div><span>Factuur</span><strong>" + escapeHtml(d.invoiceNo || "—") + "</strong></div>" +
      "<div><span>Vervaldatum</span><strong>" + escapeHtml(formatDateNl(d.dueDate) || "—") + "</strong></div>" +
      "<div><span>Van</span><strong>" + escapeHtml(d.sellerMail || "hello@studio.example") + "</strong></div>" +
      "</div>" +
      "<div class=\"amount\">" + escapeHtml(amt) + "</div>" +
      "<div class=\"body\">" + paras + "</div>" +
      "</article>";
  }

  function leadInner(d) {
    function row(label, value) {
      if (!value) return "";
      return "<div><div class=\"k\">" + escapeHtml(label) + "</div><div class=\"v\">" + escapeHtml(value) + "</div></div>";
    }
    return "<article class=\"sheet\">" +
      "<div class=\"kicker\">" + escapeHtml(d.sellerName || "Studio Noord") + "</div>" +
      "<div class=\"word\">INTAKE</div>" +
      "<div class=\"parties\" style=\"margin-top:18px\">" +
      row("Naam", d.leadName) +
      row("Bedrijf", d.leadCompany) +
      row("E-mail", d.leadEmail) +
      row("Telefoon", d.leadPhone) +
      row("Deadline", d.leadDeadline ? formatDateNl(d.leadDeadline) : "") +
      row("Budget", d.leadBudget) +
      "</div>" +
      "<div><div class=\"k\">Job</div><div class=\"v\">" + escapeHtml(d.leadJob) + "</div></div>" +
      (d.leadNotes ? "<div style=\"margin-top:14px\"><div class=\"k\">Notities</div><div class=\"v\">" + escapeHtml(d.leadNotes) + "</div></div>" : "") +
      "<p class=\"note\">Mail: " + escapeHtml(d.sellerMail || "hello@studio.example") + "</p>" +
      "</article>";
  }

  function val(id, fallback) {
    var el = $(id);
    if (!el) return fallback == null ? "" : fallback;
    return el.value;
  }

  function bindValue(id, value) {
    var el = $(id);
    if (el) el.value = value == null ? "" : value;
  }

  function collectParties() {
    return {
      sellerName: val("sellerName"),
      sellerAddress: val("sellerAddress"),
      sellerVat: val("sellerVat"),
      sellerMail: val("sellerMail"),
      clientName: val("clientName"),
      clientAddress: val("clientAddress"),
      clientVat: val("clientVat"),
      clientMail: val("clientMail")
    };
  }

  function applyLeadToOfferte(state) {
    if (state.leadCompany) state.clientName = state.leadCompany;
    else if (state.leadName) state.clientName = state.leadName;
    if (state.leadEmail) state.clientMail = state.leadEmail;
    if (state.leadJob && (!state.lines || !state.lines[0] || !state.lines[0].desc)) {
      state.lines = [{ desc: state.leadJob, qty: "1", price: state.leadBudget || "" }];
    }
    if (state.leadJob && !state.offerteIntro) {
      state.offerteIntro = "Offerte op basis van de intake van " + state.leadName + ".";
    }
    return state;
  }

  function applyOfferteToInvoice(state) {
    return state;
  }

  function applyInvoiceToReminder(state, tot) {
    var incl = tot ? tot.inclCents : 0;
    state.reminderAmount = formatEur(incl).replace(" €", "");
    state.reminderBody =
      "Beste " + state.clientName + ",\n\n" +
      "Onze factuur " + state.invoiceNo +
      " van " + formatDateNl(state.invoiceDate) +
      " is vervallen op " + formatDateNl(state.dueDate) +
      ". Het openstaande bedrag is " + formatEur(incl) + " incl. " +
      String(state.vatRate).replace(".", ",") + "% BTW.\n\n" +
      "Gelieve te betalen met vermelding van het factuurnummer. Vragen? Antwoord op dit bericht of gebruik " +
      state.sellerMail + ".\n\n" +
      "Met vriendelijke groeten,\n" +
      state.sellerName;
    return state;
  }

  function formFieldsHtml() {
    return "<section class=\"card\">" +
      "<h2>Lead</h2>" +
      "<div id=\"error\" class=\"error hidden\" role=\"alert\"></div>" +
      "<div class=\"row two\">" +
      "<label class=\"field\"><span>Naam</span><input id=\"leadName\" type=\"text\" autocomplete=\"name\"></label>" +
      "<label class=\"field\"><span>Bedrijf (optioneel)</span><input id=\"leadCompany\" type=\"text\"></label>" +
      "</div>" +
      "<div class=\"row two\">" +
      "<label class=\"field\"><span>E-mail</span><input id=\"leadEmail\" type=\"email\" autocomplete=\"email\"></label>" +
      "<label class=\"field\"><span>Telefoon (optioneel)</span><input id=\"leadPhone\" type=\"text\"></label>" +
      "</div>" +
      "<label class=\"field\"><span>Wat moet er gebeuren?</span><textarea id=\"leadJob\"></textarea></label>" +
      "<div class=\"row two\">" +
      "<label class=\"field\"><span>Gewenste deadline</span><input id=\"leadDeadline\" type=\"date\"></label>" +
      "<label class=\"field\"><span>Budget (indicatief, EUR)</span><input id=\"leadBudget\" type=\"text\" inputmode=\"decimal\"></label>" +
      "</div>" +
      "<label class=\"field\"><span>Extra notities</span><textarea id=\"leadNotes\"></textarea></label>" +
      "<div class=\"actions\">" +
      "<button type=\"button\" class=\"primary\" id=\"downloadBtn\">Download brief</button>" +
      "<button type=\"button\" class=\"ghost\" id=\"nextBtn\">Naar offerte</button>" +
      "</div>" +
      "<p class=\"ok hidden\" id=\"status\"></p>" +
      "<p class=\"note\">Mailto en demo-mail: hello@studio.example (RFC 2606). Geen Gmail, geen live inbox. De brief bevat geen treasury-adres.</p>" +
      "</section>";
  }

  function quoteInvoiceFieldsHtml(kind) {
    var isOff = kind === "offerte";
    var title = isOff ? "Offerte" : "Factuur";
    var nextLabel = isOff ? "Naar factuur (lijnen meenemen)" : "Naar herinnering";
    var dlLabel = isOff ? "Download HTML offerte" : "Download HTML invoice";
    var numId = isOff ? "offerteNo" : "invoiceNo";
    var dateId = isOff ? "offerteDate" : "invoiceDate";
    var extraDate = isOff
      ? "<label class=\"field\"><span>Geldig tot</span><input id=\"offerteValid\" type=\"date\"></label>"
      : "<label class=\"field\"><span>Vervaldatum</span><input id=\"dueDate\" type=\"date\"></label>";
    var intro = isOff
      ? "<label class=\"field\"><span>Inleiding</span><textarea id=\"offerteIntro\"></textarea></label>"
      : "";
    return "<div class=\"layout split\">" +
      "<div class=\"stack\">" +
      "<section class=\"card\"><h2>Verkoper</h2>" +
      "<label class=\"field\"><span>Naam</span><input id=\"sellerName\" type=\"text\"></label>" +
      "<label class=\"field\"><span>Adres</span><textarea id=\"sellerAddress\"></textarea></label>" +
      "<div class=\"row two\">" +
      "<label class=\"field\"><span>BE BTW / KBO</span><input id=\"sellerVat\" type=\"text\"></label>" +
      "<label class=\"field\"><span>Mail</span><input id=\"sellerMail\" type=\"email\"></label>" +
      "</div></section>" +
      "<section class=\"card\"><h2>Klant</h2>" +
      "<label class=\"field\"><span>Naam</span><input id=\"clientName\" type=\"text\"></label>" +
      "<label class=\"field\"><span>Adres</span><textarea id=\"clientAddress\"></textarea></label>" +
      "<div class=\"row two\">" +
      "<label class=\"field\"><span>BE BTW / KBO</span><input id=\"clientVat\" type=\"text\"></label>" +
      "<label class=\"field\"><span>Mail</span><input id=\"clientMail\" type=\"email\"></label>" +
      "</div></section>" +
      "<section class=\"card\"><h2>" + title + "</h2>" +
      "<div id=\"error\" class=\"error hidden\" role=\"alert\"></div>" +
      "<div class=\"row two\">" +
      "<label class=\"field\"><span>Nummer</span><input id=\"" + numId + "\" type=\"text\"></label>" +
      "<label class=\"field\"><span>Datum</span><input id=\"" + dateId + "\" type=\"date\"></label>" +
      "</div>" +
      "<div class=\"row two\">" + extraDate +
      "<label class=\"field\"><span>BTW-tarief (%)</span><input id=\"vatRate\" type=\"text\" inputmode=\"decimal\"></label>" +
      "</div>" +
      intro +
      "<p class=\"note\">Belgium’s standard rate is 21%. Confirm the rate that applies to this job.</p>" +
      "<h3>Lijnen</h3>" +
      "<div class=\"lines\" id=\"lines\"></div>" +
      "<div class=\"actions\" style=\"margin:10px 0 12px\">" +
      "<button type=\"button\" class=\"ghost\" id=\"addLineBtn\">Add line</button>" +
      "</div>" +
      "<div class=\"totals\">" +
      "<div><span>Excl. BTW</span><span id=\"sumExcl\">0,00 €</span></div>" +
      "<div><span id=\"sumVatLabel\">BTW 21%</span><span id=\"sumVat\">0,00 €</span></div>" +
      "<div class=\"grand\"><span>Incl. BTW</span><span id=\"sumIncl\">0,00 €</span></div>" +
      "</div>" +
      "<div class=\"actions\">" +
      "<button type=\"button\" class=\"primary\" id=\"downloadBtn\">" + dlLabel + "</button>" +
      "<button type=\"button\" class=\"ghost\" id=\"nextBtn\">" + nextLabel + "</button>" +
      "</div>" +
      "<p class=\"ok hidden\" id=\"status\"></p>" +
      "<p class=\"note\">The downloaded file is self-contained. No scripts. No treasury address.</p>" +
      "</section></div>" +
      "<section class=\"card\"><h2>Preview</h2><div id=\"preview\"></div></section>" +
      "</div>";
  }

  function reminderFieldsHtml() {
    return "<div class=\"layout split\">" +
      "<section class=\"card\"><h2>Gegevens</h2>" +
      "<div id=\"error\" class=\"error hidden\" role=\"alert\"></div>" +
      "<div class=\"row two\">" +
      "<label class=\"field\"><span>Van</span><input id=\"sellerName\" type=\"text\"></label>" +
      "<label class=\"field\"><span>Van-mail</span><input id=\"sellerMail\" type=\"email\"></label>" +
      "</div>" +
      "<div class=\"row two\">" +
      "<label class=\"field\"><span>Aan</span><input id=\"clientName\" type=\"text\"></label>" +
      "<label class=\"field\"><span>Aan-mail</span><input id=\"clientMail\" type=\"email\"></label>" +
      "</div>" +
      "<div class=\"row two\">" +
      "<label class=\"field\"><span>Factuurnummer</span><input id=\"invoiceNo\" type=\"text\"></label>" +
      "<label class=\"field\"><span>Vervaldatum</span><input id=\"dueDate\" type=\"date\"></label>" +
      "</div>" +
      "<label class=\"field\"><span>Bedrag incl. BTW (EUR)</span><input id=\"reminderAmount\" type=\"text\" inputmode=\"decimal\"></label>" +
      "<label class=\"field\"><span>Brief</span><textarea class=\"tall\" id=\"reminderBody\"></textarea></label>" +
      "<div class=\"actions\">" +
      "<button type=\"button\" class=\"primary\" id=\"downloadBtn\">Download reminder</button>" +
      "<button type=\"button\" class=\"ghost\" id=\"mailBtn\">Open mailto</button>" +
      "</div>" +
      "<p class=\"ok hidden\" id=\"status\"></p>" +
      "<p class=\"note\">Mailto uses RFC 2606 addresses only in this demo (billing@client.example).</p>" +
      "</section>" +
      "<section class=\"card\"><h2>Preview</h2><div id=\"preview\"></div></section>" +
      "</div>";
  }

  function go(href) {
    window.location.href = href;
  }

  function fillForm(state) {
    bindValue("leadName", state.leadName);
    bindValue("leadCompany", state.leadCompany);
    bindValue("leadEmail", state.leadEmail);
    bindValue("leadPhone", state.leadPhone);
    bindValue("leadJob", state.leadJob);
    bindValue("leadDeadline", state.leadDeadline);
    bindValue("leadBudget", state.leadBudget);
    bindValue("leadNotes", state.leadNotes);
  }

  function readFormInto(state) {
    state.leadName = val("leadName");
    state.leadCompany = val("leadCompany");
    state.leadEmail = val("leadEmail");
    state.leadPhone = val("leadPhone");
    state.leadJob = val("leadJob");
    state.leadDeadline = val("leadDeadline");
    state.leadBudget = val("leadBudget");
    state.leadNotes = val("leadNotes");
    return state;
  }

  function fillParties(state) {
    bindValue("sellerName", state.sellerName);
    bindValue("sellerAddress", state.sellerAddress);
    bindValue("sellerVat", state.sellerVat);
    bindValue("sellerMail", state.sellerMail);
    bindValue("clientName", state.clientName);
    bindValue("clientAddress", state.clientAddress);
    bindValue("clientVat", state.clientVat);
    bindValue("clientMail", state.clientMail);
    bindValue("vatRate", state.vatRate);
  }

  function readPartiesInto(state) {
    var p = collectParties();
    var key;
    for (key in p) {
      if (Object.prototype.hasOwnProperty.call(p, key)) state[key] = p[key];
    }
    state.vatRate = val("vatRate");
    return state;
  }

  function currentDoc(kind, state, linesEl) {
    var lines = readLinesFrom(linesEl);
    var vat = parseDecimal(val("vatRate", state.vatRate));
    var d = {
      sellerName: val("sellerName", state.sellerName).trim(),
      sellerAddress: val("sellerAddress", state.sellerAddress).trim(),
      sellerVat: val("sellerVat", state.sellerVat).trim(),
      sellerMail: val("sellerMail", state.sellerMail).trim(),
      clientName: val("clientName", state.clientName).trim(),
      clientAddress: val("clientAddress", state.clientAddress).trim(),
      clientVat: val("clientVat", state.clientVat).trim(),
      clientMail: val("clientMail", state.clientMail).trim(),
      offerteNo: val("offerteNo", state.offerteNo).trim(),
      offerteDate: val("offerteDate", state.offerteDate).trim(),
      offerteValid: val("offerteValid", state.offerteValid).trim(),
      offerteIntro: val("offerteIntro", state.offerteIntro).trim(),
      invoiceNo: val("invoiceNo", state.invoiceNo).trim(),
      invoiceDate: val("invoiceDate", state.invoiceDate).trim(),
      dueDate: val("dueDate", state.dueDate).trim(),
      vatRate: vat,
      lines: lines
    };
    return d;
  }

  function persistFromDom(kind, state, linesEl) {
    if (kind === "form") return readFormInto(state);
    if (kind === "reminder") {
      state.sellerName = val("sellerName").trim();
      state.sellerMail = val("sellerMail").trim();
      state.clientName = val("clientName").trim();
      state.clientMail = val("clientMail").trim();
      state.invoiceNo = val("invoiceNo").trim();
      state.dueDate = val("dueDate").trim();
      state.reminderAmount = val("reminderAmount").trim();
      state.reminderBody = val("reminderBody");
      return state;
    }
    readPartiesInto(state);
    if (kind === "offerte") {
      state.offerteNo = val("offerteNo");
      state.offerteDate = val("offerteDate");
      state.offerteValid = val("offerteValid");
      state.offerteIntro = val("offerteIntro");
    }
    if (kind === "invoice") {
      state.invoiceNo = val("invoiceNo");
      state.invoiceDate = val("invoiceDate");
      state.dueDate = val("dueDate");
    }
    if (linesEl) state.lines = linesForSave(linesEl);
    return state;
  }

  function wireForm(state, opts) {
    fillForm(state);
    var errorEl = $("error");
    var statusEl = $("status");

    function snapshot() {
      persistFromDom("form", state);
      saveState(state);
      return {
        leadName: state.leadName.trim(),
        leadCompany: state.leadCompany.trim(),
        leadEmail: state.leadEmail.trim(),
        leadPhone: state.leadPhone.trim(),
        leadJob: state.leadJob.trim(),
        leadDeadline: state.leadDeadline.trim(),
        leadBudget: state.leadBudget.trim(),
        leadNotes: state.leadNotes.trim(),
        sellerName: state.sellerName,
        sellerMail: state.sellerMail
      };
    }

    ["leadName", "leadCompany", "leadEmail", "leadPhone", "leadJob", "leadDeadline", "leadBudget", "leadNotes"].forEach(function (id) {
      var el = $(id);
      if (!el) return;
      el.addEventListener("input", function () { snapshot(); });
      el.addEventListener("change", function () { snapshot(); });
    });

    $("downloadBtn").addEventListener("click", function () {
      var d = snapshot();
      var err = validateForm(d);
      if (err) { setError(errorEl, err); setStatus(statusEl, ""); return; }
      setError(errorEl, "");
      var name = "intake-" + slug(d.leadName) + ".html";
      downloadFile(name, wrapDownload("Intake — " + d.leadName, leadInner(d)));
      setStatus(statusEl, "Downloaded " + name + ".");
    });

    $("nextBtn").addEventListener("click", function () {
      var d = snapshot();
      var err = validateForm(d);
      if (err) { setError(errorEl, err); return; }
      setError(errorEl, "");
      applyLeadToOfferte(state);
      saveState(state);
      if (opts && opts.onNext) opts.onNext("offerte");
      else go("offerte.html");
    });
  }

  function wireQuoteInvoice(kind, state, opts) {
    fillParties(state);
    if (kind === "offerte") {
      bindValue("offerteNo", state.offerteNo);
      bindValue("offerteDate", state.offerteDate);
      bindValue("offerteValid", state.offerteValid);
      bindValue("offerteIntro", state.offerteIntro);
    } else {
      bindValue("invoiceNo", state.invoiceNo);
      bindValue("invoiceDate", state.invoiceDate);
      bindValue("dueDate", state.dueDate);
    }
    var linesEl = $("lines");
    var errorEl = $("error");
    var statusEl = $("status");

    function refresh() {
      persistFromDom(kind, state, linesEl);
      saveState(state);
      var d = currentDoc(kind, state, linesEl);
      var err = validateQuoteOrInvoice(d, kind);
      setError(errorEl, err);
      $("downloadBtn").disabled = Boolean(err);
      $("nextBtn").disabled = Boolean(err);
      var tot = (d.vatRate === null)
        ? { exclCents: 0, vatCents: 0, inclCents: 0 }
        : totalsOf(d.lines, d.vatRate);
      var rateText = d.vatRate === null ? "—" : String(d.vatRate).replace(".", ",") + "%";
      $("sumExcl").textContent = formatEur(tot.exclCents);
      $("sumVat").textContent = formatEur(tot.vatCents);
      $("sumIncl").textContent = formatEur(tot.inclCents);
      $("sumVatLabel").textContent = "BTW " + rateText;
      $("preview").innerHTML = kind === "offerte" ? offerteInner(d, tot) : invoiceInner(d, tot);
      return { d: d, err: err, tot: tot };
    }

    renderLineRows(linesEl, state.lines, refresh);
    $("addLineBtn").addEventListener("click", function () {
      addLineRow(linesEl, "", "", "", refresh);
      refresh();
    });

    ["sellerName", "sellerAddress", "sellerVat", "sellerMail", "clientName", "clientAddress", "clientVat", "clientMail", "vatRate", "offerteNo", "offerteDate", "offerteValid", "offerteIntro", "invoiceNo", "invoiceDate", "dueDate"].forEach(function (id) {
      var el = $(id);
      if (!el) return;
      el.addEventListener("input", refresh);
      el.addEventListener("change", refresh);
    });

    $("downloadBtn").addEventListener("click", function () {
      var r = refresh();
      if (r.err) return;
      var name, html;
      if (kind === "offerte") {
        name = "offerte-" + slug(r.d.offerteNo || r.d.clientName) + ".html";
        html = wrapDownload("Offerte " + r.d.offerteNo, offerteInner(r.d, r.tot));
      } else {
        name = (r.d.invoiceNo || "factuur").replace(/[^A-Za-z0-9._-]+/g, "-") + ".html";
        html = wrapDownload("Factuur " + r.d.invoiceNo, invoiceInner(r.d, r.tot));
      }
      downloadFile(name, html);
      setStatus(statusEl, "Downloaded " + name + ".");
    });

    $("nextBtn").addEventListener("click", function () {
      var r = refresh();
      if (r.err) return;
      if (kind === "offerte") {
        applyOfferteToInvoice(state);
        saveState(state);
        if (opts && opts.onNext) opts.onNext("invoice");
        else go("invoice.html");
      } else {
        applyInvoiceToReminder(state, r.tot);
        saveState(state);
        if (opts && opts.onNext) opts.onNext("reminder");
        else go("reminder.html");
      }
    });

    refresh();
  }

  function parseAmountField(raw) {
    var n = parseDecimal(raw);
    return n;
  }

  function invoiceTotalsFromState(state) {
    var lines = [];
    var i, qty, price, unitCents;
    for (i = 0; i < state.lines.length; i++) {
      qty = parseDecimal(state.lines[i].qty);
      price = parseDecimal(state.lines[i].price);
      if (qty === null || price === null) continue;
      unitCents = toCents(price);
      lines.push({ invalid: false, exclCents: Math.round(qty * unitCents) });
    }
    var vat = parseDecimal(state.vatRate);
    if (vat === null) return { exclCents: 0, vatCents: 0, inclCents: 0 };
    return totalsOf(lines, vat);
  }

  function wireReminder(state, opts) {
    bindValue("sellerName", state.sellerName);
    bindValue("sellerMail", state.sellerMail);
    bindValue("clientName", state.clientName);
    bindValue("clientMail", state.clientMail);
    bindValue("invoiceNo", state.invoiceNo);
    bindValue("dueDate", state.dueDate);
    var tot = invoiceTotalsFromState(state);
    state.reminderAmount = formatEur(tot.inclCents).replace(" €", "");
    if (!state.reminderBody) applyInvoiceToReminder(state, tot);
    bindValue("reminderAmount", state.reminderAmount);
    bindValue("reminderBody", state.reminderBody);

    var errorEl = $("error");
    var statusEl = $("status");

    function current() {
      persistFromDom("reminder", state);
      saveState(state);
      return {
        sellerName: state.sellerName,
        sellerMail: state.sellerMail,
        clientName: state.clientName,
        clientMail: state.clientMail,
        invoiceNo: state.invoiceNo,
        dueDate: state.dueDate,
        amount: parseAmountField(state.reminderAmount),
        reminderBody: state.reminderBody.trim()
      };
    }

    function refresh() {
      var d = current();
      var err = validateReminder(d);
      setError(errorEl, err);
      $("downloadBtn").disabled = Boolean(err);
      $("mailBtn").disabled = Boolean(err);
      $("preview").innerHTML = reminderInner(d);
      return { d: d, err: err };
    }

    ["sellerName", "sellerMail", "clientName", "clientMail", "invoiceNo", "dueDate", "reminderAmount", "reminderBody"].forEach(function (id) {
      $(id).addEventListener("input", refresh);
      $(id).addEventListener("change", refresh);
    });

    $("downloadBtn").addEventListener("click", function () {
      var r = refresh();
      if (r.err) return;
      var name = "herinnering-" + slug(r.d.invoiceNo) + ".html";
      downloadFile(name, wrapDownload("Herinnering " + r.d.invoiceNo, reminderInner(r.d)));
      setStatus(statusEl, "Downloaded " + name + ".");
    });

    $("mailBtn").addEventListener("click", function () {
      var r = refresh();
      if (r.err) return;
      var subject = "Herinnering " + r.d.invoiceNo + " — " + (r.d.amount === null ? "" : formatEur(toCents(r.d.amount)));
      window.location.href = "mailto:" + r.d.clientMail +
        "?subject=" + encodeURIComponent(subject) +
        "&body=" + encodeURIComponent(r.d.reminderBody);
      setStatus(statusEl, "Mailto opened to " + r.d.clientMail + ".");
    });

    refresh();
  }

  var WIZARD_STEPS = [
    { id: "form", n: "1", label: "Form" },
    { id: "offerte", n: "2", label: "Offerte" },
    { id: "invoice", n: "3", label: "Factuur" },
    { id: "reminder", n: "4", label: "Herinnering" }
  ];

  function railHtml(current) {
    var html = "<ol class=\"rail\" aria-label=\"Pipeline\">";
    var i, s;
    for (i = 0; i < WIZARD_STEPS.length; i++) {
      s = WIZARD_STEPS[i];
      html += "<li><button type=\"button\" data-step=\"" + s.id + "\"" +
        (s.id === current ? " aria-current=\"step\"" : "") +
        "><span class=\"n\">Stap " + s.n + "</span>" + s.label + "</button></li>";
    }
    return html + "</ol>";
  }

  function mountStep(kind, mount, state, opts) {
    if (kind === "form") {
      mount.innerHTML = formFieldsHtml();
      wireForm(state, opts);
      return;
    }
    if (kind === "offerte") {
      mount.innerHTML = quoteInvoiceFieldsHtml("offerte");
      wireQuoteInvoice("offerte", state, opts);
      return;
    }
    if (kind === "invoice") {
      mount.innerHTML = quoteInvoiceFieldsHtml("invoice");
      wireQuoteInvoice("invoice", state, opts);
      return;
    }
    if (kind === "reminder") {
      mount.innerHTML = reminderFieldsHtml();
      wireReminder(state, opts);
      return;
    }
  }

  function mountWizard(root) {
    var state = loadState();
    var current = "form";
    root.innerHTML = railHtml(current) + "<div id=\"stepMount\"></div>";
    var stepMount = $("stepMount");

    function show(kind) {
      current = kind;
      var buttons = root.querySelectorAll("[data-step]");
      var i;
      for (i = 0; i < buttons.length; i++) {
        if (buttons[i].getAttribute("data-step") === kind) buttons[i].setAttribute("aria-current", "step");
        else buttons[i].removeAttribute("aria-current");
      }
      mountStep(kind, stepMount, state, {
        onNext: function (next) { show(next); }
      });
    }

    root.addEventListener("click", function (e) {
      var btn = e.target.closest("[data-step]");
      if (!btn || !root.contains(btn)) return;
      persistCurrent();
      show(btn.getAttribute("data-step"));
    });

    function persistCurrent() {
      var linesEl = $("lines");
      persistFromDom(current, state, linesEl);
      saveState(state);
    }

    show("form");
  }

  function mount(kind) {
    var root = $("mount");
    if (!root) return;
    var state = loadState();
    if (kind === "wizard") {
      mountWizard(root);
      return;
    }
    mountStep(kind, root, state, null);
  }

  function bindSell() {
    var btn = $("copyBtn");
    var status = $("copyStatus");
    if (!btn || !status) return;
    btn.addEventListener("click", function () { copyPayTo(status); });
    var reset = $("resetDemo");
    if (reset) {
      reset.addEventListener("click", function () {
        resetState();
        var mount = $("mount");
        if (mount) mountWizard(mount);
        status.textContent = "Demo reset to Studio Noord / Client BV.";
      });
    }
  }

  global.Pipeline = {
    PAY_TO: PAY_TO,
    USDC_MINT: USDC_MINT,
    PRICE: PRICE,
    DEMO: DEMO,
    mount: mount,
    bindSell: bindSell,
    formatEur: formatEur,
    totalsOf: totalsOf,
    parseDecimal: parseDecimal,
    toCents: toCents,
    loadState: loadState,
    resetState: resetState
  };
})(window);
