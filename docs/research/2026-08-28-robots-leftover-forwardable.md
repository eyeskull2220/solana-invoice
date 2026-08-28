# RESEARCH — robots, leftover hosts, one forwardable stuk

**Seat:** Builder research. **Date opened:** 2026-08-28.  
**Still OFFERTE.** No FACTUUR. No invented KBO/VAT/tel/street. No 7th shop chip.  
**This file is repo research, not a public shop page.** Do not surge it. Do not surge `main`. Do not surge a second shop. Live shop host **HOLD:** https://sovereignforge.surge.sh/ (PR 213 tree, EUR-first, frozen six, Versie 3).  
**Operator is not the freelancer. Scout owns mail.** This seat does not mail.

Every URL below was opened over HTTP unless marked **UNVERIFIED**.

---

## Path to a forwardable shop that can get paid

A Vlaamse club secretaris does not forward a six-price catalog. They forward **one stuk that looks like a club site**. Paid path after that stuk is already live on the shop host (HOLD, no recutover):

1. Secretaris opens the shop: https://sovereignforge.surge.sh/ — H1 *Voor de secretaris die vanavond nog een voorstel naar het bestuur stuurt.* Frozen six in euro. Stamp OFFERTE. No card, no IBAN.
2. Clicks **Open het voorbeeld** on Club- of vzw-site → https://club-site-kit-treasury.surge.sh/ (this is the stuk).
3. Forwards **that URL** to het bestuur. Chrome job matches Turnkring Boom (home / over / agenda / lid / contact) without copying Boom’s phone, street, or KBO.
4. Bestuur or secretaris mails the OFFERTE to `sasha.de.vree.rene@gmail.com` (shop *Vraag deze OFFERTE*). Scout owns that inbox.
5. After akkoord, betaalgegevens go **apart, per mail** — https://sovereignforge.surge.sh/betalen.html H1 *Betaalgegevens na akkoord.* No rekeningnummer on the page.

**Blocker today:** the live club host is not forwardable (pay-box, empty *Kopieer adres*, operator Gmail, Editor/README on member pages). The tree in PR 213 already killed those. NOW is republish **that kit host only**, not the shop.

---

## 1. Why HTTP robots is `Disallow` while the file is `Allow`

### What was opened

| URL | HTTP `/robots.txt` (no query) | File in this tree | HTTP with `?v=2` |
|---|---|---|---|
| https://sovereignforge.surge.sh/robots.txt | `User-agent: *` / `Disallow: /` (26 bytes, `\r\n`) | `shop/sovereignforge/robots.txt` = `Allow: /` | `Allow: /` (23 bytes) |
| https://club-site-kit-treasury.surge.sh/robots.txt | same `Disallow: /` | `kits/club/robots.txt` = `Allow: /` | `Allow: /` |
| https://treasury-tools.surge.sh/robots.txt | same `Disallow: /` | no robots file in leftover root catalog | `?v=2` → Surge **page not found** (no uploaded file) |
| https://solana-invoice-treasury.surge.sh/robots.txt | same `Disallow: /` | — | not needed |
| https://pipeline-treasury.surge.sh/robots.txt | same `Disallow: /` | — | not needed |

