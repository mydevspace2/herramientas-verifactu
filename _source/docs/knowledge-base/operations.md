# Operations: accounts, where things live, how to build and deploy

No passwords, tokens or codes are in this file. Logins are in Yasir's Hark vault or in his own head.

## Accounts (by name only)

| Account | Used for | Notes |
|---|---|---|
| **GitHub `mydevspace2`** | Hosts both sites (GitHub Pages) and their repos: `mydevspace2/numer-ksef` and `mydevspace2/herramientas-verifactu` | Yasir signed up on his phone (Hark's browser signup was blocked by GitHub's anti-bot check). The account email is not topelitemindset1. Yasir then **connected GitHub to Hark** and installed the Hark GitHub App on both repos. |
| **DigitalPlat** (dashboard.digitalplat.org) | Free domain `numerksef.dpdns.org` | Sign in **with GitHub** (mydevspace2); identity verified via GitHub. Free plan = **1 free domain slot, used**. Registered 12 Nov 2026, expires **12 Nov 2027**, free renewal within 120 days of expiry (from ~15 Jul 2027). DNS: 4 A records `@` → 185.199.108.153 / .109.153 / .110.153 / .111.153, CNAME `www` → mydevspace2.github.io. Apex CNAME is not allowed. |
| **Google `topelitemindset1@gmail.com`** | Google Search Console (KSeF property `https://numerksef.dpdns.org/`, URL-prefix, HTML-tag verified) | Google sign-ins ask Yasir to approve on his phone (number prompt). Keep the `google-site-verification` meta tag in the KSeF `index.html`. |
| **Bing Webmaster Tools** (same Google account) | KSeF site imported from GSC | GSC is linked under Settings. |
| **Facebook `gramideo14@gmail.com`** (Yasir's own) | Planned brand Page "Numer KSeF – darmowe narzędzia" | Hark's login stalled at Facebook's new-device check (13 Nov). Yasir will create the Page from his app. Rule: never log out of his accounts. |
| **Spaceship / Dynadot / Hostinger** | Possible paid domains (verifactuya.com, numerksef.pl) | Nothing bought. Yasir has a Dynadot login. |
| **Ahrefs free tools, SBMM extension** | Keyword data | No account needed for the Ahrefs free tools. SBMM runs in Yasir's own Chrome. |

## How Hark pushes to GitHub
- Hark works on a local git clone in the project workspace:
  - KSeF: `work/repo/`
  - Verifactu: `work/verifactu/site/repo/`
- It commits there and pushes to `origin main` over HTTPS **as the connected GitHub account** (the GitHub connector supplies the credential; no token is stored in files).
- GitHub Pages redeploys from `main` / root in 1–2 minutes. After a push, check the live URL with curl.
- If a push fails with **403**, the Hark GitHub App isn't installed on that repo. Yasir adds the repo in GitHub → Settings → Applications. This happened once on 13 Nov 2026.
- The App can't edit repo settings (description/homepage returned 403). Yasir can set those by hand.
- **Yasir can edit without Hark:** open a file on github.com → pencil → Commit. Each repo has a plain-English handover `README.md`.

## Where things live (project workspace)
| Path | What |
|---|---|
| `work/knowledge-base/` | This knowledge base |
| `work/tool-site-playbook.md` | Full notes from the 6 videos + realonlineruler |
| `work/research.md` | KSeF competitor research + technical specs |
| `work/seo/` | KSeF keywords, 30-post blog calendar, promo drafts, IndexNow payload, autocomplete scripts and data |
| `work/build/` | KSeF site generator (Python) + `assets-src/` (JS/CSS sources) + `tools/` (minifier) |
| `work/site-v2/` | KSeF build output |
| `work/repo/` | KSeF git clone (= live site) |
| `work/qa/` | KSeF tests + `RESULTS.md` |
| `work/verifactu/` | Verifactu `research.md` and `project-notes.md`; `site/build` (generator), `site/out` (output), `site/repo` (git clone), `site/qa` (tests); `.tools/` (Playwright Chromium, large) |
| `work/niches/` | `plan.md` + raw autocomplete/BOE data |
| `work/domain-shortlist.md` | Domain candidates and prices |
| `/workspace/web/notes/<project>/` | Browser notes (Ahrefs tables, GSC, Bing, DigitalPlat, PageSpeed) |

## Build and test commands

### KSeF (numerksef.dpdns.org)
```
cd work/build/tools && npm install           # once: terser + csso
cd .. && python3 build.py                    # runs tools/minify.js itself, writes work/site-v2/
cd ../qa && npm install                      # once
node test-core.js                            # logic tests (CRC-8, IZ, NIP, MPP, XML, QR, JDG): expect 52/52
node test-site.js                            # links, meta, JSON-LD, one H1, lang, word counts
node test-browser-csp.js                     # real Chromium with CSP (needs Playwright)
python3 validate.py                          # extra checks (XSD in qa/xsd)
```
Deploy:
1. Copy `work/site-v2/*` over `work/repo/`. **Keep** `CNAME`, the IndexNow key file `523ef9e7a671a55d7f695ae2f374abab.txt`, `.nojekyll`, `README.md` and `_source/`.
2. `git add -A && git commit -m "..." && git push origin main`.
3. curl the live pages, then IndexNow the changed URLs (POST `work/seo/indexnow-payload.json` format to https://api.indexnow.org/indexnow).

New blog post: add it to `VP.POSTS` in `work/build/v3_pages.py`, then rebuild. The sitemap and related-article blocks update automatically.

Settings live in `work/build/common.py`: `DOMAIN`, `UPDATED_ISO`/`UPDATED_PL` (the "last updated" date), `ASSET_V` (cache-busting version), `INDEXNOW_KEY`.

### Verifactu (herramientas-verifactu)
```
cd work/verifactu/site/build/tools && npm install
cd .. && python3 build.py                    # writes work/verifactu/site/out/
#   env: VF_SITE_URL, VF_BASE (default /herramientas-verifactu), VF_CNAME, VF_GSV (Search Console token)
cd ../qa && npm install @xmldom/xmldom jsdom playwright   # once
node test-core.js                            # 42 unit tests incl. 3 official AEAT hash examples
python3 test-xsd-qr.py                       # XML vs official XSD + QR read-back (lxml, pillow, zxing-cpp)
node test-site.js                            # 112 static checks
node test-browser-csp.js                     # Chromium + CSP (PLAYWRIGHT_BROWSERS_PATH=work/verifactu/.tools/browsers)
```
After a sandbox reset Playwright may need `sudo npx playwright install-deps chromium`. Deploy by copying `site/out/*` over `site/repo/` (keep `README.md`, `_source/`, `.gitignore`), then commit and push.

## How to switch a domain

**A. Free → first custom domain on GitHub Pages** (e.g. Verifactu → verifactuya.com):
1. Buy it (only with Yasir's explicit OK; 1 year; auto-renew off; free WHOIS privacy).
2. DNS at the registrar (or Cloudflare free): 4 A records `@` → the GitHub Pages IPs above, plus CNAME `www` → `mydevspace2.github.io`.
3. Rebuild for the root. For Verifactu:
   ```
   VF_SITE_URL=https://verifactuya.com VF_BASE= VF_CNAME=verifactuya.com python3 build.py
   ```
   Then copy and push.
4. GitHub repo → Settings → Pages → Custom domain → Save → wait for "DNS check successful" → tick **Enforce HTTPS**.
5. Check that `www` → root returns a 301 and that the old github.io URL redirects.
6. GSC (Domain property via DNS TXT if DNS is at Cloudflare; otherwise URL-prefix + `VF_GSV` meta tag), then the sitemap, Request Indexing, Bing import and IndexNow key.

**B. Existing live domain → new domain** (e.g. numerksef.dpdns.org → numerksef.pl):
1. Buy the new domain and set it up as in A.
2. Change `DOMAIN` in `work/build/common.py`, then rebuild (canonical, OG, sitemap, hreflang and robots all follow).
3. Put the new name in `CNAME` in the repo and push. GitHub serves the new domain.
4. **301 every old URL to the same path on the new domain.** GitHub Pages can't 301 from a second domain. Free option:
   - Point `numerksef.dpdns.org` at **Cloudflare free** (change nameservers in DigitalPlat if allowed).
   - Add a Redirect Rule `https://numerksef.dpdns.org/*` → `https://numerksef.pl/${1}`, 301, preserving the path and query.
   - Fallback: keep a tiny GitHub repo on the old domain with per-page HTML (meta refresh + canonical), which is weaker.
5. GSC: add and verify the new property, then on the **old** property use Settings → **Change of Address**. Submit the new sitemap. Bing has a similar Site Move tool.
6. Keep the old free domain renewed for at least a year so the redirects keep working.
7. Expect a dip of a few weeks. The earlier the switch, the smaller the loss.

## Zero-budget rules
- No paid hosting, plans, slots, links, ads or tools. Free tiers only: GitHub Pages, DigitalPlat, Ahrefs free, autocomplete, SBMM.
- The only acceptable spend is a cheap domain, **1 year only, auto-renew off**, and **only after Yasir's explicit "buy it"**. Compare first-year and renewal prices, including tax.
- Tools must be 100% client-side (no server costs, no paid APIs).
- Don't sign up for anything that needs a card unless Yasir asks.

## Approval rules
- **Ask first:**
  - any purchase or payment
  - **every** public post, comment or group message (approval covers that one post only)
  - creating accounts or Pages
  - anything binding or destructive
- **No approval needed:** building and testing, pushing to his own repos, GSC/Bing/IndexNow submissions, and research.
- **Never:**
  - log out of his accounts (standing rule)
  - create fake personas
  - state unverified legal dates or fine amounts on the sites
  - put passwords or tokens in files
