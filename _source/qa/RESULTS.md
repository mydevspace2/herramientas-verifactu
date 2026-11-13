# QA – Herramientas Verifactu, 2026-11-13 (v3: pase SEO completo + 2 guías nuevas + etiqueta de Search Console)

Resumen: unitarias Verifactu 42/42 · unitarias B2B 29/29 · XSD + QR 13/13 · estáticas 205/205 (incluye Organization/WebSite/Article/FAQPage/BreadcrumbList, lastmod AAAA-MM-DD, description < 160, ≥ 3 guías relacionadas, img con alt, meta google-site-verification solo en portada) · Chromium con CSP (escritorio, móvil 375 px, modo oscuro) 143/143 = 432/432. Compilado con VF_GSV.

## t-core
```
Huella – ejemplos oficiales AEAT (doc. huella v0.1.2, apdo. 6)
  ✓ Caso 1 (alta, primer registro) = 3C464DAF…8F12F60
  ✓ Caso 2 (alta encadenada) = F7B94CFD…802A2B97
  ✓ Caso 3 (anulación) = 177547C0…88F90C68
  ✓ EJEMPLOS incluidos en la web coinciden con la AEAT
  ✓ Recorta espacios iniciales y finales, no los interiores
  ✓ Evento: 9 campos en el orden oficial, NIF dos veces, ID vacío
  ✓ SHA-256 propio = crypto de Node (200 cadenas aleatorias, UTF-8, varias longitudes)
  ✓ avisosHuella detecta fecha sin huso y huella anterior en minúsculas
NIF / NIE / CIF
  ✓ DNI y NIF especial AEAT de pruebas 89890001K
  ✓ DNI con letra errónea
  ✓ DNI 12345678Z correcto
  ✓ NIE X1234567L / Y… / Z…
  ✓ CIF B12345674 correcto, B12345675 incorrecto
  ✓ CIF con letra (P, Q, S…) exige letra de control
  ✓ Longitud distinta de 9
Importes y fechas
  ✓ 241,4 → 241.40; 1.234,56 → 1234.56; 1,234.56 → 1234.56; 1210 → 1210.00
  ✓ 1.234 se interpreta como miles con aviso
  ✓ 3 decimales con coma y 13 enteros = error; 12.345 = miles
  ✓ Fechas: 2024-09-01 → 01-09-2024, 1/9/2024 → 01-09-2024, 30-02-2024 inválida
  ✓ ahoraMadrid() con huso horario
URL del QR tributario (doc. QR v0.5.0)
  ✓ Ejemplo oficial 8.3 (producción, VERI*FACTU) se reproduce
  ✓ Rutas: pruebas y NoVerifactu
  ✓ «&» se codifica como %26 (ejemplo del apdo. 4)
  ✓ Errores 1001–1004, 2002, 2003, 2004, 2005
  ✓ parseQrUrl: ejemplo oficial correcto
  ✓ parseQrUrl: & sin codificar + importe con coma (ejemplo erróneo de la AEAT)
  ✓ parseQrUrl: NIF 891K (ejemplo AEAT) → 2001
  ✓ parseQrUrl: dominio que imita a la AEAT → phishing
  ✓ parseQrUrl: http, formato=json, idioma inválido, parámetro faltante
  ✓ parseQrUrl: NoVerifactu + idioma válido + espacios como + y %20
  ✓ Ida y vuelta: buildQrUrl → parseQrUrl con caracteres especiales
Codificador QR (nivel M) – lectura con zxing-cpp en test-qr.py
  ✓ Nivel M y versión 7–8 para una URL normal (45–49 módulos)
  ✓ La URL más larga posible cabe (versión ≤ 10)
XML de alta, comprobación estructural y cadena
  ✓ Totales: cuota 21.00, importe 171.00
  ✓ Huella del XML = huella de la cadena oficial
  ✓ Caracteres especiales escapados en el XML
  ✓ checkAltaXml: XML generado sin errores (F1, F1 encadenada, F2)
  ✓ checkAltaXml: detecta huella alterada, orden y obligatorios
[xmldom fatalError]	Opening and ending tag mismatch: "b" != "a" 
@#[line:1,col:4]
  ✓ checkAltaXml: XML mal formado
  ✓ checkChain: ejemplos AEAT en XML → cadena correcta
  ✓ checkChain: registros generados encadenados (b1 → b2) correctos
  ✓ checkChain: importe 123.4 vs 123.40 → aviso de decimales, no error

Resultado: 42 correctas, 0 fallidas
```

## t-b2b
```
Fechas, importes y CSV
  ✓ parseDate: AAAA-MM-DD, DD/MM/AAAA, DD-MM-AA; rechaza 31/02
  ✓ parseAmount: 1.234,56 · 1234,56 · 1,234.56 · 1 234,56 € · 1.234 · 12.5 · -50
  ✓ fmt: formato español con miles y coma decimal
  ✓ parseCsv: separador ; , y tabulador, comillas
PMP – método ICAC (BOE-A-2016-1112, art. 5)
  ✓ Ejemplo 1: ratio pagadas 56,67 · pendientes 34,00 · PMP 47,60
  ✓ Ejemplo 1: días por operación (30, 70, 46, 30) y la pagada tras el cierre cuenta como pendiente
  ✓ Ejemplo 1: DA 3.ª Ley 15/2010 – pagadas dentro de 60 días: 1 de 2 facturas (50 %) y 1.000 de 3.000 € (33,33 %)
  ✓ Ejemplo 2 (supera 60 días): 10.000 € pagados a 90 días + 10.000 € pendientes 40 días → PMP 65
  ✓ Fórmula: PMP = media ponderada por importe de todos los días (identidad algebraica, 500 casos aleatorios)
  ✓ Filtros: operación posterior al cierre, pago anterior al ejercicio, fechas e importes no válidos → omitidos con aviso
  ✓ Sin cierre o sin filas válidas → error
  ✓ Modelo abreviado (art. 5.5): 50.000 / 400.000 × 365 = 45,625 días; saldo medio (40.000 + 60.000) / 2
  ✓ CSV con cabecera de la plantilla, en otro orden, sin cabecera y fila pegada de Excel con texto
Intereses de demora – Ley 3/2004, art. 7 (tipos del BOE)
  ✓ La tabla de tipos coincide con las 27 resoluciones del BOE descargadas (2.º sem. 2013 – 2.º sem. 2026)
  ✓ Tipos clave: 2.º sem. 2026 = 10,40 % (BOE-A-2026-14327); 1.º sem. 2026 = 10,15 %; 1.º sem. 2024 = 12,50 %
  ✓ Ejemplo: 10.000 € vencidos 15/06/2025 y pagados 14/08/2025 → 60 días, 2 tramos, 170,96 €
  ✓ Ejemplo: 2.420 € (IVA incluido) vencidos 31/12/2025 y pagados 31/01/2026 → 31 días al 10,15 % = 20,86 €
  ✓ Pago en plazo → 0; tipo pactado sustituye al legal (art. 7.1)
  ✓ Fuera de la tabla: antes del 1/7/2013 error; 2027 sin publicar → error salvo «estimar»
  ✓ Vencimiento (art. 4): 30 días por defecto; pactos > 60 días se limitan a 60
Plazo de 4 días (RD 238/2026, arts. 10.3 y 12.3)
  ✓ Pascua: 2026-04-05, 2027-03-28, 2028-04-16
  ✓ Viernes Santo calculado = el de la lista del BOE (2026: 3 abr; 2027: 26 mar)
  ✓ Pago el viernes 08/10/2027 → límite viernes 15/10/2027 (salta sábado, domingo y el 12 de octubre)
  ✓ Pago el miércoles 22/12/2027 → límite martes 28/12/2027 (salta sábado 25, Navidad, y domingo 26)
  ✓ Pago el jueves 30/12/2027 → límite miércoles 05/01/2028 (provisional: 2028 aún sin lista oficial)
  ✓ Pago el lunes 06/11/2028 → viernes 10/11/2028 (año sin lista oficial: marcado provisional)
  ✓ Festivo adicional del usuario (p. ej. autonómico) también se salta
Factura electrónica B2B – RD 238/2026 DF 4.ª, DT 2.ª y 3.ª; Orden HAC/1028/2026 en vigor el 06/10/2026
  ✓ Fechas: 06/10/2027 (> 8 M€), 06/10/2028 (resto), 06/10/2029 (estados, personas físicas ≤ 8 M€)
  ✓ Checker: grande → 2027 + PDF; sociedad pequeña → 2028; autónomo pequeño → emitir 2028, estados 2029; solo tiques → no emite

Resultado: 29 correctas, 0 fallidas
```

