# AI handover: Herramientas Verifactu (Spanish invoicing tools)

Live site: https://mydevspace2.github.io/herramientas-verifactu/
Owner: Yasir Ali (GitHub mydevspace2). Everything here belongs to the owner and runs free on GitHub Pages, with or without any AI subscription.

## What this site is
Free Spanish tools: Verifactu QR generator/validator, huella (SHA-256), XML example, B2B e-invoicing obligation checker (2027/2028), periodo medio de pago calculator, late-payment interest calculator, guides. Language: Spanish.

Other sites by the same owner, built the same way: mydevspace2/numer-ksef, mydevspace2/herramientas-verifactu, mydevspace2/trade-charts.

## Rules (always follow)
- Zero budget. Never buy anything (domains, tools, ads) without the owner's explicit "yes".
- Never post anywhere outside this site (Facebook, forums, Reddit) without the owner's OK for that exact post. Drafts live in `_source/docs/` or `_source/seo/promo-drafts.md`.
- Never invent data: every figure, date, legal rule, chart value or rate must come from a cited official or published source. If it can't be verified, leave it out.
- Run every test in `_source/qa/` before pushing. Push only when all pass.
- Never put passwords or tokens in this repo. Logins belong to the owner.
- Keep the Google `google-site-verification` meta tag on the home page (build with `VF_GSV` set to the token in `_source/docs/project-notes.md`, or the tag disappears).

## How to continue with any AI (ChatGPT, Claude, Gemini, Cursor, Copilot)
1. Give the AI this file, `README.md`, and the notes in `_source/docs/` (start with `project-notes.md` if present, then `knowledge-base/README.md`).
2. Paste the daily routine below as your request.
3. The AI edits files in `_source/build/`, rebuilds, runs `_source/qa/`, and copies the output to the repo root. Then commit and push to `main`. GitHub Pages publishes in 1–2 minutes.
4. With no coding tool: open a file on github.com, tap the pencil, paste the AI's edited version, then commit.

## Daily routine (paste to the AI)
Publish 2–3 new Spanish posts from `_source/docs/seo/blog-calendar.md`, B2B e-invoicing and morosidad first (900–1,400 words, FAQ, link to the matching tool, BOE/AEAT sources only; always separate 'in the BOE' from 'only announced'). One SEO fix. Add new URLs to the sitemap. Run all tests, then push.

## Weekly / yearly
- Mondays: Google Search Console (search.google.com/search-console, account topelitemindset1@gmail.com) and Bing Webmaster. Check coverage errors, sitemap status and top queries. Rewrite titles of pages with impressions but low CTR.
- After each new page: Search Console → URL Inspection → Request Indexing (a few a day; quota is limited).
- ~30 Dec and ~30 Jun: add the new interés de demora rate from the BOE.
- When the Verifactu 2028 delay is published in the BOE, update all dates.
- Domain verifactuya.com is planned (branch `domain-verifactuya`). Buy only with the owner's yes, then merge that branch.

## Where things are
- `_source/build/`: site generator (Python). `_source/qa/`: tests.
- `_source/docs/` (and `_source/seo/`): blog calendar, keywords, research, project notes, SEO knowledge base and playbook.
- Repo root: the published site (HTML, sitemap.xml, robots.txt).
