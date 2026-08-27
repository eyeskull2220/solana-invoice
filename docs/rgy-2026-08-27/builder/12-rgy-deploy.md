# Builder 12 — RGY DEPLOY

**Seat:** RGY reviewer (after adversarial DEPLOY).  
**Date:** 2026-08-27.  
**Live origin (this pass):** `https://sovereignforge.surge.sh/` — Surge, not `.be`.  
**Constraint:** `.be` is paid at OVH invoice **#256963027** with **no zone yet**. No `.be` publish. No DNS invent.  
**This PR:** review notes only. Does not deploy, does not touch OVH, does not rewrite shop HTML.

**Overall: RED.** A shop is live on Surge. It is not a shippable Belgian sales origin. Deploying *this* repo onto that origin would make it worse.

Adversarial pass `06-adv-deploy` (`bc-d74983e1-3813-4028-a800-9d72bca2e03d`) started the same attack list and did not finish a file. This note re-runs the probes and scores them.

---

## Adversarial pass (then RGY)

Assume deploy is a bad layout. Attack:

| Attack | Result this pass |
| --- | --- |
| Surge with no check | **Hit.** Live `surge-cache: HIT`. No `.github`, no CNAME in this repo, no `.surgeignore`, no red/green gate. Anyone with Surge creds can `surge .` the leftover `solana-invoice` tree onto a live host. |
| robots `Disallow: /` live | **Hit.** Every public shop and kit host probed today serves `User-agent: *` / `Disallow: /`. |
| `.be` not ready | **Hit, correctly unpublished.** `sovereignforge.be` is **NXDOMAIN** at `1.1.1.1` (SOA on `be.`, no zone). Do not invent records. Do not publish. |
| Leftover repo `solana-invoice` treated as shop | **Hit.** `main` is still the USDC pay page + 4-tool English catalog. Live shop HTML is **not in this tree**. |
| No red/green deploy | **Hit.** No workflow, no health URL, no “euro-face + robots Allow + privacy” check before Surge. |
| No inhouse CI | **Hit.** GitHub API: no `.github`. |

---

## RED

1. **Named live shop still prints USDC on the sales face.**  
   `https://sovereignforge.surge.sh/` (HTTP 200, 5360 B, `lang="nl"`, chalkboard):
   - meta: *“Charge in USDC, euro is omrekening.”*
   - lede: *“Charge blijft USDC op Solana.”*
   - Club card: *“900 USDC · ±€774”* and CTA **“Betaal 900 USDC”**.
   - Same pattern for 199 / 349 USDC kits.
   - Footer rate line: *“1 USDC ≈ €0,86 … Charge blijft USDC.”*  
   `/pakketten.html` has a USDC column. `/betalen.html` is a USDC checkout: printed Solana address `96BT6r5C35cvokdVop8ro4vDtv9zKUxpzrLbXqQbuHk3`, QR `qr/900.svg`, *“Betaal exact dat bedrag in USDC op Solana”*.  
   **RGY:** marketing home is not euro-only. Betalen is allowed to be checkout; home/pakketten are not.

2. **Live robots hide the shop from crawlers.**  
   `https://sovereignforge.surge.sh/robots.txt` → `200 text/plain` 26 B:

   ```
   User-agent: *
   Disallow: /
   ```

   Same 26-byte file on `treasury-tools.surge.sh` and every `*-treasury.surge.sh` kit host below.  
   **Contradiction:** `treasury-tools.surge.sh` HTML has `<meta name="robots" content="index,follow">` while `robots.txt` forbids `/`.  
   **RGY:** do **not** flip `Allow: /` while USDC is still on the named home. Indexers would cache the crypto face. Sequence is: euro-only HTML **then** `Allow: /`.

