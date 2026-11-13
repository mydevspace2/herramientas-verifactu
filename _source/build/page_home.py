# -*- coding: utf-8 -*-
import sources as S

ESTADO = """
<section class="tool" aria-labelledby="estado-h">
<h2 id="estado-h">¿Desde cuándo es obligatorio Verifactu? Estado a 13 de noviembre de 2026</h2>
<div class="dates">
 <div class="date-card"><span class="tag">En el BOE · vigente</span><span class="big">1 de enero de 2027</span><small>Sociedades (Impuesto sobre Sociedades): sistemas adaptados <strong>antes</strong> de esta fecha · <span id="cd-is">fecha vigente</span></small></div>
 <div class="date-card"><span class="tag">En el BOE · vigente</span><span class="big">1 de julio de 2027</span><small>Autónomos y resto de obligados: <strong>antes</strong> de esta fecha · <span id="cd-resto">fecha vigente</span></small></div>
 <div class="date-card pending"><span class="tag pending">Solo anunciado · sin BOE</span><span class="big">Octubre de 2028</span><small>Hacienda anunció el 05/10/2026 su intención de aplazar todas las obligaciones pendientes. Sin día concreto y sin norma publicada.</small></div>
</div>
<p class="checked"><strong>Última comprobación: 13 de noviembre de 2026.</strong> El texto consolidado del <a href="https://www.boe.es/buscar/act.php?id=BOE-A-2023-24840" rel="noopener" target="_blank">RD 1007/2023 en el BOE</a> sigue con las fechas de 2027 (última actualización publicada el 03/12/2025). El aplazamiento a 2028 consta en la <a href="https://www.hacienda.gob.es/sgt/gabsehacienda/nota-informativa-verifactu.pdf" rel="noopener" target="_blank">nota de Hacienda del 05/10/2026</a> y la <a href="https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu.html" rel="noopener" target="_blank">AEAT</a> lo presenta como «previsión». Actualizaremos esta página el día que se publique la norma.</p>
</section>
"""

TOOL = ESTADO + """
<section class="tool" aria-labelledby="ob-h">
<h2 id="ob-h">Test: ¿estoy obligado a Verifactu?</h2>
<form id="ob-form" novalidate>
<fieldset><legend>1. ¿Dónde tienes tu domicilio fiscal?</legend><div class="radios">
<label><input type="radio" name="dom" value="comun" checked> Territorio común (resto de España, incluidas Canarias, Ceuta y Melilla)</label>
<label><input type="radio" name="dom" value="pv"> País Vasco</label>
<label><input type="radio" name="dom" value="navarra"> Navarra</label>
</div></fieldset>
<fieldset><legend>2. ¿Cómo tributas?</legend><div class="radios">
<label><input type="radio" name="tipo" value="sociedad"> Sociedad (S.L., S.A., cooperativa…) – Impuesto sobre Sociedades</label>
<label><input type="radio" name="tipo" value="autonomo"> Autónomo o profesional (IRPF, estimación directa u objetiva/módulos)</label>
<label><input type="radio" name="tipo" value="atribucion"> Comunidad de bienes, sociedad civil o herencia yacente con actividad</label>
<label><input type="radio" name="tipo" value="nr-ep"> No residente con establecimiento permanente en España</label>
<label><input type="radio" name="tipo" value="nr-sin-ep"> No residente sin establecimiento permanente</label>
<label><input type="radio" name="tipo" value="exenta"> Entidad totalmente exenta del IS (art. 9.1 LIS)</label>
<label><input type="radio" name="tipo" value="parcial"> Entidad parcialmente exenta (asociación, fundación… art. 9.2–9.4 LIS)</label>
<label><input type="radio" name="tipo" value="productor"> Produzco o vendo software de facturación</label>
</div></fieldset>
<fieldset><legend>3. ¿Llevas los libros registro de IVA por el SII (Suministro Inmediato de Información)?</legend><div class="radios">
<label><input type="radio" name="sii" value="no" checked> No</label>
<label><input type="radio" name="sii" value="si"> Sí</label>
</div></fieldset>
<fieldset><legend>4. ¿Cómo emites tus facturas o tiques?</legend><div class="radios">
<label><input type="radio" name="emi" value="programa"> Con un programa, app, TPV o caja registradora</label>
<label><input type="radio" name="emi" value="excel"> Con Excel, Word o similares</label>
<label><input type="radio" name="emi" value="tercero"> Las emite mi cliente o un tercero por mí</label>
<label><input type="radio" name="emi" value="mano"> Solo a mano (talonario de papel)</label>
<label><input type="radio" name="emi" value="no"> No emito facturas</label>
</div></fieldset>
<div class="btns"><button class="btn" type="submit">Ver mi resultado</button><button class="btn ghost" type="reset">Empezar de nuevo</button></div>
</form>
<div id="ob-out" class="status" role="status" aria-live="polite"></div>
<p class="hint">Basado en los arts. 1.3, 3, 4 y 6 y la disposición final 4.ª del RD 1007/2023. Las respuestas no salen de tu navegador.</p>
</section>
"""

