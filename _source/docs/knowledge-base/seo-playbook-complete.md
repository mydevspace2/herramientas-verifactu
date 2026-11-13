# SEO playbook: the complete version

Written 13 Nov 2026 for Yasir's zero-budget micro-tool website business.

**Source tags** (each rule says where it came from):
- **[V]**: from the 6 Compile Future videos, his blog, or the realonlineruler.com analysis. Full notes are in `work/tool-site-playbook.md`.
- **[O]**: our own experience building numerksef.dpdns.org (KSeF, Polish) and Herramientas Verifactu (Spanish), 12–13 Nov 2026.
- **[R]**: our niche research of 13 Nov 2026 (`work/niches/plan.md`, `work/verifactu/research.md`, `work/research.md`).
- **[V→O]**: a video rule that we changed to fit a zero budget.

**Honesty rule.** Neither site has any traffic or ranking data yet: both are days old. Every volume figure below is an Ahrefs free-tool bucket (for example ">100" or ">1K"), so treat it as an estimate.

---

## 1. Idea finding

1. **[V] Start from a small, real problem.** Good sources:
   - your own Google searches (write each one down)
   - `"is there a tool for" site:reddit.com` (also try `site:quora.com`)
   - asking an AI for *problems*, not for website ideas
   
   Big problems attract funded companies; small ones rank faster.
2. **[V] Keep winning ideas private.** After his ruler video, 100+ clones appeared.
3. **[O] New laws create new searches.** A legal deadline (an e-invoicing mandate, a new payment rule) creates searches that big sites haven't covered yet. Both of our sites came from this:
   - KSeF numbers must appear in Polish bank transfers from 1 Jan 2027.
   - Spain's Verifactu dates are 2027 in the BOE, with a delay to Oct 2028 announced.
4. **[R] Mandate niches fill up fast.** By Nov 2026 almost every EU e-invoicing niche already had 8–17 free tool pages. Look for **boring, formula-based tasks** where the results are mostly PDFs and government pages with only 1–2 tools. The Spanish *periodo medio de pago a proveedores* calculator is the one example found so far.
5. **[R] Check client-side feasibility early.** We only build tools that run 100% in the browser (static JS, no paid API, no server). That is what keeps hosting free.

## 2. Keyword research (free tools only)

