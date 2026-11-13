# -*- coding: utf-8 -*-
import sources as S

GEN_TOOL = """
<section class="tool" aria-labelledby="q-h">
<h2 id="q-h">Datos de la factura</h2>
<form id="q-form" novalidate>
<div class="grid2">
 <div class="field"><label for="q-nif">NIF del emisor</label><input id="q-nif" type="text" class="mono" autocomplete="off" spellcheck="false" maxlength="15" placeholder="B12345674"><p class="hint">9 caracteres: DNI, NIE o NIF de la empresa.</p></div>
 <div class="field"><label for="q-ns">Serie y número de factura</label><input id="q-ns" type="text" class="mono" autocomplete="off" spellcheck="false" maxlength="80" placeholder="2026-A-0001"><p class="hint">Máximo 60 caracteres, sin tildes ni ñ.</p></div>
 <div class="field"><label for="q-fecha">Fecha de expedición</label><input id="q-fecha" type="date"></div>
 <div class="field"><label for="q-imp">Importe total (€)</label><input id="q-imp" type="text" inputmode="decimal" autocomplete="off" placeholder="1.210,00"><p class="hint">Puedes escribir 1.210,00; en el QR irá 1210.00.</p></div>
</div>
<fieldset><legend>Modalidad del programa de facturación</legend><div class="radios">
 <label><input type="radio" name="modo" value="verifactu" checked> VERI*FACTU (envía los registros a la AEAT)</label>
 <label><input type="radio" name="modo" value="no"> No VERI*FACTU</label>
</div></fieldset>
<fieldset><legend>Entorno</legend><div class="radios">
 <label><input type="radio" name="entorno" value="produccion" checked> Producción (facturas reales)</label>
 <label><input type="radio" name="entorno" value="pruebas"> Pruebas (prewww2.aeat.es)</label>
</div></fieldset>
<h3>Formato de impresión</h3>
<div class="grid3">
 <div class="field"><label for="q-size">Tamaño del QR (mm)</label><select id="q-size"><option value="30">30 × 30 mm (mínimo)</option><option value="35" selected>35 × 35 mm</option><option value="40">40 × 40 mm (máximo)</option></select></div>
 <div class="field"><label for="q-margin">Margen en blanco (mm)</label><select id="q-margin"><option value="2">2 mm (mínimo)</option><option value="4" selected>4 mm</option><option value="6">6 mm (recomendado)</option></select></div>
 <div class="field"><label for="q-pt">Tamaño de letra (pt)</label><select id="q-pt"><option value="7">7 pt</option><option value="8">8 pt</option><option value="9" selected>9 pt</option><option value="10">10 pt</option><option value="11">11 pt</option><option value="12">12 pt</option></select><p class="hint">Igual o mayor que el resto de datos de la factura.</p></div>
</div>
<div class="grid2">
 <fieldset><legend>Leyenda bajo el QR (solo VERI*FACTU)</legend><div class="radios">
  <label><input type="radio" name="leyenda" value="corta" checked> «VERI*FACTU»</label>
  <label><input type="radio" name="leyenda" value="larga"> «Factura verificable en la sede electrónica de la AEAT»</label>
 </div></fieldset>
 <div class="field"><label for="q-paper">Vista previa sobre</label><select id="q-paper"><option value="a4" selected>DIN A4 vertical (210 mm)</option><option value="t80">Tique de 80 mm</option><option value="t57">Tique de 57 mm</option></select></div>
</div>
<div class="btns"><button class="btn" type="submit">Generar QR tributario</button><button class="btn ghost" type="button" id="q-ex">Ejemplo oficial de la AEAT</button></div>
</form>
<div id="q-res" class="status" role="status" aria-live="polite" tabindex="-1"></div>
<div class="qr-layout">
 <div>
  <p class="label">Vista previa de impresión</p>
  <div class="paper-wrap"><div id="q-preview" class="paper"></div></div>
  <label class="check mt8"><input type="checkbox" id="q-real"> Mostrar a tamaño real (en pantalla, aproximado)</label>
  <p class="mm-note">La regla superior marca cada 5 mm. La AEAT pide el QR al principio de la factura, arriba y preferiblemente centrado; en DIN A4 puedes poner los datos del emisor y del destinatario a los lados.</p>
 </div>
 <div>
  <p class="label">URL codificada en el QR</p>
  <p id="q-url" class="out placeholder">La URL aparecerá aquí.</p>
  <div class="btns mt8">
   <button class="btn small ghost" type="button" id="q-copy" data-copy="q-url" disabled>Copiar URL</button>
   <button class="btn small" type="button" id="q-svg" disabled>Descargar SVG (tamaño real)</button>
   <button class="btn small" type="button" id="q-png" disabled>Descargar PNG 600 ppp</button>
   <button class="btn small ghost" type="button" id="q-print" disabled>Imprimir a tamaño real</button>
  </div>
  <p class="hint">El SVG lleva las medidas en milímetros: al insertarlo en tu plantilla conserva el tamaño exacto. El PNG está a 600 ppp; si tu programa no lee la resolución, ajústalo al ancho indicado arriba.</p>
 </div>
</div>
</section>
"""

