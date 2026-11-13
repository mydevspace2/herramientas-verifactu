# Verifactu micro-tool site — research (2026-11-13)

Owner: Yasir. Planned as a Spanish-only static site (GitHub Pages, client-side JS only), following the method in `work/tool-site-playbook.md`.
Status: research only. Nothing built, bought or posted.

---

## 0. Verdict first (read this before building)

**This niche is already crowded with exactly the site we would build.** At least 12 independent sites already offer free, in-browser Verifactu tools: QR generator and validator, QR reader from photo or PDF, huella calculator and chain checker, XSD validator, and "¿estoy obligado?" tests. Several of them reproduce the three official AEAT hash examples, run AdSense, and cite the BOE. The strongest, **factulupa.es**, is essentially our full planned site, already live.

Demand is also weak where tools would fit, and it is shrinking:
- Ahrefs (Spain) puts the tool keywords at **<100/mo**: "qr verifactu" >100, every QR variant <100, "huella verifactu" no data at all, "verifactu excel" <100.
- The real volume is in **informational/news** queries ("verifactu" >10K, "que es verifactu", "verifactu es obligatorio", "cuando entra en vigor", "verifactu 2028" all >1K). Those results are dominated by the AEAT, national media (El Mundo, eldiario.es, Público) and software vendors.
- On 05/10/2026 Hacienda announced it **intends to postpone all pending obligations to October 2028** (not yet in the BOE; see §3.5). Urgency, and so search interest, will probably fall through 2027.
- Ahrefs' free traffic checker shows **0 organic traffic** for every dedicated Verifactu tool site checked (factulupa.es, recibeo.com, verifactu.co, verifactuhoy.com, lectorqrverifactu.com, facturaenregla.com, kiwop's calculator URL). These are estimates, but they suggest tool pages in this niche earn little even when they rank.

By the playbook's tests (keyword in the domain is already taken by competitors, funded vendors in the results, dedicated sites already ranking, tool volume ~100), this is a **weak candidate**. My recommendation: **don't build it as a second site now**, or build it only as a small, cheap experiment with the differentiators in §4. A better next step is to research the **B2B factura electrónica obligatoria** wave (RD 238/2026; fixed dates of 06/10/2027 for companies over €8M and 06/10/2028 for everyone else, in the BOE via Orden HAC/1028/2026), which is rising instead of fading. I have not researched that niche's competition.

---

## 1. Keywords

Source: Google Spain autocomplete (`suggestqueries.google.com … hl=es&gl=es`), 30 seeds, a–z on "verifactu" and "qr verifactu", plus about 50 long-tail probes. That gave 503+ unique suggestions, saved raw in `work/verifactu/autocomplete.json`.
Volumes come from the Ahrefs Free Keyword Generator, country Spain, run 2026-11-13. They are **Ahrefs buckets, so every number is an estimate**. The free tool shows only 20 rows and hides KD on the lower rows. Raw tables: `/workspace/web/notes/4d33c9a5-39ad-43fa-885b-d72bfcc6b372/ahrefs-free-tu_ie5zqzjkuktwobnkqk2dfnnxm6/ahrefs-keyword-generator.md`.

### Clusters → page mapping

