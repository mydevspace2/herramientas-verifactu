# Herramientas Verifactu – project notes (built 2026-11-13)

## Status
- LIVE: https://mydevspace2.github.io/herramientas-verifactu/ (GitHub Pages, repo https://github.com/mydevspace2/herramientas-verifactu, branch main, root). HTTPS enforced automatically (github.io).
- Commits: 5590b68 (v1), e100cb7 (QA), 99b7c2a (B2B + morosidad), a2c0858 (SEO pass + GSC tag), d1e1b26 (AI handover docs), **39c8b7d (2026-11-13: mobile UX fixes) – main HEAD 39c8b7ddac7efea0517f39a29f04b891d58811ae**.
- Branch `domain-verifactuya` = 673382a (673382af11b70125ccbfd72606566a0e8b73748e; rebuilt from main 39c8b7d via merge -s ours + domain build; before: a5295b6 from a2c0858, so merging into main later is a fast-forward; earlier 6a29b2d): same site built for https://verifactuya.com (CNAME, canonical/OG/sitemap/hreflang/robots, brand VerifactuYa) + switch steps in its README. NOT merged, NOT live. Worktree: site/repo-domain. Domain not bought yet.
- Custom domain NOT done: DigitalPlat shows herramientasverifactu.dpdns.org as available, but the account has 0 free domain slots (numerksef.dpdns.org uses the only one). The browser starred github.com/DigitalPlatDev/FreeDomain and re-verified GitHub on DigitalPlat to try the "+1 slot for stargazers" bonus – not credited as of 15:30 PKT; there is no claim button. Paid slots/plans were not used.
- Search Console: HTML-tag token in work/verifactu/gsv.txt (PBIzVZ_WTR9JENZ2TnCvFsTs3YWHua2ZJY0Cq2uO-6k) is live on the homepage since 13/11/2026. ALWAYS build with VF_GSV="$(cat ../../gsv.txt)" or the tag disappears.
- Nothing posted anywhere. No money spent.

## Pages (19 + 404) – v2 adds /factura-electronica-obligatoria/ /periodo-medio-pago-proveedores/ /intereses-demora-comerciales/ + blog diferencias-verifactu-factura-electronica-b2b, factura-electronica-obligatoria-autonomos, calcular-periodo-medio-pago-proveedores-ejemplo
/ (¿estoy obligado? + BOE 2027 vs announced Oct 2028, last checked 13/11/2026) · /generador-qr-verifactu/ · /validar-qr-verifactu/ · /calcular-huella-verifactu/ · /ejemplo-xml-verifactu/ · /blog/ + fechas-verifactu-2027-2028, verifactu-gratis-aplicacion-aeat, tamano-posicion-qr-verifactu · /sobre-nosotros/ /contacto/ /aviso-legal/ /privacidad/ · 404.html

## Where things are (this project workspace)
- Build: work/verifactu/site/build/ (python3 build.py → site/out). Content: page_home.py, page_qr.py, page_dev.py, page_blog.py; template common.py; sources.py (official URLs).
- Assets: site/build/assets-src (core.js = SHA-256, huella, NIF, QR URL build/parse, XML build/check, chain check; qr.js encoder; jsqr.js reader; page-*.js).
- Tests: site/qa (test-core.js, test-xsd-qr.py, test-site.js, test-browser-csp.js), results in site/qa/RESULTS.md. Playwright + Chromium installed in work/verifactu/.tools (set PLAYWRIGHT_BROWSERS_PATH and NODE_PATH; needs `sudo npx playwright install-deps chromium` after a sandbox reset). Sandbox Chromium cannot reach the internet; live checks done with curl + Hark browser.
- Git working copy: site/repo (pushed). Official XSDs (copy from github.com/hectorsipe/aeat-verifactu): verifactu/src/.
- Verified sources: verifactu/research.md + verifactu/src (BOE RD 1007/2023 text, AEAT hash/QR specs fetched 2026-11-13).