GEN_CONTENT = """
<h2 id="como">Cómo crear el QR de una factura Verifactu</h2>
<ol class="steps">
<li><strong>Escribe los cuatro datos</strong> que exige la AEAT: NIF del emisor, serie y número, fecha de expedición e importe total. Son los mismos que figuran en la factura.</li>
<li><strong>Elige la modalidad.</strong> Si tu programa envía los registros a la AEAT (VERI*FACTU), la URL usa la ruta <code>ValidarQR</code> y debajo del QR va la leyenda. Si no, la ruta es <code>ValidarQRNoVerifactu</code> y no lleva leyenda.</li>
<li><strong>Ajusta tamaño, margen y letra</strong> y mira la vista previa sobre un A4 o un tique. La herramienta te avisa si el bloque no cabe en el papel o si el margen es justo.</li>
<li><strong>Descarga el SVG o el PNG</strong>, o imprímelo directamente a tamaño real para comprobarlo con una regla y la cámara del móvil.</li>
</ol>
<p class="note">Importante: generar el QR no registra la factura en la AEAT. En la modalidad VERI*FACTU es tu programa de facturación el que envía el registro; si no lo ha enviado, al escanear el QR la AEAT responderá «No encontrada». Este generador sirve para pruebas, para revisar el diseño y para entender el formato.</p>

<h2 id="url">Formato de la URL del QR tributario</h2>
<p>El código QR contiene una dirección web del servicio de cotejo de la AEAT con exactamente cuatro parámetros obligatorios. Estos son los cuatro formatos posibles, según el documento técnico de la AEAT (versión 0.5.0):</p>
<div class="table-wrap"><table>
<thead><tr><th>Sistema</th><th>Entorno</th><th>URL base</th></tr></thead>
<tbody>
<tr><td>VERI*FACTU</td><td>Producción</td><td><code>https://www2.agenciatributaria.gob.es/wlpl/TIKE-CONT/ValidarQR</code></td></tr>
<tr><td>VERI*FACTU</td><td>Pruebas</td><td><code>https://prewww2.aeat.es/wlpl/TIKE-CONT/ValidarQR</code></td></tr>
<tr><td>No VERI*FACTU</td><td>Producción</td><td><code>https://www2.agenciatributaria.gob.es/wlpl/TIKE-CONT/ValidarQRNoVerifactu</code></td></tr>
<tr><td>No VERI*FACTU</td><td>Pruebas</td><td><code>https://prewww2.aeat.es/wlpl/TIKE-CONT/ValidarQRNoVerifactu</code></td></tr>
</tbody></table></div>
<div class="table-wrap"><table>
<thead><tr><th>Parámetro</th><th>Contenido</th><th>Formato</th></tr></thead>
<tbody>
<tr><td><code>nif</code></td><td>NIF del obligado a expedir la factura</td><td>9 caracteres</td></tr>
<tr><td><code>numserie</code></td><td>Serie + número de la factura</td><td>Máx. 60 caracteres ASCII imprimibles (32–126)</td></tr>
<tr><td><code>fecha</code></td><td>Fecha de expedición</td><td>DD-MM-AAAA, con guiones</td></tr>
<tr><td><code>importe</code></td><td>Importe total de la factura</td><td>Punto decimal; máx. 12 enteros y 2 decimales</td></tr>
</tbody></table></div>
<p>Los valores se codifican con «URL encoding» en UTF-8. El caso típico es un número de serie con «&amp;»: <code>12345678&amp;G33</code> debe ir como <code>12345678%26G33</code>; si no, la URL se parte y la AEAT no encuentra la factura. El generador lo hace automáticamente y convierte el importe al formato con punto (1.210,00 → <code>1210.00</code>). El parámetro opcional <code>formato=json</code> nunca puede ir en el QR impreso.</p>
<p>Ejemplo oficial (producción, VERI*FACTU): <code>https://www2.agenciatributaria.gob.es/wlpl/TIKE-CONT/ValidarQR?nif=89890001K&amp;numserie=12345678-G33&amp;fecha=01-09-2024&amp;importe=241.4</code></p>

<h2 id="medidas">Medidas, margen y posición en la factura</h2>
<p>La Orden HAC/1177/2024 (art. 21) fija un tamaño de <strong>entre 30 × 30 y 40 × 40 mm</strong>, la norma ISO/IEC 18004 y el <strong>nivel M</strong> de corrección de errores. El documento técnico de la AEAT añade los detalles de presentación:</p>
<ul>
<li><strong>Margen en blanco</strong> de al menos 2 mm por los cuatro lados; se recomiendan 6 mm. Contraste alto entre el código y el fondo.</li>
<li><strong>Posición:</strong> al principio de la factura, antes del contenido, y como primer QR si hay otros. En formato vertical, arriba, preferiblemente centrado (o arriba a la izquierda); en apaisado, a la izquierda. En facturas de varias páginas, solo en la primera.</li>
<li><strong>Texto «QR tributario:»</strong> siempre encima del código, preferiblemente centrado.</li>
<li><strong>Leyenda «VERI*FACTU»</strong> o «Factura verificable en la sede electrónica de la AEAT» justo debajo, solo en la modalidad VERI*FACTU. Puede ocupar varias líneas.</li>
<li>Ambos textos con una letra <strong>igual o mayor</strong> que la del resto de datos de la factura.</li>
</ul>
<p>Con una URL normal el QR resultante tiene unos 45–50 módulos por lado, así que en 30 mm cada módulo mide unos 0,6 mm: se lee bien con cualquier móvil si la impresora no emborrona. En tiques térmicos de 57 mm, un QR de 40 mm con 2 mm de margen cabe holgado; la herramienta te avisa si te pasas de ancho. Más detalles y ejemplos en la guía <a href="/blog/tamano-posicion-qr-verifactu/">Tamaño y posición del QR Verifactu</a>.</p>

<h2 id="descargas">SVG, PNG o impresión directa: qué formato usar</h2>
<p><strong>SVG</strong> es la mejor opción si tu plantilla de factura o tu programa de maquetación lo admite: es vectorial, no pierde calidad al imprimir y lleva las medidas reales en milímetros, incluidos el texto «QR tributario:» y la leyenda. <strong>PNG a 600 ppp</strong> sirve para procesadores de texto y programas que solo aceptan imágenes; al insertarlo, fija el ancho que indica la herramienta para que el QR mida lo que has elegido. <strong>Imprimir a tamaño real</strong> abre el diálogo de impresión solo con el bloque del QR: imprímelo al 100 %, sin «ajustar a la página», y mide el código con una regla.</p>

<h2 id="errores">Errores frecuentes al colocar el QR</h2>
<ul>
<li>La plantilla reduce la imagen para que quepa en una celda y el QR queda por debajo de 30 mm.</li>
<li>El QR va en el pie o en la última página, en lugar de al principio.</li>
<li>Falta «QR tributario:» encima, o la leyenda «VERI*FACTU» aparece en un programa que no envía los registros.</li>
<li>La URL apunta al entorno de pruebas o el importe usa coma decimal.</li>
</ul>

<h2 id="comprobar">Cómo comprobar el QR una vez impreso</h2>
<p>Imprime la factura o el bloque descargado, mide el código con una regla y escanéalo con la cámara del móvil. Después pega la URL en nuestro <a href="/validar-qr-verifactu/">validador de QR Verifactu</a>: revisa el dominio, la ruta, los cuatro parámetros y sus formatos y te da el enlace al cotejo oficial. Si el QR apunta al entorno de pruebas, la AEAT no reconocerá facturas reales.</p>
"""

