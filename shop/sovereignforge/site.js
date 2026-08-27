(function () {
  var header = document.querySelector("[data-header]");
  var toggle = document.querySelector("[data-nav-toggle]");
  var nav = document.querySelector("[data-nav]");
  if (toggle && header && nav) {
    toggle.addEventListener("click", function () {
      var open = header.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      toggle.textContent = open ? "Sluit" : "Menu";
    });
  }

  var year = document.querySelector("[data-year]");
  if (year) year.textContent = String(new Date().getFullYear());

  var params = new URLSearchParams(window.location.search);
  var pack = params.get("pakket");
  var select = document.getElementById("pakket");
  if (pack && select) {
    var allowed = { menu: 1, sponsor: 1, vakman: 1, inbox: 1, lid: 1, club: 1 };
    if (allowed[pack]) select.value = pack;
  }

  var form = document.getElementById("mail-form");
  if (!form) return;

  var labels = {
    menu: "Menukaart €199",
    sponsor: "Sponsorblad €199",
    vakman: "Vakman €249",
    inbox: "Inbox-ops €299",
    lid: "Lidformulier €349",
    club: "Clubsite €900"
  };

  form.addEventListener("submit", function (event) {
    event.preventDefault();
    var naam = (document.getElementById("naam").value || "").trim();
    var zaak = (document.getElementById("zaak").value || "").trim();
    var chosen = document.getElementById("pakket").value;
    var bericht = (document.getElementById("bericht").value || "").trim();
    var status = document.getElementById("form-status");
    if (!naam || !chosen) {
      status.textContent = "Vul minstens uw naam en een pakket in.";
      return;
    }
    var packLabel = labels[chosen] || chosen;
    var subject = "OFFERTE " + packLabel;
    var body =
      "Naam: " + naam + "\n" +
      "Zaak of club: " + (zaak || "—") + "\n" +
      "Pakket: " + packLabel + "\n\n" +
      (bericht || "Ik wil dit pakket. Stuur een OFFERTE in euro.");
    var href =
      "mailto:hello@studio.example?subject=" + encodeURIComponent(subject) +
      "&body=" + encodeURIComponent(body);
    status.textContent = "Uw mailprogramma opent. Niets gaat naar een server.";
    window.location.href = href;
  });
})();
