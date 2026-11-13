# -*- coding: utf-8 -*-
import sources as S
from common import e

LABELS = {
    "alta": [("IDEmisorFactura", "NIF del emisor", "89890001K"), ("NumSerieFactura", "Serie y número", "12345678/G33"), ("FechaExpedicionFactura", "Fecha de expedición (DD-MM-AAAA)", "01-01-2024"),
             ("TipoFactura", "Tipo de factura (F1, F2, R1…)", "F1"), ("CuotaTotal", "Cuota total", "12.35"), ("ImporteTotal", "Importe total", "123.45"),
             ("Huella", "Huella del registro anterior (vacía si es el primero)", ""), ("FechaHoraHusoGenRegistro", "Fecha, hora y huso de generación", "2024-01-01T19:20:30+01:00")],
    "anulacion": [("IDEmisorFacturaAnulada", "NIF del emisor de la factura anulada", "89890001K"), ("NumSerieFacturaAnulada", "Serie y número anulados", "12345679/G34"),
                  ("FechaExpedicionFacturaAnulada", "Fecha de expedición (DD-MM-AAAA)", "01-01-2024"), ("Huella", "Huella del registro anterior", ""),
                  ("FechaHoraHusoGenRegistro", "Fecha, hora y huso de generación", "2024-01-01T19:20:40+01:00")],
    "evento": [("NIF", "NIF del productor del sistema (SistemaInformatico/NIF)", "89890001K"), ("ID", "ID (IDOtro/ID), solo si no hay NIF", ""),
               ("IdSistemaInformatico", "IdSistemaInformatico", "77"), ("Version", "Versión del sistema", "1.0.03"), ("NumeroInstalacion", "Número de instalación", "383"),
               ("NIF", "NIF del obligado a emitir (ObligadoEmision/NIF)", "89890001K"), ("TipoEvento", "Tipo de evento (01–10, 90)", "01"),
               ("HuellaEvento", "Huella del evento anterior (vacía si es el primero)", ""), ("FechaHoraHusoGenEvento", "Fecha, hora y huso del evento", "2024-01-01T19:20:30+01:00")],
}


def form(tipo, hidden):
    fields = ""
    for i, (name, label, ph) in enumerate(LABELS[tipo]):
        wide = "Huella" in name or "FechaHora" in name
        fields += '<div class="field%s"><label for="h-%s-%d">%s <code>%s</code></label><input id="h-%s-%d" type="text" class="mono" spellcheck="false" autocomplete="off" placeholder="%s"></div>' % (
            "" if not wide else "", tipo, i, e(label), name, tipo, i, e(ph))
    nm = {"alta": "alta", "anulacion": "anulación", "evento": "evento"}[tipo]
    return ('<div class="panel" id="p-%s" role="tabpanel" aria-labelledby="t-%s"%s><form id="h-form-%s" novalidate><div class="grid2">%s</div>'
            '<div class="btns"><button class="btn" type="submit">Calcular huella de %s</button><button class="btn ghost small" type="button" id="h-now-%s">Fecha y hora actual (Madrid)</button></div></form></div>') % (
        tipo, tipo, " hidden" if hidden else "", tipo, fields, nm, tipo)


