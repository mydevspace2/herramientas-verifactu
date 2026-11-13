# Micro-Tool Website Playbook (Compile Future method)

Sources: 6 Compile Future videos (₹4L/month 1h20 build; ₹50 LPA 3h masterclass; 10X traffic / international; DESIGN.md; backlinks HT93qgZ3SAc; AdSense on 80+ sites MdRLRRt9kxg), his prompt pages compilefuture.com/blog/how-to-earn-using-ai/ and compilefuture.com/blog/making-50-lpa-from-my-own-ai-business/, and realonlineruler.com (fetched 2026-11-13). Anything marked **(inferred)** is my reading, not his words.

**Model in one line:** find a small problem → build a one-purpose tool site with AI (Astro + Cloudflare, free hosting) → on-page SEO → rank → AdSense. Aim for 1 site a month (12 a year). He expects about 2–3 of every 10 to work. His first success was his 8th or 9th site.

---

## 1) Idea and keyword research

**Finding ideas**
- **Your own problems first.** Every Google search you make is a possible idea: ask "can I build a better one?" Write each one down in a notes app and research it later. Your job or field gives you ideas nobody else has.
- **Reddit/Quora search:** Google `"is there a tool for" site:reddit.com` (also try `site:quora.com`). Paste long threads into Gemini/Claude and ask it to pull out tool ideas.
- Ask Gemini, Claude or ChatGPT for problems (not website ideas).
- **Pick small problems.** Big problems mean funded competitors. Small ones mean low competition, faster ranking and early motivation (₹500–1,000/month).
- **Don't copy ideas he has shown publicly.** After his online-ruler video, 100+ clone sites appeared. Keep your own ideas private.

**Free tools he uses**
- Ahrefs **Free Keyword Generator** (ahrefs.com/keyword-generator): volume, the Questions tab (for FAQs/blogs), related keywords. Change the country for non-US checks.
- Ahrefs **Free Traffic Checker**: a competitor's monthly organic traffic, its top keywords and countries, and its traffic history.
- Ahrefs **Free Backlink Checker**: a competitor's backlinks or your own.
- Google autocomplete: type the keyword, then a space **after** it and a space **before** it, then try letters a–z. You can also add "how to", "what is" or "what if".
- Google **People Also Ask**: open and close entries to load more questions.
- instantdomainsearch.com for domain availability.
- For international research: **Urban VPN** Chrome extension, the country's Google (e.g. Google Brazil), and Google Translate.

**His thresholds (US volume in the Ahrefs generator)**
- ~100 = easy, ~1,000 = medium, ~10,000 = "a bit tough". Start around 100, then move to 1,000; take 10,000 only once you have experience. He says he "generally sticks to 1,000–10,000". Remember these are US-only numbers; other countries add more.
- **Ignore Ahrefs' KD number for English keywords.** Judge difficulty yourself from the SERP:
  - Top-ranking domains **don't contain the keyword** (or only half of it) = good sign.
  - Top results are big multi-tool sites rather than dedicated sites = good sign.
  - **Reddit/Quora threads, Play Store links, PDFs, blogs, a government site or other irrelevant results on pages 1–4** = "golden keyword", because Google has nothing good to show. Reddit on page 1–2 is easy; on page 3 it is harder.
  - vercel.app or other subdomain sites ranking = weak competition.
- **Competitor audit:** open each top site and note bugs, missing features (dark mode, device list, calibration, filters), a bad mobile layout and ugly UI. Your site must fix all of them.
- **Competitor traffic check:** paste the competitor URL into the Traffic Checker. Look at monthly traffic, its trend (fontdetector.org grew from 3.8K in Mar 2025 to about 51K/month), which keywords drive it and which countries.
- **Pick the keyword people actually use**, not your own wording. He searched "online scale" but every site said "online ruler". Use the main keyword the top results share.
- **Feature/page expansion from keyword variants:** e.g. font finder by image / URL / PDF / GIF each get their own page.
- **Target the US by default** for high CPM.

