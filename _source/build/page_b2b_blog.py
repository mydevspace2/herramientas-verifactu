# -*- coding: utf-8 -*-
"""Guías de la sección factura electrónica B2B y morosidad (palabras clave de work/niches/raw/es_b2b.txt)."""
import sources as S

POSTS = []

POSTS.append(dict(
    slug="diferencias-verifactu-factura-electronica-b2b",
    title="Verifactu y factura electrónica B2B: diferencias y fechas",
    desc="Diferencias entre Verifactu (Ley Antifraude) y la factura electrónica B2B (Ley Crea y Crece): qué regula cada una, a quién afecta y desde cuándo.",
    h1="Verifactu y factura electrónica B2B (Ley Crea y Crece): diferencias",
    intro="Son dos obligaciones distintas que se solapan en el tiempo y se confunden a menudo. Esta guía compara qué exige cada una, quién está obligado y cuándo, con las fuentes del BOE. Revisada el 13 de noviembre de 2026.",
    content="""
<p class="note"><strong>Respuesta corta:</strong> Verifactu (Ley 11/2021 «Antifraude» y RD 1007/2023) obliga a que el <em>programa</em> con el que emites facturas sea inalterable, genere registros con huella y ponga un QR tributario. La factura electrónica B2B (Ley 18/2022 «Crea y Crece» y RD 238/2026) obliga a que la <em>factura</em> entre empresas sea un fichero estructurado, se intercambie por plataformas o por la solución pública de la AEAT y que el cliente informe de cuándo la paga. Una empresa puede tener que cumplir las dos.</p>

<h2 id="tabla">Comparativa rápida</h2>
<div class="table-wrap"><table>
<thead><tr><th></th><th>Verifactu</th><th>Factura electrónica B2B</th></tr></thead>
<tbody>
<tr><td>Ley de origen</td><td>Ley 11/2021, de medidas de prevención y lucha contra el fraude fiscal («Ley Antifraude»)</td><td>Ley 18/2022, de creación y crecimiento de empresas («Ley Crea y Crece»)</td></tr>
<tr><td>Reglamento</td><td>Real Decreto 1007/2023 y Orden HAC/1177/2024</td><td>Real Decreto 238/2026 y Orden HAC/1028/2026</td></tr>
<tr><td>Finalidad</td><td>Tributaria: evitar el software de doble uso y la manipulación de la facturación</td><td>Mercantil: combatir la morosidad y digitalizar el intercambio de facturas</td></tr>
<tr><td>Qué regula</td><td>El sistema informático de facturación: registros, huella SHA-256, QR, envío a la AEAT o conservación firmada</td><td>El formato de la factura (EN 16931: UBL, CII, EDIFACT o Facturae), su intercambio y los estados de pago</td></tr>
<tr><td>Operaciones</td><td>Todas las facturas emitidas con programa, también a particulares y tiques</td><td>Solo facturas a empresarios y profesionales establecidos en España; los tiques no cualificados quedan fuera</td></tr>
<tr><td>Fechas en el BOE</td><td>Antes del 1/1/2027 (sociedades) y del 1/7/2027 (resto); Hacienda anunció su intención de aplazarlo a octubre de 2028, sin norma publicada a 13/11/2026</td><td>6/10/2027 (más de 8 M€ de volumen de operaciones) y 6/10/2028 (resto); estados y pagos de autónomos ≤ 8 M€, 6/10/2029</td></tr>
<tr><td>Quién queda fuera</td><td>Quien lleva el SII, domicilio fiscal en País Vasco o Navarra, quien factura solo a mano</td><td>Quien solo vende a particulares o emite solo tiques no cualificados</td></tr>
<tr><td>Herramienta gratuita de la AEAT</td><td>Aplicación de facturación VERI*FACTU (ya disponible)</td><td>Solución pública de facturación electrónica y un formulario gratuito (DA 1.ª del RD 238/2026)</td></tr>
</tbody></table></div>

<h2 id="verifactu">Verifactu: el programa de facturación</h2>
<p>Verifactu no cambia el formato que recibe tu cliente: puedes seguir mandando un PDF o imprimiendo un tique. Lo que cambia es el software que usas para expedirlo, que debe generar un <strong>registro de facturación</strong> por cada factura, encadenado al anterior con una <a href="/calcular-huella-verifactu/">huella SHA-256</a>, y poner en la factura un <a href="/generador-qr-verifactu/">QR tributario</a> con el que cualquiera puede cotejarla en la sede de la AEAT. En la modalidad VERI*FACTU el programa envía cada registro a la AEAT al emitir la factura; en la modalidad no VERI*FACTU los guarda firmados. Afecta a sociedades, autónomos y demás obligados que facturan con programa, vendan a empresas o a particulares. Si quieres saber si te afecta, usa el <a href="/">test «¿estoy obligado a Verifactu?»</a>.</p>

<h2 id="b2b">Factura electrónica B2B: el documento y el pago</h2>
<p>La factura electrónica obligatoria va un paso más allá en el formato: entre empresas ya no valdrá un PDF, sino un <strong>mensaje estructurado</strong> conforme a la norma europea EN 16931 en una de las cuatro sintaxis admitidas por el artículo 7 del RD 238/2026. Se intercambiará por plataformas privadas interconectadas o por la solución pública de la AEAT (que usa UBL), que además recibe una copia fiel de las facturas. Y el cliente debe informar de si acepta o rechaza la factura y, sobre todo, de la <strong>fecha en que la paga</strong>, en un máximo de cuatro días naturales excluyendo sábados, domingos y festivos nacionales (arts. 10.3 y 12.3). Con esos datos, la AEAT facilitará el seguimiento de los plazos de pago y el listado de empresas que incumplen la Ley de morosidad (art. 14). Consulta las fechas exactas y haz el test en <a href="/factura-electronica-obligatoria/">factura electrónica obligatoria B2B</a>.</p>

<h2 id="solapan">Dónde se solapan</h2>
<p>Las dos normas afectan a la misma factura cuando una sociedad o un autónomo emite, con un programa, una factura completa a otra empresa española. En ese caso el programa tendrá que generar el registro Verifactu y el QR y, además, emitir la factura en formato estructurado y gestionar su envío y sus estados. La nota de Hacienda del 5 de octubre de 2026 explica precisamente que se quiere aplazar Verifactu a octubre de 2028 para hacerlo coincidir con la factura electrónica de las empresas de hasta 8 millones de euros, pero ese aplazamiento todavía no está en el BOE: lo detallamos en <a href="/blog/fechas-verifactu-2027-2028/">fechas de Verifactu: 2027 en el BOE y 2028 anunciado</a>.</p>
<p>¿Cumplir una significa cumplir la otra? No. Un programa Verifactu que solo genera PDF no cumple la factura electrónica B2B, y una plataforma de factura electrónica que no genera registros con huella no cumple Verifactu. Pregunta a tu proveedor de software qué cubre y desde qué versión.</p>

<h2 id="morosidad">El hilo común con la morosidad</h2>
<p>La Ley Crea y Crece también reforzó la información sobre plazos de pago en las cuentas anuales: las sociedades que no presentan cuentas abreviadas deben publicar el número e importe de facturas pagadas dentro del plazo legal y su porcentaje. Puedes calcularlo, junto con el <a href="/periodo-medio-pago-proveedores/">periodo medio de pago a proveedores</a> del método ICAC, con nuestra calculadora. Y si te pagan tarde, la <a href="/intereses-demora-comerciales/">calculadora de intereses de demora</a> aplica los tipos del BOE y la compensación de 40 euros por factura.</p>

<h2 id="checklist">Lista de comprobación</h2>
<ul class="checklist">
<li class="must"><span class="when">Verifactu</span>¿Uso un programa para facturar? ¿Está adaptado y en qué modalidad? ¿Lleva el QR?</li>
<li class="must"><span class="when">Factura B2B</span>¿Facturo a empresas españolas? ¿Cuál fue mi volumen de operaciones el año anterior? ¿Mi software o plataforma emitirá en un formato EN 16931 y enviará la copia fiel?</li>
<li class="must"><span class="when">Pagos</span>¿Puedo informar cada pago a mis proveedores en cuatro días laborables? ¿Cumplo los 60 días máximos?</li>
<li class="pending"><span class="when">Pendiente</span>Vigilar la publicación en el BOE del aplazamiento de Verifactu.</li>
</ul>
""",
    faq=[
        ("¿Verifactu y la factura electrónica son lo mismo?", "No. Verifactu regula el software de facturación (registros, huella y QR) por motivos fiscales; la factura electrónica B2B regula el formato y el intercambio de las facturas entre empresas y la comunicación de los pagos."),
        ("¿Qué diferencia hay entre la Ley Antifraude y la Ley Crea y Crece?", "La Ley 11/2021 (Antifraude) dio origen a Verifactu y busca evitar la manipulación de la facturación. La Ley 18/2022 (Crea y Crece) impuso la factura electrónica entre empresas para luchar contra la morosidad."),
        ("¿Si cumplo Verifactu ya cumplo la factura electrónica?", "No necesariamente. Un PDF con QR Verifactu no es una factura electrónica estructurada. Necesitarás que tu software emita además en un formato EN 16931 (UBL, CII, EDIFACT o Facturae) o usar la solución pública de la AEAT."),
        ("¿Qué obligación llega antes?", "Según el BOE, Verifactu: antes del 1/1/2027 para sociedades y del 1/7/2027 para el resto (con un aplazamiento a octubre de 2028 anunciado pero no publicado). La factura electrónica B2B empieza el 6/10/2027 para quien supera 8 M€ y el 6/10/2028 para el resto."),
        ("¿La factura electrónica B2B afecta a las ventas a particulares?", "No. Solo a las facturas emitidas a empresarios y profesionales establecidos en España. Verifactu, en cambio, sí afecta a todas las facturas y tiques emitidos con programa."),
    ],
    sources=[S.RD238, S.ORDEN1028, S.AEAT_CAL, S.RD, S.NOTA, S.LEY18],
))