HUE_TOOL = """
<section class="tool" aria-labelledby="h-h">
<h2 id="h-h">Calculadora de huella Verifactu</h2>
<div class="btns"><span class="label self-c">Ejemplos oficiales AEAT:</span>
<button class="btn ghost small" type="button" id="h-ex1">1 · Alta (primer registro)</button>
<button class="btn ghost small" type="button" id="h-ex2">2 · Alta encadenada</button>
<button class="btn ghost small" type="button" id="h-ex3">3 · Anulación</button>
<button class="btn ghost small" type="button" id="h-ex-ev">Evento (ilustrativo)</button></div>
<div class="tabs" id="h-tabs" role="tablist" aria-label="Tipo de registro">
<button type="button" role="tab" id="t-alta" data-tab="alta" aria-controls="p-alta" aria-selected="true">Registro de alta</button>
<button type="button" role="tab" id="t-anulacion" data-tab="anulacion" aria-controls="p-anulacion" aria-selected="false" tabindex="-1">Registro de anulación</button>
<button type="button" role="tab" id="t-evento" data-tab="evento" aria-controls="p-evento" aria-selected="false" tabindex="-1">Registro de evento</button>
</div>
""" + form("alta", False) + form("anulacion", True) + form("evento", True) + """
<div id="h-out" class="status" role="status" aria-live="polite" tabindex="-1"></div>
</section>
<section class="tool" aria-labelledby="c-h">
<h2 id="c-h">Comprobar la cadena de registros (XML)</h2>
<form id="c-form" novalidate>
<div class="field"><label for="c-xml">XML con uno o varios registros (RegistroAlta, RegistroAnulacion, RegistroEvento)</label><textarea id="c-xml" class="mono" rows="8" spellcheck="false" placeholder="&lt;sf:RegistroAlta&gt;…&lt;/sf:RegistroAlta&gt;"></textarea></div>
<label class="file" id="c-drop" for="c-file"><strong>…o carga un archivo .xml</strong><br><span class="hint">Se lee en tu navegador</span><input id="c-file" type="file" accept=".xml,text/xml,application/xml"></label>
<div class="btns mt12"><button class="btn" type="submit">Comprobar huellas y encadenamiento</button><button class="btn ghost small" type="button" id="c-ex">Cargar ejemplo correcto</button><button class="btn ghost small" type="button" id="c-ex-bad">Ejemplo con un dato alterado</button></div>
</form>
<div id="c-res" class="status" role="status" aria-live="polite" tabindex="-1"></div>
</section>
"""

