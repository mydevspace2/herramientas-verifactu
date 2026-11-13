/*! Generador de QR tributario Verifactu con vista previa de impresión en milímetros */
(function () {
  "use strict";
  var VF = window.VF, U = window.UI, Q = window.QR, $ = U.$;
  var form = $("q-form");
  if (!form) return;
  var last = null; // { url, qr, opts }
  function radio(name) { var r = form.querySelector('input[name="' + name + '"]:checked'); return r ? r.value : ""; }
  function num(id, def) { var v = parseFloat($(id).value); return isFinite(v) ? v : def; }
  var PT = 25.4 / 72; // 1 punto tipográfico en mm
  var CH = 0.55;      // anchura media de un carácter (en em) para Arial – estimación prudente

  function wrap(text, fontMm, maxW) {
    var words = text.split(" "), lines = [], cur = "";
    words.forEach(function (w) {
      var t = cur ? cur + " " + w : w;
      if (cur && t.length * fontMm * CH > maxW) { lines.push(cur); cur = w; } else cur = t;
    });
    if (cur) lines.push(cur);
    return lines;
  }
  function f2(n) { return (Math.round(n * 100) / 100).toString(); }
  // Devuelve el bloque «QR tributario:» + QR + leyenda como SVG en milímetros
  function labelSvg(o) {
    var qr = o.qr, n = qr.size, size = o.size, m = o.margin, font = o.pt * PT;
    var caption = o.verifactu ? (o.caption === "larga" ? "Factura verificable en la sede electrónica de la AEAT" : "VERI*FACTU") : "";
    var minW = size + 2 * m;
    var capLines = caption ? wrap(caption, font, Math.max(minW, 30)) : [];
    var labelW = "QR tributario:".length * font * CH;
    var capW = capLines.reduce(function (a, l) { return Math.max(a, l.length * font * CH); }, 0);
    var W = Math.max(minW, labelW + 2, capW + 2);
    var lh = font * 1.25, pad = 1;
    var yLabel = pad + font * 0.95;
    var qrY = pad + lh + m, qrX = (W - size) / 2;
    var H = qrY + size + m + capLines.length * lh + (capLines.length ? pad : 0);
    var ms = size / n, d = "";
    for (var y = 0; y < n; y++) for (var x = 0; x < n; x++) if (qr.modules[y][x]) d += "M" + x + " " + y + "h1v1h-1z";
    var s = '<svg xmlns="http://www.w3.org/2000/svg"' + (o.realSize ? ' width="' + f2(W) + 'mm" height="' + f2(H) + 'mm"' : "") +
      ' viewBox="0 0 ' + f2(W) + " " + f2(H) + '" role="img" aria-label="QR tributario ' + (o.verifactu ? "VERI*FACTU" : "") + '">' +
      '<rect width="' + f2(W) + '" height="' + f2(H) + '" fill="#fff"/>' +
      '<text x="' + f2(W / 2) + '" y="' + f2(yLabel) + '" font-family="Arial, Helvetica, sans-serif" font-size="' + f2(font) + '" text-anchor="middle" fill="#000">QR tributario:</text>' +
      '<g transform="translate(' + f2(qrX) + " " + f2(qrY) + ") scale(" + (ms) + ')"><path d="' + d + '" fill="#000" shape-rendering="crispEdges"/></g>';
    capLines.forEach(function (l, i) {
      s += '<text x="' + f2(W / 2) + '" y="' + f2(qrY + size + m + font * 0.95 + i * lh) + '" font-family="Arial, Helvetica, sans-serif" font-size="' + f2(font) + '" text-anchor="middle" fill="#000">' + VF.esc(l) + "</text>";
    });
    s += "</svg>";
    return { svg: s, W: W, H: H, moduleMm: ms };
  }
  var PAPERS = { t57: { w: 57, name: "tique de 57 mm" }, t80: { w: 80, name: "tique de 80 mm" }, a4: { w: 210, name: "DIN A4 vertical" } };
  function previewSvg(o, lab) {
    var p = PAPERS[o.paper] || PAPERS.a4, W = p.w, top = o.paper === "a4" ? 12 : 4;
    var x = (W - lab.W) / 2, H = top + lab.H + (o.paper === "a4" ? 60 : 40);
    var inner = lab.svg.replace(/^<svg[^>]*>/, "").replace(/<\/svg>$/, "");
    var s = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ' + W + " " + f2(H) + '" class="paper-svg" role="img" aria-label="Vista previa: ' + p.name + '">' +
      '<rect width="' + W + '" height="' + f2(H) + '" fill="#fff"/>';
    // regla en milímetros (cada 10 mm)
    for (var mm = 0; mm <= W; mm += 5) s += '<line x1="' + mm + '" y1="0" x2="' + mm + '" y2="' + (mm % 10 ? 1 : 2) + '" stroke="#9aa4b2" stroke-width="0.2"/>';
    s += '<g transform="translate(' + f2(x) + " " + top + ')">' + inner + "</g>";
    if (o.paper === "a4") {
      s += '<rect x="12" y="' + top + '" width="' + f2(Math.max(10, x - 18)) + '" height="' + f2(lab.H) + '" fill="#eef2f7" stroke="#c3cedd" stroke-width="0.3"/>';
      s += '<text x="' + f2(12 + Math.max(10, x - 18) / 2) + '" y="' + f2(top + lab.H / 2) + '" font-size="3.2" text-anchor="middle" fill="#64748b" font-family="Arial">Emisor / logotipo</text>';
      s += '<rect x="' + f2(x + lab.W + 6) + '" y="' + top + '" width="' + f2(Math.max(10, W - 12 - (x + lab.W + 6))) + '" height="' + f2(lab.H) + '" fill="#eef2f7" stroke="#c3cedd" stroke-width="0.3"/>';
      s += '<text x="' + f2(x + lab.W + 6 + Math.max(10, W - 12 - (x + lab.W + 6)) / 2) + '" y="' + f2(top + lab.H / 2) + '" font-size="3.2" text-anchor="middle" fill="#64748b" font-family="Arial">Destinatario</text>';
    }
    var y0 = top + lab.H + 6, mx = o.paper === "a4" ? 12 : 3;
    for (var i = 0; i < 6; i++) s += '<rect x="' + mx + '" y="' + f2(y0 + i * 6) + '" width="' + f2((W - 2 * mx) * (i % 3 === 2 ? 0.6 : 1)) + '" height="2.4" rx="0.6" fill="#e2e8f0"/>';
    s += '<text x="' + f2(W / 2) + '" y="' + f2(y0 + 40) + '" font-size="3" text-anchor="middle" fill="#94a3b8" font-family="Arial">contenido de la factura</text>';
    s += "</svg>";
    return { svg: s, W: W, H: H };
  }

  function generate(focus) {
    var o = {
      nif: $("q-nif").value, numserie: $("q-ns").value, fecha: $("q-fecha").value, importe: $("q-imp").value,
      verifactu: radio("modo") !== "no", entorno: radio("entorno") || "produccion",
      size: Math.min(40, Math.max(30, num("q-size", 35))), margin: Math.max(2, num("q-margin", 4)), pt: Math.max(6, num("q-pt", 9)),
      caption: radio("leyenda") || "corta", paper: $("q-paper").value
    };
    var r = VF.buildQrUrl(o), res = $("q-res");
    var errs = r.errors.map(function (e) { return (e.code ? "[" + e.code + "] " : "") + e.msg; });
    if (!r.ok) {
      U.statusBox(res, "bad", "Revisa los datos de la factura", { errors: errs, warnings: r.warnings });
      ["q-svg", "q-png", "q-print", "q-copy"].forEach(function (id) { $(id).disabled = true; });
      $("q-preview").innerHTML = ""; $("q-url").textContent = "La URL aparecerá aquí."; $("q-url").classList.add("placeholder");
      last = null; if (focus) res.focus(); return;
    }
    var qr = Q.encode(r.url, "M");
    o.qr = qr;
    var lab = labelSvg(o);
    var notes = ["Código QR versión " + qr.version + " (" + qr.size + "×" + qr.size + " módulos), corrección de errores nivel M.",
      "Cada módulo mide " + lab.moduleMm.toFixed(2).replace(".", ",") + " mm; el bloque completo mide " + lab.W.toFixed(1).replace(".", ",") + " × " + lab.H.toFixed(1).replace(".", ",") + " mm."];
    var warns = r.warnings.slice();
    if (o.margin < 4 * lab.moduleMm) warns.push("Margen de " + o.margin + " mm: cumple el mínimo de la AEAT (2 mm), pero es menor que 4 módulos (" + (4 * lab.moduleMm).toFixed(1).replace(".", ",") + " mm), lo recomendado por la norma ISO. La AEAT recomienda 6 mm.");
    if (!o.verifactu) notes.push("Sistema «No VERI*FACTU»: debajo del QR no va la frase «VERI*FACTU».");
    if (lab.W > (PAPERS[o.paper] || PAPERS.a4).w - 2) warns.push("El bloque es más ancho que el papel elegido: reduce el tamaño, el margen o la letra.");
    U.statusBox(res, warns.length ? "warn" : "ok", "QR tributario generado", { warnings: warns, notes: notes });
    $("q-url").textContent = r.url; $("q-url").classList.remove("placeholder"); $("q-url").setAttribute("data-value", r.url);
    var pv = previewSvg(o, lab);
    $("q-preview").innerHTML = pv.svg;
    var svgEl = $("q-preview").querySelector("svg");
    var real = $("q-real").checked;
    $("q-preview").classList.toggle("real", real);
    if (real) { svgEl.setAttribute("width", pv.W + "mm"); svgEl.setAttribute("height", f2(pv.H) + "mm"); }
    ["q-svg", "q-png", "q-print", "q-copy"].forEach(function (id) { $(id).disabled = false; });
    last = { url: r.url, o: o, lab: lab, params: r.params };
    if (focus) res.focus();
  }
  form.addEventListener("submit", function (e) { e.preventDefault(); generate(true); });
  form.addEventListener("change", function () { if (last) generate(false); });
  $("q-ex").addEventListener("click", function () {
    $("q-nif").value = "89890001K"; $("q-ns").value = "12345678-G33"; $("q-fecha").value = "2024-09-01"; $("q-imp").value = "241,40";
    form.querySelector('input[name="entorno"][value="pruebas"]').checked = true;
    generate(true);
  });
  function fileBase() { return "qr-tributario-" + (last ? last.params.numserie.replace(/[^A-Za-z0-9\-_]+/g, "_") : "factura"); }
  $("q-svg").addEventListener("click", function () {
    if (!last) return;
    var o = Object.assign({}, last.o, { realSize: true });
    U.download(fileBase() + ".svg", '<?xml version="1.0" encoding="UTF-8"?>\n' + labelSvg(o).svg, "image/svg+xml;charset=utf-8");
  });
  $("q-png").addEventListener("click", function () {
    if (!last) return;
    var dpi = 600, lab = labelSvg(Object.assign({}, last.o, { realSize: true }));
    var w = Math.round(lab.W / 25.4 * dpi), h = Math.round(lab.H / 25.4 * dpi);
    var img = new Image();
    img.onload = function () {
      var c = document.createElement("canvas"); c.width = w; c.height = h;
      var ctx = c.getContext("2d"); ctx.fillStyle = "#fff"; ctx.fillRect(0, 0, w, h); ctx.imageSmoothingEnabled = false;
      ctx.drawImage(img, 0, 0, w, h);
      c.toBlob(function (b) { U.download(fileBase() + "-600ppp.png", b, "image/png"); }, "image/png");
    };
    img.src = "data:image/svg+xml;charset=utf-8," + encodeURIComponent(lab.svg.replace(/ width="[^"]*mm" height="[^"]*mm"/, ' width="' + w + '" height="' + h + '"'));
  });
  $("q-print").addEventListener("click", function () {
    if (!last) return;
    var sheet = $("print-sheet");
    sheet.innerHTML = labelSvg(Object.assign({}, last.o, { realSize: true })).svg;
    document.body.classList.add("printing");
    var done = function () { document.body.classList.remove("printing"); window.removeEventListener("afterprint", done); };
    window.addEventListener("afterprint", done);
    window.print();
    setTimeout(done, 1500);
  });
  $("q-real").addEventListener("change", function () { if (last) generate(false); });
  // valores iniciales
  if (!$("q-fecha").value) { var t = new Date(); $("q-fecha").value = t.getFullYear() + "-" + ("0" + (t.getMonth() + 1)).slice(-2) + "-" + ("0" + t.getDate()).slice(-2); }
  window.VFQR = { labelSvg: labelSvg };
})();
