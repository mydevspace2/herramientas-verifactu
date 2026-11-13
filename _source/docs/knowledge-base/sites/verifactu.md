# Site 2: Herramientas Verifactu (Spanish Verifactu + B2B e-invoicing tools)

Status as of 13 Nov 2026. There is no traffic or ranking data yet. The site went live on 13 Nov 2026 and is not yet in Search Console.

## What it is
A free Spanish toolkit for Verifactu, Spain's anti-fraud invoicing-software rule (RD 1007/2023). Everything runs in the browser: no server, cookies, analytics or ads. A **Spanish B2B e-invoicing + late-payment section** is being added now (Nov 2026; for example `assets-src/b2b.js` is in progress).

| Item | Value |
|---|---|
| Live URL (now) | https://mydevspace2.github.io/herramientas-verifactu/ |
| Repo | github.com/mydevspace2/herramientas-verifactu, branch `main`, GitHub Pages from root. HEAD `e100cb7`. |
| Domain status | **No own domain yet.** The DigitalPlat free slot is used by KSeF, and the "star" bonus slot was not credited (13 Nov 2026). **Yasir picked `verifactuya.com`** (Spaceship, ~$3.18 first year, ~$10.88 renewal, prices seen 13 Nov 2026). **Not bought:** he wants the site finished first and will say "buy it". Free alternatives seen: herramientasverifactu.com, verifactu24.com. Source: `work/domain-shortlist.md`. |
| Search Console / Bing | **Not set up on purpose.** Do it once, after the domain is live. |
| Tests | Unit 42/42 (3 official AEAT hash examples exact) · XSD+QR 13/13 · static 112/112 · Chromium with CSP 92/92 · live 22 URLs = 200. Source: `work/verifactu/project-notes.md`, `work/verifactu/site/qa/RESULTS.md`. |

### Pages (13 in the sitemap + 404)
| Page | Purpose |
|---|---|
| `/` | "¿Estoy obligado a Verifactu?" 4-question checker + dates (BOE 1 Jan 2027 / 1 Jul 2027 vs **announced** Oct 2028) |
| `/generador-qr-verifactu/` | QR tributario generator: level M, 30–40 mm, "QR tributario:" + VERI*FACTU caption, mm print preview (A4 / 80 mm / 57 mm), SVG + PNG 600 dpi |
| `/validar-qr-verifactu/` | QR validator/reader (URL, photo, screenshot, camera); phishing domain check; AEAT error codes 1001–2006 |
| `/calcular-huella-verifactu/` | SHA-256 huella (hash) for alta, anulación **and evento**, plus chain checker |
| `/ejemplo-xml-verifactu/` | RegistroAlta XML example builder + structure check (valid against the official XSD) |
| `/blog/` + 3 guides | dates (BOE vs announced) · "Verifactu gratis" (the free AEAT app) · QR size and position |
| `/sobre-nosotros/`, `/contacto/`, `/aviso-legal/`, `/privacidad/`, `404.html` | trust/legal |
| *(in progress)* B2B section | Supplier average payment period (PMP, ICAC method) calculator, 2027–2028 B2B e-invoice checker, late-payment interest calculator, more guides (`work/niches/plan.md` §A.4, §C.1) |

## Why this site has scope (and why it's a calculated bet)