HUE_CONTENT = """
<h2 id="que-es">Qué es la huella de Verifactu</h2>
<p>Cada registro de facturación (alta o anulación) y cada registro de evento lleva una <strong>huella</strong> o «hash»: un resumen de 64 caracteres calculado con el algoritmo <strong>SHA-256</strong> sobre algunos campos del propio registro y sobre la huella del registro anterior. Así, los registros quedan encadenados: si alguien cambia un importe o borra una factura intermedia, las huellas siguientes dejan de cuadrar. Es la base de la «inalterabilidad» que exige el reglamento.</p>
<p>La AEAT recalcula la huella de los registros que recibe de un sistema VERI*FACTU. Si no coincide con la que envía el programa, el registro se marca como «Aceptado con errores». Por eso conviene probar el cálculo con los ejemplos oficiales antes de poner un programa en producción.</p>

<h2 id="campos">Campos y orden exacto de cada registro</h2>
<p>La cadena de entrada tiene la forma <code>campo1=valor1&amp;campo2=valor2&amp;…</code>, en este orden, codificada en UTF-8:</p>
<div class="table-wrap"><table>
<thead><tr><th>#</th><th>Alta</th><th>Anulación</th><th>Evento</th></tr></thead>
<tbody>
<tr><td>1</td><td>IDEmisorFactura</td><td>IDEmisorFacturaAnulada</td><td>NIF (productor del sistema)</td></tr>
<tr><td>2</td><td>NumSerieFactura</td><td>NumSerieFacturaAnulada</td><td>ID (IDOtro)</td></tr>
<tr><td>3</td><td>FechaExpedicionFactura</td><td>FechaExpedicionFacturaAnulada</td><td>IdSistemaInformatico</td></tr>
<tr><td>4</td><td>TipoFactura</td><td>Huella (anterior)</td><td>Version</td></tr>
<tr><td>5</td><td>CuotaTotal</td><td>FechaHoraHusoGenRegistro</td><td>NumeroInstalacion</td></tr>
<tr><td>6</td><td>ImporteTotal</td><td>—</td><td>NIF (obligado a emitir)</td></tr>
<tr><td>7</td><td>Huella (anterior)</td><td>—</td><td>TipoEvento</td></tr>
<tr><td>8</td><td>FechaHoraHusoGenRegistro</td><td>—</td><td>HuellaEvento (anterior)</td></tr>
<tr><td>9</td><td>—</td><td>—</td><td>FechaHoraHusoGenEvento</td></tr>
</tbody></table></div>
<h3>Reglas que más fallan</h3>
<ul>
<li><strong>Espacios:</strong> se eliminan los del principio y el final de cada valor, no los interiores (<code>12345678 / G33</code> se queda igual).</li>
<li><strong>Campos vacíos:</strong> se escribe el nombre y el signo igual, sin valor. En el primer registro: <code>…&amp;Huella=&amp;FechaHoraHusoGenRegistro=…</code>.</li>
<li><strong>Importes:</strong> la AEAT da por buenos uno o dos decimales (123.1 o 123.10). Lo seguro es usar en la huella exactamente el mismo texto que en el XML.</li>
<li><strong>Fecha y hora:</strong> con huso horario, por ejemplo <code>2024-01-01T19:20:30+01:00</code>. El botón «Fecha y hora actual» la genera con el huso de Madrid.</li>
<li><strong>Salida:</strong> hexadecimal en MAYÚSCULAS, 64 caracteres. Se guarda también en el primer registro, que además lleva <code>PrimerRegistro=S</code>.</li>
<li><strong>Dos cadenas separadas:</strong> los registros de facturación (altas y anulaciones) forman una cadena; los de evento, otra.</li>
</ul>

<h2 id="ejemplos">Ejemplos oficiales de la AEAT</h2>
<p>El documento de especificaciones de la huella (versión 0.1.2) incluye tres casos. Esta calculadora los reproduce exactamente; pulsa los botones de ejemplo para verlos:</p>
<div class="table-wrap"><table>
<thead><tr><th>Caso</th><th>Huella oficial</th></tr></thead>
<tbody>
<tr><td>1. Alta, primer registro (12345678/G33)</td><td class="mono">3C464DAF61ACB827C65FDA19F352A4E3BDC2C640E9E9FC4CC058073F38F12F60</td></tr>
<tr><td>2. Alta encadenada (12345679/G34)</td><td class="mono">F7B94CFD8924EDFF273501B01EE5153E4CE8F259766F88CF6ACB8935802A2B97</td></tr>
<tr><td>3. Anulación de 12345679/G34</td><td class="mono">177547C0D57AC74748561D054A9CEC14B4C4EA23D1BEFD6F2E69E3A388F90C68</td></tr>
</tbody></table></div>
<p>La AEAT no publica un ejemplo numérico de registro de evento. El botón «Evento (ilustrativo)» calcula uno con datos inventados siguiendo el orden de campos oficial; úsalo para comparar con tu implementación, no como referencia oficial.</p>

<h2 id="cadena">Cómo funciona el comprobador de cadena</h2>
<p>Pega o carga un XML con varios registros (por ejemplo, un envío <code>RegFactuSistemaFacturacion</code> o una exportación de tu programa). La herramienta busca todos los <code>RegistroAlta</code>, <code>RegistroAnulacion</code> y <code>RegistroEvento</code> sin importar el prefijo de espacio de nombres, recalcula la huella de cada uno y comprueba que cada registro apunte a la huella del anterior. Si un registro no cuadra, te dice cuál y por qué: huella distinta, cadena rota, falta el encadenamiento o la huella solo coincide escribiendo los importes con otro número de decimales.</p>
<p>El comprobador acepta cualquier XML que contenga registros, aunque falten otros elementos del esquema: solo necesita los campos que intervienen en la huella y el bloque de encadenamiento. Así puedes revisar también extractos o ficheros de exportación.</p>
<p class="note">Todo el cálculo se hace en tu navegador con una implementación de SHA-256 incluida en la web. No se envían datos a ningún servidor, así que puedes usarla con registros reales.</p>

<h2 id="paso-a-paso">Ejemplo paso a paso: tres registros encadenados</h2>
<ol class="steps">
<li><strong>Primer registro (alta).</strong> Pulsa «1 · Alta (primer registro)». Fíjate en que el campo de huella anterior está vacío y la cadena contiene <code>Huella=&amp;</code>. El resultado, <code>3C464DAF…</code>, es la huella que el programa guarda en ese registro.</li>
<li><strong>Segundo registro (alta).</strong> Pulsa «Usar como huella anterior del siguiente registro»: la huella pasa al campo correspondiente y se pone la hora actual. Cambia la serie y número y los importes de la nueva factura y vuelve a calcular. Con el botón «2 · Alta encadenada» verás el caso oficial, cuyo resultado es <code>F7B94CFD…</code>.</li>
<li><strong>Tercer registro (anulación).</strong> Se anula la segunda factura. La anulación usa sus propios campos (NIF, número y fecha de la factura anulada) y la huella del registro anterior de la cadena, que es la del segundo registro. El caso oficial da <code>177547C0…</code>.</li>
<li><strong>Comprueba la cadena.</strong> En el comprobador, «Cargar ejemplo correcto» monta estos tres registros en un XML y confirma que cada eslabón apunta al anterior. «Ejemplo con un dato alterado» cambia un céntimo de la cuota del primer registro: su huella deja de cuadrar y la herramienta lo señala.</li>
</ol>
<p>Este mismo procedimiento sirve para auditar una exportación de tu programa: si alguien modificó un registro después de emitirlo, el recálculo lo delata aunque se hayan regenerado las huellas posteriores, porque estas ya no coincidirán con las que la AEAT recibió o con las copias de seguridad.</p>

<h2 id="dev">Para desarrolladores</h2>
<p>El cálculo equivale a <code>SHA256(UTF8(cadena)).toHex().toUpperCase()</code>. Si tu implementación da otra huella, compara la cadena exacta que muestra la calculadora con la tuya: casi siempre el fallo está en el formato de la fecha y hora, en un espacio sobrante, en el número de decimales o en el orden de los campos. Para generar un registro completo con su huella, prueba el <a href="/ejemplo-xml-verifactu/">ejemplo XML de registro de alta</a>.</p>
"""