**International / other-language method**
1. Take your proven English keyword (e.g. "online ruler").
2. Translate it with Google Translate (→ "régua online").
3. In the Ahrefs Keyword Generator, select the target country (Brazil) and compare with the US. "online ruler" in the US was 1K+ and Hard; "régua online" in Brazil was 1K+ and **Easy**.
4. Turn on the VPN for that country, open the local Google, and search the translated keyword to see the real SERP. The VPN must be off again before you deploy.
5. Put the #1 local site into the Traffic Checker to find what locals **actually** type. Machine translation is often wrong (pt-BR nuance). Example: he found "régua tamanho real" (1K+, Easy) with the exact .com available.
6. Use the competitor's ranking keywords as supporting keywords; translate each one back to English to confirm it is relevant.

**Dedicated site vs i18n (his rule of thumb)**
- **1,000+ monthly searches and low difficulty in one language/country → build a dedicated single-language micro-niche site** on its own domain. Hyper-focused sites outrank translated sections: the dedicated Portuguese site ranked #1 above an English site's /pt/ folder.
- **About 100 to under 1,000 → add multi-language (i18n) to your existing English site** to collect traffic from many countries. fontdetector.org ranks almost only on non-English keywords this way, and he says this can multiply traffic 4–10×.

---

## 2) Domain naming and buying

- **.com only.** Cheap .xyz-type domains he bought early "didn't rank". Subdomains (pages.dev, workers.dev, vercel.app, netlify.app) don't rank either.
- **The main keyword must be in the domain** (exact or partial match). If .com is taken, add a word before or after it from autocomplete: real / free / accurate / AI. For example, realonlineruler.com was free when onlineruler.com was taken, and fontfinderai.com when AI Font Finder was taken.
  - Avoid modifiers that narrow the scope (e.g. "inches").
  - Prefer the shorter option.
  - Keep the higher-volume keyword (finder over detector).
  - Avoid hyphens (stated on his blog).
- **ccTLDs** (.com.br, .in) rank faster for a single country but often need a local ID or tax number. Workaround: use a **.com spelled in the target-language keyword** (reguatamanhoreal.com).
- **Buy the domain last**, after the code works. He bought domains before for ideas he never built.
- **Buy 1 year only.** Ignore "₹1" offers that lock you into a 3-year plan. Remove add-ons and **turn auto-renew off**. Renew only if the site is working after a year.
- **Registrars**
  - **Spaceship:** his current pick. Cheapest, and debit cards usually work. Free WHOIS privacy. Renewal $9.98.
  - **Namecheap:** needs a credit card. Free privacy. Renewal $14.98.
  - **Hostinger:** takes UPI. Free privacy.
  - **GoDaddy / BigRock:** take UPI, but privacy costs extra (about ₹500–600).
  - Compare the **final price including tax and the renewal price** every time. Move domains to wherever is cheapest.
- **Promo:** Spaceship code **COM67** (he also says "COOM67" in the 3h video). It brought a .com from $8.88 to about **$3.62 (₹360–374)**. If it has expired, check Spaceship's deals page.
- A normal price is about ₹1,000/year. Don't let that cost stop you; it is the only unavoidable expense.

---

## 3) Build stack and workflow

**Stack**
- **Astro.js:** server-first MPA, sends zero JS by default, fastest, SEO-friendly. He also notes Cloudflare acquired Astro.
- **Not React/Next SPAs.** Bots see an empty root div and the JS load is heavy. Use Next only for dashboard-heavy apps (deployed on Vercel).
- **Tailwind CSS v4.**
- **Cloudflare Pages** for static sites (about 99% of tools): free, unlimited traffic.
- **Cloudflare Workers** for dynamic sites (image upload, APIs): 100k requests/day free, $5/month paid. Workers AI gives 10,000 neurons/day free, which he used for Font Finder.
- He rejects **Vercel/Netlify:** 100 GB/month (about 50k page views) and the site goes offline when you hit it. Vercel's free tier is for personal use only.
- Keep the site **static** wherever possible. Avoid ideas that need paid APIs.

**Install once:** Git, Node.js, VS Code (or Antigravity or Zed), and an AI agent. He uses Claude Code. Free alternatives: Antigravity, OpenCode, Gemini CLI, Cursor free tier, Kilo Code, Codex. Free offers change, so check his "Code with AI" playlist.

**Project setup (every site)**
1. Create a folder named after the planned domain. In the terminal, `cd` into it and run `npm create astro@latest .`. Choose the Basic template and **Yes** to initialise Git.
2. Open it in VS Code or Antigravity (`code .` / `agy ide .`) and install the **Astro extension**.
3. Install skills (from skills.sh), choosing **Project** scope and symlink:
   - **tailwind-4-docs** (Lombiq), because agents mix up Tailwind v3 and v4.
   - **web-design-guidelines** (Vercel). He used this in the first video, then dropped it once he used DESIGN.md.