## xsd-qr
```
XSD oficial AEAT (SuministroLR.xsd + SuministroInformacion.xsd)
  ✓ alta-1.xml válido contra el XSD
  ✓ alta-2.xml válido contra el XSD
  ✓ alta-f2.xml válido contra el XSD
  ✓ control negativo: TipoFactura F9 es rechazado por el XSD
Lectura de los QR generados (zxing-cpp)
  ✓ QR 1 (v8, 49 módulos) se lee y coincide con la URL
  ✓ QR 1 con nivel de corrección M
  ✓ QR 2 (v10, 57 módulos) se lee y coincide con la URL
  ✓ QR 2 con nivel de corrección M
  ✓ QR 3 (v8, 49 módulos) se lee y coincide con la URL
  ✓ QR 3 con nivel de corrección M
Archivos producidos en el navegador (test-browser-csp.js), si existen
  ✓ XML generado en Chromium válido contra el XSD
  ✓ PNG descargado (600 ppp, 1016x1250 px) se lee: https://prewww2.aeat.es/wlpl/TIKE-CONT/Valida…
  ✓ SVG descargado en mm: bloque 43 × 52.94 mm, QR de 45 módulos × 0.778 mm = 35.00 mm (35 mm pedidos)

Resultado: 13 correctas, 0 fallidas
```