HUE_FAQ = [
    ("¿Qué algoritmo usa la huella de Verifactu?", "SHA-256, el único permitido por la AEAT (lista L12 del anexo de la orden). El resultado se expresa en hexadecimal, en mayúsculas, con 64 caracteres."),
    ("¿Qué huella anterior pongo en el primer registro?", "Ninguna: el campo se escribe vacío (Huella=) en la cadena y el registro lleva PrimerRegistro=S. Aun así, el primer registro debe incluir su propia huella."),
    ("¿Por qué mi huella no coincide con la de la AEAT?", "Las causas habituales son: fecha y hora sin huso horario o con otro formato, espacios al principio o al final, campos en otro orden, minúsculas en la salida o importes con un número de decimales distinto al del XML."),
    ("¿La anulación se encadena con las altas?", "Sí. Altas y anulaciones forman una única cadena de registros de facturación: la anulación lleva la huella del registro inmediatamente anterior, sea alta o anulación."),
    ("¿Los eventos van en la misma cadena?", "No. Los registros de evento, propios de los sistemas no VERI*FACTU, tienen su propia cadena con HuellaEvento y PrimerEvento."),
    ("¿Qué pasa si la huella enviada es incorrecta?", "Según la AEAT, si en una remisión VERI*FACTU la huella no coincide con su cálculo, el registro se marca como «Aceptado con errores»."),
]

HUE = dict(
    title="Calcular huella Verifactu (hash SHA-256) – alta, anulación y evento",
    desc="Calcula la huella SHA-256 de registros Verifactu de alta, anulación y evento con los ejemplos oficiales de la AEAT y comprueba la cadena de un XML.",
    app_name="Calculadora de huella Verifactu",
    h1="Calcular la huella (hash) de Verifactu y comprobar la cadena",
    intro="Calcula la huella SHA-256 de un registro de alta, anulación o evento, ve la cadena exacta que se resume y comprueba si los registros de un XML están bien encadenados.",
    trail=[("Inicio", "/"), ("Calcular huella Verifactu", "/calcular-huella-verifactu/")],
    tool=HUE_TOOL, content=HUE_CONTENT, faq=HUE_FAQ, scripts=["page-huella.js"],
    sources=[S.HASH, S.HASH_FAQ, S.ORDEN, S.XSD],
)

CLAVES = "".join('<option value="%s"%s>%s</option>' % (c, " selected" if c == "01" else "", c + (" – régimen general" if c == "01" else "")) for c in
                 ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "14", "15", "17", "18", "19", "20"])
