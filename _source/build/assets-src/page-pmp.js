/*! Calculadora del periodo medio de pago a proveedores – Resolución ICAC de 29/01/2016 (BOE-A-2016-1112) */
(function () {
  "use strict";
  var U = window.UI, B = window.B2B, K = window.VF, $ = U.$;
  if (!$("pmp-rows") || !B) return;
  var esc = K.esc, fmt = B.fmt;
  function siteName() { var m = document.querySelector('meta[property="og:site_name"]'); return m ? m.content : ""; }

  // pestañas
  var tabs = [].slice.call(document.querySelectorAll("#pmp-tabs [role=tab]"));
  function selTab(t) { tabs.forEach(function (b) { var on = b.getAttribute("data-tab") === t; b.setAttribute("aria-selected", on ? "true" : "false"); b.tabIndex = on ? 0 : -1; $("p-" + b.getAttribute("data-tab")).hidden = !on; }); }
  tabs.forEach(function (b, i) {
    b.addEventListener("click", function () { selTab(b.getAttribute("data-tab")); });
    b.addEventListener("keydown", function (e) {
      var j = e.key === "ArrowRight" ? i + 1 : e.key === "ArrowLeft" ? i - 1 : null; if (j === null) return;
      e.preventDefault(); j = (j + tabs.length) % tabs.length; tabs[j].focus(); selTab(tabs[j].getAttribute("data-tab"));
    });
  });

  var tbody = $("pmp-rows");
  function toIso(s) { var t = B.parseDate(s); return t == null ? "" : B.iso(t); }
  function renumber() { [].forEach.call(tbody.rows, function (tr, i) { tr.cells[0].textContent = i + 1; [].forEach.call(tr.querySelectorAll("input"), function (inp) { inp.setAttribute("aria-label", inp.getAttribute("data-l") + ", fila " + (i + 1)); }); }); }
  function addRow(r) {
    r = r || {};
    var tr = document.createElement("tr");
    tr.innerHTML = "<td></td>" +
      '<td data-h="Factura"><input type="text" class="w-s" data-k="factura" data-l="Factura" autocomplete="off"></td>' +
      '<td data-h="Proveedor"><input type="text" class="w-m" data-k="proveedor" data-l="Proveedor" autocomplete="off"></td>' +
      '<td data-h="Importe (€)"><input type="text" class="w-s" data-k="importe" data-l="Importe" inputmode="decimal" autocomplete="off"></td>' +
      '<td data-h="Inicio del cómputo"><input type="date" data-k="inicio" data-l="Inicio del cómputo"></td>' +
      '<td data-h="Fecha de pago (vacía = pendiente)"><input type="date" data-k="pago" data-l="Fecha de pago"></td>' +
      '<td><button type="button" class="btn ghost small del" aria-label="Quitar fila">✕</button></td>';
    tr.querySelector('[data-k="factura"]').value = r.factura || "";
    tr.querySelector('[data-k="proveedor"]').value = r.proveedor || "";
    tr.querySelector('[data-k="importe"]').value = r.importe || "";
    tr.querySelector('[data-k="inicio"]').value = r.inicio ? toIso(r.inicio) : "";
    tr.querySelector('[data-k="pago"]').value = r.pago ? toIso(r.pago) : "";
    tbody.appendChild(tr); renumber();
    return tr;
  }
  tbody.addEventListener("click", function (e) {
    var b = e.target.closest && e.target.closest("button.del"); if (!b) return;
    b.closest("tr").remove(); if (!tbody.rows.length) addRow(); renumber();
  });
  function readRows() {
    return [].map.call(tbody.rows, function (tr) {
      var o = {}; [].forEach.call(tr.querySelectorAll("input"), function (i) { o[i.getAttribute("data-k")] = i.value; }); return o;
    });
  }
  function clear() { tbody.innerHTML = ""; }
  function loadRows(rows) {
    var cur = readRows().filter(function (r) { return r.importe || r.inicio || r.pago || r.factura; });
    clear(); cur.concat(rows).forEach(addRow); if (!tbody.rows.length) addRow();
  }
  var EJ = [
    { factura: "A-1", proveedor: "Suministros Norte", importe: "1.000,00", inicio: "2025-01-10", pago: "2025-02-09" },
    { factura: "A-2", proveedor: "Transportes Sur", importe: "2.000,00", inicio: "2025-03-01", pago: "2025-05-10" },
    { factura: "A-3", proveedor: "Papelería Centro", importe: "500,00", inicio: "2025-11-15", pago: "" },
    { factura: "A-4", proveedor: "Servicios IT", importe: "1.500,00", inicio: "2025-12-01", pago: "2026-01-20" }];
  for (var i = 0; i < 3; i++) addRow();
  $("pmp-add").addEventListener("click", function () { addRow().querySelector("input").focus(); });
  $("pmp-clear").addEventListener("click", function () { clear(); addRow(); addRow(); addRow(); U.statusBox($("pmp-out"), null); $("pmp-res").innerHTML = ""; });
  $("pmp-ex").addEventListener("click", function () { clear(); EJ.forEach(addRow); $("pmp-ap").value = "2025-01-01"; $("pmp-cierre").value = "2025-12-31"; calc(); });
  $("pmp-tpl").addEventListener("click", function () {
    U.download("plantilla-periodo-medio-pago.csv", "\ufefffactura;proveedor;importe;fecha_inicio;fecha_pago\nA-1;Suministros Norte;1.000,00;10/01/2025;09/02/2025\nA-3;Papelería Centro;500,00;15/11/2025;\n");
  });
  function importText(text, origin) {
    var r = B.pmpRowsFromCsv(text);
    if (!r.rows.length) { U.statusBox($("pmp-out"), "warn", "No he encontrado filas en " + origin + "."); return; }
    loadRows(r.rows);
    U.statusBox($("pmp-out"), "info", r.rows.length + " fila(s) añadidas desde " + origin + ". Revisa la tabla y pulsa «Calcular PMP».", { warnings: r.warnings });
  }
  U.dropZone($("pmp-drop"), $("pmp-csv"), function (files) { U.readFile(files[0], true).then(function (t) { importText(t, "el archivo «" + files[0].name + "»"); }); });
  $("pmp-paste-go").addEventListener("click", function () { var t = $("pmp-paste").value; if (t.trim()) { importText(t, "el texto pegado"); $("pmp-paste").value = ""; } });

  var last = null;
  function d(x) { return fmt(x, 2); }
  function memoriaTable(r) {
    var n1 = B.parseAmount($("pmp-n1").value), n1s = n1 == null ? "—" : d(n1);
    return '<div class="table-wrap"><table class="memoria"><caption>Información sobre el periodo medio de pago a proveedores. Disposición adicional tercera. «Deber de información» de la Ley 15/2010, de 5 de julio</caption>' +
      "<thead><tr><th></th><th>N (ejercicio actual)</th><th>N-1 (ejercicio anterior)</th></tr></thead><tbody>" +
      '<tr><th colspan="3" class="sub">Días</th></tr>' +
      "<tr><td>Periodo medio de pago a proveedores</td><td>" + d(r.pmp) + "</td><td>" + n1s + "</td></tr>" +
      "<tr><td>Ratio de operaciones pagadas</td><td>" + d(r.pagadas.ratio) + "</td><td>—</td></tr>" +
      "<tr><td>Ratio de operaciones pendientes de pago</td><td>" + d(r.pendientes.ratio) + "</td><td>—</td></tr>" +
      '<tr><th colspan="3" class="sub">Importe (euros)</th></tr>' +
      "<tr><td>Total pagos realizados</td><td>" + d(r.pagadas.importe) + "</td><td>—</td></tr>" +
      "<tr><td>Total pagos pendientes</td><td>" + d(r.pendientes.importe) + "</td><td>—</td></tr>" +
      "</tbody></table></div>";
  }
  function extraTable(r) {
    return '<div class="table-wrap"><table><caption>Facturas pagadas dentro del plazo máximo legal (≤ ' + r.limite + " días) · DA 3.ª Ley 15/2010</caption>" +
      "<thead><tr><th></th><th>Número</th><th>Importe (€)</th></tr></thead><tbody>" +
      "<tr><td>Pagadas en plazo</td><td>" + r.dentro.n + "</td><td>" + d(r.dentro.importe) + "</td></tr>" +
      "<tr><td>Total pagadas en el ejercicio</td><td>" + r.pagadas.n + "</td><td>" + d(r.pagadas.importe) + "</td></tr>" +
      "<tr><td>Porcentaje</td><td>" + d(r.dentro.pctN) + " %</td><td>" + d(r.dentro.pctImporte) + " %</td></tr></tbody></table></div>";
  }
  function detailTable(r) {
    var tr = r.detail.map(function (x) {
      var st = x.estado === "pagada" ? '<span class="badge ' + (x.dias > r.limite ? "warn" : "ok") + '">pagada</span>' : x.estado === "pendiente" ? '<span class="badge info">pendiente' + (x.nota ? " (" + x.nota + ")" : "") + "</span>" : '<span class="badge bad">omitida</span>';
      return "<tr><td>" + x.n + "</td><td>" + esc(x.factura) + "</td><td>" + esc(x.proveedor) + "</td><td>" + (x.importe == null ? "—" : d(x.importe)) + "</td><td>" + (x.inicio == null ? "—" : B.es(x.inicio)) + "</td><td>" + (x.pago == null ? "—" : B.es(x.pago)) + "</td><td>" + st + "</td><td>" + (x.dias == null ? "—" : x.dias) + "</td></tr>";
    }).join("");
    return '<div class="table-wrap"><table class="detail"><caption>Detalle por factura</caption><thead><tr><th>#</th><th>Factura</th><th>Proveedor</th><th>Importe</th><th>Inicio</th><th>Pago</th><th>Situación al cierre</th><th>Días</th></tr></thead><tbody>' + tr + "</tbody></table></div>";
  }
  function calc() {
    var out = $("pmp-out"), res = $("pmp-res");
    var r = B.pmp(readRows(), { cierre: $("pmp-cierre").value, apertura: $("pmp-ap").value, limite: +$("pmp-lim").value });
    last = r;
    if (!r.ok) { res.innerHTML = ""; U.statusBox(out, "bad", r.errors.join(" "), { warnings: r.warnings }); out.focus(); return; }
    var head = "PMP: " + d(r.pmp) + " días · " + (r.supera ? "supera el máximo legal de 60 días" : "dentro del máximo legal de 60 días");
    var notes = ["Ratio de operaciones pagadas: " + d(r.pagadas.ratio) + " días (" + r.pagadas.n + " facturas, " + d(r.pagadas.importe) + " €).",
      "Ratio de operaciones pendientes de pago: " + d(r.pendientes.ratio) + " días (" + r.pendientes.n + " facturas, " + d(r.pendientes.importe) + " €).",
      "Pagadas en ≤ " + r.limite + " días: " + r.dentro.n + " de " + r.pagadas.n + " (" + d(r.dentro.pctN) + " % del número y " + d(r.dentro.pctImporte) + " % del importe pagado)."];
    var over = r.detail.filter(function (x) { return x.estado === "pagada" && x.dias > r.limite; }).length;
    if (over) notes.push(over + " factura(s) pagadas en más de " + r.limite + " días: revisa los intereses de demora que pueden reclamarte.");
    U.statusBox(out, r.supera ? "warn" : "ok", head, { notes: notes, warnings: r.warnings });
    res.innerHTML = '<h3 class="mt14">Cuadro para la memoria (art. 6.1 de la resolución)</h3>' + memoriaTable(r) + extraTable(r) + detailTable(r) +
      '<div class="btns"><button class="btn" type="button" id="pmp-print">Imprimir o guardar en PDF</button><button class="btn ghost" type="button" id="pmp-dl">Descargar resultado (CSV)</button><button class="btn ghost" type="button" data-copy="pmp-copytext">Copiar cuadro</button></div>' +
      '<p id="pmp-copytext" class="sr-only"></p>';
    $("pmp-copytext").textContent = ["Periodo medio de pago a proveedores\t" + d(r.pmp), "Ratio de operaciones pagadas\t" + d(r.pagadas.ratio), "Ratio de operaciones pendientes de pago\t" + d(r.pendientes.ratio), "Total pagos realizados\t" + d(r.pagadas.importe), "Total pagos pendientes\t" + d(r.pendientes.importe)].join("\n");
    $("pmp-print").addEventListener("click", printIt);
    $("pmp-dl").addEventListener("click", function () {
      var lines = ["factura;proveedor;importe;fecha_inicio;fecha_pago;situacion;dias"];
      r.detail.forEach(function (x) { lines.push([x.factura, x.proveedor, x.importe == null ? "" : d(x.importe).replace(/\./g, ""), x.inicio == null ? "" : B.es(x.inicio), x.pago == null ? "" : B.es(x.pago), x.estado, x.dias == null ? "" : x.dias].map(function (v) { v = String(v); return /[;"\n]/.test(v) ? '"' + v.replace(/"/g, '""') + '"' : v; }).join(";")); });
      lines.push(""); lines.push("PMP;" + d(r.pmp)); lines.push("Ratio pagadas;" + d(r.pagadas.ratio)); lines.push("Ratio pendientes;" + d(r.pendientes.ratio));
      lines.push("Total pagos realizados;" + d(r.pagadas.importe).replace(/\./g, "")); lines.push("Total pagos pendientes;" + d(r.pendientes.importe).replace(/\./g, ""));
      U.download("periodo-medio-pago-" + $("pmp-cierre").value + ".csv", "\ufeff" + lines.join("\n") + "\n");
    });
    out.focus();
  }
  function printIt() {
    if (!last || !last.ok) return;
    var soc = $("pmp-soc").value.trim(), ap = $("pmp-ap").value, ci = $("pmp-cierre").value;
    var sheet = $("print-sheet");
    sheet.innerHTML = '<div class="print-doc"><h1>Periodo medio de pago a proveedores' + (soc ? " – " + esc(soc) : "") + "</h1>" +
      "<p>Ejercicio " + (ap ? B.es(B.parseDate(ap)) + " – " : "hasta ") + B.es(B.parseDate(ci)) + ". Método: Resolución del ICAC de 29 de enero de 2016 (BOE-A-2016-1112), art. 5.1 a 5.4 (memoria normal).</p>" +
      memoriaTable(last) + extraTable(last) + detailTable(last) +
      "<p class=\"small\">Generado el " + B.es(B.todayUTC()) + " con la calculadora gratuita de " + esc(siteName()) + ". Cálculo realizado en el navegador; orientativo.</p></div>";
    document.body.classList.add("printing");
    var done = function () { document.body.classList.remove("printing"); window.removeEventListener("afterprint", done); };
    window.addEventListener("afterprint", done);
    window.print();
  }
  $("pmp-go").addEventListener("click", calc);

  // modelo abreviado
  var abf = $("ab-form"), abo = $("ab-out");
  abf.addEventListener("submit", function (e) {
    e.preventDefault();
    var sm = B.saldoMedio($("ab-ini").value, $("ab-fin").value);
    if (sm == null) { U.statusBox(abo, "bad", "Introduce el saldo inicial y el saldo final de acreedores comerciales."); abo.focus(); return; }
    var r = B.pmpAbreviado(sm, $("ab-com").value);
    if (!r.ok) { U.statusBox(abo, "bad", r.errors.join(" ")); abo.focus(); return; }
    U.statusBox(abo, r.supera ? "warn" : "ok", "PMP (modelo abreviado): " + d(r.pmp) + " días · " + (r.supera ? "supera los 60 días" : "dentro de los 60 días"),
      { notes: ["Saldo medio de acreedores comerciales: " + d(sm) + " €.", "Cálculo: " + d(sm) + " ÷ " + d(B.parseAmount($("ab-com").value)) + " × 365 = " + d(r.pmp) + " días (art. 5.5).", "En la memoria abreviada solo se informa del PMP, para N y N-1 (art. 6.3)."] });
    abo.focus();
  });
  $("ab-ex").addEventListener("click", function () { $("ab-ini").value = "40.000,00"; $("ab-fin").value = "60.000,00"; $("ab-com").value = "400.000,00"; abf.requestSubmit ? abf.requestSubmit() : abf.dispatchEvent(new Event("submit")); });
})();
