# QA – Herramientas Verifactu, 2026-11-13

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
  ✓ checkAltaXml: XML mal formado
  ✓ checkChain: ejemplos AEAT en XML → cadena correcta
  ✓ checkChain: registros generados encadenados (b1 → b2) correctos
  ✓ checkChain: importe 123.4 vs 123.40 → aviso de decimales, no error

Resultado: 42 correctas, 0 fallidas
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
Sitio: https://mydevspace2.github.io/herramientas-verifactu (BASE «/herramientas-verifactu») – 14 páginas HTML

Palabras en el cuerpo de cada página:
     205  /404.html
     309  /aviso-legal/
    1149  /blog/fechas-verifactu-2027-2028/
     312  /blog/
    1070  /blog/tamano-posicion-qr-verifactu/
    1023  /blog/verifactu-gratis-aplicacion-aeat/
    1255  /calcular-huella-verifactu/
     139  /contacto/
    1234  /ejemplo-xml-verifactu/
    1347  /generador-qr-verifactu/
    1516  /
     329  /privacidad/
     431  /sobre-nosotros/
    1264  /validar-qr-verifactu/

Resultado: 112 correctas, 0 fallidas
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

Resultado: 92 correctas, 0 fallidas
```
