#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const dir = path.dirname(fileURLToPath(import.meta.url));
const htmlPath = path.join(dir, "index.html");
const readmePath = path.join(dir, "README.md");
const scanPath = path.join(dir, "PII-SCAN.md");
const html = fs.readFileSync(htmlPath, "utf8");
const readme = fs.readFileSync(readmePath, "utf8");
const piiDoc = fs.existsSync(scanPath) ? fs.readFileSync(scanPath, "utf8") : "";
const product = html + "\n" + readme;
const combined = product + "\n" + piiDoc;
const withoutQrLib = html.replace(/<script>\s*var QRCode;[\s\S]*?<\/script>/, "");

const SOLANA = "96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3";
const BASE = "0x9eb954b567ef3616424a6e1bf42c63724930aa54";
const SOLANA_MINT = "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v";
const BASE_USDC = "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913";
const INVOICE = "INV-20260826";
const KBO_LINE = "KBO/BTW: nog niet toegekend";
const PAY_URL =
  "solana:" + SOLANA +
  "?amount=490&spl-token=" + SOLANA_MINT +
  "&memo=" + INVOICE +
  "&label=" + encodeURIComponent("Dual-chain USDC offerte");

const failures = [];
function ok(cond, msg) {
  if (!cond) failures.push(msg);
}

ok(html.includes('data-invoice-number="' + INVOICE + '"'), "document number data attr");
ok(html.includes(">" + INVOICE + "<"), "document number in DOM");
ok((html.match(/INV-20260826/g) || []).length >= 1, "document number present");
ok(!/INV-\d{8}-\d/.test(html), "no extra document-number suffixes");
ok(html.includes('data-issued="2026-08-26"'), "issued date");
ok(html.includes("August 26, 2026"), "issued date label");
ok(html.includes('data-amount="490"'), "amount 490");
ok(html.includes("490.00"), "amount 490.00");
ok(html.includes(SOLANA), "solana pay-to");
ok(html.includes(BASE), "base pay-to");
ok(html.includes(SOLANA_MINT), "solana usdc mint");
ok(html.includes(BASE_USDC), "base usdc contract");
ok(html.includes(PAY_URL), "solana pay url constant");
ok(!/reference=/.test(html), "no solana pay reference=");
ok(!/walletconnect/i.test(product), "no walletconnect");
ok(!/\bSIWE\b/.test(html.replace(/No SIWE/g, "")), "SIWE only in prohibition copy");
ok(!/sign-in with ethereum/i.test(product), "no SIWE flow");
ok(!/ethereum\.request/.test(html), "no ethereum.request");
ok(!/window\.ethereum/.test(html), "no window.ethereum");
ok(!/@phantom\//.test(html), "no Phantom SDK");
ok(!/wagmi|rainbowkit|web3modal|reown/i.test(html), "no wallet UI kits");

ok(html.includes('<div class="word">OFFERTE</div>'), "OFFERTE stamp");
ok(html.includes('data-doc-stamp="OFFERTE"'), "OFFERTE data stamp");
ok(html.includes(KBO_LINE), "exact KBO/BTW unassigned line");
ok(!/\bFACTUUR\b/.test(withoutQrLib), "no FACTUUR in product html");
ok(!/\bFACTUUR\b/.test(readme), "no FACTUUR in readme");
ok(!/<div class="word">INVOICE<\/div>/.test(html), "stamp is not INVOICE");
ok(!/<div class="word">FACTUUR<\/div>/.test(html), "stamp is not FACTUUR");

const vatBe = /BE[\s.]?0\d{3}[\s.]?\d{3}[\s.]?\d{3}/i;
ok(!vatBe.test(combined), "no BE + digit KBO/BTW shape");
ok(!/\b0\d{3}\.\d{3}\.\d{3}\b/.test(combined), "no dotted 10-digit enterprise-number shape");
ok(!/\b0{4}\.0{3}\.0{3}\b/.test(combined), "no all-zero dotted enterprise-number shape");

ok(!/<input\b[^>]*(iban|kbo|btw|vat|bank)/i.test(withoutQrLib), "no IBAN/KBO inputs");
ok(!/\bIBAN\s*:/i.test(withoutQrLib), "no IBAN field label");
ok(/No IBAN/.test(withoutQrLib), "IBAN denied in copy");
ok(!/\bPhantom\b/i.test(withoutQrLib), "no Phantom in product html");
ok(!/\bPhantom\b.{0,80}\bIBAN\b|\bIBAN\b.{0,80}\bPhantom\b/i.test(product), "Phantom not next to IBAN");

ok(/Not Peppol/.test(withoutQrLib), "Not Peppol");
ok(/Not an Access Point/.test(withoutQrLib), "Not an Access Point");
ok(!/Peppol/i.test(withoutQrLib.replace(/Not Peppol/g, "")), "Peppol only as Not Peppol");
ok(!/Access Point/i.test(withoutQrLib.replace(/Not an Access Point/g, "")), "Access Point only as denial");
ok(!/Peppol[- ]compliant|is an Access Point|PEPPOL Access Point|Peppol participant/i.test(combined), "no Peppol compliance claim");

const scanText = withoutQrLib + "\n" + readme + "\n" + piiDoc;
const base58 = scanText.match(/\b[1-9A-HJ-NP-Za-km-z]{32,44}\b/g) || [];
const unexpectedSolana = [...new Set(base58)].filter(function (s) {
  return s !== SOLANA && s !== SOLANA_MINT;
});
ok(unexpectedSolana.length === 0, "unexpected base58: " + unexpectedSolana.join(","));

const evm = scanText.match(/0x[a-fA-F0-9]{40}/g) || [];
const unexpectedEvm = [...new Set(evm)].filter(function (s) {
  return s.toLowerCase() !== BASE && s.toLowerCase() !== BASE_USDC.toLowerCase();
});
ok(unexpectedEvm.length === 0, "unexpected evm: " + unexpectedEvm.join(","));
ok(withoutQrLib.length > 2000, "qr library stripped, app html remains");

const email = product.match(/[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}/gi) || [];
const badEmail = email.filter(function (e) {
  return !/@[A-Z0-9.-]+\.example$/i.test(e);
});
ok(badEmail.length === 0, "non-example emails: " + badEmail.join(","));

const phone = product.match(/(?:\+1[\s.-]?)?(?:\(?\d{3}\)?[\s.-]?)\d{3}[\s.-]?\d{4}\b/g) || [];
ok(phone.length === 0, "phones: " + (phone || []).join(","));

ok(!/seed phrase|mnemonic|private key|secret key|BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY/i.test(product), "no secrets language");
ok(!/\b(sk-|sk_live_|ghp_|xoxb-|AKIA)[A-Za-z0-9]/i.test(product), "no api tokens");
ok(!/\beyJ[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]+\./.test(product), "no JWTs");
ok(!/tel:/.test(product), "no tel:");
ok(!/\b\d{1,5}\s+\w+\s+(Street|St|Avenue|Ave|Road|Rd|Boulevard|Blvd)\b/i.test(product), "no street addresses");

if (failures.length) {
  console.error("FAIL");
  failures.forEach(function (f) { console.error(" - " + f); });
  process.exit(1);
}

console.log("PASS");
console.log("invoice=" + INVOICE);
console.log("stamp=OFFERTE");
console.log("kbo=" + KBO_LINE);
console.log("amount=490 USDC");
console.log("solana=" + SOLANA);
console.log("base=" + BASE);
console.log("payUrl=" + PAY_URL);
console.log("pii=clean");