| # | Cluster | Example queries (autocomplete) | Est. volume (Ahrefs ES) | Maps to |
|---|---|---|---|---|
| A | **Fechas / aplazamiento** (news-driven, biggest) | verifactu 2027, verifactu 2028, verifactu aplazamiento boe, aplazamiento verifactu 2028 boe, verifactu se aplaza a 2028, verifactu retraso, verifactu boe hoy, verifactu ultima hora, verifactu entrada en vigor, cuando entra verifactu para autonomos | "verifactu entrada en vigor" >1K (Medium), "verifactu cuando entra en vigor" >1K, "verifactu 2027" >1K (Easy), "verifactu 2028" >1K, "retraso verifactu" >100, "se aplaza / se retrasa verifactu" >100 | Guide: "Fechas de Verifactu: qué está en el BOE y qué solo anunciado" + countdown widget |
| B | **¿Estoy obligado?** | verifactu es obligatorio, verifactu quien esta obligado, verifactu obligatorio autonomos, verifactu autónomos módulos, verifactu exentos, estoy obligado a verifactu, verifactu recargo de equivalencia, verifactu navarra, verifactu sii | "verifactu es obligatorio" >1K (**Easy**), "verifactu obligatorio" >100, "quien esta obligado a verifactu" >100, "verifactu autónomos" >100 | Tool: "¿Estoy obligado a Verifactu?" checker |
| C | **Qué es / cómo funciona** | que es verifactu, que es verifactu y como funciona, verifactu para que sirve, verifactu vs sii, verifactu y factura electronica es lo mismo, verifactu y ticketbai | "que es verifactu" >1K (Medium), "como funciona verifactu" >100 | Guides (home-page body + FAQ) |
| D | **Gratis / programa** (commercial; vendor-dominated) | verifactu gratis, verifactu gratis aeat, programa facturacion verifactu gratis, verifactu software gratis, aplicación gratuita aeat | "verifactu gratis" >1K (**Easy**) | Guide: "Cómo cumplir Verifactu gratis" (AEAT free app + free tools); affiliate-free |
| E | **QR** | qr verifactu, generar qr verifactu, crear qr verifactu, validar qr verifactu, verificar / comprobar / leer / lector qr verifactu, qr verifactu tamaño / medidas / posicion / ubicacion / dimensiones, url qr verifactu, verifactu url pruebas / produccion, qr verifactu ejemplo, requisitos / especificaciones / normativa qr verifactu, qr tributario verifactu, qr no verifactu | "qr verifactu" >100; all variants <100 | Tools: QR generator, QR validator/reader; guide: QR size/position rules |
| F | **Huella / hash** | huella verifactu, calculo huella verifactu, calcular huella verifactu, hash verifactu, codigo hash verifactu, verifactu huella hash | no Ahrefs data (<100 implied) | Tool: huella calculator + chain checker |
| G | **XML / técnico (devs)** | verifactu xml, verifactu xml ejemplo, verifactu xsd, verifactu esquema / estructura / formato xml, verifactu validar xml, verificar xml verifactu, verifactu wsdl, verifactu api, verifactu github, verifactu javascript, verifactu codigos error, listado errores verifactu, verifactu tipo factura f1/f3, verifactu clave regimen, verifactu calificacion operacion, verifactu subsanacion, registro de anulacion | not measured; likely <100 each | Tools: XML example generator + XSD validator; reference pages for TipoFactura / error codes |
| H | **Excel / Word** | verifactu excel, verifactu excel y word, verifactu facturas excel, obligacion verifactu excel, ley antifraude facturas excel, plantilla factura verifactu, factura excel verifactu | "verifactu excel" <100 | Guide: "¿Puedo seguir facturando con Excel?" |
| I | **Sectores** | verifactu bares / hosteleria / taxi / tpv / tickets / venta ambulante / maquinas vending / abogados / farmacias / kiosco / tienda online / woocommerce | "tpv verifactu" >100; rest <100 | Long-tail guides (blog-style, later) |
| J | **Sanciones** | verifactu multas, multa verifactu, verifactu sanciones | not measured | Guide |
| K | **NIF** (adjacent, high volume, very competitive) | validar nif, validar nif aeat, comprobar nif verifactu | not measured | Optional tool: NIF/CIF/NIE check digit |
| L | **TicketBAI / Navarra** (different law, Basque/Navarra only) | ticketbai, ticketbai bizkaia / gipuzkoa / alava, verifactu ticketbai, verifactu navarra | not measured | One comparison guide only; separate niche |
| M | Brand/vendor (exclude) | verifactu holded / odoo / sage / factusol / quipu / zoho / b2brouter… | — | Exclude (playbook: no brand keywords) |

Takeaways: the tool clusters (E, F, G) are tiny. The volume is in A, B, C and D, which are informational and news-shaped. A, B and D are the only >1K "Easy" opportunities Ahrefs shows ("verifactu 2027", "verifactu es obligatorio", "verifactu gratis").

---

## 2. Competitors (Google ES, top phrases)