3. **This repo is leftover HTML, not the live shop.**  
   Workspace `main` (`2170952`):

   | File | What it is | Live `sovereignforge.surge.sh` |
   | --- | --- | --- |
   | `index.html` (50 251 B) | English Solana Invoice **9 USDC** pay/unlock | Dutch bestuur-voorstel, 5360 B, USDC on cards |
   | `catalog.html` (4 882 B) | English 4-tool USDC catalog | **404** (custom Dutch “Pagina niet gevonden”) |
   | `solana-invoice.html` | Kit editor | **404** |
   | `robots.txt` | **absent** | `Disallow: /` |
   | `privacy.html` / `pakketten.html` / `betalen.html` / `contact.html` | **absent** | all **200** |
   | `.github/` | **absent** | n/a |

   README still says “Live catalog: https://treasury-tools.surge.sh/” and lists `solana-invoice-treasury` / `csv-cleaner-treasury` / `form-to-email-treasury` / `rss-to-webhook-treasury` at 9/49 USDC.

   **Deploying `main` (or PR #111) with `surge .` onto `sovereignforge.surge.sh` would clobber the chalkboard shop** with leftover or €9/€49 cream pages, drop privacy/contact, and 404 the live kit table.

4. **Two live catalogs, neither matches `main`, neither is a clean cutover.**  
   - `sovereignforge.surge.sh` — chalkboard, USDC on face, privacy **200**, custom 404, `CNAME` body = `sovereignforge.surge.sh` (not `.be`).
   - `treasury-tools.surge.sh` — cream Belgian 11-pack, euro copy on the face, Stripe **test** link, JSON-LD ItemList of kit hosts, **no privacy** (no footer link; unknown paths 404 into Surge’s default Mozilla-font 404, 8247 B), `meta robots index,follow` vs `Disallow: /`.  
   Schema on treasury-tools still lists junk SKUs the FIX seat wants off the marketing home: pipeline, peppol-chase, dual-invoice, peppol-ready, plus `solana-invoice-treasury` as “Eén klus”.  
   **RGY:** catalog cutover is not “pick a host and delete the other.” See [Catalog cutover](#catalog-cutover-do-not-cut-mailed-links).

5. **No red/green deploy, no inhouse CI.**  
   No workflow will stop a bad Surge publish. `surge-cache: HIT` on the named origin (`surge-stamp` `2668141::1787857596996-…`, probed 2026-08-27 19:14 UTC). There is no documented publish dir, no allow-list of hosts, no post-deploy grep for `USDC` on `/`.

6. **`.be` is paid and has no zone — publishing it would be invention.**  
   User fact: OVH **#256963027**, no zone yet.  
   Observed: `dig @1.1.1.1 sovereignforge.be SOA` → **NXDOMAIN**, authority `be. SOA a.nsset.be.`. `getaddrinfo` for `sovereignforge.be` and `www.sovereignforge.be` fails (`Name or service not known`).  
   Live `CNAME` file on Surge is the Surge hostname, not a `.be` name.  
   **RGY:** leave it. Do not create NS/A/AAAA/CNAME. Do not `surge` to a `.be` domain.

---

## YELLOW

1. **PR #111 is a false shop source.**  
   https://github.com/eyeskull2220/solana-invoice/pull/111 (`cursor/euro-shop-face-00e2`) rewrites root `index.html` / `catalog.html` to euro OFFERTE and adds `robots.txt` `Allow: /`. Prices are **€9 / €49**, not the live €199–€900 kit ladder. It parks USDC checkout in `kit-pay.html` (unlinked, still crawlable if `Allow: /`). **Not merged. Not what is live.** Do not Surge it onto either origin.

2. **Kit hosts stay up (good) and stay USDC/Disallow (bad).**  
   All 200 today. Do not take them down. Do not put USDC in the *shop* title/CTA; kit demos may keep product copy until a later kit pass.

   | Host | Title (live) | `USDC\|Solana\|Phantom` hits | robots |
   | --- | --- | ---: | --- |
   | club-site-kit-treasury.surge.sh | ZWV De Golfbreker — zwemclub in Geel (demo) | 5 | Disallow |
   | menu-kit-treasury.surge.sh | Menukaart + QR/allergenen — **199 USDC** | 14 | Disallow |
   | sponsor-kit-treasury.surge.sh | sponsorblad vzw (OFFERTE) | 2 | Disallow |
   | lid-kit-treasury.surge.sh | Desk Noord — lid-inschrijving (OFFERTE) | 2 | Disallow |
   | vakman-kit-treasury.surge.sh | Vakman one-pager — **249 USDC** | 14 | Disallow |
   | inbox-ops-treasury.surge.sh | Inbox-ops — **299 USDC** | 10 | Disallow |
   | pipeline-treasury.surge.sh | Lead tot offerte — €399 | 0 | Disallow |
   | peppol-chase-treasury.surge.sh | Belgisch Peppol Client-Chase Pack — **399 USDC** | 10 | Disallow |
   | dual-invoice-treasury.surge.sh | Twee-keten USDC-offerte — **490 USDC** | 42 | Disallow |
   | peppol-ready-treasury.surge.sh | Peppol Ready Kit — **249 USDC** | 13 | Disallow |
   | solana-invoice-treasury.surge.sh | Eén klus — €49 · OFFERTE | 0 | Disallow |
   | csv-cleaner-treasury.surge.sh | CSV Cleaner (EN leftover) | 0 title; EN tool | Disallow |
   | form-to-email-treasury.surge.sh | Form to Email (EN leftover) | 2 | Disallow |
   | rss-to-webhook-treasury.surge.sh | RSS to Webhook (EN leftover) | 2 | Disallow |

3. **treasury-tools 404 is Surge default leftover, not the shop 404.**  
   Named origin has a Dutch custom 404 (1917 B). Catalog origin 404s into Surge chrome (8247 B, Mozilla CDN fonts). Cutover that only updates `/` leaves junk 404 on mailed deep links.

4. **FIX seat (`hide-coin + robots`) is still running** and plans `shop/sovereignforge/` at €199–€900. Until that (or a successor) is merged **and** Surge-published to the named origin, live remains RED. Do not wait on `.be`.

5. **Twelve.tools already points at treasury-tools.** Footer on that origin: *“Vermeld op Twelve.tools.”* That is an external catalog link. Cutover must keep `https://treasury-tools.surge.sh/` answering 200 (redirect to named origin is OK; 404 is not).

---

## GREEN

1. **Named origin is live on Surge, not imaginary.** HTTP/2 200, `server: Surge`, canonical `https://sovereignforge.surge.sh/`. Shop IA exists: `/`, `/pakketten.html`, `/betalen.html`, `/contact.html`, `/privacy.html`, favicons, `styles.css`. Custom Dutch 404. Skip link. OFFERTE/VOORBEELD stamp. `KBO/BTW: nog niet toegekend`. No fake BE0. No cookie banner. Privacy 200 (4353 B).

2. **`.be` was not published.** NXDOMAIN + no zone matches the OVH invoice fact. This is the correct unpublished state.

3. **Kit demo URLs still 200.** Club maatstaf `club-site-kit-treasury.surge.sh` is up. Catalog cutover has not 404’d the voorbeeld links.

4. **Contact is mail-only** (`sasha.de.vree.rene@gmail.com`). No invented phone, no form inbox on the named origin.

5. **This review does not deploy.** No Surge publish, no OVH zone, no DNS records in this PR.

---

## Notes

### Surge vs leftover HTML

Three trees, one leftover repo:

| Tree | Role today | If you `surge` the wrong tree |
| --- | --- | --- |
| Live `sovereignforge.surge.sh` | Named shop. Chalkboard. USDC on face. Privacy. | — |
| Live `treasury-tools.surge.sh` | Older/other catalog. Euro face, cream, 11 kits + Stripe test, no privacy. README still calls this “Live catalog”. | — |
| Git `main` (`index.html` + `catalog.html`) | Leftover Solana Invoice 9 USDC + EN 4-tool catalog | Overwrites either live shop. **Do not.** |
| PR #111 euro face | €9/€49 cream OFFERTE, `Allow: /`, `kit-pay.html` | Overwrites named shop with wrong SKUs. **Do not.** |

Leftover also means: EN tools still live (`csv-cleaner`, `form-to-email`, `rss-to-webhook`) while the named shop no longer lists them. They are sticky URLs, not the sales face. Keep them 200; do not put them on `/`.

Live named origin `CNAME` file contents: `sovereignforge.surge.sh` (24 B). That is a Surge hostname file, not a `.be` zone.

### robots

| Origin | `robots.txt` | HTML meta |
| --- | --- | --- |
| sovereignforge.surge.sh | `Disallow: /` | none observed |
| treasury-tools.surge.sh | `Disallow: /` | `index,follow` |
| kit hosts | `Disallow: /` | n/a this pass |
| repo `main` | file missing | n/a |
| PR #111 | `Allow: /` (not live) | n/a |

**Order:** euro-only named home + privacy on every shop origin → then `Allow: /` on those origins → then consider kit hosts. Flipping Allow first is how the USDC lede gets cached.

Shop-origin `Allow: /` does **not** require indexing `kit-pay.html` or leftover EN tools. If those files remain on a host, give them `noindex` or keep them off the named origin.

### Catalog cutover (do not cut mailed links)

Cutover = one sales origin + sticky old URLs. It is not a delete.

**Keep 200 (redirect to named origin is OK; 404 is not):**

| URL | Why sticky |
| --- | --- |
| `https://sovereignforge.surge.sh/` and `/pakketten.html` `/betalen.html` `/contact.html` `/privacy.html` | Named live shop. Canonical on the chalkboard face. |
| `https://treasury-tools.surge.sh/` | README “Live catalog”; Twelve.tools mention; prior catalog origin. |
| `https://club-site-kit-treasury.surge.sh/` | Voorbeeld linked from both live catalogs; Golfbreker demo. |
| `https://menu-kit-treasury.surge.sh/` `sponsor-kit-treasury.surge.sh` `lid-kit-treasury.surge.sh` `vakman-kit-treasury.surge.sh` `inbox-ops-treasury.surge.sh` | Linked from live `/pakketten.html` and treasury-tools ItemList. |
| `https://pipeline-treasury.surge.sh/` `peppol-chase-treasury.surge.sh` `dual-invoice-treasury.surge.sh` `peppol-ready-treasury.surge.sh` `solana-invoice-treasury.surge.sh` | Still in live tables / JSON-LD. May drop from **marketing home** later; hosts stay. |
| `https://csv-cleaner-treasury.surge.sh/` `form-to-email-treasury.surge.sh` `rss-to-webhook-treasury.surge.sh` | README + leftover catalog. EN USDC tools. Sticky, not sales face. |

**Mailed (do not 404 whatever URL was in the mail):**

- PR #105: **Dolfijnen Middelkerke — mailed once**; KWZC already first outreach. This repo does not store the exact href. Treat named Surge + club-site kit as the possible paste.
- PR #103 Geel `info@` log: **no mail sent**.
- Other sweep PRs: “Nothing was emailed” / “No mail sent”.

Until the mailed href is recovered from the sent box, **do not retire** `sovereignforge.surge.sh`, `treasury-tools.surge.sh`, or `club-site-kit-treasury.surge.sh`.

**Cutover steps (when a real shop tree exists — not this PR):**

1. Publish euro-only chalkboard HTML to **`sovereignforge.surge.sh` only**.
2. Leave kit hosts on their current Surge names.
3. Point `treasury-tools.surge.sh/` at a **200 redirect or duplicate index** to the named origin. Do not 404.
4. Grep live `/` `/pakketten.html` for `USDC|Solana|Phantom` → none on marketing files.
5. Then `robots.txt` `Allow: /` on the named origin (and treasury-tools if it still serves a face).
6. `.be` stays unpublished until there is an OVH **zone** (not just invoice #256963027). No records in this review.

### `.be` / OVH (observe only)

| Claim | Source | This pass |
| --- | --- | --- |
| Domain paid | User: OVH **#256963027** | Not re-fetched from OVH (no connector). Quoted as given. |
| No zone yet | User | Matches **NXDOMAIN** / no NS of our own |
| Publish `.be` | Forbidden | Not done |
| Invent A/AAAA/CNAME/NS | Forbidden | Not done |

`whois` is not available in this environment. Absence of a whois dump is not a zone.

---

## Design-out list

Do **not** do these from the Builder DEPLOY seat (or from this PR):

1. **No `.be` DNS invent.** No OVH zone create, no NS, no A/AAAA, no CNAME, no `www`. Invoice #256963027 ≠ a zone.
2. **No `.be` Surge publish.** Live stays `sovereignforge.surge.sh`.
3. **No `surge .` of this repo (`main` or PR #111) onto `sovereignforge.surge.sh` or `treasury-tools.surge.sh`.** That is leftover HTML overwriting the shop.
4. **No 404 of mailed / listed Surge URLs** (named origin, treasury-tools, club-site kit, other kit hosts, leftover EN tools).
5. **No robots `Allow: /` on the named origin while USDC remains on `/`.**
6. **No delete of kit hosts** to “clean the catalog.” Drop SKUs from marketing copy only.
7. **No fake KBO / BE0 / FACTUUR** on a future face.
8. **No claiming inhouse CI or red/green deploy exists.** It does not.
9. **No Stripe live keys** on treasury-tools (sandbox link is already test-only; do not promote it on the named origin).
10. **No paper-bot / journal code** in a shop deploy.
11. **No merge of PR #111 as the live shop** (€9/€49 ≠ live ladder; cream ≠ chalkboard).
12. **No treating `catalog.html` on `main` as the live catalog.** It is leftover EN USDC.

---

## What would turn DEPLOY green

All of:

- Named origin `/` and `/pakketten.html` grep-clean of `USDC|Solana|Phantom|crypto|wallet` (betalen may keep checkout in a separate file, unlinked from the marketing lede, or “betaalgegevens na akkoord” with no address on the face).
- Integer euro prices on the live ladder (€199 / €249 / €299 / €349 / €900 as the FIX seat specified — not €9/€49).
- `robots.txt` `Allow: /` **after** the euro face is live; meta and robots agree.
- Privacy 200 on **every** shop origin that still serves a face (`treasury-tools` today: fail).
- Publish path is **not** `main` leftover HTML. Document the actual directory / branch that Surge uses.
- A red/green check (even a one-shot script) that curls live `/` + `robots.txt` before calling a host “shipped”.
- `.be` still unpublished until a real zone exists.

Until then: **RED**. Serve Surge. Do not touch OVH DNS.

---

## Probe log (2026-08-27 ~19:14–19:17 UTC)

Method: `curl -sSI` / `curl -sS`, `dig @1.1.1.1`, `getaddrinfo`. No browser. No OVH API. No Surge deploy.

```
sovereignforge.surge.sh/          200  5360  Surge HIT  USDC on face
  /robots.txt                     200    26  Disallow: /
  /pakketten.html                 200  6896  USDC column
  /betalen.html                   200  5076  USDC checkout + printed address
  /contact.html                   200  2127  mail only
  /privacy.html                   200  4353
  /catalog.html                   404  1917  custom NL 404
  /CNAME                          200    24  "sovereignforge.surge.sh"
treasury-tools.surge.sh/          200 10952  euro face, cream, 11 kits
  /robots.txt                     200    26  Disallow: /  (meta index,follow)
  unknown path                    404  8247  Surge default 404
sovereignforge.be                 NXDOMAIN (be. SOA)  — no zone, no invent
```

Sibling: reviewer rubric PR https://github.com/eyeskull2220/solana-invoice/pull/112 (FAIL, live USDC + Disallow). Euro-face PR https://github.com/eyeskull2220/solana-invoice/pull/111 (not live, wrong prices). Adversarial 06 transcript incomplete; this file is the scored DEPLOY note.