CALIF = ('<option value="S1" selected>S1 – Sujeta y no exenta</option><option value="S2">S2 – Sujeta, inversión del sujeto pasivo</option>'
         '<option value="N1">N1 – No sujeta (art. 7, 14, otros)</option><option value="N2">N2 – No sujeta por reglas de localización</option>'
         '<option value="E1">E1 – Exenta art. 20</option><option value="E2">E2 – Exenta art. 21</option><option value="E3">E3 – Exenta art. 22</option>'
         '<option value="E4">E4 – Exenta art. 24</option><option value="E5">E5 – Exenta art. 25</option><option value="E6">E6 – Exenta (otros)</option>')
TIPOS = "".join('<option value="%s"%s>%s %%</option>' % (t, " selected" if t == "21" else "", t) for t in ["21", "10", "4", "0"])


def linea(i):
    return ('<div class="line-row"><p class="label mb8">Línea %d%s</p><div class="grid3">'
            '<div class="field"><label for="x-l%d-base">Base imponible (€)</label><input id="x-l%d-base" type="text" inputmode="decimal" placeholder="100,00"></div>'
            '<div class="field"><label for="x-l%d-cal">Calificación / exención</label><select id="x-l%d-cal">%s</select></div>'
            '<div class="field"><label for="x-l%d-tipo">Tipo de IVA</label><select id="x-l%d-tipo">%s</select></div>'
            '<div class="field"><label for="x-l%d-clave">Clave de régimen</label><select id="x-l%d-clave">%s</select></div>'
            '</div></div>') % (i, "" if i == 1 else " (opcional)", i, i, i, i, CALIF, i, i, TIPOS, i, i, CLAVES)


def fld(id_, label, ph="", extra="", name=""):
    return '<div class="field"><label for="%s">%s</label><input id="%s" type="text" autocomplete="off" spellcheck="false" placeholder="%s"%s%s></div>' % (
        id_, label, id_, e(ph), (' data-name="%s"' % e(name)) if name else "", extra)


XML_TOOL = """
<section class="tool" aria-labelledby="x-h">
<h2 id="x-h">Generador de registro de alta</h2>
<form id="x-form" novalidate>
<div class="btns"><button class="btn ghost small" type="button" id="x-ex">Rellenar con un ejemplo</button></div>
<h3>Factura</h3>
<div class="grid2">""" + fld("x-enif", "NIF del emisor", "B12345674", ' class="mono"') + fld("x-enom", "Nombre o razón social del emisor", "Mi Empresa SL") + \
    fld("x-ns", "Serie y número", "2026-A-0001", ' class="mono"') + """<div class="field"><label for="x-fecha">Fecha de expedición</label><input id="x-fecha" type="date"></div>
<div class="field"><label for="x-tipo">Tipo de factura</label><select id="x-tipo"><option value="F1" selected>F1 – Factura completa</option><option value="F2">F2 – Factura simplificada (tique)</option></select></div>
""" + fld("x-desc", "Descripción de la operación", "Venta de mercaderías") + fld("x-dnif", "NIF del destinatario (obligatorio en F1)", "A12345674", ' class="mono"') + fld("x-dnom", "Nombre del destinatario", "Cliente SA") + """</div>
<h3>Desglose (IVA)</h3>""" + linea(1) + linea(2) + """
<h3>Encadenamiento</h3>
<fieldset><legend>¿Es el primer registro de este sistema?</legend><div class="radios">
<label><input type="radio" name="enc" value="primero" checked> Sí, primer registro (PrimerRegistro = S)</label>
<label><input type="radio" name="enc" value="anterior"> No, hay un registro anterior</label></div></fieldset>
<div id="x-anterior" class="grid2" hidden>""" + fld("x-a-nif", "NIF del emisor del registro anterior", "", ' class="mono"') + fld("x-a-ns", "Serie y número del registro anterior", "", ' class="mono"') + \
    fld("x-a-fecha", "Fecha de expedición anterior (DD-MM-AAAA)", "01-11-2026", ' class="mono"') + fld("x-a-huella", "Huella del registro anterior", "64 caracteres hexadecimales", ' class="mono"') + """</div>
<h3>Sistema informático (software)</h3>
<div class="grid3">""" + fld("x-s-nom", "Productor (nombre)", "Software SL", "", "productor") + fld("x-s-nif", "NIF del productor", "B12345674", ' class="mono"') + \
    fld("x-s-name", "Nombre del sistema", "MiFacturador", "", "nombre del sistema") + fld("x-s-id", "IdSistemaInformatico (2 car.)", "01", ' maxlength="4"', "IdSistemaInformatico") + \
    fld("x-s-ver", "Versión", "1.0", "", "versión") + fld("x-s-inst", "Número de instalación", "0001", "", "número de instalación") + """</div>
<div class="field"><label for="x-ts">Fecha, hora y huso de generación del registro</label><input id="x-ts" type="text" class="mono" spellcheck="false" autocomplete="off"><button class="btn ghost small mt8" type="button" id="x-now">Ahora (hora de Madrid)</button></div>
<div class="btns"><button class="btn" type="submit">Generar XML</button></div>
</form>
<div id="x-hres" class="status" role="status" aria-live="polite" tabindex="-1"></div>
<div class="field mt12"><label for="x-in">XML (puedes editarlo o pegar el tuyo)</label><textarea id="x-in" class="mono" rows="14" spellcheck="false"></textarea></div>
<div class="btns"><button class="btn" type="button" id="x-check">Comprobar estructura</button><button class="btn ghost" type="button" data-copy="x-in">Copiar XML</button><button class="btn ghost" type="button" id="x-dl" disabled>Descargar .xml</button></div>
<div id="x-res" class="status" role="status" aria-live="polite" tabindex="-1"></div>
</section>
"""