## t-site
```
Sitio: https://mydevspace2.github.io/herramientas-verifactu (BASE «/herramientas-verifactu») – 22 páginas HTML
  ✓ robots.txt bloquea /_source/ y enlaza el sitemap
  ✓ sitemap.xml bien formado con 21 URL y <lastmod> solo AAAA-MM-DD
  ✓ /404.html – enlaces internos existen (con BASE)
  ✓ /404.html – anclas #id existen y no hay id duplicados
  ✓ /404.html – JSON-LD válido (WebApplication/WebPage, BreadcrumbList, FAQPage = FAQ visible)
  ✓ /404.html – SEO: Organization + WebSite en JSON-LD, Article con fechas ISO en guías, <img> con alt, <time> ISO
  ✓ /404.html – meta: title ≤ 70, description 70–160, canonical, hreflang es/x-default, OG, un H1, lang=es
  ✓ /404.html – seguridad y rendimiento: CSP, CSS inline, sin style=, sin scripts inline salvo tema/JSON-LD, sin CDN
  ✓ /404.html – accesibilidad: campos con etiqueta, botones con texto
  ✓ /404.html – enlaces visibles a privacidad, aviso legal, contacto y sobre nosotros
  ✓ /aviso-legal/ – enlaces internos existen (con BASE)
  ✓ /aviso-legal/ – anclas #id existen y no hay id duplicados
  ✓ /aviso-legal/ – JSON-LD válido (WebApplication/WebPage, BreadcrumbList, FAQPage = FAQ visible)
  ✓ /aviso-legal/ – SEO: Organization + WebSite en JSON-LD, Article con fechas ISO en guías, <img> con alt, <time> ISO
  ✓ /aviso-legal/ – meta: title ≤ 70, description 70–160, canonical, hreflang es/x-default, OG, un H1, lang=es
  ✓ /aviso-legal/ – seguridad y rendimiento: CSP, CSS inline, sin style=, sin scripts inline salvo tema/JSON-LD, sin CDN
  ✓ /aviso-legal/ – accesibilidad: campos con etiqueta, botones con texto
  ✓ /aviso-legal/ – enlaces visibles a privacidad, aviso legal, contacto y sobre nosotros
  ✓ /blog/calcular-periodo-medio-pago-proveedores-ejemplo/ – enlaces internos existen (con BASE)
  ✓ /blog/calcular-periodo-medio-pago-proveedores-ejemplo/ – anclas #id existen y no hay id duplicados
  ✓ /blog/calcular-periodo-medio-pago-proveedores-ejemplo/ – JSON-LD válido (WebApplication/WebPage, BreadcrumbList, FAQPage = FAQ visible)
  ✓ /blog/calcular-periodo-medio-pago-proveedores-ejemplo/ – SEO: Organization + WebSite en JSON-LD, Article con fechas ISO en guías, <img> con alt, <time> ISO
  ✓ /blog/calcular-periodo-medio-pago-proveedores-ejemplo/ – meta: title ≤ 70, description 70–160, canonical, hreflang es/x-default, OG, un H1, lang=es
  ✓ /blog/calcular-periodo-medio-pago-proveedores-ejemplo/ – seguridad y rendimiento: CSP, CSS inline, sin style=, sin scripts inline salvo tema/JSON-LD, sin CDN
  ✓ /blog/calcular-periodo-medio-pago-proveedores-ejemplo/ – accesibilidad: campos con etiqueta, botones con texto
  ✓ /blog/calcular-periodo-medio-pago-proveedores-ejemplo/ – enlaces visibles a privacidad, aviso legal, contacto y sobre nosotros
  ✓ /blog/calcular-periodo-medio-pago-proveedores-ejemplo/ – guía ≥ 700 palabras (1342)
  ✓ /blog/diferencias-verifactu-factura-electronica-b2b/ – enlaces internos existen (con BASE)
  ✓ /blog/diferencias-verifactu-factura-electronica-b2b/ – anclas #id existen y no hay id duplicados
  ✓ /blog/diferencias-verifactu-factura-electronica-b2b/ – JSON-LD válido (WebApplication/WebPage, BreadcrumbList, FAQPage = FAQ visible)
  ✓ /blog/diferencias-verifactu-factura-electronica-b2b/ – SEO: Organization + WebSite en JSON-LD, Article con fechas ISO en guías, <img> con alt, <time> ISO
  ✓ /blog/diferencias-verifactu-factura-electronica-b2b/ – meta: title ≤ 70, description 70–160, canonical, hreflang es/x-default, OG, un H1, lang=es
  ✓ /blog/diferencias-verifactu-factura-electronica-b2b/ – seguridad y rendimiento: CSP, CSS inline, sin style=, sin scripts inline salvo tema/JSON-LD, sin CDN
  ✓ /blog/diferencias-verifactu-factura-electronica-b2b/ – accesibilidad: campos con etiqueta, botones con texto
  ✓ /blog/diferencias-verifactu-factura-electronica-b2b/ – enlaces visibles a privacidad, aviso legal, contacto y sobre nosotros
  ✓ /blog/diferencias-verifactu-factura-electronica-b2b/ – guía ≥ 700 palabras (1471)
  ✓ /blog/factura-electronica-obligatoria-autonomos/ – enlaces internos existen (con BASE)
  ✓ /blog/factura-electronica-obligatoria-autonomos/ – anclas #id existen y no hay id duplicados
  ✓ /blog/factura-electronica-obligatoria-autonomos/ – JSON-LD válido (WebApplication/WebPage, BreadcrumbList, FAQPage = FAQ visible)
  ✓ /blog/factura-electronica-obligatoria-autonomos/ – SEO: Organization + WebSite en JSON-LD, Article con fechas ISO en guías, <img> con alt, <time> ISO
  ✓ /blog/factura-electronica-obligatoria-autonomos/ – meta: title ≤ 70, description 70–160, canonical, hreflang es/x-default, OG, un H1, lang=es
  ✓ /blog/factura-electronica-obligatoria-autonomos/ – seguridad y rendimiento: CSP, CSS inline, sin style=, sin scripts inline salvo tema/JSON-LD, sin CDN
  ✓ /blog/factura-electronica-obligatoria-autonomos/ – accesibilidad: campos con etiqueta, botones con texto
  ✓ /blog/factura-electronica-obligatoria-autonomos/ – enlaces visibles a privacidad, aviso legal, contacto y sobre nosotros
  ✓ /blog/factura-electronica-obligatoria-autonomos/ – guía ≥ 700 palabras (1325)
  ✓ /blog/fechas-verifactu-2027-2028/ – enlaces internos existen (con BASE)
  ✓ /blog/fechas-verifactu-2027-2028/ – anclas #id existen y no hay id duplicados
  ✓ /blog/fechas-verifactu-2027-2028/ – JSON-LD válido (WebApplication/WebPage, BreadcrumbList, FAQPage = FAQ visible)
  ✓ /blog/fechas-verifactu-2027-2028/ – SEO: Organization + WebSite en JSON-LD, Article con fechas ISO en guías, <img> con alt, <time> ISO
  ✓ /blog/fechas-verifactu-2027-2028/ – meta: title ≤ 70, description 70–160, canonical, hreflang es/x-default, OG, un H1, lang=es
  ✓ /blog/fechas-verifactu-2027-2028/ – seguridad y rendimiento: CSP, CSS inline, sin style=, sin scripts inline salvo tema/JSON-LD, sin CDN
  ✓ /blog/fechas-verifactu-2027-2028/ – accesibilidad: campos con etiqueta, botones con texto
  ✓ /blog/fechas-verifactu-2027-2028/ – enlaces visibles a privacidad, aviso legal, contacto y sobre nosotros
  ✓ /blog/fechas-verifactu-2027-2028/ – guía ≥ 700 palabras (1242)
  ✓ /blog/ – enlaces internos existen (con BASE)
  ✓ /blog/ – anclas #id existen y no hay id duplicados
  ✓ /blog/ – JSON-LD válido (WebApplication/WebPage, BreadcrumbList, FAQPage = FAQ visible)
  ✓ /blog/ – SEO: Organization + WebSite en JSON-LD, Article con fechas ISO en guías, <img> con alt, <time> ISO
  ✓ /blog/ – meta: title ≤ 70, description 70–160, canonical, hreflang es/x-default, OG, un H1, lang=es
  ✓ /blog/ – seguridad y rendimiento: CSP, CSS inline, sin style=, sin scripts inline salvo tema/JSON-LD, sin CDN
  ✓ /blog/ – accesibilidad: campos con etiqueta, botones con texto
  ✓ /blog/ – enlaces visibles a privacidad, aviso legal, contacto y sobre nosotros
  ✓ /blog/plazos-pago-ley-morosidad/ – enlaces internos existen (con BASE)
  ✓ /blog/plazos-pago-ley-morosidad/ – anclas #id existen y no hay id duplicados
  ✓ /blog/plazos-pago-ley-morosidad/ – JSON-LD válido (WebApplication/WebPage, BreadcrumbList, FAQPage = FAQ visible)
  ✓ /blog/plazos-pago-ley-morosidad/ – SEO: Organization + WebSite en JSON-LD, Article con fechas ISO en guías, <img> con alt, <time> ISO
  ✓ /blog/plazos-pago-ley-morosidad/ – meta: title ≤ 70, description 70–160, canonical, hreflang es/x-default, OG, un H1, lang=es
  ✓ /blog/plazos-pago-ley-morosidad/ – seguridad y rendimiento: CSP, CSS inline, sin style=, sin scripts inline salvo tema/JSON-LD, sin CDN
  ✓ /blog/plazos-pago-ley-morosidad/ – accesibilidad: campos con etiqueta, botones con texto
  ✓ /blog/plazos-pago-ley-morosidad/ – enlaces visibles a privacidad, aviso legal, contacto y sobre nosotros
  ✓ /blog/plazos-pago-ley-morosidad/ – guía ≥ 700 palabras (1560)
  ✓ /blog/tamano-posicion-qr-verifactu/ – enlaces internos existen (con BASE)
  ✓ /blog/tamano-posicion-qr-verifactu/ – anclas #id existen y no hay id duplicados
  ✓ /blog/tamano-posicion-qr-verifactu/ – JSON-LD válido (WebApplication/WebPage, BreadcrumbList, FAQPage = FAQ visible)
  ✓ /blog/tamano-posicion-qr-verifactu/ – SEO: Organization + WebSite en JSON-LD, Article con fechas ISO en guías, <img> con alt, <time> ISO
  ✓ /blog/tamano-posicion-qr-verifactu/ – meta: title ≤ 70, description 70–160, canonical, hreflang es/x-default, OG, un H1, lang=es
  ✓ /blog/tamano-posicion-qr-verifactu/ – seguridad y rendimiento: CSP, CSS inline, sin style=, sin scripts inline salvo tema/JSON-LD, sin CDN
  ✓ /blog/tamano-posicion-qr-verifactu/ – accesibilidad: campos con etiqueta, botones con texto
  ✓ /blog/tamano-posicion-qr-verifactu/ – enlaces visibles a privacidad, aviso legal, contacto y sobre nosotros
  ✓ /blog/tamano-posicion-qr-verifactu/ – guía ≥ 700 palabras (1164)
  ✓ /blog/verifactu-autonomos/ – enlaces internos existen (con BASE)
  ✓ /blog/verifactu-autonomos/ – anclas #id existen y no hay id duplicados
  ✓ /blog/verifactu-autonomos/ – JSON-LD válido (WebApplication/WebPage, BreadcrumbList, FAQPage = FAQ visible)
  ✓ /blog/verifactu-autonomos/ – SEO: Organization + WebSite en JSON-LD, Article con fechas ISO en guías, <img> con alt, <time> ISO
  ✓ /blog/verifactu-autonomos/ – meta: title ≤ 70, description 70–160, canonical, hreflang es/x-default, OG, un H1, lang=es
  ✓ /blog/verifactu-autonomos/ – seguridad y rendimiento: CSP, CSS inline, sin style=, sin scripts inline salvo tema/JSON-LD, sin CDN
  ✓ /blog/verifactu-autonomos/ – accesibilidad: campos con etiqueta, botones con texto
  ✓ /blog/verifactu-autonomos/ – enlaces visibles a privacidad, aviso legal, contacto y sobre nosotros
  ✓ /blog/verifactu-autonomos/ – guía ≥ 700 palabras (1697)
  ✓ /blog/verifactu-gratis-aplicacion-aeat/ – enlaces internos existen (con BASE)
  ✓ /blog/verifactu-gratis-aplicacion-aeat/ – anclas #id existen y no hay id duplicados
  ✓ /blog/verifactu-gratis-aplicacion-aeat/ – JSON-LD válido (WebApplication/WebPage, BreadcrumbList, FAQPage = FAQ visible)
  ✓ /blog/verifactu-gratis-aplicacion-aeat/ – SEO: Organization + WebSite en JSON-LD, Article con fechas ISO en guías, <img> con alt, <time> ISO
  ✓ /blog/verifactu-gratis-aplicacion-aeat/ – meta: title ≤ 70, description 70–160, canonical, hreflang es/x-default, OG, un H1, lang=es
  ✓ /blog/verifactu-gratis-aplicacion-aeat/ – seguridad y rendimiento: CSP, CSS inline, sin style=, sin scripts inline salvo tema/JSON-LD, sin CDN
  ✓ /blog/verifactu-gratis-aplicacion-aeat/ – accesibilidad: campos con etiqueta, botones con texto
  ✓ /blog/verifactu-gratis-aplicacion-aeat/ – enlaces visibles a privacidad, aviso legal, contacto y sobre nosotros
  ✓ /blog/verifactu-gratis-aplicacion-aeat/ – guía ≥ 700 palabras (1117)
  ✓ /calcular-huella-verifactu/ – enlaces internos existen (con BASE)
  ✓ /calcular-huella-verifactu/ – anclas #id existen y no hay id duplicados
  ✓ /calcular-huella-verifactu/ – JSON-LD válido (WebApplication/WebPage, BreadcrumbList, FAQPage = FAQ visible)
  ✓ /calcular-huella-verifactu/ – SEO: Organization + WebSite en JSON-LD, Article con fechas ISO en guías, <img> con alt, <time> ISO
  ✓ /calcular-huella-verifactu/ – meta: title ≤ 70, description 70–160, canonical, hreflang es/x-default, OG, un H1, lang=es
  ✓ /calcular-huella-verifactu/ – seguridad y rendimiento: CSP, CSS inline, sin style=, sin scripts inline salvo tema/JSON-LD, sin CDN
  ✓ /calcular-huella-verifactu/ – accesibilidad: campos con etiqueta, botones con texto
  ✓ /calcular-huella-verifactu/ – enlaces visibles a privacidad, aviso legal, contacto y sobre nosotros
  ✓ /calcular-huella-verifactu/ – contenido útil bajo la herramienta ≥ 800 palabras (1317)
  ✓ /contacto/ – enlaces internos existen (con BASE)
  ✓ /contacto/ – anclas #id existen y no hay id duplicados
  ✓ /contacto/ – JSON-LD válido (WebApplication/WebPage, BreadcrumbList, FAQPage = FAQ visible)
  ✓ /contacto/ – SEO: Organization + WebSite en JSON-LD, Article con fechas ISO en guías, <img> con alt, <time> ISO
  ✓ /contacto/ – meta: title ≤ 70, description 70–160, canonical, hreflang es/x-default, OG, un H1, lang=es
  ✓ /contacto/ – seguridad y rendimiento: CSP, CSS inline, sin style=, sin scripts inline salvo tema/JSON-LD, sin CDN
  ✓ /contacto/ – accesibilidad: campos con etiqueta, botones con texto
  ✓ /contacto/ – enlaces visibles a privacidad, aviso legal, contacto y sobre nosotros
  ✓ /ejemplo-xml-verifactu/ – enlaces internos existen (con BASE)
  ✓ /ejemplo-xml-verifactu/ – anclas #id existen y no hay id duplicados
  ✓ /ejemplo-xml-verifactu/ – JSON-LD válido (WebApplication/WebPage, BreadcrumbList, FAQPage = FAQ visible)
  ✓ /ejemplo-xml-verifactu/ – SEO: Organization + WebSite en JSON-LD, Article con fechas ISO en guías, <img> con alt, <time> ISO
  ✓ /ejemplo-xml-verifactu/ – meta: title ≤ 70, description 70–160, canonical, hreflang es/x-default, OG, un H1, lang=es
  ✓ /ejemplo-xml-verifactu/ – seguridad y rendimiento: CSP, CSS inline, sin style=, sin scripts inline salvo tema/JSON-LD, sin CDN
  ✓ /ejemplo-xml-verifactu/ – accesibilidad: campos con etiqueta, botones con texto
  ✓ /ejemplo-xml-verifactu/ – enlaces visibles a privacidad, aviso legal, contacto y sobre nosotros
  ✓ /ejemplo-xml-verifactu/ – contenido útil bajo la herramienta ≥ 800 palabras (1297)
  ✓ /factura-electronica-obligatoria/ – enlaces internos existen (con BASE)
  ✓ /factura-electronica-obligatoria/ – anclas #id existen y no hay id duplicados
  ✓ /factura-electronica-obligatoria/ – JSON-LD válido (WebApplication/WebPage, BreadcrumbList, FAQPage = FAQ visible)
  ✓ /factura-electronica-obligatoria/ – SEO: Organization + WebSite en JSON-LD, Article con fechas ISO en guías, <img> con alt, <time> ISO
  ✓ /factura-electronica-obligatoria/ – meta: title ≤ 70, description 70–160, canonical, hreflang es/x-default, OG, un H1, lang=es
  ✓ /factura-electronica-obligatoria/ – seguridad y rendimiento: CSP, CSS inline, sin style=, sin scripts inline salvo tema/JSON-LD, sin CDN
  ✓ /factura-electronica-obligatoria/ – accesibilidad: campos con etiqueta, botones con texto
  ✓ /factura-electronica-obligatoria/ – enlaces visibles a privacidad, aviso legal, contacto y sobre nosotros
  ✓ /factura-electronica-obligatoria/ – contenido útil bajo la herramienta ≥ 800 palabras (1779)
  ✓ /generador-qr-verifactu/ – enlaces internos existen (con BASE)
  ✓ /generador-qr-verifactu/ – anclas #id existen y no hay id duplicados
  ✓ /generador-qr-verifactu/ – JSON-LD válido (WebApplication/WebPage, BreadcrumbList, FAQPage = FAQ visible)
  ✓ /generador-qr-verifactu/ – SEO: Organization + WebSite en JSON-LD, Article con fechas ISO en guías, <img> con alt, <time> ISO
  ✓ /generador-qr-verifactu/ – meta: title ≤ 70, description 70–160, canonical, hreflang es/x-default, OG, un H1, lang=es
  ✓ /generador-qr-verifactu/ – seguridad y rendimiento: CSP, CSS inline, sin style=, sin scripts inline salvo tema/JSON-LD, sin CDN
  ✓ /generador-qr-verifactu/ – accesibilidad: campos con etiqueta, botones con texto
  ✓ /generador-qr-verifactu/ – enlaces visibles a privacidad, aviso legal, contacto y sobre nosotros
  ✓ /generador-qr-verifactu/ – contenido útil bajo la herramienta ≥ 800 palabras (1409)
  ✓ / – enlaces internos existen (con BASE)
  ✓ / – anclas #id existen y no hay id duplicados
  ✓ / – JSON-LD válido (WebApplication/WebPage, BreadcrumbList, FAQPage = FAQ visible)
  ✓ / – SEO: Organization + WebSite en JSON-LD, Article con fechas ISO en guías, <img> con alt, <time> ISO
  ✓ / – meta: title ≤ 70, description 70–160, canonical, hreflang es/x-default, OG, un H1, lang=es
  ✓ / – seguridad y rendimiento: CSP, CSS inline, sin style=, sin scripts inline salvo tema/JSON-LD, sin CDN
  ✓ / – accesibilidad: campos con etiqueta, botones con texto
  ✓ / – enlaces visibles a privacidad, aviso legal, contacto y sobre nosotros
  ✓ / – contenido útil bajo la herramienta ≥ 800 palabras (1739)
  ✓ /intereses-demora-comerciales/ – enlaces internos existen (con BASE)
  ✓ /intereses-demora-comerciales/ – anclas #id existen y no hay id duplicados
  ✓ /intereses-demora-comerciales/ – JSON-LD válido (WebApplication/WebPage, BreadcrumbList, FAQPage = FAQ visible)
  ✓ /intereses-demora-comerciales/ – SEO: Organization + WebSite en JSON-LD, Article con fechas ISO en guías, <img> con alt, <time> ISO
  ✓ /intereses-demora-comerciales/ – meta: title ≤ 70, description 70–160, canonical, hreflang es/x-default, OG, un H1, lang=es
  ✓ /intereses-demora-comerciales/ – seguridad y rendimiento: CSP, CSS inline, sin style=, sin scripts inline salvo tema/JSON-LD, sin CDN
  ✓ /intereses-demora-comerciales/ – accesibilidad: campos con etiqueta, botones con texto
  ✓ /intereses-demora-comerciales/ – enlaces visibles a privacidad, aviso legal, contacto y sobre nosotros
  ✓ /intereses-demora-comerciales/ – contenido útil bajo la herramienta ≥ 800 palabras (1669)
  ✓ /periodo-medio-pago-proveedores/ – enlaces internos existen (con BASE)
  ✓ /periodo-medio-pago-proveedores/ – anclas #id existen y no hay id duplicados
  ✓ /periodo-medio-pago-proveedores/ – JSON-LD válido (WebApplication/WebPage, BreadcrumbList, FAQPage = FAQ visible)
  ✓ /periodo-medio-pago-proveedores/ – SEO: Organization + WebSite en JSON-LD, Article con fechas ISO en guías, <img> con alt, <time> ISO
  ✓ /periodo-medio-pago-proveedores/ – meta: title ≤ 70, description 70–160, canonical, hreflang es/x-default, OG, un H1, lang=es
  ✓ /periodo-medio-pago-proveedores/ – seguridad y rendimiento: CSP, CSS inline, sin style=, sin scripts inline salvo tema/JSON-LD, sin CDN
  ✓ /periodo-medio-pago-proveedores/ – accesibilidad: campos con etiqueta, botones con texto
  ✓ /periodo-medio-pago-proveedores/ – enlaces visibles a privacidad, aviso legal, contacto y sobre nosotros
  ✓ /periodo-medio-pago-proveedores/ – contenido útil bajo la herramienta ≥ 800 palabras (1935)
  ✓ /privacidad/ – enlaces internos existen (con BASE)
  ✓ /privacidad/ – anclas #id existen y no hay id duplicados
  ✓ /privacidad/ – JSON-LD válido (WebApplication/WebPage, BreadcrumbList, FAQPage = FAQ visible)
  ✓ /privacidad/ – SEO: Organization + WebSite en JSON-LD, Article con fechas ISO en guías, <img> con alt, <time> ISO
  ✓ /privacidad/ – meta: title ≤ 70, description 70–160, canonical, hreflang es/x-default, OG, un H1, lang=es
  ✓ /privacidad/ – seguridad y rendimiento: CSP, CSS inline, sin style=, sin scripts inline salvo tema/JSON-LD, sin CDN
  ✓ /privacidad/ – accesibilidad: campos con etiqueta, botones con texto
  ✓ /privacidad/ – enlaces visibles a privacidad, aviso legal, contacto y sobre nosotros
  ✓ /sobre-nosotros/ – enlaces internos existen (con BASE)
  ✓ /sobre-nosotros/ – anclas #id existen y no hay id duplicados
  ✓ /sobre-nosotros/ – JSON-LD válido (WebApplication/WebPage, BreadcrumbList, FAQPage = FAQ visible)
  ✓ /sobre-nosotros/ – SEO: Organization + WebSite en JSON-LD, Article con fechas ISO en guías, <img> con alt, <time> ISO
  ✓ /sobre-nosotros/ – meta: title ≤ 70, description 70–160, canonical, hreflang es/x-default, OG, un H1, lang=es
  ✓ /sobre-nosotros/ – seguridad y rendimiento: CSP, CSS inline, sin style=, sin scripts inline salvo tema/JSON-LD, sin CDN
  ✓ /sobre-nosotros/ – accesibilidad: campos con etiqueta, botones con texto
  ✓ /sobre-nosotros/ – enlaces visibles a privacidad, aviso legal, contacto y sobre nosotros
  ✓ /validar-qr-verifactu/ – enlaces internos existen (con BASE)
  ✓ /validar-qr-verifactu/ – anclas #id existen y no hay id duplicados
  ✓ /validar-qr-verifactu/ – JSON-LD válido (WebApplication/WebPage, BreadcrumbList, FAQPage = FAQ visible)
  ✓ /validar-qr-verifactu/ – SEO: Organization + WebSite en JSON-LD, Article con fechas ISO en guías, <img> con alt, <time> ISO
  ✓ /validar-qr-verifactu/ – meta: title ≤ 70, description 70–160, canonical, hreflang es/x-default, OG, un H1, lang=es
  ✓ /validar-qr-verifactu/ – seguridad y rendimiento: CSP, CSS inline, sin style=, sin scripts inline salvo tema/JSON-LD, sin CDN
  ✓ /validar-qr-verifactu/ – accesibilidad: campos con etiqueta, botones con texto
  ✓ /validar-qr-verifactu/ – enlaces visibles a privacidad, aviso legal, contacto y sobre nosotros
  ✓ /validar-qr-verifactu/ – contenido útil bajo la herramienta ≥ 800 palabras (1320)
  ✓ Ninguna página afirma importes de sanciones
  ✓ Portada: muestra 1/1/2027, 1/7/2027, octubre 2028, «Última comprobación: 13 de noviembre de 2026» y enlaza BOE + nota de Hacienda
  ✓ Huella: los tres resultados oficiales aparecen en la página
  ✓ Navegación: las 8 herramientas y Guías en la cabecera de cada página
  ✓ Factura B2B: 6/10/2027, 6/10/2028, 6/10/2029, «Última comprobación: 13 de noviembre de 2026», enlaces BOE RD 238/2026 y Orden HAC/1028/2026, art. 12 de 4 días
  ✓ PMP: cita BOE-A-2016-1112, las tres fórmulas del art. 5, el ejemplo (47,60) y el límite de 60 días
  ✓ Intereses de demora: tabla con las 27 resoluciones del BOE (2013-2 a 2026-2), 10,40 %, art. 8.1 citado literalmente y TJUE C-585/20
  ✓ Las tres herramientas B2B cargan b2b.js y su script propio
  ✓ Ningún importe de sanción en la sección B2B (solo se citarían literalmente del BOE)
  ✓ JS de producción minificado y sin eval
  ✓ Search Console: meta google-site-verification solo en la portada cuando se compila con VF_GSV

Palabras en el cuerpo de cada página:
     268  /404.html
     309  /aviso-legal/
    1342  /blog/calcular-periodo-medio-pago-proveedores-ejemplo/
    1471  /blog/diferencias-verifactu-factura-electronica-b2b/
    1325  /blog/factura-electronica-obligatoria-autonomos/
    1242  /blog/fechas-verifactu-2027-2028/
     536  /blog/
    1560  /blog/plazos-pago-ley-morosidad/
    1164  /blog/tamano-posicion-qr-verifactu/
    1697  /blog/verifactu-autonomos/
    1117  /blog/verifactu-gratis-aplicacion-aeat/
    1317  /calcular-huella-verifactu/
     139  /contacto/
    1297  /ejemplo-xml-verifactu/
    1779  /factura-electronica-obligatoria/
    1409  /generador-qr-verifactu/
    1739  /
    1669  /intereses-demora-comerciales/
    1935  /periodo-medio-pago-proveedores/
     329  /privacidad/
     494  /sobre-nosotros/
    1320  /validar-qr-verifactu/

Resultado: 205 correctas, 0 fallidas
```