GEN_FAQ = [
    ("¿Qué tamaño debe tener el QR de Verifactu?", "Entre 30 × 30 y 40 × 40 milímetros, con nivel M de corrección de errores y al menos 2 mm de margen en blanco alrededor (la AEAT recomienda 6 mm)."),
    ("¿Dónde se coloca el QR en la factura?", "Al principio de la factura, antes de su contenido. En formato vertical, arriba y preferiblemente centrado; en apaisado, a la izquierda. Encima debe ir el texto «QR tributario:» y, en VERI*FACTU, debajo la leyenda «VERI*FACTU»."),
    ("¿Generar el QR aquí registra mi factura en la AEAT?", "No. El QR solo contiene una URL. Quien registra la factura es tu programa de facturación cuando envía el registro a la AEAT (modalidad VERI*FACTU). Este generador sirve para probar el formato y el diseño de impresión."),
    ("¿Qué diferencia hay entre ValidarQR y ValidarQRNoVerifactu?", "ValidarQR es la ruta para facturas de sistemas VERI*FACTU, que la AEAT puede encontrar. ValidarQRNoVerifactu es para sistemas que no envían los registros; al escanearlo, la AEAT responde «No contrastable» y guarda la información que remite el receptor."),
    ("¿Cómo escribo el importe en el QR?", "Con punto como separador decimal y sin separador de miles: 1210.00 o 1210.5. Una coma (1210,50) provoca el error 2005 de la AEAT. Aquí puedes escribirlo como en España y se convierte solo."),
    ("¿Puedo usar «VERI*FACTU» si mi programa no envía los registros?", "No. La leyenda solo corresponde a facturas expedidas por sistemas que emiten facturas verificables (modalidad VERI*FACTU). Un sistema no VERI*FACTU lleva el QR y el texto «QR tributario:», pero no la leyenda."),
    ("¿El QR tiene que ser en blanco y negro?", "La AEAT exige contraste suficientemente alto entre el código y el fondo. Negro sobre blanco es la opción segura; evita fondos de color o tramas detrás del código."),
]

