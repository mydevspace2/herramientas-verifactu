# -*- coding: utf-8 -*-
"""Sección «factura electrónica B2B y morosidad»: PMP (ICAC), factura electrónica obligatoria B2B y plazo de 4 días,
intereses de demora (Ley 3/2004). Datos comprobados en el BOE el 13/11/2026."""
import sources as S
from common import e

CHECKED_ES = "13 de noviembre de 2026"

# Tipos legales de interés de demora (art. 7 Ley 3/2004) publicados en el BOE – igual que TIPOS en assets-src/b2b.js
TIPOS = [
    ("2026-2", "10,40", "BOE-A-2026-14327", "01/07/2026"), ("2026-1", "10,15", "BOE-A-2025-27201", "31/12/2025"),
    ("2025-2", "10,15", "BOE-A-2025-13217", "28/06/2025"), ("2025-1", "11,15", "BOE-A-2024-27618", "31/12/2024"),
    ("2024-2", "12,25", "BOE-A-2024-13089", "28/06/2024"), ("2024-1", "12,50", "BOE-A-2023-26709", "29/12/2023"),
    ("2023-2", "12,00", "BOE-A-2023-15221", "29/06/2023"), ("2023-1", "10,50", "BOE-A-2022-24416", "30/12/2022"),
    ("2022-2", "8,00", "BOE-A-2022-10844", "30/06/2022"), ("2022-1", "8,00", "BOE-A-2021-21959", "31/12/2021"),
    ("2021-2", "8,00", "BOE-A-2021-10869", "30/06/2021"), ("2021-1", "8,00", "BOE-A-2020-17415", "31/12/2020"),
    ("2020-2", "8,00", "BOE-A-2020-6848", "27/06/2020"), ("2020-1", "8,00", "BOE-A-2019-18736", "30/12/2019"),
    ("2019-2", "8,00", "BOE-A-2019-9730", "28/06/2019"), ("2019-1", "8,00", "BOE-A-2018-17661", "22/12/2018"),
    ("2018-2", "8,00", "BOE-A-2018-9001", "29/06/2018"), ("2018-1", "8,00", "BOE-A-2017-15428", "23/12/2017"),
    ("2017-2", "8,00", "BOE-A-2017-7469", "28/06/2017"), ("2017-1", "8,00", "BOE-A-2016-12482", "29/12/2016"),
    ("2016-2", "8,00", "BOE-A-2016-6299", "29/06/2016"), ("2016-1", "8,05", "BOE-A-2015-14331", "30/12/2015"),
    ("2015-2", "8,05", "BOE-A-2015-7292", "30/06/2015"), ("2015-1", "8,05", "BOE-A-2014-13716", "31/12/2014"),
    ("2014-2", "8,15", "BOE-A-2014-6914", "01/07/2014"), ("2014-1", "8,25", "BOE-A-2013-13835", "31/12/2013"),
    ("2013-2", "8,50", "BOE-A-2013-7090", "29/06/2013"),
]


def boe_link(i, text=None):
    return '<a href="https://www.boe.es/diario_boe/txt.php?id=%s" rel="noopener" target="_blank">%s</a>' % (i, text or i)


def tipos_table():
    rows = "".join('<tr><td>%s.º semestre de %s</td><td>%s %%</td><td>%s</td><td>%s</td></tr>' % (s.split("-")[1], s.split("-")[0], t, boe_link(b), p) for s, t, b, p in TIPOS)
    return ('<div class="table-wrap"><table class="rates-table"><thead><tr><th>Periodo</th><th>Tipo legal</th><th>Resolución en el BOE</th><th>Publicada</th></tr></thead>'
            '<tbody>%s</tbody></table></div>') % rows


# ======================================================================================
# 1. PMP – periodo medio de pago a proveedores (método ICAC)
# ======================================================================================
PMP_TOOL = """
<section class="tool" aria-labelledby="pmp-h">
<h2 id="pmp-h">Calculadora del periodo medio de pago (Resolución ICAC de 29/01/2016)</h2>
<div class="tabs" id="pmp-tabs" role="tablist" aria-label="Modelo de memoria">
<button type="button" role="tab" id="t-normal" data-tab="normal" aria-controls="p-normal" aria-selected="true">Memoria normal (factura a factura)</button>
<button type="button" role="tab" id="t-abrev" data-tab="abrev" aria-controls="p-abrev" aria-selected="false" tabindex="-1">Memoria abreviada o PGC Pymes</button>
</div>
<div class="panel" id="p-normal" role="tabpanel" aria-labelledby="t-normal">
<div class="grid3">
<div class="field"><label for="pmp-soc">Sociedad (opcional, para el informe)</label><input id="pmp-soc" type="text" autocomplete="organization" placeholder="Ejemplo, S.L."></div>
<div class="field"><label for="pmp-ap">Inicio del ejercicio</label><input id="pmp-ap" type="date" value="2025-01-01"></div>
<div class="field"><label for="pmp-cierre">Cierre del ejercicio</label><input id="pmp-cierre" type="date" value="2025-12-31"></div>
</div>
<div class="grid3">
<div class="field"><label for="pmp-lim">Plazo máximo legal para el recuento de facturas</label><select id="pmp-lim"><option value="60" selected>60 días (máximo pactable, art. 4.3 Ley 3/2004)</option><option value="30">30 días (plazo sin pacto, art. 4.1)</option></select></div>
<div class="field"><label for="pmp-n1">PMP del ejercicio anterior (N-1), opcional</label><input id="pmp-n1" type="text" inputmode="decimal" placeholder="p. ej. 41,25"></div>
<div class="field"><label for="pmp-csv">Cargar CSV o pegar desde Excel</label><label class="file" id="pmp-drop" for="pmp-csv"><strong>Elegir archivo .csv</strong><br><span class="hint">Se lee en tu navegador</span><input id="pmp-csv" type="file" accept=".csv,.txt,text/csv,text/plain"></label></div>
</div>
<div class="field"><label for="pmp-paste">…o pega aquí las filas copiadas de tu hoja de cálculo (factura; proveedor; importe; fecha inicio; fecha pago)</label><textarea id="pmp-paste" class="mono paste" rows="2" spellcheck="false" placeholder="A-1;Proveedor;1.000,00;10/01/2025;09/02/2025"></textarea></div>
<div class="btns"><button class="btn ghost small" type="button" id="pmp-paste-go">Añadir filas pegadas</button><button class="btn ghost small" type="button" id="pmp-tpl">Descargar plantilla CSV</button><button class="btn ghost small" type="button" id="pmp-ex">Cargar ejemplo</button><button class="btn ghost small" type="button" id="pmp-clear">Vaciar tabla</button></div>
<div class="table-wrap"><table class="rows-table" id="pmp-table"><thead><tr><th>#</th><th>Factura</th><th>Proveedor</th><th>Importe (€)</th><th>Inicio del cómputo</th><th>Fecha de pago <span class="muted">(vacía = pendiente)</span></th><th><span class="sr-only">Quitar</span></th></tr></thead><tbody id="pmp-rows"></tbody></table></div>
<div class="btns"><button class="btn ghost small" type="button" id="pmp-add">+ Añadir fila</button><button class="btn" type="button" id="pmp-go">Calcular PMP</button></div>
<p class="hint">Inicio del cómputo: fecha de recepción de las mercancías o de prestación de los servicios; si no la conoces con fiabilidad, la de recepción de la factura (art. 5.4). Importe: el de la operación (IVA incluido, como figura en la deuda con el proveedor).</p>
<div id="pmp-out" class="status" role="status" aria-live="polite" tabindex="-1"></div>
<div id="pmp-res"></div>
</div>
<div class="panel" id="p-abrev" role="tabpanel" aria-labelledby="t-abrev" hidden>
<form id="ab-form" novalidate>
<div class="grid3">
<div class="field"><label for="ab-ini">Saldo de acreedores comerciales al inicio (€)</label><input id="ab-ini" type="text" inputmode="decimal" placeholder="40.000,00"></div>
<div class="field"><label for="ab-fin">Saldo de acreedores comerciales al cierre (€)</label><input id="ab-fin" type="text" inputmode="decimal" placeholder="60.000,00"></div>
<div class="field"><label for="ab-com">Compras netas y gastos por servicios exteriores (€)</label><input id="ab-com" type="text" inputmode="decimal" placeholder="400.000,00"></div>
</div>
<div class="btns"><button class="btn" type="submit">Calcular PMP (modelo abreviado)</button><button class="btn ghost small" type="button" id="ab-ex">Cargar ejemplo</button></div>
</form>
<div id="ab-out" class="status" role="status" aria-live="polite" tabindex="-1"></div>
<p class="hint">Art. 5.5: PMP = saldo medio de acreedores comerciales ÷ (compras netas + gastos por servicios exteriores) × 365. El saldo medio se calcula aquí como la media del saldo inicial y final; si llevas saldos mensuales, puedes poner su media en ambas casillas.</p>
</div>
</section>
"""