CONTENT = """
<h2 id="que-es">Qué es Verifactu, en dos minutos</h2>
<p>«Verifactu» es el nombre con el que se conoce el <strong>Reglamento de sistemas informáticos de facturación</strong>, aprobado por el Real Decreto 1007/2023. Desarrolla la Ley 11/2021 antifraude y fija qué requisitos tiene que cumplir el programa con el que una empresa o un autónomo expide sus facturas: que no se puedan borrar ni alterar sin dejar rastro, que cada factura genere un <em>registro de facturación</em> encadenado con el anterior mediante una huella (hash SHA-256) y que la factura impresa lleve un <strong>código QR tributario</strong> con el que el cliente puede comprobarla en la web de la Agencia Tributaria.</p>
<p>El reglamento permite dos modalidades. En la modalidad <strong>VERI*FACTU</strong> el programa envía cada registro a la AEAT en el momento en que se emite la factura, y la factura lleva la leyenda «VERI*FACTU» o «Factura verificable en la sede electrónica de la AEAT». En la modalidad <strong>no VERI*FACTU</strong> los registros se guardan en el propio sistema, firmados electrónicamente y con un registro de eventos, y se entregan a Hacienda solo si los pide. En ambos casos el software tiene que estar adaptado.</p>

<h2 id="quien">¿Quién está obligado? (art. 3 del RD 1007/2023)</h2>
<p>Están obligados quienes <strong>usen un sistema informático para facturar</strong>, aunque solo sea para una parte de su actividad, y además sean:</p>
<div class="table-wrap"><table>
<thead><tr><th>Quién</th><th>¿Obligado?</th><th>Fecha vigente (BOE)</th></tr></thead>
<tbody>
<tr><td>Sociedades y demás contribuyentes del Impuesto sobre Sociedades</td><td>Sí</td><td>Antes del 1/1/2027</td></tr>
<tr><td>Autónomos y profesionales en IRPF (también en módulos)</td><td>Sí, si facturan con programa</td><td>Antes del 1/7/2027</td></tr>
<tr><td>Comunidades de bienes y entidades en atribución de rentas con actividad</td><td>Sí</td><td>Antes del 1/7/2027</td></tr>
<tr><td>No residentes con establecimiento permanente</td><td>Sí</td><td>Antes del 1/7/2027</td></tr>
<tr><td>Entidades parcialmente exentas del IS</td><td>Solo por las rentas sujetas y no exentas</td><td>Antes del 1/1/2027</td></tr>
<tr><td>Entidades totalmente exentas del IS (art. 9.1 LIS)</td><td>No</td><td>—</td></tr>
<tr><td>Quien lleva los libros de IVA por el SII</td><td>No (art. 3.3)</td><td>—</td></tr>
<tr><td>Domicilio fiscal en País Vasco o Navarra</td><td>No por el reglamento estatal (normativa foral, TicketBAI en el País Vasco)</td><td>—</td></tr>
<tr><td>Productores y vendedores de software de facturación</td><td>Sí (art. 3.2)</td><td>Desde el 29/7/2025</td></tr>
</tbody></table></div>
<p>El art. 4 excluye además algunas operaciones, como las facturas de establecimientos permanentes situados en el extranjero, y el art. 5 permite pedir a la AEAT que no se aplique el reglamento a sectores o contribuyentes concretos por razones justificadas. Son casos poco frecuentes: si crees que encajas, consúltalo con tu asesor.</p>

<h2 id="fechas">Fechas: lo que dice el BOE y lo que se ha anunciado</h2>
<p>La disposición final cuarta del RD 1007/2023, en la redacción que le dio el <strong>Real Decreto-ley 15/2025, de 2 de diciembre</strong>, establece que los contribuyentes del Impuesto sobre Sociedades deben tener sus sistemas adaptados <strong>antes del 1 de enero de 2027</strong> y el resto de obligados <strong>antes del 1 de julio de 2027</strong>. Es la norma vigente y es la que aparece en el texto consolidado del BOE.</p>
<p>El <strong>5 de octubre de 2026</strong> el Ministerio de Hacienda publicó una nota informativa en la que anuncia la «previsión» de aplazar las obligaciones pendientes <strong>hasta octubre de 2028</strong>, para hacerlas coincidir con la factura electrónica obligatoria de las empresas que facturan hasta 8 millones de euros. La nota no da un día concreto ni dice con qué norma se hará. Hasta que esa norma se publique en el BOE, una nota de prensa no cambia las fechas legales. Lo explicamos con detalle en <a href="/blog/fechas-verifactu-2027-2028/">Fechas de Verifactu: 2027 en el BOE y octubre de 2028 anunciado</a>.</p>
<p>¿Qué hacer mientras tanto? Lo prudente es no esperar a la última semana: pregunta a tu proveedor de software si su programa ya está adaptado y en qué modalidad, prueba el QR de tus facturas con nuestro <a href="/validar-qr-verifactu/">validador de QR</a> y, si emites pocas facturas, valora la <a href="/blog/verifactu-gratis-aplicacion-aeat/">aplicación gratuita de la AEAT</a>.</p>

<h2 id="modalidad">VERI*FACTU o no VERI*FACTU: ¿qué modalidad elegir?</h2>
<p>Las dos cumplen el reglamento. Con <strong>VERI*FACTU</strong> el programa remite cada registro a la AEAT al emitir la factura; a cambio, el reglamento simplifica otros requisitos (por ejemplo, no hace falta firmar los registros ni llevar el registro de eventos) y tus clientes pueden comprobar la factura con el QR. Con la modalidad <strong>no VERI*FACTU</strong> no se envía nada en el momento, pero el sistema debe firmar electrónicamente los registros, llevar un registro de eventos y conservarlo todo para entregarlo si la AEAT lo pide. Para un autónomo o una pyme, la modalidad VERI*FACTU suele ser la más sencilla; la aplicación gratuita de la AEAT trabaja así.</p>

<h2 id="excel">¿Y si facturo con Excel o Word?</h2>
<p>Según las preguntas frecuentes de la AEAT, el reglamento <strong>no te afecta</strong> si usas la hoja de cálculo o el procesador de textos solo para introducir los datos, expedir e imprimir las facturas y conservarlas. Sí te afecta si, por ejemplo, programas una macro que genera el libro registro de facturas expedidas: en ese caso la hoja de cálculo se considera un sistema informático de facturación y tiene que cumplir los requisitos.</p>

<h2 id="b2b">Además de Verifactu: factura electrónica B2B y morosidad</h2>
<p>Verifactu no es la única obligación que llega. El <strong>Real Decreto 238/2026</strong> hace obligatoria la factura electrónica entre empresas y profesionales desde el <strong>6 de octubre de 2027</strong> para quien supera 8 millones de euros de volumen de operaciones y desde el <strong>6 de octubre de 2028</strong> para el resto, y obliga a informar de cada pago en un máximo de cuatro días (excluidos sábados, domingos y festivos nacionales). Su objetivo es reducir la morosidad, así que también conviene controlar el periodo medio de pago y los intereses de demora:</p>
<div class="hub">
<a href="/factura-electronica-obligatoria/"><strong>Factura electrónica B2B: ¿cuándo me obliga?</strong><span>Test con las fechas del BOE y calculadora del plazo de 4 días para informar pagos y rechazos.</span></a>
<a href="/periodo-medio-pago-proveedores/"><strong>Periodo medio de pago a proveedores</strong><span>Método ICAC con CSV, ratios de pagadas y pendientes y cuadro listo para la memoria.</span></a>
<a href="/intereses-demora-comerciales/"><strong>Intereses de demora</strong><span>Tipos del BOE de cada semestre (10,40 % en el 2.º semestre de 2026) y 40 € por factura.</span></a>
</div>

<h2 id="que-cambia">Qué cambia en tus facturas</h2>
<ol class="steps">
<li><strong>Un QR tributario al principio de la factura</strong>, de 30 a 40 mm, con el texto «QR tributario:» encima. Puedes crearlo y ver cómo queda impreso con el <a href="/generador-qr-verifactu/">generador de QR</a>.</li>
<li><strong>La leyenda «VERI*FACTU»</strong> (o la frase larga) debajo del QR si tu programa trabaja en esa modalidad.</li>
<li><strong>Un registro de facturación</strong> por cada factura emitida o anulada, encadenado con el anterior mediante su <a href="/calcular-huella-verifactu/">huella SHA-256</a>.</li>
<li><strong>Un XML con formato oficial</strong> para cada registro. Si eres desarrollador, nuestro <a href="/ejemplo-xml-verifactu/">ejemplo XML</a> genera un registro de alta y revisa su estructura.</li>
</ol>
"""