4. **Astro Docs MCP:** add it to the agent (command from docs.astro.build/en/guides/build-with-ai/). For agents without a command, paste the MCP text to the agent.
5. **DESIGN.md** in the project root (colours, typography, spacing, components). This stops "AI slop" gradients, gives consistent pages and saves tokens.
   - Vercel's: `npx getdesign@latest add vercel` (getdesign.md).
   - His newer favourite is **"Open DESIGN.md"**: Google "open design md", click "Search instead for open design md", take the first result. It has about 1,000–1,200 free DESIGN.md files with screenshots, a copy button and a one-line install command. (Exact URL not verified.)
   - To choose one: give the agent the site's **JSON index URL**: *"I want to make an [expense tracker], choose top three DESIGN.mds from [JSON index URL]"*. Check each pick's screenshots or "Visit site" before installing.
   - He liked Arc, Sentry, Apple, Stripe and Wise; the agent suggested finance brands for a finance app.
   - Existing site: *"redesign my whole project according to this DESIGN.md"*.

**Prompts he publishes (verbatim)**

Website creation (use plan mode, Shift+Tab, in Claude Code):
```
I have initialized a new astrojs project, use astro docs mcp and tailwind-4-docs skill for creating the website. Also use @DESIGN.md file for the website design.

Name: [Site Name]
Domain: [domain.com]

Website Description:
[What the tool does + must-have features]

My competitor website is [competitor URL] and it have some features which we need and we need to make a website better than it. Give me ideas how to make it better. go on to this website and check what exactly we need to make. Do not copy design or ui from that website.
```
Also tell it to make the site an **MPA, not an SPA**, and to give each feature variant its own page.

SEO:
```
Do the On Page SEO of this Website for

Main Keyword: [main keyword]
Supporting Keywords: [relevant Ahrefs/autocomplete keywords]

these above keywords, also use proper og meta tags for SEO
on home page write 800 - 1200 words about the tool for SEO
```
(This was 600 words in the first video.)

FAQ:
```
add seo friendly FAQ section for these below questions:
[one question per line from Ahrefs Questions + People Also Ask]

NOTE: Use JSON-LD for FAQ SEO
example: <script type="application/ld+json"> {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[...]} </script>
```

Other one-liners he uses:
- Pages for AdSense: generate Privacy Policy, About Us, Terms & Conditions and Contact Us, plus *"This website should be MPA multi-page application for best SEO. Make these pages visible in the home page of the website."* If the links only sit in the footer, also ask: "Add these links in the hero section too".
- "add error pages" (both 404 and 500).
- "create sitemap.xml for this website, use the Astro Docs MCP to check how to add it", then "add robots and add a sitemap link to it".
- "Add dark mode to this website with a toggle".
- "the website is not mobile responsive" / "make the website mobile responsive".
- Favicon: "I have added all the favicon images in the public directory, please add this code for favicon support".
- Logo: "use this SVG icon as the logo of the website, the favicon is already done, do not touch it". Use SVG so the logo turns white in dark mode.
- Analytics: "add this Google Analytics code in this website".
- Static or dynamic? "this website is static or not? and should i deploy it in cloudflare pages or workers ?"
- Single-language conversion:
  ```
  this is my english website, convert this full website to rank on "[kw]" and domain : [domain], we want to rank in [country] and every [language] countries.
  Add hreflang markup of [Language].
  NOTE: Do not just give a /lang pages, convert this whole website to a [language] website only. we only want [language] language no other languages.
  Change the full content of this website to rank on main keyword: [kw]
  Supportive keywords: [list]
  ```
- Multi-language:
  ```
  https://docs.astro.build/en/recipes/i18n/  use this to provide multi lang support to this website so that it ranks on other languages keywords.
  provide support for: Español, 日本語, Français, Deutsch, Português, 한국어, Italiano
  note: Add hreflang markup for each language.
  ```
  (In the video he also asks for SEO and meta tags per language and a `lang` attribute per route.)