PMP_CONTENT = """
<h2 id="que-es">Qué es el periodo medio de pago a proveedores</h2>
<p>El <strong>periodo medio de pago a proveedores (PMP)</strong> es el número medio de días que una sociedad tarda en pagar a sus proveedores, ponderado por el importe de cada operación. La disposición adicional tercera de la Ley 15/2010 obliga a <strong>todas las sociedades mercantiles</strong> a incluirlo de forma expresa en la memoria de sus cuentas anuales, y la <a href="https://www.boe.es/buscar/act.php?id=BOE-A-2016-1112" rel="noopener" target="_blank">Resolución del ICAC de 29 de enero de 2016</a> fija cómo se calcula. Esta calculadora aplica exactamente las fórmulas de su artículo 5 y prepara el cuadro de su artículo 6 listo para copiar o imprimir.</p>
<p>Para la resolución, «proveedores» son los acreedores comerciales del pasivo corriente por deudas con suministradores de bienes o servicios (art. 4.b), y el PMP es el plazo que transcurre desde la entrega de los bienes o la prestación de los servicios hasta el pago material de la operación (art. 4.a). Quedan fuera las deudas retenidas por embargos, mandamientos de ejecución o compensaciones administrativas (art. 3.3) y, en general, todo lo que no sea una operación comercial del artículo 3 de la Ley 3/2004: por ejemplo, los pagos a la Seguridad Social, a Hacienda o los préstamos.</p>

<h2 id="formula">La fórmula del ICAC, paso a paso (memoria normal)</h2>
<p>Las sociedades que presentan el modelo normal de memoria calculan tres datos. Primero, la <strong>ratio de operaciones pagadas</strong> (art. 5.2): para cada factura pagada en el ejercicio se multiplican los días de pago por el importe, se suman los resultados y se dividen entre el total pagado. Los días de pago son los días naturales desde el inicio del cómputo hasta el pago material.</p>
<p>Segundo, la <strong>ratio de operaciones pendientes de pago</strong> (art. 5.3): lo mismo con las facturas pendientes al cierre, contando los días naturales desde el inicio del cómputo hasta el último día del ejercicio. Tercero, el <strong>PMP</strong> (art. 5.1), que es la media de las dos ratios ponderada por sus importes:</p>
<div class="formula"><p><strong>Ratio pagadas</strong> = Σ (días de pago × importe pagado) ÷ total pagos realizados</p><p><strong>Ratio pendientes</strong> = Σ (días pendientes × importe pendiente) ÷ total pagos pendientes</p><p><strong>PMP</strong> = (ratio pagadas × total pagado + ratio pendientes × total pendiente) ÷ (total pagado + total pendiente)</p></div>
<p>El cómputo empieza en la fecha de recepción de las mercancías o de prestación de los servicios. Solo si no hay información fiable sobre ese momento se puede usar la fecha de recepción de la factura (art. 5.4). Fíjate en que el PMP del ICAC mide <strong>días totales</strong> desde la entrega, no los días de retraso sobre el vencimiento.</p>

<h2 id="ejemplo">Ejemplo resuelto</h2>
<p>Una sociedad cierra el 31/12/2025 con estas cuatro operaciones (es el ejemplo que carga el botón «Cargar ejemplo»):</p>
<div class="table-wrap"><table>
<thead><tr><th>Factura</th><th>Importe</th><th>Inicio</th><th>Pago</th><th>Situación al cierre</th><th>Días</th></tr></thead>
<tbody>
<tr><td>A-1</td><td>1.000,00 €</td><td>10/01/2025</td><td>09/02/2025</td><td>Pagada</td><td>30</td></tr>
<tr><td>A-2</td><td>2.000,00 €</td><td>01/03/2025</td><td>10/05/2025</td><td>Pagada</td><td>70</td></tr>
<tr><td>A-3</td><td>500,00 €</td><td>15/11/2025</td><td>—</td><td>Pendiente</td><td>46</td></tr>
<tr><td>A-4</td><td>1.500,00 €</td><td>01/12/2025</td><td>20/01/2026</td><td>Pendiente (se pagó después del cierre)</td><td>30</td></tr>
</tbody></table></div>
<p>Ratio de operaciones pagadas = (30 × 1.000 + 70 × 2.000) ÷ 3.000 = <strong>56,67 días</strong>. Ratio de operaciones pendientes = (46 × 500 + 30 × 1.500) ÷ 2.000 = <strong>34,00 días</strong>. PMP = (56,67 × 3.000 + 34 × 2.000) ÷ 5.000 = <strong>47,60 días</strong>. La factura A-4 se pagó en enero de 2026, pero a 31 de diciembre estaba pendiente, así que cuenta como pendiente con 30 días. Si quieres ver cómo se hace a mano o en Excel, lo explicamos en la guía <a href="/blog/calcular-periodo-medio-pago-proveedores-ejemplo/">cómo calcular el periodo medio de pago a proveedores</a>.</p>

<h2 id="abreviada">Memoria abreviada y PGC de Pymes: la fórmula simplificada</h2>
<p>Las sociedades que formulan la memoria abreviada o aplican el Plan General de Contabilidad de Pymes no necesitan ir factura a factura. El artículo 5.5 les permite usar: <strong>PMP = saldo medio de acreedores comerciales ÷ (compras netas + gastos por servicios exteriores) × 365</strong>. Los acreedores comerciales incluyen proveedores y acreedores varios por deudas con suministradores de bienes o servicios sujetos a los plazos legales, y las compras y gastos son los importes contabilizados en los subgrupos del PGC. En la pestaña «Memoria abreviada» introduces el saldo inicial y final y la calculadora hace la media. En la memoria abreviada solo se informa del PMP (art. 6.3), sin ratios.</p>

<h2 id="memoria">Qué hay que poner en la memoria</h2>
<p>El artículo 6.1 exige una nota titulada «Información sobre el periodo medio de pago a proveedores. Disposición adicional tercera. "Deber de información" de la Ley 15/2010, de 5 de julio», con un cuadro de dos columnas (ejercicio actual N y anterior N-1) que recoja: el periodo medio de pago a proveedores, la ratio de operaciones pagadas y la ratio de operaciones pendientes de pago, en días; y el total de pagos realizados y el total de pagos pendientes, en euros. La calculadora genera ese cuadro y, si escribes el PMP del año anterior, lo coloca en la columna N-1.</p>
<p>Desde la Ley 18/2022 («Crea y Crece»), la misma disposición adicional tercera pide además a las sociedades cotizadas y a las no cotizadas que no presenten cuentas anuales abreviadas que publiquen <strong>el volumen monetario y el número de facturas pagadas en un periodo inferior al máximo establecido en la normativa de morosidad</strong>, y el porcentaje que suponen sobre el total de facturas y sobre el total monetario de pagos, en su página web si la tienen y en la memoria. La calculadora cuenta esas facturas con el límite que elijas (60 días por defecto, el máximo pactable del artículo 4.3 de la Ley 3/2004) y te da los dos porcentajes.</p>

<h2 id="60-dias">El límite de 60 días y qué pasa si lo superas</h2>
<p>El plazo de pago legal entre empresas es de 30 días naturales desde la recepción de las mercancías o la prestación de los servicios si no se pacta otro, y las partes pueden ampliarlo hasta un máximo de <strong>60 días naturales</strong> (art. 4 de la Ley 3/2004). Por eso la calculadora compara el PMP con 60 días. Un PMP superior indica que, de media, se paga por encima del máximo legal; uno inferior no garantiza que todas las facturas se hayan pagado en plazo, porque es una media. Para revisar cada factura, mira la columna de días del detalle o la lista de facturas pagadas fuera del límite.</p>
<p>Superar los plazos tiene consecuencias económicas directas para el deudor: el proveedor puede reclamar intereses de demora y una compensación por costes de cobro (arts. 5 a 8 de la Ley 3/2004), que puedes estimar con nuestra <a href="/intereses-demora-comerciales/">calculadora de intereses de demora</a>. Además, con la <a href="/factura-electronica-obligatoria/">factura electrónica obligatoria entre empresas</a>, los destinatarios tendrán que comunicar a la AEAT la fecha de pago de cada factura (art. 12 del RD 238/2026), y la AEAT enviará al Observatorio Estatal de la Morosidad Privada la información para elaborar el listado de empresas incumplidoras (art. 14). El PMP dejará de ser un dato que solo se mira al cerrar las cuentas.</p>

<h2 id="csv">Cómo preparar el CSV</h2>
<p>Descarga la plantilla y rellena una fila por factura: <code>factura;proveedor;importe;fecha_inicio;fecha_pago</code>. Acepta separador punto y coma, coma o tabulador, importes con coma decimal (<code>1.234,56</code>) o punto (<code>1234.56</code>) y fechas <code>DD/MM/AAAA</code> o <code>AAAA-MM-DD</code>. Deja vacía la fecha de pago si la factura está pendiente al cierre. Si tu programa exporta columnas en otro orden, la calculadora las reconoce por el nombre de la cabecera («importe», «fecha recepción», «fecha pago»…). También puedes copiar las filas directamente desde Excel y pegarlas en el cuadro de texto. El archivo no se sube a ningún servidor: se lee en tu navegador.</p>
<p>Las filas con fechas o importes no válidos, las operaciones que empiezan después del cierre y los pagos anteriores al inicio del ejercicio se omiten y se listan en los avisos, para que sepas exactamente qué ha entrado en el cálculo.</p>
"""

