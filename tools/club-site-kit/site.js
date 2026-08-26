(function () {
  "use strict";

  var PAY_TO = "96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3";
  var club = window.CLUB_KIT || {};

  function closest(el, sel) {
    while (el && el.nodeType === 1) {
      if (el.matches(sel)) return el;
      el = el.parentElement;
    }
    return null;
  }

  function applyClub() {
    var name = club.name || "Voorbeeldclub vzw";
    var city = club.city || "Voorbeeldstad";
    var sport = club.sport || "Sport en ontspanning";
    var email = club.email || "info@voorbeeldclub.example";
    var root = document.documentElement;
    if (club.colors) {
      if (club.colors.pine) root.style.setProperty("--pine", club.colors.pine);
      if (club.colors.pineDeep) root.style.setProperty("--pine-deep", club.colors.pineDeep);
      if (club.colors.moss) root.style.setProperty("--moss", club.colors.moss);
    }
    var nodes = document.querySelectorAll("[data-club]");
    var i;
    for (i = 0; i < nodes.length; i++) {
      switch (nodes[i].getAttribute("data-club")) {
        case "name":
          nodes[i].textContent = name;
          break;
        case "city":
          nodes[i].textContent = city;
          break;
        case "sport":
          nodes[i].textContent = sport;
          break;
        case "email":
          nodes[i].textContent = email;
          break;
        case "feeAdult":
          nodes[i].textContent = club.feeAdult || "€ 40";
          break;
        case "feeYouth":
          nodes[i].textContent = club.feeYouth || "€ 25";
          break;
        case "feeFamily":
          nodes[i].textContent = club.feeFamily || "€ 90";
          break;
        default:
          break;
      }
    }
    var mails = document.querySelectorAll("[data-club-mail]");
    for (i = 0; i < mails.length; i++) {
      var href = mails[i].getAttribute("href") || "";
      if (href.indexOf("mailto:") === 0) {
        var rest = href.slice("mailto:".length);
        var at = rest.indexOf("?");
        var qs = at === -1 ? "" : rest.slice(at);
        mails[i].setAttribute("href", "mailto:" + email + qs);
      } else {
        mails[i].setAttribute("href", "mailto:" + email);
      }
    }
  }

  function copyText(text, statusEl) {
    function ok() {
      if (statusEl) {
        statusEl.textContent = "Adres gekopieerd. Stuur exact 900 USDC op Solana.";
        statusEl.classList.remove("is-err");
      }
    }
    function fail() {
      if (statusEl) {
        statusEl.textContent = "Kopieer handmatig: selecteer het adres.";
        statusEl.classList.add("is-err");
      }
    }
    if (!text) {
      fail();
      return;
    }
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(ok).catch(function () {
        fallbackCopy(text, ok, fail);
      });
    } else {
      fallbackCopy(text, ok, fail);
    }
  }

  function fallbackCopy(text, ok, fail) {
    var ta = document.createElement("textarea");
    ta.value = text;
    ta.setAttribute("readonly", "");
    ta.style.position = "fixed";
    ta.style.left = "-9999px";
    document.body.appendChild(ta);
    ta.select();
    var worked = false;
    try {
      worked = document.execCommand("copy");
    } catch (e) {
      worked = false;
    }
    document.body.removeChild(ta);
    if (worked) ok();
    else fail();
  }

  var toggle = document.querySelector("[data-nav-toggle]");
  var menu = document.querySelector("[data-nav]");
  if (toggle && menu) {
    toggle.addEventListener("click", function () {
      var open = menu.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      toggle.textContent = open ? "Sluit" : "Menu";
    });
    menu.addEventListener("click", function (e) {
      if (e.target && e.target.tagName === "A" && menu.classList.contains("is-open")) {
        menu.classList.remove("is-open");
        toggle.setAttribute("aria-expanded", "false");
        toggle.textContent = "Menu";
      }
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && menu.classList.contains("is-open")) {
        menu.classList.remove("is-open");
        toggle.setAttribute("aria-expanded", "false");
        toggle.textContent = "Menu";
        toggle.focus();
      }
    });
  }

  document.addEventListener("click", function (e) {
    var btn = closest(e.target, "[data-copy]");
    if (!btn) return;
    var sel = btn.getAttribute("data-copy");
    var node = sel ? document.querySelector(sel) : null;
    var text = ((node && (node.textContent || node.value)) || PAY_TO).replace(/\s+/g, "");
    var status = document.querySelector(btn.getAttribute("data-copy-status") || "#copy-status");
    copyText(text, status);
  });

  var form = document.getElementById("contact-form");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var email = club.email || "info@voorbeeldclub.example";
      var naam = (form.elements.naam && form.elements.naam.value || "").trim();
      var from = (form.elements.from && form.elements.from.value || "").trim();
      var bericht = (form.elements.bericht && form.elements.bericht.value || "").trim();
      var status = document.getElementById("form-status");
      if (!naam || !bericht) {
        if (status) {
          status.textContent = "Vul een naam en een bericht in.";
          status.classList.add("is-err");
        }
        return;
      }
      var body = "Naam: " + naam + "\n";
      if (from) body += "Antwoordadres: " + from + "\n";
      body += "\n" + bericht;
      var url =
        "mailto:" +
        encodeURIComponent(email) +
        "?subject=" +
        encodeURIComponent("Bericht via de site — " + (club.name || "Voorbeeldclub vzw")) +
        "&body=" +
        encodeURIComponent(body);
      if (status) {
        status.textContent = "Je mailprogramma opent. Er gaat niets naar een server.";
        status.classList.remove("is-err");
      }
      window.location.href = url;
    });
  }

  var yearEl = document.querySelector("[data-year]");
  if (yearEl) yearEl.textContent = String(new Date().getFullYear());

  applyClub();
})();