GEN = dict(
    title="Generador QR Verifactu gratis – QR tributario para imprimir",
    desc="Crea el QR tributario de tu factura (nivel M, 30–40 mm) con «QR tributario:» y leyenda VERI*FACTU. Vista previa en mm y descarga SVG o PNG.",
    app_name="Generador de QR tributario Verifactu",
    h1="Generador de QR Verifactu con vista previa de impresión",
    intro="Crea el código QR tributario de una factura con el formato oficial de la AEAT y comprueba cómo queda impreso, en milímetros, sobre un A4 o un tique.",
    trail=[("Inicio", "/"), ("Generador de QR Verifactu", "/generador-qr-verifactu/")],
    tool=GEN_TOOL, content=GEN_CONTENT, faq=GEN_FAQ, scripts=["qr.js", "page-qrgen.js"],
    sources=[S.QR, S.ORDEN, S.ROF, S.AEAT],
)

VAL_TOOL = """
<section class="tool" aria-labelledby="v-h">
<h2 id="v-h">Comprueba un QR tributario</h2>
<form id="v-form" novalidate>
<div class="field"><label for="v-url">URL del código QR</label><textarea id="v-url" class="mono" rows="3" spellcheck="false" autocomplete="off" placeholder="https://www2.agenciatributaria.gob.es/wlpl/TIKE-CONT/ValidarQR?nif=…&amp;numserie=…&amp;fecha=…&amp;importe=…"></textarea>
<p class="hint">Escanea el QR con el móvil y pega aquí el enlace, o usa la foto o la cámara de abajo.</p></div>
<div class="btns"><button class="btn" type="submit">Validar URL</button>
<button class="btn ghost small" type="button" id="v-ex-ok">Ejemplo correcto</button>
<button class="btn ghost small" type="button" id="v-ex-amp">Ejemplo con errores</button>
<button class="btn ghost small" type="button" id="v-ex-bad">Ejemplo de phishing</button></div>
</form>
<div class="grid2">
 <label class="file" id="v-drop" for="v-file"><strong>Sube una foto o captura del QR</strong><br><span class="hint">JPG, PNG o WebP · también puedes pegarla con <span class="kbd">Ctrl</span>+<span class="kbd">V</span></span><input id="v-file" type="file" accept="image/*"></label>
 <div class="cam"><button class="btn" type="button" id="v-cam">Escanear con la cámara</button><button class="btn ghost" type="button" id="v-cam-stop" hidden>Detener cámara</button><video id="v-video" playsinline muted hidden aria-label="Vista de la cámara"></video><p class="hint">La imagen se analiza en tu dispositivo; no se sube a ningún servidor.</p></div>
</div>
<div id="v-res" class="status" role="status" aria-live="polite" tabindex="-1"></div>
</section>
"""