**Working habits**
- Start a fresh session (`/clear` or `/new`) for every new task; long sessions burn tokens. Stay in the same session only for small follow-ups.
- **Commit before every prompt** (Source Control: stage, write a message, commit). If the AI does something wrong, use Discard/revert instead of spending tokens to undo it.
- GitHub backup is optional: `gh auth login`, private repo, Sync Changes.
- For a language clone: copy the English project into a new folder and **delete `.wrangler`** (old deploy cache).
- **Build and test in English first**, then localise, because you can't test a tool in a language you don't read.

**Testing**
- `npm run dev` and click through every feature yourself.
- Check mobile in Chrome DevTools (Toggle device, e.g. iPhone 14 Pro Max). Google and AdSense penalise non-responsive sites.
- Test dark and light modes.
- The sitemap only exists after `npm run build` then `npm run preview`.
- The agent self-tests in a browser and fixes bugs.
- Keep iterating until the site is clearly better than every first-page competitor.

**Favicon:** logofa.st (pick an icon, radius about 60, padding 0, no shadow) → realfavicongenerator.net (full and short name) → put the files in `/public` and give the agent the HTML snippet.

---

## 4) On-page SEO checklist

- [ ] One focused tool per site (micro-niche); the main keyword is in the domain.
- [ ] Title and meta description contain the main keyword. His blog says the meta description should be under 160 characters (blog only, not said in the videos).
- [ ] Open Graph tags (title, description, image, URL, type).
- [ ] **Tool above the fold**, then long helpful text on the home page:
  - 600 words (first checklist) → 800–1,200 (3h video) → **2,000–3,000** if AdSense says "Low value content".
  - It must be genuinely useful: real detail and examples, not padding.
