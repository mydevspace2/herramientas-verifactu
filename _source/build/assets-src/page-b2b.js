/*! Factura electrónica obligatoria B2B – test de fechas (RD 238/2026) y plazo de 4 días (arts. 10.3 y 12.3) */
(function () {
  "use strict";
  var U = window.UI, B = window.B2B, $ = U.$;
  if (!B) return;
  function hoy() { return B.todayUTC(); }
  function txtDias(t) { var n = B.diffDays(hoy(), t); return n > 1 ? "quedan " + n + " días" : n === 1 ? "queda 1 día" : n === 0 ? "es hoy" : "fecha ya alcanzada"; }
  if ($("cd-27")) $("cd-27").textContent = txtDias(B.FECHAS_B2B.grandes);
  if ($("cd-28")) $("cd-28").textContent = txtDias(B.FECHAS_B2B.resto);
  function largo(t) { return B.largo(t).replace(/^[^,]+, /, ""); }

  var form = $("fe-form"), out = $("fe-out");
  if (form) {
    var val = function (n) { var r = form.querySelector('input[name="' + n + '"]:checked'); return r ? r.value : ""; };
    var complete = function () { return !!(val("b2b") && val("forma") && val("vol") && val("simp")); };
    form.addEventListener("submit", function (e) { e.preventDefault(); evaluate(true); });
    U.autoForm(form, complete, evaluate);
    function evaluate(fromButton) {
      var a = { b2b: val("b2b"), forma: val("forma"), volumen: val("vol"), simplificadas: val("simp") }, falta = [];
      if (!a.forma) falta.push("qué eres"); if (!a.volumen) falta.push("volumen de operaciones");
      if (falta.length) { U.statusBox(out, "warn", "Falta responder: " + falta.join(", ") + "."); U.reveal(out, fromButton); return; }
      var r = B.obligacionB2B(a), notes = [], head, lvl = "warn", cards = [];
      function card(tag, t, small) { return '<div class="date-card"><span class="tag">' + tag + '</span><span class="big">' + largo(t) + "</span><small>" + small + " · " + txtDias(t) + "</small></div>"; }
      if (r.emitir) {
        head = "Debes emitir y recibir facturas electrónicas desde el " + largo(r.emitir) + ".";
        cards.push(card("Emitir y recibir", r.emitir, a.volumen === "mas" ? "DF 4.ª.1.a RD 238/2026" : "DF 4.ª.1.b RD 238/2026"));
      } else {
        lvl = "info";
        head = a.b2b === "no" ? "Si solo facturas a particulares, no tienes que emitir facturas electrónicas por el RD 238/2026." : "Las facturas simplificadas no cualificadas están excluidas (art. 4): no tienes que emitirlas en formato electrónico.";
        notes.push("Aun así, como empresario o profesional deberás poder recibir facturas electrónicas de tus proveedores obligados desde el " + largo(r.recibir) + ".");
        cards.push(card("Recibir", r.recibir, a.volumen === "mas" ? "DF 4.ª.1.a RD 238/2026" : "DF 4.ª.1.b RD 238/2026"));
        if (a.simplificadas === "solo") notes.push("Si un cliente empresario te pide factura completa o simplificada cualificada, esa factura sí tendrá que ser electrónica.");
      }
      cards.push(card("Informar estados y pagos", r.estados, a.volumen === "mas" ? "arts. 10 y 12, DF 4.ª.1.a" : a.forma === "fisica" ? "DT 3.ª RD 238/2026 (antes, voluntario)" : "arts. 10 y 12, DF 4.ª.1.b"));
      if (r.pdf) notes.push("Durante los 12 meses siguientes a esa fecha deberás acompañar cada factura electrónica de un PDF que garantice su legibilidad, salvo que el destinatario acepte expresamente recibirla solo en su formato original (DT 2.ª).");
      if (a.volumen === "mas") notes.push("El volumen de operaciones es el del art. 121 de la Ley del IVA en el año natural inmediato anterior: para el 6/10/2027, el de 2026.");
      notes.push("Informar el pago: como destinatario, cada pago completo o rechazo se comunica a la solución pública de la AEAT en un máximo de 4 días naturales, excluidos sábados, domingos y festivos nacionales (art. 12.3). Usa la calculadora de abajo.");
      notes.push("Orientativo. Una orden ministerial puede excluir temporalmente algunos sectores (art. 4.2). Comprobado en el BOE el 13/11/2026.");
      U.statusBox(out, lvl, head, { notes: notes, html: '<div class="dates">' + cards.join("") + "</div>", copy: true });
      U.reveal(out, fromButton);
    }
    form.addEventListener("reset", function () { U.statusBox(out, null); });
  }

  var pf = $("p4-form"), po = $("p4-out");
  if (pf) pf.addEventListener("submit", function (e) {
    e.preventDefault();
    var extra = $("p4-extra").value.split(/[,;\s]+/).filter(Boolean), bad = extra.filter(function (x) { return B.parseDate(x) == null; });
    if (bad.length) { U.statusBox(po, "bad", "Fecha no válida en los festivos adicionales: " + bad.join(", ")); po.focus(); return; }
    var r = B.plazo4($("p4-date").value, { extra: extra });
    if (!r.ok) { U.statusBox(po, "bad", "Indica la fecha del pago, la aceptación o el rechazo."); po.focus(); return; }
    var qu = { pago: "el pago efectivo completo", rechazo: "el rechazo", estado: "la aceptación o el rechazo comercial" }[$("p4-tipo").value];
    var notes = ["Días que cuentan: " + r.computados.map(B.es).join(", ") + "."];
    if (r.saltados.length) notes.push("Días excluidos (sábados, domingos y festivos): " + r.saltados.map(function (t) { return B.es(t); }).join(", ") + ".");
    var y = new Date(r.fecha).getUTCFullYear(), f = B.festivosAnio(y);
    notes.push(f.oficial ? "Festivos nacionales de " + y + " según " + f.boe + "." : "Provisional: el BOE aún no ha publicado la relación de fiestas de " + y + "; se usan las fiestas nacionales no sustituibles (1/1, Viernes Santo, 1/5, 15/8, 12/10, 1/11, 6/12, 8/12 y 25/12).");
    notes.push("Si te afectan fiestas autonómicas o locales, añádelas arriba para ver una fecha más prudente.");
    U.statusBox(po, r.provisional ? "warn" : "ok", "Último día para informar " + qu + ": " + B.largo(r.fecha), { notes: notes, copy: true });
    U.reveal(po, true);
  });
})();