XML_CONTENT = """
<h2 id="estructura">Estructura de un registro de alta Verifactu</h2>
<p>Un programa VERI*FACTU envía a la AEAT un mensaje <code>RegFactuSistemaFacturacion</code> (esquema <code>SuministroLR.xsd</code>) con una <code>Cabecera</code> y hasta 1.000 <code>RegistroFactura</code>. Cada uno contiene un <code>RegistroAlta</code> o un <code>RegistroAnulacion</code>, definidos en <code>SuministroInformacion.xsd</code>. Los elementos del alta van en este orden (los opcionales menos habituales se omiten):</p>
<div class="table-wrap"><table>
<thead><tr><th>Elemento</th><th>Contenido</th><th>¿Obligatorio?</th></tr></thead>
<tbody>
<tr><td><code>IDVersion</code></td><td>Siempre 1.0</td><td>Sí</td></tr>
<tr><td><code>IDFactura</code></td><td>IDEmisorFactura (NIF), NumSerieFactura (máx. 60), FechaExpedicionFactura (DD-MM-AAAA)</td><td>Sí</td></tr>
<tr><td><code>NombreRazonEmisor</code></td><td>Nombre del emisor (máx. 120)</td><td>Sí</td></tr>
<tr><td><code>TipoFactura</code></td><td>F1, F2, F3, R1–R5</td><td>Sí</td></tr>
<tr><td><code>DescripcionOperacion</code></td><td>Texto libre (máx. 500)</td><td>Sí</td></tr>
<tr><td><code>Destinatarios</code></td><td>IDDestinatario con NombreRazon y NIF (o IDOtro)</td><td>Según el tipo</td></tr>
<tr><td><code>Desglose</code></td><td>1 a 12 DetalleDesglose: impuesto, clave de régimen, calificación o exención, tipo, base y cuota</td><td>Sí</td></tr>
<tr><td><code>CuotaTotal</code> / <code>ImporteTotal</code></td><td>Importes con punto decimal (máx. 12 enteros y 2 decimales)</td><td>Sí</td></tr>
<tr><td><code>Encadenamiento</code></td><td>PrimerRegistro = S o RegistroAnterior (NIF, número, fecha y huella)</td><td>Sí</td></tr>
<tr><td><code>SistemaInformatico</code></td><td>Productor, nombre, IdSistemaInformatico, versión, nº de instalación e indicadores de uso</td><td>Sí</td></tr>
<tr><td><code>FechaHoraHusoGenRegistro</code></td><td>Fecha y hora con huso horario</td><td>Sí</td></tr>
<tr><td><code>TipoHuella</code> / <code>Huella</code></td><td>01 (SHA-256) y la huella del registro</td><td>Sí</td></tr>
</tbody></table></div>
<p>Los elementos de la cabecera y del cuerpo pertenecen a dos espacios de nombres distintos (<code>SuministroLR.xsd</code> y <code>SuministroInformacion.xsd</code>), que el generador declara con los prefijos <code>sfLR</code> y <code>sf</code>. En el envío real todo ello va dentro de un sobre SOAP y se transmite con certificado electrónico.</p>

<h2 id="que-revisa">Qué revisa la comprobación estructural</h2>
<ul>
<li>Que el XML esté bien formado y que el elemento raíz y los espacios de nombres sean los oficiales.</li>
<li>Que estén todos los elementos obligatorios del <code>RegistroAlta</code> y en el orden del esquema.</li>
<li>Formatos: NIF de 9 caracteres (y su carácter de control), fecha DD-MM-AAAA, importes 12.2, TipoFactura, CalificacionOperacion u OperacionExenta (excluyentes), máximo 12 líneas de desglose.</li>
<li>Coherencia: CuotaTotal frente a la suma de cuotas e ImporteTotal frente a bases más cuotas (como aviso, porque puede haber suplidos u otros conceptos).</li>
<li>Encadenamiento: PrimerRegistro o RegistroAnterior completo, nunca ambos.</li>
<li><strong>Huella:</strong> la recalcula y te dice si coincide con la del registro.</li>
</ul>
<p class="note">No es una validación contra el XSD completo ni contra todas las reglas de negocio del documento de validaciones y errores de la AEAT, y no sustituye las pruebas en el entorno de pruebas de la AEAT. Sí detecta en segundos los errores más habituales al montar el XML a mano. Nosotros verificamos los XML que produce este generador contra los esquemas oficiales de la AEAT en nuestras pruebas automáticas.</p>

<h2 id="como-usar">Cómo usar el generador</h2>
<ol class="steps">
<li><strong>Rellena la factura:</strong> NIF y nombre del emisor, serie y número, fecha, tipo (F1 o F2), descripción y, en F1, el destinatario. Con «Rellenar con un ejemplo» verás un caso completo.</li>
<li><strong>Añade el desglose:</strong> para cada línea, la base imponible, la calificación (S1 sujeta y no exenta, S2 con inversión del sujeto pasivo, N1/N2 no sujeta o E1–E6 exenta), el tipo de IVA y la clave de régimen (01 es el régimen general). La cuota, CuotaTotal e ImporteTotal se calculan solos.</li>
<li><strong>Indica el encadenamiento:</strong> si es el primer registro del sistema, se marca PrimerRegistro = S; si no, introduce los datos y la huella del registro anterior (puedes calcularla con la <a href="/calcular-huella-verifactu/">calculadora de huella</a>).</li>
<li><strong>Completa el sistema informático:</strong> productor, nombre del programa, identificador de dos caracteres, versión y número de instalación.</li>
<li><strong>Genera y revisa:</strong> el XML aparece en el cuadro editable y se comprueba automáticamente. Puedes modificarlo, pegar el tuyo y volver a pulsar «Comprobar estructura».</li>
</ol>

<h2 id="errores">Errores habituales al montar el XML a mano</h2>
<ul>
<li>Elementos en otro orden del que marca el esquema (por ejemplo, TipoFactura después de DescripcionOperacion).</li>
<li>Fechas en formato AAAA-MM-DD en <code>FechaExpedicionFactura</code>, que exige DD-MM-AAAA.</li>
<li><code>FechaHoraHusoGenRegistro</code> sin huso horario, o distinta de la usada para calcular la huella.</li>
<li>Importes con coma decimal o con más de dos decimales.</li>
<li>Indicar a la vez <code>PrimerRegistro</code> y <code>RegistroAnterior</code>, o ninguno de los dos.</li>
<li>Usar <code>CalificacionOperacion</code> y <code>OperacionExenta</code> en la misma línea de desglose: son excluyentes.</li>
</ul>

<h2 id="tipos">Tipos de factura y claves más usados</h2>
<div class="table-wrap"><table>
<thead><tr><th>Código</th><th>Significado (según el esquema de la AEAT)</th></tr></thead>
<tbody>
<tr><td>F1</td><td>Factura (art. 6, 7.2 y 7.3 del RD 1619/2012)</td></tr>
<tr><td>F2</td><td>Factura simplificada y facturas sin identificación del destinatario (art. 6.1.d)</td></tr>
<tr><td>F3</td><td>Factura emitida en sustitución de facturas simplificadas facturadas y declaradas</td></tr>
<tr><td>R1–R4</td><td>Facturas rectificativas (art. 80.1 y 80.2 y error fundado en derecho; art. 80.3; art. 80.4; resto)</td></tr>
<tr><td>R5</td><td>Factura rectificativa en facturas simplificadas</td></tr>
<tr><td>S1 / S2</td><td>Operación sujeta y no exenta, sin / con inversión del sujeto pasivo</td></tr>
<tr><td>N1 / N2</td><td>Operación no sujeta (art. 7, 14, otros) / por reglas de localización</td></tr>
<tr><td>E1–E6</td><td>Operación exenta por los arts. 20, 21, 22, 24, 25 de la Ley del IVA u otros</td></tr>
</tbody></table></div>
<p>Las claves de régimen (01 a 20) se definen en el anexo de la Orden HAC/1177/2024; la 01 corresponde a la operación de régimen general, la más habitual.</p>
<p>El generador solo crea facturas F1 y F2 con IVA, que cubren la mayoría de casos. Las rectificativas necesitan además <code>TipoRectificativa</code> y las facturas rectificadas, y la comprobación te avisará si faltan.</p>

<h2 id="pasos">Siguientes pasos</h2>
<p>Comprueba la huella de varios registros encadenados con la <a href="/calcular-huella-verifactu/">calculadora de huella y comprobador de cadena</a> y genera el QR de la misma factura con el <a href="/generador-qr-verifactu/">generador de QR tributario</a>. Los esquemas XSD y el documento de validaciones y errores están en el portal de desarrolladores de la AEAT.</p>
"""

