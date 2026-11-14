# -*- coding: utf-8 -*-
"""Guías long-tail del calendario SEO (work/verifactu/seo/blog-calendar.md). Publicadas el 13/11/2026.
Reglas: hechos citados al BOE o a la AEAT, «en el BOE» separado de «solo anunciado», ninguna cuantía de multa."""
import sources as S

POSTS = []

# ---------------------------------------------------------------- #1 verifactu autónomos
POSTS.append(dict(
    slug="verifactu-autonomos",
    published="2026-11-13",
    title="Verifactu para autónomos: cuándo es obligatorio y qué hacer",
    desc="¿Verifactu es obligatorio para autónomos? Fecha del BOE (antes del 1/7/2027), aplazamiento a 2028 solo anunciado, módulos, Excel, SII y opción gratuita.",
    h1="Verifactu para autónomos: cuándo es obligatorio y qué tienes que hacer",
    intro="Qué dice el Real Decreto 1007/2023 sobre los autónomos, qué fecha está en el BOE, qué se ha anunciado para 2028 y cómo prepararte sin gastar de más. Revisado en el BOE el 13 de noviembre de 2026.",
    content="""
<p class="note"><strong>Respuesta corta:</strong> sí, Verifactu es obligatorio para los autónomos que emiten sus facturas o tiques con un programa, una app, un TPV o una caja registradora, tributen en estimación directa o en módulos. Según el BOE, deben tener el sistema operativo <strong>antes del 1 de julio de 2027</strong>. Hacienda anunció el 5 de octubre de 2026 su intención de aplazarlo a <strong>octubre de 2028</strong>, pero a 13 de noviembre de 2026 ese aplazamiento no está publicado en el BOE. Quien factura solo a mano, quien lleva el SII o tiene su domicilio fiscal en el País Vasco o Navarra queda fuera del reglamento estatal.</p>
<p>¿Quieres saberlo en tu caso concreto? Responde las cuatro preguntas del <a href="/">test «¿Verifactu es obligatorio para mí?»</a>; tarda un minuto y no guarda ningún dato.</p>

<h2 id="por-que">Por qué Verifactu afecta a los autónomos</h2>
<p>El artículo 3.1 del Reglamento de sistemas informáticos de facturación (aprobado por el Real Decreto 1007/2023) enumera a quién se aplica. Su letra b) incluye a «los contribuyentes del Impuesto sobre la Renta de las Personas Físicas que desarrollen actividades económicas». Es decir, a todos los autónomos y profesionales, sin distinguir el método de estimación del rendimiento. La letra d) añade las entidades en régimen de atribución de rentas con actividad económica, como las comunidades de bienes y las sociedades civiles sin personalidad jurídica a efectos del Impuesto sobre Sociedades.</p>
<p>La condición decisiva no es el tipo de autónomo, sino la herramienta: el reglamento se aplica a quien «utilice sistemas informáticos de facturación, aunque solo los use para una parte de su actividad». Si haces la mayoría de tus facturas a mano pero los tiques del mostrador salen de un TPV, ese TPV tiene que cumplir.</p>

<h2 id="fechas">Fechas para autónomos: BOE frente a anuncio</h2>
<div class="table-wrap"><table>
<thead><tr><th>Situación</th><th>Fecha</th><th>¿Es norma?</th></tr></thead>
<tbody>
<tr><td>Autónomos, comunidades de bienes y no residentes con establecimiento permanente</td><td>Sistema operativo <strong>antes del 1 de julio de 2027</strong></td><td>Sí: disposición final 4.ª del RD 1007/2023, redacción del Real Decreto-ley 15/2025 (BOE)</td></tr>
<tr><td>Sociedades (Impuesto sobre Sociedades), como referencia</td><td>Antes del 1 de enero de 2027</td><td>Sí: misma disposición</td></tr>
<tr><td>Aplazamiento general</td><td>Octubre de 2028, sin día concreto</td><td><strong>No</strong>: solo una nota informativa de Hacienda del 5/10/2026</td></tr>
</tbody></table></div>
<p>Una nota de prensa no modifica un real decreto. Mientras no se publique en el BOE la norma que lo cambie, la fecha legal para un autónomo sigue siendo el 1 de julio de 2027. Lo contamos con todos los detalles en <a href="/blog/fechas-verifactu-2027-2028/">fechas de Verifactu: 2027 en el BOE y 2028 solo anunciado</a>, y revisamos el BOE cada vez que hay novedades.</p>

<h2 id="casos">Casos habituales de autónomos</h2>
<div class="table-wrap"><table>
<thead><tr><th>Tu situación</th><th>¿Te obliga Verifactu?</th><th>Por qué</th></tr></thead>
<tbody>
<tr><td>Estimación directa, facturas con un programa o app</td><td>Sí</td><td>Art. 3.1.b del reglamento</td></tr>
<tr><td>Módulos (estimación objetiva) con TPV o caja registradora</td><td>Sí</td><td>El art. 3.1.b no distingue el método de estimación</td></tr>
<tr><td>Recargo de equivalencia (comercio minorista) con TPV</td><td>Sí</td><td>El reglamento no excluye este régimen de IVA; lo determinante es usar un sistema informático</td></tr>
<tr><td>Facturas hechas a mano en un talonario</td><td>No</td><td>No usas un sistema informático de facturación</td></tr>
<tr><td>Excel o Word solo para escribir, imprimir y guardar facturas</td><td>No, según la AEAT</td><td>Preguntas frecuentes de la AEAT sobre el ámbito de aplicación</td></tr>
<tr><td>Excel con macros que generan el libro de facturas expedidas</td><td>Sí, según la AEAT</td><td>La hoja de cálculo pasa a ser un sistema de facturación</td></tr>
<tr><td>Llevas los libros de IVA por el SII</td><td>No</td><td>Art. 3.3 del reglamento</td></tr>
<tr><td>Domicilio fiscal en País Vasco o Navarra</td><td>No por el reglamento estatal</td><td>Se aplica la normativa foral (TicketBAI en el País Vasco)</td></tr>
</tbody></table></div>
<p>Hay además exclusiones por operaciones concretas en el artículo 4, por ejemplo las facturas de establecimientos permanentes situados en el extranjero. Son poco frecuentes en un autónomo: si crees que te afectan, confírmalo con tu asesor.</p>

<h2 id="que-cambia">Qué cambia en tu día a día</h2>
<p>Para el cliente, la factura sigue pareciendo una factura normal; el cambio está en el programa que la genera. En la práctica:</p>
<ol class="steps">
<li><strong>Un QR tributario</strong> al principio de cada factura o tique, de 30 a 40 mm, con el texto «QR tributario:» encima. Con él tu cliente puede cotejar la factura en la sede de la AEAT. Puedes ver cómo queda con nuestro <a href="/generador-qr-verifactu/">generador de QR Verifactu</a>.</li>
<li><strong>Un registro de facturación</strong> por cada factura emitida o anulada, que el programa encadena con el anterior mediante una huella SHA-256. No lo haces tú: lo hace el software. Si eres curioso o desarrollador, el <a href="/calcular-huella-verifactu/">calculador de huella</a> muestra cómo funciona.</li>
<li><strong>Una modalidad</strong>: VERI*FACTU (el programa envía cada registro a la AEAT al emitir la factura y la factura lleva esa leyenda) o no VERI*FACTU (los registros se guardan firmados y se entregan si la AEAT los pide). Para la mayoría de autónomos la primera es la más sencilla, porque el reglamento le simplifica otros requisitos.</li>
<li><strong>No poder borrar facturas sin dejar rastro</strong>: los errores se corrigen con anulaciones o facturas rectificativas, que también generan su registro.</li>
</ol>

<h2 id="gratis">¿Puedo cumplir Verifactu gratis siendo autónomo?</h2>
<p>Sí, en muchos casos. La AEAT ofrece una <strong>aplicación gratuita de facturación</strong> pensada para quien emite pocas facturas o tiene una facturación sencilla: genera facturas completas con el QR y envía los registros a la AEAT en modalidad VERI*FACTU. Su gran límite es que no emite facturas simplificadas (tiques), así que no sirve para un comercio o un bar que vende en mostrador. Lo explicamos paso a paso en <a href="/blog/verifactu-gratis-aplicacion-aeat/">Verifactu gratis: la aplicación de facturación de la AEAT</a>. Si ya pagas un programa de facturación, lo normal es que el proveedor lo adapte dentro de tu suscripción: pregúntale por escrito desde qué versión cumple y en qué modalidad.</p>

<h2 id="pasos">Lista de pasos para un autónomo</h2>
<ul class="checklist">
<li class="must"><span class="when">Hoy</span>Haz el <a href="/">test de obligación</a> y anota si te afecta y por qué.</li>
<li class="must"><span class="when">Este trimestre</span>Haz inventario de lo que usas para facturar: programa, app del banco, TPV, Excel con macros, plataforma de tu tienda online.</li>
<li class="must"><span class="when">Antes de 2027</span>Pide a cada proveedor un compromiso escrito de adaptación (fecha y modalidad). Si no lo hay, compara alternativas o valora la aplicación gratuita de la AEAT.</li>
<li class="must"><span class="when">Al adaptar</span>Emite una factura de prueba y comprueba su QR con el <a href="/validar-qr-verifactu/">validador de QR Verifactu</a>: dominio de la AEAT, NIF, fecha e importe.</li>
<li class="pending"><span class="when">Pendiente</span>Vigila si el aplazamiento a octubre de 2028 llega al BOE. Hasta entonces, la fecha legal es el 1 de julio de 2027.</li>
</ul>

<h2 id="b2b">No lo confundas con la factura electrónica obligatoria</h2>
<p>Verifactu no te obliga a mandar facturas en XML a tus clientes. Eso lo exige otra norma, el Real Decreto 238/2026 de factura electrónica entre empresarios, que para la mayoría de autónomos empieza el 6 de octubre de 2028. Son obligaciones distintas que pueden coincidir en la misma factura; lo resumimos en <a href="/blog/diferencias-verifactu-factura-electronica-b2b/">diferencias entre Verifactu y la factura electrónica B2B</a> y en la guía de <a href="/blog/factura-electronica-obligatoria-autonomos/">factura electrónica obligatoria para autónomos</a>.</p>
""",
    faq=[
        ("¿Verifactu es obligatorio para todos los autónomos?", "Para todos los que expiden facturas o tiques con un sistema informático (programa, app, TPV, caja registradora), según el art. 3.1.b del RD 1007/2023. No para quien factura solo a mano, quien lleva el SII o quien tiene el domicilio fiscal en el País Vasco o Navarra."),
        ("¿Cuándo entra en vigor Verifactu para autónomos?", "Según el BOE, los autónomos deben tener su sistema operativo antes del 1 de julio de 2027 (disposición final 4.ª del RD 1007/2023, redacción del RDL 15/2025). Hacienda anunció el 5/10/2026 un aplazamiento a octubre de 2028, pero a 13/11/2026 no está publicado en el BOE."),
        ("¿Los autónomos en módulos tienen que cumplir Verifactu?", "Sí, si emiten facturas o tiques con un sistema informático. El reglamento incluye a todos los contribuyentes del IRPF con actividades económicas, sin distinguir entre estimación directa y objetiva."),
        ("Si facturo con Excel, ¿me afecta Verifactu?", "Según las preguntas frecuentes de la AEAT, no si solo usas Excel o Word para escribir, imprimir y guardar las facturas. Sí si la hoja tiene macros u otras funciones que la convierten en un sistema de facturación, por ejemplo para generar el libro de facturas expedidas."),
        ("¿Tengo que comprar un programa nuevo?", "No necesariamente. Si tu programa actual se adapta, basta con actualizarlo. Si emites pocas facturas completas, la aplicación gratuita de la AEAT cumple Verifactu, aunque no emite tiques."),
        ("¿Verifactu me obliga a enviar mis facturas a Hacienda?", "Solo en la modalidad VERI*FACTU, y lo hace el programa automáticamente al emitir cada factura. En la modalidad no VERI*FACTU los registros se guardan firmados en tu sistema y se entregan si la AEAT los pide."),
    ],
    sources=[S.RD, S.RDL, S.NOTA, S.FAQ_AMB, S.APP_GUIA, S.AEAT],
))