PMP_FAQ = [
    ("¿Cómo se calcula el periodo medio de pago a proveedores?", "Con la fórmula del art. 5 de la Resolución del ICAC de 29/01/2016: PMP = (ratio de operaciones pagadas × total pagado + ratio de operaciones pendientes × total pendiente) ÷ (total pagado + total pendiente). Cada ratio es la media de días ponderada por importe de las facturas pagadas en el ejercicio o pendientes al cierre."),
    ("¿Desde qué fecha se cuentan los días?", "Desde la recepción de las mercancías o la prestación de los servicios. Solo si no hay información fiable sobre esa fecha se puede usar la de recepción de la factura (art. 5.4 de la resolución). Se cuentan días naturales."),
    ("¿Cuál es la fórmula del PMP en la memoria abreviada?", "Saldo medio de acreedores comerciales ÷ (compras netas + gastos por servicios exteriores) × 365 (art. 5.5). La aplican quienes formulan memoria abreviada o usan el PGC de Pymes, y en la memoria solo informan del PMP."),
    ("¿Cuál es el plazo máximo de pago a proveedores?", "30 días naturales desde la recepción de los bienes o servicios si no hay pacto, ampliables por acuerdo hasta un máximo de 60 días naturales (art. 4 de la Ley 3/2004). Por eso el PMP se compara con 60 días."),
    ("¿Qué facturas no entran en el PMP?", "Las que no son operaciones comerciales de la Ley 3/2004 y las obligaciones de pago retenidas por embargos, mandamientos de ejecución o compensaciones administrativas o judiciales (art. 3.3 de la resolución)."),
    ("¿Qué información extra exige la Ley Crea y Crece sobre el PMP?", "Las sociedades cotizadas y las no cotizadas que no presenten cuentas abreviadas deben publicar el número e importe de las facturas pagadas en un periodo inferior al máximo legal y el porcentaje que suponen sobre el total de facturas y de pagos (DA 3.ª de la Ley 15/2010, en la redacción de la Ley 18/2022). La calculadora lo calcula."),
    ("¿Se envían mis facturas a algún servidor?", "No. El CSV y las filas que escribes se procesan en tu navegador y desaparecen al cerrar la página."),
]

