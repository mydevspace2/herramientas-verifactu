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
<p>Nuestra <a href="/intereses-demora-comerciales/">calculadora de intereses de demora</a> aplica a cada factura el tipo del BOE de cada semestre en el que estuvo impagada y suma los 40 euros, y puedes exportar el resultado a CSV para reclamarlo.</p>

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