Method: web_search with country=ES for the main tool phrases (generar/validar qr, huella, xml, obligado) plus the date queries, fetching the leaders. These are search-engine results, not a live VPN SERP, so treat positions as approximate. Traffic comes from the Ahrefs Free Traffic Checker (2026-11-13, estimates). Raw file: `/workspace/web/notes/4d33c9a5-39ad-43fa-885b-d72bfcc6b372/ahrefs-free-tu_ie5zqzjkuktwobnkqk2dfnnxm6/ahrefs-traffic-checker.md`.

| Site | What it offers | Gaps / weaknesses | Ahrefs traffic est. |
|---|---|---|---|
| **factulupa.es** (https://factulupa.es/) | Full hub: QR validator (URL + photo, error codes 1001–2006), huella chain checker (paste XML, finds the broken link), QR generator (level M, SVG/PNG), XSD validator (libxml2-WASM, errors in Spanish), "¿desde cuándo me obliga?", software comparison, guides (plazos, obligados, sanciones, TicketBAI/SII), developer pages with code. Reproduces the 3 AEAT vectors. AdSense + GA4. | Homepage reviewed 25/09/2026 still shows only the RD-ley 15/2025 dates, with no visible note about the Oct-2028 announcement (on the homepage I fetched). No print-ready invoice/QR layout preview (mm sizing, "QR tributario:" label, legend). No anulación/evento builder beyond checking. Not mobile-tested by me. | 0 (too new or not ranking) |
| **recibeo.com** (/herramientas/calculadora-huella-verifactu, /validador-qr-verifactu) | Huella calculator (alta + anulación, with official examples), QR validator (PDF, photo, camera, link; checks real AEAT domain, test vs production, NIF check digit, unencoded "&"). | Part of a SaaS (vendor site). No XSD validation, no evento hash, no generator with print layout. | 0 |
| **kiwop.com/calculadora-huella-verifactu** | Huella for alta, anulación **and evento**, chaining, QR URL and QR image; in ES/EN/PT. | An agency site, so a weak domain-topic match. No XML validation, no obligation checker. | 0 (exact URL) |
| verifactu.co (/laboratorio/) | "Lab": choose F1/F2, IVA/IGIC/IPSI etc. and get JSON, cURL, code, XML, QR and huella. | Dev-only (API vendor based in Estonia); hard for non-technical users. | 0 |
| validatefin.com/es/tools/verifactu | XSD + AEAT business-rule validation (validaciones v1.2.2) + huella recompute; sample files. | Multi-tool finance site; its traffic is German IBAN/SEPA, not Verifactu. | 875/mo total (only ~9% Spain, none of it Verifactu) |
| verifactu.tools | XML validator (schema + 214 rules + chain) and an API. | Dev/SaaS beta; English-style product pitch. | not checked |
| einvoicechecker.com/es/validador-verifactu | XML, AEAT response XML, QR URL check; explains error 2000. | Generic e-invoice brand. | not checked |
| verifactuhoy.com | Huella calculator, obligation check, QR reader, B2B e-invoice check, embeddable widgets. | — | 0 |
| lectorqrverifactu.com | Exact-match domain: QR reader from image/camera/clipboard. | Single tool; says obligation is "desde octubre de 2025", which is outdated/wrong. | 0 |
| bluefactu.com/generador-qr-verifactu, usezivo.com/tools/verifactu-qr-generator, okverifactu.com, selloqr.com, facturaenregla.com, facilgestor.es, rulesdue.com, softnet.es, lou.tools | QR generators/readers and "¿estoy obligado?" tests. | Mostly vendor lead magnets; usezivo's Spanish page is in English. | facturaenregla 0; others not checked |
| GitHub libraries (verifactu-js, kreyo-io/verifactu-hash-calculator, gwi1i.github.io/verifactu) | Code/libraries; one github.io page ranks. | — | — |

For the informational cluster (dates, "es obligatorio"), the results are AEAT (sede), El Mundo, eldiario.es, Público, and vendor guides (contix.es, faktu.org, autonomofactura.com, billin.net, getrenn, factucheck…). That is very competitive.

**Top 3 competitors and their gaps**
1. **factulupa.es**: covers almost everything. Gaps: the 2028 announcement isn't prominent on its homepage, there's no printable invoice/QR-placement preview, and there's no evento-hash tool.
2. **recibeo.com**: strong QR validator and huella tool. Gaps: no XSD validation, no evento hash, and it's a vendor (sales intent).
3. **kiwop.com calculator**: the only one with an evento hash next to alta/anulación. Gaps: one page on an agency domain, no obligation checker, no XML.

Remaining openings, all small: (a) a printable **"plantilla QR tributario"** layout tool that outputs a 30–40 mm QR with the "QR tributario:" label and legend, positioned per §3.2, as a PDF/PNG to paste onto an invoice; (b) a **TipoFactura / ClaveRegimen / CalificacionOperacion / error-code lookup** in plain Spanish; (c) a dates page kept strictly current, "BOE vs anunciado", updated the day a new norm appears.

---

## 3. Official specs (AEAT/BOE only)

### 3.1 QR URL format (AEAT doc v0.5.0, 10/12/2025)
Source: https://www.agenciatributaria.es/static_files/AEAT_Desarrolladores/EEDD/IVA/VERI-FACTU/DetalleEspecificacTecnCodigoQRfactura.pdf (§§4–8)

- Verifiable (VERI*FACTU) systems:
  - Test: `https://prewww2.aeat.es/wlpl/TIKE-CONT/ValidarQR?nif=…&numserie=…&fecha=DD-MM-AAAA&importe=…`
  - Production: `https://www2.agenciatributaria.gob.es/wlpl/TIKE-CONT/ValidarQR?nif=…&numserie=…&fecha=…&importe=…`
- Non-verifiable (No VERI*FACTU) systems: the same hosts with path `/wlpl/TIKE-CONT/ValidarQRNoVerifactu?…`
- Exactly **4 mandatory parameters** (§6):
  - `nif`: NIF format, length 9.
  - `numserie`: series + number, max 60 chars, printable ASCII 32–126.
  - `fecha`: date of issue, DD-MM-AAAA with hyphens.
  - `importe`: invoice total, "." as decimal separator, max 12 integer + 2 decimal digits.
- Parameter values must be URL-encoded in UTF-8 (e.g. `12345678&G33` → `12345678%26G33`).
- Optional parameters (§7): `idioma` (gl, ca, eu, es, va, en; default es) and `formato=json`. `formato` must **never** appear in the URL printed in the QR; it is only for machine checks.
- Official example: `https://www2.agenciatributaria.gob.es/wlpl/TIKE-CONT/ValidarQR?nif=89890001K&numserie=12345678-G33&fecha=01-09-2024&importe=241.4`
- Cotejo results: `"00"` Encontrada, `"01"` No encontrada (or annulled), `"02"` No contrastable (non-verifiable system).
- Error codes: 1001–1004 for a missing nif/numserie/fecha/importe; 2001 bad NIF; 2002 numserie too long; 2003 invalid chars; 2004 bad date; 2005 bad importe format (e.g. a comma); 2006 importe too long; 3001 technical error; 3002 daily attempt limit exceeded.

### 3.2 QR size and position
Same doc, §2 (quoting Orden HAC/1177/2024 art. 21) and §3.
- Size **30×30 to 40×40 mm**, ISO/IEC 18004:2015, error correction **level M**.
- Quiet zone at least **2 mm** on all sides (6 mm recommended); high contrast.
- Placed **at the start of the invoice**, before the content, and the first QR on the invoice. On a multi-page invoice it appears once, on page 1.
  - Portrait: top, near the top margin, preferably centred (otherwise top-left).
  - Landscape: on the left, preferably top-left.
  - On A4, issuer/recipient data and a logo may sit beside it (annex examples i–k).
- The text **"QR tributario:"** must appear above the QR.
- VERI*FACTU systems only: **"Factura verificable en la sede electrónica de la AEAT"** or **"VERI*FACTU"** directly below the QR.
- Both texts in a font size equal to or larger than the rest of the invoice data.
- The legal basis for the QR and legend on invoices is RD 1619/2012 art. 6.5 / 7.5 as added by RD 1007/2023 DF 1ª (BOE consolidated text, link in §3.5).

### 3.3 Huella (hash) (AEAT doc v0.1.2, 27/08/2024)
Source: https://www.agenciatributaria.es/static_files/AEAT_Desarrolladores/EEDD/IVA/VERI-FACTU/Veri-Factu_especificaciones_huella_hash_registros.pdf
- Algorithm **SHA-256**, the only one allowed (list L12). Output is **hexadecimal, UPPERCASE, 64 chars**.
- Input string: `campo1=valor1&campo2=valor2&…`, encoded as **UTF-8** bytes.
  - Values are trimmed (leading/trailing spaces removed).
  - Numeric fields: 1 or 2 decimals are equivalent (123.1 = 123.10).
  - An empty or absent field is written as `Nombre=` (e.g. the first record has `Huella=`).
- **Alta** field order:
  1. IDEmisorFactura
  2. NumSerieFactura
  3. FechaExpedicionFactura
  4. TipoFactura
  5. CuotaTotal
  6. ImporteTotal
  7. Huella (of the previous record)
  8. FechaHoraHusoGenRegistro
- **Anulación** field order:
  1. IDEmisorFacturaAnulada
  2. NumSerieFacturaAnulada
  3. FechaExpedicionFacturaAnulada
  4. Huella (previous)
  5. FechaHoraHusoGenRegistro
- **Evento** field order:
  1. NIF (SistemaInformatico)
  2. ID (IDOtro)
  3. IdSistemaInformatico
  4. Version
  5. NumeroInstalacion
  6. NIF (ObligadoEmision)
  7. TipoEvento
  8. HuellaEvento (previous)
  9. FechaHoraHusoGenEvento
- Where it is stored: RegistroAlta/Huella, RegistroAnulacion/Huella, RegistroEvento/Evento/HuellaEvento. The first record sets PrimerRegistro="S" and still carries its own Huella.
- If the hash a VERI*FACTU system sends doesn't match the AEAT's own calculation, the record is marked **"Aceptado con errores"** (§7).
- **Official worked examples. I re-computed all three with Python and they match exactly:**
  - Alta 1: `IDEmisorFactura=89890001K&NumSerieFactura=12345678/G33&FechaExpedicionFactura=01-01-2024&TipoFactura=F1&CuotaTotal=12.35&ImporteTotal=123.45&Huella=&FechaHoraHusoGenRegistro=2024-01-01T19:20:30+01:00` → `3C464DAF61ACB827C65FDA19F352A4E3BDC2C640E9E9FC4CC058073F38F12F60`
  - Alta 2: NumSerie `12345679/G34`, Huella = the hash above, timestamp `2024-01-01T19:20:35+01:00` → `F7B94CFD8924EDFF273501B01EE5153E4CE8F259766F88CF6ACB8935802A2B97`
  - Anulación: `IDEmisorFacturaAnulada=89890001K&NumSerieFacturaAnulada=12345679/G34&FechaExpedicionFacturaAnulada=01-01-2024&Huella=F7B94…2B97&FechaHoraHusoGenRegistro=2024-01-01T19:20:40+01:00` → `177547C0D57AC74748561D054A9CEC14B4C4EA23D1BEFD6F2E69E3A388F90C68`
  - (Note: my fetch tool garbled the timestamps in the PDF text. The values above are the ones that reproduce the official hashes.)
- AEAT FAQ confirming SHA-256 for all record types: https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu/preguntas-frecuentes/huella-hash.html

### 3.4 XML schemas (AEAT developer page)
Source: https://www.agenciatributaria.es/AEAT.desarrolladores/Desarrolladores/_menu_/Documentacion/Sistemas_Informaticos_de_Facturacion_y_Sistemas_VERI_FACTU/Esquemas_de_los_servicios_web/Esquemas_de_los_servicios_web.html
- `SuministroLR.xsd`: alta and anulación operations (VERI*FACTU and No VERI*FACTU).
- `SuministroInformacion.xsd`: common types.
- `RespuestaSuministro.xsd`: response to submissions.
- `ConsultaLR.xsd` / `RespuestaConsultaLR.xsd`: query of records (VERI*FACTU).
- `EventosSIF.xsd`: event log (No VERI*FACTU).
- `RespuestaValRegistNoVeriFactu.xsd`: validation response for non-VERI*FACTU records.
- Base path: `https://prewww2.aeat.es/static_files/common/internet/dep/aplicaciones/es/aeat/tikeV1.0/cont/ws/` (the page marks these "con certificado", so a direct download may need a client certificate; competitors bundle copies).
- Other docs on the developer page: Descripción servicios web v1.0.3, WSDL, Validaciones y errores, firma electrónica spec, FAQs desarrolladores (updated 04-12-2025), Ejemplos de declaraciones responsables. The root element of a submission is `RegFactuSistemaFacturacion`, which contains `RegistroAlta` / `RegistroAnulacion` (per the XSD names; also seen in competitor samples).
- Technical order: Orden HAC/1177/2024 (BOE 28-10-2024): https://www.boe.es/buscar/act.php?id=BOE-A-2024-22138

### 3.5 Obligation dates: what is law vs announced
- **In force (BOE):** RD 1007/2023 DF 4ª, as worded by **Real Decreto-ley 15/2025, de 2 de diciembre** (BOE-A-2025-24446). Corporate-tax payers (art. 3.1.a) must be adapted **before 1 January 2027**; everyone else in art. 3.1 (autónomos/IRPF with activity, atribución de rentas entities, IRNR with a permanent establishment) **before 1 July 2027**. Software producers have had to offer adapted products since 29/07/2025, nine months after the Orden came into force (29/10/2024).
  - Source: BOE consolidated text, "última actualización publicada el 03/12/2025", fetched 2026-11-13: https://www.boe.es/buscar/act.php?id=BOE-A-2023-24840
  - The AEAT note confirms the same dates and that the period before them is a test period: https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu/nota-informativa-ampliacion-plazo-adaptacion-facturacion.html
- **Announced only, NOT in the BOE:** Ministerio de Hacienda nota informativa of **05/10/2026** announcing the *intention* ("previsión") to postpone the pending obligations **"hasta octubre de 2028"**, to align with B2B e-invoicing for businesses with turnover up to €8M. It gives no exact day. It also says a later modification will align scope and technical aspects with ViDA.
  - Source: https://www.hacienda.gob.es/sgt/gabsehacienda/nota-informativa-verifactu.pdf
  - The AEAT Verifactu page (updated 03/11/2026) lists it as "Previsión de ampliación del plazo": https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu.html
- **Conflict, stated explicitly:** as of 2026-11-13 the BOE consolidated text still shows the **2027 dates**. I found no BOE norm implementing the 2028 delay.
  - Secondary sources (not official) dated up to 07–09/11/2026 agree that it is unpublished.
  - They also report the Cortes were dissolved on 05/10/2026, with general elections on 29/11/2026 (Gestifácil, 07/11/2026; I have not verified this against an official source). That could affect how and when a delay is enacted.
  - Much of the press (El Mundo, eldiario.es, Público, some vendors) reports 2028 as if it were final, which it is not yet.
  - Any site we publish must show **"2027 vigente (BOE) / octubre 2028 anunciado"** and be updated the day a norm appears.
- Related, in the BOE: Orden HAC/1028/2026 (BOE 05/10/2026, in force 06/10/2026) started the B2B e-invoice clock under RD 238/2026: 12 months for businesses over €8M and 24 months for the rest (AEAT news: https://sede.agenciatributaria.gob.es/Sede/todas-noticias/2026/octubre/7/solucion-publica-facturacion-electronica.html).
- Scope (BOE art. 3): the Reglamento does not apply to SII taxpayers (art. 3.3), and it applies only to taxpayers with fiscal domicile in territorio común (art. 1.3). The País Vasco has TicketBAI and Navarra its own rules. Art. 5 provides for a resolution of non-application.
- Sanctions: art. 201 bis LGT is linked from the AEAT page. The amounts (€50,000 per year for users, €150,000 for producers) come from secondary sources and I did not open the BOE article, so **verify before publishing**.

---

## 4. Recommended site plan (only if Yasir still wants to build it)

### Domains (checked by DNS only; NXDOMAIN suggests free, not guaranteed)
1. Free first: **herramientasverifactu.dpdns.org** or **qrverifactu.dpdns.org** (both NXDOMAIN). The playbook warns subdomains rank poorly; fine for a test.
2. Cheap paid later: **huellaverifactu.es / .com**, **herramientasverifactu.es / .com**, **qrverifactu.es**, **validarverifactu.es**, **comprobarverifactu.es**, **generadorqrverifactu.es** (all NXDOMAIN).
3. Taken: qrverifactu.com, verifactuqr.es/.com, verifactugratis.es/.com, verifactufacil.es.

### Tool pages ranked by opportunity (all client-side JS: Web Crypto SHA-256, a JS QR encoder, jsQR/pdf.js for reading, libxml2-wasm for XSD)
1. **"¿Estoy obligado a Verifactu?" + fecha checker.** Biggest Easy keyword ("verifactu es obligatorio" >1K). Must show both the BOE date and the announced Oct-2028 date, with sources. Many competitors have it, but most are vendor lead magnets.
2. **QR tributario generator with a print-ready layout.** Our differentiator: mm-exact 30/35/40 mm, level M, "QR tributario:" label, VERI*FACTU legend option, test/production/NoVerifactu toggle, A4/ticket (57 mm) preview, PNG/SVG/PDF export.
3. **QR validator / reader** (paste URL, photo, PDF or camera). Checks host, path, the 4 parameters, encoding, NIF check digit and AEAT error codes, then links to the official cotejo.
4. **Huella calculator + chain checker.** Alta, anulación **and evento**, the 3 official vectors preloaded, and chaining of several records.
5. **XML example builder + XSD validator** (RegistroAlta/Anulación generator that fills the huella and validates against the bundled XSDs).
6. **Code reference lookup:** TipoFactura (F1, F2, R1–R5, F3), ClaveRegimen, CalificacionOperacion, the AEAT error-code list, all in plain Spanish. Low competition, long tail.
7. Optional: **NIF/CIF/NIE validator** (huge but competitive keyword; "comprobar nif verifactu" angle).

### Guide topics
1. Fechas de Verifactu: 2027 en el BOE vs octubre 2028 anunciado (keep current; "verifactu 2027/2028", "aplazamiento boe").
2. Verifactu gratis: la aplicación gratuita de la AEAT y cómo cumplir sin pagar.
3. ¿Puedo seguir facturando con Excel o Word? (AEAT criterion).
4. Tamaño y posición del QR tributario: reglas oficiales con ejemplos.
5. Verifactu vs TicketBAI vs SII vs factura electrónica obligatoria (B2B 2027/2028).
(Later: per-sector guides for bares, taxis, TPV, autónomos en módulos and recargo de equivalencia, plus sanciones.)

### Honest expectations
Based on the evidence above, expect very little organic traffic for this niche: tool keywords are <100/mo each, a dozen near-identical free sites already exist, and urgency is likely to drop once the 2028 delay is legislated. If built, keep it to one weekend of work. Reuse the KSeF site's template and the playbook's on-page checklist. Launch it with the "fechas BOE vs anunciado" page as the main traffic bet, then judge after 3 months in Search Console.

---

## Files
- This report: `/workspace/projects/4d33c9a5-39ad-43fa-885b-d72bfcc6b372/work/verifactu/research.md`
- Raw autocomplete (503+ suggestions): `/workspace/projects/4d33c9a5-39ad-43fa-885b-d72bfcc6b372/work/verifactu/autocomplete.json` (scripts `ac.py`, `ac2.py`)
- Ahrefs raw tables: `/workspace/web/notes/4d33c9a5-39ad-43fa-885b-d72bfcc6b372/ahrefs-free-tu_ie5zqzjkuktwobnkqk2dfnnxm6/ahrefs-keyword-generator.md` and `…/ahrefs-traffic-checker.md`