## Test results (2026-11-13)
- Unit 42/42 (3 official AEAT hash examples exact, SHA-256 vs Node crypto, NIF/NIE/CIF, QR URL incl. AEAT examples/errors, XML, chain).
- XSD + QR 13/13 (generated XML valid vs official SuministroLR.xsd; QR read back by zxing-cpp at level M; downloaded PNG/SVG checked; SVG QR exactly 35.00 mm).
- Static 112/112 (links, meta, JSON-LD/FAQPage, hreflang es/x-default, CSP, no inline style, sitemap 13 URLs, robots Disallow /_source/, ≥800 words per tool page).
- Chromium with CSP 92/92 (all tools, downloads, print stub, camera not testable, image upload decode via lazy jsQR, dark mode, mobile 375 px no overflow, 404).
- Live: all 22 URLs 200 (404 for unknown path); md5 of live files = tested build; Hark browser smoke test passed all 6 checks.

## To do / decisions for Yasir
- Domain: wait for DigitalPlat star bonus, or buy a cheap .es/.com later, then rebuild with VF_SITE_URL/VF_BASE=""/VF_CNAME and set the custom domain + Enforce HTTPS (see README).
- On github.io sub-path, robots.txt is not read by crawlers (only host root) – fine until a domain is added.
- Update dates the day the 2028 delay is published in the BOE (README lists the 3 places).
- Search Console + Bing when he wants.

## v2 – B2B e-invoicing + late payment section (2026-11-13)
- Code: build/page_b2b.py (3 tool pages), build/page_b2b_blog.py (3 posts), assets-src/b2b.js (PMP ICAC, interest, 4-day deadline, B2B dates; UMD, unit-tested), page-pmp.js, page-b2b.js, page-demora.js. Build env VF_BRAND added (domain branch uses VerifactuYa). sync-repo.sh copies out/ + sources to repo/.
- BOE sources fetched 13/11/2026 into verifactu/src/b2b/ (RD 238/2026, Orden HAC/1028/2026, Ley 3/2004 = BOE-A-2004-21830, ICAC 2016 = BOE-A-2016-1112, Ley 15/2010 DA3, 27 Tesoro rate resolutions 2013-2 → 2026-2 in tipos/, fiestas 2026/2027).
- Facts that differ from the original brief: (1) art. 12.3 RD 238/2026 = 4 días naturales EXCLUDING Saturdays, Sundays and national holidays (not plain calendar days); (2) the >€8M threshold is "volumen de operaciones" (art. 121 LIVA) of the previous calendar year, not turnover; (3) dates 6/10/2027 and 6/10/2028 are not written as dates in the BOE – the BOE says 12/24 months from the Orden's entry into force (06/10/2026); AEAT calendar states the dates; (4) status/payment reporting for personas físicas ≤ €8M: 6/10/2029 (DT 3.ª); (5) €40: law (art. 8.1) says "una cantidad fija de 40 euros" when in mora; "per invoice" comes from CJEU C-585/20.
- Tests 13/11/2026: unit Verifactu 42/42, unit B2B 29/29, XSD+QR 13/13, static 166/166, Chromium CSP 131/131 (= 381). Domain build also passes static 166/166 + Chromium 131/131. Live: 39/39 files byte-identical, unknown path 404.
- Maintenance: add the interest rate every semester (b2b.js TIPOS, page_b2b.py TIPOS, qa/boe-tipos-demora.json); add 2028 holiday list in Oct 2027 (b2b.js FESTIVOS).
- Sandbox reset needs: `sudo npx playwright install-deps chromium` (in .tools) and `pip install zxing-cpp lxml pillow`.

