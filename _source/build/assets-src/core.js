/*! Herramientas Verifactu – lógica común (huella SHA-256, NIF, URL del QR tributario, XML de alta).
 *  Todo se ejecuta en el navegador; no se envía nada a ningún servidor. */
(function (root, factory) {
  var api = factory();
  if (typeof module === "object" && module.exports) module.exports = api;
  else root.VF = api;
})(typeof self !== "undefined" ? self : this, function () {
  "use strict";

  // ---------- utilidades ----------
  function esc(s) {
    return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }
  function utf8(str) {
    if (typeof TextEncoder !== "undefined") return Array.prototype.slice.call(new TextEncoder().encode(str));
    var out = [], s = unescape(encodeURIComponent(str));
    for (var i = 0; i < s.length; i++) out.push(s.charCodeAt(i));
    return out;
  }

  // ---------- SHA-256 (FIPS 180-4), salida hexadecimal en MAYÚSCULAS ----------
  var K = [
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
    0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
    0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
    0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
    0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
    0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
    0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
    0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2];
  function sha256(str) {
    var bytes = utf8(String(str)), l = bytes.length, bitLen = l * 8;
    bytes.push(0x80);
    while (bytes.length % 64 !== 56) bytes.push(0);
    var hi = Math.floor(bitLen / 0x100000000), lo = bitLen >>> 0;
    bytes.push((hi >>> 24) & 255, (hi >>> 16) & 255, (hi >>> 8) & 255, hi & 255, (lo >>> 24) & 255, (lo >>> 16) & 255, (lo >>> 8) & 255, lo & 255);
    var H = [0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19];
    var w = new Array(64);
    for (var off = 0; off < bytes.length; off += 64) {
      for (var i = 0; i < 16; i++) w[i] = (bytes[off + i * 4] << 24) | (bytes[off + i * 4 + 1] << 16) | (bytes[off + i * 4 + 2] << 8) | bytes[off + i * 4 + 3];
      for (i = 16; i < 64; i++) {
        var x = w[i - 15], y = w[i - 2];
        var s0 = ((x >>> 7) | (x << 25)) ^ ((x >>> 18) | (x << 14)) ^ (x >>> 3);
        var s1 = ((y >>> 17) | (y << 15)) ^ ((y >>> 19) | (y << 13)) ^ (y >>> 10);
        w[i] = (w[i - 16] + s0 + w[i - 7] + s1) | 0;
      }
      var a = H[0], b = H[1], c = H[2], d = H[3], e = H[4], f = H[5], g = H[6], h = H[7];
      for (i = 0; i < 64; i++) {
        var S1 = ((e >>> 6) | (e << 26)) ^ ((e >>> 11) | (e << 21)) ^ ((e >>> 25) | (e << 7));
        var ch = (e & f) ^ (~e & g);
        var t1 = (h + S1 + ch + K[i] + w[i]) | 0;
        var S0 = ((a >>> 2) | (a << 30)) ^ ((a >>> 13) | (a << 19)) ^ ((a >>> 22) | (a << 10));
        var maj = (a & b) ^ (a & c) ^ (b & c);
        var t2 = (S0 + maj) | 0;
        h = g; g = f; f = e; e = (d + t1) | 0; d = c; c = b; b = a; a = (t1 + t2) | 0;
      }
      H[0] = (H[0] + a) | 0; H[1] = (H[1] + b) | 0; H[2] = (H[2] + c) | 0; H[3] = (H[3] + d) | 0;
      H[4] = (H[4] + e) | 0; H[5] = (H[5] + f) | 0; H[6] = (H[6] + g) | 0; H[7] = (H[7] + h) | 0;
    }
    return H.map(function (v) { return ("00000000" + (v >>> 0).toString(16)).slice(-8); }).join("").toUpperCase();
  }

  // ---------- Huella de los registros (AEAT, especificaciones huella v0.1.2) ----------
  var FIELDS = {
    alta: ["IDEmisorFactura", "NumSerieFactura", "FechaExpedicionFactura", "TipoFactura", "CuotaTotal", "ImporteTotal", "Huella", "FechaHoraHusoGenRegistro"],
    anulacion: ["IDEmisorFacturaAnulada", "NumSerieFacturaAnulada", "FechaExpedicionFacturaAnulada", "Huella", "FechaHoraHusoGenRegistro"],
    // En el evento el nombre "NIF" aparece dos veces: 1.º NIF del productor (SistemaInformatico), 6.º NIF del obligado.
    evento: ["NIF", "ID", "IdSistemaInformatico", "Version", "NumeroInstalacion", "NIF", "TipoEvento", "HuellaEvento", "FechaHoraHusoGenEvento"]
  };
  // valores: array en el orden de FIELDS[tipo]
  function cadena(tipo, valores) {
    var f = FIELDS[tipo];
    if (!f) throw new Error("Tipo de registro desconocido: " + tipo);
    return f.map(function (n, i) { var v = valores[i]; return n + "=" + (v == null ? "" : String(v).trim()); }).join("&");
  }
  function huella(tipo, valores) {
    var s = cadena(tipo, valores);
    return { cadena: s, huella: sha256(s) };
  }
  var RE_HASH = /^[0-9A-F]{64}$/;
  var RE_TS = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:[+-]\d{2}:\d{2}|Z)$/;
  // Avisos de formato para los valores que entran en la huella
  function avisosHuella(tipo, valores) {
    var w = [], f = FIELDS[tipo];
    f.forEach(function (n, i) {
      var v = valores[i] == null ? "" : String(valores[i]).trim();
      if ((n === "Huella" || n === "HuellaEvento") && v && !RE_HASH.test(v)) w.push(n + " anterior: debe tener 64 caracteres hexadecimales en mayúsculas.");
      if (/^FechaHoraHuso/.test(n) && !RE_TS.test(v)) w.push(n + ": formato esperado AAAA-MM-DDThh:mm:ss+hh:mm (con huso horario).");
      if (/^FechaExpedicion/.test(n) && !/^\d{2}-\d{2}-\d{4}$/.test(v)) w.push(n + ": formato esperado DD-MM-AAAA.");
      if ((n === "CuotaTotal" || n === "ImporteTotal") && !/^[+-]?\d{1,12}(\.\d{1,2})?$/.test(v)) w.push(n + ": importe con punto decimal y máximo 2 decimales (p. ej. 123.45).");
      if ((n === "IDEmisorFactura" || n === "IDEmisorFacturaAnulada") && v.length !== 9) w.push(n + ": el NIF debe tener 9 caracteres.");
      if ((n === "NumSerieFactura" || n === "NumSerieFacturaAnulada") && (v.length === 0 || v.length > 60)) w.push(n + ": entre 1 y 60 caracteres.");
      if (n === "TipoFactura" && ["F1", "F2", "F3", "R1", "R2", "R3", "R4", "R5"].indexOf(v) < 0) w.push("TipoFactura: valores admitidos F1, F2, F3, R1–R5.");
    });
    return w;
  }
  // Ejemplos oficiales de la AEAT (documento de huella v0.1.2, apartado 6)
  var EJEMPLOS = [
    { tipo: "alta", valores: ["89890001K", "12345678/G33", "01-01-2024", "F1", "12.35", "123.45", "", "2024-01-01T19:20:30+01:00"], huella: "3C464DAF61ACB827C65FDA19F352A4E3BDC2C640E9E9FC4CC058073F38F12F60" },
    { tipo: "alta", valores: ["89890001K", "12345679/G34", "01-01-2024", "F1", "12.35", "123.45", "3C464DAF61ACB827C65FDA19F352A4E3BDC2C640E9E9FC4CC058073F38F12F60", "2024-01-01T19:20:35+01:00"], huella: "F7B94CFD8924EDFF273501B01EE5153E4CE8F259766F88CF6ACB8935802A2B97" },
    { tipo: "anulacion", valores: ["89890001K", "12345679/G34", "01-01-2024", "F7B94CFD8924EDFF273501B01EE5153E4CE8F259766F88CF6ACB8935802A2B97", "2024-01-01T19:20:40+01:00"], huella: "177547C0D57AC74748561D054A9CEC14B4C4EA23D1BEFD6F2E69E3A388F90C68" }
  ];

  // ---------- NIF / NIE / CIF ----------
  var DNI_L = "TRWAGMYFPDXBNJZSQVHLCKE";
  function checkNif(input) {
    var s = String(input || "").toUpperCase().replace(/[\s.\-]/g, "");
    var r = { input: input, value: s, ok: false, kind: "", msg: "" };
    if (s.length !== 9) { r.msg = "El NIF debe tener exactamente 9 caracteres (tiene " + s.length + ")."; return r; }
    var m;
    if ((m = /^(\d{8})([A-Z])$/.exec(s))) {
      r.kind = "DNI (persona física)";
      var exp = DNI_L[parseInt(m[1], 10) % 23];
      r.ok = exp === m[2]; if (!r.ok) r.msg = "La letra de control no corresponde: debería ser " + exp + "."; return r;
    }
    if ((m = /^([XYZ])(\d{7})([A-Z])$/.exec(s))) {
      r.kind = "NIE (extranjero)";
      var n = parseInt({ X: "0", Y: "1", Z: "2" }[m[1]] + m[2], 10), e2 = DNI_L[n % 23];
      r.ok = e2 === m[3]; if (!r.ok) r.msg = "La letra de control no corresponde: debería ser " + e2 + "."; return r;
    }
    if ((m = /^([KLM])(\d{7})([A-Z])$/.exec(s))) {
      r.kind = "NIF especial (K, L, M)";
      var e3 = DNI_L[parseInt(m[2], 10) % 23];
      r.ok = e3 === m[3]; if (!r.ok) r.msg = "La letra de control no corresponde: debería ser " + e3 + "."; return r;
    }
    if ((m = /^([ABCDEFGHJNPQRSUVW])(\d{7})([0-9A-J])$/.exec(s))) {
      r.kind = "NIF de persona jurídica o entidad";
      var d = m[2], sum = 0;
      for (var i = 0; i < 7; i++) {
        var v = +d[i];
        if (i % 2 === 0) { v *= 2; sum += Math.floor(v / 10) + (v % 10); } else sum += v;
      }
      var ctl = (10 - (sum % 10)) % 10, letra = "JABCDEFGHI"[ctl], c = m[3];
      var soloLetra = "PQRSNW".indexOf(m[1]) >= 0, soloNum = "ABEH".indexOf(m[1]) >= 0;
      if (soloLetra) r.ok = c === letra;
      else if (soloNum) r.ok = c === String(ctl);
      else r.ok = c === letra || c === String(ctl);
      if (!r.ok) r.msg = "El carácter de control no corresponde: debería ser " + (soloLetra ? letra : soloNum ? ctl : ctl + " o " + letra) + ".";
      return r;
    }
    r.msg = "Formato no reconocido: se espera DNI (8 cifras + letra), NIE (X/Y/Z + 7 cifras + letra) o NIF de entidad (letra + 7 cifras + control).";
    return r;
  }

  // ---------- Importes y fechas ----------
  // Convierte lo que escribe el usuario ("1.234,56", "1234,5", "241.4") al formato del QR ("1234.56")
  function normImporte(input) {
    var s = String(input == null ? "" : input).trim().replace(/\s|€|EUR/gi, "");
    var r = { input: input, value: "", ok: false, msg: "", warn: "" };
    if (!s) { r.msg = "Introduce el importe total de la factura."; return r; }
    var neg = false;
    if (/^[+-]/.test(s)) { neg = s[0] === "-"; s = s.slice(1); }
    var lastDot = s.lastIndexOf("."), lastComma = s.lastIndexOf(",");
    var intPart, dec = "";
    if (lastDot >= 0 && lastComma >= 0) {
      var sep = lastDot > lastComma ? "." : ",", other = sep === "." ? "," : ".";
      var p = s.split(sep); if (p.length !== 2) { r.msg = "Formato de importe no válido."; return r; }
      intPart = p[0].split(other).join(""); dec = p[1];
    } else if (lastComma >= 0) {
      var pc = s.split(",");
      if (pc.length !== 2) { r.msg = "Formato de importe no válido."; return r; }
      intPart = pc[0]; dec = pc[1];
    } else if (lastDot >= 0) {
      var pd = s.split(".");
      if (pd.length > 2 || (pd.length === 2 && pd[1].length === 3 && pd[0].length <= 3)) {
        if (pd.slice(1).every(function (g) { return g.length === 3; })) { intPart = pd.join(""); dec = ""; r.warn = "He interpretado el punto como separador de miles (" + s + " → " + pd.join("") + "). Si eran decimales, escribe una coma o máximo 2 decimales."; }
        else { r.msg = "Formato de importe no válido."; return r; }
      } else { intPart = pd[0]; dec = pd[1] || ""; }
    } else intPart = s;
    if (!/^\d+$/.test(intPart || "") || !/^\d*$/.test(dec)) { r.msg = "El importe solo puede contener cifras y un separador decimal."; return r; }
    if (dec.length > 2) { r.msg = "Máximo 2 decimales (código de error AEAT 2005)."; return r; }
    intPart = intPart.replace(/^0+(?=\d)/, "");
    if (intPart.length > 12) { r.msg = "Máximo 12 cifras en la parte entera (código de error AEAT 2006)."; return r; }
    while (dec.length < 2) dec += "0";
    r.value = (neg ? "-" : "") + intPart + "." + dec;
    r.ok = true;
    if (neg) r.warn = (r.warn ? r.warn + " " : "") + "Importe negativo: habitual solo en facturas rectificativas.";
    return r;
  }
  function validDate(d, m, y) {
    if (y < 1900 || y > 2100 || m < 1 || m > 12 || d < 1) return false;
    var dim = [31, (y % 4 === 0 && y % 100 !== 0) || y % 400 === 0 ? 29 : 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][m - 1];
    return d <= dim;
  }
  // Acepta "2026-11-13" (input date), "13/11/2026", "13-11-2026" → "13-11-2026"
  function normFecha(input) {
    var s = String(input || "").trim(), m, r = { input: input, value: "", ok: false, msg: "" };
    if ((m = /^(\d{4})-(\d{2})-(\d{2})$/.exec(s))) s = m[3] + "-" + m[2] + "-" + m[1];
    else if ((m = /^(\d{1,2})[\/.\-](\d{1,2})[\/.\-](\d{4})$/.exec(s))) s = ("0" + m[1]).slice(-2) + "-" + ("0" + m[2]).slice(-2) + "-" + m[3];
    if (!(m = /^(\d{2})-(\d{2})-(\d{4})$/.exec(s))) { r.msg = "La fecha debe tener el formato DD-MM-AAAA (código de error AEAT 2004)."; return r; }
    if (!validDate(+m[1], +m[2], +m[3])) { r.msg = "La fecha " + s + " no existe."; return r; }
    r.value = s; r.ok = true; return r;
  }
  // Fecha y hora actual con el huso horario de Madrid (península): "2026-11-13T11:04:05+01:00"
  function ahoraMadrid(date) {
    date = date || new Date();
    try {
      var f = new Intl.DateTimeFormat("en-GB", { timeZone: "Europe/Madrid", year: "numeric", month: "2-digit", day: "2-digit", hour: "2-digit", minute: "2-digit", second: "2-digit", hourCycle: "h23", timeZoneName: "longOffset" });
      var p = {}; f.formatToParts(date).forEach(function (x) { p[x.type] = x.value; });
      var off = (p.timeZoneName || "GMT").replace("GMT", "") || "+00:00";
      if (/^[+-]\d{1,2}$/.test(off)) off = off[0] + ("0" + off.slice(1)).slice(-2) + ":00";
      return p.year + "-" + p.month + "-" + p.day + "T" + p.hour + ":" + p.minute + ":" + p.second + off;
    } catch (e) {
      var o = -date.getTimezoneOffset(), sg = o >= 0 ? "+" : "-"; o = Math.abs(o);
      function z(n) { return ("0" + n).slice(-2); }
      return date.getFullYear() + "-" + z(date.getMonth() + 1) + "-" + z(date.getDate()) + "T" + z(date.getHours()) + ":" + z(date.getMinutes()) + ":" + z(date.getSeconds()) + sg + z(Math.floor(o / 60)) + ":" + z(o % 60);
    }
  }

  // ---------- URL del QR tributario (AEAT, especificaciones QR v0.5.0) ----------
  var HOSTS = { "www2.agenciatributaria.gob.es": "produccion", "prewww2.aeat.es": "pruebas" };
  var PATHS = { "/wlpl/TIKE-CONT/ValidarQR": true, "/wlpl/TIKE-CONT/ValidarQRNoVerifactu": false };
  var IDIOMAS = ["gl", "ca", "eu", "es", "va", "en"];
  var ERRORES = {
    1001: "No se ha remitido el parámetro: nif",
    1002: "No se ha remitido el parámetro: numserie",
    1003: "No se ha remitido el parámetro: fecha",
    1004: "No se ha remitido el parámetro: importe",
    2001: "El NIF tiene un formato erróneo o no es válido",
    2002: "El número de serie excede el número máximo de caracteres",
    2003: "El número de serie contiene caracteres no permitidos",
    2004: "La fecha de expedición tiene formato inválido y debe tener el formato DD-MM-AAAA",
    2005: "El importe tiene un formato incorrecto",
    2006: "El importe excede el número máximo de caracteres",
    3001: "Error técnico en los sistemas de la Agencia Tributaria",
    3002: "Se ha excedido el número máximo de intentos permitidos por día"
  };
  // Codificación como java.net.URLEncoder (UTF-8), igual que el ejemplo de la AEAT: espacio → "+"
  function encodeParam(v) {
    return encodeURIComponent(v).replace(/%20/g, "+").replace(/[!'()~]/g, function (c) { return "%" + c.charCodeAt(0).toString(16).toUpperCase(); });
  }
  function base(entorno, verifactu) {
    var host = entorno === "pruebas" ? "https://prewww2.aeat.es" : "https://www2.agenciatributaria.gob.es";
    return host + "/wlpl/TIKE-CONT/" + (verifactu === false ? "ValidarQRNoVerifactu" : "ValidarQR");
  }
  function checkNumSerie(ns) {
    var errs = [];
    if (!ns) errs.push({ code: 1002, msg: "Falta el número de serie y número de la factura." });
    else {
      if (ns.length > 60) errs.push({ code: 2002, msg: "El número de serie tiene " + ns.length + " caracteres; el máximo es 60." });
      var bad = [];
      for (var i = 0; i < ns.length; i++) { var c = ns.charCodeAt(i); if (c < 32 || c > 126) bad.push(ns[i]); }
      if (bad.length) errs.push({ code: 2003, msg: "Caracteres no permitidos (solo ASCII imprimible 32–126, sin tildes ni ñ): " + bad.join(" ") });
    }
    return errs;
  }
  // d = { nif, numserie, fecha, importe, entorno: "produccion"|"pruebas", verifactu: true|false }
  function buildQrUrl(d) {
    var errors = [], warnings = [];
    var nif = checkNif(d.nif);
    if (!String(d.nif || "").trim()) errors.push({ code: 1001, msg: "Falta el NIF del emisor." });
    else if (nif.value.length !== 9) errors.push({ code: 2001, msg: nif.msg });
    else if (!nif.ok) warnings.push("NIF " + nif.value + ": " + nif.msg + " La AEAT rechazará el cotejo si el NIF no es válido (error 2001).");
    var ns = String(d.numserie == null ? "" : d.numserie).trim();
    errors = errors.concat(checkNumSerie(ns));
    var fe = normFecha(d.fecha);
    if (!String(d.fecha || "").trim()) errors.push({ code: 1003, msg: "Falta la fecha de expedición." });
    else if (!fe.ok) errors.push({ code: 2004, msg: fe.msg });
    var im = normImporte(d.importe);
    if (!String(d.importe == null ? "" : d.importe).trim()) errors.push({ code: 1004, msg: "Falta el importe total." });
    else if (!im.ok) errors.push({ code: /12 cifras/.test(im.msg) ? 2006 : 2005, msg: im.msg });
    else if (im.warn) warnings.push(im.warn);
    if (errors.length) return { ok: false, errors: errors, warnings: warnings, url: "" };
    var url = base(d.entorno, d.verifactu) + "?nif=" + encodeParam(nif.value) + "&numserie=" + encodeParam(ns) + "&fecha=" + encodeParam(fe.value) + "&importe=" + encodeParam(im.value);
    if (d.entorno === "pruebas") warnings.push("URL del entorno de PRUEBAS (prewww2.aeat.es): no la uses en facturas reales.");
    return { ok: true, errors: errors, warnings: warnings, url: url, params: { nif: nif.value, numserie: ns, fecha: fe.value, importe: im.value } };
  }
  function decodeParam(v) {
    try { return decodeURIComponent(v.replace(/\+/g, " ")); } catch (e) { return null; }
  }
  var LOOKALIKE = /agencia|tributaria|aeat|hacienda/i;
  // Analiza una URL leída de un QR tributario
  function parseQrUrl(raw) {
    var s = String(raw || "").trim(), r = { input: s, ok: false, errors: [], warnings: [], notes: [], params: {}, entorno: "", verifactu: null, oficial: false };
    if (!s) { r.errors.push({ msg: "Pega la URL del código QR." }); return r; }
    var m = /^([a-z][a-z0-9+.\-]*):\/\/([^\/?#]+)([^?#]*)(\?[^#]*)?(#.*)?$/i.exec(s);
    if (!m) { r.errors.push({ msg: "No es una URL válida. El QR tributario contiene una dirección que empieza por https://" }); return r; }
    var scheme = m[1].toLowerCase(), host = m[2].toLowerCase(), path = m[3], query = (m[4] || "").slice(1);
    if (host.indexOf("@") >= 0 || /:\d+$/.test(host)) r.errors.push({ msg: "La dirección incluye usuario o puerto: no es una URL oficial de la AEAT." });
    host = host.replace(/:\d+$/, "");
    if (HOSTS[host]) { r.entorno = HOSTS[host]; r.oficial = true; }
    else {
      r.errors.push({ msg: "El dominio " + host + " no es de la AEAT. Solo son válidos www2.agenciatributaria.gob.es (producción) y prewww2.aeat.es (pruebas)." + (LOOKALIKE.test(host) ? " ¡Ojo! Imita el nombre de la Agencia Tributaria: posible fraude (phishing)." : "") });
    }
    if (scheme !== "https") r.errors.push({ msg: "La URL debe empezar por https:// (lleva " + scheme + "://)." });
    if (Object.prototype.hasOwnProperty.call(PATHS, path)) r.verifactu = PATHS[path];
    else if (r.oficial) r.errors.push({ msg: "Ruta no reconocida: " + (path || "/") + ". Debe ser /wlpl/TIKE-CONT/ValidarQR (VERI*FACTU) o /wlpl/TIKE-CONT/ValidarQRNoVerifactu." });
    if (r.entorno === "pruebas") r.warnings.push("Entorno de PRUEBAS (prewww2.aeat.es). Una factura real debe llevar la URL de producción.");
    if (r.verifactu === false) r.notes.push("Sistema «No VERI*FACTU»: la AEAT responderá «No contrastable» (código 02); la factura no se ha remitido en el momento.");
    if (r.verifactu === true) r.notes.push("Sistema VERI*FACTU: la factura debería constar en la AEAT («Encontrada», código 00). Debajo del QR debe figurar «VERI*FACTU» o «Factura verificable en la sede electrónica de la AEAT».");
    // parámetros
    var seen = {}, extra = [], dup = [], params = {};
    if (query) query.split("&").forEach(function (kv) {
      if (kv === "") return;
      var i = kv.indexOf("="), k = i < 0 ? kv : kv.slice(0, i), v = i < 0 ? null : kv.slice(i + 1);
      var key = k.toLowerCase();
      if (seen[key]) dup.push(k); seen[key] = true;
      if (["nif", "numserie", "fecha", "importe", "idioma", "formato"].indexOf(key) < 0) { extra.push(k); return; }
      if (k !== key) r.warnings.push("El parámetro «" + k + "» debería escribirse en minúsculas: «" + key + "».");
      var dv = v == null ? "" : decodeParam(v);
      if (dv == null) r.errors.push({ msg: "El parámetro " + key + " tiene una codificación % no válida." });
      params[key] = dv == null ? v : dv;
      if (key === "numserie" && v && /[^A-Za-z0-9%+.\-_*]/.test(v)) r.warnings.push("El número de serie contiene caracteres sin codificar (" + v + "). La AEAT pide aplicar «URL encoding» UTF-8 a los valores.");
    });
    r.params = params;
    if (dup.length) r.errors.push({ msg: "Parámetros repetidos: " + dup.join(", ") + "." });
    if (extra.length) r.errors.push({ msg: "Parámetros no previstos: " + extra.join(", ") + ". Si el número de serie contiene «&», debe codificarse como %26; si no, la URL se parte y la AEAT no encuentra la factura." });
    if (params.formato != null) r.errors.push({ msg: "El parámetro «formato» nunca puede ir en la URL impresa en el QR de la factura (solo para consultas automáticas)." });
    if (params.idioma != null && IDIOMAS.indexOf(params.idioma) < 0) r.errors.push({ msg: "idioma=" + params.idioma + " no es válido (gl, ca, eu, es, va, en)." });
    else if (params.idioma != null) r.notes.push("Parámetro opcional idioma=" + params.idioma + " (idioma de la respuesta de la AEAT).");
    // obligatorios
    if (params.nif == null || params.nif === "") r.errors.push({ code: 1001, msg: ERRORES[1001] + "." });
    else {
      var n = checkNif(params.nif);
      if (params.nif.length !== 9 || !/^[0-9A-Z]{9}$/.test(params.nif)) r.errors.push({ code: 2001, msg: ERRORES[2001] + ": «" + params.nif + "» debe tener 9 caracteres (cifras y letras mayúsculas)." });
      else if (!n.ok) r.errors.push({ code: 2001, msg: ERRORES[2001] + ": " + n.msg });
      else r.notes.push("NIF " + n.value + " correcto (" + n.kind + ").");
    }
    if (params.numserie == null || params.numserie === "") r.errors.push({ code: 1002, msg: ERRORES[1002] + "." });
    else checkNumSerie(params.numserie).forEach(function (e) { r.errors.push(e); });
    if (params.fecha == null || params.fecha === "") r.errors.push({ code: 1003, msg: ERRORES[1003] + "." });
    else {
      var fm = /^(\d{2})-(\d{2})-(\d{4})$/.exec(params.fecha);
      if (!fm) r.errors.push({ code: 2004, msg: ERRORES[2004] + " (recibido: «" + params.fecha + "»)." });
      else if (!validDate(+fm[1], +fm[2], +fm[3])) r.errors.push({ code: 2004, msg: "La fecha " + params.fecha + " no existe." });
    }
    if (params.importe == null || params.importe === "") r.errors.push({ code: 1004, msg: ERRORES[1004] + "." });
    else {
      var im = params.importe, mm = /^([+-]?)(\d+)(?:\.(\d+))?$/.exec(im);
      if (!mm) r.errors.push({ code: 2005, msg: ERRORES[2005] + ": «" + im + "»." + (/,/.test(im) ? " Usa el punto «.» como separador decimal, no la coma." : "") });
      else if (mm[2].length > 12) r.errors.push({ code: 2006, msg: ERRORES[2006] + " (máximo 12 cifras enteras)." });
      else if (mm[3] && mm[3].length > 2) r.errors.push({ code: 2005, msg: ERRORES[2005] + " (máximo 2 decimales)." });
    }
    r.ok = r.errors.length === 0;
    return r;
  }

  // ---------- XML del registro de alta (SuministroLR.xsd / SuministroInformacion.xsd v1.0) ----------
  var NS_LR = "https://www2.agenciatributaria.gob.es/static_files/common/internet/dep/aplicaciones/es/aeat/tike/cont/ws/SuministroLR.xsd";
  var NS_SF = "https://www2.agenciatributaria.gob.es/static_files/common/internet/dep/aplicaciones/es/aeat/tike/cont/ws/SuministroInformacion.xsd";
  function xe(s) { return String(s == null ? "" : s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;"); }
  function money(n) { return (Math.round(n * 100) / 100).toFixed(2); }
  // d: { emisorNif, emisorNombre, numSerie, fecha (DD-MM-AAAA), tipoFactura, descripcion, destNif, destNombre,
  //      lineas: [{ impuesto, clave, calificacion | exenta, tipo, base, cuota }], primerRegistro: bool,
  //      anterior: { nif, numSerie, fecha, huella }, sif: { nombreRazon, nif, nombre, id, version, instalacion, soloVerifactu, multiOT, indicadorMultiOT },
  //      fechaHora }
  function buildAlta(d) {
    var cuotaTotal = 0, importeTotal = 0;
    var lineas = (d.lineas || []).map(function (l) {
      var b = +l.base || 0, c = l.exenta ? 0 : (l.cuota != null && l.cuota !== "" ? +l.cuota : b * (+l.tipo || 0) / 100);
      cuotaTotal += c; importeTotal += b + c;
      return { impuesto: l.impuesto || "01", clave: l.clave || "01", calificacion: l.calificacion, exenta: l.exenta, tipo: l.tipo, base: money(b), cuota: money(c) };
    });
    var ct = money(cuotaTotal), it = money(importeTotal);
    var anterior = d.primerRegistro ? "" : ((d.anterior && d.anterior.huella) || "");
    var h = huella("alta", [d.emisorNif, d.numSerie, d.fecha, d.tipoFactura, ct, it, anterior, d.fechaHora]);
    var x = [];
    x.push('<?xml version="1.0" encoding="UTF-8"?>');
    x.push('<sfLR:RegFactuSistemaFacturacion xmlns:sfLR="' + NS_LR + '" xmlns:sf="' + NS_SF + '">');
    x.push("  <sfLR:Cabecera>");
    x.push("    <sf:ObligadoEmision>");
    x.push("      <sf:NombreRazon>" + xe(d.emisorNombre) + "</sf:NombreRazon>");
    x.push("      <sf:NIF>" + xe(d.emisorNif) + "</sf:NIF>");
    x.push("    </sf:ObligadoEmision>");
    x.push("  </sfLR:Cabecera>");
    x.push("  <sfLR:RegistroFactura>");
    x.push("    <sf:RegistroAlta>");
    x.push("      <sf:IDVersion>1.0</sf:IDVersion>");
    x.push("      <sf:IDFactura>");
    x.push("        <sf:IDEmisorFactura>" + xe(d.emisorNif) + "</sf:IDEmisorFactura>");
    x.push("        <sf:NumSerieFactura>" + xe(d.numSerie) + "</sf:NumSerieFactura>");
    x.push("        <sf:FechaExpedicionFactura>" + xe(d.fecha) + "</sf:FechaExpedicionFactura>");
    x.push("      </sf:IDFactura>");
    x.push("      <sf:NombreRazonEmisor>" + xe(d.emisorNombre) + "</sf:NombreRazonEmisor>");
    x.push("      <sf:TipoFactura>" + xe(d.tipoFactura) + "</sf:TipoFactura>");
    x.push("      <sf:DescripcionOperacion>" + xe(d.descripcion) + "</sf:DescripcionOperacion>");
    if (d.destNif) {
      x.push("      <sf:Destinatarios>");
      x.push("        <sf:IDDestinatario>");
      x.push("          <sf:NombreRazon>" + xe(d.destNombre) + "</sf:NombreRazon>");
      x.push("          <sf:NIF>" + xe(d.destNif) + "</sf:NIF>");
      x.push("        </sf:IDDestinatario>");
      x.push("      </sf:Destinatarios>");
    }
    x.push("      <sf:Desglose>");
    lineas.forEach(function (l) {
      x.push("        <sf:DetalleDesglose>");
      x.push("          <sf:Impuesto>" + xe(l.impuesto) + "</sf:Impuesto>");
      x.push("          <sf:ClaveRegimen>" + xe(l.clave) + "</sf:ClaveRegimen>");
      if (l.exenta) x.push("          <sf:OperacionExenta>" + xe(l.exenta) + "</sf:OperacionExenta>");
      else {
        x.push("          <sf:CalificacionOperacion>" + xe(l.calificacion || "S1") + "</sf:CalificacionOperacion>");
        if (/^S/.test(l.calificacion || "S1")) x.push("          <sf:TipoImpositivo>" + xe(String(+l.tipo || 0)) + "</sf:TipoImpositivo>");
      }
      x.push("          <sf:BaseImponibleOimporteNoSujeto>" + l.base + "</sf:BaseImponibleOimporteNoSujeto>");
      if (!l.exenta && /^S/.test(l.calificacion || "S1")) x.push("          <sf:CuotaRepercutida>" + l.cuota + "</sf:CuotaRepercutida>");
      x.push("        </sf:DetalleDesglose>");
    });
    x.push("      </sf:Desglose>");
    x.push("      <sf:CuotaTotal>" + ct + "</sf:CuotaTotal>");
    x.push("      <sf:ImporteTotal>" + it + "</sf:ImporteTotal>");
    x.push("      <sf:Encadenamiento>");
    if (d.primerRegistro) x.push("        <sf:PrimerRegistro>S</sf:PrimerRegistro>");
    else {
      var a = d.anterior || {};
      x.push("        <sf:RegistroAnterior>");
      x.push("          <sf:IDEmisorFactura>" + xe(a.nif) + "</sf:IDEmisorFactura>");
      x.push("          <sf:NumSerieFactura>" + xe(a.numSerie) + "</sf:NumSerieFactura>");
      x.push("          <sf:FechaExpedicionFactura>" + xe(a.fecha) + "</sf:FechaExpedicionFactura>");
      x.push("          <sf:Huella>" + xe(a.huella) + "</sf:Huella>");
      x.push("        </sf:RegistroAnterior>");
    }
    x.push("      </sf:Encadenamiento>");
    var s = d.sif || {};
    x.push("      <sf:SistemaInformatico>");
    x.push("        <sf:NombreRazon>" + xe(s.nombreRazon) + "</sf:NombreRazon>");
    x.push("        <sf:NIF>" + xe(s.nif) + "</sf:NIF>");
    x.push("        <sf:NombreSistemaInformatico>" + xe(s.nombre) + "</sf:NombreSistemaInformatico>");
    x.push("        <sf:IdSistemaInformatico>" + xe(s.id) + "</sf:IdSistemaInformatico>");
    x.push("        <sf:Version>" + xe(s.version) + "</sf:Version>");
    x.push("        <sf:NumeroInstalacion>" + xe(s.instalacion) + "</sf:NumeroInstalacion>");
    x.push("        <sf:TipoUsoPosibleSoloVerifactu>" + (s.soloVerifactu || "S") + "</sf:TipoUsoPosibleSoloVerifactu>");
    x.push("        <sf:TipoUsoPosibleMultiOT>" + (s.multiOT || "N") + "</sf:TipoUsoPosibleMultiOT>");
    x.push("        <sf:IndicadorMultiplesOT>" + (s.indicadorMultiOT || "N") + "</sf:IndicadorMultiplesOT>");
    x.push("      </sf:SistemaInformatico>");
    x.push("      <sf:FechaHoraHusoGenRegistro>" + xe(d.fechaHora) + "</sf:FechaHoraHusoGenRegistro>");
    x.push("      <sf:TipoHuella>01</sf:TipoHuella>");
    x.push("      <sf:Huella>" + h.huella + "</sf:Huella>");
    x.push("    </sf:RegistroAlta>");
    x.push("  </sfLR:RegistroFactura>");
    x.push("</sfLR:RegFactuSistemaFacturacion>");
    return { xml: x.join("\n") + "\n", huella: h.huella, cadena: h.cadena, cuotaTotal: ct, importeTotal: it };
  }

  // --- lectura de XML independiente del prefijo de espacio de nombres ---
  function kids(el, name) {
    var out = [];
    if (!el) return out;
    for (var n = el.firstChild; n; n = n.nextSibling) if (n.nodeType === 1 && (n.localName || n.nodeName.replace(/^.*:/, "")) === name) out.push(n);
    return out;
  }
  function kid(el, name) { return kids(el, name)[0] || null; }
  function path(el, p) { p.split("/").forEach(function (nm) { el = el ? kid(el, nm) : null; }); return el; }
  function txt(el, p) { var n = p ? path(el, p) : el; return n ? String(n.textContent) : null; }
  function elementChildren(el) { var out = []; for (var n = el.firstChild; n; n = n.nextSibling) if (n.nodeType === 1) out.push(n.localName || n.nodeName.replace(/^.*:/, "")); return out; }
  function allByLocal(doc, name) {
    var out = [], all = doc.getElementsByTagName("*");
    for (var i = 0; i < all.length; i++) if ((all[i].localName || all[i].nodeName.replace(/^.*:/, "")) === name) out.push(all[i]);
    return out;
  }
  function parseXml(text, DP) {
    DP = DP || (typeof DOMParser !== "undefined" ? DOMParser : null);
    var doc;
    try { doc = new DP().parseFromString(String(text), "application/xml"); } catch (e) { return { error: "El XML no está bien formado: " + e.message }; }
    var pe = doc.getElementsByTagName("parsererror");
    if (pe.length || !doc.documentElement) return { error: "El XML no está bien formado" + (pe.length ? ": " + String(pe[0].textContent).trim().slice(0, 200) : ".") };
    return { doc: doc };
  }
  // Valores que entran en la huella para un elemento RegistroAlta / RegistroAnulacion / RegistroEvento
  function valoresRegistro(el) {
    var ln = el.localName || el.nodeName.replace(/^.*:/, "");
    if (ln === "RegistroAlta") return { tipo: "alta", id: txt(el, "IDFactura/NumSerieFactura"), guardada: txt(el, "Huella"), anterior: txt(el, "Encadenamiento/RegistroAnterior/Huella"), primero: txt(el, "Encadenamiento/PrimerRegistro") === "S",
      valores: [txt(el, "IDFactura/IDEmisorFactura"), txt(el, "IDFactura/NumSerieFactura"), txt(el, "IDFactura/FechaExpedicionFactura"), txt(el, "TipoFactura"), txt(el, "CuotaTotal"), txt(el, "ImporteTotal"), txt(el, "Encadenamiento/RegistroAnterior/Huella"), txt(el, "FechaHoraHusoGenRegistro")] };
    if (ln === "RegistroAnulacion") return { tipo: "anulacion", id: txt(el, "IDFactura/NumSerieFacturaAnulada"), guardada: txt(el, "Huella"), anterior: txt(el, "Encadenamiento/RegistroAnterior/Huella"), primero: txt(el, "Encadenamiento/PrimerRegistro") === "S",
      valores: [txt(el, "IDFactura/IDEmisorFacturaAnulada"), txt(el, "IDFactura/NumSerieFacturaAnulada"), txt(el, "IDFactura/FechaExpedicionFacturaAnulada"), txt(el, "Encadenamiento/RegistroAnterior/Huella"), txt(el, "FechaHoraHusoGenRegistro")] };
    if (ln === "RegistroEvento") {
      var ev = kid(el, "Evento") || el;
      return { tipo: "evento", id: "Evento " + (txt(ev, "TipoEvento") || ""), guardada: txt(ev, "HuellaEvento"), anterior: txt(ev, "Encadenamiento/EventoAnterior/HuellaEvento"), primero: txt(ev, "Encadenamiento/PrimerEvento") === "S",
        valores: [txt(ev, "SistemaInformatico/NIF"), txt(ev, "SistemaInformatico/IDOtro/ID"), txt(ev, "SistemaInformatico/IdSistemaInformatico"), txt(ev, "SistemaInformatico/Version"), txt(ev, "SistemaInformatico/NumeroInstalacion"), txt(ev, "ObligadoEmision/NIF"), txt(ev, "TipoEvento"), txt(ev, "Encadenamiento/EventoAnterior/HuellaEvento"), txt(ev, "FechaHoraHusoGenEvento")] };
    }
    return null;
  }
  // Variantes de importes (1 o 2 decimales) para detectar diferencias solo de formato
  function variantesImporte(v) {
    var out = [v], m = /^([+-]?\d+)(?:\.(\d{1,2}))?$/.exec(String(v || "").trim());
    if (!m) return out;
    var dec = m[2] || "";
    [dec, dec.replace(/0+$/, ""), (dec + "00").slice(0, 2), (dec + "0").slice(0, Math.max(1, dec.replace(/0+$/, "").length))].forEach(function (d2) {
      var s = d2 ? m[1] + "." + d2 : m[1]; if (out.indexOf(s) < 0) out.push(s);
    });
    return out;
  }
  // Comprueba huellas y encadenamiento de todos los registros de un XML (alta, anulación y evento)
  function checkChain(text, DP) {
    var p = parseXml(text, DP);
    if (p.error) return { error: p.error, rows: [] };
    var els = [];
    (function walk(n) {
      for (var c = n.firstChild; c; c = c.nextSibling) if (c.nodeType === 1) {
        var ln = c.localName || c.nodeName.replace(/^.*:/, "");
        if (ln === "RegistroAlta" || ln === "RegistroAnulacion" || ln === "RegistroEvento") els.push(c); else walk(c);
      }
    })(p.doc);
    if (!els.length) return { error: "No se ha encontrado ningún RegistroAlta, RegistroAnulacion ni RegistroEvento.", rows: [] };
    var rows = [], prev = { factura: null, evento: null }, prevN = { factura: 0, evento: 0 }, okAll = true;
    els.forEach(function (el, i) {
      var r = valoresRegistro(el), cadenaKey = r.tipo === "evento" ? "evento" : "factura";
      var calc = huella(r.tipo, r.valores), row = { n: i + 1, tipo: r.tipo, id: r.id, guardada: (r.guardada || "").trim(), calculada: calc.huella, cadena: calc.cadena, problemas: [], avisos: [] };
      if (!row.guardada) row.problemas.push("El registro no incluye su huella.");
      else if (row.guardada !== calc.huella) {
        var alt = null;
        if (r.tipo === "alta") variantesImporte(r.valores[4]).forEach(function (c4) { variantesImporte(r.valores[5]).forEach(function (c5) {
          if (alt) return; var v = r.valores.slice(); v[4] = c4; v[5] = c5; var hh = huella("alta", v); if (hh.huella === row.guardada) alt = hh; }); });
        if (alt) row.avisos.push("La huella coincide si los importes se escriben con otro número de decimales (" + alt.cadena.match(/CuotaTotal=[^&]*&ImporteTotal=[^&]*/)[0] + "). La AEAT considera equivalentes 1 o 2 decimales, pero conviene usar el mismo valor que en el XML.");
        else row.problemas.push("La huella guardada no coincide con la calculada: algún dato del registro o del orden de campos no cuadra.");
      }
      if (row.guardada && !RE_HASH.test(row.guardada)) row.problemas.push("La huella debe tener 64 caracteres hexadecimales en MAYÚSCULAS.");
      var last = prev[cadenaKey];
      if (r.primero) { if (last) row.avisos.push("Marcado como primer registro, pero no es el primero de la cadena en este fichero."); }
      else if (!r.anterior) row.problemas.push("Falta el encadenamiento: debe indicar PrimerRegistro=S o la huella del registro anterior.");
      else if (last && r.anterior.trim() !== last) row.problemas.push("Cadena rota: la huella anterior indicada no coincide con la del registro " + prevN[cadenaKey] + ".");
      else if (!last) row.avisos.push("La huella anterior apunta a un registro que no está en este fichero (no se puede comprobar el eslabón).");
      prev[cadenaKey] = row.guardada || calc.huella; prevN[cadenaKey] = i + 1;
      if (row.problemas.length) okAll = false;
      rows.push(row);
    });
    return { ok: okAll, rows: rows };
  }

  // Comprobación estructural básica de un RegistroAlta (orden, obligatorios, formatos, totales y huella)
  var ORDEN_ALTA = ["IDVersion", "IDFactura", "RefExterna", "NombreRazonEmisor", "Subsanacion", "RechazoPrevio", "TipoFactura", "TipoRectificativa", "FacturasRectificadas", "FacturasSustituidas", "ImporteRectificacion", "FechaOperacion", "DescripcionOperacion", "FacturaSimplificadaArt7273", "FacturaSinIdentifDestinatarioArt61d", "Macrodato", "EmitidaPorTerceroODestinatario", "Tercero", "Destinatarios", "Cupon", "Desglose", "CuotaTotal", "ImporteTotal", "Encadenamiento", "SistemaInformatico", "FechaHoraHusoGenRegistro", "NumRegistroAcuerdoFacturacion", "IdAcuerdoSistemaInformatico", "TipoHuella", "Huella", "Signature"];
  var OBLIG_ALTA = ["IDVersion", "IDFactura", "NombreRazonEmisor", "TipoFactura", "DescripcionOperacion", "Desglose", "CuotaTotal", "ImporteTotal", "Encadenamiento", "SistemaInformatico", "FechaHoraHusoGenRegistro", "TipoHuella", "Huella"];
  var RE_IMP = /^[+-]?\d{1,12}(\.\d{0,2})?$/;
  function checkAltaXml(text, DP) {
    var p = parseXml(text, DP), res = { ok: false, errors: [], warnings: [], notes: [], registros: 0 };
    if (p.error) { res.errors.push(p.error); return res; }
    var root = p.doc.documentElement, rl = root.localName || root.nodeName.replace(/^.*:/, "");
    if (rl !== "RegFactuSistemaFacturacion") res.warnings.push("El elemento raíz es «" + rl + "»; en un envío a la AEAT es «RegFactuSistemaFacturacion» (dentro del sobre SOAP). Se analizan los RegistroAlta que contenga.");
    else {
      if (root.namespaceURI !== NS_LR) res.errors.push("Espacio de nombres del elemento raíz incorrecto: se espera " + NS_LR);
      var cab = kid(root, "Cabecera");
      if (!cab) res.errors.push("Falta Cabecera (con ObligadoEmision: NombreRazon y NIF).");
      else if (!txt(cab, "ObligadoEmision/NIF")) res.errors.push("Cabecera: falta ObligadoEmision/NIF.");
    }
    var altas = allByLocal(p.doc, "RegistroAlta");
    res.registros = altas.length;
    if (!altas.length) { res.errors.push("No hay ningún RegistroAlta."); return res; }
    if (altas.length > 1000) res.errors.push("Un envío admite como máximo 1000 registros.");
    altas.forEach(function (el, idx) {
      var pre = altas.length > 1 ? "Registro " + (idx + 1) + ": " : "";
      if (el.namespaceURI !== NS_SF) res.errors.push(pre + "RegistroAlta debe estar en el espacio de nombres de SuministroInformacion.xsd.");
      var ch = elementChildren(el), pos = -1;
      ch.forEach(function (c) {
        var i = ORDEN_ALTA.indexOf(c);
        if (i < 0) res.errors.push(pre + "Elemento no previsto en RegistroAlta: " + c + ".");
        else if (i < pos) res.errors.push(pre + "Orden incorrecto: «" + c + "» debe ir antes de «" + ORDEN_ALTA[pos] + "».");
        else pos = i;
      });
      OBLIG_ALTA.forEach(function (o) { if (ch.indexOf(o) < 0) res.errors.push(pre + "Falta el elemento obligatorio " + o + "."); });
      if (txt(el, "IDVersion") && txt(el, "IDVersion") !== "1.0") res.errors.push(pre + "IDVersion debe ser 1.0.");
      var nif = txt(el, "IDFactura/IDEmisorFactura"), ns = txt(el, "IDFactura/NumSerieFactura"), fe = txt(el, "IDFactura/FechaExpedicionFactura");
      if (!nif) res.errors.push(pre + "Falta IDFactura/IDEmisorFactura."); else if (nif.length !== 9) res.errors.push(pre + "IDEmisorFactura debe tener 9 caracteres."); else if (!checkNif(nif).ok) res.warnings.push(pre + "IDEmisorFactura " + nif + ": " + checkNif(nif).msg);
      if (!ns) res.errors.push(pre + "Falta IDFactura/NumSerieFactura."); else if (ns.length > 60) res.errors.push(pre + "NumSerieFactura supera 60 caracteres.");
      if (!fe || !normFecha(fe).ok || !/^\d{2}-\d{2}-\d{4}$/.test(fe)) res.errors.push(pre + "FechaExpedicionFactura debe ser una fecha DD-MM-AAAA válida.");
      var tf = txt(el, "TipoFactura");
      if (tf && ["F1", "F2", "F3", "R1", "R2", "R3", "R4", "R5"].indexOf(tf) < 0) res.errors.push(pre + "TipoFactura «" + tf + "» no válido.");
      if (/^R/.test(tf || "") && !txt(el, "TipoRectificativa")) res.errors.push(pre + "Las facturas rectificativas (R1–R5) requieren TipoRectificativa.");
      if (tf === "F1" && !kid(el, "Destinatarios")) res.warnings.push(pre + "Una factura completa F1 debe identificar al destinatario (Destinatarios).");
      var desc = txt(el, "DescripcionOperacion"); if (desc != null && desc.length > 500) res.errors.push(pre + "DescripcionOperacion supera 500 caracteres.");
      var dets = kids(kid(el, "Desglose"), "DetalleDesglose"), sumC = 0, sumB = 0;
      if (kid(el, "Desglose") && !dets.length) res.errors.push(pre + "Desglose debe contener al menos un DetalleDesglose.");
      if (dets.length > 12) res.errors.push(pre + "Máximo 12 DetalleDesglose.");
      dets.forEach(function (dd, j) {
        var cal = txt(dd, "CalificacionOperacion"), ex = txt(dd, "OperacionExenta"), b = txt(dd, "BaseImponibleOimporteNoSujeto"), c = txt(dd, "CuotaRepercutida");
        var pj = pre + "DetalleDesglose " + (j + 1) + ": ";
        if (!cal && !ex) res.errors.push(pj + "falta CalificacionOperacion u OperacionExenta.");
        if (cal && ex) res.errors.push(pj + "CalificacionOperacion y OperacionExenta son excluyentes.");
        if (cal && ["S1", "S2", "N1", "N2"].indexOf(cal) < 0) res.errors.push(pj + "CalificacionOperacion «" + cal + "» no válida.");
        if (ex && ["E1", "E2", "E3", "E4", "E5", "E6"].indexOf(ex) < 0) res.errors.push(pj + "OperacionExenta «" + ex + "» no válida.");
        if (b == null || !RE_IMP.test(b)) res.errors.push(pj + "BaseImponibleOimporteNoSujeto obligatoria con formato 12.2.");
        if (c != null && !RE_IMP.test(c)) res.errors.push(pj + "CuotaRepercutida con formato incorrecto.");
        if (cal === "S1" && c == null) res.warnings.push(pj + "una operación S1 normalmente informa TipoImpositivo y CuotaRepercutida.");
        sumB += +b || 0; sumC += +c || 0; sumC += +(txt(dd, "CuotaRecargoEquivalencia") || 0);
      });
      var ct = txt(el, "CuotaTotal"), it = txt(el, "ImporteTotal");
      if (ct != null && !RE_IMP.test(ct)) res.errors.push(pre + "CuotaTotal con formato incorrecto (número con punto decimal y máximo 2 decimales).");
      if (it != null && !RE_IMP.test(it)) res.errors.push(pre + "ImporteTotal con formato incorrecto.");
      if (ct != null && dets.length && Math.abs(+ct - sumC) > 0.01) res.warnings.push(pre + "CuotaTotal (" + ct + ") no coincide con la suma de cuotas del desglose (" + money(sumC) + ").");
      if (it != null && dets.length && Math.abs(+it - (sumB + sumC)) > 0.01) res.warnings.push(pre + "ImporteTotal (" + it + ") no coincide con bases + cuotas (" + money(sumB + sumC) + "). Puede ser correcto si hay suplidos o retenciones; revísalo.");
      var enc = kid(el, "Encadenamiento");
      if (enc) {
        var pr = kid(enc, "PrimerRegistro"), ra = kid(enc, "RegistroAnterior");
        if (!!pr === !!ra) res.errors.push(pre + "Encadenamiento debe contener PrimerRegistro (S) o RegistroAnterior, pero no ambos.");
        if (pr && txt(pr) !== "S") res.errors.push(pre + "PrimerRegistro solo admite el valor S.");
        if (ra) ["IDEmisorFactura", "NumSerieFactura", "FechaExpedicionFactura", "Huella"].forEach(function (f) { if (!txt(ra, f)) res.errors.push(pre + "RegistroAnterior: falta " + f + "."); });
        if (ra && txt(ra, "Huella") && !RE_HASH.test(txt(ra, "Huella"))) res.errors.push(pre + "RegistroAnterior/Huella debe ser hexadecimal de 64 caracteres en mayúsculas.");
      }
      var si = kid(el, "SistemaInformatico");
      if (si) {
        ["NombreRazon", "IdSistemaInformatico", "Version", "NumeroInstalacion"].forEach(function (f) { if (!txt(si, f)) res.errors.push(pre + "SistemaInformatico: falta " + f + "."); });
        if (!txt(si, "NIF") && !kid(si, "IDOtro")) res.errors.push(pre + "SistemaInformatico: falta NIF (o IDOtro) del productor.");
        var ids = txt(si, "IdSistemaInformatico"); if (ids && ids.length > 2) res.errors.push(pre + "IdSistemaInformatico admite como máximo 2 caracteres.");
      }
      var ts = txt(el, "FechaHoraHusoGenRegistro"); if (ts && !RE_TS.test(ts)) res.errors.push(pre + "FechaHoraHusoGenRegistro debe incluir el huso horario (p. ej. 2026-11-13T10:15:00+01:00).");
      if (txt(el, "TipoHuella") && txt(el, "TipoHuella") !== "01") res.errors.push(pre + "TipoHuella debe ser 01 (SHA-256).");
      var hv = valoresRegistro(el), calc = huella("alta", hv.valores), g = txt(el, "Huella");
      if (g && g.trim() !== calc.huella) res.errors.push(pre + "La Huella no coincide con la calculada (" + calc.huella + "). Revisa los campos que intervienen en el cálculo.");
      else if (g) res.notes.push(pre + "Huella correcta: " + calc.huella);
    });
    res.ok = res.errors.length === 0;
    return res;
  }

  return {
    esc: esc, sha256: sha256, FIELDS: FIELDS, cadena: cadena, huella: huella, avisosHuella: avisosHuella, EJEMPLOS: EJEMPLOS, RE_HASH: RE_HASH,
    checkNif: checkNif, normImporte: normImporte, normFecha: normFecha, ahoraMadrid: ahoraMadrid,
    buildQrUrl: buildQrUrl, parseQrUrl: parseQrUrl, encodeParam: encodeParam, base: base, ERRORES: ERRORES,
    buildAlta: buildAlta, checkAltaXml: checkAltaXml, checkChain: checkChain, parseXml: parseXml, NS_LR: NS_LR, NS_SF: NS_SF
  };
});