## browser-csp
```
  ✓ / – CSS inline aplicado (light)
  ✓ / – la herramienta funciona en Chromium
  ✓ / – conmutador de tema (light → dark, fondo rgb(11, 18, 32))
  ✓ / – sin errores JS ni violaciones CSP
  ✓ / [móvil 375px] – sin desbordamiento horizontal (scrollWidth 375)
  ✓ / [móvil 375px] – menú móvil se abre
  ✓ / [móvil 375px] – sin errores JS ni violaciones CSP
  ✓ /generador-qr-verifactu/ – CSS inline aplicado (light)
  ✓ /generador-qr-verifactu/ – la herramienta funciona en Chromium
  ✓ /generador-qr-verifactu/ – conmutador de tema (light → dark, fondo rgb(11, 18, 32))
  ✓ /generador-qr-verifactu/ – sin errores JS ni violaciones CSP
  ✓ /generador-qr-verifactu/ [móvil 375px] – sin desbordamiento horizontal (scrollWidth 375)
  ✓ /generador-qr-verifactu/ [móvil 375px] – menú móvil se abre
  ✓ /generador-qr-verifactu/ [móvil 375px] – vista previa A4 cabe en móvil (375)
  ✓ /generador-qr-verifactu/ [móvil 375px] – sin errores JS ni violaciones CSP
  ✓ /validar-qr-verifactu/ – CSS inline aplicado (light)
  ✓ /validar-qr-verifactu/ – la herramienta funciona en Chromium
  ✓ /validar-qr-verifactu/ – conmutador de tema (light → dark, fondo rgb(11, 18, 32))
  ✓ /validar-qr-verifactu/ – sin errores JS ni violaciones CSP
  ✓ /validar-qr-verifactu/ [móvil 375px] – sin desbordamiento horizontal (scrollWidth 375)
  ✓ /validar-qr-verifactu/ [móvil 375px] – menú móvil se abre
  ✓ /validar-qr-verifactu/ [móvil 375px] – sin errores JS ni violaciones CSP
  ✓ /calcular-huella-verifactu/ – CSS inline aplicado (light)
  ✓ /calcular-huella-verifactu/ – la herramienta funciona en Chromium
  ✓ /calcular-huella-verifactu/ – conmutador de tema (light → dark, fondo rgb(11, 18, 32))
  ✓ /calcular-huella-verifactu/ – sin errores JS ni violaciones CSP
  ✓ /calcular-huella-verifactu/ [móvil 375px] – sin desbordamiento horizontal (scrollWidth 375)
  ✓ /calcular-huella-verifactu/ [móvil 375px] – menú móvil se abre
  ✓ /calcular-huella-verifactu/ [móvil 375px] – sin errores JS ni violaciones CSP
  ✓ /ejemplo-xml-verifactu/ – CSS inline aplicado (light)
  ✓ /ejemplo-xml-verifactu/ – la herramienta funciona en Chromium
  ✓ /ejemplo-xml-verifactu/ – conmutador de tema (light → dark, fondo rgb(11, 18, 32))
  ✓ /ejemplo-xml-verifactu/ – sin errores JS ni violaciones CSP
  ✓ /ejemplo-xml-verifactu/ [móvil 375px] – sin desbordamiento horizontal (scrollWidth 375)
  ✓ /ejemplo-xml-verifactu/ [móvil 375px] – menú móvil se abre
  ✓ /ejemplo-xml-verifactu/ [móvil 375px] – sin errores JS ni violaciones CSP
  ✓ /factura-electronica-obligatoria/ – CSS inline aplicado (light)
  ✓ /factura-electronica-obligatoria/ – la herramienta funciona en Chromium
  ✓ /factura-electronica-obligatoria/ – conmutador de tema (light → dark, fondo rgb(11, 18, 32))
  ✓ /factura-electronica-obligatoria/ – sin errores JS ni violaciones CSP
  ✓ /factura-electronica-obligatoria/ [móvil 375px] – sin desbordamiento horizontal (scrollWidth 375)
  ✓ /factura-electronica-obligatoria/ [móvil 375px] – menú móvil se abre
  ✓ /factura-electronica-obligatoria/ [móvil 375px] – sin errores JS ni violaciones CSP
  ✓ /periodo-medio-pago-proveedores/ – CSS inline aplicado (light)
  ✓ /periodo-medio-pago-proveedores/ – la herramienta funciona en Chromium
  ✓ /periodo-medio-pago-proveedores/ – conmutador de tema (light → dark, fondo rgb(11, 18, 32))
  ✓ /periodo-medio-pago-proveedores/ – sin errores JS ni violaciones CSP
  ✓ /periodo-medio-pago-proveedores/ [móvil 375px] – sin desbordamiento horizontal (scrollWidth 375)
  ✓ /periodo-medio-pago-proveedores/ [móvil 375px] – menú móvil se abre
  ✓ /periodo-medio-pago-proveedores/ [móvil 375px] – sin errores JS ni violaciones CSP
  ✓ /intereses-demora-comerciales/ – CSS inline aplicado (light)
  ✓ /intereses-demora-comerciales/ – la herramienta funciona en Chromium
  ✓ /intereses-demora-comerciales/ – conmutador de tema (light → dark, fondo rgb(11, 18, 32))
  ✓ /intereses-demora-comerciales/ – sin errores JS ni violaciones CSP
  ✓ /intereses-demora-comerciales/ [móvil 375px] – sin desbordamiento horizontal (scrollWidth 375)
  ✓ /intereses-demora-comerciales/ [móvil 375px] – menú móvil se abre
  ✓ /intereses-demora-comerciales/ [móvil 375px] – sin errores JS ni violaciones CSP
  ✓ /blog/ – CSS inline aplicado (light)
  ✓ /blog/ – conmutador de tema (light → dark, fondo rgb(11, 18, 32))
  ✓ /blog/ – sin errores JS ni violaciones CSP
  ✓ /blog/ [móvil 375px] – sin desbordamiento horizontal (scrollWidth 375)
  ✓ /blog/ [móvil 375px] – menú móvil se abre
  ✓ /blog/ [móvil 375px] – sin errores JS ni violaciones CSP
  ✓ /blog/fechas-verifactu-2027-2028/ – CSS inline aplicado (light)
  ✓ /blog/fechas-verifactu-2027-2028/ – conmutador de tema (light → dark, fondo rgb(11, 18, 32))
  ✓ /blog/fechas-verifactu-2027-2028/ – sin errores JS ni violaciones CSP
  ✓ /blog/fechas-verifactu-2027-2028/ [móvil 375px] – sin desbordamiento horizontal (scrollWidth 375)
  ✓ /blog/fechas-verifactu-2027-2028/ [móvil 375px] – menú móvil se abre
  ✓ /blog/fechas-verifactu-2027-2028/ [móvil 375px] – sin errores JS ni violaciones CSP
  ✓ /blog/verifactu-gratis-aplicacion-aeat/ – CSS inline aplicado (light)
  ✓ /blog/verifactu-gratis-aplicacion-aeat/ – conmutador de tema (light → dark, fondo rgb(11, 18, 32))
  ✓ /blog/verifactu-gratis-aplicacion-aeat/ – sin errores JS ni violaciones CSP
  ✓ /blog/verifactu-gratis-aplicacion-aeat/ [móvil 375px] – sin desbordamiento horizontal (scrollWidth 375)
  ✓ /blog/verifactu-gratis-aplicacion-aeat/ [móvil 375px] – menú móvil se abre
  ✓ /blog/verifactu-gratis-aplicacion-aeat/ [móvil 375px] – sin errores JS ni violaciones CSP
  ✓ /blog/tamano-posicion-qr-verifactu/ – CSS inline aplicado (light)
  ✓ /blog/tamano-posicion-qr-verifactu/ – conmutador de tema (light → dark, fondo rgb(11, 18, 32))
  ✓ /blog/tamano-posicion-qr-verifactu/ – sin errores JS ni violaciones CSP
  ✓ /blog/tamano-posicion-qr-verifactu/ [móvil 375px] – sin desbordamiento horizontal (scrollWidth 375)
  ✓ /blog/tamano-posicion-qr-verifactu/ [móvil 375px] – menú móvil se abre
  ✓ /blog/tamano-posicion-qr-verifactu/ [móvil 375px] – sin errores JS ni violaciones CSP
  ✓ /blog/diferencias-verifactu-factura-electronica-b2b/ – CSS inline aplicado (light)
  ✓ /blog/diferencias-verifactu-factura-electronica-b2b/ – conmutador de tema (light → dark, fondo rgb(11, 18, 32))
  ✓ /blog/diferencias-verifactu-factura-electronica-b2b/ – sin errores JS ni violaciones CSP
  ✓ /blog/diferencias-verifactu-factura-electronica-b2b/ [móvil 375px] – sin desbordamiento horizontal (scrollWidth 375)
  ✓ /blog/diferencias-verifactu-factura-electronica-b2b/ [móvil 375px] – menú móvil se abre
  ✓ /blog/diferencias-verifactu-factura-electronica-b2b/ [móvil 375px] – sin errores JS ni violaciones CSP
  ✓ /blog/factura-electronica-obligatoria-autonomos/ – CSS inline aplicado (light)
  ✓ /blog/factura-electronica-obligatoria-autonomos/ – conmutador de tema (light → dark, fondo rgb(11, 18, 32))
  ✓ /blog/factura-electronica-obligatoria-autonomos/ – sin errores JS ni violaciones CSP
  ✓ /blog/factura-electronica-obligatoria-autonomos/ [móvil 375px] – sin desbordamiento horizontal (scrollWidth 375)
  ✓ /blog/factura-electronica-obligatoria-autonomos/ [móvil 375px] – menú móvil se abre
  ✓ /blog/factura-electronica-obligatoria-autonomos/ [móvil 375px] – sin errores JS ni violaciones CSP
  ✓ /blog/calcular-periodo-medio-pago-proveedores-ejemplo/ – CSS inline aplicado (light)
  ✓ /blog/calcular-periodo-medio-pago-proveedores-ejemplo/ – conmutador de tema (light → dark, fondo rgb(11, 18, 32))
  ✓ /blog/calcular-periodo-medio-pago-proveedores-ejemplo/ – sin errores JS ni violaciones CSP
  ✓ /blog/calcular-periodo-medio-pago-proveedores-ejemplo/ [móvil 375px] – sin desbordamiento horizontal (scrollWidth 375)
  ✓ /blog/calcular-periodo-medio-pago-proveedores-ejemplo/ [móvil 375px] – menú móvil se abre
  ✓ /blog/calcular-periodo-medio-pago-proveedores-ejemplo/ [móvil 375px] – sin errores JS ni violaciones CSP
  ✓ /blog/verifactu-autonomos/ – CSS inline aplicado (light)
  ✓ /blog/verifactu-autonomos/ – conmutador de tema (light → dark, fondo rgb(11, 18, 32))
  ✓ /blog/verifactu-autonomos/ – sin errores JS ni violaciones CSP
  ✓ /blog/verifactu-autonomos/ [móvil 375px] – sin desbordamiento horizontal (scrollWidth 375)
  ✓ /blog/verifactu-autonomos/ [móvil 375px] – menú móvil se abre
  ✓ /blog/verifactu-autonomos/ [móvil 375px] – sin errores JS ni violaciones CSP
  ✓ /blog/plazos-pago-ley-morosidad/ – CSS inline aplicado (light)
  ✓ /blog/plazos-pago-ley-morosidad/ – conmutador de tema (light → dark, fondo rgb(11, 18, 32))
  ✓ /blog/plazos-pago-ley-morosidad/ – sin errores JS ni violaciones CSP
  ✓ /blog/plazos-pago-ley-morosidad/ [móvil 375px] – sin desbordamiento horizontal (scrollWidth 375)
  ✓ /blog/plazos-pago-ley-morosidad/ [móvil 375px] – menú móvil se abre
  ✓ /blog/plazos-pago-ley-morosidad/ [móvil 375px] – sin errores JS ni violaciones CSP
  ✓ /sobre-nosotros/ – CSS inline aplicado (light)
  ✓ /sobre-nosotros/ – conmutador de tema (light → dark, fondo rgb(11, 18, 32))
  ✓ /sobre-nosotros/ – sin errores JS ni violaciones CSP
  ✓ /sobre-nosotros/ [móvil 375px] – sin desbordamiento horizontal (scrollWidth 375)
  ✓ /sobre-nosotros/ [móvil 375px] – menú móvil se abre
  ✓ /sobre-nosotros/ [móvil 375px] – sin errores JS ni violaciones CSP
  ✓ /contacto/ – CSS inline aplicado (light)
  ✓ /contacto/ – conmutador de tema (light → dark, fondo rgb(11, 18, 32))
  ✓ /contacto/ – sin errores JS ni violaciones CSP
  ✓ /contacto/ [móvil 375px] – sin desbordamiento horizontal (scrollWidth 375)
  ✓ /contacto/ [móvil 375px] – menú móvil se abre
  ✓ /contacto/ [móvil 375px] – sin errores JS ni violaciones CSP
  ✓ /aviso-legal/ – CSS inline aplicado (light)
  ✓ /aviso-legal/ – conmutador de tema (light → dark, fondo rgb(11, 18, 32))
  ✓ /aviso-legal/ – sin errores JS ni violaciones CSP
  ✓ /aviso-legal/ [móvil 375px] – sin desbordamiento horizontal (scrollWidth 375)
  ✓ /aviso-legal/ [móvil 375px] – menú móvil se abre
  ✓ /aviso-legal/ [móvil 375px] – sin errores JS ni violaciones CSP
  ✓ /privacidad/ – CSS inline aplicado (light)
  ✓ /privacidad/ – conmutador de tema (light → dark, fondo rgb(11, 18, 32))
  ✓ /privacidad/ – sin errores JS ni violaciones CSP
  ✓ /privacidad/ [móvil 375px] – sin desbordamiento horizontal (scrollWidth 375)
  ✓ /privacidad/ [móvil 375px] – menú móvil se abre
  ✓ /privacidad/ [móvil 375px] – sin errores JS ni violaciones CSP
  ✓ /no-existe/ – CSS inline aplicado (light)
  ✓ /no-existe/ – la herramienta funciona en Chromium
  ✓ /no-existe/ – responde 404 con la página 404
  ✓ /no-existe/ – conmutador de tema (light → dark, fondo rgb(11, 18, 32))
  ✓ /no-existe/ – sin errores JS ni violaciones CSP
  ✓ /no-existe/ [móvil 375px] – sin desbordamiento horizontal (scrollWidth 375)
  ✓ /no-existe/ [móvil 375px] – menú móvil se abre
  ✓ /no-existe/ [móvil 375px] – sin errores JS ni violaciones CSP

Resultado: 143 correctas, 0 fallidas
```