## v3 – SEO pass (2026-11-13)
- Files: seo/keywords.md (autocomplete 238 queries → 910 suggestions + Ahrefs ES buckets), seo/blog-calendar.md (30 posts, #1–2 published), seo/promo-drafts.md (5 drafts, NOT posted), seo/ac.py + raw json.
- On-page: leads now contain each page's keyword; titles changed: huella ("Calcular huella Verifactu (hash SHA-256) gratis y online"), B2B ("Factura electrónica obligatoria: fechas 2027-2028 y test"), PMP ("Periodo medio de pago a proveedores: calculadora y fórmula"), blog index ("Guías: Verifactu, factura electrónica y morosidad"), autónomos post (≤60 chars).
- JSON-LD: Organization + WebSite on every page; WebApplication (tools), CollectionPage (blog), Article with per-post ISO datePublished (field `published`), FAQPage, BreadcrumbList. Build asserts UPDATED_ISO/lastmod are YYYY-MM-DD.
- New posts in build/page_blog_2.py: /blog/verifactu-autonomos/ and /blog/plazos-pago-ley-morosidad/; related-guides map in build.py is slug-based (no more fixed 6-tuple unpack).
- Tests: unit 42 + B2B 29 + XSD/QR 13 + static 205 + Chromium CSP 143 = 432/432 (domain build: static 205 + Chromium 143). Live: 41/41 files byte-identical, 404 for unknown path.

## v4 – UX móvil (2026-11-13, from work/ux-audit/report.md)
- Home: test «¿estoy obligado?» right under H1 + one-line lead; the date-status card (same dates/sources) now sits BELOW the test. B2B page: test first, then the date card, then the 4-day calculator. On 375×812 the home test card starts at 337 px (was ~1,350), B2B at 403 px (was ~1,980).
- Question tests (home + B2B): result appears as soon as every question is answered (button kept), Enter on an option submits, result scrolls into view (UI.autoForm / UI.reveal in ui.js); «Copiar resultado» button on obligation, B2B and 4-day results (copies plain text + page URL).
- CSS: .status text wraps (overflow-wrap:anywhere) so long hashes never widen the page; all text inputs ≥16 px (rows-table inputs were 15.2 px); .btn.small and row ✕ buttons 44 px; .badge/.tag 13 px; grid children min-width:0.
- Wording: badge «Sin publicidad ni seguimiento» → «Gratis, sin registro» (+ «Los datos no salen de tu navegador.»); removed «sin publicidad» from footer, About and privacy meta description. Privacy body paragraph kept (it already says the policy will be updated before any ads/analytics). Footer «sin cookies y sin seguimiento» kept (true today) – must change if AdSense/analytics are added.
- No legal data, dates or rates changed (only moved). New test qa/test-ux-mobile.js (34 checks) + qa/run-all.sh. Total 466/466.
- Deployed 39c8b7d: live check 37/37 HTML/JS/XML/TXT files byte-identical, unknown path 404. IndexNow is NOT configured on this site (no key file), so no ping was sent.

## Daily run 2026-11-14 (Phase 1, day 1 of the scheduled task)
- Published 3 posts (build/page_blog_2.py, `published` 2026-11-14): /blog/tipo-interes-demora-2026/ (#5), /blog/reclamar-factura-impagada-intereses/ (#29), /blog/informar-pago-factura-4-dias/ (#23). Figures only from local BOE copies (src/b2b/tipos/tipos.json, ley3.txt, act-BOE-A-2026-7295.txt) and the calculator code (b2b.js interes/plazo4) for worked examples. New sources in sources.py: TESORO26A, TESORO25B, FIESTAS26.
- Internal links: REL map in build.py (TID/REC/INF), contextual links added in /intereses-demora-comerciales/, /factura-electronica-obligatoria/ (4-day section) and /blog/plazos-pago-ley-morosidad/.
- Fix: 4-day section on /factura-electronica-obligatoria/ said adding regional holidays was the "safe" option (it gives a LATER date). Reworded: prudent = don't count them.
- Build: common.UPDATED_ISO now = VF_UPDATED or today's date (sitemap lastmod + «Última revisión» update on every build). qa/test-site.js sitemap test now counts pages instead of a hard-coded 21.
- BOE checks: RD 1007/2023 consolidated still «última actualización 03/12/2025» → Verifactu 2028 delay NOT in BOE. No new Tesoro rate (next ~end Dec 2026 for 1st half 2027).
- Tests 493/493 (42+29+13+232+143+34). 24 URLs in sitemap. Calendar: 5/30 done; 25 left (B2B/morosidad left: #6, #20–22, #24–28, #30).
- Domain branch domain-verifactuya NOT rebuilt (rebuild before merging once the domain is bought).
