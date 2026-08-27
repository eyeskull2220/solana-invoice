(function () {
  "use strict";

  var PAY_TO = "";

  function closest(el, sel) {
    while (el && el.nodeType === 1) {
      if (el.matches(sel)) return el;
      el = el.parentElement;
    }
    return null;
  }

  function copyText(text, statusEl) {
    function ok() {
      if (statusEl) {
        statusEl.textContent = "Adres gekopieerd.";
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
    var text = (node && (node.textContent || node.value) || PAY_TO).replace(/\s+/g, "");
    var status = document.querySelector(btn.getAttribute("data-copy-status") || "#copy-status");
    copyText(text, status);
  });

  var yearEl = document.querySelector("[data-year]");
  if (yearEl) yearEl.textContent = String(new Date().getFullYear());
})();