POSTS.append(dict(
    slug="factura-electronica-obligatoria-autonomos",
    title="Factura electrónica obligatoria para autónomos: cuándo empieza",
    desc="Cuándo es obligatoria la factura electrónica para autónomos: 6/10/2028 para emitir y recibir y 6/10/2029 para informar pagos. Excepciones y opción gratuita.",
    h1="Factura electrónica obligatoria para autónomos: cuándo y cómo",
    intro="Qué fechas aplican a los autónomos según el RD 238/2026, quién queda fuera y qué opciones gratuitas habrá. Revisado en el BOE el 13 de noviembre de 2026.",
    content="""
<p class="note"><strong>Respuesta corta:</strong> si eres autónomo y facturas a empresas o a otros autónomos, tendrás que emitir y recibir facturas electrónicas desde el <strong>6 de octubre de 2028</strong>, salvo que tu volumen de operaciones del año anterior supere 8 millones de euros (entonces, desde el 6 de octubre de 2027). La obligación de informar de los estados y pagos de las facturas que recibes no te será exigible hasta el <strong>6 de octubre de 2029</strong>.</p>

<h2 id="fechas">Las fechas para autónomos, con su base legal</h2>
<div class="table-wrap"><table>
<thead><tr><th>Obligación</th><th>Autónomo con volumen ≤ 8 M€</th><th>Base legal</th></tr></thead>
<tbody>
<tr><td>Emitir facturas electrónicas a empresas y profesionales</td><td>6 de octubre de 2028</td><td>RD 238/2026, DF 4.ª.1.b</td></tr>
<tr><td>Recibir facturas electrónicas de tus proveedores</td><td>6 de octubre de 2028</td><td>RD 238/2026, DF 4.ª.1.b</td></tr>
<tr><td>Informar aceptación, rechazo y pago de las facturas recibidas</td><td>6 de octubre de 2029 (hasta entonces, voluntario)</td><td>RD 238/2026, DT 3.ª</td></tr>
</tbody></table></div>
<p>Los plazos se cuentan desde la entrada en vigor de la Orden HAC/1028/2026, el 6 de octubre de 2026: 24 meses para el resto de empresarios y profesionales y 12 meses más para la información de estados de las personas físicas y entidades en régimen de atribución de rentas (comunidades de bienes, sociedades civiles) con volumen de operaciones de hasta 8 millones de euros. La AEAT confirma estas fechas en su <a href="https://sede.agenciatributaria.gob.es/Sede/iva/factura-electronica/calendario-implantacion.html" rel="noopener" target="_blank">calendario de implantación</a>. Comprueba tu caso con el <a href="/factura-electronica-obligatoria/">test de factura electrónica B2B</a>.</p>

<h2 id="quien">¿A qué autónomos afecta?</h2>
<p>A los que deben expedir factura según el Reglamento de facturación por operaciones con <strong>empresarios o profesionales establecidos en España</strong> (art. 3 del RD 238/2026). Da igual el régimen de IRPF (estimación directa u objetiva) o de IVA: el reglamento no los distingue. Lo que importa es a quién facturas y con qué documento.</p>
<h3>Cuándo no te afecta</h3>
<ul>
<li><strong>Solo vendes a particulares.</strong> Las facturas a consumidores finales no entran en esta obligación.</li>
<li><strong>Solo emites tiques (facturas simplificadas) no cualificados.</strong> El art. 4 los excluye. Si un cliente empresario te pide una factura completa o una simplificada cualificada, esa sí tendrá que ser electrónica.</li>
</ul>
<p>Aunque no emitas facturas electrónicas, desde tu fecha tendrás que <strong>recibir</strong> en formato electrónico las de tus proveedores que estén obligados.</p>

<h2 id="gratis">¿Habrá una opción gratuita?</h2>
<p>Sí. La disposición adicional primera del RD 238/2026 encarga a la AEAT una <strong>aplicación o formulario gratuito</strong> para que todos los empresarios y profesionales puedan expedir facturas electrónicas, generar la información sobre su estado (incluido el pago) y ponerla a disposición de sus clientes a través de la solución pública de facturación electrónica. El acceso a la solución pública y a sus usos es gratuito para los usuarios (art. 11.10). Para la otra obligación, Verifactu, la AEAT ya ofrece una aplicación de facturación gratuita: lo contamos en <a href="/blog/verifactu-gratis-aplicacion-aeat/">Verifactu gratis</a>.</p>

<h2 id="formato">¿Vale un PDF o un Excel?</h2>
<p>No. Una factura electrónica a efectos del RD 238/2026 es un mensaje estructurado que sigue el modelo semántico europeo EN 16931 en una de estas sintaxis: UBL, CII, EDIFACT o Facturae (art. 7). Un PDF, aunque se mande por correo, no lo es. Si usas una plataforma privada, las facturas deberán ir firmadas con firma electrónica avanzada (art. 7.3). Si usas la solución pública, se emitirán en UBL (art. 11.2).</p>

<h2 id="verifactu">¿Y Verifactu?</h2>
<p>Es otra obligación, con otras fechas. Según el BOE, los autónomos que facturan con programa deben tenerlo adaptado <strong>antes del 1 de julio de 2027</strong>; el 5 de octubre de 2026 Hacienda anunció que quiere aplazarlo a octubre de 2028, pero a 13 de noviembre de 2026 ese cambio no está publicado. Haz el <a href="/">test de Verifactu</a> y lee las <a href="/blog/diferencias-verifactu-factura-electronica-b2b/">diferencias entre Verifactu y la factura electrónica B2B</a>.</p>

<h2 id="pagos">Tus cobros: lo que gana el autónomo</h2>
<p>La factura electrónica B2B se creó para reducir la morosidad. Cuando tus clientes estén obligados, tendrán que informar de la fecha en que te pagan, y la AEAT podrá seguir los plazos de pago. Recuerda que el plazo legal es de 30 días desde la entrega si no se pacta otro, y nunca más de 60 (art. 4 de la Ley 3/2004). Si te pagan tarde, tienes derecho a intereses de demora y a 40 euros por factura: calcúlalos con la <a href="/intereses-demora-comerciales/">calculadora de intereses de demora</a>.</p>

<h2 id="pasos">Qué puedes hacer ya</h2>
<ol class="steps">
<li>Anota tu fecha: 6/10/2028 para emitir y recibir; 6/10/2029 para informar estados y pagos.</li>
<li>Pregunta a tu programa de facturación si emitirá en formato estructurado y cómo enviará las facturas.</li>
<li>Si facturas poco, sigue las novedades del formulario gratuito de la AEAT.</li>
<li>Revisa los plazos de pago que pactas con tus clientes.</li>
</ol>
""",
    faq=[
        ("¿Cuándo tienen que hacer factura electrónica los autónomos?", "Desde el 6 de octubre de 2028 si su volumen de operaciones no supera 8 millones de euros, y desde el 6 de octubre de 2027 si lo supera (RD 238/2026, DF 4.ª)."),
        ("¿Los autónomos en módulos están obligados a la factura electrónica?", "Sí, si deben expedir factura a empresarios o profesionales. El RD 238/2026 no distingue por el método de estimación del IRPF."),
        ("¿Qué autónomos están exentos de la factura electrónica?", "Los que solo venden a particulares y los que solo emiten facturas simplificadas no cualificadas (art. 4). Aun así, desde su fecha deberán poder recibir facturas electrónicas."),
        ("¿Cuándo tienen que informar los autónomos del pago de las facturas?", "Los autónomos con volumen de hasta 8 M€ no estarán obligados a informar de los estados y pagos hasta el 6 de octubre de 2029 (DT 3.ª); antes pueden hacerlo de forma voluntaria."),
        ("¿Habrá un programa gratuito de factura electrónica para autónomos?", "Sí. La DA 1.ª del RD 238/2026 obliga a la AEAT a desarrollar una aplicación o formulario gratuito para emitir facturas electrónicas e informar de su estado a través de la solución pública."),
        ("¿Una factura en PDF es una factura electrónica?", "No a efectos del RD 238/2026. Debe ser un mensaje estructurado EN 16931 en sintaxis UBL, CII, EDIFACT o Facturae."),
    ],
    sources=[S.RD238, S.ORDEN1028, S.AEAT_CAL, S.LEY3, S.RD, S.NOTA],
))