**Legal deadlines.**
- **Verifactu (in the BOE):**
  - Corporate-tax payers must adapt before **1 Jan 2027**; everyone else (autónomos etc.) before **1 Jul 2027**.
  - Source: RD 1007/2023 DF 4ª as worded by RD-ley 15/2025 (https://www.boe.es/buscar/act.php?id=BOE-A-2023-24840), confirmed by the AEAT.
- **Verifactu (announced only, NOT law):**
  - Hacienda announced on 5 Oct 2026 that it intends to postpone to **October 2028**. There is no BOE norm yet (checked 13 Nov 2026).
  - Source: https://www.hacienda.gob.es/sgt/gabsehacienda/nota-informativa-verifactu.pdf
  - All of this is in `work/verifactu/research.md` §3.5.
- **B2B e-invoicing (in the BOE, rising):**
  - RD 238/2026 + Orden HAC/1028/2026 (in force 6 Oct 2026) set **6 Oct 2027** for businesses over €8M and **6 Oct 2028** for everyone else.
  - Status/payment reporting for small natural persons runs to **6 Oct 2029** (DT 3ª; our calculation).
  - Source: `work/niches/plan.md` §A.1.

**Who must comply.** Verifactu covers almost every business and autónomo in common-territory Spain that issues invoices with software. The exceptions are SII taxpayers and the Basque Country/Navarra (TicketBAI). B2B e-invoicing covers every business invoicing another business.

**Search demand (Ahrefs ES buckets, estimates).**
- Informational queries are big:
  - "verifactu 2027" >1K Easy
  - "verifactu es obligatorio" >1K **Easy**
  - "verifactu gratis" >1K **Easy**
  - "que es verifactu" >1K
- Tool queries are tiny: "qr verifactu" >100, other QR/huella variants <100.
- B2B side:
  - "ley crea y crece" >1K
  - "intereses de demora" >1K Easy
  - "periodo medio de pago a proveedores" >100 **Easy**, with a near-empty SERP (only 2 calculators, one using the wrong formula)
- Sources: `work/verifactu/research.md` §1, `work/niches/plan.md` §A.2–A.3.

**Competitor gaps** (`work/verifactu/research.md` §2):
- factulupa.es covers almost everything, but its homepage didn't show the 2028 announcement prominently and it has no print-ready QR layout and no evento hash.
- recibeo.com has no XSD validation and no evento hash, and it's a vendor.
- kiwop.com has no obligation checker and no XML.
- All the dedicated tool sites showed **0 Ahrefs traffic**.

Our edge: strict "BOE vs announced" dates, a mm-exact print layout, evento hash, and a B2B/PMP section nobody combines.

**Honest verdict from research:** by the crowding rule this is a weak niche **as a stand-alone Verifactu site** (12+ near-identical tools, tool volume <100, delay likely to cool interest). Yasir chose to build it lean anyway (13 Nov 2026), because it reused the KSeF build at zero cost. Its long-term scope comes from growing into a **Spanish e-invoicing + payments hub**, where the B2B dates rise toward Oct 2027 / Oct 2028.

## Risks
- **Crowded niche:** 12+ free Verifactu tools, all at ~0 traffic.
- **Date risk:**
  - If the 2028 delay is published in the BOE, the site must change **the same day**. There are 3 places to edit, listed in the repo README:
    - `index.html` status box
    - `blog/fechas-verifactu-2027-2028/`
    - `assets/page-home.js`
  - Spain's Cortes were reportedly dissolved, with elections on 29 Nov 2026 (secondary source, unverified), which may delay any BOE norm.
- **No domain yet:**
  - On a github.io sub-folder, robots.txt is ignored and `ads.txt` can't be placed at the root, so **AdSense is impossible until a domain is bought**.
  - Adding a domain later means rebuilding with the new base path.
- **Fines:** don't publish amounts until they are verified in the BOE (art. 201 bis LGT).
- **Low CPM** relative to the US, and lower than the "premium countries" goal.

## Monetisation path
1. Buy `verifactuya.com` (Yasir's go-ahead), rebuild for the root, set up the custom domain + HTTPS, then GSC + Bing + IndexNow.
2. Grow the B2B/PMP section and guides for ~3 months.
3. Apply to AdSense once there is steady organic traffic. Update `/privacidad/` and add a consent banner at the same time, because the site currently says "no cookies".
4. Optional later: an Excel template download for PMP (free; a lead to the calculator), and embeddable widgets.

## 12-month plan (Nov 2026 → Nov 2027)

**Every week:**
- Publish 3–7 Spanish posts (1 a day in the first month after indexing starts).
- IndexNow + Request Indexing per post.

**Every month:**
- Check the BOE consolidated text (RD 1007/2023 DF 4ª) and the AEAT Verifactu + SPFE pages.
- Run the tests before each push.

| Month | Posts / content | Indexing | Links / promo | Domain / AdSense / legal |
|---|---|---|---|---|
| **Nov 2026** (rest) | Finish the B2B section (PMP calculator first, then due date, 4-day deadline, intereses de demora + 40 €, "¿cuándo me obliga?"). | — (no domain yet) | None yet | **Buy `verifactuya.com` when Yasir says "buy it"** (1 year, auto-renew off). Rebuild with `VF_SITE_URL`/`VF_BASE=""`/`VF_CNAME`. |
| **Dec 2026** | Write a Spanish 30-post calendar (dates, "es obligatorio", "gratis", PMP, morosidad). Start 1 post a day. | GSC (Domain or URL-prefix) + sitemap + Request Indexing; Bing import; IndexNow key + submit. | Approved posts only (Spanish autónomo forums/groups). | Watch for a BOE norm on the 2028 delay. |
| **Jan 2027** | Posts continue. Update for the 1 Jan 2027 status (in force vs delayed). | Per post | 1 own-network link at most, and only if a related site ranks | — |
| **Feb 2027** | 8–12 posts. Home page toward 2,000 words. | — | 1 link | Prepare the AdSense prerequisites. |
| **Mar 2027** | PMP posts before cuentas anuales season (Mar–Jul). | — | 1 link | **AdSense only with steady organic clicks.** "Low value content" fix if needed. |
| **Apr–Jun 2027** | 6–10 posts a month. B2B posts ahead of 6 Oct 2027. Update any AEAT SPFE artefacts (UBL validation) once published. | — | 1 link a month | Approval → Auto ads + GDPR consent. |
| **Jul 2027** | Verifactu: if the BOE still says 1 Jul 2027, this is the autónomo deadline month, so refresh everything. | — | 1 link | — |
| **Aug–Oct 2027** | B2B mandate (>€8M) on **6 Oct 2027**: checklists, "copia fiel UBL" guide. | — | 1 link a month | — |
| **Nov 2027** | Annual review. | — | — | **Renew `verifactuya.com` by hand ~Nov/Dec 2027** (1 year after purchase; auto-renew off), only if the site works. |

**Whenever the law changes:** same-day edit of the 3 date places, the checker logic, FAQs and the affected posts; then rebuild, push and IndexNow. Always keep "en el BOE" and "solo anunciado" separate.