# ---------------------------------------------------------------- #2 plazos ley de morosidad
POSTS.append(dict(
    slug="plazos-pago-ley-morosidad",
    published="2026-11-13",
    title="Plazos de pago de la Ley de morosidad: 30 y 60 días",
    desc="Plazo máximo de pago a proveedores según la Ley 3/2004: 30 días sin pacto, 60 como máximo, cómo se cuentan, facturas agrupadas, intereses y 40 euros.",
    h1="Plazos de pago de la Ley de morosidad: 30 días, 60 como máximo",
    intro="Qué plazo tiene tu cliente para pagarte una factura según la Ley 3/2004 de lucha contra la morosidad, cómo se cuenta y qué puedes reclamar si se pasa. Texto consolidado del BOE revisado el 13 de noviembre de 2026.",
    content="""
<p class="note"><strong>Respuesta corta:</strong> entre empresas y autónomos, si el contrato no fija plazo, hay que pagar en <strong>30 días naturales</strong> desde la entrega de la mercancía o la prestación del servicio. Las partes pueden ampliarlo por pacto, pero <strong>nunca por encima de 60 días naturales</strong> (art. 4 de la Ley 3/2004). Si el cliente se retrasa, debe intereses de demora automáticamente, sin necesidad de reclamarlos, y una cantidad fija de 40 euros por costes de cobro.</p>
<p>Si ya tienes facturas cobradas tarde, calcula lo que te deben con la <a href="/intereses-demora-comerciales/">calculadora de intereses de demora</a>, que usa el tipo oficial del BOE de cada semestre.</p>

<h2 id="ambito">¿A quién se aplican estos plazos?</h2>
<p>La Ley 3/2004 se aplica a los pagos que son contraprestación de <strong>operaciones comerciales entre empresas</strong>, o entre empresas y la Administración, y a los pagos entre contratistas principales y sus proveedores y subcontratistas (art. 3.1). Para la ley, «empresa» es cualquier persona física o jurídica que actúa en el ejercicio de su actividad económica o profesional independiente (art. 2.a): un autónomo también lo es.</p>
<p>Quedan fuera las operaciones en las que interviene un <strong>consumidor</strong>, los intereses de cheques, pagarés y letras, las indemnizaciones por daños y las deudas sometidas a un concurso (art. 3.2). Los contratos con la Administración tienen además sus propias reglas en la normativa de contratos del sector público, que no tratamos aquí.</p>

<h2 id="plazos">Los plazos del artículo 4, uno a uno</h2>
<div class="table-wrap"><table>
<thead><tr><th>Situación</th><th>Plazo de pago</th><th>Desde cuándo se cuenta</th><th>Base</th></tr></thead>
<tbody>
<tr><td>El contrato no dice nada</td><td>30 días naturales</td><td>Recepción de las mercancías o prestación de los servicios, aunque la factura llegara antes</td><td>Art. 4.1</td></tr>
<tr><td>Hay un procedimiento de aceptación o comprobación</td><td>30 días naturales</td><td>Fecha de la aceptación, que no puede tardar más de 30 días desde la entrega</td><td>Art. 4.2</td></tr>
<tr><td>Plazo pactado en el contrato</td><td>El pactado, con un <strong>máximo de 60 días naturales</strong></td><td>Lo que fije el contrato; la recepción electrónica de la factura puede iniciar el cómputo si se garantiza su autenticidad e integridad</td><td>Art. 4.1 y 4.3</td></tr>
<tr><td>Factura resumen o agrupación periódica (hasta 15 días)</td><td>Máximo 60 días naturales</td><td>Desde la mitad del periodo agrupado</td><td>Art. 4.4</td></tr>
</tbody></table></div>
<p>Dos detalles que se olvidan a menudo. El proveedor debe hacer llegar la factura a su cliente <strong>antes de que pasen 15 días naturales</strong> desde la entrega o el servicio (art. 4.1, párrafo segundo). Y los plazos se cuentan en <strong>días naturales</strong>: son nulos los pactos que excluyan del cómputo los periodos de vacaciones (art. 2.d).</p>

<h2 id="ejemplos">Ejemplos con fechas</h2>
<div class="table-wrap"><table>
<thead><tr><th>Caso</th><th>Entrega o servicio</th><th>Plazo</th><th>Último día para pagar</th></tr></thead>
<tbody>
<tr><td>Sin pacto</td><td>2 de marzo</td><td>30 días naturales</td><td>1 de abril</td></tr>
<tr><td>Pacto a 60 días</td><td>2 de marzo</td><td>60 días naturales</td><td>1 de mayo</td></tr>
<tr><td>Pacto a 90 días</td><td>2 de marzo</td><td>60 días (el exceso no vale)</td><td>1 de mayo</td></tr>
<tr><td>Agrupación del 1 al 15 de marzo</td><td>Mitad del periodo: 8 de marzo</td><td>60 días como máximo</td><td>7 de mayo</td></tr>
</tbody></table></div>
<p>En el último caso, la ley toma como inicio la fecha que corresponde a la mitad del periodo agrupado; con una agrupación del 1 al 15, esa fecha es el 8. Si el contrato dice 90 días, el pacto no puede superar el límite legal de 60, y además el artículo 9 permite declarar nulas las cláusulas sobre el plazo de pago que sean manifiestamente abusivas para el acreedor.</p>

<h2 id="retraso">Qué pasa si te pagan tarde</h2>
<p>El deudor incurre en mora y debe pagar intereses <strong>automáticamente</strong>, «por el mero incumplimiento del pago en el plazo pactado o legalmente establecido, sin necesidad de aviso de vencimiento ni intimación alguna» (art. 5). Para exigirlos, tú debes haber cumplido tus obligaciones y no haber cobrado a tiempo, salvo que el deudor pruebe que no es responsable del retraso (art. 6).</p>
<ul>
<li><strong>Interés de demora:</strong> el pactado en el contrato o, si no hay pacto, el tipo legal: el tipo del Banco Central Europeo más ocho puntos, que el Ministerio publica cada semestre en el BOE (art. 7). Para el segundo semestre de 2026 es el <strong>10,40 %</strong> (Resolución del Tesoro de 30 de junio de 2026). Es abusivo, salvo prueba en contrario, pactar un interés un 70 % inferior al legal (art. 9.1).</li>
<li><strong>Costes de cobro:</strong> «una cantidad fija de 40 euros, que se añadirá en todo caso y sin necesidad de petición expresa a la deuda principal», más los costes de cobro acreditados que superen esa cifra (art. 8.1). El Tribunal de Justicia de la UE aclaró en el asunto C-585/20 que se deben por cada factura pagada tarde.</li>
</ul>
<p>Nuestra <a href="/intereses-demora-comerciales/">calculadora de intereses de demora</a> aplica a cada factura el tipo del BOE de cada semestre en el que estuvo impagada y suma los 40 euros, y puedes exportar el resultado a CSV para reclamarlo. Tienes los tipos de este año en <a href="/blog/tipo-interes-demora-2026/">tipo de interés de demora 2026</a> y un modelo de carta en <a href="/blog/reclamar-factura-impagada-intereses/">cómo reclamar una factura impagada con intereses y 40 €</a>.</p>

<h2 id="pmp">Plazos de pago y cuentas anuales</h2>
<p>Las sociedades informan de su cumplimiento en la memoria de las cuentas anuales mediante el <strong>periodo medio de pago a proveedores</strong>, calculado con el método de la Resolución del ICAC de 2016, y, si no presentan cuentas abreviadas, del número e importe de facturas pagadas dentro del plazo legal (disposición adicional tercera de la Ley 15/2010, en la redacción de la Ley 18/2022). Lo calculas con la <a href="/periodo-medio-pago-proveedores/">calculadora del periodo medio de pago</a> y lo explicamos con números en <a href="/blog/calcular-periodo-medio-pago-proveedores-ejemplo/">cómo calcular el periodo medio de pago a proveedores</a>.</p>

<h2 id="2027">Lo que cambiará con la factura electrónica B2B</h2>
<p>El Real Decreto 238/2026 de factura electrónica obligatoria entre empresas obligará a los clientes a informar de la fecha en que pagan cada factura, en un plazo de cuatro días naturales excluyendo sábados, domingos y festivos nacionales (art. 12.3). Con esos datos la AEAT podrá seguir los plazos de pago reales. Las fechas para cada empresa están en <a href="/factura-electronica-obligatoria/">factura electrónica obligatoria: fechas y test</a>.</p>
""",
    faq=[
        ("¿Cuál es el plazo máximo de pago a proveedores en España?", "60 días naturales entre empresas. Sin pacto, el plazo es de 30 días naturales desde la entrega o el servicio; las partes pueden ampliarlo, pero nunca por encima de 60 días (art. 4.3 de la Ley 3/2004)."),
        ("¿Desde cuándo se cuentan los 30 días?", "Desde la recepción de las mercancías o la prestación de los servicios, aunque la factura se haya recibido antes (art. 4.1). Si hay un procedimiento de aceptación, desde la aceptación, que no puede tardar más de 30 días."),
        ("¿Se pueden pactar 90 o 120 días de pago?", "No. La ley no permite acordar un plazo superior a 60 días naturales, y el artículo 9 permite declarar nulas las cláusulas sobre el plazo de pago manifiestamente abusivas para el acreedor."),
        ("¿Los días de vacaciones o agosto cuentan?", "Sí. Los plazos se cuentan en días naturales y son nulos los pactos que excluyan del cómputo los periodos vacacionales (art. 2.d de la Ley 3/2004)."),
        ("¿La Ley de morosidad se aplica a las ventas a particulares?", "No. El art. 3.2 excluye las operaciones comerciales en las que intervienen consumidores."),
        ("¿Qué puedo reclamar si me pagan tarde?", "Intereses de demora desde el día siguiente al vencimiento, sin necesidad de aviso (el pactado o el tipo legal del BOE: 10,40 % en el 2.º semestre de 2026), más 40 euros por costes de cobro y los costes de cobro acreditados que superen esa cantidad."),
    ],
    sources=[S.LEY3, S.TESORO26, S.TJUE40, S.LEY15, S.ICAC, S.RD238],
))