FAQ = [
    ("¿Verifactu es obligatorio?", "Sí, para quien expide facturas con un programa informático y es sociedad, autónomo, entidad en atribución de rentas o no residente con establecimiento permanente, salvo excepciones como el SII o el domicilio fiscal en País Vasco o Navarra. Según el BOE, las sociedades deben estar adaptadas antes del 1 de enero de 2027 y el resto antes del 1 de julio de 2027."),
    ("¿Se ha aplazado Verifactu a 2028?", "Se ha anunciado, pero no está aprobado. El 5 de octubre de 2026 Hacienda comunicó su intención de aplazarlo hasta octubre de 2028. A 13 de noviembre de 2026 no hay ninguna norma publicada en el BOE que lo haga efectivo, así que siguen vigentes las fechas de 2027."),
    ("¿Los autónomos en módulos están obligados a Verifactu?", "Sí, si expiden facturas con un programa. El art. 3.1.b incluye a todos los contribuyentes del IRPF que desarrollan actividades económicas, sin distinguir el método de estimación."),
    ("Si estoy en el SII, ¿tengo que cumplir Verifactu?", "No. El art. 3.3 del RD 1007/2023 excluye a quienes llevan los libros registro de IVA a través de la sede electrónica de la AEAT (SII)."),
    ("¿Puedo seguir haciendo facturas a mano?", "Sí. Verifactu regula los sistemas informáticos de facturación. Si expides tus facturas solo a mano, en un talonario, no usas un sistema informático y el reglamento no te obliga. En cuanto uses un programa, aunque sea para una parte de tu actividad, sí."),
    ("¿Tengo que enviar mis facturas a Hacienda?", "Solo si eliges la modalidad VERI*FACTU: el programa envía automáticamente cada registro a la AEAT. En la modalidad no VERI*FACTU los registros se guardan firmados en tu sistema y se entregan solo si la AEAT los requiere."),
    ("¿Qué pasa si vivo en el País Vasco o en Navarra?", "El reglamento estatal solo se aplica en esos territorios a quien tiene su domicilio fiscal en territorio común. En el País Vasco rige TicketBAI y en Navarra su normativa foral."),
    ("¿Hay una forma gratuita de cumplir Verifactu?", "Sí. La AEAT ofrece una aplicación gratuita de facturación para quien emite pocas facturas o tiene una facturación sencilla. Emite facturas completas con el QR y envía los registros a la AEAT, pero no hace facturas simplificadas (tiques). Lo explicamos en la guía <a href=\"/blog/verifactu-gratis-aplicacion-aeat/\">Verifactu gratis</a>."),
]

HOME = dict(
    title="¿Verifactu es obligatorio? Test gratis y fechas 2027/2028",
    desc="Comprueba si Verifactu te obliga y desde cuándo: fechas del BOE (1/1/2027 y 1/7/2027) y aplazamiento a 2028 anunciado pero aún no publicado.",
    app_name="¿Estoy obligado a Verifactu? – test gratuito",
    h1="¿Verifactu es obligatorio para ti? Compruébalo en 1 minuto",
    intro="Responde cuatro preguntas y verás si te afecta el reglamento Verifactu y qué fecha te aplica: la vigente en el BOE y la anunciada por Hacienda.",
    trail=[("Inicio", "/")],
    tool=TOOL, content=CONTENT, faq=FAQ, scripts=["page-home.js"],
    sources=[S.RD, S.RDL, S.NOTA, S.AEAT, S.FAQ_AMB],
)
