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
    desc="¿Verifactu es obligatorio para autónomos? Fecha del BOE (6/10/2028 tras el RDL 43/2026), módulos, Excel, SII y opción gratuita.",
    h1="Verifactu para autónomos: cuándo es obligatorio y qué tienes que hacer",
    intro="Qué dice el Real Decreto 1007/2023 sobre los autónomos, qué fecha está en el BOE (aplazada a 2028), y cómo prepararte sin gastar de más. Revisado en el BOE el 26 de noviembre de 2026.",
    content="""
<p class="note"><strong>Respuesta corta:</strong> sí, Verifactu es obligatorio para los autónomos que emiten sus facturas o tiques con un programa, una app, un TPV o una caja registradora, tributen en estimación directa o en módulos. Según el BOE, tras el Real Decreto-ley 43/2026 (25/11/2026), deben tener el sistema adaptado <strong>antes del 6 de octubre de 2028</strong> (antes era el 1 de julio de 2027). Quien factura solo a mano, quien lleva el SII o tiene su domicilio fiscal en el País Vasco o Navarra queda fuera del reglamento estatal.</p>
<p>¿Quieres saberlo en tu caso concreto? Responde las cuatro preguntas del <a href="/">test «¿Verifactu es obligatorio para mí?»</a>; tarda un minuto y no guarda ningún dato.</p>

<h2 id="por-que">Por qué Verifactu afecta a los autónomos</h2>
<p>El artículo 3.1 del Reglamento de sistemas informáticos de facturación (aprobado por el Real Decreto 1007/2023) enumera a quién se aplica. Su letra b) incluye a «los contribuyentes del Impuesto sobre la Renta de las Personas Físicas que desarrollen actividades económicas». Es decir, a todos los autónomos y profesionales, sin distinguir el método de estimación del rendimiento. La letra d) añade las entidades en régimen de atribución de rentas con actividad económica, como las comunidades de bienes y las sociedades civiles sin personalidad jurídica a efectos del Impuesto sobre Sociedades.</p>
<p>La condición decisiva no es el tipo de autónomo, sino la herramienta: el reglamento se aplica a quien «utilice sistemas informáticos de facturación, aunque solo los use para una parte de su actividad». Si haces la mayoría de tus facturas a mano pero los tiques del mostrador salen de un TPV, ese TPV tiene que cumplir.</p>

<h2 id="fechas">Fechas para autónomos: BOE frente a anuncio</h2>
<div class="table-wrap"><table>
<thead><tr><th>Situación</th><th>Fecha</th><th>¿Es norma?</th></tr></thead>
<tbody>
<tr><td>Autónomos, comunidades de bienes y no residentes con establecimiento permanente</td><td>Sistema operativo <strong>antes del 6 de octubre de 2028</strong></td><td>Sí: disposición final 4.ª del RD 1007/2023, redacción del Real Decreto-ley 43/2026 (BOE)</td></tr>
<tr><td>Sociedades (Impuesto sobre Sociedades), como referencia</td><td>Antes del 6 de octubre de 2028</td><td>Sí: misma disposición</td></tr>
<tr><td>Aplazamiento general</td><td>Octubre de 2028, sin día concreto</td><td><strong>No</strong>: solo una nota informativa de Hacienda del 5/10/2026</td></tr>
</tbody></table></div>
<p>El aplazamiento anunciado por Hacienda se hizo efectivo con el Real Decreto-ley 43/2026, que sustituye el 1 de julio de 2027 por el 6 de octubre de 2028. Lo contamos con detalle en <a href="/blog/fechas-verifactu-2027-2028/">fechas de Verifactu: el aplazamiento a 2028 ya está en el BOE</a>.</p>

<h2 id="casos">Casos habituales de autónomos</h2>
<div class="table-wrap"><table>
<thead><tr><th>Tu situación</th><th>¿Te obliga Verifactu?</th><th>Por qué</th></tr></thead>
<tbody>
<tr><td>Estimación directa, facturas con un programa o app</td><td>Sí</td><td>Art. 3.1.b del reglamento</td></tr>
<tr><td>Módulos (estimación objetiva) con TPV o caja registradora</td><td>Sí</td><td>El art. 3.1.b no distingue el método de estimación</td></tr>
<tr><td>Recargo de equivalencia (comercio minorista) con TPV</td><td>Sí, si expides facturas con él</td><td>El reglamento no excluye este régimen de IVA; lo determinante es facturar con un sistema informático (<a href="/blog/verifactu-recargo-equivalencia/">detalle</a>)</td></tr>
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
<li class="pending"><span class="when">Pendiente</span>Pregunta a tu proveedor cuándo adaptará el programa; la fecha legal es el 6 de octubre de 2028.</li>
</ul>

<h2 id="b2b">No lo confundas con la factura electrónica obligatoria</h2>
<p>Verifactu no te obliga a mandar facturas en XML a tus clientes. Eso lo exige otra norma, el Real Decreto 238/2026 de factura electrónica entre empresarios, que para la mayoría de autónomos empieza el 6 de octubre de 2028. Son obligaciones distintas que pueden coincidir en la misma factura; lo resumimos en <a href="/blog/diferencias-verifactu-factura-electronica-b2b/">diferencias entre Verifactu y la factura electrónica B2B</a> y en la guía de <a href="/blog/factura-electronica-obligatoria-autonomos/">factura electrónica obligatoria para autónomos</a>.</p>
""",
    faq=[
        ("¿Verifactu es obligatorio para todos los autónomos?", "Para todos los que expiden facturas o tiques con un sistema informático (programa, app, TPV, caja registradora), según el art. 3.1.b del RD 1007/2023. No para quien factura solo a mano, quien lleva el SII o quien tiene el domicilio fiscal en el País Vasco o Navarra."),
        ("¿Cuándo entra en vigor Verifactu para autónomos?", "Según el BOE, los autónomos deben tener su sistema adaptado antes del 6 de octubre de 2028 (disposición final 4.ª del RD 1007/2023, redacción del RDL 43/2026; antes era el 1 de julio de 2027)."),
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

# ---------------------------------------------------------------- #20 factura electrónica 2027 empresas +8 M€
POSTS.append(dict(
    slug="factura-electronica-obligatoria-2027-empresas",
    published="2026-11-15",
    title="Factura electrónica obligatoria 2027: empresas de +8 M€",
    desc="Factura electrónica obligatoria: quién entra el 6 de octubre de 2027 (más de 8 M€ de operaciones), qué cambia, el PDF transitorio y cómo prepararte.",
    h1="Factura electrónica obligatoria en 2027: qué deben hacer las empresas de más de 8 millones",
    intro="Las empresas con más de 8 millones de euros de volumen de operaciones son las primeras en pasar a la factura electrónica entre empresarios y profesionales. Qué dice el RD 238/2026, qué calendario publica la AEAT y qué conviene hacer ya. Revisado en el BOE el 15 de noviembre de 2026.",
    content="""
<p class="note"><strong>Respuesta corta:</strong> según el calendario de la AEAT, los empresarios y profesionales cuyo <strong>volumen de operaciones</strong> del año natural anterior supere los <strong>8 millones de euros</strong> deben emitir y recibir factura electrónica en sus operaciones con otros empresarios o profesionales desde el <strong>6 de octubre de 2027</strong>. El resto, desde el 6 de octubre de 2028. Compruébalo con el <a href="/factura-electronica-obligatoria/">test de factura electrónica obligatoria</a>.</p>

<h2 id="fecha">De dónde sale el 6 de octubre de 2027</h2>
<p>El Real Decreto 238/2026 no escribe esa fecha: su disposición final cuarta hace depender los efectos de la entrada en vigor de la Orden HAC/1028/2026, que se produjo el <strong>6 de octubre de 2026</strong>. Para las empresas de mayor tamaño, la obligación se aplica 12 meses después; para el resto, 24 meses. La AEAT recoge ambas fechas en su calendario de implantación. Cuando hablamos de 2027 hablamos, pues, de un año exacto desde la orden.</p>

<h2 id="umbral">Qué significa «más de 8 millones»</h2>
<p>No es la cifra de negocios del balance. La disposición transitoria segunda se refiere al <strong>volumen de operaciones, calculado conforme al artículo 121 de la Ley del IVA</strong>, que superó los 8 millones de euros durante el <strong>año natural inmediato anterior</strong>. Es el mismo concepto que aparece en las declaraciones de IVA, y conviene mirarlo con tu asesor, porque incluye operaciones que no siempre coinciden con la facturación contable. Para fijar tu fecha, mira el año anterior al de la entrada en la obligación.</p>

<h2 id="ambito">Qué facturas entran</h2>
<ul>
<li><strong>Operaciones entre empresarios o profesionales</strong> cuyo destinatario tenga en España su sede de actividad, un establecimiento permanente o, en su defecto, su domicilio (art. 3.1).</li>
<li><strong>Quedan fuera</strong> las facturas simplificadas, salvo las cualificadas del artículo 7.2 del Reglamento de facturación (art. 4.1). Las facturas a consumidores finales tampoco son operaciones entre empresarios.</li>
<li>Una orden ministerial puede excluir otras operaciones, normalmente de forma temporal, si un sector tiene dificultades relevantes de adaptación (art. 4.2).</li>
</ul>

<h2 id="pdf">El PDF durante los primeros 12 meses</h2>
<p>La disposición transitoria segunda tiene una cautela útil para este grupo: durante los doce meses siguientes a la fecha en que el real decreto produzca efectos para ellas, las empresas de más de 8 millones <strong>deben acompañar cada factura electrónica de un PDF que asegure su legibilidad</strong>, salvo que el destinatario acepte voluntaria y expresamente recibirla solo en formato original. Ese PDF se envía al cliente por cualquier medio y <strong>no se manda a la solución pública</strong> de la AEAT.</p>

<h2 id="como">Qué cambia en la práctica</h2>
<div class="table-wrap"><table>
<thead><tr><th>Aspecto</th><th>Hoy</th><th>Con la obligación</th></tr></thead>
<tbody>
<tr><td>Formato</td><td>PDF o papel, por acuerdo</td><td>Mensaje estructurado EN16931 en CII, UBL, EDIFACT o Facturae (art. 7.1)</td></tr>
<tr><td>Vía</td><td>Correo, portal del cliente</td><td>Plataforma privada, solución pública de la AEAT o ambas (art. 5)</td></tr>
<tr><td>Identificador</td><td>Serie y número</td><td>Código único con NIF del emisor, serie y número, y fecha (art. 7.5)</td></tr>
<tr><td>Estados</td><td>No se informa</td><td>Aceptación o rechazo y pago efectivo completo (arts. 10 y 12)</td></tr>
</tbody></table></div>
<p>Si usas una plataforma privada y no emites por la solución pública, esta debe enviar a la AEAT una copia fiel de cada factura en UBL al emitirla (art. 6.2), y las facturas que salgan firmadas deben llevar firma electrónica avanzada (art. 7.3). La solución pública es gratuita (art. 11.10).</p>

<h2 id="pagos">La parte que se olvida: informar de los pagos</h2>
<p>Para este grupo, la comunicación de pagos también empieza el 6 de octubre de 2027. Como receptor, tendrás que informar del pago efectivo completo en <strong>4 días naturales excluyendo sábados, domingos y festivos nacionales</strong> (art. 12.3), con la fecha de vencimiento. Mira <a href="/blog/informar-pago-factura-4-dias/">cómo contar el plazo de 4 días</a> y revisa tus <a href="/blog/plazos-pago-ley-morosidad/">plazos de pago de la Ley 3/2004</a>: lo que pagues tarde quedará registrado.</p>

<h2 id="preparar">Plan de preparación (12 meses)</h2>
<ol class="steps">
<li><strong>Confirma que estás en este grupo</strong>: calcula el volumen de operaciones del año anterior.</li>
<li><strong>Elige vía</strong>: plataforma privada con interconexión (art. 8) o solución pública, o una combinación.</li>
<li><strong>Publica tu punto de entrada</strong> de facturas si usas una plataforma privada. Si no lo haces, se entenderá que es la solución pública (art. 6.3).</li>
<li><strong>Habla con tus proveedores y clientes grandes</strong> sobre formato y datos extra: solo puedes exigir datos adicionales si los pactaste (art. 7.6).</li>
<li><strong>Prueba el flujo de pagos</strong> con tesorería: fecha efectiva, vencimiento y rechazos.</li>
</ol>
<p>Este post resume el texto vigente; no sustituye el asesoramiento de tu gestor. Si eres autónomo o pyme, mira la <a href="/blog/factura-electronica-obligatoria-autonomos/">guía para autónomos</a>.</p>
""",
    faq=[
        ("¿Cuándo es obligatoria la factura electrónica para empresas de más de 8 millones?", "Según el calendario de la AEAT, desde el 6 de octubre de 2027, doce meses después de la entrada en vigor de la Orden HAC/1028/2026."),
        ("¿Qué es el volumen de operaciones?", "El concepto del artículo 121 de la Ley del IVA, referido al año natural anterior. No coincide siempre con la cifra de negocios contable."),
        ("¿Hay que enviar un PDF además de la factura electrónica?", "Sí, durante los 12 primeros meses, salvo que el destinatario acepte expresamente recibirla solo en formato original (disposición transitoria segunda). El PDF no se envía a la solución pública."),
        ("¿Las facturas simplificadas entran?", "No, salvo las facturas simplificadas cualificadas del artículo 7.2 del Reglamento de facturación (art. 4.1 del RD 238/2026)."),
        ("¿Es gratis la solución pública de la AEAT?", "Sí. El artículo 11.10 establece que el acceso a la solución pública y a sus usos es gratuito para los usuarios."),
        ("¿Y las empresas de 8 millones o menos?", "Empiezan el 6 de octubre de 2028. Los autónomos de ese tamaño informan de los estados de la factura un año después."),
    ],
    sources=[S.RD238, S.ORDEN1028, S.AEAT_CAL, S.LEY18],
))

# ---------------------------------------------------------------- #21 factura electrónica cómo se hace
POSTS.append(dict(
    slug="factura-electronica-como-se-hace",
    published="2026-11-15",
    title="Factura electrónica obligatoria: cómo se hace paso a paso",
    desc="Cómo emitir y recibir factura electrónica entre empresas (RD 238/2026): formatos, plataforma privada o pública, firma, punto de entrada y estados.",
    h1="Factura electrónica obligatoria: cómo se hace, paso a paso",
    intro="Qué pasos seguir para emitir y recibir una factura electrónica entre empresarios y profesionales según el Real Decreto 238/2026: formato, vía, firma, punto de entrada, estados y pago. Revisado en el BOE el 15 de noviembre de 2026.",
    content="""
<p class="note"><strong>Respuesta corta:</strong> la factura electrónica obligatoria no es un PDF. Es un <strong>mensaje estructurado</strong> (modelo EN16931) que se emite y se recibe por una plataforma privada, por la solución pública de la AEAT o por ambas. Primero mira <a href="/factura-electronica-obligatoria/">desde cuándo te afecta</a>; luego sigue estos pasos.</p>

<h2 id="p1">Paso 1: confirma que tu operación entra</h2>
<p>La obligación afecta a las facturas entre empresarios o profesionales cuando el destinatario tiene en España su sede, un establecimiento permanente o su domicilio (art. 3.1). Las facturas simplificadas quedan exceptuadas, salvo las simplificadas cualificadas (art. 4.1). El primer grupo es el de más de 8 millones, desde el 6 de octubre de 2027; el resto, desde el 6 de octubre de 2028.</p>

<h2 id="p2">Paso 2: elige la vía</h2>
<p>El sistema español de factura electrónica son las plataformas privadas de intercambio más la solución pública de la AEAT (art. 5). Tienes tres opciones:</p>
<ul>
<li><strong>Solución pública</strong>: gestionada por la AEAT, de uso gratuito (art. 11.10). Debes usar sintaxis UBL (art. 11.2).</li>
<li><strong>Plataforma privada</strong>: tu proveedor de software. Debe interconectarse con otras plataformas si un cliente lo pide, en un máximo de un mes (arts. 8 y 9).</li>
<li><strong>Ambas</strong>: por ejemplo, emites desde tu programa y recibes por la solución pública.</li>
</ul>
<p>Si no has acordado con tus proveedores recibir por plataformas privadas, se entiende que has optado por la solución pública sin tener que declararlo (art. 6.1).</p>

<h2 id="p3">Paso 3: genera la factura en un formato admitido</h2>
<p>La factura debe seguir el modelo semántico EN16931 y una de estas sintaxis: <strong>CII, UBL, EDIFACT o Facturae</strong> (art. 7.1). El contenido mínimo es el del Reglamento de facturación (RD 1619/2012). Además, todas llevan un <strong>código único</strong> que incluye el NIF del emisor, el número y serie y la fecha de expedición (art. 7.5). Tu programa debería generarlo solo; si usas una hoja de cálculo, no basta.</p>
<p>La disposición adicional primera prevé un formulario de generación de facturas electrónicas, útil para quien emite pocas.</p>

<h2 id="p4">Paso 4: firma y envía</h2>
<ul>
<li>Por plataforma privada: las facturas deben ir con <strong>firma electrónica avanzada</strong>, del emisor o delegada (art. 7.3).</li>
<li>Si no emites por la solución pública, tu sistema debe enviarle <strong>copia fiel en UBL</strong> en el momento de emitir (art. 6.2).</li>
<li>Si tu cliente usa una plataforma distinta, las partes acuerdan la sintaxis; sin acuerdo, se usa la de la solución pública (art. 7.4).</li>
</ul>

<h2 id="p5">Paso 5: da a conocer tu punto de entrada</h2>
<p>Quien reciba por plataforma privada debe hacer público su punto de entrada en sus comunicaciones y, si la tiene, en su web (art. 6.3). Si no lo identificas, se considera punto de entrada la solución pública. Los operadores deben ofrecer una consulta abierta para saber quién los ha elegido (art. 6.4).</p>

<h2 id="p6">Paso 6: gestiona los estados y el pago</h2>
<p>Quien recibe la factura debe informar al emisor de la aceptación o rechazo y del pago efectivo completo (art. 10.1), y comunicar el pago y su vencimiento a la solución pública en <strong>4 días naturales sin contar sábados, domingos ni festivos nacionales</strong> (art. 12.3). Sin rechazo ni rectificativa, la factura se presume aceptada (art. 12.1). Los detalles están en <a href="/blog/informar-pago-factura-4-dias/">cómo contar el plazo de 4 días</a>.</p>

<h2 id="errores">Errores habituales</h2>
<div class="table-wrap"><table>
<thead><tr><th>Error</th><th>Por qué falla</th></tr></thead>
<tbody>
<tr><td>Enviar un PDF por correo</td><td>No es un mensaje estructurado EN16931 (art. 7.1)</td></tr>
<tr><td>Pedir datos extra al proveedor sin avisar</td><td>Solo pueden exigirse si se enviaron antes de la operación (art. 7.6)</td></tr>
<tr><td>No publicar el punto de entrada</td><td>Se entenderá que es la solución pública (art. 6.3)</td></tr>
<tr><td>Dejar pasar una factura sin rechazar</td><td>Se presume aceptada (art. 12.1)</td></tr>
</tbody></table></div>
<p>Si el cliente no paga, mira cómo <a href="/blog/reclamar-factura-impagada-intereses/">reclamar con intereses y 40 euros</a>.</p>
""",
    faq=[
        ("¿Basta con enviar un PDF?", "No. La factura electrónica obligatoria es un mensaje estructurado EN16931 en CII, UBL, EDIFACT o Facturae (art. 7.1 del RD 238/2026)."),
        ("¿Tengo que contratar una plataforma de pago?", "No necesariamente. La solución pública de la AEAT es gratuita (art. 11.10) y puede usarse como única vía."),
        ("¿Qué formato debo usar en la solución pública?", "UBL, en los términos de la orden ministerial que la regula (art. 11.2)."),
        ("¿Qué es el punto de entrada de facturas?", "La plataforma o vía por la que eliges recibir facturas. Si no lo declaras, se entiende que es la solución pública (art. 6.3)."),
        ("¿Quién informa del pago?", "El destinatario de la factura, en 4 días naturales sin sábados, domingos ni festivos nacionales (art. 12.3)."),
        ("¿Se puede rechazar una factura?", "Sí. Si no se rechaza ni hay factura rectificativa posterior, se presume aceptada (art. 12.1)."),
    ],
    sources=[S.RD238, S.ORDEN1028, S.AEAT_CAL, S.ROF],
))

# ---------------------------------------------------------------- #26 PMP memoria abreviada
POSTS.append(dict(
    slug="periodo-medio-pago-memoria-abreviada",
    published="2026-11-15",
    title="PMP en la memoria abreviada: fórmula con saldos",
    desc="Periodo medio de pago en memoria abreviada o PGC Pymes: fórmula del art. 5.5 de la resolución del ICAC, ejemplos con cifras y nota a incluir.",
    h1="Periodo medio de pago en la memoria abreviada: la fórmula con saldos medios",
    intro="Si tu sociedad presenta memoria abreviada o aplica el PGC de Pymes, el cálculo del periodo medio de pago es más sencillo que en el modelo normal. Fórmula, ejemplos y nota a incluir, según la Resolución del ICAC de 29 de enero de 2016. Revisado el 15 de noviembre de 2026.",
    content="""
<p class="note"><strong>Respuesta corta:</strong> en memoria abreviada o PGC Pymes, el periodo medio de pago es <strong>saldo medio de acreedores comerciales ÷ compras netas y gastos por servicios exteriores × 365</strong> (art. 5.5 de la resolución del ICAC). Calcúlalo con la <a href="/periodo-medio-pago-proveedores/">calculadora de periodo medio de pago</a>, que incluye este modo.</p>

<h2 id="quien">Quién usa esta fórmula</h2>
<p>Las sociedades mercantiles que elaboren la memoria en el modelo abreviado del Plan General de Contabilidad, o que opten por el PGC de Pymes, calculan el periodo con esta fórmula (art. 5.5). Las que presentan el modelo normal usan otra, basada en ratios de operaciones pagadas y pendientes con importes y días de cada factura. La información procede del deber de información de la disposición adicional tercera de la Ley 15/2010.</p>

<h2 id="formula">La fórmula</h2>
<p><strong>PMP = saldo medio de acreedores comerciales / (compras netas + gastos por servicios exteriores) × 365</strong></p>
<ul>
<li><strong>Acreedores comerciales</strong>: las partidas de proveedores y acreedores varios por deudas con suministradores de bienes o servicios incluidos en el alcance de la normativa de plazos legales de pago.</li>
<li><strong>Compras netas y gastos por servicios exteriores</strong>: los importes contabilizados como tales en los subgrupos de la quinta parte del PGC o del PGC de Pymes.</li>
</ul>
<p>La resolución no define aquí «saldo medio»; una práctica habitual es la media entre el saldo inicial y el final del ejercicio, que es la que usa nuestra calculadora. Si tu auditor usa otro criterio, sigue el suyo.</p>

<h2 id="ejemplos">Dos ejemplos con cifras</h2>
<div class="table-wrap"><table>
<thead><tr><th>Dato</th><th>Empresa A</th><th>Empresa B</th></tr></thead>
<tbody>
<tr><td>Acreedores comerciales iniciales</td><td>70.000 €</td><td>100.000 €</td></tr>
<tr><td>Acreedores comerciales finales</td><td>90.000 €</td><td>140.000 €</td></tr>
<tr><td>Saldo medio</td><td>80.000 €</td><td>120.000 €</td></tr>
<tr><td>Compras netas y servicios exteriores</td><td>600.000 €</td><td>720.000 €</td></tr>
<tr><td>PMP (×365)</td><td>48,67 días</td><td>60,83 días</td></tr>
</tbody></table></div>
<p>La empresa A queda por debajo de 60 días. La B los supera por menos de un día, pero lo supera: el máximo de la <a href="/blog/plazos-pago-ley-morosidad/">Ley de morosidad</a> para pagar es de 60 días, y conviene explicar en la memoria las circunstancias que distorsionen el resultado.</p>

<h2 id="nota">Qué poner en la nota de la memoria</h2>
<p>El artículo 6.3 pide una nota titulada «Información sobre el periodo medio de pago a proveedores. Disposición adicional tercera. «Deber de información» de la Ley 15/2010, de 5 de julio» con un cuadro de una línea: periodo medio de pago a proveedores, en días, del ejercicio actual (N) y del anterior (N-1). La resolución también permite añadir cualquier información que la sociedad considere adecuada para aclarar circunstancias que distorsionen el resultado.</p>

<h2 id="errores">Errores frecuentes</h2>
<ol class="steps">
<li><strong>Usar todas las cuentas del pasivo</strong>: solo cuentan los acreedores comerciales del alcance de la norma, no préstamos ni deudas con Hacienda.</li>
<li><strong>Olvidar los servicios exteriores</strong>: el denominador suma compras netas y gastos por servicios exteriores.</li>
<li><strong>Dividir entre 360</strong>: la fórmula multiplica por 365.</li>
<li><strong>Mezclar fórmulas</strong>: si presentas modelo normal, usa el cálculo por ratios; mira <a href="/blog/calcular-periodo-medio-pago-proveedores-ejemplo/">el ejemplo con facturas</a>.</li>
</ol>
""",
    faq=[
        ("¿Qué fórmula usa la memoria abreviada?", "Saldo medio de acreedores comerciales dividido entre compras netas y gastos por servicios exteriores, por 365 (art. 5.5 de la resolución del ICAC de 2016)."),
        ("¿Quién puede usar esta fórmula?", "Las sociedades que elaboren la memoria en modelo abreviado o apliquen el PGC de Pymes."),
        ("¿Qué entra en acreedores comerciales?", "Proveedores y acreedores varios por deudas con suministradores de bienes o servicios incluidos en el alcance de la normativa de plazos legales de pago."),
        ("¿Cómo se calcula el saldo medio?", "La resolución no lo detalla en este artículo. Es habitual usar la media entre el saldo inicial y el final; confírmalo con tu auditor o asesor."),
        ("¿Qué debo incluir en la memoria?", "Una nota con el periodo medio de pago a proveedores, en días, del ejercicio actual y del anterior (art. 6.3)."),
        ("¿Y si tengo modelo normal de memoria?", "Se usa la fórmula con ratios de operaciones pagadas y pendientes de pago (art. 5.1 a 5.4)."),
    ],
    sources=[S.ICAC, S.LEY15, S.LEY3],
))


POSTS.append(dict(
    slug="solucion-publica-factura-electronica-aeat",
    published="2026-11-16",
    title="Solución pública de facturación electrónica de la AEAT",
    desc="Qué es la solución pública de facturación electrónica de la AEAT, quién la usa, si es gratis y qué ocurre si no eliges plataforma privada. Según el BOE.",
    h1="Solución pública de facturación electrónica de la AEAT: qué es y cómo funciona",
    intro="La obligación de facturar electrónicamente entre empresarios y profesionales viene con una alternativa pública y gratuita gestionada por la Agencia Tributaria. Qué dice el Real Decreto 238/2026 sobre ella, para qué sirve y qué pasa si no eliges plataforma privada. Revisado el 16 de noviembre de 2026.",
    content="""
<p class="note"><strong>Respuesta corta:</strong> la solución pública de facturación electrónica es el sistema de la AEAT para emitir y recibir facturas electrónicas entre empresarios y profesionales. Su acceso y sus usos son <strong>gratuitos</strong> (RD 238/2026) y es el punto de entrada por defecto de quien no designe una plataforma privada. Comprueba tu calendario con el <a href="/factura-electronica-obligatoria/">test de factura electrónica obligatoria</a>.</p>

<h2 id="que-es">Qué es y de dónde sale</h2>
<p>El sistema español de factura electrónica B2B se compone de dos vías: las <strong>plataformas privadas de intercambio</strong> de facturas electrónicas y la <strong>solución pública de facturación electrónica</strong> (art. 5 del Real Decreto 238/2026). La segunda se apoya en la disposición adicional vigesimoprimera de la Ley 56/2007, que encarga a la AEAT desarrollarla y gestionarla con carácter voluntario para los obligados a emitir y recibir facturas electrónicas. Su desarrollo técnico lo regula la Orden HAC/1028/2026, en vigor desde el 6 de octubre de 2026.</p>
<p>Según la exposición de motivos del real decreto, se creó porque muchas peticiones de la consulta pública pedían una vía sencilla y asequible para pymes y profesionales.</p>

<h2 id="gratis">¿Es gratis?</h2>
<p>Sí. La exposición de motivos afirma que el acceso a la solución pública y sus distintos usos tendrán carácter gratuito para los usuarios. Además, la disposición adicional primera encarga a la AEAT una aplicación o formulario gratuito que permita expedir facturas electrónicas, generar la información sobre su estado (incluido el pago efectivo completo) y ponerla a disposición de las contrapartes y de la Administración, utilizando la solución pública. Las facturas expedidas con ese formulario serán verificables conforme al artículo 6.5.b) del Reglamento de facturación.</p>
<p>No confundas esta herramienta con la <a href="/blog/verifactu-gratis-aplicacion-aeat/">aplicación gratuita de Verifactu</a>: son sistemas distintos con obligaciones distintas.</p>

<h2 id="defecto">Qué pasa si no eliges plataforma privada</h2>
<p>El artículo 6.1 establece que, si no has acordado expresamente con tus proveedores recibir las facturas por una o varias plataformas privadas, se entiende que <strong>optas por la solución pública</strong> sin manifestación expresa. Y el 6.3 añade que, si no identificas públicamente tu punto de entrada de facturas, se entiende que es la solución pública. En cambio, quien recibe por plataforma privada debe hacer público su punto o puntos de entrada en todas sus comunicaciones con otros empresarios y profesionales y, si tiene, en su web.</p>

<h2 id="copias">Copias de facturas desde plataformas privadas</h2>
<p>Aunque uses una plataforma privada, esta debe remitir a la solución pública, simultáneamente a la emisión, una <strong>copia electrónica fiel en sintaxis UBL</strong> de cada factura, marcada claramente como copia (art. 6.2). Según la exposición de motivos, el objetivo es que la Administración, junto con los estados de la factura, calcule y monitorice los plazos de pago.</p>

<h2 id="pago">La comunicación del pago</h2>
<p>Los destinatarios de las facturas deben comunicar el pago efectivo completo a la solución pública (art. 12), con independencia de la vía usada para facturar. El cómputo del plazo se explica en la guía sobre <a href="/blog/informar-pago-factura-4-dias/">informar del pago en 4 días</a>. A efectos estadísticos, la disposición adicional séptima fija como inicio del cómputo la recepción de la factura electrónica y, si no se comunicó, la fecha de expedición.</p>

<h2 id="tabla">Pública o privada: resumen</h2>
<div class="table-wrap"><table>
<thead><tr><th>Aspecto</th><th>Solución pública (AEAT)</th><th>Plataforma privada</th></tr></thead>
<tbody>
<tr><td>Coste</td><td>Gratuita para el usuario</td><td>Lo fija cada operador</td></tr>
<tr><td>Punto de entrada si no eliges</td><td>Sí, por defecto</td><td>Solo si lo acuerdas y lo publicas</td></tr>
<tr><td>Copia de facturas en UBL</td><td>Es el destino</td><td>Debe enviarla a la solución pública</td></tr>
<tr><td>Comunicar el pago</td><td>Obligatorio para el destinatario</td><td>Igualmente a la solución pública</td></tr>
</tbody></table></div>

<h2 id="fechas">Cuándo te afecta</h2>
<p>Las fechas de aplicación (6 de octubre de 2027 para las empresas de más de 8 millones de volumen de operaciones y 6 de octubre de 2028 para el resto, según el calendario de la AEAT) están en la <a href="/blog/factura-electronica-obligatoria-2027-empresas/">guía de empresas de más de 8 M€</a>. La disposición adicional quinta exige que la solución pública esté disponible al menos dos meses antes de la primera aplicación efectiva.</p>
<p>Si quieres preparar el proceso paso a paso, consulta <a href="/blog/factura-electronica-como-se-hace/">cómo se hace una factura electrónica</a>.</p>
""",
    faq=[
        ("¿Qué es la solución pública de facturación electrónica?", "El sistema de la AEAT para emitir, recibir y comunicar el estado de las facturas electrónicas entre empresarios y profesionales (RD 238/2026)."),
        ("¿Es gratuita?", "Sí. El real decreto indica que su acceso y usos son gratuitos para los usuarios, y la AEAT debe ofrecer además un formulario gratuito."),
        ("¿Estoy obligado a usarla?", "No necesariamente: puedes usar plataformas privadas o combinar ambas vías. Si no designas ninguna, se entiende que optas por la pública."),
        ("¿Qué es una copia fiel en UBL?", "La copia electrónica de cada factura que una plataforma privada debe enviar a la solución pública cuando se emite."),
        ("¿Quién comunica el pago?", "El destinatario de la factura, con el pago efectivo completo, a la solución pública (art. 12)."),
        ("¿Y en País Vasco y Navarra?", "La disposición adicional tercera remite a lo dispuesto en el Concierto y el Convenio y a los acuerdos entre Haciendas Forales y AEAT."),
    ],
    sources=[S.RD238, S.ORDEN1028, S.AEAT_CAL],
))

POSTS.append(dict(
    slug="factura-electronica-pais-vasco-navarra",
    published="2026-11-16",
    title="Factura electrónica obligatoria en País Vasco y Navarra",
    desc="Qué dice el BOE sobre la factura electrónica B2B en los territorios forales: disposición adicional tercera del RD 238/2026 y qué falta por concretar.",
    h1="Factura electrónica obligatoria en País Vasco y Navarra: qué dice el BOE",
    intro="Si tu empresa tributa en Álava, Bizkaia, Gipuzkoa o Navarra, te preguntarás si el calendario de factura electrónica es el mismo. Lo que dice el Real Decreto 238/2026 sobre los territorios forales, lo que remite a otros acuerdos y lo que debes comprobar. Revisado el 16 de noviembre de 2026.",
    content="""
<p class="note"><strong>Respuesta corta:</strong> el RD 238/2026 incluye una disposición adicional (la tercera) para las Haciendas Forales: la solución pública para quienes tributan según el Concierto Económico vasco o el Convenio navarro <strong>se realizará atendiendo a lo dispuesto en esos regímenes</strong>, mediante acuerdos entre las Haciendas Forales y la AEAT. No inventes fechas propias: consulta a tu Hacienda Foral o asesor.</p>

<h2 id="texto">Lo que dice el texto</h2>
<p>La disposición adicional tercera del real decreto, titulada «Administraciones tributarias forales y solución pública de facturación electrónica», dispone que la solución pública para los empresarios o profesionales sometidos a la normativa tributaria de los territorios forales, conforme al Concierto Económico con la Comunidad Autónoma del País Vasco y al Convenio Económico entre el Estado y la Comunidad Foral de Navarra, se realizará atendiendo a lo dispuesto en los mismos, estableciéndose los oportunos acuerdos entre las Haciendas Forales y la Agencia Estatal de Administración Tributaria conforme al principio de colaboración.</p>
<p>La disposición adicional cuarta garantiza, además, que las administraciones tributarias, incluidas las forales, accedan a la información de la solución pública conforme al marco legal aplicable. Los datos tienen carácter reservado y podrán cederse, conforme al artículo 95 de la Ley General Tributaria, para la aplicación de los tributos cuya gestión compete a las Administraciones de los Territorios Históricos y de Navarra.</p>

<h2 id="obligacion">¿Hay obligación de facturar electrónicamente?</h2>
<p>La obligación de la factura electrónica entre empresarios y profesionales procede de la Ley 56/2007, modificada por la Ley 18/2022, que el real decreto desarrolla. El texto del real decreto que he revisado no establece una fecha distinta para los territorios forales, pero tampoco la detalla: remite a los acuerdos entre administraciones. Por eso, la respuesta prudente es verificar en tu Hacienda Foral cómo se aplica a tu caso.</p>
<div class="table-wrap"><table>
<thead><tr><th>Cuestión</th><th>Qué dice el RD 238/2026</th><th>Qué comprobar</th></tr></thead>
<tbody>
<tr><td>Solución pública en territorios forales</td><td>Se realizará según el Concierto o el Convenio (DA 3.ª)</td><td>Acuerdos Haciendas Forales–AEAT</td></tr>
<tr><td>Acceso de Haciendas Forales a los datos</td><td>Garantizado conforme al marco legal (DA 4.ª)</td><td>—</td></tr>
<tr><td>Rectificativas con autorización</td><td>Se menciona a empresarios autorizados por la AEAT o las Haciendas Forales</td><td>Tu autorización concreta</td></tr>
<tr><td>Fechas de aplicación</td><td>No se detallan específicamente para territorios forales</td><td>Calendario de tu Hacienda Foral</td></tr>
</tbody></table></div>

<h2 id="verifactu">¿Y Verifactu y TicketBAI?</h2>
<p>No lo mezcles: la factura electrónica B2B es una obligación distinta del sistema de facturación Verifactu. En los territorios forales hay sistemas propios para los sistemas informáticos de facturación (por ejemplo TicketBAI en el País Vasco), que no se tratan en este real decreto. La comparación se explica en las guías de <a href="/blog/diferencias-verifactu-factura-electronica-b2b/">diferencias entre Verifactu y factura electrónica B2B</a> y del <a href="/blog/verifactu-autonomos/">autónomo</a>.</p>

<h2 id="pasos">Qué hacer ahora</h2>
<ol class="steps">
<li><strong>Confirma tu régimen</strong>: si tributas en territorio común o foral (domicilio fiscal y volumen de operaciones).</li>
<li><strong>Haz el test</strong>: nuestro <a href="/factura-electronica-obligatoria/">comprobador</a> orienta con los datos estatales; no sustituye el criterio foral.</li>
<li><strong>Consulta a tu Hacienda Foral</strong> o asesor sobre el acuerdo con la AEAT y la solución pública.</li>
<li><strong>Prepara el proceso</strong>: formatos, firma y comunicación de pagos según <a href="/blog/factura-electronica-como-se-hace/">la guía paso a paso</a>.</li>
</ol>
<p>Más información sobre la herramienta estatal en <a href="/blog/solucion-publica-factura-electronica-aeat/">la solución pública de la AEAT</a>.</p>
""",
    faq=[
        ("¿Se aplica el RD 238/2026 en País Vasco y Navarra?", "Contiene una disposición adicional específica: la solución pública se aplicará según el Concierto y el Convenio, con acuerdos entre Haciendas Forales y AEAT."),
        ("¿Hay fechas distintas para los territorios forales?", "El texto revisado no las detalla. Verifica con tu Hacienda Foral."),
        ("¿Pueden las Haciendas Forales ver las facturas?", "La DA 4.ª garantiza su acceso a la información de la solución pública conforme al marco legal aplicable."),
        ("¿Es lo mismo que TicketBAI?", "No. TicketBAI es un sistema foral de facturación; la factura electrónica B2B es otra obligación."),
        ("¿Sirve vuestro test para empresas forales?", "Orienta con los datos estatales, pero no sustituye lo que determine tu Hacienda Foral."),
    ],
    sources=[S.RD238, S.LEY18, S.AEAT_CAL],
))

POSTS.append(dict(
    slug="periodo-medio-pago-maximo-legal",
    published="2026-11-16",
    title="Periodo medio de pago: máximo legal de 60 días y plazos",
    desc="Máximo legal del periodo medio de pago a proveedores: 30 días por defecto y 60 pactados (Ley 3/2004), qué debes informar y ejemplos de cálculo.",
    h1="Periodo medio de pago a proveedores: máximo legal y qué debes informar",
    intro="El «máximo legal» del periodo medio de pago no es una cifra única que aparezca en la ley del periodo medio. Qué plazos fija la Ley 3/2004, qué exige la Ley 15/2010 sobre el deber de información y cómo comparar tu resultado. Revisado el 16 de noviembre de 2026.",
    content="""
<p class="note"><strong>Respuesta corta:</strong> la normativa de morosidad fija un plazo de pago de <strong>30 días naturales</strong> por defecto, ampliable por pacto hasta <strong>60 días naturales</strong> como máximo (art. 4 de la Ley 3/2004). Es la referencia para comparar tu periodo medio de pago. Calcúlalo con la <a href="/periodo-medio-pago-proveedores/">calculadora</a>.</p>

<h2 id="plazos">Los plazos de la Ley 3/2004</h2>
<ul>
<li><strong>30 días naturales</strong> desde la recepción de las mercancías o la prestación de servicios, si el contrato no fija fecha o plazo (art. 4.1).</li>
<li><strong>Procedimiento de aceptación</strong>: no puede exceder de 30 días naturales, y el plazo de pago son 30 días desde la aceptación (art. 4.2).</li>
<li><strong>Pacto entre las partes</strong>: se puede ampliar, pero nunca por encima de 60 días naturales (art. 4.3).</li>
</ul>
<p>La Ley 15/2010, que reformó la norma, explica en su preámbulo que el plazo máximo de 60 días no podrá ampliarse por acuerdo entre las partes, para evitar prácticas abusivas de grandes empresas sobre pequeños proveedores. Más detalle en la guía de <a href="/blog/plazos-pago-ley-morosidad/">plazos de la Ley de morosidad</a>.</p>

<h2 id="info">Qué exige el deber de información</h2>
<p>La disposición adicional tercera de la Ley 15/2010 obliga a todas las sociedades mercantiles a incluir en la memoria de sus cuentas anuales su periodo medio de pago a proveedores. Además:</p>
<ul>
<li>Las <strong>cotizadas</strong> publican en su web el periodo medio de pago, el volumen monetario y número de facturas pagadas en un periodo inferior al máximo establecido en la normativa de morosidad, y los porcentajes sobre el total.</li>
<li>Las <strong>no cotizadas que no presenten cuentas abreviadas</strong> publican esos datos en su web, si la tienen, e incluyen la información en la memoria.</li>
</ul>
<p>Observa que la ley habla del «máximo establecido en la normativa de morosidad», y no define una cifra distinta: la referencia es el plazo del art. 4 de la Ley 3/2004.</p>

<h2 id="ejemplo">Ejemplo: comparar con 60 días</h2>
<div class="table-wrap"><table>
<thead><tr><th>Dato (ejemplo)</th><th>Empresa C</th><th>Empresa D</th></tr></thead>
<tbody>
<tr><td>Saldo medio de acreedores comerciales</td><td>45.000 €</td><td>90.000 €</td></tr>
<tr><td>Compras netas y servicios exteriores</td><td>540.000 €</td><td>480.000 €</td></tr>
<tr><td>PMP (saldo medio ÷ compras × 365)</td><td>30,42 días</td><td>68,44 días</td></tr>
<tr><td>Frente a 60 días</td><td>Por debajo</td><td>Por encima</td></tr>
</tbody></table></div>
<p>El cálculo usa la fórmula de la <a href="/blog/periodo-medio-pago-memoria-abreviada/">memoria abreviada</a>. La empresa D tendría que revisar sus condiciones de pago y explicar las circunstancias que distorsionen el resultado en la nota de la memoria.</p>

<h2 id="matices">Matices importantes</h2>
<ol class="steps">
<li><strong>Un periodo medio no es un plazo por factura</strong>: puedes tener una media baja y facturas individuales en mora.</li>
<li><strong>Si pagas tarde, hay intereses</strong>: consulta el <a href="/blog/tipo-interes-demora-2026/">tipo de interés de demora vigente</a> y la <a href="/intereses-demora-comerciales/">calculadora</a>.</li>
<li><strong>Sectores especiales</strong>: la ley incluye plazos específicos, como 30 días para productos de alimentación frescos y perecederos (Ley 15/2010).</li>
<li><strong>Modelo normal o abreviado</strong>: cada uno usa una fórmula distinta; mira el <a href="/blog/calcular-periodo-medio-pago-proveedores-ejemplo/">ejemplo con facturas</a>.</li>
</ol>
""",
    faq=[
        ("¿Cuál es el máximo legal del periodo medio de pago?", "La referencia es el plazo máximo de la normativa de morosidad: 60 días naturales pactados (art. 4.3 Ley 3/2004), con 30 días por defecto."),
        ("¿Qué sociedades deben informar su periodo medio de pago?", "Todas las sociedades mercantiles, en la memoria de sus cuentas anuales (DA 3.ª Ley 15/2010)."),
        ("¿Hay plazos distintos para alimentación?", "Sí, la Ley 15/2010 fija 30 días para productos de alimentación frescos y perecederos."),
        ("¿Debo publicarlo en mi web?", "Cotizadas y no cotizadas sin cuentas abreviadas, en los términos de la DA 3.ª, si tienen web."),
        ("¿Qué hago si supero 60 días de media?", "Revisa tus condiciones de pago y explica las circunstancias en la memoria; consulta a tu asesor sobre otras consecuencias."),
    ],
    sources=[S.LEY3, S.LEY15, S.ICAC],
))

POSTS.append(dict(
    slug="verifactu-sii-exentos",
    published="2026-11-17",
    title="Verifactu y SII: quién queda fuera del reglamento",
    desc="Quién no está sometido al reglamento Verifactu: contribuyentes con libros del IVA por el SII, entidades exentas y operaciones excluidas (RD 1007/2023).",
    h1="Verifactu y SII: quién queda fuera del reglamento de facturación",
    intro="El reglamento de los sistemas informáticos de facturación no se aplica a todo el mundo ni a todas las operaciones. Quién queda fuera según el propio texto del BOE, con qué matices y cómo comprobar tu caso. Revisado el 17 de noviembre de 2026.",
    content="""
<p class="note"><strong>Respuesta corta:</strong> el art. 3.3 del Real Decreto 1007/2023 dice que el reglamento <strong>no se aplica a los contribuyentes que llevan los libros registro en los términos del art. 62.6 del Reglamento del IVA</strong>, que es la vía del Suministro Inmediato de Información (SII). Hay más exclusiones por tipo de entidad y de operación. Haz primero el <a href="/">test «¿estoy obligado?»</a>.</p>

<h2 id="sii">1. Contribuyentes que llevan los libros por el SII</h2>
<p>El art. 3.3 excluye del ámbito subjetivo a quienes llevan los libros registro del IVA en los términos del art. 62.6 del Reglamento del IVA (RD 1624/1992). El preámbulo del propio real decreto menciona el SII, implantado en 2017, como precedente de la información sobre el contenido de las facturas. Si tu empresa está en el SII, pregunta a tu asesor si esa exclusión te alcanza a todas tus operaciones.</p>

<h2 id="exentas">2. Entidades exentas del Impuesto sobre Sociedades</h2>
<p>El art. 3.1.a) incluye a los contribuyentes del Impuesto sobre Sociedades, pero <strong>no a las entidades exentas del art. 9.1 de la Ley 27/2014</strong>. Las parcialmente exentas (art. 9, apartados 2, 3 y 4) solo quedan sometidas por las operaciones que generen rentas sujetas y no exentas.</p>

<h2 id="operaciones">3. Operaciones que el reglamento no cubre</h2>
<p>El art. 4 enumera operaciones excluidas aunque el emisor sí esté obligado:</p>
<ul>
<li>Las de las disposiciones adicionales tercera y sexta del Reglamento de facturación (RD 1619/2012).</li>
<li>Las documentadas en facturas de operaciones realizadas por establecimientos permanentes en el extranjero.</li>
<li>Las facturas expedidas por el destinatario o por un tercero por disposiciones de obligado cumplimiento (art. 5 del Reglamento de facturación), siempre que se lleven los libros según el art. 62.6 del Reglamento del IVA.</li>
</ul>

<h2 id="territorio">4. Territorio</h2>
<p>El reglamento se aplica en todo el territorio español, sin perjuicio de los regímenes forales de País Vasco y Navarra. A los obligados con domicilio fiscal en territorio común sí se les aplica, aunque operen allí. Para los demás, consulta la <a href="/blog/factura-electronica-pais-vasco-navarra/">guía sobre País Vasco y Navarra</a> y la comparativa <a href="/blog/verifactu-ticketbai-diferencias/">Verifactu y TicketBAI</a>.</p>

<h2 id="no-aplicacion">5. Solicitar la no aplicación</h2>
<p>El art. 5 permite que el Departamento de Inspección Financiera y Tributaria de la AEAT resuelva la no aplicación, a petición del interesado, para sectores o contribuyentes concretos cuando lo justifiquen las prácticas del sector, o ante circunstancias técnicas excepcionales. Puede ser temporal y llevar condiciones especiales.</p>

<h2 id="resumen">Cuadro resumen</h2>
<div class="table-wrap"><table>
<thead><tr><th>Caso</th><th>¿Sometido al reglamento?</th><th>Base</th></tr></thead>
<tbody>
<tr><td>Libros del IVA por SII (art. 62.6 RIVA)</td><td>No</td><td>Art. 3.3</td></tr>
<tr><td>Entidad exenta (art. 9.1 Ley 27/2014)</td><td>No</td><td>Art. 3.1.a)</td></tr>
<tr><td>Entidad parcialmente exenta</td><td>Solo por rentas sujetas y no exentas</td><td>Art. 3.1.a)</td></tr>
<tr><td>Autónomo con actividad económica</td><td>Sí</td><td>Art. 3.1.b)</td></tr>
<tr><td>Sociedad (IS) no exenta</td><td>Sí</td><td>Art. 3.1.a)</td></tr>
</tbody></table></div>
<p>Esta guía no sustituye el asesoramiento profesional: la exclusión del SII depende de tu situación concreta. Los plazos generales están en <a href="/blog/fechas-verifactu-2027-2028/">fechas de Verifactu</a>.</p>
""",
    faq=[
        ("¿Estoy excluido de Verifactu si estoy en el SII?", "El art. 3.3 excluye a quienes llevan los libros registro en los términos del art. 62.6 del Reglamento del IVA, que es la vía del SII. Confirma tu caso con tu asesor."),
        ("¿Las asociaciones sin ánimo de lucro están obligadas?", "Las entidades exentas del art. 9.1 de la Ley 27/2014 no; las parcialmente exentas solo por operaciones con rentas sujetas y no exentas."),
        ("¿Se puede pedir quedar fuera del reglamento?", "El art. 5 permite solicitar la no aplicación a la AEAT en dos supuestos: prácticas del sector o circunstancias técnicas excepcionales."),
        ("¿Y si facturo desde el País Vasco o Navarra?", "El reglamento se aplica a obligados con domicilio fiscal en territorio común; los regímenes forales tienen su normativa."),
        ("¿Quién queda sometido siempre?", "Contribuyentes del IS no exentos, del IRPF con actividad económica, del IRNR con establecimiento permanente y entidades en atribución de rentas con actividad."),
    ],
    sources=[S.RD, S.ROF],
))

POSTS.append(dict(
    slug="verifactu-programa-facturacion-requisitos",
    published="2026-11-17",
    title="Requisitos de un programa de facturación Verifactu",
    desc="Qué exige el RD 1007/2023 a un software de facturación: integridad, trazabilidad, registro de eventos, huella, firma y declaración responsable del productor.",
    h1="Requisitos de un programa de facturación según el reglamento Verifactu",
    intro="Antes de contratar o cambiar de programa, conviene saber qué exige el reglamento a un sistema informático de facturación. Resumen artículo por artículo del Real Decreto 1007/2023. Revisado el 17 de noviembre de 2026.",
    content="""
<p class="note"><strong>Respuesta corta:</strong> el programa debe garantizar integridad, conservación, accesibilidad, legibilidad, trazabilidad e inalterabilidad de los registros de facturación (art. 8), generar un registro por cada factura (art. 9), añadir huella y, salvo en VERI*FACTU, firma electrónica (art. 12) y llevar una declaración responsable del productor (art. 13).</p>

<h2 id="registros">Registros de facturación</h2>
<p>El sistema genera automáticamente un <strong>registro de alta</strong> de forma simultánea o inmediatamente anterior a la expedición de cada factura (art. 9). Su contenido está en el art. 10: NIF y nombre del emisor, número y serie, fechas, tipo de factura, importe total, base, tipos y cuotas de IVA, datos del registro anterior con parte de su huella, código del sistema informático y fecha, hora, minuto y segundo de generación. Los importes se expresan en euros. Si se emite una factura por error, se genera un <strong>registro de anulación</strong> (art. 11). Puedes ver ambos en el <a href="/ejemplo-xml-verifactu/">ejemplo de XML</a>.</p>

<h2 id="garantias">Lo que debe garantizar (art. 8)</h2>
<ol class="steps">
<li><strong>Integridad e inalterabilidad</strong>: una vez generados, los registros no pueden alterarse sin que el sistema lo detecte y avise. Las correcciones se hacen con un registro adicional posterior.</li>
<li><strong>Trazabilidad</strong>: registros encadenados, de modo que se pueda seguir su secuencia desde el primero al último, y correctamente fechados.</li>
<li><strong>Conservación y exportación</strong>: durante el plazo de la Ley General Tributaria, con un procedimiento de descarga y archivo seguro en formato electrónico legible.</li>
<li><strong>Registro de eventos</strong>: recoge automáticamente interacciones y sucesos del sistema y se puede consultar desde él.</li>
<li><strong>Acceso disociado</strong>: la información con trascendencia tributaria se separa de la información confidencial no patrimonial.</li>
<li><strong>Capacidad de remisión</strong>: debe poder enviar los registros a la Administración por medios electrónicos.</li>
</ol>

<h2 id="huella">Huella y firma</h2>
<p>El art. 12 exige añadir una huella o hash a los registros de alta y de anulación y firmarlos electrónicamente. En los sistemas VERI*FACTU basta con calcular la huella (art. 16.3). Pruébalo con la <a href="/calcular-huella-verifactu/">calculadora de huella</a>.</p>

<h2 id="declaracion">Declaración responsable</h2>
<p>El productor certifica que el sistema cumple la Ley General Tributaria y el reglamento (art. 13). Debe constar por escrito y de modo visible en el programa, en cada versión, y entregarse al cliente al adquirirlo. El cliente o la AEAT pueden solicitarla. Incluye datos que identifican el sistema y al productor, y la fecha y lugar de la firma.</p>

<h2 id="elegir">Cómo usarlo al elegir programa</h2>
<div class="table-wrap"><table>
<thead><tr><th>Pregunta al proveedor</th><th>Artículo</th></tr></thead>
<tbody>
<tr><td>¿Puedo ver la declaración responsable de la versión que uso?</td><td>13</td></tr>
<tr><td>¿Genera registro de alta antes de emitir la factura?</td><td>9</td></tr>
<tr><td>¿Corrige con registros nuevos, sin borrar?</td><td>8.2.a)</td></tr>
<tr><td>¿Tiene registro de eventos y exportación?</td><td>8.2.c) y 8.3</td></tr>
<tr><td>¿Calcula huella y firma, o remite a la AEAT?</td><td>12 y 16</td></tr>
</tbody></table></div>
<p>La alternativa gratuita es la aplicación de la AEAT: ver <a href="/blog/verifactu-gratis-aplicacion-aeat/">Verifactu gratis</a>.</p>
""",
    faq=[
        ("¿Quién emite la declaración responsable?", "La persona o entidad productora del sistema informático (art. 13.1)."),
        ("¿Se pueden borrar facturas en el programa?", "No sin dejar rastro: las correcciones o anulaciones se hacen con al menos un registro adicional posterior (art. 8.2.a)."),
        ("¿Es obligatoria la firma electrónica?", "Sí para los sistemas no VERI*FACTU; los VERI*FACTU solo necesitan calcular la huella (art. 16.3)."),
        ("¿Qué es el registro de eventos?", "Un registro automático de interacciones y sucesos del sistema, consultable desde él (art. 8.3)."),
        ("¿Puedo usar un solo programa para varios obligados?", "Sí, si los registros de cada obligado están diferenciados y se cumplen los requisitos por separado (art. 7.a)."),
    ],
    sources=[S.RD],
))

POSTS.append(dict(
    slug="verifactu-modalidad-no-verifactu",
    published="2026-11-17",
    title="VERI*FACTU o no VERI*FACTU: qué modalidad elegir",
    desc="Diferencias entre enviar los registros a la AEAT (VERI*FACTU) y conservarlos en tu sistema: qué cambia en firma, frase y verificación (RD 1007/2023).",
    h1="VERI*FACTU o sistema sin envío: diferencias y cómo elegir",
    intro="El reglamento prevé dos caminos: un sistema que solo conserva los registros y otro que los envía a la AEAT («VERI*FACTU»). Qué cambia entre ambos según el texto del BOE. Revisado el 17 de noviembre de 2026.",
    content="""
<p class="note"><strong>Respuesta corta:</strong> en la modalidad VERI*FACTU el sistema remite todos los registros a la AEAT de forma continuada (arts. 15 y 16); a cambio no necesita firma electrónica, solo huella, y se presume que cumple por diseño los requisitos del art. 8. Sin envío, el sistema conserva los registros, los firma y debe poder entregarlos si la AEAT los requiere.</p>

<h2 id="dos">Las dos opciones</h2>
<p>El art. 7 ofrece dos recursos: (a) un sistema informático propio que cumpla la Ley General Tributaria y el reglamento, o (b) la aplicación que desarrolle la Administración. La aplicación de la AEAT tiene siempre la consideración de VERI*FACTU (art. 16.4). Un sistema del tipo (a) puede, además, optar por remitir los registros: la remisión es voluntaria (art. 15).</p>

<h2 id="tabla">Comparativa según el reglamento</h2>
<div class="table-wrap"><table>
<thead><tr><th>Aspecto</th><th>Sin envío a la AEAT</th><th>VERI*FACTU</th></tr></thead>
<tbody>
<tr><td>Envío de registros</td><td>Capacidad de remitir; entrega si se requiere (art. 14)</td><td>Remisión efectiva y continuada (art. 16.1)</td></tr>
<tr><td>Firma electrónica</td><td>Obligatoria (art. 12)</td><td>No; basta la huella (art. 16.3)</td></tr>
<tr><td>Frase en la factura</td><td>No</td><td>«Factura verificable en la sede electrónica de la AEAT» o «VERI*FACTU»</td></tr>
<tr><td>Cumplimiento del art. 8</td><td>Debe acreditarse</td><td>Se presume por diseño (art. 16.2)</td></tr>
<tr><td>QR en la factura</td><td>Sí</td><td>Sí</td></tr>
</tbody></table></div>
<p>La frase y el QR vienen de las modificaciones del Reglamento de facturación (art. 6.5): el QR va en todas las facturas expedidas con estos sistemas y la frase solo cuando el sistema remite todos los registros. Mira el <a href="/generador-qr-verifactu/">generador de QR</a> y la <a href="/blog/tamano-posicion-qr-verifactu/">guía de tamaño y posición</a>.</p>

<h2 id="permanencia">Cuánto dura la opción</h2>
<p>Se entiende que optas por VERI*FACTU al iniciar sistemáticamente la remisión de registros. La opción se prolonga al menos hasta el final del año natural del primer envío efectivo (art. 16.5).</p>

<h2 id="controlar">Control por parte de la AEAT y del receptor</h2>
<p>Sin envío, la AEAT puede personarse y exigir acceso a los registros de facturación y de eventos (art. 14). El receptor de cualquier factura puede enviar los datos del QR a la AEAT; con la frase VERI*FACTU puede comprobar que el emisor la remitió (art. 17). Compruébalo con el <a href="/validar-qr-verifactu/">validador de QR</a>.</p>

<h2 id="elegir">Cómo decidir</h2>
<ol class="steps">
<li>Consulta qué modalidad soporta tu programa; no todos permiten ambas.</li>
<li>Si quieres evitar la firma electrónica y la carga de acreditar el art. 8, la remisión lo simplifica.</li>
<li>Si prefieres no enviar nada de forma automática, necesitas un sistema con firma, registro de eventos y exportación.</li>
<li>Revisa la <a href="/blog/verifactu-programa-facturacion-requisitos/">lista de requisitos</a>, la <a href="/blog/huella-verifactu-que-es/">huella</a> y las <a href="/blog/fechas-verifactu-2027-2028/">fechas</a> antes de decidir.</li>
</ol>
""",
    faq=[
        ("¿Qué significa VERI*FACTU?", "Es el nombre de los «Sistemas de emisión de facturas verificables»: los que remiten efectivamente todos los registros de facturación a la AEAT (art. 16.1)."),
        ("¿Es obligatorio enviar los registros a la AEAT?", "No; el envío es voluntario (art. 15), aunque el sistema debe tener capacidad de remitir (art. 8.1)."),
        ("¿Qué frase debe llevar la factura?", "«Factura verificable en la sede electrónica de la AEAT» o «VERI*FACTU», solo si el sistema remite todos los registros."),
        ("¿La aplicación gratuita de la AEAT es VERI*FACTU?", "Sí, tiene esa consideración a todos los efectos (art. 16.4)."),
        ("¿Puedo cambiar de modalidad?", "La opción dura al menos hasta fin del año natural del primer envío (art. 16.5); consulta los plazos de renuncia en la normativa de desarrollo."),
    ],
    sources=[S.RD, S.ROF, S.ORDEN],
))

POSTS.append(dict(
    slug="verifactu-qr-obligatorio",
    published="2026-11-18",
    title="¿Es obligatorio el QR en todas las facturas Verifactu?",
    desc="Qué dice el BOE sobre el QR en facturas con sistemas Verifactu: cuándo es obligatorio, qué pasa en la factura electrónica y cuándo se añade la frase.",
    h1="¿Es obligatorio el código QR en todas las facturas Verifactu?",
    intro="Una de las dudas más repetidas: si el QR va siempre o solo en algunos casos. La respuesta está en el Reglamento de facturación, tal y como lo modifica el RD 1007/2023. Revisado el 18 de noviembre de 2026.",
    content="""
<p class="note"><strong>Respuesta corta:</strong> sí. Las facturas expedidas con los sistemas informáticos de facturación del reglamento deben incluir la representación gráfica de parte de su contenido mediante un código QR (art. 6.5.a del Reglamento de facturación). Si la factura es electrónica, el QR puede sustituirse por el contenido que representa. La frase «VERI*FACTU» es otra cosa: solo va si el sistema remite todos los registros a la AEAT.</p>

<h2 id="norma">Qué dice la norma</h2>
<p>La disposición final primera del RD 1007/2023 añade un apartado 5 al artículo 6 del Reglamento de facturación (RD 1619/2012). Según ese texto, en las facturas expedidas con los sistemas del artículo 7 del reglamento Verifactu deberá incluirse, de acuerdo con las especificaciones de una orden ministerial, la representación gráfica del contenido parcial de la factura mediante un código QR.</p>
<p>El mismo cambio se aplica a las facturas simplificadas (nuevo apartado 5 del artículo 7). Es decir, el QR no depende del tipo de factura: afecta a completas y simplificadas.</p>

<h2 id="tabla">QR y frase: qué va en cada caso</h2>
<div class="table-wrap"><table>
<thead><tr><th>Situación</th><th>Código QR</th><th>Frase «VERI*FACTU»</th></tr></thead>
<tbody>
<tr><td>Sistema que remite todos los registros a la AEAT</td><td>Sí</td><td>Sí</td></tr>
<tr><td>Sistema que conserva los registros sin remitirlos</td><td>Sí</td><td>No</td></tr>
<tr><td>Factura electrónica</td><td>Puede sustituirse por su contenido</td><td>Solo si hay remisión</td></tr>
<tr><td>Factura en papel o PDF</td><td>Sí, impreso o visible</td><td>Solo si hay remisión</td></tr>
</tbody></table></div>
<p>La frase admitida es «Factura verificable en la sede electrónica de la AEAT» o «VERI*FACTU», y únicamente cuando el sistema realiza la remisión de todos los registros conforme a los artículos 15 y 16.</p>

<h2 id="para-que">Para qué sirve el QR</h2>
<p>El artículo 17 permite al receptor de la factura, sea empresario o consumidor final, proporcionar de forma voluntaria determinada información a la AEAT con los datos del QR. La sede electrónica muestra esos datos en formato legible. Si la factura lleva la frase VERI*FACTU, el receptor puede comprobar así que el emisor la remitió. Esa remisión no tiene la consideración de denuncia pública.</p>

<h2 id="electronica">Qué ocurre con la factura electrónica</h2>
<p>El texto dice que, si la factura es electrónica, la representación gráfica puede sustituirse por el contenido que representa el QR. Cómo debe incorporarse ese contenido lo fijan las especificaciones técnicas de la AEAT; consúltalas antes de diseñar tu formato. Para la factura electrónica entre empresas mira también la <a href="/factura-electronica-obligatoria/">comprobación de fechas</a>.</p>

<h2 id="hacer">Qué hacer en la práctica</h2>
<ol class="steps">
<li>Comprueba que tu programa genera el QR de forma automática; no deberías montarlo a mano en cada factura.</li>
<li>Prueba una factura real con el <a href="/validar-qr-verifactu/">validador de QR</a> y revisa que los datos coinciden.</li>
<li>Si quieres ver cómo se compone, usa el <a href="/generador-qr-verifactu/">generador de QR</a>.</li>
<li>Revisa <a href="/blog/tamano-posicion-qr-verifactu/">tamaño y posición</a> y qué <a href="/blog/verifactu-modalidad-no-verifactu/">modalidad</a> usas para saber si añades la frase.</li>
</ol>

<h2 id="aviso">Qué no dice el BOE aquí</h2>
<p>El reglamento remite a una orden ministerial para las especificaciones del QR (la Orden HAC/1177/2024, arts. 20 y 21, y el documento técnico de la AEAT). En este artículo no damos medidas ni parámetros más allá de lo ya publicado en la guía de tamaño y posición. Las fechas de aplicación están en la <a href="/blog/fechas-verifactu-2027-2028/">guía de fechas</a>.</p>
""",
    faq=[
        ("¿El QR es obligatorio en facturas simplificadas?", "Sí. El apartado 5 que se añade al artículo 7 del Reglamento de facturación remite al contenido del artículo 6.5, QR incluido."),
        ("¿Y si no envío los registros a la AEAT?", "El QR sigue siendo obligatorio; lo que no se incluye es la frase «VERI*FACTU»."),
        ("¿Qué significa que el QR se puede sustituir en una factura electrónica?", "Que en lugar de la imagen puede incluirse el contenido que esta representa, según las especificaciones técnicas."),
        ("¿Quién puede escanear el QR?", "Cualquier receptor, empresario o consumidor final, para enviar voluntariamente los datos a la AEAT (art. 17)."),
        ("¿Enviar los datos del QR es una denuncia?", "No; el artículo 17.1 indica que no tiene la consideración de denuncia pública."),
        ("¿Dónde están las medidas del QR?", "En la Orden HAC/1177/2024 y en las especificaciones técnicas de la AEAT; revisa nuestra guía de tamaño y posición."),
    ],
    sources=[S.RD, S.ROF, S.ORDEN, S.QR],
))

POSTS.append(dict(
    slug="verifactu-factura-simplificada-ticket",
    published="2026-11-18",
    title="Verifactu y facturas simplificadas (tiques): qué cambia",
    desc="Qué exige el BOE a facturas simplificadas y tiques con sistemas Verifactu: registro de alta, QR, frase y qué hacer si sustituyes un tique por una factura.",
    h1="Verifactu y facturas simplificadas (tiques): qué cambia",
    intro="Comercios, bares o talleres emiten sobre todo facturas simplificadas. El reglamento Verifactu las incluye expresamente. Esto es lo que sí dice el texto del BOE. Revisado el 18 de noviembre de 2026.",
    content="""
<p class="note"><strong>Respuesta corta:</strong> el reglamento considera «factura» tanto la completa como la simplificada (art. 1.2). Por tanto, cada tique o factura simplificada expedida con un sistema informático de facturación genera su registro de alta, y debe llevar el código QR; la frase VERI*FACTU se añade solo si el sistema remite todos los registros.</p>

<h2 id="incluidas">Las simplificadas están dentro</h2>
<p>El artículo 1.2 aclara que el término factura incluye la factura completa y la simplificada. No hay un régimen aparte para los tiques: si el sistema que los emite entra en el ámbito del artículo 3 y no hay una exclusión del artículo 4, se aplican los mismos requisitos.</p>

<h2 id="registro">Un registro por cada documento</h2>
<p>El artículo 9 obliga a generar automáticamente un registro de facturación de alta de forma simultánea o inmediatamente anterior a la expedición de cada factura. Con un TPV, eso significa un registro por cada tique emitido. El contenido (art. 10) incluye, entre otros, el tipo de factura expedida, indicando si es completa o simplificada, el importe total, la base, el tipo de IVA y la cuota, la huella del registro anterior y la fecha, hora, minuto y segundo de generación.</p>

<h2 id="qr">QR y frase en el tique</h2>
<p>El apartado 5 que la disposición final primera añade al artículo 7 del Reglamento de facturación dice que a las facturas simplificadas se les aplica lo previsto en el artículo 6.5: QR y, en su caso, la frase. Detalles en la guía sobre si el <a href="/blog/verifactu-qr-obligatorio/">QR es obligatorio</a> y en el <a href="/generador-qr-verifactu/">generador de QR</a>.</p>

<h2 id="sustitucion">Si sustituyes tiques por una factura completa</h2>
<p>El artículo 10.1.h exige que el registro de alta de una factura emitida en sustitución de simplificadas anteriores identifique las simplificadas sustituidas. Es decir, el vínculo entre ambos documentos debe quedar en el registro y no solo en el papel.</p>

<h2 id="errores">Si te equivocas al emitir</h2>
<p>El artículo 8.2.a establece que las correcciones se hacen con registros adicionales posteriores y nunca borrando el original. Si una factura se emitió por error, el artículo 11 prevé un registro de facturación de anulación. Para las rectificaciones, el artículo 10.1.g pide indicar su tipo y las facturas rectificadas cuando sea preceptivo.</p>

<h2 id="tabla">Resumen por documento</h2>
<div class="table-wrap"><table>
<thead><tr><th>Documento</th><th>Registro de alta</th><th>QR</th><th>Frase</th></tr></thead>
<tbody>
<tr><td>Tique o factura simplificada</td><td>Sí (art. 9)</td><td>Sí</td><td>Si hay remisión</td></tr>
<tr><td>Factura completa</td><td>Sí (art. 9)</td><td>Sí</td><td>Si hay remisión</td></tr>
<tr><td>Anulación de una factura emitida por error</td><td>Registro de anulación (art. 11)</td><td>—</td><td>—</td></tr>
</tbody></table></div>

<h2 id="pasos">Pasos para un comercio</h2>
<ol class="steps">
<li>Pregunta a tu proveedor de TPV si su software está adaptado y si ofrece la declaración responsable (art. 13).</li>
<li>Comprueba que el tique impreso o digital incluye el QR.</li>
<li>Prueba el QR con el <a href="/validar-qr-verifactu/">validador</a>.</li>
<li>Revisa si tu caso queda fuera del reglamento con el <a href="/">test de obligación</a> y las <a href="/blog/fechas-verifactu-2027-2028/">fechas</a>.</li>
</ol>
<p>Más sobre cómo se encadenan los registros en <a href="/blog/verifactu-programa-facturacion-requisitos/">requisitos del programa</a>.</p>
""",
    faq=[
        ("¿Un tique cuenta como factura a efectos de Verifactu?", "Sí: el artículo 1.2 incluye la factura simplificada en el término factura."),
        ("¿Hay que generar un registro por cada tique?", "Sí, un registro de alta por cada factura, simultáneo o inmediatamente anterior a su expedición (art. 9)."),
        ("¿El tique lleva QR?", "Sí; el artículo 7.5 del Reglamento de facturación remite al contenido del artículo 6.5."),
        ("¿Cuándo va la frase VERI*FACTU?", "Solo cuando el sistema remite todos los registros a la AEAT."),
        ("¿Cómo corrijo un tique emitido por error?", "Con un registro adicional: anulación (art. 11) o rectificación, sin borrar el original (art. 8.2.a)."),
        ("¿Qué pasa si sustituyo tiques por una factura completa?", "El registro de alta debe identificar las simplificadas sustituidas (art. 10.1.h)."),
    ],
    sources=[S.RD, S.ROF],
))

POSTS.append(dict(
    slug="huella-verifactu-que-es",
    published="2026-11-18",
    title="Qué es la huella (hash) de Verifactu y cómo se calcula",
    desc="Qué es la huella o hash de los registros de Verifactu, qué dice el BOE, cómo encadena los registros y dónde está la especificación oficial de la AEAT.",
    h1="Qué es la huella (hash) de Verifactu y cómo se calcula",
    intro="La huella es el elemento que encadena unos registros con otros e impide alterarlos sin que se note. Explicamos qué exige el BOE y dónde está el cálculo oficial. Revisado el 18 de noviembre de 2026.",
    content="""
<p class="note"><strong>Respuesta corta:</strong> la huella o «hash» es una cadena que el sistema añade a cada registro de facturación de alta y de anulación (art. 12). El registro siguiente incluye parte de la huella del anterior (art. 10.1.ñ), de modo que cualquier cambio posterior rompe la cadena. El cálculo exacto no lo fija el Real Decreto sino la especificación técnica de la AEAT.</p>

<h2 id="que">Qué es</h2>
<p>Una huella (hash) es el resultado de aplicar una función matemática a unos datos: si cambia un solo carácter, cambia la huella. El reglamento obliga a que los sistemas informáticos añadan una huella a los registros de alta y de anulación «según las especificaciones que se determinen» (art. 12).</p>

<h2 id="cadena">Cómo encadena los registros</h2>
<p>Los registros deben estar encadenados para poder verificar su rastro desde el primero hasta el último (art. 8.2.b). Para ello, cuando no es el primer registro, incluye el número, la serie, la fecha de expedición del registro inmediatamente anterior y parte de su huella (arts. 10.1.ñ y 11.2.e). Si alguien oculta o modifica un registro antiguo, la huella almacenada en el siguiente deja de coincidir.</p>

<h2 id="alteracion">Qué cuenta como alteración</h2>
<p>El artículo 8.2.a define alteración: ocultar o eliminar un registro, ocultar o modificar sus datos total o parcialmente, o añadir registros simulados. El sistema debe detectarlo y avisar. Cualquier corrección se hace con un registro adicional posterior.</p>

<h2 id="firma">Huella y firma electrónica</h2>
<div class="table-wrap"><table>
<thead><tr><th>Modalidad</th><th>Huella</th><th>Firma electrónica</th></tr></thead>
<tbody>
<tr><td>Sistema que no remite los registros</td><td>Obligatoria</td><td>Obligatoria (art. 12)</td></tr>
<tr><td>Sistema VERI*FACTU</td><td>Obligatoria</td><td>No; basta calcular la huella (art. 16.3)</td></tr>
</tbody></table></div>
<p>Más sobre las dos modalidades en <a href="/blog/verifactu-modalidad-no-verifactu/">VERI*FACTU o no VERI*FACTU</a>.</p>

<h2 id="calculo">Dónde está el cálculo oficial</h2>
<p>La disposición final tercera permite que una orden ministerial detalle las especificaciones de la huella y de la firma. La AEAT publica el documento técnico «especificaciones de la huella o hash de los registros» (v0.1.2) y preguntas frecuentes sobre el tema. Allí se indican los campos que intervienen y el orden en que se concatenan; no los reproducimos aquí para no inducir a error si el documento cambia.</p>
<p>Para comprobar un cálculo con datos de ejemplo, usa la <a href="/calcular-huella-verifactu/">calculadora de huella</a> de esta web, que sigue la especificación de la AEAT y funciona en tu navegador. Contrasta siempre el resultado con tu programa de facturación.</p>

<h2 id="pasos">Cómo revisarla en tu programa</h2>
<ol class="steps">
<li>Pide a tu proveedor la declaración responsable de cumplimiento (art. 13).</li>
<li>Emite dos facturas de prueba y comprueba que la segunda referencia a la primera.</li>
<li>Prueba el XML con el <a href="/ejemplo-xml-verifactu/">ejemplo de XML</a> y los datos del QR con el <a href="/validar-qr-verifactu/">validador</a>.</li>
<li>Revisa los <a href="/blog/verifactu-programa-facturacion-requisitos/">requisitos del programa</a>.</li>
</ol>
""",
    faq=[
        ("¿Qué es la huella de Verifactu?", "Una cadena calculada sobre los datos de cada registro de alta o anulación que permite detectar modificaciones (art. 12)."),
        ("¿Quién calcula la huella?", "El sistema informático de facturación, de forma automática al generar cada registro."),
        ("¿Es lo mismo que la firma electrónica?", "No. Los sistemas VERI*FACTU solo necesitan calcular la huella; los demás, además, firman (arts. 12 y 16.3)."),
        ("¿Qué pasa si altero un registro antiguo?", "El sistema debe detectarlo y avisar; el encadenamiento deja de ser coherente (art. 8.2.a)."),
        ("¿Dónde está la fórmula exacta?", "En la especificación técnica de la AEAT sobre la huella o hash de los registros."),
        ("¿Puedo comprobar una huella gratis?", "Sí, con la calculadora de huella de esta web; contrasta el resultado con tu programa."),
    ],
    sources=[S.RD, S.HASH, S.HASH_FAQ],
))

# ---------------------------------------------------------------- 2026-11-19 (#4, #11, #12)
POSTS.append(dict(
    slug="verifactu-excel-word",
    published="2026-11-19",
    title="Verifactu y Excel o Word: cuándo te afecta, según la AEAT",
    desc="¿Puedo facturar con Excel o Word con Verifactu? Criterio de la AEAT: cuándo no te afecta y cuándo la hoja de cálculo pasa a ser un sistema de facturación.",
    h1="¿Puedo facturar con Excel o Word con Verifactu?",
    intro="Muchos autónomos y pymes emiten sus facturas con una plantilla de Excel o de Word. La AEAT ha publicado un criterio sobre ese caso en sus preguntas frecuentes (actualizadas a 21 de octubre de 2026). Revisado el 19 de noviembre de 2026.",
    content="""
<p class="note"><strong>Respuesta corta:</strong> según la AEAT, el reglamento <strong>no te afecta</strong> si usas el procesador de textos o la hoja de cálculo solo para introducir los datos de las facturas, expedirlas e imprimirlas y conservar la información. <strong>Sí te afecta</strong> si, además, la utilizas para procesar esa información y generar directamente los libros registro de IVA o de IRPF, la contabilidad u otro resultado que sirva para cumplir voluntariamente obligaciones tributarias.</p>

<h2 id="definicion">Qué es un sistema informático de facturación</h2>
<p>El artículo 1.2 del reglamento llama sistema informático de facturación al conjunto de hardware y software que se usa para expedir facturas y que hace alguna de estas tres cosas: admitir la entrada de información de facturación por cualquier método, conservarla, o procesarla para producir otros resultados derivados. Por eso la pregunta no es «¿uso Excel?», sino <strong>«¿qué hace mi hoja?»</strong>.</p>

<h2 id="tabla">Casos según el criterio de la AEAT</h2>
<div class="table-wrap"><table>
<thead><tr><th>Uso de la hoja o del documento</th><th>¿Te afecta el reglamento?</th></tr></thead>
<tbody>
<tr><td>Escribir los datos de la factura, imprimirla o exportarla a PDF y guardarla</td><td>No</td></tr>
<tr><td>Listado simple de facturas emitidas con sumatorios u otras reglas de cálculo</td><td>No (ejemplo de la propia AEAT)</td></tr>
<tr><td>Macro que genera el libro registro de facturas expedidas</td><td>Sí: pasa a ser un sistema de facturación</td></tr>
<tr><td>Cálculo que alimenta los libros de IVA o de IRPF, la contabilidad u otro resultado fiscal voluntario</td><td>Sí</td></tr>
<tr><td>Talonario o factura escrita a mano o a máquina, sin ningún sistema informático</td><td>No</td></tr>
</tbody></table></div>
<p>La AEAT añade que podrá comprobar si los procesadores de texto o las hojas de cálculo que se usan para emitir facturas cumplen los criterios de un sistema informático de facturación, en función de las capacidades y herramientas que utilicen. La línea entre un listado con sumas y una macro que genera libros no depende del nombre del programa sino de lo que hace.</p>

<h2 id="todo-o-nada">Todo informático o todo manual</h2>
<p>Las mismas preguntas frecuentes explican que, con carácter general, no es posible que convivan facturas emitidas con un sistema informático y otras a mano: si utilizas un sistema de facturación para producir facturas, toda la facturación debe ser informática y cumplir el reglamento. La única excepción que cita la AEAT es la de quien emite facturas electrónicas a una Administración con el programa gratuito MiFacturae y no usa ningún otro sistema; no vale para facturas generadas por un programa en formato Facturae e integradas con FACe.</p>

<h2 id="si-te-afecta">Si tu hoja cuenta como sistema de facturación</h2>
<p>Entonces debe cumplir el artículo 8: integridad, conservación, accesibilidad, legibilidad, trazabilidad e inalterabilidad de los registros. Los registros no pueden alterarse sin que el sistema lo detecte, y cualquier corrección debe hacerse con un registro adicional (art. 8.2.a). Debe además generar un registro de alta por cada factura (art. 9), con huella y, según la modalidad, firma electrónica (art. 12). Una hoja de cálculo corriente, en la que cualquiera puede cambiar una celda sin dejar rastro, difícilmente cumple eso por sí sola; es una valoración nuestra, no un criterio de la AEAT.</p>
<p>Las salidas habituales son dos: pasar a un <a href="/blog/verifactu-programa-facturacion-requisitos/">programa de facturación adaptado</a> (el productor debe ofrecer su declaración responsable, art. 13) o usar la <a href="/blog/verifactu-gratis-aplicacion-aeat/">aplicación gratuita de la AEAT</a>, que la propia Agencia presenta como alternativa para pequeños empresarios y profesionales siempre que sus funciones se ajusten a lo que necesitan.</p>

<h2 id="errores">Tres errores frecuentes</h2>
<ul class="checklist">
<li><strong>Pensar que «Excel» o «Word» es un permiso o una prohibición.</strong> El criterio es funcional: lo que cuenta es lo que hace el archivo, no su nombre.</li>
<li><strong>Mezclar plantilla y programa.</strong> Si ya usas un programa de facturación para algunos clientes, la plantilla de Word para otros deja de ser una opción segura, porque la facturación no puede ser mitad manual y mitad informática.</li>
<li><strong>Olvidar al gestor.</strong> Si tu asesor emite facturas por ti con su programa, el sistema relevante es el suyo, pero la responsabilidad de cumplir sigue siendo tuya.</li>
</ul>

<h2 id="gestor">¿Y si mi gestor hace las facturas?</h2>
<p>Depende de quién las expide materialmente. Si tú las haces a mano o con Word o Excel que no son un sistema de facturación y se las entregas al gestor para llevar los libros, el reglamento no te afecta por eso. Si es el gestor quien las expide con un sistema de facturación, él debe generar el registro de alta y, en la modalidad VERI*FACTU, remitirlo; y, según la AEAT, la delegación no te libera de la responsabilidad de cumplir.</p>

<h2 id="pasos">Qué hacer</h2>
<ol class="steps">
<li>Anota qué hace exactamente tu plantilla: ¿solo escribe e imprime, o también genera libros, contabilidad o declaraciones?</li>
<li>Si genera algo más que un listado, trátala como sistema de facturación y planifica el cambio de programa con las <a href="/blog/fechas-verifactu-2027-2028/">fechas vigentes</a>.</li>
<li>Haz el <a href="/">test de obligación</a> para ver si estás dentro del ámbito (SII, territorio foral y otras exclusiones).</li>
<li>Si cambias de programa, prueba su QR con el <a href="/validar-qr-verifactu/">validador</a>.</li>
</ol>
""",
    faq=[
        ("¿Puedo seguir usando Excel para mis facturas?", "Según la AEAT, sí si solo lo usas para introducir datos, expedir e imprimir facturas y conservar la información."),
        ("¿Qué convierte una hoja de cálculo en sistema de facturación?", "Procesar la información para generar directamente los libros registro, la contabilidad u otro resultado fiscal; por ejemplo, con una macro."),
        ("¿Un listado de facturas con sumas me afecta?", "No: la AEAT cita expresamente los simples listados de facturas con sumatorios o reglas de cálculo."),
        ("¿Puedo emitir unas facturas a mano y otras con programa?", "Con carácter general no; si usas un sistema de facturación, toda la facturación debe ser informática. Hay una excepción para MiFacturae."),
        ("¿Puede la AEAT comprobar mi hoja de cálculo?", "Sí: la AEAT indica que puede verificar si encaja en la definición según las capacidades y herramientas que use."),
        ("¿Hay alternativa gratuita?", "La AEAT ofrece una aplicación básica de facturación, utilizable si sus funciones y condiciones se ajustan a tus necesidades."),
    ],
    sources=[S.RD, S.FAQ_AMB, S.APP_GUIA],
))

POSTS.append(dict(
    slug="verifactu-recargo-equivalencia",
    published="2026-11-19",
    title="Verifactu y recargo de equivalencia: ¿te afecta?",
    desc="Comercios en recargo de equivalencia: cuándo te afecta Verifactu según la AEAT, en qué casos debes expedir factura y qué pasa con tiques y cajas registradoras.",
    h1="Verifactu y recargo de equivalencia: comercios minoristas",
    intro="Si eres comerciante minorista en el régimen especial del recargo de equivalencia, la duda es si tienes que adaptar tu caja o tu programa. La respuesta depende de si expides facturas. Revisado el 19 de noviembre de 2026.",
    content="""
<p class="note"><strong>Respuesta corta:</strong> según la AEAT, quien solo realiza operaciones en recargo de equivalencia <strong>no está afectado con carácter general</strong>, porque no está obligado a expedir factura salvo excepciones. Pero si expides facturas (o facturas simplificadas) con un sistema informático, el reglamento sí se aplica, sea cual sea el motivo por el que las emites.</p>

<h2 id="clave">La clave: ¿expides facturas?</h2>
<p>El reglamento regula los sistemas informáticos que sirven para expedir facturas, completas o simplificadas (art. 1.2). No regula otros documentos justificativos de una venta. La AEAT lo resume así: lo que importa es si, según la normativa de facturación, estás obligado a facturar o si facturas voluntariamente con un sistema informático.</p>

<h2 id="casos">Cuándo tienes que expedir factura en recargo de equivalencia</h2>
<p>Según las preguntas frecuentes de la AEAT, estos son los supuestos que obligan a facturar a un contribuyente en recargo de equivalencia:</p>
<div class="table-wrap"><table>
<thead><tr><th>Supuesto</th><th>Consecuencia</th></tr></thead>
<tbody>
<tr><td>Entregas de inmuebles sujetas y no exentas de IVA</td><td>Factura obligatoria</td></tr>
<tr><td>Tributas en IRPF en estimación directa</td><td>Factura obligatoria</td></tr>
<tr><td>El cliente es empresario, profesional o una Administración Pública</td><td>Factura obligatoria</td></tr>
<tr><td>El destinatario la exige para ejercer un derecho de naturaleza tributaria</td><td>Factura obligatoria</td></tr>
<tr><td>Determinadas operaciones de comercio exterior</td><td>Factura obligatoria</td></tr>
</tbody></table></div>
<p>En cualquiera de esos casos, si usas un sistema informático para expedir la factura, ese sistema debe cumplir el reglamento. Para esas operaciones excepcionales, la AEAT indica que se puede utilizar el sistema facilitado por la propia Agencia en su sede electrónica (art. 7.b del reglamento).</p>

<h2 id="farmacias">El ejemplo de las farmacias</h2>
<p>La AEAT pone como ejemplo a las oficinas de farmacia en recargo de equivalencia: les afecta el reglamento porque, a efectos del IRPF, determinan su rendimiento por estimación directa, y el artículo 26 del Reglamento de facturación obliga a expedir factura a quien obtiene rendimientos de actividades económicas por ese método con independencia del régimen de IVA. Lo mismo vale para cualquier otro contribuyente en estimación directa.</p>

<h2 id="cajas">Cajas registradoras y tiques</h2>
<p>Un comercio en recargo suele emitir justificantes de venta con la caja. Según la AEAT, si esos documentos no son facturas completas ni simplificadas y se emiten en operaciones excluidas de la obligación de facturar, <strong>no están sometidos al reglamento</strong>, aunque se emitan voluntariamente. Pero si la caja imprime lo que es una factura simplificada, esa caja es un sistema de facturación y debe adaptarse. Más detalle en <a href="/blog/verifactu-factura-simplificada-ticket/">Verifactu y facturas simplificadas</a>.</p>
<p>Y si al cierre del día sacas una «factura recapitulativa» con todas las ventas, la AEAT aclara que eso no sustituye a las facturas simplificadas ya emitidas: estas siguen sometidas al reglamento.</p>

<h2 id="otros">Régimen simplificado y agricultura, ganadería y pesca</h2>
<p>La AEAT da la misma respuesta general para quien solo opera en el régimen simplificado de IVA o en el régimen especial de agricultura, ganadería y pesca: no hay obligación de facturar salvo excepciones (por ejemplo, vender activos fijos en el simplificado, facturar a empresarios o a Administraciones, o entregar inmuebles en el régimen agrario), y quien utiliza un sistema informático para expedir facturas, incluidas las voluntarias, queda dentro del reglamento. Es siempre la misma pregunta: ¿expido facturas con un sistema informático?</p>

<h2 id="registro">Cómo aparece el recargo en el registro</h2>
<p>Cuando sí corresponde generar el registro de facturación de alta, el artículo 10.1.m exige incluir el tipo y la cuota del recargo de equivalencia aplicados e informar si la operación la ha realizado un contribuyente en régimen simplificado o en recargo de equivalencia. Esa parte la resuelve el programa; tú solo necesitas que esté adaptado.</p>

<h2 id="pasos">Qué hacer</h2>
<ol class="steps">
<li>Revisa si en tu actividad se dan los cinco supuestos de la tabla, sobre todo si vendes a empresas o tributas por estimación directa.</li>
<li>Si no facturas nunca con sistema informático, no tienes que adaptar nada, pero revisa el punto anterior cada vez que cambie tu forma de vender.</li>
<li>Si facturas, pregunta a tu proveedor de caja o programa por su declaración responsable (art. 13) y por las <a href="/blog/fechas-verifactu-2027-2028/">fechas</a>.</li>
<li>Haz el <a href="/">test de obligación</a> para comprobar las exclusiones (SII, territorio foral).</li>
</ol>
""",
    faq=[
        ("¿Estoy obligado a Verifactu si solo vendo en recargo de equivalencia?", "Con carácter general no, según la AEAT, porque no hay obligación de facturar salvo excepciones; pero sí si facturas con un sistema informático."),
        ("¿Y si un cliente empresario me pide factura?", "Debes expedirla, y si usas un sistema informático para ello, el reglamento se aplica."),
        ("¿Las farmacias en recargo están afectadas?", "Sí, según la AEAT, porque tributan en IRPF por estimación directa y deben facturar."),
        ("¿Un tique de caja que no es factura simplificada está sujeto?", "No, si se emite en operaciones excluidas de la obligación de facturar (criterio de la AEAT)."),
        ("¿Una factura recapitulativa diaria me exime?", "No: las facturas simplificadas ya emitidas siguen sometidas al reglamento."),
        ("¿Qué sistema puedo usar si solo facturo de forma excepcional?", "La AEAT señala que puede utilizarse el sistema facilitado por la propia Agencia en su sede electrónica."),
    ],
    sources=[S.RD, S.ROF, S.FAQ_AMB],
))

POSTS.append(dict(
    slug="verifactu-ticketbai-diferencias",
    published="2026-11-19",
    title="Verifactu y TicketBAI: diferencias y quién aplica cada uno",
    desc="Verifactu o TicketBAI: manda el domicilio fiscal. Qué dice el art. 1.3 del RD 1007/2023, qué aclara la AEAT sobre territorios forales y si operas con ambos.",
    h1="Verifactu y TicketBAI: diferencias y quién usa cada uno",
    intro="Verifactu y TicketBAI se parecen, pero no son lo mismo ni se aplican a las mismas empresas. Te explicamos el criterio que fija el BOE y lo que aclara la AEAT. Revisado el 19 de noviembre de 2026.",
    content="""
<p class="note"><strong>Respuesta corta:</strong> el reglamento de Verifactu (RD 1007/2023) se aplica en territorio común, y en el País Vasco y Navarra solo a los obligados con domicilio fiscal en territorio común (art. 1.3). Quien tributa a las Haciendas Forales vascas se rige por su normativa foral, que en Gipuzkoa, Bizkaia y Álava es el sistema TicketBAI. La AEAT lo describe como un sistema «de contenido similar» a la modalidad VERI*FACTU.</p>

<h2 id="criterio">El criterio: dónde tienes el domicilio fiscal</h2>
<p>El artículo 1.3 dice que el reglamento es aplicable en todo el territorio español, sin perjuicio de los regímenes forales de concierto y convenio económico, y que en relación con el País Vasco y Navarra se aplica a los obligados del artículo 3 «cuando tengan su domicilio fiscal en territorio común». La AEAT explica que la clave es si la competencia sobre la imposición directa (IRPF e Impuesto sobre Sociedades) corresponde a las Haciendas Forales según el Concierto Económico (arts. 6 y 14) o el Convenio con Navarra (arts. 9 y 18).</p>

<h2 id="tabla">Comparativa rápida</h2>
<div class="table-wrap"><table>
<thead><tr><th>Aspecto</th><th>Verifactu (RD 1007/2023)</th><th>Territorios forales</th></tr></thead>
<tbody>
<tr><td>A quién se aplica</td><td>Obligados del art. 3 con domicilio fiscal en territorio común (incluidos Canarias, Ceuta y Melilla)</td><td>Quien tributa a la Hacienda Foral por la imposición directa</td></tr>
<tr><td>Norma</td><td>Real Decreto 1007/2023 y su orden de desarrollo</td><td>Normativa de la Hacienda Foral correspondiente</td></tr>
<tr><td>Sistema</td><td>Modalidad VERI*FACTU o no VERI*FACTU</td><td>TicketBAI en Gipuzkoa, Bizkaia y Álava, en distintas modalidades</td></tr>
<tr><td>Navarra</td><td>No, con carácter general, si se sujetan a normativa foral</td><td>Su propia normativa foral</td></tr>
</tbody></table></div>
<p>Los detalles técnicos de TicketBAI no están en el Real Decreto 1007/2023 y no los reproducimos aquí: consulta a tu Hacienda Foral.</p>

<h2 id="que-es">Qué tienen en común y qué no</h2>
<p>Los dos sistemas buscan que el programa de facturación genere registros de cada factura que no puedan alterarse sin dejar rastro y que la Administración pueda consultar. Pero se rigen por normas distintas, aprobadas por administraciones distintas. No des por hecho que un programa adaptado a uno sirve para el otro. Si desarrollas o compras software para ambos territorios, comprueba la compatibilidad por separado.</p>

<h2 id="canarias">Canarias, Ceuta y Melilla no son forales</h2>
<p>Los contribuyentes con domicilio fiscal en Canarias, Ceuta o Melilla sí están dentro del ámbito del reglamento: las referencias al IVA se entienden hechas también al IGIC y al IPSI (art. 1.3, confirmado por la AEAT).</p>

<h2 id="relaciones">Qué pasa si operas con empresas de los dos territorios</h2>
<p>La AEAT da un ejemplo: si una empresa con domicilio foral y otra con domicilio en territorio común se relacionan comercialmente, el sistema de facturación de la primera queda sometido a las obligaciones de su Hacienda Foral y el de la segunda al reglamento estatal. Cada una cumple el suyo.</p>
<p>Hay una excepción práctica en la autofacturación. Si una empresa foral emite materialmente las facturas como destinataria en nombre de proveedores de territorio común: si está adscrita al SII foral, no tiene que cumplir el reglamento estatal por esas operaciones (art. 4.3); si no está adscrita al SII foral, sí debe hacerlo, enviando los registros a VERI*FACTU o conservándolos a disposición de la AEAT.</p>

<h2 id="sii">Y el SII</h2>
<p>El SII es otra exclusión distinta: quienes llevan los libros registro de IVA en la sede electrónica de la AEAT quedan fuera del reglamento respecto de sus propias facturas (art. 3.3). Lo explicamos en <a href="/blog/verifactu-sii-exentos/">Verifactu y SII</a>.</p>

<h2 id="pasos">Qué hacer</h2>
<ol class="steps">
<li>Mira dónde está tu domicilio fiscal y a qué Hacienda tributas por IRPF o Sociedades.</li>
<li>Si es territorio común, sigue las <a href="/blog/fechas-verifactu-2027-2028/">fechas de Verifactu</a> y haz el <a href="/">test de obligación</a>.</li>
<li>Si es foral, consulta el calendario y las modalidades de tu Hacienda Foral; este sitio no cubre TicketBAI.</li>
<li>Si tu proveedor de software trabaja en ambos territorios, pregúntale por qué normativa cumple cada producto.</li>
</ol>
<p>Si tu negocio es un bar o restaurante, mira <a href="/blog/verifactu-bares-restaurantes/">Verifactu en hostelería</a> y <a href="/blog/tpv-verifactu/">qué debe cumplir un TPV</a>; para corregir facturas, <a href="/blog/factura-rectificativa-verifactu/">rectificativas</a>.</p>
<p>La factura electrónica entre empresas tiene también reglas específicas en estos territorios: <a href="/blog/factura-electronica-pais-vasco-navarra/">País Vasco y Navarra</a>.</p>
""",
    faq=[
        ("¿Verifactu y TicketBAI son lo mismo?", "No. Son sistemas distintos con normativa distinta; la AEAT dice que TicketBAI tiene un contenido similar a la modalidad VERI*FACTU."),
        ("¿Qué manda: mi domicilio o el de mi cliente?", "Tu domicilio fiscal: cada empresa cumple con la normativa de su territorio."),
        ("¿Se aplica Verifactu en Navarra?", "Con carácter general no, cuando el empresario se sujeta a la normativa foral según el Convenio Económico, según la AEAT."),
        ("¿Y en Canarias, Ceuta y Melilla?", "Sí, el reglamento se aplica, entendiendo las referencias al IVA hechas también al IGIC y al IPSI."),
        ("¿Dónde se explica TicketBAI?", "En la normativa de cada Hacienda Foral; no está en el RD 1007/2023."),
        ("¿Puedo estar excluido por SII y por territorio foral a la vez?", "Son exclusiones independientes; se analiza cada una según tu situación."),
    ],
    sources=[S.RD, S.FAQ_AMB],
))


POSTS.append(dict(
    slug="factura-rectificativa-verifactu",
    published="2026-11-20",
    title="Factura rectificativa con Verifactu: tipos R1 a R5",
    desc="Qué son los tipos R1 a R5 y las claves S e I del esquema XML de la AEAT, cuándo se anula un registro y cómo se corrige una factura sin borrarla en Verifactu.",
    h1="Factura rectificativa con Verifactu: tipos R1 a R5",
    intro="Con Verifactu una factura emitida no se borra ni se edita: se corrige con un registro nuevo. Te explicamos los tipos de rectificativa que define el esquema de la AEAT y la diferencia con anular. Revisado el 20 de noviembre de 2026.",
    content="""
<p class="note"><strong>Respuesta corta:</strong> el art. 8.2.a del RD 1007/2023 dice que cualquier corrección o anulación debe hacerse «mediante al menos un registro de facturación adicional posterior», conservando inalterados los datos originales. En el esquema XML de la AEAT, una factura rectificativa se marca con un tipo R1 a R5 y con una clave S (sustitutiva) o I (incremental).</p>

<h2 id="principio">El principio: no se altera, se añade</h2>
<p>El reglamento define alteración como ocultar o eliminar un registro ya generado, o modificar sus datos. Por eso, si te equivocas en una factura, el programa no puede cambiar el registro original. Tiene que generar otro registro que corrija el error, y los dos quedan encadenados en la secuencia (art. 8.2.b).</p>

<h2 id="tipos">Los tipos de factura rectificativa</h2>
<p>El artículo 10.1.g exige indicar, si la factura es rectificativa, «su tipo, características» y las facturas rectificadas cuando sea preceptivo. El detalle lo fija el esquema XSD publicado por la AEAT, que distingue cinco tipos:</p>
<div class="table-wrap"><table>
<thead><tr><th>Tipo</th><th>Descripción en el esquema</th></tr></thead>
<tbody>
<tr><td>R1</td><td>Factura rectificativa (art. 80.1 y 80.2 y error fundado en derecho)</td></tr>
<tr><td>R2</td><td>Factura rectificativa (art. 80.3)</td></tr>
<tr><td>R3</td><td>Factura rectificativa (art. 80.4)</td></tr>
<tr><td>R4</td><td>Factura rectificativa (resto)</td></tr>
<tr><td>R5</td><td>Factura rectificativa en facturas simplificadas</td></tr>
</tbody></table></div>
<p>Las referencias a «art. 80» son a la Ley del IVA. Qué tipo corresponde a tu caso depende del motivo de la rectificación; si dudas, consúltalo con tu gestor.</p>

<h2 id="clave">Sustitutiva (S) o incremental (I)</h2>
<p>Además del tipo, el esquema incluye un campo de tipo de rectificación con dos valores: <strong>S</strong>, sustitutiva, e <strong>I</strong>, incremental. El esquema permite indicar las facturas rectificadas (hasta 1.000) y, en las sustitutivas, el desglose de la base y la cuota rectificadas. Te lo mostramos en un <a href="/ejemplo-xml-verifactu/">ejemplo de XML</a>.</p>

<h2 id="anular">Rectificar no es anular</h2>
<p>El art. 11 regula otro registro distinto: el de anulación. Procede «cuando se haya emitido erróneamente una factura» y hace falta anular su registro de alta. Incluye el número, la serie y la fecha de la factura anulada. Es decir: la rectificativa corrige una factura que existe; la anulación deja sin efecto un registro generado por error.</p>

<h2 id="simplificadas">Facturas simplificadas</h2>
<p>Para tickets el esquema tiene el tipo R5, y también el F3, «factura emitida en sustitución de facturas simplificadas facturadas y declaradas». El art. 10.1.h exige identificar las simplificadas sustituidas. Más en <a href="/blog/verifactu-factura-simplificada-ticket/">Verifactu y facturas simplificadas</a>.</p>

<h2 id="pasos">Qué hacer cuando te equivocas</h2>
<ol class="steps">
<li>No intentes editar ni borrar la factura original en tu programa: debería impedirlo.</li>
<li>Decide si la factura es errónea de forma que haya que anularla o si basta una rectificativa.</li>
<li>Emite la rectificativa desde el programa, que elegirá el tipo y la relacionará con la original.</li>
<li>Comprueba que el registro nuevo queda encadenado: <a href="/calcular-huella-verifactu/">la huella</a> incluye la del registro anterior.</li>
<li>Si el programa te pide elegir el tipo R1 a R5, pregunta a tu asesor cuál corresponde.</li>
</ol>
<p>La huella y el registro de eventos permiten que cualquier hueco o cambio se detecte. Si el programa no lo garantiza, no cumple el art. 8: revisa los <a href="/blog/verifactu-programa-facturacion-requisitos/">requisitos del programa</a>.</p>
""",
    faq=[
        ("¿Puedo borrar una factura emitida con Verifactu?", "No. Cualquier corrección o anulación exige al menos un registro adicional posterior (art. 8.2.a del RD 1007/2023)."),
        ("¿Qué significan R1, R2, R3, R4 y R5?", "Son los tipos de factura rectificativa del esquema de la AEAT: R1 (art. 80.1, 80.2 y error fundado en derecho), R2 (80.3), R3 (80.4), R4 (resto) y R5 (facturas simplificadas)."),
        ("¿Qué diferencia hay entre S e I?", "Son los dos valores del campo de tipo de rectificación: S es sustitutiva e I es incremental."),
        ("¿Es lo mismo anular que rectificar?", "No. La anulación (art. 11) deja sin efecto el registro de una factura emitida por error; la rectificativa corrige una factura."),
        ("¿Cuántas facturas puede rectificar una sola rectificativa?", "El esquema XSD admite hasta 1.000 identificadores de facturas rectificadas."),
        ("¿Quién elige el tipo R1 a R5?", "El programa lo pide o lo propone, pero la responsabilidad es tuya: consulta a tu asesor si dudas."),
    ],
    sources=[S.RD, S.XSD],
))

POSTS.append(dict(
    slug="tpv-verifactu",
    published="2026-11-20",
    title="TPV Verifactu: qué debe cumplir tu caja registradora",
    desc="Requisitos del RD 1007/2023 para un TPV o caja: registros de alta, huella, registro de eventos, declaración responsable y exportación. Qué pedir al fabricante.",
    h1="TPV Verifactu: qué debe cumplir tu caja registradora",
    intro="Si tu negocio cobra con TPV o caja, el programa que emite el ticket es un sistema informático de facturación. Repasamos lo que exige el reglamento y qué preguntar al proveedor. Revisado el 20 de noviembre de 2026.",
    content="""
<p class="note"><strong>Respuesta corta:</strong> un TPV entra en el reglamento si genera facturas, incluidas las simplificadas (art. 1.2, que define factura como completa o simplificada). Debe generar un registro de alta por cada una, encadenarlo, añadir la huella, llevar un registro de eventos y contar con la declaración responsable del fabricante.</p>

<h2 id="entra">¿Mi TPV es un sistema informático de facturación?</h2>
<p>El art. 1.2 define el sistema informático de facturación como el hardware y software que admite información de facturación, la conserva y la procesa para expedir facturas. Una caja que imprime tickets con la venta encaja. El reglamento se aplica aunque solo lo uses para una parte de tu actividad (art. 3.1).</p>

<h2 id="requisitos">Lo que debe hacer el programa</h2>
<ul class="checklist">
<li><strong>Registro de alta por cada factura</strong>, generado de forma simultánea o inmediatamente anterior a su expedición (art. 9), con los datos del art. 10: emisor, número y serie, fecha, tipo, importe, impuestos, fecha y hora del registro y código del sistema.</li>
<li><strong>Encadenamiento</strong>: cada registro lleva parte de la huella del anterior (art. 10.1.ñ), de modo que se pueda seguir la secuencia (art. 8.2.b).</li>
<li><strong>Huella o hash</strong> y, salvo en VERI*FACTU, <strong>firma electrónica</strong> (arts. 12 y 16.3). Lo explicamos en <a href="/blog/huella-verifactu-que-es/">qué es la huella</a>.</li>
<li><strong>Inalterabilidad</strong>: no se puede borrar ni modificar un registro sin que el sistema lo detecte (art. 8.2.a). Una corrección es otro registro: <a href="/blog/factura-rectificativa-verifactu/">facturas rectificativas</a>.</li>
<li><strong>Registro de eventos</strong> automático, consultable desde el propio programa (art. 8.3).</li>
<li><strong>Conservación y exportación</strong> de los registros a un almacenamiento externo en formato legible (art. 8.2.c).</li>
<li><strong>Acceso de la Administración</strong>: separar la información fiscal de la confidencial (art. 8.4) y permitir el acceso y la descarga (art. 14).</li>
</ul>

<h2 id="qr">El QR en el ticket</h2>
<p>Las facturas emitidas con estos sistemas deben incluir un código QR (art. 6.5 del Reglamento de facturación, introducido por la disposición final primera). La frase «Factura verificable en la sede electrónica de la AEAT» o «VERI*FACTU» solo se añade cuando el sistema envía todos los registros a la AEAT. Puedes comprobar el tuyo con el <a href="/validar-qr-verifactu/">validador de QR</a> y leer más en <a href="/blog/verifactu-qr-obligatorio/">QR obligatorio</a>.</p>

<h2 id="declaracion">Declaración responsable del fabricante</h2>
<p>El productor del programa debe certificar por escrito, mediante una declaración responsable, que cumple la Ley General Tributaria y el reglamento (art. 13.1). Debe constar de forma visible en el propio sistema, en cada versión, y entregarse al cliente al comprarlo (art. 13.2). Tú puedes pedirla (art. 13.3).</p>

<h2 id="modalidad">VERI*FACTU o no VERI*FACTU</h2>
<p>Un TPV puede enviar los registros a la AEAT al emitir cada ticket (modalidad VERI*FACTU) o conservarlos. La opción dura al menos hasta el fin del año natural del primer envío (art. 16.5). Compáralas en <a href="/blog/verifactu-modalidad-no-verifactu/">modalidades</a>.</p>

<h2 id="preguntas">Qué preguntar a tu proveedor</h2>
<ol class="steps">
<li>¿Tiene declaración responsable de la versión que tengo instalada?</li>
<li>¿Genera el QR y la huella en cada ticket, y funciona sin conexión?</li>
<li>¿Qué modalidad soporta y cómo se cambia?</li>
<li>¿Cómo se corrige o anula un ticket sin borrarlo?</li>
<li>¿Cómo se exportan los registros y el registro de eventos?</li>
<li>¿Se actualizará antes de tu fecha de obligación? Consulta las <a href="/blog/fechas-verifactu-2027-2028/">fechas</a>.</li>
</ol>
<p>Los productores deben ofrecer sus productos adaptados en el plazo fijado por la disposición final cuarta. Para el detalle de requisitos de un programa, mira <a href="/blog/verifactu-programa-facturacion-requisitos/">requisitos del programa de facturación</a>.</p>
""",
    faq=[
        ("¿Mi caja registradora tiene que cumplir Verifactu?", "Si genera facturas, completas o simplificadas, es un sistema informático de facturación y el reglamento se aplica a su titular si es un obligado del art. 3.1."),
        ("¿Qué es el registro de eventos?", "Un registro automático de interacciones, operaciones y sucesos del sistema, consultable desde el propio programa (art. 8.3)."),
        ("¿Puede mi TPV borrar un ticket?", "No debe poder alterar un registro sin que el sistema lo detecte; las correcciones se hacen con registros adicionales."),
        ("¿Quién emite la declaración responsable?", "La persona o entidad que produce el sistema informático (art. 13)."),
        ("¿Es obligatorio enviar los tickets a la AEAT?", "No. La remisión es voluntaria: es la modalidad VERI*FACTU (arts. 15 y 16)."),
        ("¿Cómo compruebo el QR de un ticket?", "Con el validador de QR de este sitio o escaneándolo; abre la URL de cotejo de la AEAT."),
    ],
    sources=[S.RD, S.ORDEN],
))

POSTS.append(dict(
    slug="verifactu-bares-restaurantes",
    published="2026-11-20",
    title="Verifactu en bares y restaurantes: tiques, TPV y QR",
    desc="Qué cambia para bares y restaurantes con Verifactu: TPV, tiques como facturas simplificadas, QR y cómo prepararte según el RD 1007/2023.",
    h1="Verifactu en bares y restaurantes: tiques, TPV y QR",
    intro="Un bar o restaurante que cobra con TPV y da tique usa un sistema informático de facturación. Te contamos qué exige el reglamento y qué hacer antes de tu fecha. Revisado el 20 de noviembre de 2026.",
    content="""
<p class="note"><strong>Respuesta corta:</strong> el reglamento no tiene normas específicas para hostelería. Si tu negocio es un obligado del art. 3.1 (sociedad, o autónomo con actividad económica) y usa un TPV o programa que emite tiques o facturas, ese programa debe cumplir el RD 1007/2023. El tique es, en general, una factura simplificada.</p>

<h2 id="aplica">Por qué te afecta</h2>
<p>El art. 3.1 incluye a los contribuyentes del Impuesto sobre Sociedades y a los del IRPF que desarrollan actividades económicas, aunque solo usen el sistema para parte de su actividad. Si tienes un bar como autónomo o como sociedad, estás dentro, salvo exclusiones como el SII (<a href="/blog/verifactu-sii-exentos/">quiénes quedan fuera</a>). Haz el <a href="/">test de obligación</a> para tu fecha.</p>

<h2 id="tique">El tique de la mesa</h2>
<p>El reglamento entiende por factura tanto la completa como la simplificada (art. 1.2). Cada tique que expide tu TPV genera un registro de alta, simultáneo o inmediatamente anterior a la emisión (art. 9). Y si un cliente pide factura con sus datos fiscales, esa factura también se registra. Más detalle: <a href="/blog/verifactu-factura-simplificada-ticket/">facturas simplificadas</a>.</p>

<h2 id="tpv">Tu TPV o programa de hostelería</h2>
<p>Lo que debe cumplir es lo mismo que cualquier caja: registros encadenados con huella, inalterabilidad, registro de eventos y conservación exportable. Está resumido en <a href="/blog/tpv-verifactu/">TPV Verifactu</a>. Lo importante en un bar es que lo cumpla el software, no que tú cambies de hábitos: el productor debe darte una declaración responsable (art. 13).</p>

<h2 id="qr">El QR en el tique</h2>
<p>El tique emitido con estos sistemas debe incluir el QR (art. 7.5 del Reglamento de facturación, añadido por el RD 1007/2023). La frase «VERI*FACTU» solo si el sistema envía los registros a la AEAT. Si el cliente escanea el QR, puede remitir los datos a la AEAT, y si el tique lleva la frase, comprobar que se envió (art. 17).</p>

<h2 id="correcciones">Errores en la cuenta</h2>
<p>Si cobras mal o cancelas un tique, el sistema no debe permitir borrarlo sin dejar rastro: el art. 11 regula el registro de anulación para facturas emitidas erróneamente y el art. 8.2.a las correcciones. Explicado en <a href="/blog/factura-rectificativa-verifactu/">facturas rectificativas</a>.</p>

<h2 id="comandas">¿Y las comandas y los pedidos?</h2>
<p>El reglamento regula los sistemas que soportan la facturación. No incluimos aquí cómo tratar comandas o pre-cuentas porque no lo desarrolla el texto del RD 1007/2023: pregunta a tu proveedor cómo las gestiona su producto.</p>

<h2 id="pasos">Cómo prepararte</h2>
<ol class="steps">
<li>Averigua tu fecha en las <a href="/blog/fechas-verifactu-2027-2028/">fechas de Verifactu</a>.</li>
<li>Pregunta a tu proveedor de TPV si ya tiene versión con declaración responsable.</li>
<li>Decide si enviarás los registros a la AEAT (VERI*FACTU) o no: <a href="/blog/verifactu-modalidad-no-verifactu/">modalidades</a>.</li>
<li>Prueba que un tique sale con QR y valídalo en el <a href="/validar-qr-verifactu/">validador</a>.</li>
<li>Forma al personal de sala en cómo se anula o corrige un cobro.</li>
</ol>
""",
    faq=[
        ("¿Un bar pequeño tiene que cumplir Verifactu?", "Si es obligado del art. 3.1 y su programa emite tiques o facturas, sí; las fechas dependen del tipo de obligado."),
        ("¿El tique de un restaurante es una factura?", "Para el reglamento, el término factura incluye la completa y la simplificada (art. 1.2); el tique suele ser simplificada."),
        ("¿Qué pasa si el cliente pide factura?", "Esa factura también genera un registro de alta en el sistema."),
        ("¿Debe llevar QR el tique?", "Sí, en las facturas emitidas con estos sistemas, incluidas las simplificadas, según el Reglamento de facturación modificado por el RD 1007/2023."),
        ("¿Puedo anular un tique cobrado por error?", "Sí, pero con un registro de anulación o de corrección, no borrándolo."),
        ("¿Dónde veo mi fecha límite?", "En el test de obligación de este sitio y en la guía de fechas de Verifactu."),
    ],
    sources=[S.RD, S.RDL],
))

POSTS.append(dict(
    slug="verifactu-modulos-estimacion-objetiva",
    published="2026-11-21",
    title="Verifactu y autónomos en módulos: ¿estoy obligado?",
    desc="Estar en módulos no te excluye de Verifactu por sí solo: lo que decide es si expides facturas con un programa. Criterio de la AEAT y pasos a seguir.",
    h1="Verifactu y autónomos en módulos: ¿estoy obligado?",
    intro="«Estoy en módulos, así que no me afecta»: es una de las frases más repetidas, y no es del todo exacta. Aquí tienes lo que dice la AEAT en sus preguntas frecuentes (actualizadas el 21 de octubre de 2026). Revisado el 21 de noviembre de 2026.",
    content="""
<p class="note"><strong>Respuesta corta:</strong> el reglamento no menciona la estimación objetiva. Lo que decide es si expides facturas (completas o simplificadas) y si lo haces con algún sistema informático de facturación. Si no expides factura, o la haces toda a mano, no te afecta; si expides alguna con un programa, sí.</p>

<h2 id="clave">La clave es la factura, no el régimen</h2>
<p>La AEAT explica que el reglamento solo se aplica a los sistemas informáticos de facturación, es decir, a los que sirven para expedir <em>facturas</em>, incluidas las simplificadas. Quien por su régimen no está obligado a expedir factura y no la expide, queda fuera, siempre que no use un programa para ello.</p>
<p>Pero la propia AEAT añade que, si en algún momento expides una factura por el motivo que sea y para ello usas un sistema informático, el reglamento sí se te aplica (con el resto de condiciones de la «regla de los 4 NO»).</p>

<h2 id="cuatro-no">La regla de los 4 «NO»</h2>
<p>Según la AEAT, quedan sometidos los empresarios y profesionales establecidos en España que expidan facturas y cumplan estas cuatro condiciones:</p>
<ol class="steps">
<li>No facturan exclusivamente a mano, sin ayuda de un sistema informático.</li>
<li>No están adscritos, de forma obligatoria o voluntaria, al Suministro Inmediato de Información (SII).</li>
<li>No tienen domicilio fiscal en los territorios históricos del País Vasco ni en Navarra.</li>
<li>No tienen una resolución en vigor de no aplicación (art. 5 del reglamento).</li>
</ol>
<p>Más sobre los excluidos en <a href="/blog/verifactu-sii-exentos/">quién queda fuera de Verifactu</a>.</p>

<h2 id="simplificado">Régimen simplificado de IVA</h2>
<p>Muchos autónomos «en módulos» lo están también en el régimen simplificado del IVA. La AEAT indica que, con carácter general, no están obligados a expedir factura, salvo excepciones. Entre ellas, la AEAT enumera: cuando las cuotas devengadas se determinan en función del volumen de ingresos, la venta de activos fijos, cuando el cliente es empresario, profesional o Administración Pública, cuando el destinatario la exige para ejercer un derecho tributario y determinadas operaciones de comercio exterior.</p>
<p>Si expides alguna de esas facturas con un programa, debes usar uno adaptado. Para estas operaciones excepcionales puedes usar la aplicación que la AEAT ofrece en su sede electrónica (art. 7.b del reglamento).</p>

<h2 id="recargo">Recargo de equivalencia y agricultura</h2>
<p>Lo mismo ocurre con el recargo de equivalencia y el régimen especial agrario: en general no hay obligación de expedir factura, pero sí cuando se da alguna de las excepciones. Las vemos en <a href="/blog/verifactu-recargo-equivalencia/">Verifactu y recargo de equivalencia</a>.</p>

<h2 id="tiques">¿Y si doy tiques con caja registradora?</h2>
<p>Depende de qué documento sea. La AEAT aclara que los justificantes de venta que no sean facturas completas ni simplificadas, emitidos en operaciones excluidas de la obligación de facturar, no están sometidos al reglamento. Si tu caja emite lo que en realidad es una factura simplificada, sí. Cualquiera que sea la razón por la que emitas facturas con un sistema informático, debes adaptarlo. Detalle en <a href="/blog/tpv-verifactu/">TPV Verifactu</a>.</p>

<h2 id="excel">¿Y si hago las facturas con Excel o Word?</h2>
<p>La AEAT dice que no te afecta si la hoja o el documento solo sirven para introducir datos, expedir e imprimir facturas y conservar la información. Sí te afecta si además procesas esos datos para generar libros registro u otros resultados fiscales. Está explicado en <a href="/blog/verifactu-excel-word/">Verifactu con Excel y Word</a>.</p>

<h2 id="fechas">Fechas si te afecta</h2>
<p>Los autónomos (contribuyentes del IRPF con actividad económica) deben tener los sistemas adaptados antes del 6 de octubre de 2028 (disposición final cuarta del RD 1007/2023, tras el Real Decreto-ley 43/2026). Comprueba tu caso en el <a href="/">test de obligación</a> y en la <a href="/blog/fechas-verifactu-2027-2028/">guía de fechas</a>.</p>

<h2 id="pasos">Qué hacer</h2>
<ol class="steps">
<li>Anota si expides facturas y de qué tipo (completa, simplificada).</li>
<li>Mira con qué las haces: a mano, hoja de cálculo, caja, programa.</li>
<li>Si usas un programa, pregunta a tu proveedor desde qué versión cumple.</li>
<li>Si facturas poco, valora la <a href="/blog/verifactu-gratis-aplicacion-aeat/">aplicación gratuita de la AEAT</a>.</li>
<li>Ante dudas concretas, consulta con tu gestor: aquí damos criterio general, no asesoramiento personal.</li>
</ol>
""",
    faq=[
        ("¿Los autónomos en módulos están obligados a Verifactu?", "No por estar en módulos: la AEAT lo vincula a si expides facturas con un sistema informático."),
        ("¿Y si no emito facturas?", "Si no expides factura, o todas las haces a mano, el reglamento no te afecta."),
        ("¿Qué pasa si un cliente me pide factura?", "Si la expides con un programa, ese programa debe estar adaptado al reglamento."),
        ("¿Puedo usar la aplicación gratuita de la AEAT?", "Sí para las facturas excepcionales, según el art. 7.b del reglamento; no emite facturas simplificadas."),
        ("¿Cuál es mi fecha límite?", "Los autónomos con actividad económica, antes del 6 de octubre de 2028, salvo que quedes fuera por la regla de los 4 NO."),
        ("¿Esto es asesoramiento fiscal?", "No: es una explicación general basada en las preguntas frecuentes de la AEAT."),
    ],
    sources=[S.RD, S.FAQ_AMB, S.RDL],
))

POSTS.append(dict(
    slug="qr-verifactu-ejemplo",
    published="2026-11-21",
    title="QR Verifactu: ejemplo real de URL y cómo se lee",
    desc="Ejemplo oficial de la URL del QR de Verifactu, qué significa cada parámetro (nif, numserie, fecha, importe) y cómo comprobarla paso a paso.",
    h1="QR Verifactu: ejemplo real de URL y cómo se lee",
    intro="El QR de una factura Verifactu es solo una URL con cuatro datos. Aquí tienes el ejemplo oficial, qué significa cada parte y cómo comprobarlo. Basado en las especificaciones técnicas de la AEAT v0.5.0 (10/12/2025). Revisado el 21 de noviembre de 2026.",
    content="""
<p class="note"><strong>Respuesta corta:</strong> el QR contiene la dirección de cotejo de la AEAT con cuatro parámetros: <code>nif</code>, <code>numserie</code>, <code>fecha</code> e <code>importe</code>. Quien lo escanea llega a la sede de la AEAT para comprobar que la factura consta.</p>

<h2 id="ejemplo">El ejemplo oficial</h2>
<p>La documentación técnica de la AEAT incluye este ejemplo de URL de producción:</p>
<p><code>https://www2.agenciatributaria.gob.es/wlpl/TIKE-CONT/ValidarQR?nif=89890001K&amp;numserie=12345678-G33&amp;fecha=01-09-2024&amp;importe=241.4</code></p>

<h2 id="partes">Qué significa cada parte</h2>
<div class="table-wrap"><table>
<thead><tr><th>Parte</th><th>Qué es</th><th>En el ejemplo</th></tr></thead>
<tbody>
<tr><td>Dominio y ruta</td><td>Servicio de cotejo de la AEAT (producción)</td><td>www2.agenciatributaria.gob.es/wlpl/TIKE-CONT/ValidarQR</td></tr>
<tr><td>nif</td><td>NIF del emisor, 9 caracteres</td><td>89890001K</td></tr>
<tr><td>numserie</td><td>Serie y número de la factura, hasta 60 caracteres</td><td>12345678-G33</td></tr>
<tr><td>fecha</td><td>Fecha de expedición, DD-MM-AAAA con guiones</td><td>01-09-2024</td></tr>
<tr><td>importe</td><td>Total de la factura, con punto decimal</td><td>241.4</td></tr>
</tbody></table></div>

<h2 id="reglas">Reglas de cada dato</h2>
<ul class="checklist">
<li>Son exactamente cuatro parámetros obligatorios.</li>
<li>El número de serie admite caracteres ASCII imprimibles (32 a 126) y se codifica en la URL: por ejemplo, el símbolo &amp; pasa a %26.</li>
<li>El importe usa punto como separador decimal, con un máximo de 12 cifras enteras y 2 decimales.</li>
<li>La fecha va en formato DD-MM-AAAA.</li>
<li>Hay un parámetro opcional de idioma (gl, ca, eu, es, va, en), que por defecto es es.</li>
</ul>

<h2 id="pruebas">Entorno de pruebas y sistemas sin VERI*FACTU</h2>
<p>La AEAT tiene un entorno de pruebas (prewww2.aeat.es). Los sistemas que no envían los registros (modalidad NO VERI*FACTU) usan la ruta <code>ValidarQRNoVerifactu</code> en los mismos dominios. Ver <a href="/blog/verifactu-modalidad-no-verifactu/">las dos modalidades</a>.</p>

<h2 id="resultado">Qué ves al abrirla</h2>
<p>El cotejo devuelve «Encontrada» si el registro consta, «No encontrada» si no consta (o está anulada) y «No contrastable» si el sistema no envía registros. Una factura de un sistema NO VERI*FACTU no se puede cotejar en línea.</p>

<h2 id="leer">Cómo leerlo y comprobarlo</h2>
<ol class="steps">
<li>Escanea el QR con el móvil sin abrirlo y mira la URL completa.</li>
<li>Comprueba que el dominio es el de la AEAT.</li>
<li>Compara nif, fecha e importe con los de la factura impresa.</li>
<li>Pégala en el <a href="/validar-qr-verifactu/">validador de QR Verifactu</a>, que revisa el formato.</li>
<li>Si falla, mira <a href="/blog/errores-qr-verifactu-1001-2006/">los códigos de error del QR</a>.</li>
</ol>
<p>Para crear uno de prueba usa el <a href="/generador-qr-verifactu/">generador de QR</a>. Dónde colocarlo y qué tamaño: <a href="/blog/verifactu-qr-obligatorio/">QR obligatorio</a>.</p>
""",
    faq=[
        ("¿Qué contiene el QR de Verifactu?", "Una URL de la AEAT con cuatro parámetros: nif, numserie, fecha e importe."),
        ("¿Cómo se escribe la fecha?", "En formato DD-MM-AAAA, con guiones."),
        ("¿Cómo se escribe el importe?", "Con punto decimal, hasta 12 cifras enteras y 2 decimales."),
        ("¿Se puede probar con datos de ejemplo?", "Sí, existe un entorno de pruebas de la AEAT; los datos de ejemplo no son facturas reales."),
        ("¿Qué pasa si mi sistema no envía los registros?", "Usa la ruta ValidarQRNoVerifactu y el cotejo devuelve «No contrastable»."),
        ("¿Dónde compruebo mi QR?", "En el validador de QR de este sitio y, para el cotejo real, en el enlace oficial de la AEAT."),
    ],
    sources=[S.QR, S.ORDEN, S.RD],
))

POSTS.append(dict(
    slug="errores-qr-verifactu-1001-2006",
    published="2026-11-21",
    title="Errores del QR Verifactu (1001 a 2006) y cómo corregirlos",
    desc="Lista de códigos de error del cotejo del QR de Verifactu (1001 a 2006, 3001 y 3002), qué significan y cómo corregir cada uno.",
    h1="Errores del QR Verifactu (1001 a 2006) y cómo corregirlos",
    intro="Si al abrir el QR de una factura la AEAT devuelve un código, el problema suele estar en uno de los cuatro datos de la URL. Esta es la lista según las especificaciones técnicas de la AEAT v0.5.0. Revisado el 21 de noviembre de 2026.",
    content="""
<p class="note"><strong>Respuesta corta:</strong> los errores 1001 a 1004 indican que falta un parámetro; los 2001 a 2006 que un valor tiene mal el formato o es demasiado largo; y los 3001 y 3002 son errores técnicos o límite de intentos.</p>

<h2 id="tabla">Tabla de códigos</h2>
<div class="table-wrap"><table>
<thead><tr><th>Código</th><th>Significado</th><th>Cómo corregirlo</th></tr></thead>
<tbody>
<tr><td>1001</td><td>No se ha remitido el parámetro nif</td><td>Añade el NIF del emisor a la URL</td></tr>
<tr><td>1002</td><td>No se ha remitido el parámetro numserie</td><td>Añade serie y número de factura</td></tr>
<tr><td>1003</td><td>No se ha remitido el parámetro fecha</td><td>Añade la fecha de expedición</td></tr>
<tr><td>1004</td><td>No se ha remitido el parámetro importe</td><td>Añade el importe total</td></tr>
<tr><td>2001</td><td>NIF con formato erróneo o no válido</td><td>Revisa los 9 caracteres y la letra</td></tr>
<tr><td>2002</td><td>Número de serie demasiado largo</td><td>Máximo 60 caracteres</td></tr>
<tr><td>2003</td><td>Número de serie con caracteres no permitidos</td><td>Usa solo ASCII imprimible y codifica la URL</td></tr>
<tr><td>2004</td><td>Fecha con formato inválido</td><td>Usa DD-MM-AAAA</td></tr>
<tr><td>2005</td><td>Importe con formato incorrecto</td><td>Usa punto decimal, no coma</td></tr>
<tr><td>2006</td><td>Importe demasiado largo</td><td>Máximo 12 enteros y 2 decimales</td></tr>
<tr><td>3001</td><td>Error técnico en los sistemas de la AEAT</td><td>Reintenta más tarde</td></tr>
<tr><td>3002</td><td>Máximo de intentos diarios superado</td><td>Espera al día siguiente</td></tr>
</tbody></table></div>

<h2 id="faltan">Errores 1001 a 1004: falta un dato</h2>
<p>Suelen aparecer cuando el programa genera la URL sin uno de los cuatro campos, o cuando un carácter especial corta la cadena. Comprueba la URL escaneada completa, no solo el dibujo del QR. Cómo es una URL correcta: <a href="/blog/qr-verifactu-ejemplo/">ejemplo de QR Verifactu</a>.</p>

<h2 id="formato">Errores 2001 a 2006: formato</h2>
<ul class="checklist">
<li><strong>2001:</strong> el NIF debe tener 9 caracteres y ser válido.</li>
<li><strong>2002 y 2003:</strong> el número de serie no puede pasar de 60 caracteres ni llevar caracteres fuera del ASCII imprimible. Si lleva un símbolo como &amp;, debe ir codificado (%26).</li>
<li><strong>2004:</strong> la fecha va con guiones y el día primero: 01-09-2024.</li>
<li><strong>2005 y 2006:</strong> el importe se escribe 241.4 y no 241,4; con 12 enteros y 2 decimales como máximo.</li>
</ul>

<h2 id="tecnicos">Errores 3001 y 3002</h2>
<p>El 3001 es un fallo de los sistemas de la AEAT, no de tu factura. El 3002 indica que se ha superado el número máximo de intentos por día, así que conviene no repetir pruebas en bucle.</p>

<h2 id="noencontrada">Y si dice «No encontrada»</h2>
<p>No es un código de error: significa que el cotejo no halla el registro (o consta anulado). Puede ser que el sistema aún no lo haya enviado, que los datos no coincidan exactamente o que la factura venga de un sistema NO VERI*FACTU. El resultado «No contrastable» indica precisamente eso último.</p>

<h2 id="pasos">Cómo diagnosticarlo</h2>
<ol class="steps">
<li>Escanea el QR y copia la URL completa.</li>
<li>Pégala en el <a href="/validar-qr-verifactu/">validador de QR Verifactu</a>: revisa los cuatro parámetros y muestra el código que corresponde.</li>
<li>Corrige el dato en tu programa de facturación y vuelve a emitir.</li>
<li>Genera una prueba con el <a href="/generador-qr-verifactu/">generador de QR</a> y compárala.</li>
</ol>
<p>Si el problema es de tamaño o posición del QR, no del contenido, mira <a href="/blog/verifactu-qr-obligatorio/">qué exige el QR obligatorio</a>.</p>
""",
    faq=[
        ("¿Qué significa el error 1001 del QR Verifactu?", "Que la URL no incluye el parámetro nif."),
        ("¿Qué significa el error 2005?", "Que el importe tiene un formato incorrecto, por ejemplo con coma en vez de punto."),
        ("¿Y el 2004?", "Que la fecha no tiene el formato DD-MM-AAAA."),
        ("¿Qué es el error 3002?", "Que se ha superado el número máximo de intentos permitidos por día."),
        ("¿«No encontrada» es un error?", "No: el cotejo no halla el registro, o consta anulado."),
        ("¿Cómo corrijo el error en mi factura?", "Corrige el dato en tu programa y emite el QR correcto; el validador de este sitio te indica cuál falla."),
    ],
    sources=[S.QR, S.ORDEN],
))

# ---------------------------------------------------------------- #6 demora Hacienda vs comerciales (22/11/2026)
POSTS.append(dict(
    slug="intereses-demora-hacienda-vs-comerciales",
    published="2026-11-22",
    title="Intereses de demora: Hacienda frente a los comerciales",
    desc="Diferencia entre el interés de demora tributario (art. 26 LGT) y el de facturas entre empresas (Ley 3/2004): fórmula, tipo y ejemplo.",
    h1="Intereses de demora de Hacienda frente a los comerciales: diferencias",
    intro="Se llaman igual, pero no se calculan igual. Comparamos el interés de demora tributario de la Ley General Tributaria con el de las operaciones comerciales de la Ley 3/2004, con el tipo comercial vigente y un ejemplo. Revisado en el BOE el 22 de noviembre de 2026.",
    content="""
<p class="note"><strong>Respuesta corta:</strong> el interés de demora <strong>tributario</strong> es el interés legal del dinero incrementado en un 25 %, salvo que la Ley de Presupuestos fije otro (art. 26.6 de la Ley General Tributaria). El <strong>comercial</strong> es el pactado en el contrato o, si no hay pacto, el tipo del Banco Central Europeo más ocho puntos, que el Tesoro publica cada semestre (art. 7 de la Ley 3/2004). Son dos regímenes distintos.</p>

<h2 id="cuadro">Cuadro comparativo</h2>
<div class="table-wrap"><table>
<thead><tr><th>Aspecto</th><th>Tributario (Hacienda)</th><th>Comercial (entre empresas)</th></tr></thead>
<tbody>
<tr><td>Norma</td><td>Ley 58/2003 General Tributaria, art. 26</td><td>Ley 3/2004 contra la morosidad, art. 7</td></tr>
<tr><td>Quién lo cobra</td><td>La Administración tributaria al obligado</td><td>El proveedor al cliente que paga tarde</td></tr>
<tr><td>Cálculo del tipo</td><td>Interés legal del dinero vigente + 25 %, salvo otra previsión de la Ley de Presupuestos</td><td>Pacto contractual o, por defecto, BCE + 8 puntos</td></tr>
<tr><td>Revisión</td><td>Según el interés legal vigente en el periodo en que es exigible</td><td>Cada semestre natural, por resolución del Tesoro en el BOE</td></tr>
<tr><td>¿Requiere reclamar?</td><td>No requiere intimación previa ni retraso culpable</td><td>Se devenga desde el día siguiente al vencimiento; conviene reclamarlo</td></tr>
</tbody></table></div>

<h2 id="tributario">El interés de demora tributario</h2>
<p>El artículo 26 de la Ley General Tributaria lo define como una prestación accesoria que se exige por pagar fuera de plazo, presentar tarde una autoliquidación con cantidad a ingresar, cobrar una devolución improcedente y otros casos previstos en la normativa. Dos rasgos importantes:</p>
<ul>
<li>No requiere que la Administración te intime antes ni que haya un retraso culpable por tu parte (art. 26.1).</li>
<li>Se calcula sobre el importe no ingresado a tiempo y es exigible mientras dura el retraso (art. 26.3).</li>
</ul>
<p>El apartado 6 fija el tipo: el interés legal del dinero vigente a lo largo del periodo en que es exigible, más un 25 %, salvo que la Ley de Presupuestos Generales del Estado establezca otro. Si hay aplazamiento, fraccionamiento o suspensión con aval solidario de entidad de crédito, sociedad de garantía recíproca o seguro de caución por toda la deuda, el interés exigible es el interés legal sin incremento. <strong>Aquí no damos un porcentaje</strong>: depende de la Ley de Presupuestos de cada año, así que consulta el vigente en la AEAT antes de calcular una deuda concreta.</p>
<p>Además, el apartado 4 prevé que no se exijan intereses desde que la Administración incumple por causa imputable a ella algún plazo legal para resolver, hasta que dicte resolución, con excepciones como las solicitudes de aplazamiento o fraccionamiento.</p>

<h2 id="comercial">El interés de demora comercial</h2>
<p>En las facturas entre empresas, el artículo 7 de la Ley 3/2004 dice que el deudor pagará el interés del contrato y, a falta de pacto, el tipo legal: el tipo aplicado por el BCE a su operación principal de financiación más reciente antes del primer día del semestre, más ocho puntos. Ese tipo rige seis meses y el Ministerio publica el resultado en el BOE cada semestre.</p>
<p>Para el segundo semestre de 2026, la resolución del Tesoro de 30 de junio de 2026 publica un <strong>10,40 %</strong> (BCE 2,40 % + 8 puntos). Para el primer semestre de 2026 fue el 10,15 %. Puedes comprobar cualquier fecha con la <a href="/intereses-demora-comerciales/">calculadora de intereses de demora comerciales</a>.</p>
<div class="table-wrap"><table>
<thead><tr><th>Dato</th><th>Valor</th></tr></thead>
<tbody>
<tr><td>Factura impagada</td><td>10.000 €</td></tr>
<tr><td>Retraso</td><td>30 días naturales dentro del segundo semestre de 2026</td></tr>
<tr><td>Tipo aplicable (sin pacto)</td><td>10,40 % anual</td></tr>
<tr><td>Cálculo</td><td>10.000 × 10,40 % × 30 / 365</td></tr>
<tr><td>Interés de demora</td><td>85,48 €</td></tr>
</tbody></table></div>
<p>A ese interés se suma, en su caso, la indemnización por costes de cobro que prevé la Ley 3/2004, de 40 euros por factura. Te lo explicamos en <a href="/blog/reclamar-factura-impagada-intereses/">cómo reclamar una factura impagada con intereses</a>.</p>

<h2 id="confusion">Errores frecuentes</h2>
<ol class="steps">
<li><strong>Aplicar el tipo de Hacienda a una factura entre empresas.</strong> No corresponde: a un impago comercial se le aplica el pacto o el tipo de la Ley 3/2004.</li>
<li><strong>Usar el tipo comercial para una deuda tributaria.</strong> Tampoco: la deuda con Hacienda sigue el artículo 26 de la LGT.</li>
<li><strong>Olvidar que el tipo comercial cambia cada semestre.</strong> Si el retraso cruza el 1 de julio o el 1 de enero, hay que aplicar cada tipo a su tramo.</li>
<li><strong>Dar por hecho un tipo sin mirar la fuente.</strong> Confirma siempre la resolución del Tesoro del semestre en el <a href="/blog/tipo-interes-demora-2026/">resumen de tipos vigentes</a>.</li>
</ol>

<h2 id="ap">Cuándo importa cada uno</h2>
<p>Si eres autónomo o empresa y un cliente te paga tarde, importa el comercial; usa también la guía de <a href="/blog/plazos-pago-ley-morosidad/">plazos de pago de la ley de morosidad</a>. Si tú pagas tarde un impuesto o una sanción, importa el tributario y su tipo anual lo marca la normativa presupuestaria.</p>
""",
    faq=[
        ("¿Es el mismo interés el de Hacienda y el de una factura?", "No: el tributario se rige por el art. 26 de la LGT y el comercial por el art. 7 de la Ley 3/2004."),
        ("¿Cómo se calcula el interés tributario?", "Es el interés legal del dinero vigente en el periodo, incrementado en un 25 %, salvo que la Ley de Presupuestos fije otro (art. 26.6 LGT)."),
        ("¿Cuál es el tipo comercial del segundo semestre de 2026?", "10,40 %, según la resolución del Tesoro de 30 de junio de 2026 (BCE 2,40 % más 8 puntos)."),
        ("¿Hay que reclamar el interés comercial?", "Se devenga por el retraso, pero en la práctica conviene reclamarlo por escrito al deudor."),
        ("¿Se pueden pactar otros intereses entre empresas?", "El art. 7 da preferencia al pacto contractual; el tipo legal se aplica a falta de pacto."),
        ("¿Dónde veo el tipo vigente?", "En la resolución semestral del Tesoro publicada en el BOE y en la calculadora de este sitio."),
    ],
    sources=[S.LGT, S.LEY3, S.TESORO26, S.TESORO26A],
))

# ---------------------------------------------------------------- #25 PMP entidades locales (22/11/2026)
POSTS.append(dict(
    slug="periodo-medio-pago-entidades-locales",
    published="2026-11-22",
    title="Periodo medio de pago de entidades locales (RD 635/2014)",
    desc="Cómo calcula una entidad local su periodo medio de pago según el RD 635/2014: operaciones, días de pago, ratios pagadas y pendientes, y publicación.",
    h1="Periodo medio de pago de las entidades locales: cálculo según el RD 635/2014",
    intro="El Real Decreto 635/2014 fija cómo calculan el periodo medio de pago las Administraciones Públicas, entre ellas las corporaciones locales. Resumimos qué operaciones cuentan, desde qué fecha se cuentan los días y qué se publica. Revisado en el BOE el 22 de noviembre de 2026.",
    content="""
<p class="note"><strong>Respuesta corta:</strong> el periodo medio de pago de una entidad combina la ratio de operaciones pagadas y la de operaciones pendientes, ponderadas por sus importes (art. 5 del RD 635/2014). Cuenta los días naturales desde la aprobación de la certificación o de la conformidad, o desde la entrada de la factura en el registro, hasta el pago o hasta el último día del periodo. No es lo mismo que el cálculo del periodo medio de pago de las empresas, que regula el ICAC.</p>

<h2 id="ambito">A quién se aplica</h2>
<p>El artículo 2 del real decreto lo aplica a todos los sujetos del artículo 2.1 de la Ley Orgánica 2/2012 de estabilidad presupuestaria, es decir, las Administraciones Públicas. El artículo 4 menciona expresamente a la Administración Central, las comunidades autónomas, las corporaciones locales y las Administraciones de la Seguridad Social. Si eres una empresa privada, tu obligación es otra: mira el <a href="/periodo-medio-pago-proveedores/">calculador de periodo medio de pago a proveedores</a> y la guía <a href="/blog/periodo-medio-pago-maximo-legal/">sobre el máximo legal</a>.</p>

<h2 id="operaciones">Qué operaciones entran</h2>
<ul>
<li>Las facturas expedidas desde el 1 de enero de 2014 que consten en el registro contable de facturas o sistema equivalente, y las certificaciones mensuales de obra aprobadas desde esa fecha (art. 3.1).</li>
<li>Quedan excluidas las obligaciones entre entidades que sean Administraciones Públicas en contabilidad nacional y las pagadas con cargo al Fondo para la Financiación de los Pagos a Proveedores.</li>
<li>También quedan excluidas las propuestas de pago retenidas por embargos, mandamientos de ejecución, procedimientos administrativos de compensación o actos análogos de órganos judiciales o administrativos (art. 3.2).</li>
</ul>

<h2 id="dias">Desde cuándo se cuentan los días</h2>
<div class="table-wrap"><table>
<thead><tr><th>Caso</th><th>Los días naturales se cuentan desde…</th></tr></thead>
<tbody>
<tr><td>Certificaciones de obra</td><td>La fecha de aprobación de la certificación</td></tr>
<tr><td>Hay aceptación o comprobación de bienes o servicios</td><td>La fecha de aprobación del documento de conformidad</td></tr>
<tr><td>No hay aceptación, o la factura llega después de la conformidad</td><td>La fecha de entrada de la factura en el registro administrativo</td></tr>
<tr><td>No hay obligación de registro contable</td><td>La fecha de recepción de la factura en el registro administrativo</td></tr>
</tbody></table></div>
<p>El final del cómputo es distinto según la operación esté pagada o pendiente: para las pagadas, la fecha de pago material; para las pendientes, el último día del periodo al que se refieren los datos publicados (art. 5.2 y 5.3).</p>

<h2 id="formula">Las dos ratios y el resultado</h2>
<ol class="steps">
<li><strong>Ratio de operaciones pagadas:</strong> media de los días de pago de cada operación pagada en el periodo, ponderada por su importe.</li>
<li><strong>Ratio de operaciones pendientes:</strong> lo mismo con los días pendientes de las operaciones aún sin pagar al final del periodo.</li>
<li><strong>Periodo medio de pago de la entidad:</strong> (ratio pagadas × importe pagado + ratio pendientes × importe pendiente) / (importe pagado + importe pendiente).</li>
</ol>
<p>Ejemplo ilustrativo con cifras inventadas para entender la mecánica: una entidad pagó 120.000 € con ratio de 20 días y tiene 60.000 € pendientes con ratio de 40 días. El cálculo es (20 × 120.000 + 40 × 60.000) / 180.000 = 26,67 días.</p>

<h2 id="trimestre">Mensual o trimestral</h2>
<p>La referencia al mes se entiende hecha al <strong>trimestre</strong> en las corporaciones locales no incluidas en el ámbito de los artículos 111 y 135 del texto refundido de la Ley Reguladora de las Haciendas Locales (art. 5.4, redacción vigente desde el 1 de abril de 2018).</p>

<h2 id="publicidad">Qué se publica</h2>
<p>Las corporaciones locales remiten al Ministerio y publican en sus portales web, con criterios homogéneos, el periodo medio de pago global, el de cada entidad, y la ratio de operaciones pagadas y pendientes de cada una, con su serie histórica, referidos al mes o trimestre anterior (art. 6.2). Es una información sobre las Administraciones, que sirve a los proveedores para saber cuánto tarda en pagar su ayuntamiento.</p>

<h2 id="empresa">Y si facturo a un ayuntamiento</h2>
<p>El periodo medio de pago de la entidad es un indicador agregado, no un plazo que puedas reclamar. Tu derecho a cobrar y a intereses nace de la factura concreta y de la Ley 3/2004; consulta <a href="/intereses-demora-comerciales/">la calculadora de intereses</a> y la guía de <a href="/blog/informar-pago-factura-4-dias/">plazos de pago</a>.</p>
""",
    faq=[
        ("¿Qué norma regula el PMP de las entidades locales?", "El Real Decreto 635/2014, de 25 de julio, en su texto consolidado."),
        ("¿Cuenta desde la fecha de la factura?", "No siempre: puede contar desde la conformidad o la aprobación de la certificación; solo en algunos casos desde la entrada de la factura en el registro."),
        ("¿El PMP local es mensual?", "Depende: en las corporaciones locales fuera del ámbito de los arts. 111 y 135 del TRLRHL, la referencia es trimestral."),
        ("¿Qué se excluye del cálculo?", "Obligaciones entre Administraciones, pagos del Fondo de proveedores y propuestas retenidas por embargos o compensaciones."),
        ("¿Es lo mismo que el PMP de las empresas?", "No: las empresas lo calculan según la resolución del ICAC de 2016."),
        ("¿Dónde se publica el PMP de un ayuntamiento?", "En el portal web de la propia entidad y en el Ministerio de Hacienda, según el art. 6.2."),
    ],
    sources=[S.RD635, S.ICAC],
))

# ---------------------------------------------------------------- Phase 2: cláusulas abusivas de plazo de pago
POSTS.append(dict(
    slug="clausulas-abusivas-plazo-pago-morosidad",
    published="2026-11-24",
    title="Cláusulas abusivas de pago: cuándo un pacto es nulo",
    desc="Pago a 90 días, intereses rebajados o sin 40 euros: qué dice el art. 9 de la Ley 3/2004, el límite de 60 días y la regla del 70 % sobre el interés legal.",
    h1="Cláusulas abusivas de plazo de pago: cuándo un pacto con tu cliente es nulo",
    intro="Muchos contratos entre empresas fijan pagos a 90 o 120 días o excluyen los intereses de demora. La Ley 3/2004 limita lo que se puede pactar. Esto es lo que dice el texto consolidado del BOE, con un ejemplo numérico.",
    content="""
<p class="note"><strong>Respuesta corta:</strong> entre empresas y autónomos, el plazo de pago pactado no puede superar los <strong>60 días naturales</strong> (art. 4.3), y es nula toda cláusula que excluya los intereses de demora o los 40 euros de costes de cobro (art. 9.1). Un interés pactado un 70 % por debajo del legal se considera abusivo, salvo prueba en contrario.</p>
<p>Esta guía resume la Ley 3/2004, de 29 de diciembre, en su texto consolidado. No es asesoramiento jurídico: si hay una cantidad importante en juego, consulta a un abogado o a tu asociación empresarial.</p>

<h2 id="limite">El límite de 60 días</h2>
<p>El artículo 4 fija el plazo general en 30 días naturales desde la entrega de los bienes o la prestación del servicio. Las partes pueden ampliarlo por pacto, pero «en ningún caso» más de <strong>60 días naturales</strong> (art. 4.3). Un contrato que diga «pago a 90 días fecha factura» choca, por tanto, con la ley.</p>
<p>Si hay un procedimiento de aceptación o comprobación de la conformidad, este no puede durar más de 30 días naturales desde la recepción, y el plazo de pago es de 30 días tras la aceptación, aunque la factura hubiera llegado antes (art. 4.2).</p>

<h2 id="abusiva">Qué considera abusivo el artículo 9</h2>
<p>El artículo 9.1 declara nula una cláusula o práctica sobre la fecha o plazo de pago, el tipo de interés de demora o la compensación por costes de cobro cuando sea «manifiestamente abusiva» en perjuicio del acreedor. El juez valora todas las circunstancias, entre ellas:</p>
<ul>
<li>una desviación grave de las buenas prácticas comerciales, contraria a la buena fe;</li>
<li>la naturaleza del bien o del servicio;</li>
<li>si el deudor tiene una razón objetiva para apartarse del interés legal de demora o de los 40 euros;</li>
<li>si la cláusula sirve sobre todo para darle al deudor liquidez adicional a costa del acreedor;</li>
<li>si un contratista principal impone a sus subcontratistas condiciones de pago que no están justificadas por las condiciones de las que él mismo se beneficia.</li>
</ul>

<h2 id="siempre-nulas">Siempre nulas, sin matices</h2>
<p>El mismo artículo 9.1 añade que son nulas en todo caso las cláusulas o prácticas contrarias a los requisitos para exigir intereses (art. 6) y las que excluyan el cobro del interés de demora o de la indemnización por costes de cobro del artículo 8. Un contrato que diga «no se devengarán intereses por demora» o «el proveedor renuncia a los 40 euros» no tiene efecto sobre esos derechos.</p>

<h2 id="setenta">La regla del 70 %</h2>
<p>Un interés pactado distinto del legal es válido si no es abusivo. La ley presume abusivo el interés pactado que sea <strong>un 70 por ciento inferior al interés legal de demora</strong>, salvo que, atendiendo a las circunstancias del artículo 9, se pruebe que no es abusivo.</p>
<div class="table-wrap"><table>
<thead><tr><th>Dato</th><th>Valor</th></tr></thead>
<tbody>
<tr><td>Tipo legal de demora, segundo semestre de 2026</td><td>10,40 %</td></tr>
<tr><td>Un 70 % inferior</td><td>10,40 × (1 − 0,70) = 3,12 %</td></tr>
<tr><td>Interés pactado de 2 %</td><td>Por debajo de 3,12 %: se presume abusivo</td></tr>
<tr><td>Interés pactado de 6 %</td><td>No alcanza esa presunción; se valora en el caso concreto</td></tr>
</tbody></table></div>
<p>La cuenta es aritmética sobre el tipo publicado; comprueba siempre el tipo del semestre en el que venció tu factura con la <a href="/intereses-demora-comerciales/">calculadora de intereses de demora</a>, y lee cómo se fija en <a href="/blog/tipo-interes-demora-2026/">el tipo de interés de demora de 2026</a>.</p>

<h2 id="juez">Qué hace el juez si una cláusula es nula</h2>
<p>Según el artículo 9.2, el juez que declare la nulidad integra el contrato conforme al artículo 1.258 del Código Civil y puede moderar los derechos y obligaciones de las partes. Las condiciones generales de contratación abusivas también son nulas (art. 9.3), y asociaciones de empresarios, de autónomos y las cámaras de comercio pueden ejercer acciones de cesación (art. 9.4).</p>

<h2 id="pasos">Qué hacer si tu contrato tiene una cláusula así</h2>
<ol class="steps">
<li><strong>Localiza la cláusula</strong> y anota el plazo, el interés y si menciona costes de cobro.</li>
<li><strong>Compara con la ley:</strong> plazo máximo de 60 días, interés pactado frente al legal, exclusiones.</li>
<li><strong>Calcula lo que te corresponde</strong> con el tipo legal desde el día siguiente al vencimiento legal o pactado válido.</li>
<li><strong>Reclama por escrito</strong> siguiendo los pasos de <a href="/blog/reclamar-factura-impagada-intereses/">cómo reclamar una factura impagada</a>.</li>
</ol>

<h2 id="comerciante">Una excepción a tener presente</h2>
<p>La disposición adicional primera de la Ley 3/2004 indica que, en los pagos a proveedores del comercio minorista regulado por la Ley 7/1996, se aplica primero su artículo 17 y, de forma supletoria, la Ley 3/2004. Si vendes a un comercio minorista, revisa también esa norma.</p>
<p>Para entender el plazo que realmente se aplica a tus facturas, consulta los <a href="/blog/plazos-pago-ley-morosidad/">plazos de pago de la Ley de morosidad</a>, y para medirlo en tu empresa, el <a href="/periodo-medio-pago-proveedores/">periodo medio de pago</a>.</p>
""",
    faq=[
        ("¿Se puede pactar pago a 90 días entre empresas?", "No: el art. 4.3 de la Ley 3/2004 prohíbe acordar un plazo superior a 60 días naturales."),
        ("¿Puedo renunciar a los intereses de demora en el contrato?", "La cláusula que excluya el cobro de intereses es nula en todo caso (art. 9.1)."),
        ("¿Y a los 40 euros de costes de cobro?", "También es nula la cláusula que excluya la indemnización del art. 8."),
        ("¿Qué interés pactado se presume abusivo?", "El que sea un 70 % inferior al interés legal, salvo que se pruebe que no es abusivo."),
        ("¿Qué pasa si el juez anula la cláusula?", "Integra el contrato según el art. 1.258 del Código Civil y puede moderar las consecuencias (art. 9.2)."),
        ("¿Quién puede denunciar estas cláusulas en grupo?", "Asociaciones de empresarios, profesionales y autónomos, cámaras de comercio y colegios profesionales (art. 9.4)."),
    ],
    sources=[S.LEY3],
))

# ---------------------------------------------------------------- Phase 2: 40 euros costes de cobro
POSTS.append(dict(
    slug="40-euros-costes-de-cobro-morosidad",
    published="2026-11-25",
    title="Los 40 euros de costes de cobro por factura impagada",
    desc="Cuándo puedes cobrar los 40 euros de la Ley 3/2004 por una factura impagada, si se suman a los intereses, qué pasa en pagos a plazos y cuándo no se deben.",
    h1="Los 40 euros de costes de cobro: cuándo se suman a una factura impagada",
    intro="Además de los intereses de demora, la Ley 3/2004 te da derecho a una cantidad fija de 40 euros cuando un cliente empresa te paga tarde. Esto dice el texto consolidado del BOE, con un ejemplo.",
    content="""
<p class="note"><strong>Respuesta corta:</strong> si el deudor incurre en mora, el acreedor tiene derecho a cobrar <strong>40 euros</strong> que se añaden «en todo caso y sin necesidad de petición expresa» a la deuda principal (art. 8.1). Además puedes reclamar los costes de cobro acreditados que superen esa cantidad.</p>
<p>Esta guía resume la Ley 3/2004, de 29 de diciembre, en su texto consolidado. No es asesoramiento jurídico.</p>

<h2 id="que-es">Qué son los 40 euros</h2>
<p>El artículo 8 se titula «Indemnización por costes de cobro». Es una cantidad fija, no un porcentaje: no depende del importe de la factura. Se suma a la deuda principal y es independiente de los intereses de demora del artículo 7.</p>
<p>Además, el acreedor puede reclamar una indemnización por todos los costes de cobro debidamente acreditados que haya sufrido por la mora y que superen esos 40 euros (art. 8.1, segundo párrafo). Piensa en gastos de gestión de reclamación que puedas justificar con documentos.</p>

<h2 id="requisitos">Requisitos para poder exigirlo</h2>
<p>El artículo 6 exige que concurran a la vez dos requisitos para reclamar intereses de demora, y la ley de costes de cobro se apoya en la misma situación de mora:</p>
<ul>
<li>que hayas cumplido tus obligaciones contractuales y legales;</li>
<li>que no hayas recibido a tiempo la cantidad debida, salvo que el deudor pruebe que no es responsable del retraso.</li>
</ul>

<h2 id="no-debe">Cuándo no se deben</h2>
<p>El artículo 8.2 dice que el deudor no está obligado a pagar esta indemnización cuando no sea responsable del retraso en el pago. Y, al revés, es nula toda cláusula que excluya los 40 euros (art. 9.1), como explicamos en <a href="/blog/clausulas-abusivas-plazo-pago-morosidad/">cláusulas abusivas de plazo de pago</a>.</p>

<h2 id="plazos">Pagos a plazos</h2>
<p>Si pactáis un calendario de pagos y una cuota no se abona en su fecha, los intereses y la compensación de la ley se calculan únicamente sobre las cantidades vencidas (art. 6, último párrafo).</p>

<h2 id="ejemplo">Ejemplo con cifras</h2>
<p>Una factura de 1.000 € venció y se pagó con retraso. Con un tipo de demora del 10,40 % (segundo semestre de 2026) y 30 días de retraso:</p>
<div class="table-wrap"><table>
<thead><tr><th>Concepto</th><th>Importe</th></tr></thead>
<tbody>
<tr><td>Deuda principal</td><td>1.000,00 €</td></tr>
<tr><td>Intereses: 1.000 × 10,40 % × 30 / 365</td><td>8,55 €</td></tr>
<tr><td>Costes de cobro (art. 8.1)</td><td>40,00 €</td></tr>
<tr><td>Total reclamable</td><td>1.048,55 €</td></tr>
</tbody></table></div>
<p>Observa que los 40 euros pesan mucho más que los intereses en deudas pequeñas. Calcula tu caso con la <a href="/intereses-demora-comerciales/">calculadora de intereses de demora</a> (usa el tipo del semestre en que venció la factura).</p>

<h2 id="pasos">Cómo reclamarlos</h2>
<ol class="steps">
<li><strong>Comprueba el vencimiento</strong> con los <a href="/blog/plazos-pago-ley-morosidad/">plazos de la Ley de morosidad</a>.</li>
<li><strong>Calcula intereses y 40 euros</strong> y deja constancia de ambos conceptos por separado.</li>
<li><strong>Reclama por escrito</strong> siguiendo <a href="/blog/reclamar-factura-impagada-intereses/">cómo reclamar una factura impagada</a>.</li>
<li><strong>Guarda los justificantes</strong> de cualquier otro coste de cobro para pedir la diferencia.</li>
</ol>
""",
    faq=[
        ("¿Cuánto es la indemnización por costes de cobro?", "Una cantidad fija de 40 euros (art. 8.1 de la Ley 3/2004)."),
        ("¿Hay que pedirla expresamente?", "No: se añade en todo caso y sin necesidad de petición expresa a la deuda principal."),
        ("¿Se suma a los intereses de demora?", "Sí, son conceptos distintos: intereses del art. 7 e indemnización del art. 8."),
        ("¿Puedo reclamar más de 40 euros?", "Sí, los costes de cobro debidamente acreditados que superen esa cantidad."),
        ("¿Cuándo no se debe?", "Cuando el deudor no es responsable del retraso (art. 8.2)."),
        ("¿Se cobran 40 euros por cada cuota de un pago a plazos?", "La ley no lo precisa; solo establece que se calculan sobre las cantidades vencidas. Consulta a un profesional."),
    ],
    sources=[S.LEY3],
))


# ---------------------------------------------------------------- Phase 2: calendario conjunto 2027-2029
POSTS.append(dict(
    slug="calendario-verifactu-factura-electronica-2027-2029",
    published="2026-11-26",
    title="Calendario 2027-2029: Verifactu y factura electrónica",
    desc="Calendario conjunto tras el RDL 43/2026: factura electrónica B2B desde el 6/10/2027, Verifactu y resto de empresas el 6/10/2028, y estados de factura en 2029.",
    h1="Calendario 2027-2029: Verifactu y factura electrónica entre empresas",
    intro="Con el aplazamiento de Verifactu publicado en el BOE el 25 de noviembre de 2026, las dos obligaciones convergen. Este calendario las junta, con la norma de cada fecha.",
    content="""
<p class="note"><strong>Respuesta corta:</strong> la factura electrónica entre empresas empieza el 6 de octubre de 2027 para quien superó 8 millones de euros de volumen de operaciones y el 6 de octubre de 2028 para el resto. Verifactu, tras el Real Decreto-ley 43/2026, debe estar adaptado para el último de esos plazos: el 6 de octubre de 2028.</p>
<p>Resumen de normas publicadas en el BOE. No sustituye el asesoramiento profesional.</p>

<h2 id="tabla">Calendario conjunto</h2>
<div class="table-wrap"><table>
<thead><tr><th>Fecha</th><th>Qué ocurre</th><th>Norma</th></tr></thead>
<tbody>
<tr><td>6 de octubre de 2027</td><td>Factura electrónica B2B obligatoria para empresarios y profesionales que superaron 8 M€ de volumen de operaciones el año anterior</td><td>RD 238/2026, DF 4.ª.1.a</td></tr>
<tr><td>6 de octubre de 2028</td><td>Factura electrónica B2B para el resto, y fecha límite de adaptación de los sistemas de facturación a Verifactu</td><td>RD 238/2026, DF 4.ª.1.b; RD 1007/2023, DF 4.ª (RDL 43/2026)</td></tr>
<tr><td>6 de octubre de 2029</td><td>Obligación de informar de los estados de la factura para personas físicas y entidades en atribución de rentas de hasta 8 M€ (hasta entonces, voluntaria)</td><td>RD 238/2026, DT 3.ª</td></tr>
</tbody></table></div>

<h2 id="verifactu">Qué ha cambiado en Verifactu</h2>
<p>Antes, el RD 1007/2023 fijaba el 1 de enero de 2027 para sociedades y el 1 de julio de 2027 para el resto. El Real Decreto-ley 43/2026, de 24 de noviembre, lo sustituye por una remisión: los obligados del artículo 3.1 deben tener adaptados sus sistemas cuando transcurra el plazo de la letra b) del apartado 1 de la disposición final cuarta del RD 238/2026. Detalle en <a href="/blog/fechas-verifactu-2027-2028/">fechas de Verifactu</a>.</p>

<h2 id="b2b">Qué no cambia en la factura electrónica</h2>
<p>El RDL 43/2026 no modifica los plazos del RD 238/2026. Si tu empresa superó los 8 millones de euros, tu primera fecha sigue siendo el 6 de octubre de 2027, aunque Verifactu llegue después. Compruébalo con el <a href="/factura-electronica-obligatoria/">comprobador de factura electrónica B2B</a>.</p>

<h2 id="diferencia">Dos obligaciones distintas</h2>
<p>Verifactu trata de cómo tu programa registra las facturas (registros, huella y QR). La factura electrónica B2B trata del formato estructurado y del envío al cliente. Una misma factura puede estar afectada por las dos; la explicamos en <a href="/blog/diferencias-verifactu-factura-electronica-b2b/">diferencias entre Verifactu y la factura electrónica B2B</a>.</p>

<h2 id="plan">Plan práctico</h2>
<ol class="steps">
<li><strong>Averigua tu tramo:</strong> más o menos de 8 M€ de volumen de operaciones del año natural anterior.</li>
<li><strong>Anota las dos fechas</strong> que te afectan y la más cercana.</li>
<li><strong>Pide a tu proveedor</strong> su plan de adaptación a ambas obligaciones.</li>
<li><strong>Vigila los pagos:</strong> la factura electrónica B2B trae también <a href="/blog/plazos-pago-ley-morosidad/">plazos de pago de la Ley de morosidad</a> que conviene dominar.</li>
</ol>
""",
    faq=[
        ("¿Cuándo es obligatoria la factura electrónica entre empresas?", "El 6 de octubre de 2027 para quien superó 8 M€ de volumen de operaciones el año anterior y el 6 de octubre de 2028 para el resto (RD 238/2026)."),
        ("¿Cuándo es obligatorio Verifactu?", "Los sistemas deben estar adaptados antes del 6 de octubre de 2028 tras el RDL 43/2026."),
        ("¿El aplazamiento afecta a la factura electrónica B2B?", "No: el RDL 43/2026 modifica el RD 1007/2023 (Verifactu), no los plazos del RD 238/2026."),
        ("¿Qué pasa en 2029?", "Para autónomos y entidades en atribución de rentas de hasta 8 M€ pasa a ser obligatorio informar de los estados de la factura (DT 3.ª del RD 238/2026)."),
        ("¿Y los fabricantes de software?", "Deben ofrecer sistemas adaptados en el plazo máximo de nueve meses desde la entrada en vigor de la orden ministerial de la DF 3.ª del RD 1007/2023."),
    ],
    sources=[S.RD, S.RDL43, S.AEAT_CAL],
))


# ---------------------------------------------------------------- Phase 2: aceptacion y factura resumen
POSTS.append(dict(
    slug="plazo-pago-aceptacion-factura-resumen",
    published="2026-11-27",
    title="Plazo de pago: aceptación de la mercancía y factura resumen",
    desc="Cómo cuenta el plazo de pago de 30 o 60 días cuando hay aceptación de la mercancía o facturas agrupadas, según el art. 4 de la Ley 3/2004, con ejemplos.",
    h1="Plazo de pago con aceptación de la mercancía y factura resumen",
    intro="El plazo de pago de la Ley 3/2004 no siempre empieza el día de la factura. Cuando hay un procedimiento de aceptación o agrupas facturas, la fecha de inicio cambia. Esto dice el texto consolidado del BOE.",
    content="""
<p class="note"><strong>Respuesta corta:</strong> sin fecha pactada, el plazo es de 30 días naturales desde la recepción de la mercancía o la prestación del servicio, aunque la factura llegara antes. Si hay aceptación o verificación, esos 30 días cuentan desde que esta se produce. El máximo pactado es de 60 días naturales.</p>
<p>Esta guía resume el artículo 4 de la Ley 3/2004, de 29 de diciembre, en su texto consolidado. No es asesoramiento jurídico.</p>

<h2 id="regla">La regla general del artículo 4.1</h2>
<p>Si el contrato no fija fecha o plazo de pago, el plazo será de <strong>treinta días naturales después de la fecha de recepción de las mercancías o prestación de los servicios</strong>, incluso cuando se hubiera recibido la factura con anterioridad. Es decir: mandar la factura pronto no adelanta el vencimiento.</p>
<p>La ley añade una obligación para el proveedor: debe hacer llegar la factura o solicitud de pago equivalente antes de que se cumplan quince días naturales desde la recepción efectiva de las mercancías o de la prestación.</p>
<p>Cuando el contrato sí fija un plazo, la recepción de la factura por medios electrónicos produce el inicio del cómputo, siempre que esté garantizada la identidad y autenticidad del firmante, la integridad de la factura y su recepción por el interesado. Por eso conviene conservar el justificante de entrega de la factura electrónica.</p>

<h2 id="aceptacion">Cuando hay aceptación o verificación (art. 4.2)</h2>
<p>Algunos contratos prevén un procedimiento mediante el cual se verifica que los bienes o servicios son conformes con lo pactado. La ley pone dos límites:</p>
<ul>
<li>ese procedimiento <strong>no puede durar más de treinta días naturales</strong> desde la recepción de los bienes o la prestación del servicio;</li>
<li>el plazo de pago es de <strong>treinta días después de la fecha en que tiene lugar la aceptación o verificación</strong>, aunque la factura se hubiera recibido antes.</li>
</ul>
<p>La consecuencia es que un cliente no puede alargar el pago con un proceso de revisión indefinido: la verificación tiene tope de 30 días, y el pago llega 30 días después de ella.</p>

<h2 id="ampliacion">Ampliar el plazo por pacto (art. 4.3)</h2>
<p>Las partes pueden ampliar los plazos anteriores, pero <strong>nunca por encima de 60 días naturales</strong>. Una cláusula que fije un plazo superior puede ser abusiva; lo vemos en <a href="/blog/clausulas-abusivas-plazo-pago-morosidad/">cláusulas abusivas de plazo de pago</a>.</p>

<h2 id="resumen">Factura resumen y agrupación periódica (art. 4.4)</h2>
<p>La ley permite agrupar facturas a lo largo de un período determinado <strong>no superior a quince días</strong>, mediante una factura resumen periódica o agrupándolas en un único documento para facilitar la gestión del pago. Con estas condiciones:</p>
<ul>
<li>la fecha de inicio del cómputo es la correspondiente <strong>a la mitad del período</strong> de la factura resumen o de la agrupación;</li>
<li>el plazo de pago no puede superar los sesenta días naturales desde esa fecha.</li>
</ul>

<h2 id="ejemplos">Ejemplos de cómputo</h2>
<p>Las fechas son ilustrativas; el cálculo se basa solo en las reglas anteriores y en días naturales.</p>
<div class="table-wrap"><table>
<thead><tr><th>Situación</th><th>Fecha de inicio</th><th>Plazo</th></tr></thead>
<tbody>
<tr><td>Sin plazo pactado. Entrega el 4 de mayo, factura el 2 de mayo</td><td>4 de mayo (recepción)</td><td>30 días: vence el 3 de junio</td></tr>
<tr><td>Con aceptación. Entrega el 4 de mayo, aceptación el 20 de mayo</td><td>20 de mayo</td><td>30 días: vence el 19 de junio</td></tr>
<tr><td>Factura resumen de las entregas del 1 al 15 de mayo, pago a 60 días</td><td>mitad del período</td><td>hasta 60 días desde esa fecha</td></tr>
</tbody></table></div>
<p>Si el pago llega después del vencimiento, la mora se devenga automáticamente (art. 5): sin aviso de vencimiento ni intimación del acreedor. Calcula el importe con la <a href="/intereses-demora-comerciales/">calculadora de intereses de demora</a>.</p>

<h2 id="pasos">Cómo aplicarlo a tu negocio</h2>
<ol class="steps">
<li><strong>Anota la fecha de recepción</strong> de la mercancía o del servicio, no solo la de la factura.</li>
<li><strong>Si hay aceptación,</strong> registra por escrito cuándo se produjo y comprueba que no excedió 30 días.</li>
<li><strong>Envía la factura</strong> dentro de los quince días siguientes a la recepción.</li>
<li><strong>Revisa el plazo</strong> con la guía de <a href="/blog/plazos-pago-ley-morosidad/">plazos de la Ley de morosidad</a> y, si vence sin pago, sigue <a href="/blog/reclamar-factura-impagada-intereses/">cómo reclamar una factura impagada</a>.</li>
</ol>
<p>Para vigilar tu comportamiento global de pago, usa también la <a href="/periodo-medio-pago-proveedores/">calculadora del periodo medio de pago</a>.</p>
""",
    faq=[
        ("¿Desde cuándo cuenta el plazo si no hay nada pactado?", "Treinta días naturales desde la recepción de las mercancías o la prestación del servicio, aunque la factura llegara antes (art. 4.1)."),
        ("¿Cuánto puede durar el procedimiento de aceptación?", "No más de treinta días naturales desde la recepción de los bienes o servicios (art. 4.2)."),
        ("¿Cuál es el plazo máximo que se puede pactar?", "60 días naturales (art. 4.3)."),
        ("¿Cuándo debe el proveedor enviar la factura?", "Antes de que se cumplan quince días naturales desde la recepción efectiva de las mercancías o del servicio."),
        ("¿Cómo cuenta una factura resumen?", "Desde la mitad del período agrupado, que no puede superar quince días, y con un plazo máximo de sesenta días desde esa fecha (art. 4.4)."),
        ("¿Hace falta avisar al deudor para que haya mora?", "No: la mora se produce automáticamente por el mero incumplimiento del plazo (art. 5)."),
    ],
    sources=[S.LEY3],
))
