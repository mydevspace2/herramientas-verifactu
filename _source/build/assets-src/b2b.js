/*! Herramientas Verifactu – cálculos B2B y morosidad (PMP método ICAC, intereses de demora Ley 3/2004,
 *  plazo de 4 días del RD 238/2026). Todo se ejecuta en el navegador. */
(function (root, factory) {
  var api = factory();
  if (typeof module === "object" && module.exports) module.exports = api;
  else root.B2B = api;
})(typeof self !== "undefined" ? self : this, function () {
  "use strict";
  var DAY = 86400000;

  // ---------- fechas (siempre en UTC, sin horas) ----------
  function ymd(y, m, d) { return Date.UTC(y, m - 1, d); }
  function parseDate(s) {
    if (s == null) return null;
    s = String(s).trim();
    if (!s) return null;
    var m = /^(\d{4})-(\d{1,2})-(\d{1,2})$/.exec(s), y, mo, d;
    if (m) { y = +m[1]; mo = +m[2]; d = +m[3]; }
    else {
      m = /^(\d{1,2})[\/.\-](\d{1,2})[\/.\-](\d{2}|\d{4})$/.exec(s);
      if (!m) return null;
      d = +m[1]; mo = +m[2]; y = +m[3]; if (y < 100) y += 2000;
    }
    var t = ymd(y, mo, d), dt = new Date(t);
    if (dt.getUTCFullYear() !== y || dt.getUTCMonth() !== mo - 1 || dt.getUTCDate() !== d) return null;
    return t;
  }
  function iso(t) { var d = new Date(t); return d.getUTCFullYear() + "-" + pad(d.getUTCMonth() + 1) + "-" + pad(d.getUTCDate()); }
  function es(t) { var d = new Date(t); return pad(d.getUTCDate()) + "/" + pad(d.getUTCMonth() + 1) + "/" + d.getUTCFullYear(); }
  var MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"];
  var DIAS = ["domingo", "lunes", "martes", "miércoles", "jueves", "viernes", "sábado"];
  function largo(t) { var d = new Date(t); return DIAS[d.getUTCDay()] + ", " + d.getUTCDate() + " de " + MESES[d.getUTCMonth()] + " de " + d.getUTCFullYear(); }
  function pad(n) { return (n < 10 ? "0" : "") + n; }
  function diffDays(a, b) { return Math.round((b - a) / DAY); }
  function addDays(t, n) { return t + n * DAY; }
  function todayUTC() { var n = new Date(); return ymd(n.getFullYear(), n.getMonth() + 1, n.getDate()); }

  // ---------- importes ----------
  // Acepta 1.234,56 · 1234,56 · 1234.56 · 1,234.56 · 1 234,56 · -50
  function parseAmount(s) {
    if (typeof s === "number") return isFinite(s) ? s : null;
    if (s == null) return null;
    s = String(s).replace(/[\s\u00a0€]/g, "");
    if (!s) return null;
    var neg = /^-/.test(s); s = s.replace(/^[-+]/, "");
    if (!/^[\d.,]+$/.test(s)) return null;
    var lc = s.lastIndexOf(","), ld = s.lastIndexOf(".");
    if (lc > -1 && ld > -1) {
      if (lc > ld) s = s.replace(/\./g, "").replace(",", ".");
      else s = s.replace(/,/g, "");
    } else if (lc > -1) {
      if ((s.match(/,/g) || []).length > 1) s = s.replace(/,/g, "");
      else s = s.replace(",", ".");
    } else if (ld > -1 && (s.match(/\./g) || []).length > 1) s = s.replace(/\./g, "");
    else if (ld > -1 && /^\d{1,3}\.\d{3}$/.test(s)) s = s.replace(".", ""); // 1.234 = mil doscientos treinta y cuatro (uso español)
    var v = parseFloat(s);
    return isFinite(v) ? (neg ? -v : v) : null;
  }
  function round2(x) { return Math.round((x + (x >= 0 ? 1e-9 : -1e-9)) * 100) / 100; }
  function fmt(x, dec) {
    dec = dec == null ? 2 : dec;
    var neg = x < 0, s = Math.abs(x).toFixed(dec), p = s.split(".");
    p[0] = p[0].replace(/\B(?=(\d{3})+(?!\d))/g, ".");
    return (neg ? "-" : "") + p.join(",");
  }

  // ---------- CSV ----------
  function splitCsvLine(line, sep) {
    var out = [], cur = "", q = false;
    for (var i = 0; i < line.length; i++) {
      var c = line[i];
      if (q) { if (c === '"') { if (line[i + 1] === '"') { cur += '"'; i++; } else q = false; } else cur += c; }
      else if (c === '"') q = true;
      else if (c === sep) { out.push(cur); cur = ""; }
      else cur += c;
    }
    out.push(cur);
    return out.map(function (x) { return x.trim(); });
  }
  function parseCsv(text) {
    text = String(text || "").replace(/^\ufeff/, "");
    var lines = text.split(/\r\n|\n|\r/).filter(function (l) { return l.trim() !== ""; });
    if (!lines.length) return [];
    var first = lines[0], sep = ";";
    var counts = { ";": (first.match(/;/g) || []).length, "\t": (first.match(/\t/g) || []).length, ",": (first.match(/,/g) || []).length };
    if (counts["\t"] > counts[";"] && counts["\t"] >= counts[","]) sep = "\t";
    else if (counts[";"] === 0 && counts[","] > 0) sep = ",";
    return lines.map(function (l) { return splitCsvLine(l, sep); });
  }

  // ---------- PMP: Resolución ICAC de 29/01/2016 (BOE-A-2016-1112), art. 5 ----------
  var PMP_HEAD = { factura: ["factura", "numero", "número", "num", "documento", "id"], proveedor: ["proveedor", "acreedor", "nombre"],
    importe: ["importe", "total", "importe total", "cantidad"], inicio: ["fecha_inicio", "inicio", "fecha inicio", "fecha recepcion", "fecha recepción", "recepcion", "recepción", "fecha entrega", "entrega", "fecha factura", "fecha"],
    pago: ["fecha_pago", "pago", "fecha pago", "fecha de pago", "pagado"] };
  function norm(s) { s = String(s || "").toLowerCase().trim(); return s.normalize ? s.normalize("NFD").replace(/[\u0300-\u036f]/g, "") : s; }
  function mapHeader(row) {
    var idx = {}, used = {};
    var keys = ["pago", "inicio", "importe", "proveedor", "factura"];
    keys.forEach(function (k) {
      for (var i = 0; i < row.length; i++) {
        if (used[i]) continue;
        var h = norm(row[i]);
        if (PMP_HEAD[k].some(function (x) { return norm(x) === h || (h.indexOf(norm(x)) > -1 && norm(x).length > 3); })) { idx[k] = i; used[i] = 1; break; }
      }
    });
    return idx;
  }
  // Filas CSV -> [{factura, proveedor, importe, inicio, pago}] (texto). Columnas por cabecera o, si no hay, en el orden de la plantilla.
  function pmpRowsFromCsv(text) {
    var rows = parseCsv(text), res = { rows: [], warnings: [] };
    if (!rows.length) return res;
    // una fila de datos siempre tiene al menos una fecha; la cabecera, ninguna
    var hasHead = !rows[0].some(function (c) { return parseDate(c) != null; });
    var idx = { factura: 0, proveedor: 1, importe: 2, inicio: 3, pago: 4 };
    if (hasHead) {
      var m = mapHeader(rows[0]);
      if (m.importe == null || m.inicio == null) res.warnings.push("No reconozco las columnas «importe» y «fecha_inicio» en la cabecera; uso el orden de la plantilla.");
      else idx = { factura: m.factura, proveedor: m.proveedor, importe: m.importe, inicio: m.inicio, pago: m.pago };
      rows = rows.slice(1);
    } else if (rows[0].length < 5) {
      idx = rows[0].length === 3 ? { importe: 0, inicio: 1, pago: 2 } : { factura: 0, importe: 1, inicio: 2, pago: 3 };
    }
    rows.forEach(function (r) {
      function g(k) { return idx[k] == null ? "" : (r[idx[k]] || ""); }
      res.rows.push({ factura: g("factura"), proveedor: g("proveedor"), importe: g("importe"), inicio: g("inicio"), pago: g("pago") });
    });
    return res;
  }

  /* opts: { cierre: "AAAA-MM-DD" (obligatorio), apertura: "AAAA-MM-DD" (opcional), limite: 60 }
     rows: [{factura, proveedor, importe, inicio, pago}] con importe y fechas en texto o número.
     Devuelve las ratios del art. 5.2 y 5.3, el PMP del art. 5.1 y la información adicional de la DA 3.ª Ley 15/2010. */
  function pmp(rows, opts) {
    opts = opts || {};
    var cierre = parseDate(opts.cierre), apertura = opts.apertura ? parseDate(opts.apertura) : null;
    var limite = opts.limite == null ? 60 : +opts.limite;
    var r = { ok: false, errors: [], warnings: [], detail: [], pagadas: { n: 0, importe: 0, suma: 0, ratio: 0 }, pendientes: { n: 0, importe: 0, suma: 0, ratio: 0 },
      dentro: { n: 0, importe: 0, pctN: 0, pctImporte: 0 }, limite: limite, pmp: 0 };
    if (cierre == null) { r.errors.push("Indica la fecha de cierre del ejercicio."); return r; }
    if (apertura != null && apertura > cierre) { r.errors.push("La fecha de inicio del ejercicio es posterior a la de cierre."); return r; }
    (rows || []).forEach(function (row, i) {
      var n = i + 1, id = row.factura ? "«" + row.factura + "»" : "fila " + n;
      var blank = !String(row.importe || "").trim() && !String(row.inicio || "").trim() && !String(row.pago || "").trim();
      if (blank) return;
      var imp = parseAmount(row.importe), ini = parseDate(row.inicio), pag = String(row.pago || "").trim() ? parseDate(row.pago) : null;
      var d = { n: n, factura: row.factura || "", proveedor: row.proveedor || "", importe: imp, inicio: ini, pago: pag, estado: "", dias: null };
      if (imp == null) { r.warnings.push(id + ": importe no válido; se omite."); d.estado = "omitida"; r.detail.push(d); return; }
      if (ini == null) { r.warnings.push(id + ": fecha de inicio del cómputo no válida; se omite."); d.estado = "omitida"; r.detail.push(d); return; }
      if (String(row.pago || "").trim() && pag == null) { r.warnings.push(id + ": fecha de pago no válida; se omite."); d.estado = "omitida"; r.detail.push(d); return; }
      if (ini > cierre) { r.warnings.push(id + ": la operación empieza después del cierre; no entra en este ejercicio."); d.estado = "omitida"; r.detail.push(d); return; }
      if (pag != null && apertura != null && pag < apertura) { r.warnings.push(id + ": se pagó antes del inicio del ejercicio; no entra en este ejercicio."); d.estado = "omitida"; r.detail.push(d); return; }
      if (imp < 0) r.warnings.push(id + ": importe negativo (abono). Se incluye tal cual; revisa si debe restarse de la factura original.");
      if (pag != null && pag <= cierre) {
        d.estado = "pagada"; d.dias = diffDays(ini, pag);
        if (d.dias < 0) r.warnings.push(id + ": pago anterior a la fecha de inicio del cómputo (" + d.dias + " días). Revisa las fechas o si es un anticipo.");
        r.pagadas.n++; r.pagadas.importe += imp; r.pagadas.suma += d.dias * imp;
        if (d.dias <= limite) { r.dentro.n++; r.dentro.importe += imp; }
      } else {
        d.estado = "pendiente"; d.dias = diffDays(ini, cierre);
        if (pag != null) d.nota = "pagada después del cierre";
        r.pendientes.n++; r.pendientes.importe += imp; r.pendientes.suma += d.dias * imp;
      }
      r.detail.push(d);
    });
    var tp = r.pagadas.importe, tq = r.pendientes.importe;
    if (r.pagadas.n + r.pendientes.n === 0) { r.errors.push("No hay ninguna operación válida para calcular."); return r; }
    r.pagadas.ratio = tp ? r.pagadas.suma / tp : 0;
    r.pendientes.ratio = tq ? r.pendientes.suma / tq : 0;
    if (tp + tq === 0) { r.errors.push("La suma de importes es cero; no se puede calcular el PMP."); return r; }
    r.pmp = (r.pagadas.ratio * tp + r.pendientes.ratio * tq) / (tp + tq);
    r.dentro.pctN = r.pagadas.n ? r.dentro.n / r.pagadas.n * 100 : 0;
    r.dentro.pctImporte = tp ? r.dentro.importe / tp * 100 : 0;
    r.supera = r.pmp > 60;
    r.ok = true;
    return r;
  }
  // Modelo abreviado / PGC Pymes (art. 5.5): saldo medio acreedores comerciales / compras netas y gastos por servicios exteriores × 365
  function pmpAbreviado(saldoMedio, compras) {
    var s = parseAmount(saldoMedio), c = parseAmount(compras), r = { ok: false, errors: [] };
    if (s == null || s < 0) r.errors.push("Saldo medio de acreedores comerciales no válido.");
    if (c == null || c <= 0) r.errors.push("Compras netas y gastos por servicios exteriores deben ser mayores que cero.");
    if (r.errors.length) return r;
    r.pmp = s / c * 365; r.ok = true; r.supera = r.pmp > 60;
    return r;
  }
  function saldoMedio(inicial, final) {
    var a = parseAmount(inicial), b = parseAmount(final);
    return a == null || b == null ? null : (a + b) / 2;
  }

  // ---------- Interés de demora comercial: art. 7 Ley 3/2004 ----------
  // Tipo legal publicado cada semestre en el BOE (BCE + 8 puntos). Fuente: resoluciones del Tesoro citadas en "boe".
  var TIPOS = [
    ["2013-2", 8.50, "BOE-A-2013-7090"], ["2014-1", 8.25, "BOE-A-2013-13835"], ["2014-2", 8.15, "BOE-A-2014-6914"],
    ["2015-1", 8.05, "BOE-A-2014-13716"], ["2015-2", 8.05, "BOE-A-2015-7292"], ["2016-1", 8.05, "BOE-A-2015-14331"],
    ["2016-2", 8.00, "BOE-A-2016-6299"], ["2017-1", 8.00, "BOE-A-2016-12482"], ["2017-2", 8.00, "BOE-A-2017-7469"],
    ["2018-1", 8.00, "BOE-A-2017-15428"], ["2018-2", 8.00, "BOE-A-2018-9001"], ["2019-1", 8.00, "BOE-A-2018-17661"],
    ["2019-2", 8.00, "BOE-A-2019-9730"], ["2020-1", 8.00, "BOE-A-2019-18736"], ["2020-2", 8.00, "BOE-A-2020-6848"],
    ["2021-1", 8.00, "BOE-A-2020-17415"], ["2021-2", 8.00, "BOE-A-2021-10869"], ["2022-1", 8.00, "BOE-A-2021-21959"],
    ["2022-2", 8.00, "BOE-A-2022-10844"], ["2023-1", 10.50, "BOE-A-2022-24416"], ["2023-2", 12.00, "BOE-A-2023-15221"],
    ["2024-1", 12.50, "BOE-A-2023-26709"], ["2024-2", 12.25, "BOE-A-2024-13089"], ["2025-1", 11.15, "BOE-A-2024-27618"],
    ["2025-2", 10.15, "BOE-A-2025-13217"], ["2026-1", 10.15, "BOE-A-2025-27201"], ["2026-2", 10.40, "BOE-A-2026-14327"]
  ].map(function (x) { var p = x[0].split("-"); return { y: +p[0], s: +p[1], tipo: x[1], boe: x[2] }; });
  var PRIMERO = ymd(2013, 7, 1);
  var ULTIMO = TIPOS[TIPOS.length - 1];
  var FIN_TABLA = ULTIMO.s === 1 ? ymd(ULTIMO.y, 6, 30) : ymd(ULTIMO.y, 12, 31);
  function semestre(t) { var d = new Date(t); return { y: d.getUTCFullYear(), s: d.getUTCMonth() < 6 ? 1 : 2 }; }
  function tipoDe(t) {
    var s = semestre(t);
    for (var i = 0; i < TIPOS.length; i++) if (TIPOS[i].y === s.y && TIPOS[i].s === s.s) return TIPOS[i];
    return null;
  }
  function finSemestre(t) { var s = semestre(t); return s.s === 1 ? ymd(s.y, 6, 30) : ymd(s.y, 12, 31); }
  /* Interés simple, base 365: devenga desde el día siguiente al vencimiento hasta el día del pago (ambos incluidos),
     cada día al tipo del semestre natural en que cae. opts: { pactado: % anual (si hay pacto, art. 7.1), estimar: true usa el último tipo publicado después de la tabla } */
  function interes(importe, venc, pago, opts) {
    opts = opts || {};
    var p = parseAmount(importe), v = typeof venc === "number" ? venc : parseDate(venc), f = typeof pago === "number" ? pago : parseDate(pago);
    var r = { ok: false, errors: [], tramos: [], dias: 0, interes: 0, estimado: false };
    if (p == null || p <= 0) r.errors.push("Importe no válido.");
    if (v == null) r.errors.push("Fecha de vencimiento no válida.");
    if (f == null) r.errors.push("Fecha de pago no válida.");
    if (r.errors.length) return r;
    if (f <= v) { r.ok = true; r.enPlazo = true; return r; }
    var pact = opts.pactado != null && opts.pactado !== "" ? parseAmount(opts.pactado) : null;
    if (opts.pactado != null && opts.pactado !== "" && (pact == null || pact < 0)) { r.errors.push("Tipo pactado no válido."); return r; }
    var d = addDays(v, 1);
    if (pact == null && d < PRIMERO) { r.errors.push("La tabla de tipos de esta calculadora empieza el 1 de julio de 2013. Para periodos anteriores usa el tipo publicado en el BOE de ese semestre."); return r; }
    while (d <= f) {
      var fin = Math.min(finSemestre(d), f), n = diffDays(d, fin) + 1, t, ref;
      if (pact != null) { t = pact; ref = "pactado"; }
      else {
        var x = tipoDe(d);
        if (!x) {
          if (!opts.estimar) { r.errors.push("Aún no se ha publicado en el BOE el tipo del " + semestre(d).s + ".º semestre de " + semestre(d).y + ". Marca «estimar con el último tipo publicado» o limita la fecha de pago."); r.tramos = []; return r; }
          x = { tipo: ULTIMO.tipo, boe: ULTIMO.boe, y: semestre(d).y, s: semestre(d).s }; r.estimado = true; ref = "estimado";
        } else ref = x.boe;
        t = x.tipo;
      }
      var i = p * t / 100 * n / 365;
      r.tramos.push({ desde: d, hasta: fin, dias: n, tipo: t, boe: ref, interes: i });
      r.dias += n; r.interes += i;
      d = addDays(fin, 1);
    }
    r.interesRed = round2(r.interes);
    r.ok = true;
    return r;
  }
  // Vencimiento legal (art. 4 Ley 3/2004): 30 días desde la recepción si no hay pacto; con pacto, máximo 60.
  function vencimiento(entrega, dias) {
    var e = parseDate(entrega), n = dias == null || dias === "" ? 30 : parseInt(dias, 10), r = { ok: false, errors: [], warnings: [] };
    if (e == null) r.errors.push("Fecha de entrega o prestación no válida.");
    if (!(n >= 0)) r.errors.push("Plazo en días no válido.");
    if (r.errors.length) return r;
    if (n > 60) { r.warnings.push("La ley no permite pactar más de 60 días naturales (art. 4.3 Ley 3/2004): se usa 60."); n = 60; }
    r.dias = n; r.fecha = addDays(e, n); r.ok = true;
    return r;
  }

  // ---------- Plazo de 4 días (arts. 10.3 y 12.3 RD 238/2026) ----------
  // «Festivos nacionales»: fiestas de ámbito nacional comunes a todo el territorio en la relación publicada en el BOE.
  var FESTIVOS = {
    2026: { boe: "BOE-A-2025-21667", oficial: true, dias: ["2026-01-01", "2026-01-06", "2026-04-03", "2026-05-01", "2026-08-15", "2026-10-12", "2026-12-08", "2026-12-25"] },
    2027: { boe: "BOE-A-2026-21254", oficial: true, dias: ["2027-01-01", "2027-01-06", "2027-03-26", "2027-05-01", "2027-10-12", "2027-11-01", "2027-12-06", "2027-12-08", "2027-12-25"] }
  };
  function pascua(y) { // algoritmo de Meeus/Jones/Butcher (calendario gregoriano)
    var a = y % 19, b = Math.floor(y / 100), c = y % 100, d = Math.floor(b / 4), e = b % 4, f = Math.floor((b + 8) / 25), g = Math.floor((b - f + 1) / 3),
      h = (19 * a + b - d - g + 15) % 30, i = Math.floor(c / 4), k = c % 4, l = (32 + 2 * e + 2 * i - h - k) % 7, m = Math.floor((a + 11 * h + 22 * l) / 451),
      mo = Math.floor((h + l - 7 * m + 114) / 31), da = ((h + l - 7 * m + 114) % 31) + 1;
    return ymd(y, mo, da);
  }
  // Para años sin relación publicada: solo las fiestas nacionales no sustituibles (las marcadas con * en las relaciones del BOE).
  function festivosAnio(y) {
    if (FESTIVOS[y]) return { oficial: true, boe: FESTIVOS[y].boe, dias: FESTIVOS[y].dias.map(parseDate) };
    var f = [ymd(y, 1, 1), addDays(pascua(y), -2), ymd(y, 5, 1), ymd(y, 8, 15), ymd(y, 10, 12), ymd(y, 11, 1), ymd(y, 12, 6), ymd(y, 12, 8), ymd(y, 12, 25)];
    return { oficial: false, boe: null, dias: f };
  }
  function esFestivo(t, extra) {
    var y = new Date(t).getUTCFullYear(), f = festivosAnio(y).dias;
    if (f.indexOf(t) > -1) return true;
    return !!(extra && extra.indexOf(t) > -1);
  }
  function habil(t, extra) { var w = new Date(t).getUTCDay(); return w !== 0 && w !== 6 && !esFestivo(t, extra); }
  /* Último día para informar: 4 días contados desde el día siguiente al hecho, excluyendo sábados, domingos y festivos nacionales. */
  function plazo4(fecha, opts) {
    opts = opts || {};
    var t = typeof fecha === "number" ? fecha : parseDate(fecha), n = opts.dias || 4, extra = (opts.extra || []).map(function (x) { return typeof x === "number" ? x : parseDate(x); }).filter(function (x) { return x != null; });
    var r = { ok: false, errors: [], saltados: [], computados: [], provisional: false };
    if (t == null) { r.errors.push("Fecha no válida."); return r; }
    var d = t, c = 0;
    while (c < n) {
      d = addDays(d, 1);
      if (!festivosAnio(new Date(d).getUTCFullYear()).oficial) r.provisional = true;
      if (habil(d, extra)) { c++; r.computados.push(d); }
      else r.saltados.push(d);
    }
    r.fecha = d; r.ok = true;
    return r;
  }

  // ---------- factura electrónica B2B: RD 238/2026 + Orden HAC/1028/2026 ----------
  var ORDEN_VIGOR = ymd(2026, 10, 6);
  var FECHAS_B2B = { grandes: ymd(2027, 10, 6), resto: ymd(2028, 10, 6), fisicasEstados: ymd(2029, 10, 6) };
  /* a: { b2b: "si"|"no", forma: "juridica"|"fisica", volumen: "mas"|"menos", simplificadas: "solo"|"no" } */
  function obligacionB2B(a) {
    var r = { emitir: null, recibir: null, estados: null, pdf: false, notas: [] };
    var grande = a.volumen === "mas";
    r.recibir = grande ? FECHAS_B2B.grandes : FECHAS_B2B.resto;
    if (a.b2b === "no") r.notas.push("sin-b2b");
    else if (a.simplificadas === "solo") r.notas.push("simplificadas");
    else { r.emitir = r.recibir; if (grande) r.pdf = true; }
    r.estados = grande ? FECHAS_B2B.grandes : (a.forma === "fisica" ? FECHAS_B2B.fisicasEstados : FECHAS_B2B.resto);
    return r;
  }

  return {
    parseDate: parseDate, iso: iso, es: es, largo: largo, diffDays: diffDays, addDays: addDays, todayUTC: todayUTC, ymd: ymd,
    parseAmount: parseAmount, round2: round2, fmt: fmt, parseCsv: parseCsv, pmpRowsFromCsv: pmpRowsFromCsv,
    pmp: pmp, pmpAbreviado: pmpAbreviado, saldoMedio: saldoMedio,
    TIPOS: TIPOS, tipoDe: tipoDe, interes: interes, vencimiento: vencimiento, FIN_TABLA: FIN_TABLA,
    FESTIVOS: FESTIVOS, festivosAnio: festivosAnio, pascua: pascua, plazo4: plazo4, habil: habil,
    ORDEN_VIGOR: ORDEN_VIGOR, FECHAS_B2B: FECHAS_B2B, obligacionB2B: obligacionB2B
  };
});
