/* Draw a QR SVG into `mount` for `text`. Requires qrcode-generator (qrcode.min.js). */
function drawKaartQr(mount, text) {
  if (!mount || typeof qrcode !== "function") return;
  if (qrcode.stringToBytesFuncs && qrcode.stringToBytesFuncs["UTF-8"]) {
    qrcode.stringToBytes = qrcode.stringToBytesFuncs["UTF-8"];
  }
  var qr = qrcode(0, "M");
  qr.addData(text, "Byte");
  qr.make();
  mount.innerHTML = qr.createSvgTag({ scalable: true, margin: 1 });
  var svg = mount.querySelector("svg");
  if (svg) {
    svg.setAttribute("role", "img");
    svg.setAttribute("aria-label", "QR-code naar deze pagina");
    svg.removeAttribute("width");
    svg.removeAttribute("height");
  }
}

function fillKaartQr() {
  var mount = document.getElementById("qr");
  var urlEl = document.getElementById("qr-url");
  if (!mount) return;
  var url = window.location.href.split("#")[0];
  if (urlEl) urlEl.textContent = url;
  if (url.indexOf("http://") !== 0 && url.indexOf("https://") !== 0) {
    mount.innerHTML = "";
    mount.classList.add("qr-missing");
    return;
  }
  drawKaartQr(mount, url);
}

document.addEventListener("DOMContentLoaded", fillKaartQr);
