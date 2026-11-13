/*! Calculadora de huella (hash SHA-256) Verifactu: alta, anulación y evento + comprobador de cadena */
(function () {
  "use strict";
  var VF = window.VF, U = window.UI, $ = U.$;
  if (!$("h-tabs")) return;
  var tipoActual = "alta";
  // pestañas
  var tabs = [].slice.call(document.querySelectorAll("#h-tabs [role=tab]"));
  function selTab(t) {
    tipoActual = t;
    tabs.forEach(function (b) { var on = b.getAttribute("data-tab") === t; b.setAttribute("aria-selected", on ? "true" : "false"); b.tabIndex = on ? 0 : -1; $("p-" + b.getAttribute("data-tab")).hidden = !on; });
  }
  tabs.forEach(function (b, i) {
    b.addEventListener("click", function () { selTab(b.getAttribute("data-tab")); });
    b.addEventListener("keydown", function (e) {
      var j = e.key === "ArrowRight" ? i + 1 : e.key === "ArrowLeft" ? i - 1 : -1;
      if (j < 0 && e.key !== "ArrowLeft") return;
      j = (j + tabs.length) % tabs.length; tabs[j].focus(); selTab(tabs[j].getAttribute("data-tab"));
    });
  });
  function valores(t) { return VF.FIELDS[t].map(function (_n, i) { return $("h-" + t + "-" + i).value; }); }
  function setValores(t, v) { v.forEach(function (x, i) { $("h-" + t + "-" + i).value = x; }); }
  var out = $("h-out"), lastHash = "";
  function calc(t, oficial) {
    var v = valores(t), r = VF.huella(t, v), w = VF.avisosHuella(t, v);
    lastHash = r.huella;
    var notes = [];
    if (oficial) notes.push(oficial === r.huella ? "Coincide exactamente con el resultado oficial del documento de la AEAT ✓" : "No coincide con el resultado oficial (" + oficial + ")");
    var html = '<p class="label mt8">Huella (SHA-256, hexadecimal en mayúsculas)</p><p class="hashout" id="h-hash" data-value="' + r.huella + '">' + r.huella + "</p>" +
      '<div class="btns mt8"><button type="button" class="btn small" data-copy="h-hash">Copiar huella</button><button type="button" class="btn small ghost" id="h-next">Usar como huella anterior del siguiente registro</button></div>' +
      '<p class="label">Cadena exacta sobre la que se calcula</p><p class="out" id="h-cad" data-value="' + VF.esc(r.cadena) + '">' + VF.esc(r.cadena) + "</p>" +
      '<div class="btns mt8"><button type="button" class="btn small ghost" data-copy="h-cad">Copiar cadena</button></div>';
    U.statusBox(out, w.length ? "warn" : "ok", "Huella del registro de " + (t === "alta" ? "alta" : t === "anulacion" ? "anulación" : "evento"), { warnings: w, notes: notes, html: html });
    $("h-next").addEventListener("click", function () {
      var idx = VF.FIELDS[t].indexOf(t === "evento" ? "HuellaEvento" : "Huella");
      $("h-" + t + "-" + idx).value = lastHash;
      var ts = VF.FIELDS[t].length - 1; $("h-" + t + "-" + ts).value = VF.ahoraMadrid();
      U.statusBox(out, "info", "Huella copiada al campo «huella anterior». Cambia los datos del nuevo registro y vuelve a calcular.");
      $("h-" + t + "-0").focus();
    });
    return r;
  }
  ["alta", "anulacion", "evento"].forEach(function (t) {
    $("h-form-" + t).addEventListener("submit", function (e) { e.preventDefault(); calc(t); out.focus(); });
    var now = $("h-now-" + t);
    if (now) now.addEventListener("click", function () { $("h-" + t + "-" + (VF.FIELDS[t].length - 1)).value = VF.ahoraMadrid(); });
  });
  // ejemplos oficiales de la AEAT
  VF.EJEMPLOS.forEach(function (ej, i) {
    var b = $("h-ex" + (i + 1));
    if (b) b.addEventListener("click", function () { selTab(ej.tipo); setValores(ej.tipo, ej.valores); calc(ej.tipo, ej.huella); out.focus(); });
  });
  var bev = $("h-ex-ev");
  if (bev) bev.addEventListener("click", function () {
    selTab("evento");
    setValores("evento", ["89890001K", "", "77", "1.0.03", "383", "89890001K", "01", "", "2024-01-01T19:20:30+01:00"]);
    calc("evento");
  });

  // --- comprobador de cadena ---
  var cres = $("c-res");
  function ejemploXml() {
    var e = VF.EJEMPLOS, ns = 'xmlns:sf="' + VF.NS_SF + '"';
    function alta(v, primero, prevNum) {
      return "  <sf:RegistroAlta>\n    <sf:IDVersion>1.0</sf:IDVersion>\n    <sf:IDFactura><sf:IDEmisorFactura>" + v[0] + "</sf:IDEmisorFactura><sf:NumSerieFactura>" + v[1] + "</sf:NumSerieFactura><sf:FechaExpedicionFactura>" + v[2] + "</sf:FechaExpedicionFactura></sf:IDFactura>\n" +
        "    <sf:TipoFactura>" + v[3] + "</sf:TipoFactura>\n    <sf:CuotaTotal>" + v[4] + "</sf:CuotaTotal>\n    <sf:ImporteTotal>" + v[5] + "</sf:ImporteTotal>\n" +
        "    <sf:Encadenamiento>" + (primero ? "<sf:PrimerRegistro>S</sf:PrimerRegistro>" : "<sf:RegistroAnterior><sf:IDEmisorFactura>" + v[0] + "</sf:IDEmisorFactura><sf:NumSerieFactura>" + prevNum + "</sf:NumSerieFactura><sf:FechaExpedicionFactura>" + v[2] + "</sf:FechaExpedicionFactura><sf:Huella>" + v[6] + "</sf:Huella></sf:RegistroAnterior>") + "</sf:Encadenamiento>\n" +
        "    <sf:FechaHoraHusoGenRegistro>" + v[7] + "</sf:FechaHoraHusoGenRegistro>\n    <sf:TipoHuella>01</sf:TipoHuella>\n    <sf:Huella>" + VF.huella("alta", v).huella + "</sf:Huella>\n  </sf:RegistroAlta>\n";
    }
    var an = e[2].valores;
    return "<!-- Ejemplo simplificado: solo los campos que intervienen en la huella (ejemplos oficiales de la AEAT) -->\n<Registros " + ns + ">\n" +
      alta(e[0].valores, true) + alta(e[1].valores, false, e[0].valores[1]) +
      "  <sf:RegistroAnulacion>\n    <sf:IDVersion>1.0</sf:IDVersion>\n    <sf:IDFactura><sf:IDEmisorFacturaAnulada>" + an[0] + "</sf:IDEmisorFacturaAnulada><sf:NumSerieFacturaAnulada>" + an[1] + "</sf:NumSerieFacturaAnulada><sf:FechaExpedicionFacturaAnulada>" + an[2] + "</sf:FechaExpedicionFacturaAnulada></sf:IDFactura>\n" +
      "    <sf:Encadenamiento><sf:RegistroAnterior><sf:IDEmisorFactura>" + an[0] + "</sf:IDEmisorFactura><sf:NumSerieFactura>" + an[1] + "</sf:NumSerieFactura><sf:FechaExpedicionFactura>" + an[2] + "</sf:FechaExpedicionFactura><sf:Huella>" + an[3] + "</sf:Huella></sf:RegistroAnterior></sf:Encadenamiento>\n" +
      "    <sf:FechaHoraHusoGenRegistro>" + an[4] + "</sf:FechaHoraHusoGenRegistro>\n    <sf:TipoHuella>01</sf:TipoHuella>\n    <sf:Huella>" + e[2].huella + "</sf:Huella>\n  </sf:RegistroAnulacion>\n</Registros>\n";
  }
  function checkChain() {
    var r = VF.checkChain($("c-xml").value);
    if (r.error) { U.statusBox(cres, "bad", r.error); return r; }
    var tr = r.rows.map(function (x) {
      var st = x.problemas.length ? '<span class="badge bad">Error</span>' : x.avisos.length ? '<span class="badge warn">Aviso</span>' : '<span class="badge ok">Correcto</span>';
      var msgs = x.problemas.concat(x.avisos).map(function (m) { return "<li>" + VF.esc(m) + "</li>"; }).join("");
      return "<tr><td>" + x.n + "</td><td>" + (x.tipo === "alta" ? "Alta" : x.tipo === "anulacion" ? "Anulación" : "Evento") + "<br><span class=\"mono\">" + VF.esc(x.id || "") + "</span></td><td>" + st + (msgs ? '<ul class="steps-small">' + msgs + "</ul>" : "") +
        '</td><td class="mono">' + VF.esc(x.guardada || "—") + (x.guardada && x.guardada !== x.calculada ? "<br>calculada: " + x.calculada : "") + "</td></tr>";
    }).join("");
    var table = '<div class="table-wrap"><table class="chain-table"><thead><tr><th>#</th><th>Registro</th><th>Resultado</th><th>Huella</th></tr></thead><tbody>' + tr + "</tbody></table></div>";
    var nErr = r.rows.filter(function (x) { return x.problemas.length; }).length;
    U.statusBox(cres, r.ok ? "ok" : "bad", r.ok ? "Cadena correcta: " + r.rows.length + " registro(s) con huella y encadenamiento válidos" : nErr + " de " + r.rows.length + " registro(s) con errores", { html: table });
    return r;
  }
  $("c-form").addEventListener("submit", function (e) { e.preventDefault(); checkChain(); cres.focus(); });
  $("c-ex").addEventListener("click", function () { $("c-xml").value = ejemploXml(); checkChain(); });
  $("c-ex-bad").addEventListener("click", function () { $("c-xml").value = ejemploXml().replace("<sf:CuotaTotal>12.35</sf:CuotaTotal>", "<sf:CuotaTotal>12.36</sf:CuotaTotal>"); checkChain(); });
  U.dropZone($("c-drop"), $("c-file"), function (files) {
    U.readFile(files[0], true).then(function (t) { $("c-xml").value = t; checkChain(); cres.focus(); }, function () { U.statusBox(cres, "bad", "No se ha podido leer el archivo."); });
  });
  window.VFH = { calc: calc, checkChain: checkChain, ejemploXml: ejemploXml };
})();