PMP = dict(
    title="Periodo medio de pago a proveedores: calculadora y fórmula",
    desc="Calcula gratis el periodo medio de pago a proveedores con el método ICAC: ratios de pagadas y pendientes, límite de 60 días, CSV y cuadro de la memoria.",
    app_name="Calculadora del periodo medio de pago a proveedores (método ICAC)",
    h1="Calculadora del periodo medio de pago a proveedores (PMP)",
    intro="Calcula el periodo medio de pago a proveedores (PMP): introduce tus facturas o carga un CSV y obtén el PMP, la ratio de operaciones pagadas y la de pendientes de pago con la fórmula de la Resolución del ICAC de 2016, comparado con el límite legal de 60 días y listo para la memoria.",
    trail=[("Inicio", "/"), ("Periodo medio de pago", "/periodo-medio-pago-proveedores/")],
    tool=PMP_TOOL, content=PMP_CONTENT, faq=PMP_FAQ, scripts=["b2b.js", "page-pmp.js"],
    sources=[S.ICAC, S.LEY15, S.LEY3, S.RD238],
)


# ======================================================================================
# 2. Factura electrónica obligatoria B2B
# ======================================================================================
B2B_TOOL = """
<section class="tool" aria-labelledby="fe-estado-h">
<h2 id="fe-estado-h">Fechas de la factura electrónica obligatoria entre empresas</h2>
<div class="dates">
 <div class="date-card"><span class="tag">En el BOE · vigente</span><span class="big">6 de octubre de 2027</span><small>Volumen de operaciones de más de 8 millones de euros en el año anterior · <span id="cd-27">fecha vigente</span></small></div>
 <div class="date-card"><span class="tag">En el BOE · vigente</span><span class="big">6 de octubre de 2028</span><small>Resto de empresarios y profesionales · <span id="cd-28">fecha vigente</span></small></div>
 <div class="date-card"><span class="tag">En el BOE · vigente</span><span class="big">6 de octubre de 2029</span><small>Estados y pagos: autónomos y entidades en atribución de rentas de hasta 8 M€ (DT 3.ª)</small></div>
</div>
<p class="checked"><strong>Última comprobación: """ + CHECKED_ES + """.</strong> El <a href="https://www.boe.es/buscar/act.php?id=BOE-A-2026-7295" rel="noopener" target="_blank">RD 238/2026 (BOE-A-2026-7295)</a> retrasa su aplicación 12 y 24 meses desde la entrada en vigor de la orden de la solución pública (DF 4.ª). La <a href="https://www.boe.es/buscar/act.php?id=BOE-A-2026-20587" rel="noopener" target="_blank">Orden HAC/1028/2026 (BOE-A-2026-20587)</a> se publicó el 05/10/2026 y entró en vigor el 06/10/2026. Las fechas de día concreto son las que publica la <a href="https://sede.agenciatributaria.gob.es/Sede/iva/factura-electronica/calendario-implantacion.html" rel="noopener" target="_blank">AEAT en su calendario</a>.</p>
</section>
<section class="tool" aria-labelledby="fe-h">
<h2 id="fe-h">Test: ¿cuándo me obliga la factura electrónica B2B?</h2>
<form id="fe-form" novalidate>
<fieldset><legend>1. ¿Facturas a empresas o profesionales establecidos en España?</legend><div class="radios">
<label><input type="radio" name="b2b" value="si" checked> Sí, tengo clientes empresas o autónomos</label>
<label><input type="radio" name="b2b" value="no"> No, solo vendo a particulares</label>
</div></fieldset>
<fieldset><legend>2. ¿Qué eres?</legend><div class="radios">
<label><input type="radio" name="forma" value="juridica"> Sociedad u otra persona jurídica o entidad</label>
<label><input type="radio" name="forma" value="fisica"> Autónomo (persona física) o entidad en atribución de rentas (comunidad de bienes, sociedad civil)</label>
</div></fieldset>
<fieldset><legend>3. Volumen de operaciones (IVA, art. 121 LIVA) del año natural anterior</legend><div class="radios">
<label><input type="radio" name="vol" value="mas"> Más de 8 millones de euros</label>
<label><input type="radio" name="vol" value="menos"> 8 millones de euros o menos</label>
</div></fieldset>
<fieldset><legend>4. ¿Cómo facturas a esos clientes?</legend><div class="radios">
<label><input type="radio" name="simp" value="no" checked> Facturas completas (o simplificadas cualificadas)</label>
<label><input type="radio" name="simp" value="solo"> Solo facturas simplificadas (tiques) no cualificadas</label>
</div></fieldset>
<div class="btns"><button class="btn" type="submit">Ver mis fechas</button><button class="btn ghost" type="reset">Empezar de nuevo</button></div>
</form>
<div id="fe-out" class="status" role="status" aria-live="polite" tabindex="-1"></div>
<p class="hint">Basado en los arts. 3, 4, 10 y 12, las DT 2.ª y 3.ª y la DF 4.ª del RD 238/2026. Orientativo; las respuestas no salen de tu navegador.</p>
</section>
<section class="tool" aria-labelledby="p4-h">
<h2 id="p4-h">Calculadora del plazo de 4 días para informar pagos y estados</h2>
<form id="p4-form" novalidate>
<div class="grid3">
<div class="field"><label for="p4-date">Fecha del pago, la aceptación o el rechazo</label><input id="p4-date" type="date" value="2027-10-08"></div>
<div class="field"><label for="p4-tipo">¿Qué tienes que informar?</label><select id="p4-tipo"><option value="pago">Pago efectivo completo (art. 12.3)</option><option value="rechazo">Rechazo de la factura (art. 12.1)</option><option value="estado">Aceptación o rechazo comercial (art. 10.3)</option></select></div>
<div class="field"><label for="p4-extra">Otros festivos que quieras excluir (opcional, DD/MM/AAAA separados por comas)</label><input id="p4-extra" type="text" placeholder="13/10/2027"></div>
</div>
<div class="btns"><button class="btn" type="submit">Calcular fecha límite</button></div>
</form>
<div id="p4-out" class="status" role="status" aria-live="polite" tabindex="-1"></div>
<p class="hint">El RD 238/2026 da 4 días naturales «excluyendo sábados, domingos y festivos nacionales». Tomamos como festivos nacionales los comunes a todo el territorio en la relación del BOE (2026: BOE-A-2025-21667; 2027: BOE-A-2026-21254). Para 2028 y siguientes, hasta que se publique su relación, usamos las fiestas nacionales no sustituibles y lo marcamos como provisional.</p>
</section>
"""

