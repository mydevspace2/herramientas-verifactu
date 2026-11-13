# Herramientas Verifactu – handover guide

Free Spanish toolkit for Verifactu, mandatory B2B e-invoicing (RD 238/2026) and late payments (Ley 3/2004). Owner: Yasir Ali. Everything here belongs to you and keeps running without Hark. The website itself is in Spanish; this guide is in English.

**Live address (now):** https://mydevspace2.github.io/herramientas-verifactu/
**Planned domain:** `verifactuya.com` – fully prepared on the branch `domain-verifactuya`, **not live**. See "Switching to verifactuya.com" below.

## What the site has
| Page | Address (after the live address) | What it does |
|---|---|---|
| Home – "¿Estoy obligado a Verifactu?" | `/` | 4-question checker + the dates: 1 Jan 2027 / 1 Jul 2027 (in the BOE) and October 2028 (announced 5 Oct 2026, **not** in the BOE) |
| QR generator | `/generador-qr-verifactu/` | Official QR URL, level M, 30–40 mm, margin, "QR tributario:" + VERI*FACTU caption, mm print preview (A4 / 80 mm / 57 mm), SVG + PNG 600 dpi download, print at real size |
| QR validator / reader | `/validar-qr-verifactu/` | Paste URL, upload photo, paste screenshot or use the camera; checks domain (phishing), path, 4 parameters, AEAT error codes 1001–2006 |
| Huella (hash) calculator | `/calcular-huella-verifactu/` | SHA-256 for alta, anulación and evento + chain checker for an XML file; reproduces the 3 official AEAT examples |
| XML example builder | `/ejemplo-xml-verifactu/` | Builds a RegistroAlta (RegFactuSistemaFacturacion) with its huella + basic structure check |
| B2B e-invoicing – "¿cuándo me obliga?" | `/factura-electronica-obligatoria/` | Dates from RD 238/2026 + Orden HAC/1028/2026 (6 Oct 2027 / 6 Oct 2028 / 6 Oct 2029), 4-question checker, 4-day reporting deadline calculator (weekends + BOE national holidays) |
| Average supplier payment period (PMP) | `/periodo-medio-pago-proveedores/` | ICAC 2016 method (memoria normal: rows or CSV/paste from Excel; memoria abreviada: balances), paid/pending ratios, 60-day check, Ley 18/2022 counts, printable memoria table, CSV export |
| Late-payment interest | `/intereses-demora-comerciales/` | Multi-invoice, official BOE rate per semester 2013-2 → 2026-2 (each with its BOE id), optional agreed rate, 40 € per invoice (art. 8.1 + CJEU C-585/20), due-date helper, print/CSV |
| Guides | `/blog/` + 6 posts | Dates BOE vs announced · "Verifactu gratis" · QR size and position · Verifactu vs B2B e-invoice · B2B e-invoice for autónomos · how to calculate the PMP (example + Excel) |
| Legal | `/sobre-nosotros/`, `/contacto/`, `/aviso-legal/`, `/privacidad/`, `404.html` | |

Everything runs in the visitor's browser. No server, no cookies, no analytics, no ads.

## Where everything lives
| What | Where | Login |
|---|---|---|
| Website files | This GitHub repo (`mydevspace2/herramientas-verifactu`, branch `main`) | GitHub account mydevspace2 |
| Hosting | GitHub Pages (free): repo → Settings → Pages, deploys from `main` / root | same |
| Source code + tests | `_source/` in this repo (blocked for search engines in `robots.txt`) | – |

## IMPORTANT: keep the dates up to date
The site says (checked 13 Nov 2026): the BOE dates are **1 Jan 2027** (companies) and **1 Jul 2027** (everyone else); Hacienda **announced** a delay to **October 2028** on 5 Oct 2026, not yet in the BOE.
When the delay is published in the BOE (a new Real Decreto / Real Decreto-ley), update these files the same day:
1. `index.html` – the "Estado a 13 de noviembre de 2026" box and the "Última comprobación" line.
2. `blog/fechas-verifactu-2027-2028/index.html` – the short answer and the tables.
3. `assets/page-home.js` – the checker result text (search for "octubre de 2028").
Check it here: https://www.boe.es/buscar/act.php?id=BOE-A-2023-24840 (look under "Disposición final cuarta" for a modification newer than 03/12/2025).
Do not add fine amounts (sanciones) unless you verify them in the BOE first.