POSTS.append(dict(
    slug="calcular-periodo-medio-pago-proveedores-ejemplo",
    title="Cómo calcular el periodo medio de pago a proveedores: ejemplo",
    desc="Cómo calcular el periodo medio de pago a proveedores paso a paso: fórmula ICAC, ejemplo resuelto, Excel, memoria abreviada y diferencia con la morosidad.",
    h1="Cómo calcular el periodo medio de pago a proveedores, con ejemplo",
    intro="La fórmula del ICAC explicada con números, cómo hacerlo en Excel y cómo se calcula en la memoria abreviada. Con enlace a la calculadora gratuita.",
    content="""
<p class="note"><strong>Resumen:</strong> el periodo medio de pago a proveedores (PMP) es la media de días entre la entrega de los bienes o servicios y el pago, ponderada por el importe. En la memoria normal se calcula factura a factura con la fórmula del art. 5 de la <a href="https://www.boe.es/buscar/act.php?id=BOE-A-2016-1112" rel="noopener" target="_blank">Resolución del ICAC de 29/01/2016</a>; en la abreviada, con saldos y compras. Si prefieres no hacerlo a mano, usa la <a href="/periodo-medio-pago-proveedores/">calculadora del periodo medio de pago</a>.</p>

<h2 id="pasos">Paso a paso con la fórmula del ICAC</h2>
<ol class="steps">
<li><strong>Reúne las facturas de proveedores comerciales</strong> del ejercicio: las pagadas durante el año y las pendientes al cierre. Excluye lo que no sean operaciones comerciales (impuestos, Seguridad Social, préstamos) y las deudas retenidas por embargos o compensaciones (art. 3.3).</li>
<li><strong>Para cada factura, toma la fecha de inicio</strong>: recepción de la mercancía o prestación del servicio; si no la tienes con fiabilidad, la de recepción de la factura (art. 5.4).</li>
<li><strong>Calcula los días</strong>: para las pagadas, hasta la fecha de pago; para las pendientes, hasta el último día del ejercicio. Días naturales.</li>
<li><strong>Multiplica días × importe</strong> en cada factura.</li>
<li><strong>Calcula las dos ratios</strong>: suma de (días × importe) de las pagadas ÷ total pagado; lo mismo para las pendientes.</li>
<li><strong>Calcula el PMP</strong>: (ratio pagadas × total pagado + ratio pendientes × total pendiente) ÷ (total pagado + total pendiente).</li>
</ol>

<h2 id="ejemplo">Ejemplo resuelto</h2>
<p>Ejercicio que cierra el 31/12/2025:</p>
<div class="table-wrap"><table>
<thead><tr><th>Factura</th><th>Importe</th><th>Inicio</th><th>Pago</th><th>Días</th><th>Días × importe</th></tr></thead>
<tbody>
<tr><td>A-1</td><td>1.000,00</td><td>10/01/2025</td><td>09/02/2025</td><td>30</td><td>30.000</td></tr>
<tr><td>A-2</td><td>2.000,00</td><td>01/03/2025</td><td>10/05/2025</td><td>70</td><td>140.000</td></tr>
<tr><td>A-3</td><td>500,00</td><td>15/11/2025</td><td>pendiente</td><td>46</td><td>23.000</td></tr>
<tr><td>A-4</td><td>1.500,00</td><td>01/12/2025</td><td>20/01/2026 (tras el cierre)</td><td>30</td><td>45.000</td></tr>
</tbody></table></div>
<ul>
<li>Total pagado: 3.000 €. Ratio de operaciones pagadas: (30.000 + 140.000) ÷ 3.000 = <strong>56,67 días</strong>.</li>
<li>Total pendiente: 2.000 €. Ratio de operaciones pendientes: (23.000 + 45.000) ÷ 2.000 = <strong>34,00 días</strong>.</li>
<li>PMP: (56,67 × 3.000 + 34 × 2.000) ÷ 5.000 = <strong>47,60 días</strong>, por debajo del máximo legal de 60 días.</li>
</ul>
<p>Detalle importante: la factura A-4 se pagó en enero del año siguiente, pero a 31 de diciembre estaba pendiente, así que se trata como pendiente y sus días se cuentan hasta el cierre. Es un error frecuente contarla como pagada a 50 días.</p>

<h2 id="excel">Cómo hacerlo en Excel</h2>
<p>Con una tabla con las columnas Importe (B), Inicio (C), Pago (D) y la fecha de cierre en la celda H1:</p>
<ul>
<li><strong>Días</strong> (columna E): <code>=SI(Y(D2&lt;&gt;"";D2&lt;=$H$1);D2-C2;$H$1-C2)</code></li>
<li><strong>Pagada</strong> (columna F): <code>=Y(D2&lt;&gt;"";D2&lt;=$H$1)</code></li>
<li><strong>Ratio pagadas</strong>: <code>=SUMAPRODUCTO((F2:F100=VERDADERO)*E2:E100*B2:B100)/SUMAR.SI(F2:F100;VERDADERO;B2:B100)</code></li>
<li><strong>Ratio pendientes</strong>: igual con <code>FALSO</code>.</li>
<li><strong>PMP</strong>: <code>=SUMAPRODUCTO(E2:E100;B2:B100)/SUMA(B2:B100)</code> (equivale a la fórmula del ICAC, porque es la media de días ponderada por importe de todas las facturas).</li>
</ul>
<p>La última fórmula muestra algo útil: el PMP del ICAC es simplemente la media ponderada de todos los días. Las dos ratios sirven para separar lo pagado de lo pendiente en la memoria. Si tu hoja tiene filas vacías, filtra antes. Y si prefieres no pelearte con fórmulas, exporta tu tabla en CSV y súbela a la <a href="/periodo-medio-pago-proveedores/">calculadora PMP</a>, que además genera el cuadro de la memoria.</p>

<h2 id="abreviada">Cálculo en la memoria abreviada</h2>
<p>Si formulas memoria abreviada o aplicas el PGC de Pymes, la fórmula es: <strong>saldo medio de acreedores comerciales ÷ (compras netas + gastos por servicios exteriores) × 365</strong> (art. 5.5). Ejemplo: saldo de proveedores y acreedores comerciales de 40.000 € al inicio y 60.000 € al cierre (saldo medio de 50.000,00 €) y compras y servicios exteriores de 400.000 €: 50.000 ÷ 400.000 × 365 = <strong>45,63 días</strong>. En la memoria abreviada solo se informa de ese dato, para el ejercicio actual y el anterior (art. 6.3).</p>

<h2 id="memoria">La nota de la memoria</h2>
<p>En la memoria normal, la nota debe titularse «Información sobre el periodo medio de pago a proveedores. Disposición adicional tercera. "Deber de información" de la Ley 15/2010, de 5 de julio» e incluir, para N y N-1, el PMP, la ratio de operaciones pagadas y la de pendientes (en días) y el total de pagos realizados y pendientes (en euros). Las sociedades no cotizadas que no presentan cuentas abreviadas, y las cotizadas, deben añadir desde la Ley 18/2022 el número e importe de facturas pagadas en un periodo inferior al máximo legal y el porcentaje sobre el total.</p>

<h2 id="morosidad">Diferencia entre periodo medio de pago y morosidad</h2>
<p>El PMP es una <strong>media</strong> de días totales desde la entrega; la morosidad es el <strong>incumplimiento</strong> del plazo de cada factura concreta. Una empresa puede tener un PMP de 45 días y pagar varias facturas a 90, o al revés. Por eso la ley pide, además del PMP, cuántas facturas se pagaron dentro del plazo. Cada factura pagada tarde genera intereses de demora y 40 euros de compensación por costes de cobro (arts. 7 y 8 de la Ley 3/2004), que puedes estimar con la <a href="/intereses-demora-comerciales/">calculadora de intereses de demora</a>. Y no confundas este PMP con el de las Administraciones públicas: la resolución del ICAC excluye a las entidades del art. 2.1 de la Ley Orgánica 2/2012 (art. 2.1 de la resolución), que se rigen por su propia metodología.</p>
""",
    faq=[
        ("¿Cómo se calcula el periodo medio de pago a proveedores?", "Media de días entre la entrega y el pago ponderada por importe: (ratio pagadas × total pagado + ratio pendientes × total pendiente) ÷ total, según el art. 5 de la Resolución del ICAC de 29/01/2016."),
        ("¿Cómo se calcula el PMP en la memoria abreviada?", "Saldo medio de acreedores comerciales ÷ (compras netas + gastos por servicios exteriores) × 365 (art. 5.5)."),
        ("¿Una factura pagada después del cierre cuenta como pagada?", "No. Si a la fecha de cierre estaba pendiente, cuenta como pendiente y sus días se calculan hasta el último día del ejercicio."),
        ("¿Se puede calcular el PMP en Excel?", "Sí. El PMP equivale a SUMAPRODUCTO(días; importes) ÷ SUMA(importes), con los días hasta el pago o hasta el cierre si está pendiente. La guía incluye las fórmulas."),
        ("¿Qué diferencia hay entre periodo medio de pago y morosidad?", "El PMP es una media; la morosidad es el incumplimiento del plazo de cada factura. Por eso la ley pide además el número e importe de facturas pagadas dentro del plazo máximo."),
        ("¿Dónde se regula el periodo medio de pago a proveedores?", "En la DA 3.ª de la Ley 15/2010 (deber de información) y en la Resolución del ICAC de 29 de enero de 2016 (BOE-A-2016-1112), que fija las fórmulas y el contenido de la memoria."),
    ],
    sources=[S.ICAC, S.LEY15, S.LEY3],
))