B2B_CONTENT = """
<h2 id="que-es">Qué es la factura electrónica obligatoria entre empresas</h2>
<p>La Ley 18/2022, de creación y crecimiento de empresas (conocida como <strong>Ley Crea y Crece</strong>), añadió a la Ley 56/2007 la obligación de que todos los empresarios y profesionales expidan, remitan y reciban <strong>facturas electrónicas</strong> en sus relaciones comerciales con otros empresarios y profesionales. Su objetivo principal no es fiscal, sino luchar contra la morosidad: con facturas estructuradas y la información de pago, la Administración podrá conocer los plazos reales de pago entre empresas. El desarrollo reglamentario llegó con el <strong>Real Decreto 238/2026, de 25 de marzo</strong>, y los detalles técnicos de la solución pública de la AEAT con la <strong>Orden HAC/1028/2026, de 2 de octubre</strong>.</p>
<p>No hay que confundirla con <a href="/">Verifactu</a>. Verifactu regula el <em>programa</em> con el que se emiten las facturas (registro, huella y QR) y es una norma tributaria; la factura electrónica B2B regula el <em>formato y el intercambio</em> de la factura entre empresas y el seguimiento de su pago. Muchas empresas tendrán que cumplir las dos. Lo explicamos en <a href="/blog/diferencias-verifactu-factura-electronica-b2b/">Verifactu y factura electrónica B2B: diferencias</a>.</p>

<h2 id="fechas">Fechas: cómo se calculan y por qué son el 6 de octubre</h2>
<p>La disposición final cuarta del RD 238/2026 dice que el real decreto entra en vigor a los veinte días de su publicación (BOE del 31/03/2026), pero que su aplicación efectiva queda diferida y se cuenta desde la entrada en vigor de la orden ministerial de la solución pública: <strong>doce meses después</strong> para quienes superaron 8 millones de euros de volumen de operaciones en el año natural anterior, y <strong>veinticuatro meses después</strong> para el resto. La Orden HAC/1028/2026 se publicó en el BOE el 5 de octubre de 2026 y entró en vigor el 6 de octubre de 2026, de modo que:</p>
<div class="table-wrap"><table>
<thead><tr><th>Quién</th><th>Emitir y recibir facturas electrónicas</th><th>Informar estados y pagos</th><th>Norma</th></tr></thead>
<tbody>
<tr><td>Volumen de operaciones &gt; 8 M€ en el año anterior</td><td>6 de octubre de 2027 (con PDF adjunto durante los primeros 12 meses)</td><td>6 de octubre de 2027</td><td>DF 4.ª.1.a y DT 2.ª</td></tr>
<tr><td>Sociedades y demás personas jurídicas o entidades ≤ 8 M€</td><td>6 de octubre de 2028</td><td>6 de octubre de 2028</td><td>DF 4.ª.1.b</td></tr>
<tr><td>Autónomos y entidades en atribución de rentas ≤ 8 M€</td><td>6 de octubre de 2028</td><td>6 de octubre de 2029 (antes, voluntario)</td><td>DF 4.ª.1.b y DT 3.ª</td></tr>
<tr><td>Plataformas privadas de intercambio</td><td colspan="2">6 de octubre de 2027 (copia fiel, interconexión y requisitos)</td><td>DF 4.ª.2</td></tr>
</tbody></table></div>
<p>El BOE expresa los plazos en meses («doce meses después», «veinticuatro meses después»); los días concretos son el cálculo que publica la AEAT en su calendario de implantación, que coincide con el nuestro. El volumen de operaciones es el del artículo 121 de la Ley del IVA en el <strong>año natural inmediato anterior</strong>.</p>

<h2 id="quien">Quién está obligado y quién no</h2>
<p>Según el artículo 3 del RD 238/2026, están obligados los empresarios y profesionales que deban expedir factura conforme al Reglamento de facturación cuando el destinatario sea otro empresario o profesional con sede, establecimiento permanente o domicilio en España. También cuando la factura la expida el propio cliente o un tercero por cuenta del proveedor: la responsabilidad sigue siendo de quien está obligado a facturar. Las ventas a <strong>particulares (B2C)</strong> no están afectadas por esta obligación.</p>
<p>El artículo 4 excluye las operaciones documentadas con <strong>facturas simplificadas</strong> (tiques), salvo que sean facturas simplificadas cualificadas, las del artículo 7.2 del Reglamento de facturación. Además, una orden ministerial podrá excluir temporalmente a sectores con dificultades de adaptación. Quien esté obligado deberá también <strong>recibir</strong> facturas electrónicas de sus proveedores desde su fecha.</p>

<h2 id="como">Cómo será la factura: formatos, plataformas y la solución pública</h2>
<p>Las facturas deberán seguir el modelo semántico europeo EN 16931 en una de las sintaxis admitidas por el artículo 7 (UBL, CII, EDIFACT o Facturae) y podrán intercambiarse a través de <strong>plataformas privadas</strong> interconectadas o de la <strong>solución pública de facturación electrónica (SPFE)</strong> de la AEAT, que usa la sintaxis UBL. Quien no emita a través de la solución pública deberá remitirle una <strong>copia fiel</strong> de cada factura. La AEAT ofrecerá además una aplicación o formulario gratuito para emitir facturas electrónicas e informar de su estado (disposición adicional primera). Para las empresas de más de 8 M€, durante sus primeros doce meses de obligación deberán acompañar cada factura electrónica de un PDF que asegure su legibilidad, salvo que el destinatario acepte recibirla solo en su formato original (DT 2.ª).</p>

<h2 id="cuatro-dias">El plazo de 4 días para informar pagos y rechazos</h2>
<p>El artículo 12.3 obliga al destinatario de cada factura electrónica a informar a la solución pública del <strong>pago efectivo completo</strong> de la factura y de su fecha, junto con la fecha de vencimiento del plazo de pago, «en un plazo máximo de 4 días naturales desde dicha fecha efectiva del pago, excluyendo sábados, domingos y festivos nacionales». El artículo 12.1 añade la comunicación del <strong>rechazo</strong>; si no hay rechazo ni factura rectificativa, la factura se presume aceptada. El artículo 10.3 aplica el mismo plazo a los estados que se comunican al emisor (aceptación o rechazo comercial y pago).</p>
<p>Aunque el texto dice «días naturales», al excluir sábados, domingos y festivos nacionales en la práctica son <strong>cuatro días laborables</strong>. Por ejemplo, un pago hecho el viernes 8 de octubre de 2027 debe informarse como tarde el viernes 15 de octubre, porque se saltan el fin de semana y el 12 de octubre. La calculadora de arriba hace este cómputo con la lista de fiestas del BOE. Las fiestas autonómicas y locales no aparecen en el texto del artículo; si quieres ir sobre seguro, añádelas como festivos opcionales y obtendrás una fecha más tardía, o informa antes.</p>
<p>El plazo de pago que se comunica se determina con el artículo 4 de la Ley 3/2004 (art. 15 del RD): 30 días desde la entrega de los bienes o la prestación de los servicios si no hay pacto, y nunca más de 60. Si la factura no indica la fecha de las operaciones, el plazo empieza en su fecha de expedición. Con estos datos, la AEAT podrá seguir los periodos de pago de cada empresa (art. 14), de ahí que convenga vigilar ya tu <a href="/periodo-medio-pago-proveedores/">periodo medio de pago a proveedores</a> y los <a href="/intereses-demora-comerciales/">intereses de demora</a> que generan los retrasos.</p>

<h2 id="preparar">Qué hacer ahora</h2>
<ol class="steps">
<li><strong>Mira tu volumen de operaciones del año anterior.</strong> Si en 2026 superas 8 M€, tu fecha es el 6/10/2027.</li>
<li><strong>Pregunta a tu proveedor de software o de plataforma</strong> si emitirá en UBL u otra sintaxis admitida, si enviará la copia fiel a la solución pública y si gestionará los estados y pagos.</li>
<li><strong>Revisa tu proceso de pagos</strong> para poder informar cada pago en cuatro días laborables y cumplir los plazos de la Ley 3/2004.</li>
<li><strong>Si eres autónomo con pocas facturas,</strong> sigue la herramienta gratuita que prepara la AEAT; lo contamos en <a href="/blog/factura-electronica-obligatoria-autonomos/">factura electrónica obligatoria para autónomos</a>.</li>
</ol>
<p>No incluimos importes de sanciones: el RD 238/2026 no los fija, y no publicamos cifras que no estén comprobadas en el BOE.</p>
"""

