# Niche pipeline

Source: `work/niches/plan.md` (research of 13 Nov 2026), with raw data in `work/niches/raw/` and the Ahrefs notes it lists. Volumes are Ahrefs free-tool buckets per country (estimates). Competitor traffic is from the Ahrefs free Traffic Checker on 13 Nov 2026. SERPs were checked with country-filtered web search, not a VPN. Nothing in this list has been built yet, except the Spanish B2B section that is now being added to the Verifactu site.

**Score (1–10)** = demand + SERP weakness + client-side feasibility + trend, with a heavy penalty for crowding.

## The crowding rule (apply before every new site)
> **If 8 or more dedicated free tools sit on pages 1–2 and most show 0 traffic in the Ahrefs Traffic Checker, skip it as a new domain.** Instead, add the tool to an existing site in the same language, or look for a "boring formula" SERP where PDFs, government pages and blogs dominate and only 1–2 tools exist.

How to run it:
1. Search the exact local keyword.
2. Count the dedicated tool pages on pages 1–2.
3. Put 3 of them into the Traffic Checker.
4. If there are 8 or more tools and most show 0 traffic, stop.

Examples at 0 traffic: verifactuhoy.com, facturaobligatoria.es, factulupa.es, einvoicechecker.com, pagamemoroso.com, efacturaspv.ro, usezivo.com, ksefnarzedzia.pl.

## Ranked list

