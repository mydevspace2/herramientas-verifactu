/*! Calculadora de intereses de demora en operaciones comerciales – Ley 3/2004, arts. 4, 7 y 8 */
(function () {
  "use strict";
  var U = window.UI, B = window.B2B, K = window.VF, $ = U.$;
  if (!$("dm-rows") || !B) return;
  var esc = K.esc, d = function (x) { return B.fmt(x, 2); };
  function siteName() { var m = document.querySelector('meta[property="og:site_name"]'); return m ? m.content : ""; }
  var tbody = $("dm-rows");
  function renumber() { [].forEach.call(tbody.rows, function (tr, i) { tr.cells[0].textContent = i + 1; [].forEach.call(tr.querySelectorAll("input"), function (inp) { inp.setAttribute("aria-label", inp.getAttribute("data-l") + ", fila " + (i + 1)); }); }); }
  function addRow(r) {
    r = r || {};
    var tr = document.createElement("tr");
    tr.innerHTML = "<td></td>" +
      '<td data-h="Factura"><input type="text" class="w-s" data-k="factura" data-l="Factura" autocomplete="off"></td>' +
      '<td data-h="Importe adeudado (€)"><input type="text" class="w-s" data-k="importe" data-l="Importe adeudado" inputmode="decimal" autocomplete="off"></td>' +
      '<td data-h="Vencimiento"><input type="date" data-k="venc" data-l="Vencimiento"></td>' +
      '<td data-h="Fecha de pago (vacía = hoy)"><input type="date" data-k="pago" data-l="Fecha de pago"></td>' +
      '<td><button type="button" class="btn ghost small del" aria-label="Quitar factura">✕</button></td>';
    ["factura", "importe", "venc", "pago"].forEach(function (k) { tr.querySelector('[data-k="' + k + '"]').value = r[k] || ""; });
    tbody.appendChild(tr); renumber(); return tr;
  }
  tbody.addEventListener("click", function (e) { var b = e.target.closest && e.target.closest("button.del"); if (!b) return; b.closest("tr").remove(); if (!tbody.rows.length) addRow(); renumber(); });
  function rows() { return [].map.call(tbody.rows, function (tr) { var o = {}; [].forEach.call(tr.querySelectorAll("input"), function (i) { o[i.getAttribute("data-k")] = i.value; }); return o; }); }
  addRow(); addRow();
  $("dm-add").addEventListener("click", function () { addRow().querySelector("input").focus(); });
  $("dm-clear").addEventListener("click", function () { tbody.innerHTML = ""; addRow(); addRow(); U.statusBox($("dm-out"), null); $("dm-res").innerHTML = ""; });
  $("dm-ex").addEventListener("click", function () {
    tbody.innerHTML = "";
    addRow({ factura: "F-2025-118", importe: "10.000,00", venc: "2025-06-15", pago: "2025-08-14" });
    addRow({ factura: "F-2025-131", importe: "2.420,00", venc: "2025-12-31", pago: "2026-01-31" });
    $("dm-pact").value = ""; $("dm-40").checked = true; calc();
  });
  $("dm-venc").addEventListener("click", function () {
    var v = B.vencimiento($("dm-ent").value, $("dm-dias").value), o = $("dm-venc-out");
    if (!v.ok) { o.textContent = v.errors.join(" "); return; }
    o.textContent = "Vence el " + B.largo(v.fecha) + " (" + v.dias + " días)." + (v.warnings.length ? " " + v.warnings[0] : "") + " Cópialo en la columna «Vencimiento».";
  });

  var last = null;
  function tablaRes(res, opts) {
    var tr = res.map(function (x) {
      if (!x.r.ok) return "<tr><td>" + esc(x.factura) + '</td><td colspan="6"><span class="badge bad">error</span> ' + esc(x.r.errors.join(" ")) + "</td></tr>";
      var tramos = x.r.enPlazo ? "Pagada en plazo" : x.r.tramos.map(function (t) { return B.es(t.desde) + "–" + B.es(t.hasta) + ": " + t.dias + " d × " + d(t.tipo) + " % (" + (t.boe === "pactado" ? "pactado" : t.boe === "estimado" ? "estimado" : t.boe) + ") = " + d(t.interes) + " €"; }).join("<br>");
      return "<tr><td>" + esc(x.factura) + "</td><td>" + d(x.importe) + "</td><td>" + B.es(x.venc) + "</td><td>" + B.es(x.pago) + (x.hoy ? " (hoy)" : "") + "</td><td>" + (x.r.dias || 0) + "</td><td class=\"tramos\">" + tramos + "</td><td>" + d(x.interes) + (x.c40 ? " + 40,00" : "") + "</td></tr>";
    }).join("");
    return '<div class="table-wrap"><table class="detail"><thead><tr><th>Factura</th><th>Importe (€)</th><th>Vencimiento</th><th>Pago</th><th>Días</th><th>Tramos (tipo y BOE)</th><th>Intereses (€)</th></tr></thead><tbody>' + tr + "</tbody></table></div>";
  }
  function calc() {
    var out = $("dm-out"), resEl = $("dm-res"), hoy = B.todayUTC(), opts = { pactado: $("dm-pact").value.trim(), estimar: $("dm-est").checked };
    var res = [], tot = 0, n40 = 0, principal = 0, errs = [], est = false;
    rows().forEach(function (r, i) {
      if (!r.importe && !r.venc && !r.pago) return;
      var id = r.factura || "Fila " + (i + 1), pago = r.pago ? B.parseDate(r.pago) : hoy, venc = B.parseDate(r.venc);
      var x = B.interes(r.importe, venc, pago, opts), item = { factura: id, importe: B.parseAmount(r.importe), venc: venc, pago: pago, hoy: !r.pago, r: x, interes: 0, c40: false };
      if (!x.ok) errs.push(id + ": " + x.errors.join(" "));
      else { item.interes = x.interesRed || 0; tot += item.interes; principal += item.importe; if (!x.enPlazo && $("dm-40").checked) { item.c40 = true; n40++; } if (x.estimado) est = true; }
      res.push(item);
    });
    if (!res.length) { resEl.innerHTML = ""; U.statusBox(out, "warn", "Añade al menos una factura con importe y vencimiento."); out.focus(); return; }
    if (errs.length === res.length) { resEl.innerHTML = ""; last = null; U.statusBox(out, "bad", "No se ha podido calcular ninguna factura.", { errors: errs }); out.focus(); return; }
    last = { res: res, tot: tot, n40: n40, principal: principal, opts: opts };
    var total = tot + 40 * n40;
    var notes = ["Intereses: " + d(tot) + " €" + (n40 ? " · Compensación por costes de cobro: " + n40 + " × 40 € = " + d(40 * n40) + " € (art. 8.1 Ley 3/2004; por factura según TJUE C-585/20)" : "") + ".",
      opts.pactado ? "Tipo pactado aplicado: " + opts.pactado + " % anual (art. 7.1)." : "Tipo legal de cada semestre según su resolución del BOE (art. 7.2: BCE + 8 puntos).",
      "Interés simple, base 365; desde el día siguiente al vencimiento hasta el día del pago, ambos incluidos."];
    if (est) notes.push("Parte del periodo usa el último tipo publicado como estimación: el tipo del semestre siguiente aún no está en el BOE.");
    U.statusBox(out, errs.length ? "warn" : "ok", "Total a reclamar: " + d(total) + " € (además del principal pendiente)", { notes: notes, errors: errs });
    resEl.innerHTML = tablaRes(res) + '<div class="btns"><button class="btn" type="button" id="dm-print">Imprimir o guardar en PDF</button><button class="btn ghost" type="button" id="dm-dl">Descargar CSV</button></div>';
    $("dm-print").addEventListener("click", printIt);
    $("dm-dl").addEventListener("click", function () {
      var L = ["factura;importe;vencimiento;pago;dias;intereses;compensacion_40"];
      res.forEach(function (x) { L.push([x.factura, x.importe == null ? "" : d(x.importe).replace(/\./g, ""), x.venc == null ? "" : B.es(x.venc), x.pago == null ? "" : B.es(x.pago), x.r.dias || 0, d(x.interes).replace(/\./g, ""), x.c40 ? "40,00" : "0,00"].join(";")); });
      L.push(""); L.push("Total intereses;" + d(tot).replace(/\./g, "")); L.push("Total compensaciones;" + d(40 * n40)); L.push("Total;" + d(total).replace(/\./g, ""));
      U.download("intereses-demora.csv", "\ufeff" + L.join("\n") + "\n");
    });
    out.focus();
  }
  function printIt() {
    if (!last) return;
    var total = last.tot + 40 * last.n40;
    $("print-sheet").innerHTML = '<div class="print-doc"><h1>Liquidación de intereses de demora</h1><p>Ley 3/2004, de 29 de diciembre, arts. 5, 7 y 8. ' +
      (last.opts.pactado ? "Tipo pactado: " + esc(last.opts.pactado) + " % anual." : "Tipo legal de interés de demora publicado semestralmente en el BOE.") + "</p>" + tablaRes(last.res) +
      "<p><strong>Intereses: " + d(last.tot) + " €</strong>" + (last.n40 ? " · <strong>Compensación por costes de cobro: " + d(40 * last.n40) + " €</strong> (40 € por factura, art. 8.1; TJUE C-585/20)" : "") + " · <strong>Total: " + d(total) + " €</strong></p>" +
      '<p class="small">Generado el ' + B.es(B.todayUTC()) + " con la calculadora gratuita de " + esc(siteName()) + ". Orientativo; no es asesoramiento jurídico.</p></div>";
    document.body.classList.add("printing");
    var done = function () { document.body.classList.remove("printing"); window.removeEventListener("afterprint", done); };
    window.addEventListener("afterprint", done);
    window.print();
  }
  $("dm-go").addEventListener("click", calc);
})();