# ================================================================ publicadas el 14/11/2026
# ---------------------------------------------------------------- #5 tipo de interés de demora 2026
POSTS.append(dict(
    slug="tipo-interes-demora-2026",
    published="2026-11-14",
    title="Tipo de interés de demora 2026 en operaciones comerciales",
    desc="Interés de demora comercial 2026: 10,15 % en el 1.er semestre y 10,40 % en el 2.º, según el BOE. Cómo se fija, tabla 2023-2026 y ejemplo de cálculo.",
    h1="Tipo de interés de demora 2026 en operaciones comerciales",
    intro="Los dos tipos legales de interés de demora de 2026 para facturas entre empresas, tal como los publicó el Tesoro en el BOE, cómo se calculan y cómo aplicarlos a una factura que cruza de semestre. Revisado en el BOE el 14 de noviembre de 2026.",
    content="""
<p class="note"><strong>Respuesta corta:</strong> el tipo legal de interés de demora para operaciones comerciales es del <strong>10,15 % del 1 de enero al 30 de junio de 2026</strong> y del <strong>10,40 % del 1 de julio al 31 de diciembre de 2026</strong>. Los publicó la Secretaría General del Tesoro y Financiación Internacional en el BOE del 31 de diciembre de 2025 (BOE-A-2025-27201) y del 1 de julio de 2026 (BOE-A-2026-14327). El tipo del primer semestre de 2027 todavía no está publicado: suele salir en el BOE a finales de diciembre.</p>
<p>Si quieres el importe exacto de una factura cobrada tarde, la <a href="/intereses-demora-comerciales/">calculadora de intereses de demora</a> aplica a cada día el tipo de su semestre y suma los 40 euros de costes de cobro.</p>

<h2 id="tipos">Los tipos de 2026, con su resolución del BOE</h2>
<div class="table-wrap"><table>
<thead><tr><th>Periodo</th><th>Tipo BCE de referencia</th><th>Tipo legal de demora</th><th>Publicación</th></tr></thead>
<tbody>
<tr><td>1 de enero a 30 de junio de 2026</td><td>2,15 %</td><td><strong>10,15 %</strong></td><td>Resolución de 23/12/2025, BOE núm. 315 de 31/12/2025 (BOE-A-2025-27201)</td></tr>
<tr><td>1 de julio a 31 de diciembre de 2026</td><td>2,40 %</td><td><strong>10,40 %</strong></td><td>Resolución de 30/06/2026, BOE núm. 159 de 01/07/2026 (BOE-A-2026-14327)</td></tr>
<tr><td>1 de enero a 30 de junio de 2027</td><td colspan="2">Pendiente de publicación</td><td>Se añadirá aquí y en la calculadora en cuanto aparezca en el BOE</td></tr>
</tbody></table></div>

<h2 id="como-se-fija">Cómo se fija el tipo: BCE más ocho puntos</h2>
<p>El artículo 7.2 de la Ley 3/2004, de lucha contra la morosidad en las operaciones comerciales, dice que el tipo legal es «la suma del tipo de interés aplicado por el Banco Central Europeo a su más reciente operación principal de financiación efectuada antes del primer día del semestre natural de que se trate más ocho puntos porcentuales». Ese tipo se aplica durante los seis meses siguientes, y el Ministerio lo publica cada semestre en el BOE (art. 7.3).</p>
<p>Por eso los números de 2026 cuadran así: 2,15 % + 8 = 10,15 % para el primer semestre y 2,40 % + 8 = 10,40 % para el segundo. Las resoluciones del Tesoro no crean el tipo, solo lo publican: la regla está en la ley.</p>
<p>Importante: este tipo legal solo se aplica <strong>si el contrato no fija otro</strong>. El artículo 7.1 da prioridad al interés pactado. Pero el pacto tiene un límite: el artículo 9.1 considera abusivo, salvo prueba en contrario, un interés pactado «un 70 por ciento inferior al interés legal de demora». Y son nulas las cláusulas que excluyan el cobro de intereses o de los 40 euros.</p>

<h2 id="historico">Evolución reciente (2023-2026)</h2>
<div class="table-wrap"><table>
<thead><tr><th>Semestre</th><th>Tipo legal</th><th>BOE</th></tr></thead>
<tbody>
<tr><td>2.º semestre de 2026</td><td>10,40 %</td><td>BOE-A-2026-14327</td></tr>
<tr><td>1.er semestre de 2026</td><td>10,15 %</td><td>BOE-A-2025-27201</td></tr>
<tr><td>2.º semestre de 2025</td><td>10,15 %</td><td>BOE-A-2025-13217</td></tr>
<tr><td>1.er semestre de 2025</td><td>11,15 %</td><td>BOE-A-2024-27618</td></tr>
<tr><td>2.º semestre de 2024</td><td>12,25 %</td><td>BOE-A-2024-13089</td></tr>
<tr><td>1.er semestre de 2024</td><td>12,50 %</td><td>BOE-A-2023-26709</td></tr>
<tr><td>2.º semestre de 2023</td><td>12,00 %</td><td>BOE-A-2023-15221</td></tr>
<tr><td>1.er semestre de 2023</td><td>10,50 %</td><td>BOE-A-2022-24416</td></tr>
</tbody></table></div>
<p>Entre el segundo semestre de 2016 y el segundo semestre de 2022 el tipo fue del 8,00 %, porque el tipo de referencia del BCE estaba en el 0 %. La tabla completa desde 2013, con el enlace a cada resolución, está en la página de la <a href="/intereses-demora-comerciales/">calculadora de intereses de demora</a>.</p>

<h2 id="ejemplo">Ejemplo: una factura que cruza el 1 de julio</h2>
<p>Una empresa debía pagar una factura de <strong>10.000 euros</strong> el 31 de mayo de 2026 y la pagó el 31 de agosto de 2026. No hay interés pactado, así que se aplica el legal. Los intereses corren desde el día siguiente al vencimiento, sin necesidad de reclamarlos (art. 5), y cada día se calcula al tipo del semestre en el que cae:</p>
<div class="table-wrap"><table>
<thead><tr><th>Tramo</th><th>Días</th><th>Tipo</th><th>Cálculo</th><th>Intereses</th></tr></thead>
<tbody>
<tr><td>1 a 30 de junio de 2026</td><td>30</td><td>10,15 %</td><td>10.000 × 10,15 % × 30 / 365</td><td>83,42 €</td></tr>
<tr><td>1 de julio a 31 de agosto de 2026</td><td>62</td><td>10,40 %</td><td>10.000 × 10,40 % × 62 / 365</td><td>176,66 €</td></tr>
<tr><td colspan="4"><strong>Total intereses (92 días)</strong></td><td><strong>260,08 €</strong></td></tr>
</tbody></table></div>
<p>A eso se suma la <strong>cantidad fija de 40 euros</strong> por costes de cobro del artículo 8.1, que se añade «en todo caso y sin necesidad de petición expresa». Total a reclamar en este ejemplo: 260,08 + 40 = <strong>300,08 euros</strong>, además de los costes de cobro acreditados que superen esos 40 euros. Usamos interés simple y año de 365 días, que es la forma habitual de calcularlo; si tu contrato pacta otra base, aplica la del contrato.</p>

<h2 id="otros-intereses">No lo confundas con otros «intereses de demora»</h2>
<p>En España se habla de interés de demora en contextos distintos, y cada uno tiene su propio tipo:</p>
<ul>
<li><strong>Interés de demora comercial</strong> (el de esta guía): deudas entre empresas y autónomos, o entre empresas y la Administración, por operaciones comerciales. Ley 3/2004, tipo semestral del Tesoro.</li>
<li><strong>Interés de demora tributario</strong>: el que cobra Hacienda cuando pagas tarde un impuesto. Lo regula la Ley General Tributaria y su tipo se fija para cada año en la Ley de Presupuestos Generales del Estado. Lo explicaremos en una guía aparte.</li>
<li><strong>Interés legal del dinero</strong>: el general del Código Civil para otras deudas, también fijado por la Ley de Presupuestos.</li>
</ul>
<p>Si una factura a un particular (consumidor) se paga tarde, la Ley 3/2004 no se aplica (art. 3.2), así que el tipo del 10,40 % no sirve para ese caso.</p>

<h2 id="pasos">Qué hacer con estos tipos</h2>
<ol class="steps">
<li><strong>Comprueba el vencimiento real</strong> de la factura: 30 días desde la entrega si no hay pacto, y nunca más de 60 por pacto. Lo explicamos en <a href="/blog/plazos-pago-ley-morosidad/">plazos de pago de la Ley de morosidad</a>.</li>
<li><strong>Calcula los intereses</strong> por tramos con la <a href="/intereses-demora-comerciales/">calculadora</a>; puedes meter varias facturas y exportar el detalle a CSV.</li>
<li><strong>Suma 40 euros por factura</strong>: el TJUE confirmó en el asunto C-585/20 que se deben por cada factura pagada tarde.</li>
<li><strong>Reclámalo por escrito</strong> con el detalle del cálculo. Tienes un modelo en <a href="/blog/reclamar-factura-impagada-intereses/">cómo reclamar una factura impagada con intereses y 40 €</a>.</li>
</ol>
<p>Las sociedades que pagan tarde de forma habitual lo verán además reflejado en su <a href="/periodo-medio-pago-proveedores/">periodo medio de pago a proveedores</a>, que deben informar en la memoria de sus cuentas anuales.</p>
""",
    faq=[
        ("¿Cuál es el interés de demora comercial en 2026?", "10,15 % del 1 de enero al 30 de junio de 2026 (BOE-A-2025-27201) y 10,40 % del 1 de julio al 31 de diciembre de 2026 (BOE-A-2026-14327), según las resoluciones del Tesoro publicadas en el BOE."),
        ("¿Cómo se calcula el tipo legal de interés de demora?", "Es el tipo de la operación principal de financiación más reciente del Banco Central Europeo antes del primer día del semestre, más ocho puntos porcentuales (art. 7.2 de la Ley 3/2004). En el 2.º semestre de 2026: 2,40 % + 8 = 10,40 %."),
        ("¿Cuándo se publica el tipo de 2027?", "El del primer semestre de 2027 se publicará en el BOE, normalmente a finales de diciembre de 2026. Hasta entonces no lo damos: la calculadora no estima tipos que no estén publicados salvo que lo pidas."),
        ("¿Puedo pactar un interés de demora más bajo?", "Sí, el interés pactado tiene prioridad (art. 7.1), pero se considera abusivo, salvo prueba en contrario, si es un 70 % inferior al legal (art. 9.1), y son nulos los pactos que excluyan los intereses o los 40 euros."),
        ("Si la factura vencía en 2025 y se paga en 2026, ¿qué tipo aplico?", "Cada día al tipo de su semestre: los días de 2025 al tipo de 2025 y los de 2026 al de 2026. La calculadora divide el periodo en tramos automáticamente."),
        ("¿El interés de demora de Hacienda es el mismo?", "No. El interés de demora tributario lo regula la Ley General Tributaria y su tipo lo fija cada año la Ley de Presupuestos Generales del Estado. El 10,40 % solo vale para deudas comerciales de la Ley 3/2004."),
    ],
    sources=[S.LEY3, S.TESORO26A, S.TESORO26, S.TESORO25B, S.TJUE40, S.BDE_TIPOS],
))