VAL_CONTENT = """
<h2 id="que-comprueba">Qué comprueba el validador</h2>
<p>El validador lee la URL del QR y la contrasta con el documento técnico de la AEAT sobre el código QR (versión 0.5.0). No necesita conexión con la AEAT: todo se revisa en tu navegador y solo al final te ofrece el enlace para hacer el cotejo oficial en la sede electrónica.</p>
<div class="table-wrap"><table>
<thead><tr><th>Comprobación</th><th>Qué debe cumplir</th><th>Error AEAT</th></tr></thead>
<tbody>
<tr><td>Dominio</td><td><code>www2.agenciatributaria.gob.es</code> (producción) o <code>prewww2.aeat.es</code> (pruebas), con https</td><td>—</td></tr>
<tr><td>Ruta</td><td><code>/wlpl/TIKE-CONT/ValidarQR</code> o <code>…/ValidarQRNoVerifactu</code></td><td>—</td></tr>
<tr><td>Parámetros presentes</td><td>nif, numserie, fecha e importe</td><td>1001–1004</td></tr>
<tr><td>NIF</td><td>9 caracteres y carácter de control correcto (DNI, NIE o NIF de entidad)</td><td>2001</td></tr>
<tr><td>Serie y número</td><td>Máximo 60 caracteres, solo ASCII 32–126</td><td>2002, 2003</td></tr>
<tr><td>Fecha</td><td>DD-MM-AAAA y fecha existente</td><td>2004</td></tr>
<tr><td>Importe</td><td>Punto decimal, máximo 12 enteros y 2 decimales</td><td>2005, 2006</td></tr>
<tr><td>Codificación</td><td>Sin «&amp;» sin codificar ni parámetros extra; nunca <code>formato=json</code></td><td>—</td></tr>
</tbody></table></div>

<h2 id="leer">Leer el QR desde una foto o con la cámara</h2>
<p>Si tienes la factura en papel, pulsa «Escanear con la cámara» y enfoca el código. Si la tienes en PDF, haz una captura de pantalla del QR y súbela o pégala con Ctrl+V. El lector usa el detector de códigos de tu navegador cuando existe y, si no, una librería de lectura de QR incluida en esta web; la imagen no sale de tu dispositivo. Funciona mejor con el código recortado, bien iluminado y sin reflejos.</p>

<h2 id="paso-a-paso">Paso a paso: comprobar una factura que has recibido</h2>
<ol class="steps">
<li><strong>Localiza el QR tributario.</strong> Debe estar al principio de la factura, con el texto «QR tributario:» encima. Si la factura tiene varios QR, el tributario es el primero.</li>
<li><strong>Léelo sin abrirlo.</strong> Usa la cámara desde esta página o sube una foto: así ves la dirección completa antes de visitarla. Si lo escaneas con la cámara del móvil, copia el enlace en lugar de abrirlo directamente.</li>
<li><strong>Revisa el resultado.</strong> El dominio debe ser el de la AEAT y los datos (NIF, número, fecha e importe) deben coincidir con los impresos en la factura. Una diferencia en el importe o en la fecha suele indicar un error del programa del emisor.</li>
<li><strong>Coteja en la sede de la AEAT.</strong> Si todo está bien, pulsa el botón de cotejo. La respuesta de la AEAT es la única que confirma si la factura consta.</li>
<li><strong>Si algo no cuadra,</strong> pide al emisor que lo revise. Si el dominio no es de la AEAT, no introduzcas datos en esa web.</li>
</ol>

<h2 id="problemas">Si el QR no se lee</h2>
<ul>
<li><strong>Foto borrosa o con reflejos:</strong> acércate hasta que el código ocupe buena parte de la imagen, evita el flash sobre papel brillante y prueba con luz natural.</li>
<li><strong>QR demasiado pequeño:</strong> si mide menos de 30 mm o la impresora térmica está gastada, los módulos se funden. Es un defecto de la factura; la norma exige entre 30 y 40 mm.</li>
<li><strong>Factura en PDF:</strong> amplía el PDF al 200 % antes de hacer la captura para que el lector tenga más píxeles por módulo.</li>
<li><strong>Logotipo encima del código o fondo de color:</strong> el nivel M solo corrige alrededor del 15 % de daños; tapar el centro o reducir el contraste puede impedir la lectura.</li>
<li><strong>Cámara bloqueada:</strong> el navegador pedirá permiso la primera vez. Si lo denegaste, actívalo en los ajustes del sitio o usa la opción de subir una foto.</li>
</ul>

<h2 id="phishing">Cuidado con los QR falsos</h2>
<p>Un QR tributario siempre lleva a un dominio de la Agencia Tributaria. Si al escanear una factura aparece otra dirección, aunque se parezca (por ejemplo, con «agenciatributaria» dentro de un dominio distinto), no la abras ni introduzcas datos: puede ser un intento de fraude. El validador marca como error cualquier dominio que no sea uno de los dos oficiales y avisa si imita el nombre de la AEAT.</p>

<h2 id="resultado">Qué significa la respuesta de la AEAT</h2>
<p>Cuando abres el enlace oficial, el servicio de cotejo puede responder:</p>
<ul>
<li><strong>Encontrada (00):</strong> la factura de un sistema VERI*FACTU consta en la AEAT con esos datos.</li>
<li><strong>No encontrada (01):</strong> no consta, o se anuló. Puede ser que el programa aún no la haya enviado o que algún dato no coincida.</li>
<li><strong>No contrastable (02):</strong> el QR es de un sistema no VERI*FACTU; la AEAT no puede comprobarla en ese momento.</li>
</ul>
<p>Ten en cuenta que «No encontrada» no significa por sí sola que la factura sea falsa: si el emisor usa la modalidad VERI*FACTU, puede haber un pequeño retraso entre la emisión y el envío, y si tiene un problema técnico el registro puede llegar más tarde. Si persiste días después, pregunta al emisor.</p>
<p>Si la AEAT devuelve un código de error, el número coincide con los de la tabla anterior: 2005, por ejemplo, suele ser un importe con coma. La AEAT también limita el número de consultas al día (error 3002).</p>

<h2 id="emisor">Si eres el emisor de la factura</h2>
<p>Valida tus propios QR antes de enviar facturas a clientes, sobre todo al cambiar de programa, de plantilla o de serie de numeración: un número de serie con «&amp;» sin codificar, un importe con coma o un QR apuntando al entorno de pruebas son errores frecuentes que tu cliente detectará al escanearlo. Para crear un QR correcto y ver su tamaño impreso usa el <a href="/generador-qr-verifactu/">generador de QR tributario</a>.</p>
"""

