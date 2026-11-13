/*! ¿Estoy obligado a Verifactu? – comprobador (art. 1.3, 3 y 4 y DF 4.ª del RD 1007/2023) */
(function () {
  "use strict";
  var U = window.UI, $ = U.$;
  var FECHA_IS = new Date(2027, 0, 1), FECHA_RESTO = new Date(2027, 6, 1);
  function dias(hasta) {
    var hoy = new Date(); hoy.setHours(0, 0, 0, 0);
    return Math.round((hasta - hoy) / 86400000);
  }
  function txtDias(n) { return n > 1 ? "quedan " + n + " días" : n === 1 ? "queda 1 día" : n === 0 ? "es hoy" : "fecha ya alcanzada"; }
  // cuenta atrás de las fechas del BOE
  ["cd-is", "cd-resto"].forEach(function (id, i) { var el = $(id); if (el) el.textContent = txtDias(dias(i ? FECHA_RESTO : FECHA_IS)); });

  var form = $("ob-form"), out = $("ob-out");
  if (!form) return;
  function val(name) { var r = form.querySelector('input[name="' + name + '"]:checked'); return r ? r.value : ""; }
  var NOTA_2028 = "Atención: el 5 de octubre de 2026 el Ministerio de Hacienda anunció su intención de aplazar estas obligaciones hasta octubre de 2028. A 13 de noviembre de 2026 ese aplazamiento NO está publicado en el BOE, así que legalmente siguen vigentes las fechas de 2027.";
  function fechaHtml(soc) {
    var f = soc ? "antes del 1 de enero de 2027" : "antes del 1 de julio de 2027";
    var d = txtDias(dias(soc ? FECHA_IS : FECHA_RESTO));
    return '<div class="dates"><div class="date-card"><span class="tag">En el BOE (vigente)</span><span class="big">' + f + "</span><small>" + d + " · RD 1007/2023, DF 4.ª (redacción del RDL 15/2025)</small></div>" +
      '<div class="date-card pending"><span class="tag pending">Anunciado, sin BOE</span><span class="big">octubre de 2028</span><small>Nota de Hacienda del 05/10/2026 · sin día concreto</small></div></div>';
  }
  function complete() { var t = val("tipo"); return !!(val("dom") && t && (t === "productor" || (val("sii") && val("emi")))); }
  form.addEventListener("submit", function (e) { e.preventDefault(); evaluate(true); });
  U.autoForm(form, complete, evaluate);
  function evaluate(fromButton) {
    var dom = val("dom"), tipo = val("tipo"), sii = val("sii"), emi = val("emi");
    var falta = [];
    if (!dom) falta.push("domicilio fiscal"); if (!tipo) falta.push("cómo tributas");
    if (tipo !== "productor") { if (!sii) falta.push("SII"); if (!emi) falta.push("cómo emites las facturas"); }
    if (falta.length) { U.statusBox(out, "warn", "Falta responder: " + falta.join(", ") + "."); U.reveal(out, fromButton); return; }
    var lvl, head, notes = [], html = "";
    if (tipo === "productor") {
      lvl = "warn"; head = "Como productor o comercializador de software de facturación, tus obligaciones ya están en vigor.";
      notes.push("El art. 3.2 del reglamento obliga a quien produce o comercializa sistemas informáticos de facturación. Debía ofrecer productos adaptados en un máximo de nueve meses desde la entrada en vigor de la Orden HAC/1177/2024 (29/10/2024), es decir, desde el 29 de julio de 2025.");
      notes.push("Si además facturas tu propia actividad con un programa, vuelve a responder eligiendo «sociedad» o «autónomo».");
    } else if (dom === "pv" || dom === "navarra") {
      lvl = "info"; head = "Con domicilio fiscal en " + (dom === "pv" ? "el País Vasco" : "Navarra") + ", el reglamento estatal (Verifactu) no se te aplica.";
      notes.push("El art. 1.3 del RD 1007/2023 solo lo aplica, respecto de estos territorios, a quien tiene su domicilio fiscal en territorio común.");
      notes.push(dom === "pv" ? "En el País Vasco rige TicketBAI (y en Bizkaia, Batuz). Consulta a tu Diputación Foral." : "Consulta la normativa foral de la Hacienda de Navarra.");
    } else if (tipo === "nr-sin-ep") {
      lvl = "info"; head = "Un no residente sin establecimiento permanente no figura entre los obligados.";
      notes.push("El art. 3.1 incluye el IRNR solo cuando se obtienen rentas mediante establecimiento permanente.");
    } else if (tipo === "exenta") {
      lvl = "info"; head = "Las entidades totalmente exentas del Impuesto sobre Sociedades (art. 9.1 LIS) no están sometidas.";
      notes.push("Lo dice expresamente el art. 3.1.a) del reglamento. Las parcialmente exentas sí lo están por las rentas sujetas y no exentas.");
    } else if (sii === "si") {
      lvl = "info"; head = "Si llevas los libros registro de IVA por el SII, Verifactu no se te aplica.";
      notes.push("Art. 3.3 del RD 1007/2023: el reglamento no se aplica a quienes llevan los libros registro conforme al art. 62.6 del Reglamento del IVA (Suministro Inmediato de Información).");
      notes.push("Si dejas el SII, pasarías a estar obligado si usas un programa de facturación.");
    } else if (emi === "mano") {
      lvl = "info"; head = "Si facturas solo a mano (talonario de papel), no usas un sistema informático de facturación.";
      notes.push("El reglamento regula los sistemas informáticos que usas para expedir facturas. En cuanto uses un programa, aunque sea para una parte de tu actividad, te afecta (art. 3.1).");
    } else if (emi === "no") {
      lvl = "info"; head = "Si no expides facturas, Verifactu no te exige nada por ahora.";
      notes.push("Verifactu afecta al software con el que se expiden facturas, completas o simplificadas (tiques). Recibir facturas no te obliga.");
    } else {
      var soc = tipo === "sociedad" || tipo === "parcial";
      if (emi === "excel") {
        lvl = "warn"; head = "Depende de cómo uses Excel o Word.";
        notes.push("Según las preguntas frecuentes de la AEAT, no te afecta si la hoja de cálculo o el procesador de textos se usan solo para introducir los datos, expedir e imprimir las facturas y conservarlas.");
        notes.push("Sí se considera sistema informático de facturación si, por ejemplo, programas una macro que genera el libro registro de facturas expedidas. En ese caso te aplicaría la fecha de abajo.");
      } else if (emi === "tercero") {
        lvl = "warn"; head = "Sigues estando obligado, aunque las facturas las emita tu cliente o un tercero.";
        notes.push("El art. 6 permite que el destinatario o un tercero cumplan materialmente las obligaciones, pero la responsabilidad sigue siendo tuya. Comprueba que su sistema esté adaptado.");
      } else {
        lvl = "warn"; head = soc ? "Sí: estás obligado. Fecha vigente en el BOE: antes del 1 de enero de 2027." : "Sí: estás obligado. Fecha vigente en el BOE: antes del 1 de julio de 2027.";
        notes.push(soc ? "Eres contribuyente del Impuesto sobre Sociedades (art. 3.1.a)." : "Estás en el art. 3.1 (" + (tipo === "autonomo" ? "IRPF con actividad económica" : tipo === "atribucion" ? "entidad en atribución de rentas" : "IRNR con establecimiento permanente") + ").");
        if (tipo === "parcial") notes.push("Como entidad parcialmente exenta, solo por las operaciones que generen rentas sujetas y no exentas del impuesto.");
        notes.push("Tu programa de facturación debe cumplir el reglamento: modalidad VERI*FACTU (envía cada registro a la AEAT) o no VERI*FACTU (guarda los registros firmados y encadenados). Si facturas poco, la AEAT ofrece una aplicación gratuita.");
      }
      html = fechaHtml(soc);
      notes.push(NOTA_2028);
    }
    notes.push("Orientativo. No sustituye el asesoramiento profesional ni contempla supuestos especiales (art. 4: operaciones excluidas; art. 5: resolución de no aplicación).");
    U.statusBox(out, lvl, head, { notes: notes, html: html, copy: true });
    U.reveal(out, fromButton);
  }
  form.addEventListener("reset", function () { U.statusBox(out, null); });
})();