B2B_FAQ = [
    ("¿Cuándo es obligatoria la factura electrónica entre empresas?", "Desde el 6 de octubre de 2027 para quienes superaron 8 millones de euros de volumen de operaciones en el año anterior y desde el 6 de octubre de 2028 para el resto. Son 12 y 24 meses desde la entrada en vigor de la Orden HAC/1028/2026 (6/10/2026), según la DF 4.ª del RD 238/2026."),
    ("¿Los autónomos están obligados a la factura electrónica?", "Sí, cuando facturan a otras empresas o profesionales: desde el 6 de octubre de 2028 si su volumen de operaciones no supera 8 M€. La comunicación de estados y pagos no les será obligatoria hasta el 6 de octubre de 2029 (DT 3.ª); antes es voluntaria."),
    ("¿Hay que hacer factura electrónica a particulares?", "No. La obligación del RD 238/2026 se refiere a facturas cuyo destinatario es un empresario o profesional establecido en España."),
    ("¿Los tiques están incluidos?", "No, el art. 4 excluye las facturas simplificadas, salvo las simplificadas cualificadas a las que se refiere el art. 7.2 del Reglamento de facturación."),
    ("¿En cuántos días hay que informar del pago de una factura?", "En un máximo de 4 días naturales desde la fecha efectiva del pago, excluyendo sábados, domingos y festivos nacionales (art. 12.3 del RD 238/2026). En la práctica, cuatro días laborables."),
    ("¿Qué es la solución pública de facturación electrónica?", "Es la plataforma de la AEAT regulada por la Orden HAC/1028/2026. Permite emitir y recibir facturas en UBL, recibe la copia fiel de las facturas que se intercambian por plataformas privadas y el servicio de comunicación de pagos."),
    ("¿Es lo mismo que Verifactu?", "No. Verifactu regula el software de facturación (registros, huella y QR) por motivos fiscales; la factura electrónica B2B regula el formato y el intercambio de facturas entre empresas y el seguimiento de los pagos. Son obligaciones distintas que pueden coincidir."),
]