- [ ] Use supporting keywords from Ahrefs and autocomplete. Exclude irrelevant ones and other brands' names (WhatTheFont, Canva, Adobe); wrong keywords can hurt ranking.
- [ ] FAQ section from Ahrefs Questions and People Also Ask, with **FAQPage JSON-LD**. No duplicate questions; keep the highest-volume version.
- [ ] MPA: every page is a full HTML page; a separate page for each feature or keyword variant.
- [ ] International: `hreflang` alternates for every language, the correct `<html lang>` per route, and localised meta. Single-language sites put the language on the root (no /pt/). Sitemap with `xhtml:link` alternates.
- [ ] Mobile responsive, dark mode, clear navigation (AdSense flags poor navigation).
- [ ] Favicon and logo (the favicon shows in Google about 7 days later; don't fiddle with it).
- [ ] Policy pages (Privacy, Terms, About, Contact) linked visibly from the home page.
- [ ] Custom 404 and 500 pages.
- [ ] robots.txt pointing to sitemap.xml.
- [ ] Speed comes from Astro (zero JS) plus the Cloudflare CDN.
- [ ] Internal links between blog posts and the tool; the agent interlinks them.
- [ ] Image alt text and clean URLs (his blog only).
- [ ] Optional /blog with long-tail posts (see section 7).

**realonlineruler.com structure (observed 2026-11-13)**
- Title: "Online Ruler — Free Accurate Ruler in cm, mm & Inches | RealOnlineRuler". The meta description contains the keyword, inches, cm, mm, actual size and "no download".
- **Above the fold:** the working tool only.
  - Toolbar: units cm/in/px, Calibrate, How to Use.
  - Edge picker: Left, Right, Top, Bottom.
  - A calibration status badge ("Not calibrated…") with "Wrong device? select your model".
  - Footer links already visible: Blog · About · Contact · Privacy Policy · Terms.
- **Calibration modal** with 4 methods: Auto-detect, Device (list of 370 devices), Diagonal, Card (85.60 × 53.98 mm).
- **Guide panel:** steps plus keyboard shortcuts (G guides, C crosshair, F fullscreen, Esc clear, 1/2/3 units, D dark mode, H toggle guide).
- **Single H1 below the tool:** "Free Online Ruler: Measure Actual Size in cm, mm and Inches". Then H2 sections:
  - Quick start
  - Why most online rulers show the wrong size (table)
  - Choosing a calibration method (table)
  - How to read the ruler (cm, inch fractions table, pixels, readout)
  - Tips for accuracy
  - Check calibration with everyday objects (table)
  - What you can measure (ring-size table, screws, jewellery, documents, design)
  - Know the limits
  - cm/inch conversions
  - FAQ (10 questions)
- **About 2,500–3,000 words** of guide text (inferred from about 17.7k characters of page text) and **5 tables**.
- **Links:**
  - Internal links to 2 blog posts (how to use an online ruler; ruler in PowerPoint Online). Those are long-tail blog keywords.
  - One contextual link to his other site, anchor "font finder" → fontfinderai.com. This is the own-network backlink from the backlinks video.
- **Footer:** Blog, About, Contact, Privacy Policy, Terms & Conditions, © line.

---

## 5) Deploy and technical SEO

1. **Cloudflare account**, then in the project terminal run `npx wrangler login` and authorise in the browser. If wrangler fails: `npm install wrangler@latest --save-dev`.
2. **Deploy prompt:**
   - Pages: `I have already loggedin to cloudflare wrangler, now deploy this astrojs website to cloudflare pages and take info from astro docs mcp if needed. Also add deploy script to package.json`
   - Workers: the same prompt with "cloudflare workers".
   - After that, every update is: commit → (sync to GitHub) → `npm run deploy`.
3. **Test on the temporary `*.pages.dev` / `*.workers.dev` URL**, including on your phone, before buying the domain.
4. **Buy the domain, then add it to Cloudflare:**
   - Domains → Overview → Add/Connect a domain → **Free plan** → Continue to Activation.
   - Copy the 2 Cloudflare nameservers into the registrar (Spaceship: Nameservers & DNS → Custom).
   - Click "I updated my nameservers" / "Check nameservers". It is usually active in 10 seconds to 10 minutes; it can take up to 48 hours, mostly for old domains.
   - In the first video he deleted the default DNS records and added a placeholder A record `@` → `8.8.8.8` before activation. For Workers, delete the existing A/CNAME records if Cloudflare complains.
   - If the Cloudflare dashboard hangs, try a browser or Chrome profile with no extensions.
5. **Custom domain:** Workers & Pages → project → Custom domains → Set up → enter the root domain → Activate. HTTPS/SSL is free.
6. **www → root 301 (his current method; replaces his older advice of adding www as a second custom domain):**
   - Add **only the apex domain** under Custom Domains.
   - Domain → Rules → Overview (or Templates) → **"Redirect www to root"** → Create rule from template → keep **Preserve query string** on → Deploy. You can also build it manually in Redirect Rules.
   - DNS → Records → Add record: **Type AAAA, Name `www`, IPv6 `100::`, Proxy ON (orange cloud)** → Save. The redirect only fires with this proxied record.
7. **Stop the duplicate content on the preview domain:**
   - **Pages:** create `public/_headers` containing:
     ```
     https://[project].pages.dev/*
       X-Robots-Tag: noindex
     ```
     Use your **base** pages.dev name, not the versioned hash URL. Keep the two-space indent before `X-Robots-Tag`. Then run `npm run deploy` and check in DevTools → Network that the noindex header appears on pages.dev and **not** on the .com. He says one of his sites failed because of exactly this.
   - **Workers:** after the custom domain is connected, Settings → Domains → **turn off the workers.dev (and preview) URLs**. Do not use `_headers` for Workers.
8. **robots.txt and sitemap.** Check `/robots.txt`. Astro generates `sitemap-index.xml` and `sitemap-0.xml`; check both after a build. Cloudflare may append its own AI-bot rules to robots.txt.
9. **Google Search Console:**
   - Add a **Domain** property (no https) and choose "Any DNS provider".
   - Add a TXT record in Cloudflare DNS with Name `@` and the verification string. Wait about 5–10 seconds, then Verify.
   - Sitemaps: submit the sitemap-index URL (he also submits sitemap-0).
   - URL Inspection on `https://domain.com` → **Request Indexing**. Repeat for any new or updated page, including each blog post.
   - Data appears after about 2 days.
10. **Bing Webmaster Tools:** sign in with Google → **Import from GSC** → URL Inspection/Submission → request indexing → submit the sitemap(s). Errors there are common; treat Bing as a backup.
11. **Google Analytics 4:**
   - Admin → Create Property → Web stream for the domain.
   - Install manually: copy the tag and give it to the agent with "add this Google Analytics code in this website", then deploy.
   - Use Test installation → Confirm.
   - Use GA for total and real-time users and countries; use GSC for Google clicks and positions.
12. **Free email (optional, on his 3h checklist):** Cloudflare → Compute → Email Service → Email Routing → onboard the domain → Activate (it sets up MX, SPF and DKIM).
   - Destination address: your Gmail (verify it).
   - Routing rules, e.g. `hello@domain` → Gmail. This is receive-only; check spam.
13. **AdSense ads.txt fix ("ads.txt not found") in Cloudflare:**
   - Caching → Cache Rules → Create: Custom, **URI Path equals `/ads.txt`** → **Bypass cache** → Deploy.
   - Security → Security Rules → Create: URI Path equals `/ads.txt` → action **Skip** → tick all boxes → place **First** → Active → Deploy.
   - Then click Update in AdSense.

---

## 6) Traffic, backlinks and promotion

**Backlink basics (as he explains them)**
- **Dofollow** links are the only kind that pass ranking. **Nofollow / sponsored / ugc** links only send traffic. `rel="noopener"` is a security attribute and still counts as dofollow.
- **Contextual** links in the main content are best. Header, footer and sidebar links count for less because they repeat on every page.
- Backlinks also make **indexing faster**, which is his fix for "my site isn't getting indexed".
- Check backlinks with Ahrefs Backlink Checker (your site or a competitor's), then right-click → Inspect each link's `rel`. Directory links are automatic and low value.

**His own-site network (main tactic, free)**
- Link your own **related** tools to each other, contextually, dofollow, with the **target keyword as anchor text**. He changed "AI Font Finder" to "Font Finder" because "font finder" was the keyword he wanted.
- **Wait about 1 month after a site launches** before linking to it. Then add **no more than 1 new backlink per site per month**, so the profile looks natural. Adding about 12 at once is link spam, and his rankings dropped when he did it.
- Prompt: `Give a backlink to https://[site]. It should be in the main content of the site, and it should be a dofollow backlink.`
- Link from a site that already ranks and gets users to the site you want to push. Example: Real Online Ruler (#2 for "online ruler") linked to Font Finder AI, which had an average position of about 9.7 for "font finder".
- With this trick he says ranking time drops from about a year to **2–4 months**.

**Other link sources**
- **Organic:** a genuinely good tool earns links by itself. Most of Real Online Ruler's links were organic.
- **Social profiles:** Instagram, YouTube, X, Threads and Telegram for the tool, each with the site link in the bio. A small boost plus awareness.
- **Paid links:** he doesn't buy them and doesn't recommend it, though he says they work if you have money.
- **Link swaps:** they rarely work; most owners ask for money.
- Bad or spammy links can hurt you ("double-edged sword").

**Promotion:** post on Reddit ("I made this, please try it"), Quora and your socials, and share with friends. This gives reach and a "genuine" signal. Don't count friend traffic as organic for AdSense.

**Extra traffic:** add i18n or language clones (section 1) and a long-tail blog (section 7).

---

## 7) Monetisation

**His numbers**
- About **₹4 lakh/month from AdSense alone**, from **80+ micro-tool sites**. He had 30+ AdSense approvals by the first video.
- Real Online Ruler (built June):
  - About 400K impressions and 21–22K clicks.
  - About 800 users/day.
  - Ahrefs estimate about 7.5K/month.
  - Ranked #2 for "online ruler" within about 1–1.5 months.
  - He hasn't put ads on it.
- "régua online" #1 site: about 2.2K traffic from that keyword. fontdetector.org: about 51K/month.
- **His projection:**
  - Even 1–2 working sites at ₹5–10k/month → reinvest → 5 sites/month → about 60 a year.
  - If 12 of those work at about ₹10k each, that is about **₹1.2 lakh/month** within 1–2 years.
  - Growth goes ₹10k → ₹50k → ₹1L → ₹4L once sites rank.
- His blog FAQ (not the videos): 1,000 daily US visitors ≈ ₹10k–50k/month; 10–15 working tools → ₹1–4 lakh/month.

**AdSense timing (his statements vary by video; the strictest is his own rule)**
- **Never apply in month 1.** He got "Low value content" when he applied straight after launch.
- Video 1: apply at **about 10 daily users**, usually after 4–5 months, or sooner if it happens within 10–15 days.
- 3h video: wait **at least 1–2 months** and **2–10 organic clicks/day in GSC**; at least 100–200 users/day is needed to earn anything meaningful.
- **His personal rule (AdSense video):** first application after **3 months**, at about **1,000 users/day**. He has also seen 10–15 users/day get approved.
- **"Chase traffic, not AdSense."** Approval with no traffic earns nothing.

**Requirements**
- Privacy, Terms, About and Contact pages, visibly linked.
- Good UI and navigation, mobile-friendly, original useful content.
- The domain is not brand new: domain age is a trust factor. Unchanged sites have been approved simply by reapplying after 3 months.
- Not every page needs to be indexed, only the main high-traffic page.
- **No other ad networks on the site while applying**, and no AdSense ads before approval.

**Applying**
- adsense.google.com → Sites → New site (no https).
- Verify with **ads.txt**: create `public/ads.txt` with the exact snippet, keep it there permanently, deploy, then tick "I have published" → Verify → Request review.
- The alternative is the head script ("add this AdSense script to header").
- Reviews take **2–4 weeks**, sometimes 1–2 months. "Getting ready" for 15–20 days is normal.

**"Low value content" fix**
- Add **/blog** with 10–20 (up to 30) posts on **long-tail keywords** in your niche, e.g. "how to format JSON in VS Code" rather than "JSON formatter". Find them in the Ahrefs Questions tab, with Google "kw how to / what is / what if", and in People Also Ask.
- Publish **1 post per day**, not all at once, and request indexing in GSC for each one.
- Grow the home page to **2,000–3,000 words** plus FAQs.
- **Reapply only after about 30 days.** Rapid reapplying can trigger a 30–60 day block.
- If it is still rejected, keep working and reapply after 3–4 months.
- Prompts:
  - `Add a blog section to my website at /blog and write one blog on the topic of [title]`
  - `I just got the Low value content error on AdSense. So make the home page content 2,000 to 3,000 words and make it valuable to the users, so that I don't get this error again. The content should be of high quality.`
  - Daily: `Create one more blog post with high value and rich content, with high quality (I got the Low value content error in AdSense) on [keyword]`
- To reapply: Sites → the site → tick "I confirm" → Request review.

**After approval**
- Ads → By site → copy the full Auto Ads code → tell the agent "This is my Auto Ads AdSense code, please implement it" → deploy.
- Turn on **Auto ads + auto-optimise** and leave the rest at defaults. He doesn't place ads manually.
- **Privacy & messaging:** create both the **European (GDPR)** and **US** consent messages. Select the site, add the site name and logo (favicon), turn off "Do not consent", then publish. He says ads won't run properly without them.
- Ad-blocking recovery message is optional.

**Account rules**
- **One AdSense account per person**, for all sites and YouTube. A registered company can hold a separate one.
- A banned account can't be replaced.
- Use a personal email with 2FA (PAN is verified on it).
- Payout happens at **$100**.

**Alternatives** (only if AdSense is impossible after about a year): Media.net (premium), Ezoic, Adsterra (pays little), Monetag. These need decent traffic too. His advice is to prefer AdSense for the first year.

**Affiliate:** he gives no affiliate method for the tool sites. The only affiliate links he mentions are his own registrar links (Spaceship/Namecheap) on his channel's blog. Any affiliate add-on would be your own idea, not his method.

---

## 8) Mistakes to avoid and timelines

**Mistakes he names**
- AI-slop design (gradients). Fix: a DESIGN.md plus design skills.
- Cheap TLDs (.xyz) or subdomains; buying the domain before building; multi-year domain deals.
- React/Next SPAs for tool sites; Vercel/Netlify limits causing downtime ("one outage hurts rankings"); cheap ₹60 hosting.
- Leaving pages.dev/workers.dev indexable. A site of his failed from this duplicate content.
- Irrelevant or brand keywords in the SEO prompt.
- Going after big problems; one giant site. His big sites failed.
- Long AI sessions (token waste); not committing before prompts.
- Many backlinks at once, spammy links, or linking unrelated sites.
- Applying to AdSense too early, reapplying repeatedly, other ad networks during review, or ads before approval. Not setting up GDPR/US consent.
- Sharing your winning ideas publicly.
- Quitting after the first failure. His success came at site 8–9.
- Messing with the favicon in Google. Wait about 7 days.

**Timelines (his numbers)**
- Build: 1 day to 1 week with AI (blog says 3–5 days). One site a month is enough.
- Ranking:
  - Generally **6 months to 1 year**; "his sites usually rank within about 4 months (4–6)".
  - Easy keywords: 1–2 months, occasionally 1–2 days.
  - Medium (online ruler, with experience): 1–1.5 months to the top 2–3.
  - Hard (10K-volume keywords): up to 2 years.
  - International SEO: 3–6 months.
  - The own-network backlink trick: 2–4 months instead of about a year.
- Keep every site live **for at least 6 months to 1 year**; the paid domain year forces this.
- AdSense: reviews take 2–4 weeks to 2 months; reapply 30 days or more after a rejection; domain-age approvals come after 3–4 months.
- Commitment: give it **1–2 years**.

---

## 9) Apply-to-next-site checklist

1. Write down a small problem you hit yourself, or one from `"is there a tool for" site:reddit.com`.
2. Search it on Google and find the main keyword the top sites actually use.
3. Check US volume in the Ahrefs Keyword Generator. Aim for about 100–1,000 for early sites (up to 10K once experienced).
4. Read the SERP pages 1–4. Go ahead if you see Reddit/Quora/PDF/Play Store results, sites without the keyword in their domain, or weak subdomain sites.
5. Run each competitor through the Ahrefs Traffic Checker (traffic, trend, keywords, countries) and list every flaw or missing feature.
6. Check the same keyword translated for other countries (VPN + local Google + Ahrefs country). 1K+ and Easy means a dedicated site; 100–1K means plan i18n.
7. Find an available **.com** with the keyword (try autocomplete words before and after it). Don't buy it yet.
8. Create the folder and run `npm create astro@latest .` (Basic, Git yes). Open it in VS Code or Antigravity and add the Astro extension.
9. Install the tailwind-4-docs skill and the Astro Docs MCP, and add a DESIGN.md (getdesign / Open DESIGN.md).
10. Run the website-creation prompt in plan mode with the competitor URL. Ask for an MPA and separate pages for feature variants.
11. Test every feature, mobile view and dark mode, and fix issues one by one in fresh sessions. Commit before every prompt.
12. Make the logo and favicon (logofa.st → realfavicongenerator) and add the SVG logo.
13. Run the SEO prompt with the main and supporting keywords (no brands or irrelevant terms), OG tags, and 800–1,200 words of home content.
14. Run the FAQ prompt with Ahrefs Questions + People Also Ask and FAQPage JSON-LD.
15. Add Privacy, Terms, About and Contact pages, linked from the hero and footer, plus 404 and 500 pages.
16. Confirm robots.txt and sitemap (`npm run build && npm run preview`).
17. Ask the agent whether the site is static or dynamic, run `npx wrangler login`, and use the Pages or Workers deploy prompt (with a deploy script). Test on pages.dev.
18. Buy the .com for 1 year at the cheapest registrar after tax (Spaceship + promo code), then turn off auto-renew.
19. Add the domain to Cloudflare (Free plan), switch nameservers and attach it as a custom domain (apex only).
20. Add the www→root 301 template (preserve query string) and a proxied AAAA `www` → `100::` record.
21. Pages: add `public/_headers` with `X-Robots-Tag: noindex` for `https://[project].pages.dev/*` and deploy. Workers: disable the workers.dev URLs. Verify the headers.
22. Optional: set up Cloudflare Email Routing (hello@ → Gmail).
23. Add GA4 through the agent, deploy, and run Test installation.
24. GSC: verify the Domain property with a TXT record, submit the sitemap(s), and Request Indexing on the homepage.
25. Bing Webmaster: import from GSC, submit the URL and sitemap.
26. Share it on Reddit, Quora and socials, and create social profiles with the site link.
27. After about 1 month, add one contextual, dofollow, keyword-anchored link to it from a related site of yours that already ranks. Then add no more than 1 new link per site per month.
28. Prepare AdSense: add the Cloudflare cache-bypass and security-skip rules for `/ads.txt`. Apply only after at least 1 month and steady organic traffic (his own rule: about 3 months). Verify with ads.txt and keep that file permanently.
29. If you get "Low value content": publish 1 long-tail blog post a day for about 30 days (index each one), grow the home page to 2,000–3,000 words, and reapply after 30 days (or wait 3–4 months).
30. Once approved: turn on Auto ads + auto-optimise, publish the GDPR and US consent messages, then repeat with the next site (or a language clone/i18n of a winner).