### B2B / late-payment section – what to update and when (checked 13 Nov 2026)
- **Late-payment interest rate, every semester** (BOE publishes it around 28 Jun and 30 Dec; search BOE for "tipo legal de interés de demora aplicable a las operaciones comerciales"). Add the new row in 3 places: `_source/build/assets-src/b2b.js` (`TIPOS`), `_source/build/page_b2b.py` (`TIPOS`), `_source/qa/boe-tipos-demora.json`; then rebuild. Until the 1st-semester-2027 rate is added, the calculator refuses periods in 2027 unless the user ticks "estimar".
- **National holidays for the 4-day calculator**: 2026 and 2027 come from the BOE lists (BOE-A-2025-21667, BOE-A-2026-21254). When the 2028 list is published (October 2027), add it to `FESTIVOS` in `b2b.js`. Until then 2028+ is marked "provisional".
- **B2B dates**: RD 238/2026 (BOE-A-2026-7295, consolidated text last updated 31/03/2026) and Orden HAC/1028/2026 (BOE-A-2026-20587, in force 06/10/2026). If either is amended, update `page_b2b.py`, `page_b2b_blog.py`, `b2b.js` (`FECHAS_B2B`) and the "Última comprobación" date.

## Quick edits (phone or PC, no tools needed)
1. Open the file on github.com (for example `index.html`).
2. Tap the pencil icon, change the text, then "Commit changes".
3. The site updates in 1–2 minutes.
Tip: for bigger changes, paste the file into any free AI (ChatGPT, Gemini), ask for the change, and paste the result back. Keep links starting with `/herramientas-verifactu/` while the site lives on github.io.

## Google Search Console (not set up yet)
1. Add a URL-prefix property for the live address.
2. Choose "HTML tag" verification and copy the `content="..."` value.
3. Either edit `index.html` and add `<meta name="google-site-verification" content="VALUE">` right after `<meta charset="utf-8">`, or rebuild with `VF_GSV=VALUE` (see below).
4. Submit `sitemap.xml` and use URL Inspection → Request Indexing on each page.
Note: on a github.io sub-folder, Google ignores `robots.txt` (it only reads it at the domain root). The sitemap still works when submitted in Search Console. A custom domain fixes this.

## Moving to your own domain (older notes – for verifactuya.com use the branch `domain-verifactuya`)
DigitalPlat said "Free domain slots: 0 available" on 13 Nov 2026 (your one free slot is used by numerksef.dpdns.org). Options: wait for the GitHub-star bonus slot, or buy a cheap `.es`/`.com` later.
When you have a domain (example `herramientasverifactu.dpdns.org`):
1. DNS: 4 A records for `@` → 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153, and CNAME `www` → `mydevspace2.github.io` (exactly like numerksef.dpdns.org).
2. Rebuild for the root of the domain (all links change from `/herramientas-verifactu/...` to `/...`):
   ```
   cd _source/build
   VF_SITE_URL=https://herramientasverifactu.dpdns.org VF_BASE= VF_CNAME=herramientasverifactu.dpdns.org python3 build.py
   ```
   then copy `_source/out/*` over the repo root (keep `README.md` and `_source/`).
3. GitHub → Settings → Pages → Custom domain → enter the domain → Save. When the certificate is ready, tick "Enforce HTTPS".

## Full rebuild (optional, for developers)
Requirements: Python 3 with Pillow, Node 18+.
```
cd _source/build/tools && npm install          # terser + csso (minifier)
cd .. && python3 build.py                      # writes _source/out/
```
Optional environment variables: `VF_SITE_URL`, `VF_BASE`, `VF_CNAME`, `VF_GSV`.

Tests (`_source/qa/`):
```
cd _source/qa && npm install @xmldom/xmldom jsdom playwright && npx playwright install --with-deps chromium
node test-core.js          # unit tests: 3 official AEAT hash examples, NIF, QR URL, XML, chain
node test-b2b.js           # unit tests: PMP (ICAC worked examples), interest (BOE rates), 4-day deadline, B2B dates
python3 test-xsd-qr.py     # XML vs official AEAT XSD (lxml) + QR read-back (pip install lxml pillow zxing-cpp)
node test-site.js          # links, meta, JSON-LD, hreflang, CSP, sitemap, word counts
node test-browser-csp.js   # real Chromium with CSP enforced: every tool, dark mode, mobile 375 px
```

## Rules worth keeping
- Always show "in the BOE" vs "only announced" separately for the dates.
- No fine amounts unless verified in the BOE.
- AdSense: apply only after ~3 months and real traffic; add `ads.txt` after approval. Adding ads also means updating `privacidad/` and a cookie consent banner.
- Third-party code: QR encoder based on Project Nayuki (MIT); QR reader jsQR (Apache 2.0).

## Switching to verifactuya.com
Everything is ready on the branch **`domain-verifactuya`** (CNAME file, all canonical/OG/sitemap/hreflang URLs on https://verifactuya.com, brand "VerifactuYa"). `main` stays on the github.io address until you merge. The exact steps are in that branch's README ("Switch to verifactuya.com – exact steps").
