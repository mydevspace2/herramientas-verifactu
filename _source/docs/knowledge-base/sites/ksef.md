# Site 1: NumerKSeF (Polish KSeF tools)

Status as of 13 Nov 2026. There is no traffic or ranking data yet; the site went live on 12–13 Nov 2026.

## What it is
A free Polish toolkit that helps businesses put the correct **KSeF number** (the ID that Poland's national e-invoice system gives every invoice) into bank transfers. Everything runs in the visitor's browser: no sign-up, no upload, no ads (yet).

| Item | Value |
|---|---|
| Live URL | https://numerksef.dpdns.org/ (HTTPS enforced; www → root 301; old github.io address 301s here) |
| Brand | NumerKSeF / "Numer KSeF – darmowe narzędzia" |
| Repo | github.com/mydevspace2/numer-ksef, branch `main`, GitHub Pages from root. HEAD `8e7f502` (handover README + `_source/`). |
| Domain | `numerksef.dpdns.org`, a free DigitalPlat domain registered 12 Nov 2026. **Expires 12 Nov 2027.** DigitalPlat says "Free renewal is available within 120 days of expiry", so the window opens about **15 Jul 2027**. DNS is at DigitalPlat: 4 A records → GitHub Pages IPs, CNAME `www` → mydevspace2.github.io. |
| Paid domain plan | `numerksef.pl` is the top pick (exact match, .pl helps in Polish Google, ~$4–5 first year at Hostinger/Dynadot; renewal is much higher, so check it). Backup: `numerksef.com`. **Not bought.** Buy only on Yasir's explicit go-ahead, for 1 year, with auto-renew off. Source: `work/domain-shortlist.md`. |
| Search Console | URL-prefix property `https://numerksef.dpdns.org/`, verified by HTML meta tag, on topelitemindset1@gmail.com. Sitemap: Success. Request Indexing hit "Quota exceeded" on 12–13 Nov. |
| Bing | Imported from GSC; sitemap Success (9 URLs at import); home page submitted. IndexNow: 15 URLs, HTTP 202. |
| PageSpeed (13 Nov) | Mobile 98 / 100 / 100 / 100; desktop 100 across the board |
| Tests | 52/52 logic tests (`work/qa/test-core.js`) + site tests (`work/qa/test-site.js`); results in `work/qa/RESULTS.md` |

### Pages (15 in the sitemap + 404)
| Page | Purpose / main keyword |
|---|---|
| `/` | KSeF number validator (CRC-8, NIP, date) + transfer title builder. Keyword: "numer KSeF w przelewie" |
| `/przelew-mpp-numer-ksef/` | MPP (split payment) message builder `/VAT/…/IDC/…/INV/…/TXT/…` |
| `/identyfikator-zbiorczy-ksef/` | Collective identifier (IZ) validator and breakdown |
| `/sprawdz-wiele-numerow-ksef/` | Bulk/CSV/bank-statement checker with CSV export |
| `/przelew-z-faktury-xml-ksef/` | FA(3) XML invoice → payment data card |
| `/kod-qr-ksef/` | KSeF QR (KOD I) link checker and generator, with an anti-phishing check |
| `/ksef-od-2027-jdg/` | "Does KSeF apply to my sole proprietorship (JDG) from 2027?" checker |
| `/blog/` + 3 posts | how to write the KSeF number in a transfer title · where to find the KSeF number · what the collective identifier is |
| `/o-serwisie/`, `/kontakt/`, `/regulamin/`, `/polityka-prywatnosci/`, `404.html` | trust/legal pages |

## Why this site has scope (the reasons, with sources)

1. **A hard legal deadline creates new searches.** From **1 Jan 2027**, payments between active VAT payers (including MPP) must carry the KSeF number of the invoice, or a collective identifier for several invoices.
   - MF: "Do końca 2026 r. odroczony jest obowiązek podawania numeru KSeF faktury podczas płatności…" (https://ksef.podatki.gov.pl/informacje-ogolne-ksef-20/podstawy-prawne-oraz-kluczowe-terminy/).
   - Details on the MF page "numer KSeF i zbiorczy identyfikator" (modified 10 Nov 2026). Source file: `work/research.md` §0.
2. **Who must comply.** Every active Polish VAT payer that pays other VAT payers by transfer. From 1 Jan 2027 the 10,000 zł/month exemption and the cash-register invoice exemption also end, so all B2B invoicers are in KSeF (`work/research.md` §0, §4.7). That covers millions of small firms (JDG), accountants and bookkeepers.
3. **Real search demand (autocomplete-proven, volumes unknown).**
   - 1,158 unique Polish autocomplete suggestions, grouped into 13 clusters. For example, "numer ksef w tytule przelewu od kiedy", "jak sprawdzić czy numer ksef jest poprawny", "identyfikator zbiorczy ksef jak wygenerować", "ksef jdg od kiedy" (188 suggestions in the JDG cluster).
   - Source: `work/seo/keywords.md`. No measured volumes yet: **Yasir can check them with SBMM / Ahrefs (country Poland)**.
4. **Competitor gaps** (`work/research.md` §1–2):
   - ksefnarzedzia.pl (the strongest; 0 Ahrefs traffic per `work/niches/plan.md`) validates **one number at a time**, explicitly **does not validate the IZ**, and has **no transfer title or MPP builder**.
   - ranx.pl has an MPP builder but sits inside a bank-ranking site.
   - czytnikfaktur.com rejects 36-character KSeF 1.0 numbers and shows ads.
   - shipailab and einvoicetool are articles with no tool.
   - **No free client-side IZ validator was found anywhere.** We have one.
   - Our edge: number → payment workflow in one place, bulk + CSV export, auto-detect of number or IZ, specific error hints (e.g. "O instead of 0 at position 23"), and a dated legal-status box.
5. **Timing.** Demand should spike in **Dec 2026 – Jan 2027**. The site launched ~6 weeks before that.

## Risks
- **Free subdomain.** The playbook says subdomains rank worse than a real domain. AdSense acceptance of `*.dpdns.org` is not verified. Moving to `numerksef.pl` early (in the first 1–2 months) costs the least ranking.
- **Domain expiry.** If the DigitalPlat renewal (window ~15 Jul – 12 Nov 2027) is missed, the site goes offline at this address.
- **Crowding.** Several competitors appeared in Oct–Nov 2026, and most have 0 traffic. We may also sit at 0 for months.
- **Legal flux.**
  - The penalties (art. 106ni) were voted by the Sejm on 6 Nov 2026 to move to 1 Jan 2028, but this is **pending in the Senate**.
  - Banks haven't all published KSeF-in-MPP rules.
  - The site deliberately states **no penalty dates or amounts**.
- **Seasonality.** The peak is around the deadline. Afterwards demand should settle into steady "how to" searches, which is evergreen but smaller.
- **Accuracy = trust.** A wrong checksum or date would damage the site. Keep the tests green.
- **Open technical issues (found 13 Nov 2026, not yet fixed):**
  - Some `<lastmod>` values in the live `sitemap.xml` are not in date format (they show "Fri 2026-11-13 2:00 PM PKT (UTC+05:00)"). Fix the `lastmod()` function in `work/build/build.py` to output `YYYY-MM-DD`, then rebuild and push.
  - The live `robots.txt` doesn't block `/_source/`, even though the commit message says it does. Add `Disallow: /_source/`.

## Monetisation path
1. **Months 0–3:** no ads. Grow content and get indexed.
2. **~Month 3 (Feb–Mar 2027)**, only if GSC shows steady organic clicks:
   - Move to a real domain first if possible.
   - Add the policy update + consent banner, then apply to AdSense with `ads.txt` at the root.
3. **After approval:** Auto ads, GDPR consent message, `ads.txt` kept permanently.
4. **Later (optional, own idea, not from the videos):**
   - an embeddable widget for accounting blogs (links back)
   - more Polish accountant tools on the same domain: VAT white-list bulk checker (the MF API allows CORS, tested 13 Nov 2026), limit VAT 2026/2027 page, interest note generator (`work/niches/plan.md` §C.3)

## 12-month plan (Dec 2026 → Nov 2027)

**Every week:**
- Publish 5–7 blog posts from `work/seo/blog-calendar.md` (1 a day in month 1).
- IndexNow every new URL.
- Request Indexing in GSC for 1–3 URLs when the quota allows.

**Every month:**
- Check GSC (clicks, impressions, queries, coverage errors) and Bing.
- Re-check the MF KSeF pages for changes.
- Run the tests before each push.

| Month | Posts / content | Indexing | Links / promo | AdSense / domain / legal |
|---|---|---|---|---|
| **Nov 2026** (rest) | Fix the sitemap lastmod + robots `/_source/`. Start the 30-post calendar (#1–#10). | Retry Request Indexing (home + 6 tools). IndexNow each post. | Yasir creates the FB brand Page. Promo drafts only with per-post approval. | Decide on buying `numerksef.pl` (needs Yasir's OK). |
| **Dec 2026** (peak build-up) | Posts #11–#30, prioritising "od kiedy", MPP and IZ posts. Refresh the legal-status box after the Senate/President act on the penalty bill. | Request indexing for each post. | 2–3 approved forum/FB answers spread over the month. First own-network link only from a site that already ranks (none yet, so skip). | If bought, move the domain now: 301 + GSC Change of Address (see `operations.md`). |
| **Jan 2027** (deadline month) | New posts from real GSC queries. Update FAQs with what banks actually do. | Watch coverage. | Answer real questions in groups (approved). | Note the first GSC clicks honestly. |
| **Feb 2027** | 8–12 posts. Grow the home page toward 2,000 words if it reads well. | — | 1 contextual link per month max. | Prepare the AdSense prerequisites (privacy text, consent banner). |
| **Mar 2027** | 8–12 posts. Consider the VAT white-list bulk checker page. | — | 1 link | **AdSense: apply only if there are steady organic clicks.** If "Low value content": 1 post a day for 30 days, home page 2–3K words, reapply after 30+ days. |
| **Apr–Jun 2027** | 6–10 posts a month. Add accountant tools (limit VAT, interest note) if the data supports them. Update for any MF FAQ/spec changes. | — | 1 link a month | Approval → Auto ads + consent messages. |
| **Jul 2027** | Content refresh of the top 10 pages. | — | 1 link | **DigitalPlat free-renewal window opens ~15 Jul 2027. Renew as soon as it opens** (if still on dpdns.org). |
| **Aug–Oct 2027** | Keep posting. Prepare 2028 content (the penalties start if the law passes). | — | 1 link a month | Check a paid domain's renewal price (if bought ~Nov/Dec 2026, it renews ~Nov/Dec 2027; auto-renew is off, so renew by hand only if the site works). |
| **Nov 2027** | Annual review: keep, grow or drop. | — | — | **Hard deadline: free domain expires 12 Nov 2027.** |

**Whenever the law changes (any month):** update the legal-status date box, the JDG checker logic, the affected FAQ answers and posts, then rebuild, push and IndexNow the changed URLs. Watch for: the Senate/President on penalties (druk 3245), MF FAQ updates, bank MPP specs, new FA schema versions.