XML_FAQ = [
    ("¿Dónde descargo los XSD oficiales de Verifactu?", "En el portal de desarrolladores de la AEAT, apartado «Esquemas de los servicios web»: SuministroLR.xsd, SuministroInformacion.xsd, EventosSIF.xsd, ConsultaLR.xsd y las respuestas. Algunos enlaces de la AEAT piden certificado electrónico."),
    ("¿Este XML se puede enviar tal cual a la AEAT?", "No. Es un ejemplo de estructura. El envío real va dentro de un sobre SOAP, se hace con certificado electrónico desde tu sistema de facturación y, en la modalidad no VERI*FACTU, los registros además se firman."),
    ("¿Qué elemento raíz tiene el envío de registros?", "RegFactuSistemaFacturacion, del esquema SuministroLR.xsd, con una Cabecera (ObligadoEmision) y entre 1 y 1.000 RegistroFactura."),
    ("¿Es obligatorio el destinatario?", "En una factura completa (F1) hay que identificar al destinatario. En una factura simplificada (F2) puede omitirse."),
    ("¿Cómo se escriben los importes en el XML?", "Con punto decimal y como máximo 12 cifras enteras y 2 decimales, por ejemplo 1210.00. Pueden llevar signo negativo en rectificativas."),
    ("¿Qué formato tiene FechaHoraHusoGenRegistro?", "Fecha y hora ISO 8601 con huso horario, por ejemplo 2026-11-13T10:15:00+01:00. Interviene en la huella, así que debe coincidir exactamente con la usada en el cálculo."),
]

XMLP = dict(
    title="Ejemplo XML Verifactu: genera y revisa un registro de alta",
    desc="Genera un XML de ejemplo de registro de alta Verifactu (RegFactuSistemaFacturacion) con su huella y revisa estructura, formatos, totales y encadenamiento.",
    app_name="Generador de XML de ejemplo Verifactu",
    h1="Ejemplo XML Verifactu: generador de registro de alta",
    intro="Rellena los datos de una factura y obtén un RegistroAlta con la estructura de los esquemas oficiales y su huella calculada. Pega también tu propio XML para revisarlo.",
    trail=[("Inicio", "/"), ("Ejemplo XML Verifactu", "/ejemplo-xml-verifactu/")],
    tool=XML_TOOL, content=XML_CONTENT, faq=XML_FAQ, scripts=["page-xml.js"],
    sources=[S.XSD, S.HASH, S.ORDEN, S.AEAT],
)