# ---------------------------------------------------------------- #29 reclamar factura impagada
POSTS.append(dict(
    slug="reclamar-factura-impagada-intereses",
    published="2026-11-14",
    title="Cómo reclamar una factura impagada con intereses y 40 €",
    desc="Reclama una factura impagada a otra empresa según la Ley 3/2004: intereses automáticos, 40 € por factura, cálculo con ejemplo y modelo de carta gratis.",
    h1="Cómo reclamar una factura impagada con intereses y 40 euros",
    intro="Lo que la Ley 3/2004 te permite reclamar cuando otra empresa o autónomo te paga tarde o no te paga, cómo calcularlo y un modelo de carta para pedirlo. Basado en el texto consolidado del BOE, revisado el 14 de noviembre de 2026.",
    content="""
<p class="note"><strong>Respuesta corta:</strong> si un cliente empresario no te paga en plazo, la Ley 3/2004 te da derecho a tres cosas sin necesidad de avisarle antes: la deuda, los <strong>intereses de demora</strong> desde el día siguiente al vencimiento (art. 5) y una cantidad fija de <strong>40 euros</strong> por costes de cobro (art. 8.1), que el TJUE ha confirmado que se debe por cada factura. Calcula el total con la <a href="/intereses-demora-comerciales/">calculadora de intereses de demora</a> y reclámalo por escrito con el detalle.</p>

<h2 id="requisitos">Antes de reclamar: ¿se aplica la Ley de morosidad?</h2>
<p>La ley se aplica a los pagos de <strong>operaciones comerciales entre empresas</strong> (sociedades y autónomos) y entre empresas y la Administración (art. 3.1). No se aplica si tu cliente es un consumidor, ni a cheques, pagarés y letras, ni a deudas incluidas en un concurso (art. 3.2). Además, el artículo 6 exige dos condiciones para cobrar intereses:</p>
<ul>
<li>que tú hayas cumplido tus obligaciones contractuales y legales (entregaste lo pactado, emitiste la factura correctamente), y</li>
<li>que no hayas cobrado a tiempo, salvo que el deudor pruebe que el retraso no es culpa suya.</li>
</ul>
<p>Si pactasteis pagos a plazos y solo falla uno, los intereses y los 40 euros se calculan únicamente sobre las cantidades vencidas (art. 6, último párrafo).</p>

<h2 id="vencimiento">Paso 1: fija la fecha de vencimiento</h2>
<p>Sin pacto, el cliente tiene <strong>30 días naturales</strong> desde la entrega de la mercancía o la prestación del servicio; con pacto, como máximo <strong>60 días naturales</strong> (art. 4). Un plazo de 90 o 120 días en el contrato no vale por encima de 60. Los intereses empiezan a contar el día siguiente al vencimiento. Tienes todos los casos (aceptación, facturas agrupadas, días de vacaciones) en <a href="/blog/plazos-pago-ley-morosidad/">plazos de pago de la Ley de morosidad</a>.</p>

<h2 id="calculo">Paso 2: calcula lo que te deben</h2>
<p>El interés es el pactado en el contrato o, si no hay pacto, el tipo legal que el Tesoro publica cada semestre en el BOE: <strong>10,15 %</strong> en el primer semestre de 2026 y <strong>10,40 %</strong> en el segundo (art. 7). Lo explicamos en <a href="/blog/tipo-interes-demora-2026/">tipo de interés de demora 2026</a>.</p>
<p>Ejemplo con tres facturas a un mismo cliente, sin interés pactado, pagadas todas el 15 de julio de 2026:</p>
<div class="table-wrap"><table>
<thead><tr><th>Factura</th><th>Importe</th><th>Vencimiento</th><th>Días de retraso</th><th>Intereses</th><th>Costes de cobro</th></tr></thead>
<tbody>
<tr><td>F-101</td><td>1.500,00 €</td><td>10/03/2026</td><td>127</td><td>53,13 €</td><td>40,00 €</td></tr>
<tr><td>F-118</td><td>3.000,00 €</td><td>20/04/2026</td><td>86</td><td>72,05 €</td><td>40,00 €</td></tr>
<tr><td>F-124</td><td>800,00 €</td><td>05/05/2026</td><td>71</td><td>15,88 €</td><td>40,00 €</td></tr>
<tr><td colspan="4"><strong>Total</strong></td><td><strong>141,06 €</strong></td><td><strong>120,00 €</strong></td></tr>
</tbody></table></div>
<p>Los días hasta el 30 de junio van al 10,15 % y los 15 días de julio al 10,40 %. Total a reclamar además de las facturas: <strong>261,06 euros</strong>. El TJUE indicó en el asunto C-585/20 que el IVA forma parte de la cantidad adeudada, así que el interés se calcula sobre el importe total de la factura, IVA incluido.</p>

<h2 id="costes">Paso 3: añade los costes de cobro</h2>
<p>Los 40 euros son un mínimo fijo: «se añadirá en todo caso y sin necesidad de petición expresa a la deuda principal» (art. 8.1). Si tus costes reales de cobro son mayores (por ejemplo, una gestoría de recobro o un burofax) y los puedes <strong>acreditar</strong>, puedes reclamar también lo que supere esos 40 euros. El deudor no tiene que pagar esta indemnización si demuestra que no es responsable del retraso (art. 8.2).</p>

<h2 id="clausulas">Si el contrato dice otra cosa</h2>
<p>El artículo 9 declara nulas las cláusulas o prácticas sobre plazo de pago, interés o costes de cobro que sean manifiestamente abusivas para el acreedor. En todo caso son nulas las que <strong>excluyan</strong> el interés de demora o los 40 euros, y se presume abusivo un interés pactado un 70 % inferior al legal. Una cláusula del tipo «el retraso en el pago no devengará intereses» no te impide reclamarlos.</p>

<h2 id="carta">Paso 4: reclámalo por escrito (modelo)</h2>
<p>La ley no te obliga a avisar para que nazcan los intereses, pero una reclamación escrita deja constancia y suele bastar para cobrar. Usa un medio que pruebe el envío y la recepción. Puedes adaptar este texto:</p>
<div class="table-wrap"><table><tbody><tr><td>
<p><strong>Asunto:</strong> Reclamación de facturas vencidas, intereses de demora y costes de cobro</p>
<p>Muy señores míos:</p>
<p>Les recordamos que las facturas F-101, F-118 y F-124, por un total de 5.300,00 euros, vencieron el 10/03/2026, el 20/04/2026 y el 05/05/2026 y se abonaron el 15/07/2026, fuera del plazo de pago.</p>
<p>De acuerdo con los artículos 5, 7 y 8 de la Ley 3/2004, de 29 de diciembre, les reclamamos 141,06 euros de intereses de demora al tipo legal publicado en el BOE (10,15 % y 10,40 % en los semestres afectados) y 120,00 euros de indemnización por costes de cobro (40 euros por factura). Adjuntamos el detalle del cálculo.</p>
<p>Les rogamos el pago de 261,06 euros en la cuenta [IBAN] en un plazo de [X] días.</p>
<p>Atentamente, [Nombre, NIF y firma]</p>
</td></tr></tbody></table></div>
<p>Si la factura sigue sin pagarse, sustituye «se abonaron el…» por «siguen pendientes de pago» y reclama también el principal; los intereses siguen corriendo hasta el día del pago.</p>

<h2 id="despues">Si no pagan</h2>
<p>Si el cliente no responde, la vía para cobrar depende de la cuantía y de si la deuda está documentada; un abogado o una gestoría de recobro te dirán la opción adecuada, y los costes acreditados que te genere entran en la indemnización del artículo 8. Si vendes bienes, pactar por escrito una <strong>reserva de dominio</strong> antes de la entrega te permite conservar la propiedad hasta el pago completo (art. 10).</p>
<p>A partir de la factura electrónica obligatoria, el cliente tendrá que informar a la AEAT de la fecha de pago de cada factura y el emisor podrá comunicar voluntariamente los impagos (art. 12 del RD 238/2026). Lo contamos en <a href="/blog/informar-pago-factura-4-dias/">informar del pago de una factura en 4 días</a> y puedes comprobar tu fecha en el <a href="/factura-electronica-obligatoria/">test de factura electrónica obligatoria</a>.</p>
""",
    faq=[
        ("¿Tengo que avisar al cliente para cobrar intereses de demora?", "No. El art. 5 de la Ley 3/2004 dice que el deudor incurre en mora automáticamente por no pagar en plazo, «sin necesidad de aviso de vencimiento ni intimación alguna». Reclamarlo por escrito sirve para dejar constancia y cobrar."),
        ("¿Los 40 euros son por factura o por cliente?", "Por factura. El art. 8.1 fija una cantidad de 40 euros cuando el deudor incurre en mora, y el TJUE confirmó en el asunto C-585/20 que se debe por cada factura no pagada a su vencimiento."),
        ("¿Se calculan los intereses con IVA o sin IVA?", "Sobre el importe total adeudado, IVA incluido: el TJUE indicó en el asunto C-585/20 que el IVA forma parte de la cantidad adeudada."),
        ("¿Qué tipo de interés aplico si el contrato no dice nada?", "El tipo legal del semestre que publica el Tesoro en el BOE: 10,15 % en el 1.er semestre de 2026 y 10,40 % en el 2.º (art. 7 de la Ley 3/2004)."),
        ("¿Puedo reclamar intereses a un particular?", "No con la Ley 3/2004: excluye las operaciones con consumidores (art. 3.2). Para esas deudas se aplican otras normas."),
        ("¿Es válida una cláusula que excluye los intereses de demora?", "No. El art. 9.1 declara nulas en todo caso las cláusulas o prácticas que excluyan el interés de demora o la indemnización de 40 euros por costes de cobro."),
    ],
    sources=[S.LEY3, S.TESORO26A, S.TESORO26, S.TJUE40, S.RD238],
))