B2B = dict(
    title="Factura electrónica obligatoria: fechas 2027-2028 y test",
    desc="Factura electrónica obligatoria entre empresas: 6/10/2027 (más de 8 M€) y 6/10/2028 (resto). Test gratis, fechas del BOE y plazo de 4 días para pagos.",
    app_name="¿Cuándo me obliga la factura electrónica B2B? – test y plazo de 4 días",
    h1="Factura electrónica obligatoria B2B: fechas y quién está obligado",
    intro="¿Desde cuándo te afecta la factura electrónica obligatoria entre empresas? Comprueba en un minuto cuándo debes emitir y recibir facturas electrónicas e informar de pagos según el RD 238/2026, y calcula el plazo de 4 días para comunicar cada pago o rechazo.",
    trail=[("Inicio", "/"), ("Factura electrónica B2B", "/factura-electronica-obligatoria/")],
    tool=B2B_TOOL, content=B2B_CONTENT, faq=B2B_FAQ, scripts=["b2b.js", "page-b2b.js"],
    sources=[S.RD238, S.ORDEN1028, S.AEAT_CAL, S.LEY18, S.LEY3, S.FIESTAS27],
)


# ======================================================================================
# 3. Intereses de demora en operaciones comerciales
# ======================================================================================
DEM_TOOL = """
<section class="tool" aria-labelledby="dm-h">
<h2 id="dm-h">Calculadora de intereses de demora (Ley 3/2004)</h2>
<div class="table-wrap"><table class="rows-table" id="dm-table"><thead><tr><th>#</th><th>Factura</th><th>Importe adeudado (€, IVA incl.)</th><th>Vencimiento</th><th>Fecha de pago <span class="muted">(vacía = hoy)</span></th><th><span class="sr-only">Quitar</span></th></tr></thead><tbody id="dm-rows"></tbody></table></div>
<div class="btns"><button class="btn ghost small" type="button" id="dm-add">+ Añadir factura</button><button class="btn ghost small" type="button" id="dm-ex">Cargar ejemplo</button><button class="btn ghost small" type="button" id="dm-clear">Vaciar</button></div>
<div class="grid3">
<div class="field"><label for="dm-pact">Tipo de interés pactado en el contrato (% anual, opcional)</label><input id="dm-pact" type="text" inputmode="decimal" placeholder="Vacío = tipo legal del BOE"></div>
<div class="field"><label class="check" for="dm-40"><input id="dm-40" type="checkbox" checked> Añadir 40 € por cada factura pagada con retraso (art. 8.1)</label><label class="check" for="dm-est"><input id="dm-est" type="checkbox"> Estimar con el último tipo publicado si el periodo llega a un semestre sin tipo en el BOE</label></div>
<div class="field"><label for="dm-ent">¿No sabes el vencimiento? Fecha de entrega o prestación</label><input id="dm-ent" type="date"><label for="dm-dias">Plazo pactado (días, máx. 60)</label><input id="dm-dias" type="text" inputmode="numeric" value="30"><button class="btn ghost small" type="button" id="dm-venc">Calcular vencimiento</button><p id="dm-venc-out" class="hint" aria-live="polite"></p></div>
</div>
<div class="btns"><button class="btn" type="button" id="dm-go">Calcular intereses</button></div>
<div id="dm-out" class="status" role="status" aria-live="polite" tabindex="-1"></div>
<div id="dm-res"></div>
</section>
"""

