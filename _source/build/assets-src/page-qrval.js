/*! Validador y lector de QR Verifactu: URL pegada, imagen o cámara */
(function () {
  "use strict";
  var VF = window.VF, U = window.UI, $ = U.$;
  var form = $("v-form");
  if (!form) return;
  var res = $("v-res");
  var EJ = {
    ok: "https://www2.agenciatributaria.gob.es/wlpl/TIKE-CONT/ValidarQR?nif=89890001K&numserie=12345678-G33&fecha=01-09-2024&importe=241.4",
    amp: "https://www2.agenciatributaria.gob.es/wlpl/TIKE-CONT/ValidarQR?nif=89890001K&numserie=12345678&G33&fecha=01-01-2024&importe=7,2",
    bad: "http://www2.agenciatributaria.gob.es.validar-factura.example/wlpl/TIKE-CONT/ValidarQR?nif=89890001K&numserie=12345678-G33&fecha=01-09-2024&importe=241.4"
  };
  function show(url, origen) {
    var r = VF.parseQrUrl(url);
    var errs = r.errors.map(function (e) { return (e.code ? "[" + e.code + "] " : "") + e.msg; });
    var rows = [];
    var P = r.params;
    if (r.entorno) rows.push(["Entorno", r.entorno === "produccion" ? "Producción (www2.agenciatributaria.gob.es)" : "Pruebas (prewww2.aeat.es)"]);
    if (r.verifactu != null) rows.push(["Tipo de sistema", r.verifactu ? "VERI*FACTU (ValidarQR)" : "No VERI*FACTU (ValidarQRNoVerifactu)"]);
    [["nif", "NIF del emisor"], ["numserie", "Serie y número"], ["fecha", "Fecha de expedición"], ["importe", "Importe total"]].forEach(function (k) {
      if (P[k[0]] != null) rows.push([k[1], '<span class="mono">' + VF.esc(P[k[0]]) + "</span>"]);
    });
    var html = (origen ? '<p class="hint">Leído de: ' + VF.esc(origen) + "</p>" : "") + '<p class="mono mt8 mb0">' + VF.esc(r.input) + "</p>" + (rows.length ? U.parts(rows) : "");
    if (r.ok && r.oficial) html += '<p class="mt12 mb0"><a class="btn" href="' + VF.esc(r.input) + '" target="_blank" rel="noopener noreferrer">Cotejar en la sede de la AEAT ↗</a></p><p class="hint mt8">El cotejo lo hace la AEAT en su web; esta herramienta no envía nada.</p>';
    var head = r.ok ? "La URL cumple el formato oficial del QR tributario" : (r.oficial ? "La URL tiene errores de formato" : "No es una URL oficial de la AEAT");
    U.statusBox(res, r.ok ? (r.warnings.length ? "warn" : "ok") : "bad", head, { errors: errs, warnings: r.warnings, notes: r.notes, html: html });
    return r;
  }
  form.addEventListener("submit", function (e) { e.preventDefault(); show($("v-url").value); res.focus(); });
  Object.keys(EJ).forEach(function (k) {
    var b = $("v-ex-" + k);
    if (b) b.addEventListener("click", function () { $("v-url").value = EJ[k]; show(EJ[k]); });
  });

  // --- decodificación de imágenes: BarcodeDetector nativo o jsQR (carga diferida, mismo origen) ---
  var jsqrP = null;
  function loadJsQR() {
    if (window.jsQR) return Promise.resolve(window.jsQR);
    if (jsqrP) return jsqrP;
    var core = document.querySelector('script[src*="assets/core.js"]');
    var base = core ? core.getAttribute("src").replace(/assets\/core\.js.*$/, "") : "/";
    jsqrP = new Promise(function (ok, ko) {
      var s = document.createElement("script"); s.src = base + "assets/jsqr.js?v=1"; s.async = true;
      s.onload = function () { window.jsQR ? ok(window.jsQR) : ko(new Error("jsQR no disponible")); };
      s.onerror = function () { jsqrP = null; ko(new Error("No se pudo cargar el lector")); };
      document.head.appendChild(s);
    });
    return jsqrP;
  }
  var detector = null;
  try { if ("BarcodeDetector" in window) detector = new window.BarcodeDetector({ formats: ["qr_code"] }); } catch (e) { detector = null; }
  function decodeCanvas(c) {
    var ctx = c.getContext("2d", { willReadFrequently: true });
    function viaJs() {
      return loadJsQR().then(function (jsQR) {
        var d = ctx.getImageData(0, 0, c.width, c.height), r = jsQR(d.data, c.width, c.height, { inversionAttempts: "attemptBoth" });
        return r ? r.data : null;
      });
    }
    if (detector) return detector.detect(c).then(function (codes) { return codes && codes.length ? codes[0].rawValue : viaJs(); }, viaJs);
    return viaJs();
  }
  function bitmapToCanvas(bmp) {
    var max = 1600, sc = Math.min(1, max / Math.max(bmp.width, bmp.height));
    var c = document.createElement("canvas"); c.width = Math.round(bmp.width * sc); c.height = Math.round(bmp.height * sc);
    var ctx = c.getContext("2d", { willReadFrequently: true }); ctx.fillStyle = "#fff"; ctx.fillRect(0, 0, c.width, c.height); ctx.drawImage(bmp, 0, 0, c.width, c.height);
    return c;
  }
  function readImage(file) {
    if (!file) return;
    if (!/^image\//.test(file.type)) { U.statusBox(res, "bad", "El archivo no es una imagen (JPG, PNG, WebP…). Para un PDF, haz una captura de pantalla del QR."); return; }
    U.statusBox(res, "info", "Leyendo el código QR de la imagen…");
    var p = window.createImageBitmap ? createImageBitmap(file) : Promise.reject(new Error("Navegador sin createImageBitmap"));
    p.then(function (bmp) { return decodeCanvas(bitmapToCanvas(bmp)); })
      .then(function (txt) {
        if (!txt) { U.statusBox(res, "bad", "No se ha encontrado ningún código QR en la imagen.", { notes: ["Prueba con una foto más nítida, recortada alrededor del QR y con buena luz."] }); return; }
        $("v-url").value = txt; show(txt, file.name); res.focus();
      })
      .catch(function (e) { U.statusBox(res, "bad", "No se ha podido leer la imagen.", { notes: [e.message] }); });
  }
  U.dropZone($("v-drop"), $("v-file"), function (files) { readImage(files[0]); });
  // pegar una captura con Ctrl+V
  document.addEventListener("paste", function (e) {
    var it = e.clipboardData && e.clipboardData.items; if (!it) return;
    for (var i = 0; i < it.length; i++) if (/^image\//.test(it[i].type)) { readImage(it[i].getAsFile()); e.preventDefault(); return; }
  });

  // --- cámara ---
  var stream = null, raf = 0, video = $("v-video"), busy = false;
  function stopCam() {
    if (raf) cancelAnimationFrame(raf); raf = 0;
    if (stream) stream.getTracks().forEach(function (t) { t.stop(); }); stream = null;
    video.hidden = true; $("v-cam-stop").hidden = true; $("v-cam").hidden = false;
  }
  function tick() {
    if (!stream) return;
    if (!busy && video.readyState >= 2 && video.videoWidth) {
      busy = true;
      var c = document.createElement("canvas"), sc = Math.min(1, 900 / video.videoWidth);
      c.width = Math.round(video.videoWidth * sc); c.height = Math.round(video.videoHeight * sc);
      c.getContext("2d", { willReadFrequently: true }).drawImage(video, 0, 0, c.width, c.height);
      decodeCanvas(c).then(function (txt) {
        busy = false;
        if (txt) { stopCam(); $("v-url").value = txt; show(txt, "cámara"); res.focus(); }
      }, function () { busy = false; });
    }
    raf = requestAnimationFrame(tick);
  }
  $("v-cam").addEventListener("click", function () {
    if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) { U.statusBox(res, "bad", "Este navegador no permite usar la cámara aquí.", { notes: ["Sube una foto del QR o pega la URL."] }); return; }
    navigator.mediaDevices.getUserMedia({ video: { facingMode: "environment" }, audio: false }).then(function (s) {
      stream = s; video.srcObject = s; video.hidden = false; $("v-cam-stop").hidden = false; $("v-cam").hidden = true;
      video.play().catch(function () {});
      U.statusBox(res, "info", "Apunta la cámara al código QR de la factura…");
      loadJsQR().catch(function () {});
      raf = requestAnimationFrame(tick);
    }, function (e) { U.statusBox(res, "bad", "No se ha podido abrir la cámara.", { notes: [e && e.name === "NotAllowedError" ? "Has denegado el permiso de cámara. Puedes subir una foto." : String(e && e.message || e)] }); });
  });
  $("v-cam-stop").addEventListener("click", stopCam);
  window.addEventListener("pagehide", stopCam);
  window.VFVAL = { show: show, decodeCanvas: decodeCanvas, readImage: readImage };
})();