Response header on the bare path: `server: Surge`. This is an **edge override** of `/robots.txt` on `*.surge.sh`, not a failed upload. The query-string body matching the repo file is the same pattern reported on [Webmasters Stack Exchange](https://webmasters.stackexchange.com/questions/148276/how-to-purge-cache-for-on-surge-sh-live-file-serves-old-version-but-new-versio) (crawlers fetch `/robots.txt` **without** a query, so they still see `Disallow`). Query-string is **not** a path to Allow.

Shop live privacy (opened): Versie 3 — 27 augustus 2026. First viewport euro. HOLD that host.

### Official / cited path to Allow — do not guess

**Cited path that works:** publish the **same files on a custom domain**. Surge then serves the project’s own `robots.txt`.

- Maintainer **sintaxi**, [sintaxi/surge#288](https://github.com/sintaxi/surge/issues/288) (2017-10-17): *“For obvious reasons we don't permit search engine indexing on our own domain with other users content. […] A `robots.txt` works as expected with a custom domain.”*
- Same policy restated in [sintaxi/surge discussion #443](https://github.com/sintaxi/surge/discussions/443) (fu-sen, 2021-04-04; sintaxi reply): `NAME.surge.sh/robots.txt` is **fixed** to `Disallow: /` to stop link-farming on Surge’s own domain. *“You should always use Custom Domain when publishing the Web with Surge.”*
- Custom domains are **free** on the Free plan: [surge.sh/docs/platform/custom-domains](https://surge.sh/docs/platform/custom-domains) — *“Every project on Surge can live at your own domain, free.”* [surge.sh/pricing](https://surge.sh/pricing) lists **Custom domain** on Surge Free. Paid Professional is **not** required for a custom domain.
- Current docs also mention `Disallow: /` only for the **`private`** setting ([surge.sh/docs/cli/config](https://surge.sh/docs/cli/config)): crawlers get `Disallow` when the project is locked. That is a **different** switch. Our shop is public; the override we measured is the `*.surge.sh` subdomain lock, not `private`.

**Current surge.sh docs site has no page that says “verify your email to Allow `*.surge.sh`.”** Getting Started ([surge.sh/docs/getting-started](https://surge.sh/docs/getting-started)) creates an account with *“just an email and password.”* AUTH docs talk about verified email for **password-protected** paths, not for public robots. **Email verification is not a cited path to Allow.** Do not treat it as one.

**Paid Surge / `surge card` is not a cited path to Allow on `*.surge.sh`.** [sintaxi/surge#257](https://github.com/sintaxi/surge/issues/257) whitelists **PDF publishing** after adding a card (`surge card`); paying customers are auto-whitelisted **for PDFs**. Discussion #443 **asked** whether that card whitelist could also lift subdomain indexing. There is **no maintainer reply that it does**. Do not upgrade to Professional hoping robots.txt on `sovereignforge.surge.sh` becomes `Allow`. Pricing does not list indexing as a Professional feature.

**Move host:** leaving `*.surge.sh` for a name you control **is** the official Allow path (custom domain on Surge, still free). Moving off Surge entirely is a product choice, not required by the robots docs. CEO said HOLD the live shop host — a custom domain can later CNAME to Surge **without** a second `*.surge.sh` shop.

**Slack/SO colour, not official docs:** [Stack Overflow 54262130](https://stackoverflow.com/questions/54262130/surge-sh-does-not-allow-modifying-robots-txt) — *“According to slack, robots.txt files on *.surge.sh subdomains are locked to prevent link farming.”* Useful confirmation, not the primary cite. Use #288 + custom-domains docs.

**Google this hunt:** a `site:surge.sh sovereignforge` web search did **not** return our hosts (consistent with `Disallow`). That does **not** mean leftover USDC is safe: GitHub `README.md` on `main` still lists live `*-treasury.surge.sh` URLs and **9 USDC / 49 USDC**. Humans paste GitHub. Robots on Surge do not cover GitHub.

---

## 2. Leftover hosts — USDC / Solana / wallet — rank

Opened 2026-08-28. Rank is **take down / euro-face / ignore**. Poison = a secretaris who googles us (or follows a GitHub / catalog link) and hits crypto, a wallet, or a 7th SKU before the club stuk.

### Take down

Still show **USDC / Solana / wallet** on the page, or the **hostname itself** is the old Solana Invoice product.

| Host | Opened | What a secretaris would see | Rank |
|---|---|---|---|
| https://json-clean-treasury.surge.sh/ | yes | Title JSON Cleaner. `49 USDC · Solana USDC`. H2 *Pay 49 USDC on Solana*. | **take down** |
| https://quote-calc-treasury.surge.sh/ | yes | `49 USDC · Solana USDC`. H2 *Pay 49 USDC on Solana*. Rate in USDC/hour. | **take down** |
| https://scope-sheet-treasury.surge.sh/ | yes | Title *Scope Sheet — 49 USDC*. Pay box + USDC mint. | **take down** |
| https://utm-builder-treasury.surge.sh/ | yes | Title *UTM Builder — 49 USDC*. *Solana Pay QR for 49 USDC*. | **take down** |
| https://md-page-treasury.surge.sh/ | yes | Title *Markdown to HTML — 49 USDC*. H2 *Pay 49 USDC on Solana*. | **take down** |
| https://form-to-email-treasury.surge.sh/ | yes | `49 USDC · billed via Solana Invoice`. “no wallet”. | **take down** |
| https://rss-to-webhook-treasury.surge.sh/ | yes | same `49 USDC` + Solana Invoice link. | **take down** |
| https://csv-cleaner-treasury.surge.sh/ | yes | English CSV tool. Lead: *no wallet*. No USDC string on this page. Still a leftover English kit on a treasury host. | **take down** (wallet word + old kit) |
| https://solana-invoice-treasury.surge.sh/ | yes | **Euro-faced** body: *Eén klus — €49 · OFFERTE*. No USDC in HTML. Hostname is still `solana-invoice-treasury`. GitHub README on `main` still captions this URL as *Solana Invoice — 9 USDC*. | **take down** (hostname + README pointer). Body is euro-face, not enough. |
| https://treasury-tools.surge.sh/ | yes | 11-item catalog pretending to be the shop: Stripe **sandbox** link, *Eén klus* → solana-invoice-treasury, Peppol Ready, dual-invoice, pipeline. JSON-LD lists all eleven. Not USDC on the page; it **routes** to leftover SKUs. | **take down** (fake shop / 11 chips). Do not euro-face this into a second catalog. |

Official teardown (when Scout runs it, **not this seat**): [surge.sh/docs/cli/revisions](https://surge.sh/docs/cli/revisions) — `surge <domain> teardown`. Does not touch the HOLD shop host.

### Euro-face leftover SKUs (no USDC on the page; not frozen six)

These are euro OFFERTE leftovers. A secretaris who lands here sees extra prices (€249 / €399 / €490) that are **not** the frozen six. They poison the shop story. They do **not** show USDC/Solana/wallet in the HTML opened today.

| Host | Opened | Face | Rank |
|---|---|---|---|
| https://pipeline-treasury.surge.sh/ | yes | Lead tot offerte €399. Mail operator Gmail. Demo `hello@studio.example`. | **euro-face** leftover SKU — prefer **take down** if teardown is cheap; do not add as 7th chip |
| https://peppol-chase-treasury.surge.sh/ | yes | Peppol-opvolging €399. Same mail. | same |
| https://peppol-ready-treasury.surge.sh/ | yes | Peppol-oriëntatie €249. | same |
| https://dual-invoice-treasury.surge.sh/ | yes | Twee-keten €490. *Te betalen €490*. No IBAN. | same |

### Featured kit hosts (linked from the live shop — not leftover)

Shop *Open het voorbeeld* targets these. HOLD the shop; these are the examples.

| Host | HTTP | Notes |
|---|---|---|
| https://menu-kit-treasury.surge.sh/ | 200 | Euro wrap €199. Inner `menu.html` / `allergenen.html`: no USDC, no operator Gmail. Demo `hello@studio.example`. |
| https://sponsor-kit-treasury.surge.sh/ | 200 | Voorbeeldharmonie sponsorblad. Inner `offerte.html`: no operator Gmail. |
| https://vakman-kit-treasury.surge.sh/ | 200 | Vakman wrap €249. Inner `offerte.html`: no operator Gmail. |
| https://lid-kit-treasury.surge.sh/ | 200 | Form is the page. **Operator Gmail on the form footer** (`lid.html`). Not the ONE stuk; NEXT if club is clean. |
| https://inbox-ops-treasury.surge.sh/ | 200 | Live wrap title still **Studio Noord**. Repo wrap (PR 213) is *Sasha · SovereignForge · Geel*. Inner intake/invoice/faq: no USDC. NEXT republish wrap only. |
| https://inbox-ops-kit-treasury.surge.sh/ | **404** project not found | **ignore** |
| https://club-site-kit-treasury.surge.sh/ | 200 | **THE stuk. Dirty live.** See §3. |
| https://club-kit-treasury.surge.sh/ | **404** | **ignore** |
| https://menu-treasury.surge.sh/ https://lid-treasury.surge.sh/ https://sponsor-treasury.surge.sh/ https://vakman-treasury.surge.sh/ | **404** | **ignore** |

### Ignore (404 this hunt)

https://waitlist-landing-treasury.surge.sh/ · https://receipt-generator-treasury.surge.sh/ · https://paywall-stub-treasury.surge.sh/ — project not found.

### GitHub `main` (not a Surge host, still googleable)

Opened via GitHub code search: `README.md`, `index.html`, `catalog.html`, `solana-invoice.html`, `config.js` still say **Solana Invoice / 9 USDC / 49 USDC** and link the live treasury hosts. Leftover root HTML is **not** the shop. Do not surge `main`. README cleanup is **NEXT** (docs on `main`), not a shop cutover.

---

## 3. The ONE forwardable stuk

**Ship next:** clean **https://club-site-kit-treasury.surge.sh/** so a secretaris will actually forward it.

Not a 7th chip. Not the shop recutover. Not menu/lid/sponsor/vakman/inbox-ops as the forwarded stuk (those are sell wraps or one-pagers). The club demo is the only artefact that looks like [Turnkring Boom](https://turnkringboom.be/) (opened): a small Vlaamse club with Home, a “who / when” page, kalender, and Contact, plus a club `info@` mailbox.

### Quality bar — live host (opened) vs tree (PR 213)

| Check | Live `club-site-kit-treasury` 2026-08-28 | Tree `kits/club/` (this PR’s base, CODE #213) |
|---|---|---|
| Pay-box | **Present:** `aside.paybox#kit-pay` — *Deze kit · €900*, operator Gmail, *open de editor* | **Gone.** Contact card only. |
| Operator Gmail on member pages | Footer `.foot-pay` on index, over, agenda, lidworden, contact, editor: `sasha.de.vree.rene@gmail.com` | **Gone.** Club mail is RFC 2606 `info@golfbreker.example`. |
| Empty *Kopieer adres* | Button `data-copy="#pay-addr-foot"` on over / agenda / lidworden / contact / editor. **`#pay-addr-foot` node is missing.** Live `site.js` has `var PAY_TO = ""`. Copy copies empty string. | **Gone.** `site.js` is nav + year only. No PAY_TO. |
| Editor / README on member chrome | Footer *Editor · README*. `editor.html` **200**. `README.md` **404**. | No `editor.html` in `kits/club/`. Footer: VOORBEELD + privacy. |
| Invented tel / street / KBO | None on live (good). | None (good). Do not copy Boom’s `0470 07 44 02`, Gasstraat 23, or RPR 0408.519.656. |
| Club chrome vs Boom | Nav: Home, Over ons, Agenda, Lid worden, Contact. Demo banner VOORBEELD. | Same five. That is the chrome model — structure, not Boom’s personal data. |

Live index still tells the club to use a club address, *nooit een privé-Gmail in de publieke demo*, then puts operator Gmail in the pay-box. That is why it fails the forward test.

**Do not invent KBO/VAT.** Golfbreker stays fictive. `info@golfbreker.example` stays. Privacy on the shop (Versie 3) already says KBO/BTW: nog niet toegekend.

**Do not mail from this seat.** Scout owns `sasha.de.vree.rene@gmail.com`. Operator is not the freelancer.

### What “clean” means (already in tree — republish only)

Kill pay-box. Kill empty *Kopieer adres* / `#pay-addr-foot` / `PAY_TO`. Kill operator Gmail on Golfbreker pages. Kill Editor/README in the member footer. Leave RFC 2606 club mail. No 7th chip.

Then the secretaris forwards https://club-site-kit-treasury.surge.sh/ and the shop (HOLD) still takes the OFFERTE mail.

---

## 4. NOW / NEXT / WAIT

### NOW — startable without cutting over the live shop

None of this republishes https://sovereignforge.surge.sh/. None of this surges `main`. None of this mails.

1. **This research page** (this PR). No public HTML.
2. **Republish `kits/club/` → existing host `club-site-kit-treasury.surge.sh` only.** Source is already cleaned in PR 213. A new revision on the **kit** host is not a second shop and not a shop cutover. After publish, re-open index / over / agenda / lidworden / contact: no pay-box, no *Kopieer adres*, no operator Gmail, no Editor footer. `editor.html` should 404 once the new snapshot is live (Surge publish is a full revision, not a patch — [revisions docs](https://surge.sh/docs/cli/revisions)).
3. **Teardown the take-down list** (Scout CLI, not this seat): json-clean, quote-calc, scope-sheet, utm-builder, md-page, form-to-email, rss-to-webhook, csv-cleaner, solana-invoice-treasury, treasury-tools. Command: `surge <host> teardown`.
4. **Do not** surge leftover root `index.html` / `catalog.html` / `solana-invoice.html`.

Paid path after (2): secretaris forwards the cleaned club URL; bestuur mails the shop OFFERTE address; Scout answers with betaalgegevens. Still OFFERTE.

### NEXT

- Custom domain for **Allow** (Scout-owned name → Surge). Official path in §1. HOLD `sovereignforge.surge.sh` until DNS is ready; do not stand up a second `*.surge.sh` shop.
- GitHub `main` README / leftover root still USDC — docs PR, not a shop surge.
- Republish **inbox-ops wrap** to `inbox-ops-treasury.surge.sh` (live kicker still Studio Noord; tree is Geel). Not the forwarded stuk.
- Lid form footer still has operator Gmail on the live lid host — after club is clean.
- Euro leftover SKUs (pipeline / chase / peppol-ready / dual) if not torn down in NOW.

### WAIT

- Recutover of https://sovereignforge.surge.sh/ (CEO HOLD).
- A second Surge shop host.
- 7th shop chip (Peppol Ready, dual-invoice, één klus, pipeline).
- FACTUUR, IBAN on a page, invented KBO/VAT/tel/street.
- Mailing clubs / secretarissen (Scout owns mail).
- Paying Surge Professional **for robots** (not cited).
- Verifying Surge email **for robots** (not cited).
- Query-string `robots.txt?v=2` as an SEO trick (crawlers do not use it).

---

## Opened URL log (2026-08-28)

**Shop / robots:** https://sovereignforge.surge.sh/ · `/robots.txt` · `/robots.txt?v=2` · `/privacy.html` · `/betalen.html` (via shop nav + this tree).

**Stuk:** https://club-site-kit-treasury.surge.sh/ · `/index.html` · `/over.html` · `/agenda.html` · `/lidworden.html` · `/contact.html` · `/editor.html` (200) · `/README.md` (404) · `/robots.txt` · `/robots.txt?v=2` · `/site.js`.

**Leftover named by CEO:** https://treasury-tools.surge.sh/ · https://pipeline-treasury.surge.sh/ · https://peppol-chase-treasury.surge.sh/ · https://dual-invoice-treasury.surge.sh/ · https://peppol-ready-treasury.surge.sh/ · https://solana-invoice-treasury.surge.sh/ (+ `/offerte.html`).

**Featured kits:** menu / lid / sponsor / vakman `*-kit-treasury.surge.sh`; inbox-ops at `inbox-ops-treasury.surge.sh` (the `-kit-` name 404s). Inner menu/allergenen/lid/offerte/intake/invoice/faq opened.

**Broaden (USDC still live):** json-clean, quote-calc, scope-sheet, utm-builder, md-page, form-to-email, rss-to-webhook, csv-cleaner.

**Club chrome model:** https://turnkringboom.be/

**Surge cites:** [custom domains](https://surge.sh/docs/platform/custom-domains) · [pricing](https://surge.sh/pricing) · [config / private](https://surge.sh/docs/cli/config) · [getting started](https://surge.sh/docs/getting-started) · [revisions / teardown](https://surge.sh/docs/cli/revisions) · [sintaxi/surge#288](https://github.com/sintaxi/surge/issues/288) · [discussion #443](https://github.com/sintaxi/surge/discussions/443) · [sintaxi/surge#257](https://github.com/sintaxi/surge/issues/257) (PDF whitelist, not robots).

**UNVERIFIED this hunt:** whether Google Search Console lists our hosts; whether any historical `site:` hit exists beyond this web search; whether a future Surge Professional SKU will ever whitelist `*.surge.sh` robots (no doc today).