DEM_CONTENT = """
<h2 id="como">Cómo calcula esta herramienta los intereses de demora</h2>
<p>En las operaciones comerciales entre empresas, y entre empresas y la Administración, el deudor que no paga en plazo <strong>incurre en mora automáticamente</strong>, sin necesidad de aviso ni reclamación (art. 5 de la Ley 3/2004). Desde ese momento debe el interés pactado en el contrato o, si no se pactó, el <strong>tipo legal de interés de demora</strong> del artículo 7: el tipo de la operación principal de financiación más reciente del Banco Central Europeo efectuada antes del primer día del semestre natural, <strong>más ocho puntos porcentuales</strong>, aplicado durante los seis meses siguientes. El Tesoro publica cada semestre en el BOE el tipo resultante.</p>
<p>La calculadora aplica un interés simple con base de 365 días. Los intereses empiezan a correr el día siguiente al vencimiento y llegan hasta el día del pago, ambos incluidos; cada día se liquida al tipo del semestre natural en que cae. Si el retraso abarca varios semestres, verás un tramo por semestre con su tipo y la resolución del BOE de la que sale. Si escribes un tipo pactado, se usa ese tipo en todo el periodo (art. 7.1: el contractual prevalece sobre el legal).</p>
<div class="formula"><p><strong>Interés de cada tramo</strong> = importe adeudado × tipo anual ÷ 100 × días del tramo ÷ 365</p></div>

<h2 id="ejemplo">Ejemplo resuelto</h2>
<p>Una factura de <strong>10.000,00 €</strong> vence el 15/06/2025 y se paga el 14/08/2025, con 60 días de retraso. Del 16 al 30 de junio (15 días) se aplica el tipo del primer semestre de 2025, 11,15 %: 10.000 × 11,15 % × 15 ÷ 365 = 45,82 €. Del 1 de julio al 14 de agosto (45 días) se aplica el del segundo semestre, 10,15 %: 10.000 × 10,15 % × 45 ÷ 365 = 125,14 €. Total de intereses: <strong>170,96 €</strong>, a los que se suman los <strong>40 €</strong> de compensación por costes de cobro. Es el ejemplo que carga el botón «Cargar ejemplo».</p>

<h2 id="tipos">Tipos legales de interés de demora publicados en el BOE</h2>
<p>Estos son los tipos que usa la calculadora, cada uno con su resolución del Tesoro en el BOE (BCE + 8 puntos). El último publicado es el del segundo semestre de 2026, <strong>10,40 %</strong> (BCE 2,40 % + 8). El del primer semestre de 2027 se publicará a finales de diciembre de 2026; hasta entonces, si tu cálculo llega a 2027, la herramienta te pide que lo marques como estimación.</p>
""" + tipos_table() + """
<p>Desde el 24 de febrero de 2013 el diferencial es de ocho puntos (antes eran siete), por eso la tabla empieza en el segundo semestre de 2013. El Banco de España mantiene un <a href="https://clientebancario.bde.es/pcb/es/menu-horizontal/podemosayudarte/tiposinteres/guia_textual/tiposinteresreferenciaotrostiposfrecuentes/tabla_tipos_interes_demora_operaciones_comerciales.html" rel="noopener" target="_blank">resumen de los mismos tipos</a>.</p>

<h2 id="cuarenta">Los 40 euros por costes de cobro</h2>
<p>El artículo 8.1 de la Ley 3/2004 dice textualmente: «Cuando el deudor incurra en mora, el acreedor tendrá derecho a cobrar del deudor una cantidad fija de 40 euros, que se añadirá en todo caso y sin necesidad de petición expresa a la deuda principal». Además, el acreedor puede reclamar los demás costes de cobro debidamente acreditados que superen esos 40 euros. El deudor no tiene que pagarlos si no es responsable del retraso (art. 8.2).</p>
<p>¿Son 40 euros por reclamación o por factura? El Tribunal de Justicia de la Unión Europea respondió en la <a href="https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:62020CJ0585" rel="noopener" target="_blank">sentencia de 20 de octubre de 2022, asunto C-585/20</a>, que la cantidad fija de 40 euros «debe abonarse por cada operación comercial no pagada a su vencimiento, acreditada en una factura, incluso cuando esa factura se presente conjuntamente con otras facturas en una reclamación administrativa o judicial única». Por eso la calculadora suma 40 € por cada factura pagada con retraso; puedes desmarcar la casilla si no quieres incluirlos.</p>

<h2 id="base">¿Sobre qué importe se calculan? ¿Incluye el IVA?</h2>
<p>Sobre la cantidad adeudada que no se pagó a su vencimiento. La misma sentencia del TJUE (C-585/20) interpreta que la «cantidad adeudada» de la Directiva 2011/7/UE incluye el IVA que figura en la factura, con independencia de si el acreedor ya lo ha ingresado en Hacienda. Si te pagaron una parte en plazo, introduce solo la parte pendiente; si el pago parcial llegó más tarde, divide la factura en dos filas con su importe y su fecha de pago.</p>

<h2 id="plazos">Cuándo vence una factura</h2>
<p>Si el contrato no fija plazo, el deudor tiene 30 días naturales desde la recepción de las mercancías o la prestación de los servicios, aunque haya recibido antes la factura (art. 4.1). Las partes pueden pactar un plazo más largo, pero nunca superior a 60 días naturales (art. 4.3). Si hay un procedimiento de aceptación o comprobación, este no puede durar más de 30 días y el plazo de pago cuenta desde la aceptación (art. 4.2). La herramienta incluye un pequeño ayudante que suma el plazo a la fecha de entrega y lo limita a 60 días. Con la factura electrónica obligatoria, el destinatario tendrá que comunicar a la AEAT tanto la fecha de vencimiento como la de pago de cada factura (art. 12.3 del RD 238/2026): consulta las fechas en <a href="/factura-electronica-obligatoria/">factura electrónica obligatoria B2B</a>.</p>

<h2 id="reclamar">Cómo usar el resultado para reclamar</h2>
<p>El resultado muestra el detalle por factura y por tramo, con la referencia del BOE de cada tipo, y puedes imprimirlo o descargarlo en CSV para adjuntarlo a un requerimiento de pago. Recuerda que las cláusulas que excluyen el interés de demora o la compensación por costes de cobro se presumen abusivas (art. 9 de la Ley 3/2004). Si eres tú quien paga, controlar estos importes ayuda a mantener un buen <a href="/periodo-medio-pago-proveedores/">periodo medio de pago a proveedores</a>. Esta calculadora es orientativa y no sustituye el consejo de un abogado: no tiene en cuenta normas especiales de algunos sectores ni los intereses procesales.</p>
"""

DEM_FAQ = [
    ("¿Cuál es el interés de demora en operaciones comerciales en 2026?", "10,15 % en el primer semestre de 2026 (BOE-A-2025-27201) y 10,40 % en el segundo semestre (BOE-A-2026-14327), salvo que el contrato fije otro tipo."),
    ("¿Cómo se calcula el interés de demora de una factura?", "Importe adeudado × tipo anual × días de retraso ÷ 365, aplicando a cada día el tipo del semestre en que cae. Los días cuentan desde el día siguiente al vencimiento hasta el día del pago."),
    ("¿Hay que reclamar para que se devenguen los intereses?", "No. El art. 5 de la Ley 3/2004 establece que el deudor incurre en mora automáticamente por el mero incumplimiento del plazo, sin aviso de vencimiento ni intimación."),
    ("¿Los 40 euros son por factura?", "Según la sentencia del TJUE de 20/10/2022 (C-585/20), sí: por cada operación comercial no pagada a su vencimiento y acreditada en una factura, aunque se reclamen varias juntas."),
    ("¿Se calculan intereses sobre el IVA?", "Sí. El TJUE (C-585/20) interpreta que la cantidad adeudada incluye el IVA indicado en la factura, aunque el acreedor no lo haya ingresado aún en Hacienda."),
    ("¿Qué tipo se aplica si hay pacto en el contrato?", "El pactado. El tipo legal solo se aplica en defecto de pacto (art. 7.1 de la Ley 3/2004). Escribe el tipo pactado en la casilla correspondiente."),
    ("¿Y si el retraso llega a 2027?", "El tipo del primer semestre de 2027 se publicará en el BOE a finales de 2026. Hasta entonces la calculadora solo puede estimarlo con el último tipo publicado, y lo indica claramente."),
]

DEM = dict(
    title="Calculadora de intereses de demora comerciales (Ley 3/2004)",
    desc="Calcula los intereses de demora de tus facturas con los tipos del BOE (10,40 % en el 2.º semestre de 2026), más 40 € por factura. Gratis y en tu navegador.",
    app_name="Calculadora de intereses de demora en operaciones comerciales",
    h1="Calculadora de intereses de demora en operaciones comerciales",
    intro="Calcula los intereses de demora de una o varias facturas impagadas o pagadas tarde con los tipos legales publicados en el BOE para cada semestre (BCE + 8 puntos) y añade la compensación de 40 € del art. 8 de la Ley 3/2004.",
    trail=[("Inicio", "/"), ("Intereses de demora", "/intereses-demora-comerciales/")],
    tool=DEM_TOOL, content=DEM_CONTENT, faq=DEM_FAQ, scripts=["b2b.js", "page-demora.js"],
    sources=[S.LEY3, S.TESORO26, S.TJUE40, S.BDE_TIPOS, S.RD238],
)