| Tool | What we use it for | Tag |
|---|---|---|
| **Ahrefs Free Keyword Generator** (ahrefs.com/keyword-generator) | Volume bucket per country, the Questions tab (FAQ and blog ideas), related keywords. Change the country for non-US checks. Free view shows ~20 rows and hides KD on lower rows. | [V], used by [R] |
| **Ahrefs Free Traffic Checker** | A competitor's monthly organic traffic, trend, top keywords and countries. Also gives per-keyword volumes for those keywords. | [V], used by [R] |
| **Ahrefs Free Backlink Checker** | A competitor's links, or our own | [V] |
| **Google Autocomplete** | Type the seed, add a space after it, add a space before it, then try a–z. Add prefixes: "jak / co to / gdzie / czy / kiedy / ile" (PL), "cómo / qué / cuándo" (ES). We scripted it with `suggestqueries.google.com?client=firefox&hl=xx&gl=xx`. KSeF: 350 queries gave 1,158 unique suggestions (`work/seo/autocomplete-raw.json`). Verifactu: 503+ (`work/verifactu/autocomplete.json`). | [V] method, [O] scripted |
| **People Also Ask** | Open and close entries to load more. We also took questions from competitor FAQs, the MF/AEAT FAQs and forums (gofin, ops.pl). | [V], [O] |
| **SBMM** (free Chrome extension) | Shows volume, KD and competitor DR right on Google. Yasir has to run it in his own Chrome, set to the target country/language, and send screenshots. We have not used it yet. | [O] (Yasir's find, 13 Nov) |
| **Urban VPN + local Google** | See the real SERP in the target country | [V]. We used web_search with a country filter instead, which is only an approximation. |

**Thresholds [V]:** US volume about 100 is easy, about 1,000 is medium, about 10,000 is "a bit tough". Start at 100–1K. Volumes for other countries are smaller, so a ">100" bucket in Poland or Spain is a real number.

**Use the exact phrase people type [V+O].** Copy the wording the top sites share, not your own. We rewrote every KSeF title and H1 from the strongest autocomplete phrases. The home page targets "numer KSeF w przelewie", for example. See `work/seo/keywords.md`.

**Cluster, then map one page per cluster [O].** KSeF has 13 clusters (C1–C13). Each maps to a tool page or a blog post. Navigational and brand clusters (login, certificates, Comarch/Optima) are skipped on purpose.

**Exclude brand and irrelevant keywords [V].** Wrong keywords can hurt ranking.

## 3. The competition judgement

**Read the SERP yourself; ignore Ahrefs' KD for English [V].** These are good signs:
- top domains don't contain the keyword
- big multi-tool sites rank, not dedicated ones
- Reddit, Quora, PDFs, Play Store pages, blogs or government pages appear on pages 1–4 (a "golden keyword")
- subdomain sites (vercel.app etc.) rank

**Competitor audit [V+O].** Open each top site and list its bugs and missing features. Our site must fix all of them. Examples from KSeF: competitors checked one number at a time, didn't validate the IZ (collective identifier), had no MPP (split payment) builder, no CSV export, and showed a wall of text above the tool. See `work/research.md` §1–2.

**Traffic check [V].** Put 3+ competitors into the Traffic Checker and look at traffic, trend, keywords and countries.

### NEW RULE: the crowding (swarm) check [R], added 13 Nov 2026
> **If 8 or more dedicated free tools sit on pages 1–2 and most of them show 0 traffic in the Ahrefs Traffic Checker, skip the niche as a new domain.**

Why: in every EU e-invoicing and finance-calculator niche we tested, many new AI-built tool sites already exist and get zero organic traffic. Examples: verifactuhoy.com, facturaobligatoria.es, factulupa.es, einvoicechecker.com, efacturaspv.ro, ksefnarzedzia.pl, all at 0. A new domain would probably sit at 0 for months too. The pages that do get traffic are old or authority domains and guide+tool hubs (zinsen-berechnen.de, qr-platba.cz, fiskalopedija.hr).

What to do instead:
- **Grow an existing site into a country hub.** Add the new tool as a section of the site that already serves that language, so it adds topical authority to an ageing domain.
- Start a new domain only for a **new country or language**, or for a SERP that is really empty.
- The Verifactu site was built anyway as a cheap experiment (Yasir's choice, 13 Nov 2026), knowing it is crowded. It is now being grown into a Spanish B2B e-invoicing hub.

## 4. The international gap trick [V]

1. Take a proven English tool keyword and translate it.
2. Check the translated keyword in the Ahrefs Keyword Generator for the target country.
3. Search it on the local Google through a VPN.
4. Put the #1 local site into the Traffic Checker to find the words locals really type. Machine translation is often wrong.

Then decide by volume:
- **1K+ and easy in one language:** build a dedicated single-language site. The language goes on the root (no /pt/), with `hreflang` and `<html lang>`.
- **100–1K:** add i18n (language versions) to an existing site. He says this can multiply traffic 4–10×.

**[O] Our version: start local, not from English.** Both our sites target non-English laws with no English equivalent (Polish KSeF, Spanish Verifactu). Hreflang there is just `pl` / `es` + `x-default`. Build and test the logic with official examples first, because we can't read every Polish or Spanish nuance by eye.

**Premium countries [V].** He targets the US by default because CPM (ad pay) is high. Our EU-language sites earn lower CPMs (Croatia lowest). A separate research track is looking for niches that can rank in the US/UK/CA/AU; see `niche-pipeline.md`.

## 5. Domain choice

- **[V] Keyword in the domain**, exact or partial. If it's taken, add real / free / online / AI. No hyphens, prefer the shorter name, avoid modifiers that narrow the scope.
- **[V] .com over cheap TLDs and subdomains.** He says .xyz and *.pages.dev-type subdomains "didn't rank". A ccTLD (.pl, .es) helps for one country but may need a local ID.
- **[V] Buy last, for 1 year only, with auto-renew off.** Compare first-year **and** renewal prices including tax. He uses Spaceship (promo codes come and go).
- **[V→O] Zero-budget version:**
  - Start on a **free DigitalPlat domain** (`numerksef.dpdns.org`) or the GitHub Pages address.
  - Buy a cheap real domain once Yasir approves the spend: `numerksef.pl` (shortlisted) and `verifactuya.com` (chosen by Yasir 13 Nov 2026, ~$3.18 first year at Spaceship, not bought yet).
  - Switch early, in the first 1–2 months: the earlier the move, the less ranking is lost. See `operations.md` for how.
- **[O] DigitalPlat gives one free slot per account.** It is used by numerksef. The "+1 slot for starring the repo" bonus was not credited (13 Nov 2026). eu.org approval takes weeks.
- **[O] Check availability with RDAP** (a 404 means available). DNS NXDOMAIN only suggests it's free. See `work/domain-shortlist.md`.

## 6. Site architecture

- **[V] MPA, not SPA.** Every page is a full static HTML page that bots can read without JS.
- **[V] One page per keyword or feature variant**, with the tool above the fold. KSeF has 7 tool pages, one per cluster:
  - `/` validator + transfer title
  - `/przelew-mpp-numer-ksef/`
  - `/identyfikator-zbiorczy-ksef/`
  - `/sprawdz-wiele-numerow-ksef/`
  - `/przelew-z-faktury-xml-ksef/`
  - `/kod-qr-ksef/`
  - `/ksef-od-2027-jdg/`
- **[V] Policy pages linked visibly:** About, Privacy, Terms, Contact. They are required for AdSense.
- **[V] /blog/ for long-tail posts**, with internal links between the posts and the tools.
- **[O] Our stack is different from his:**
  - a Python static-site generator (`build.py`) writes plain HTML
  - vanilla JS assets, minified with terser; CSS minified with csso and inlined
  - hosted on **GitHub Pages**, free, with no traffic cap we have hit
  
  He uses Astro + Cloudflare Pages. Both give zero-JS-by-default static pages.
- **[O] Everything runs in the visitor's browser.** We say so above the fold: "no upload, no sign-up". Competitors that are SaaS funnels can't say this.
- **[O] Auto-detect inputs** where possible. For example, one box accepts either a KSeF number or an IZ.

## 7. On-page SEO

| Item | Rule | What we did | Tag |
|---|---|---|---|
| Title | Main keyword first, under ~60 characters | e.g. "Numer KSeF w przelewie – sprawdź numer i tytuł przelewu" | [V+O] |
| Meta description | Keyword included, under 160 characters, says what the tool does and "free / in your browser" | done on every page | [V] (his blog) |
| H1 | One H1 per page, matching the main phrase | test-site.js checks for exactly one H1 | [V+O] |
| URL | Short slug in the local language containing the keyword | e.g. `/przelew-mpp-numer-ksef/`, `/generador-qr-verifactu/` | [V+O] |
| Content length | **800–1,200+ useful words** under the tool. Grow to 2,000–3,000 if AdSense says "Low value content". realonlineruler has ~2.5–3K words and 5 tables. | KSeF tool pages ~1,000–1,100 words (v3). Verifactu tool pages ≥800 (tested). | [V+O] |
| Tables and worked examples | Real detail: spec tables, examples, limits | KSeF: number structure table, MPP field table, IZ limits. Verifactu: QR size table, hash field order. | [V+O] |
| FAQ + **FAQPage JSON-LD** | Questions from Ahrefs Questions + People Also Ask, no duplicates | 5–8 FAQs per tool page. JSON-LD tested to parse. | [V+O] |
| Other schema | — | Organization, WebSite, WebApplication, BreadcrumbList, Article (blog) | [O] |
| Open Graph + Twitter card | title, description, image, url, type | Self-made 1200×630 OG image per site | [V+O] |
| hreflang | One per language + `x-default`, plus the correct `<html lang>` | `pl` / `es` + `x-default` | [V+O] |
| Canonical | Every page points to its own preferred URL | done | [O] |
| CSP (Content-Security-Policy) | Meta CSP with SHA-256 hashes for the one inline script and the inline CSS, no external scripts | done on both sites; Verifactu tested in real Chromium with CSP enforced (92/92) | [O] |
| Inlined CSS | Put the minified CSS in `<style>` to remove the render-blocking CSS request | done (it was the only PageSpeed opportunity flagged) | [O] |
| "Last updated / legal status" box | Dated "stan prawny na …" / "Estado a …" box with official links | done; important for law topics | [O] |
| No unverified legal claims | Never state penalty dates or amounts that aren't final law | KSeF penalty dates removed. Verifactu shows "BOE vs announced" separately. | [O] |
| Mobile + dark mode | Responsive, dark-mode toggle | 375 px without overflow tested | [V+O] |
| Favicon + logo | SVG logo; don't fiddle with the favicon (Google takes ~7 days to show it) | SVG favicon + 512 PNG | [V] |

**PageSpeed results we got [O].** numerksef.dpdns.org on 13 Nov 2026, Lighthouse 13.6:
- Mobile: Performance **98**, Accessibility 100, Best Practices 100, SEO 100. FCP/LCP 0.9 s, TBT 0 ms, CLS 0.
- Desktop: **100** in every category.

The flagged items were a render-blocking CSS file and slightly unminified JS. We fixed both by inlining the CSS and minifying with terser. The HSTS/COOP/XFO warnings were unscored, and GitHub Pages doesn't let us set those headers. Report: `/workspace/web/notes/.../pagespeed-*/`.

## 8. Technical SEO

| Item | How | Tag |
|---|---|---|
| sitemap.xml | Lists every indexable page. KSeF has 15 URLs, Verifactu 13. Submit it in GSC and Bing. | [V+O] |
| robots.txt | `Allow: /` + `Sitemap:` line. On a github.io sub-folder Google ignores robots.txt (it only reads the host root), but the sitemap still works when submitted. | [V+O] |
| 404 page | Custom `404.html` with `noindex` and links back to the tools. (He also adds a 500 page; GitHub Pages has no 500 page.) | [V+O] |
| **IndexNow** | Put a key file at the root (`/<key>.txt`) and POST the URL list to api.indexnow.org. Bing and Yandex get the pages instantly. KSeF: 15 URLs returned HTTP 202 on 13 Nov 2026. Payload: `work/seo/indexnow-payload.json`. | [O] |
| www → root | GitHub Pages does this automatically when DNS has CNAME `www` → `mydevspace2.github.io`. `http://www.numerksef.dpdns.org/` returns a 301 to `https://numerksef.dpdns.org/` (checked 13 Nov 2026). On Cloudflare he uses the "Redirect www to root" rule + a proxied AAAA `www` → `100::`. | [V] rule, [O] done |
| HTTPS | GitHub Pages → Enforce HTTPS, once the certificate is issued (minutes) | [O] |
| Noindex duplicates | Never let a second address serve the same pages. His Cloudflare `pages.dev` duplicate killed one of his sites. For us, `mydevspace2.github.io/numer-ksef/` already 301s to the custom domain (GitHub does this when a CNAME is set). | [V] rule, [O] checked |
| Keep source files out of the index | Put build source in `_source/` and add `Disallow` in robots.txt. **Done for Verifactu. Not yet live for KSeF:** the KSeF robots.txt is still plain `Allow: /`. | [O] |
| Sitemap `lastmod` format | Must be W3C date format (`2026-11-13`). **Open bug:** the live KSeF sitemap shows `Fri 2026-11-13 2:00 PM PKT (UTC+05:00)` in some `<lastmod>` fields. Fix in `build.py` (the lastmod function) and redeploy. GSC still reported the sitemap as Success. | [O] |

## 9. Google Search Console and Bing

**Google Search Console** (account topelitemindset1@gmail.com) [V+O]:
1. Add the property:
   - We used a **URL-prefix** property verified with an **HTML meta tag** on the home page (`google-site-verification`). That's the easy route when DNS is at DigitalPlat or the site is on github.io.
   - He prefers a **Domain** property verified with a DNS TXT record. That is better once the site is on a real domain with Cloudflare DNS.
2. Submit `sitemap.xml`. KSeF showed **Success, 9 pages discovered** on 13 Nov; there were 15 pages after the SEO pass.
3. URL Inspection → **Request Indexing** for the home page and every new page or post.

**The Request Indexing quota issue [O].** On a brand-new property, Request Indexing returned **"Quota exceeded"** on 12 and 13 Nov 2026, even for the first request of the day. This is common for new sites. What to do:
- Don't keep clicking. The submitted sitemap already makes Google crawl the pages.
- Use **IndexNow** for Bing/Yandex.
- Link every new page from the home page, the blog index and related posts.
- Retry Request Indexing on another day, one or two URLs at a time, most important first.

**Bing Webmaster Tools [V+O]:**
1. Sign in with Google (topelitemindset1).
2. **Import from GSC**. No separate verification is needed.
3. Submit the sitemap. KSeF: Success, 9 URLs.
4. Use URL Submission (100 URLs a day quota) for the home page.

Bing data takes up to 48 h. Bing also feeds DuckDuckGo and Yahoo.

**GA4 [V]:** not added yet. It adds a cookie and needs a consent banner, which we'd only add together with AdSense. GSC is enough for now.

## 10. Content calendar

- **[V] 1 long-tail blog post a day** for ~30 days. Request indexing (and IndexNow) for each. Don't publish all at once.
- **[O] KSeF plan:** 30 posts are planned in `work/seo/blog-calendar.md`, ranked by value.
  - Each is 800–1,200 words, with a table or worked example and 3–5 FAQs.
  - Each links to one tool above the fold and in the summary, plus 1–2 related posts.
  - Each carries a "stan prawny na …" date and an MF source.
  - No penalty dates or amounts.
  - Add each new post to `VP.POSTS` in `build/v3_pages.py`. The sitemap and the "related articles" blocks then update automatically.
  - 3 posts are live; 30 remain.
- **[O] Verifactu:** 3 guides live. The Spanish B2B section is being added now (Nov 2026).
- **[V] Long-tail sources:** Ahrefs Questions, "keyword + how to / what is", PAA, forum threads.
- **[O] Update posts when the law changes.** Law-driven sites lose trust fast if a date is wrong.

## 11. Promotion

- **[V]** Post on Reddit, Quora and social media ("I made this free tool"), and create social profiles with the link in the bio.
- **[O] Per-post approval rule.** Nothing is posted anywhere without Yasir's explicit OK for that specific post. Approval for one post doesn't cover the next.
- **[O] Drafts ready:** 5 Polish promo texts in `work/seo/promo-drafts.md`, none published:
  - a forum answer
  - a Reddit answer
  - an FB group for small businesses (JDG)
  - an FB group for accountants
  - a LinkedIn post
- **[O] Rules in the drafts:**
  - Give concrete help first, with one link only, at the end.
  - Don't mention penalty dates and don't promise "compliance".
  - Read each group's rules first.
  - Space posts days apart, and only answer threads where someone really asked.
- **[O] Facebook Page plan.** Run a **brand Page** named "Numer KSeF – darmowe narzędzia" (category Website, Polish bio, site link), not a fake Polish persona: Facebook bans fake identities. Status 13 Nov 2026:
  - Hark's browser login to Yasir's Facebook (gramideo14@gmail.com) stalled at Facebook's new-device security check.
  - Yasir will create the Page from his phone app using the prepared text. On hold until he says it exists.
  - Then: find Polish JDG/accounting groups that allow Pages, and draft posts for approval.

## 12. Link building

- **[V] Dofollow + contextual links count most.** Nofollow, ugc and sponsored links only send visitors. Footer and sidebar links count less.
- **[V] Own-site network.**
  - From a site of yours that already ranks and gets users, add **one contextual dofollow link with the target keyword as anchor**.
  - Wait about **1 month after the target site launches**.
  - Then add **at most 1 new link per site per month**. When he added ~12 at once, his rankings dropped.
  - Link only **related** sites. KSeF ↔ Verifactu is a weak relation (both e-invoicing, different countries and languages). Use it sparingly, as one "see also" link from a relevant guide.
- **[V] Backlinks also speed up indexing.**
- **[V] Don't buy links or do link swaps;** spammy links can hurt.
- **[O] Zero-budget link sources:**
  - the brand Facebook Page and other social profiles
  - genuine forum answers (nofollow, but real visitors)
  - the GitHub repo pages (repo description/homepage could not be set by Hark: API 403, so Yasir can set them by hand)

## 13. AdSense timing and the "Low value content" fix

- **[V] Never apply in month 1.** His own rule is about **3 months** and real organic traffic. 10–15 users/day has been approved; 1,000/day is his comfort level. "Chase traffic, not AdSense."
- **[V] Requirements:**
  - About/Privacy/Terms/Contact pages, good navigation, mobile, original content
  - a domain that isn't brand new
  - no other ad networks
  - verify with `ads.txt` at the domain root and keep it there permanently
- **[O] AdSense on our addresses.** `ads.txt` must sit at the domain root, so a github.io sub-folder (Verifactu now) can't be verified. Verifactu needs its own domain before applying. Whether AdSense accepts a free DigitalPlat subdomain (`*.dpdns.org`) is **not verified**. Plan to move KSeF to `numerksef.pl` before applying if possible.
- **[V] "Low value content" fix:**
  1. Publish 1 long-tail post a day for ~30 days (10–30 posts) and request indexing for each.
  2. Grow the home page to **2,000–3,000 words** + FAQ.
  3. Reapply **only after ~30 days**. Fast reapplying can trigger a 30–60 day block. If rejected again, wait 3–4 months.
- **[V] After approval:**
  - turn on Auto ads + auto-optimise
  - create the **GDPR (EU) and US consent messages**; ads won't run properly without them
  - **[O]** update `/polityka-prywatnosci/` and `/privacidad/`, because the sites currently say "no cookies"
- **[V] Account rules:** one AdSense account per person, payout at $100.

## 14. Expectations

- **[V]** Ranking usually takes **2–6 months** (easy keywords sometimes 1–2 months; hard ones up to 2 years). Expect about **2–3 out of every 10 sites** to work; his first winner was site 8 or 9. Keep each site live for at least **6–12 months**, and commit to **1–2 years**.
- **[O]** Our sites are at **day 1–2**. There is no traffic or ranking data yet, and none should be expected before December 2026 at the earliest. KSeF's search demand should peak around **Dec 2026 – Jan 2027** (the 1 Jan 2027 deadline). That is our first real test.
- **[R]** In crowded niches, many tool sites get **zero** traffic. A fast, accurate build is necessary but not enough; age, depth (hub) and links decide.

## 15. Mistakes to avoid (combined)

- **[V]**
  - AI-slop design
  - SPAs
  - leaving duplicate hosts indexable
  - brand keywords
  - big problems
  - long AI sessions
  - many links at once
  - applying to AdSense early or reapplying repeatedly
  - sharing winning ideas
  - quitting after one failure
- **[O]**
  - stating unconfirmed legal dates or fines as fact
  - leaving source folders crawlable
  - malformed sitemap dates
  - spending Request Indexing quota by hammering it
  - posting anywhere without per-post approval
  - creating fake personas on social media
- **[R]** Building a new domain in a swarm niche (see the crowding rule, §3).