| # | Niche (market) | Volume (Ahrefs est.) | Why / weakness found | SERP | Score |
|---|---|---|---|---|---|
| 1 | **ES average supplier payment period (PMP) calculator, ICAC method** | "periodo medio de pago a proveedores" >100 Easy; 175 variants | ICAC/BOE PDFs dominate. Only 2 calculators exist: cambiarerp (paste box on an ERP blog) and fube.es (wrong, DSO-style formula). Evergreen, with a seasonal peak in Mar–Jul. | **Easy**, the weakest SERP found | **7** |
| 2 | **HR KPD 2025 code finder + one page per code** (Croatia) | "kpd" >100, "kpd pretraživač" >100, 278 variants | KPD is mandatory on every eRačun line since 1 Jan 2026. KPD 2025 amendments and non-VAT issuers start 1 Jan 2027. Existing tools are single search pages; per-code pages weren't seen (not fully verified). | Medium | **6** |
| 3 | **PL VAT white-list bulk checker** (fits the KSeF site) | "biała lista vat" >10K (mostly navigational) | The official site checks one at a time, nipscan caps at 30, and paid tools gate bulk. The MF API allows CORS (tested 13 Nov 2026). | Medium-hard | **5** as a numerksef section / 3 as a new domain |
| 4 | **PT ATCUD/QR reader + SAF-T viewer** (Portugal) | "atcud" >1K Easy; "saft" >1K (navigational) | About 7 tools, mostly on multi-tool sites. QES on PDF invoices from 1 Jan 2027. | Medium | **5** |
| 5 | **PL VAT limit 2026/2027 + small taxpayer** | "limit vat 2026" >1K Easy; calculators 400–700 | 15+ near-identical calculators. Spike from the 240,000 zł limit (1 Jan 2026), fading in 2027. | Hard-ish | **4** (6 as a numerksef page) |
| 6 | **RO e-Factura XML→PDF viewer** | "transformare xml in pdf" >1K Easy | The official tools are clunky; most third-party tools are server-side. | Medium | **4** |
| 7 | **HR eRačun viewer + HUB3 / OIB** | "oib" >1K; "uplatnica" 700 | 10+ tools each | Hard | **4** (bundle with #2) |
| 8 | **Late-payment interest, multi-language** (ES/IT/FR) | ES/IT >1K | 12+ per language | Hard | **4** (i18n add-on to site 2) |
| 9 | SK e-faktúra 2027 toolkit | >100 each | 10+ vendor lead magnets; mandate 1 Jan 2027 | Hard | **3** |
| 10 | CZ QR platba / SK Pay by square | CZ "qr platba" >1K | qr-platba.cz has 6.1K/mo | Hard | **3** |
| 11 | GR VAT (ΦΠΑ) calculator | >1K Easy | 12+ calculators | Hard | **3** |
| 12 | BE Peppol ID lookup + OGM | "peppol id opzoeken" >1K | 15+ lookups; the peak has passed (mandate 1 Jan 2026) | Hard | **3** |
| 13 | DE ZUGFeRD/XRechnung validator | "zugferd validator" >1K Easy | 15+, mostly server-side KoSIT; browser Schematron is heavy | Hard | **3** |
| 14 | DE Verzugszinsen / PL interest calculator | >10K Easy | Entrenched leaders (zinsen-berechnen.de 217K/mo) | Very hard | **2–3** |
| 15 | ES IBAN / PL PESEL / HR OIB generators | >1K | Banks and established tools | Very hard | **2** |

**Not shortlisted:**
- FR e-invoice directory: the API's CORS is unverified.
- HU "e számla": navigational.
- PL working-days calculator: the SERP wasn't checked.
- Lithuania/Latvia: almost no autocomplete.

**Spain B2B as a whole:** 4/10 as a new domain, **7/10 as a section of the Verifactu site** (`work/niches/plan.md` §A.5).

## Next 3 recommendation (from plan.md §C)
1. **Grow site 2 (Verifactu) into a Spanish "factura electrónica B2B + morosidad" hub.**
   - Lead with the ICAC-exact **PMP calculator**, then the Ley 3/2004 due-date tool, the 4-day status/payment deadline, intereses de demora + 40 €, and "¿cuándo me obliga?" with BOE dates (6 Oct 2027 / 2028 / 2029).
   - *Why:* rising demand to Oct 2027, same audience and language, and it builds one domain instead of two thin ones.
   - **Status: in progress (13 Nov 2026).**
2. **Site 3 (new free domain): Croatian "KPD 2025 + eRačun" hub.**
   - KPD search with indexable per-activity/per-code pages, a 2027 changes table, and an eRačun XML viewer with a HUB3 barcode.
   - *Why:* the hard deadline is 1 Jan 2027 and there is a programmatic long-tail gap.
   - *Caveats:* Croatian CPMs are low. Run the crowding check on per-code pages first. A free domain slot is needed (the DigitalPlat slot is used).
3. **Grow site 1 (KSeF) with Polish accountant tools:** VAT white-list bulk checker, limit VAT 2026/2027, interest note generator.
   - *Why:* same audience, higher-volume queries, and no zero-authority start.
   - *Alternative third new domain:* Portugal ATCUD/QR + SAF-T.

**Lesson behind the order: fewer, deeper sites beat more micro-domains** in EU mandate niches. Start a new domain only for a new country or language, or for an empty SERP.

## Open questions (from research)
- Exact código único format (Orden HAC/1028/2026 anexo I): not extracted. Don't build that tool until it is.
- Whether a Croatian site already has per-code KPD pages: not fully verified.
- Dates for DE/FR/BE/GR/SK/RO/PT come from a secondary source (e-invoicing.org).
- Real volumes: Yasir can confirm the top picks with SBMM or Ahrefs in his own browser.

## Premium-country niches
Source: `work/niches/premium-niches.md` (research of 13 Nov 2026; Ahrefs free buckets = estimates; CPC tiers are judgement, not data). Nothing built, bought or posted.

**Finding:** in US/UK/AU every 2026–2029 regulation calculator checked (car-loan interest VIN check, no tax on overtime, UK eVED, salary-sacrifice cap, MTD, Renters' Rights notices, unfair-dismissal 6 months, AU Payday Super, Div 296, state paid leave, ICHRA) already has 8–17 free tools, and the ones checked sit at **0** organic traffic. They fail the crowding rule. What grows in premium markets is a **programmatic professional hub**: intrysys.com (HVAC + electrical, one page per variant) went ~50 → ~1,050 → ~450 visits/mo in Jul–Nov 2026, 99% US; dealwiseai.com (CRE calculators) has 103/mo, rising, 99% US.

| # | Niche (US unless noted) | Volume (Ahrefs est.) | SERP / crowding | CPC (est.) | Score |
|---|---|---|---|---|---|
| 1 | **HVAC + electrical field-reference hub** (A2L PT charts, superheat, conduit bending/fill) | "r454b pt chart" >1K Easy; long-tail 150–500 each | Generic PT chart crowded; per-variant pages proven to reach #1 | Med-High | **6.5** |
| 2 | **Commercial insurance + CRE worksheet hub** (BI worksheet, coinsurance, TI, percentage rent, CAM) | "business income worksheet" >100 Easy (+30 variants) | BI: PDFs + 2 tools (passes) | High | **5.5** |
| 3 | **401(k) top-heavy / ADP-ACP (+ ICHRA)** | <100 Easy (+13); ICHRA >100 Med | Top-heavy: 2–3 tools (passes) | High | **5** |
| 4 | Form 2210 Schedule AI penalty calculator | <100 Easy | PDFs + ~3 tools (passes) | High | 4.5 |
| 5 | Farm calibration hub (NH3, center pivot) | <100 each | PDFs + 1–3 tools (passes) | Low-Med | 4.5 |
| 6 | Hospice aggregate cap (B2B) | <100 | CMS PDFs + 2 tools | High | 4 |
| 7 | UK iXBRL viewer (software-only filing from 1 Apr 2027) | <100 | official + 5 viewers | Med-High | 4 |
| 8–15 | Davis-Bacon; no tax on overtime (>10K but brands + swarm); 1099-DA; car-loan VIN; UK RRA; UK MTD; AU Payday Super/Div 296; UK eVED/salary sacrifice | — | fail the crowding rule | — | 2–3.5 |

**Top 3 to consider:** #1 (proven growth pattern, Easy >1K head term, new A2L tables needed), #2 (highest CPC; BI-worksheet SERP is PDFs plus insurer-branded worksheet variants nobody covers), #3 (thin SERP, high-CPC B2B audience, Jan–Mar testing season; pair with #4 as one compliance domain). Free .com names (RDAP, 13 Nov 2026): a2lptchart.com, coveragecalcs.com, topheavytest.com, underpaymentcalc.com.

**Rule added for premium markets:** don't build a single "hot regulation" tool on a new domain. Plan 60–150 programmatic long-tail pages for one professional audience.

## Micro-niche gaps (all verticals, English markets)
Source: `work/niches/micro-gaps.md` (research of 13 Nov 2026; Ahrefs free buckets = estimates; CPC tiers are judgement). Nothing built, bought or posted. Raw: `work/niches/raw/micro/`, Ahrefs notes `ahrefs-micro-*` in the web notes folder.

**Finding:** the AI tool swarm now covers hobby, trade, dev and exam niches too. 23 of 26 candidates had 8+ dedicated tools on pages 1–2; all 10 tool sites checked in the Traffic Checker had 0–9 visits/mo (ratedarc, timbermath, chainsawchainsize, agebyserialnumber, layercaliber, getchipload, gradeboundaries.uk, plumbmath, statfile.tools, cutchart). The remaining gaps are data locked in **PDF manuals, door stickers and spec sheets** that nobody has transcribed.

| # | Niche (market) | Volume (Ahrefs est.) | SERP / crowding | CPC (est.) | Score |
|---|---|---|---|---|---|
| 1 | **Welding & cutting machine settings hub** (per-machine MIG door charts, TIG, plasma cut charts), US | "mig welder settings chart" >100 Easy (25 variants); "aluminum tig welding settings chart" >100; per-machine <100 / no data | 1 tool (ratedarc, 0) + PDFs, ManualsLib, forums: **passes** | Med | **6** |
| 2 | **UK grade boundaries hub** (board × subject × year), UK | "aqa a level biology grade boundaries" >1K Easy (44 variants) | PDFs + 8+ pages incl. Save My Exams | Low-Med | **5** |
| 3 | Gas pipe sizing chart, US | >1K Easy (169 variants) | 12+ tools: fails | Med-High | 4 (add to HVAC hub) |
| 4 | Water heater age by serial, US | >100 Med (50 variants; 4 brands >100) | 12+ incl. intrysys: fails | Med-High | 4 (add to HVAC hub) |
| 5 | systemd OnCalendar, US | <100 (67 variants) | 15+ incl. systemd.guru: fails | Med-High | 3.5 |
| 6–26 | Joist span, crosswind, laser/resin/CNC settings, swim converter, seed dates, drip rate, FIT viewer (3); wood movement, regear, EV charge time, prop slip, lye/SAP, quilt backing, rowing split, aquarium stocking, .sav viewer (2.5); dipole, 4K card time, game calculators (2) | mixed | all fail the crowding rule | — | 2–3 |

**Recommendation:** no new standalone micro-niche beats the HVAC hub (6.5). Widen it into one US **trades field-reference hub**: HVAC + gas pipe sizing + water-heater age + welding/plasma machine settings (estimated ~7, judgement). Free .com names (RDAP, 13 Nov 2026): weldsettingschart.com, welderchart.com, weldcharts.com, gaspipechart.com, heaterage.com, gradeboundary.com.

**Rules added:**
- The new "boring formula" signal is a SERP of ManualsLib, PDFs and forum threads with at most 1 tool site. Generic calculators and file viewers are no longer gaps in English.
- When a niche fails the crowding rule but shares an audience with a planned hub, add it to that hub instead of a new domain.

## Demand-first gaps
Source: `work/niches/demand-gaps.md` (research of 13 Nov 2026; Ahrefs free buckets = estimates; SERP checks via country-filtered web search). Nothing built, bought or posted. Raw: `work/niches/raw/demand/` (autocomplete + serp-notes.md), Ahrefs notes `ahrefs-kw-demand-*`, `ahrefs-tc-demand-*`.

**Finding:** starting from demand doesn't avoid the swarm. 28 of 34 new candidates failed the crowding rule. This includes equipment fault codes, NL/SE/JP appliance codes, car-seat expiry (>1K Easy), tire DOT codes, transponder chips, Section 232 HTS, EUDR and CBAM. Nearly every tool site checked gets 0–100 visits/mo. The only clear gap is an untranscribed trade catalogue.

| # | Niche (market) | Volume (Ahrefs est.) | SERP / crowding | Score |
|---|---|---|---|---|
| 1 | **Key blank cross-reference + locksmith hub**, US | "kw1 key blank" >100 Easy; "key blank cross reference" <100 Easy, 68 variants | Ilco PDFs, retailers, paid software; dtlgc 0/mo: **gap** | **5.5** |
| 2 | TPMS relearn by vehicle, US | <100 Easy, 96 variants | vendor PDFs + 2–3 programmatic sites (ownerspecs, scantoolmatch): borderline | 4.5 |
| 3 | Breaker interchangeability, US | <100 Easy, 15 variants | Eaton PDFs + 2 tools + articles | 4 (add to trades hub) |
| 4 | STAAR + Regents conversion hub, US | <100 each (9 / 20 variants) | official PDFs + 3–5 low-traffic tools | 4 |
| 5 | Small-engine age by serial, US | <100 (3 kw) | 2–3 thin tools | 3.5 (add to trades hub) |
| 6–15 | car-seat expiry, ANZSCO→OSCA (watch), outboard serial, garage remotes, Sec 232, tire DOT, paint equivalents, lift fault codes, lubricant equivalents, e-bike codes | mixed | fail or watch | 2.5–3.5 |

**Beats the 7/10 trades hub? No.** Add #3 and #5 to the trades hub. Consider #1 (later with #2) as the only second domain worth building. Free .com names (RDAP 404, 13 Nov 2026): keyblankfinder.com, whatkeyblank.com, keyblankcross.com, tpmsrelearns.com, breakerinterchange.com, staarconversion.com, regentscurve.com, engineagebyserial.com.

**Rules added:**
- 10/10 autocomplete depth no longer means a gap.
- The surviving gap signal is a page 1 of catalogue PDFs, retailers and paid desktop software, with no free web lookup that has traffic.
- Being in a non-English market is no longer a moat on its own.