VAL_FAQ = [
    ("¿Cómo sé si el QR de una factura es auténtico?", "Comprueba que la URL empieza por https://www2.agenciatributaria.gob.es/wlpl/TIKE-CONT/ (o prewww2.aeat.es si es de pruebas) y que los datos del QR coinciden con los de la factura. Después ábrela: la AEAT te dirá si la factura consta."),
    ("¿Este validador consulta la AEAT?", "No. Revisa el formato en tu navegador y no envía nada. Para el cotejo oficial te ofrece el enlace a la sede electrónica, que abres tú."),
    ("¿Puedo leer el QR de un PDF?", "Haz una captura de pantalla del código QR y súbela o pégala con Ctrl+V. También puedes escanear la pantalla con la cámara de otro dispositivo."),
    ("¿Por qué la AEAT dice «No encontrada»?", "Porque el registro no consta: el programa aún no lo ha enviado, la factura se anuló o algún dato del QR (NIF, número, fecha o importe) no coincide con el registro enviado."),
    ("¿Qué significa el error 2005?", "Que el importe tiene un formato incorrecto, normalmente porque usa coma decimal (7,2) en lugar de punto (7.2)."),
    ("¿Qué pasa si el número de serie tiene el símbolo &?", "Debe codificarse como %26 en la URL. Si no, el navegador interpreta lo que va detrás como un parámetro nuevo y la AEAT recibe un número de serie incompleto."),
]

VAL = dict(
    title="Validar QR Verifactu – lector y comprobador gratis",
    desc="Comprueba el QR tributario de una factura: pega la URL, sube una foto o usa la cámara. Revisa dominio AEAT, NIF, fecha, importe y errores 1001–2006.",
    app_name="Validador y lector de QR Verifactu",
    h1="Validar QR Verifactu: lee y comprueba el QR de una factura",
    intro="Pega la URL, sube una foto o escanea con la cámara. Te decimos si el QR tributario cumple el formato oficial y si apunta de verdad a la AEAT.",
    trail=[("Inicio", "/"), ("Validar QR Verifactu", "/validar-qr-verifactu/")],
    tool=VAL_TOOL, content=VAL_CONTENT, faq=VAL_FAQ, scripts=["page-qrval.js"],
    sources=[S.QR, S.ORDEN, S.AEAT],
)