# ---------------------------------------------------------------- #23 informar del pago en 4 días
POSTS.append(dict(
    slug="informar-pago-factura-4-dias",
    published="2026-11-14",
    title="Informar del pago de una factura en 4 días: cómo contar",
    desc="Factura electrónica obligatoria: plazo de 4 días para informar del pago (art. 12.3 RD 238/2026), qué se informa, desde cuándo y ejemplos con festivos 2027.",
    h1="Informar del pago de una factura en 4 días: cómo se cuenta el plazo",
    intro="Qué exige el artículo 12 del Real Decreto 238/2026 al cliente que recibe una factura electrónica, cómo se cuentan los 4 días con fines de semana y festivos y desde qué fecha te afecta. Revisado en el BOE el 14 de noviembre de 2026.",
    content="""
<p class="note"><strong>Respuesta corta:</strong> con la factura electrónica obligatoria, quien <strong>recibe</strong> una factura debe comunicar a la solución pública de la AEAT el pago efectivo completo, su fecha y la fecha de vencimiento en un máximo de <strong>4 días naturales desde el pago, excluyendo sábados, domingos y festivos nacionales</strong> (art. 12.3 del RD 238/2026). En la práctica son cuatro días laborables. Calcula tu fecha límite con la <a href="/factura-electronica-obligatoria/">calculadora del plazo de 4 días</a>.</p>

<h2 id="que">Qué hay que informar, y quién</h2>
<p>La obligación es del <strong>destinatario</strong> de la factura electrónica, sea persona física o jurídica, tanto si la factura llegó por la solución pública como por una plataforma privada (art. 12.1). Debe comunicar:</p>
<ul>
<li>el <strong>pago efectivo completo</strong> de cada factura recibida y no rechazada, con la <strong>fecha efectiva</strong> del pago;</li>
<li>la <strong>fecha de vencimiento</strong> del plazo de pago;</li>
<li>o, en su lugar, el <strong>rechazo</strong> de la factura. Si no hay rechazo ni factura rectificativa, la factura se presume aceptada (art. 12.1).</li>
</ul>
<p>Puede añadir, cuando sea relevante para el plazo de la Ley 3/2004, la fecha de recepción de la mercancía o del servicio, o la de recepción de la factura (art. 12.3). Se hace con un servicio electrónico de comunicación de pagos de la solución pública, y el cliente puede autorizar a su plataforma privada para que lo comunique por él (art. 12.2). El emisor, por su parte, podrá comunicar de forma voluntaria el cobro o el impago (art. 12.4).</p>
<p>Aparte, el artículo 10.3 aplica el mismo plazo de cuatro días a los estados que el cliente comunica al emisor: aceptación o rechazo comercial y pago completo. Los pagos parciales y la cesión de la factura a un tercero se pueden comunicar, pero no es obligatorio (art. 10.2).</p>

<h2 id="contar">Cómo se cuentan los 4 días</h2>
<p>El texto dice «4 días naturales desde dicha fecha efectiva del pago, excluyendo sábados, domingos y festivos nacionales». Contamos desde el día siguiente al pago y nos saltamos los sábados, domingos y las fiestas nacionales de la relación anual del BOE. Ejemplos con el calendario de 2027 (Resolución de fiestas laborales de 2027, BOE-A-2026-21254):</p>
<div class="table-wrap"><table>
<thead><tr><th>Pago</th><th>Días que no cuentan</th><th>Último día para informar</th></tr></thead>
<tbody>
<tr><td>Lunes 4 de octubre de 2027</td><td>Ninguno</td><td>Viernes 8 de octubre de 2027</td></tr>
<tr><td>Viernes 8 de octubre de 2027</td><td>Fin de semana y martes 12 de octubre (Fiesta Nacional)</td><td>Viernes 15 de octubre de 2027</td></tr>
<tr><td>Viernes 29 de octubre de 2027</td><td>Fin de semana y lunes 1 de noviembre (Todos los Santos)</td><td>Viernes 5 de noviembre de 2027</td></tr>
<tr><td>Viernes 3 de diciembre de 2027</td><td>Fines de semana, lunes 6 (Constitución) y miércoles 8 (Inmaculada)</td><td>Lunes 13 de diciembre de 2027</td></tr>
<tr><td>Viernes 24 de diciembre de 2027</td><td>Sábado 25 (Navidad) y domingo 26</td><td>Jueves 30 de diciembre de 2027</td></tr>
</tbody></table></div>
<p>El artículo solo habla de festivos <strong>nacionales</strong>. Las fiestas autonómicas y locales no aparecen en el texto; si quieres ir sobre seguro, no cuentes con ellas e informa antes. Nuestra calculadora te deja añadirlas como festivos opcionales para ver la diferencia. La relación de fiestas de 2028 aún no está publicada: para pagos de 2028 la calculadora usa las fiestas nacionales no sustituibles y marca el resultado como provisional.</p>

<h2 id="cuando">Desde cuándo te afecta</h2>
<p>El RD 238/2026 empieza a aplicarse 12 o 24 meses después de la entrada en vigor de la Orden HAC/1028/2026, que entró en vigor el 6 de octubre de 2026 (disposición final cuarta). El calendario de la AEAT lo traduce en fechas:</p>
<div class="table-wrap"><table>
<thead><tr><th>Quién</th><th>Factura electrónica</th><th>Informar pagos y estados</th></tr></thead>
<tbody>
<tr><td>Volumen de operaciones del año anterior de más de 8 millones de euros</td><td>6 de octubre de 2027</td><td>6 de octubre de 2027</td></tr>
<tr><td>Resto de sociedades y entidades</td><td>6 de octubre de 2028</td><td>6 de octubre de 2028</td></tr>
<tr><td>Autónomos y entidades en atribución de rentas con 8 millones o menos</td><td>6 de octubre de 2028</td><td>6 de octubre de 2029 (voluntario antes)</td></tr>
</tbody></table></div>
<p>La última fila sale de la disposición transitoria tercera: para personas físicas y entidades en atribución de rentas de hasta 8 millones, la obligación de informar de los estados (arts. 10 y 12) llega doce meses después que la factura electrónica, y hasta entonces es voluntaria. Ojo: el umbral es el <strong>volumen de operaciones</strong> del artículo 121 de la Ley del IVA, no la facturación contable. Compruébalo con el <a href="/factura-electronica-obligatoria/">test de factura electrónica obligatoria</a>.</p>

<h2 id="para-que">Para qué sirve este dato</h2>
<p>Con la fecha de pago y la de vencimiento de cada factura, la AEAT podrá seguir los plazos de pago reales entre empresas y dar esa información a los ministerios de Economía e Industria (art. 14.1). Además, cada primer trimestre enviará al Observatorio Estatal de la Morosidad Privada los datos para elaborar el listado de empresas que hayan incumplido los plazos de la Ley 3/2004 (art. 14.2). En otras palabras: pagar tarde será mucho más visible. Si tu empresa ya calcula su <a href="/periodo-medio-pago-proveedores/">periodo medio de pago a proveedores</a>, ese número debería cuadrar con lo que informes.</p>

<h2 id="preparar">Cómo prepararte</h2>
<ol class="steps">
<li><strong>Averigua tu fecha</strong> con el test y apunta si te afecta en 2027, 2028 o 2029.</li>
<li><strong>Pregunta a tu banco o a tu programa contable</strong> cómo registrarán la fecha efectiva de cada pago y si tu plataforma de facturación lo comunicará por ti (art. 12.2).</li>
<li><strong>Rechaza a tiempo</strong> las facturas que no aceptes: si no lo haces, se presumen aceptadas.</li>
<li><strong>Revisa tus plazos de pago</strong>: con los datos a la vista, cumplir los 30 o 60 días de la <a href="/blog/plazos-pago-ley-morosidad/">Ley de morosidad</a> importa más. Si pagas tarde, el proveedor puede reclamarte <a href="/blog/reclamar-factura-impagada-intereses/">intereses y 40 euros por factura</a>.</li>
</ol>
""",
    faq=[
        ("¿Cuántos días tengo para informar del pago de una factura electrónica?", "4 días naturales desde la fecha efectiva del pago, excluyendo sábados, domingos y festivos nacionales (art. 12.3 del RD 238/2026). En la práctica, cuatro días laborables."),
        ("¿Quién tiene que informar del pago, el emisor o el receptor?", "El receptor (destinatario) de la factura. El emisor puede comunicar voluntariamente el cobro o el impago (art. 12.4), y el receptor puede autorizar a su plataforma privada para que comunique los pagos (art. 12.2)."),
        ("¿Cuentan los festivos autonómicos y locales?", "El artículo solo excluye sábados, domingos y festivos nacionales. Las fiestas autonómicas y locales no se mencionan, así que lo prudente es no contar con ellas e informar antes."),
        ("¿Hay que informar de los pagos parciales?", "No es obligatorio: el art. 10.2 permite informar del pago parcial, sin que altere el cálculo del plazo de pago. La obligación es el pago efectivo completo."),
        ("¿Desde cuándo tienen que informar los autónomos?", "Los autónomos con un volumen de operaciones de hasta 8 millones de euros, desde el 6 de octubre de 2029, doce meses después de su obligación de factura electrónica (disposición transitoria tercera). Antes es voluntario."),
        ("¿Qué pasa si no rechazo una factura?", "Si no hay rechazo ni factura rectificativa posterior, la factura se presume aceptada (art. 12.1 del RD 238/2026)."),
    ],
    sources=[S.RD238, S.ORDEN1028, S.AEAT_CAL, S.FIESTAS27, S.LEY3, S.LEY18],
))
