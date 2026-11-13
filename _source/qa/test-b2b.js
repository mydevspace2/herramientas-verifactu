// Pruebas unitarias de b2b.js: PMP (Resolución ICAC 29/01/2016, art. 5), intereses de demora (Ley 3/2004 arts. 7 y 8),
// plazo de 4 días (RD 238/2026 arts. 10.3 y 12.3) y fechas de la factura electrónica B2B. Uso: node qa/test-b2b.js
const assert = require("assert"), path = require("path"), fs = require("fs");
const B = require(path.join(__dirname, "../build/assets-src/b2b.js"));
let pass = 0, fail = 0;
function t(name, fn) { try { fn(); pass++; console.log("  ✓ " + name); } catch (e) { fail++; console.log("  ✗ " + name + "\n      " + e.message); } }
const near = (a, b, eps, m) => assert.ok(Math.abs(a - b) <= (eps || 1e-9), (m || "") + " " + a + " ≠ " + b);

console.log("Fechas, importes y CSV");
t("parseDate: AAAA-MM-DD, DD/MM/AAAA, DD-MM-AA; rechaza 31/02", () => {
  assert.strictEqual(B.iso(B.parseDate("2025-03-01")), "2025-03-01");
  assert.strictEqual(B.iso(B.parseDate("1/3/2025")), "2025-03-01");
  assert.strictEqual(B.iso(B.parseDate("01-03-25")), "2025-03-01");
  assert.strictEqual(B.parseDate("31/02/2025"), null); assert.strictEqual(B.parseDate(""), null);
});
t("parseAmount: 1.234,56 · 1234,56 · 1,234.56 · 1 234,56 € · 1.234 · 12.5 · -50", () => {
  [["1.234,56", 1234.56], ["1234,56", 1234.56], ["1,234.56", 1234.56], ["1 234,56 €", 1234.56], ["1.234", 1234], ["12.5", 12.5], ["-50", -50], ["1.234.567", 1234567]].forEach(([s, v]) => near(B.parseAmount(s), v, 1e-9, s));
  assert.strictEqual(B.parseAmount("abc"), null);
});
t("fmt: formato español con miles y coma decimal", () => { assert.strictEqual(B.fmt(1234567.891), "1.234.567,89"); assert.strictEqual(B.fmt(-5, 1), "-5,0"); });
t("parseCsv: separador ; , y tabulador, comillas", () => {
  assert.deepStrictEqual(B.parseCsv('a;b;"c;d"\n1;2;3'), [["a", "b", "c;d"], ["1", "2", "3"]]);
  assert.deepStrictEqual(B.parseCsv("a,b\n1,2"), [["a", "b"], ["1", "2"]]);
  assert.deepStrictEqual(B.parseCsv("a\tb\n1\t2"), [["a", "b"], ["1", "2"]]);
});

console.log("PMP – método ICAC (BOE-A-2016-1112, art. 5)");
// Ejemplo resuelto a mano (cierre 31/12/2025):
// 1) 1.000 € recibido 10/01 pagado 09/02 → 30 días   2) 2.000 € 01/03 → 10/05 = 70 días
// 3) 500 € 15/11 pendiente → 46 días al cierre      4) 1.500 € 01/12 pagado 20/01/2026 (tras el cierre) → pendiente, 30 días
// Ratio pagadas = (30·1000 + 70·2000) / 3000 = 56,6667 · Ratio pendientes = (46·500 + 30·1500) / 2000 = 34
// PMP = (56,6667·3000 + 34·2000) / 5000 = 47,60 días
const EJ = [
  { factura: "A-1", importe: "1.000,00", inicio: "10/01/2025", pago: "09/02/2025" },
  { factura: "A-2", importe: "2000", inicio: "2025-03-01", pago: "2025-05-10" },
  { factura: "A-3", importe: "500", inicio: "15/11/2025", pago: "" },
  { factura: "A-4", importe: "1500", inicio: "01/12/2025", pago: "20/01/2026" },
];
const R = B.pmp(EJ, { cierre: "2025-12-31", limite: 60 });
t("Ejemplo 1: ratio pagadas 56,67 · pendientes 34,00 · PMP 47,60", () => {
  assert.ok(R.ok, R.errors.join());
  near(R.pagadas.ratio, 170000 / 3000); near(R.pendientes.ratio, 34); near(R.pmp, 47.6, 1e-9);
  assert.strictEqual(R.pagadas.importe, 3000); assert.strictEqual(R.pendientes.importe, 2000);
});
t("Ejemplo 1: días por operación (30, 70, 46, 30) y la pagada tras el cierre cuenta como pendiente", () => {
  assert.deepStrictEqual(R.detail.map(d => d.dias), [30, 70, 46, 30]);
  assert.deepStrictEqual(R.detail.map(d => d.estado), ["pagada", "pagada", "pendiente", "pendiente"]);
});
t("Ejemplo 1: DA 3.ª Ley 15/2010 – pagadas dentro de 60 días: 1 de 2 facturas (50 %) y 1.000 de 3.000 € (33,33 %)", () => {
  assert.strictEqual(R.dentro.n, 1); near(R.dentro.pctN, 50); near(R.dentro.pctImporte, 100 / 3, 1e-9); assert.strictEqual(R.supera, false);
});
t("Ejemplo 2 (supera 60 días): 10.000 € pagados a 90 días + 10.000 € pendientes 40 días → PMP 65", () => {
  const r = B.pmp([{ importe: "10000", inicio: "2025-01-01", pago: "2025-04-01" }, { importe: "10000", inicio: "2025-11-21", pago: "" }], { cierre: "2025-12-31" });
  assert.strictEqual(r.detail[0].dias, 90); assert.strictEqual(r.detail[1].dias, 40); near(r.pmp, 65); assert.strictEqual(r.supera, true); assert.strictEqual(r.dentro.n, 0);
});
t("Fórmula: PMP = media ponderada por importe de todos los días (identidad algebraica, 500 casos aleatorios)", () => {
  let seed = 7; const rnd = () => (seed = (seed * 16807) % 2147483647) / 2147483647;
  for (let k = 0; k < 500; k++) {
    const rows = [], n = 1 + Math.floor(rnd() * 12); let sw = 0, s = 0;
    for (let i = 0; i < n; i++) {
      const imp = Math.round(rnd() * 100000) / 100 + 1, ini = B.ymd(2025, 1, 1) + Math.floor(rnd() * 360) * 86400000;
      const paid = rnd() < 0.7, pago = paid ? ini + Math.floor(rnd() * 120) * 86400000 : null;
      rows.push({ importe: String(imp), inicio: B.iso(ini), pago: pago ? B.iso(pago) : "" });
      const end = pago && pago <= B.ymd(2025, 12, 31) ? pago : B.ymd(2025, 12, 31);
      s += imp; sw += imp * Math.round((end - ini) / 86400000);
    }
    near(B.pmp(rows, { cierre: "2025-12-31" }).pmp, sw / s, 1e-7);
  }
});
t("Filtros: operación posterior al cierre, pago anterior al ejercicio, fechas e importes no válidos → omitidos con aviso", () => {
  const r = B.pmp([{ importe: "100", inicio: "2026-01-05", pago: "" }, { importe: "100", inicio: "2024-12-01", pago: "2024-12-20" }, { importe: "x", inicio: "2025-01-01" }, { importe: "100", inicio: "2025-02-30" }, { importe: "200", inicio: "2025-06-01", pago: "2025-06-11" }],
    { cierre: "2025-12-31", apertura: "2025-01-01" });
  assert.strictEqual(r.warnings.length, 4); assert.strictEqual(r.pagadas.n, 1); near(r.pmp, 10);
});
t("Sin cierre o sin filas válidas → error", () => { assert.ok(!B.pmp(EJ, {}).ok); assert.ok(!B.pmp([], { cierre: "2025-12-31" }).ok); });
t("Modelo abreviado (art. 5.5): 50.000 / 400.000 × 365 = 45,625 días; saldo medio (40.000 + 60.000) / 2", () => {
  near(B.pmpAbreviado("50.000", "400.000").pmp, 45.625); near(B.saldoMedio("40.000", "60.000"), 50000); assert.ok(!B.pmpAbreviado("1", "0").ok);
});
t("CSV con cabecera de la plantilla, en otro orden, sin cabecera y fila pegada de Excel con texto", () => {
  const x = B.pmpRowsFromCsv("B-1\tProv\t1.000,00\t10/01/2025\t09/02/2025"); assert.strictEqual(x.rows.length, 1); assert.strictEqual(x.rows[0].proveedor, "Prov");
  const a = B.pmpRowsFromCsv("factura;proveedor;importe;fecha_inicio;fecha_pago\nA-1;Prov;1.000,00;10/01/2025;09/02/2025\n");
  assert.deepStrictEqual(a.rows[0], { factura: "A-1", proveedor: "Prov", importe: "1.000,00", inicio: "10/01/2025", pago: "09/02/2025" });
  const b = B.pmpRowsFromCsv("Fecha pago,Importe,Fecha recepción\n2025-02-09,1000,2025-01-10");
  assert.deepStrictEqual([b.rows[0].importe, b.rows[0].inicio, b.rows[0].pago], ["1000", "2025-01-10", "2025-02-09"]);
  const c = B.pmpRowsFromCsv("1000;10/01/2025;09/02/2025");
  assert.deepStrictEqual([c.rows[0].importe, c.rows[0].inicio, c.rows[0].pago], ["1000", "10/01/2025", "09/02/2025"]);
  near(B.pmp(a.rows, { cierre: "2025-12-31" }).pmp, 30);
});

console.log("Intereses de demora – Ley 3/2004, art. 7 (tipos del BOE)");
const boe = JSON.parse(fs.readFileSync(path.join(__dirname, "boe-tipos-demora.json"), "utf8"));
t("La tabla de tipos coincide con las 27 resoluciones del BOE descargadas (2.º sem. 2013 – 2.º sem. 2026)", () => {
  assert.strictEqual(B.TIPOS.length, 27);
  B.TIPOS.forEach(x => { const b = boe.find(z => z.semestre === x.y + "-" + x.s); assert.ok(b, x.y + "-" + x.s); assert.strictEqual(b.tipo, x.tipo, x.y + "-" + x.s); assert.strictEqual(b.boe, x.boe); near(b.tipo - b.bce, 8, 1e-9, "BCE + 8 puntos"); });
});
t("Tipos clave: 2.º sem. 2026 = 10,40 % (BOE-A-2026-14327); 1.º sem. 2026 = 10,15 %; 1.º sem. 2024 = 12,50 %", () => {
  assert.strictEqual(B.tipoDe(B.ymd(2026, 11, 13)).tipo, 10.4); assert.strictEqual(B.tipoDe(B.ymd(2026, 3, 1)).tipo, 10.15); assert.strictEqual(B.tipoDe(B.ymd(2024, 6, 30)).tipo, 12.5);
});
// 10.000 € vencidos el 15/06/2025, pagados el 14/08/2025: 15 días al 11,15 % (16–30 jun) + 45 días al 10,15 % (1 jul–14 ago)
// = 10000·0,1115·15/365 + 10000·0,1015·45/365 = 45,82 + 125,14 = 170,96 €
t("Ejemplo: 10.000 € vencidos 15/06/2025 y pagados 14/08/2025 → 60 días, 2 tramos, 170,96 €", () => {
  const r = B.interes("10.000", "2025-06-15", "2025-08-14");
  assert.ok(r.ok, r.errors.join()); assert.strictEqual(r.dias, 60);
  assert.deepStrictEqual(r.tramos.map(x => [x.dias, x.tipo]), [[15, 11.15], [45, 10.15]]);
  near(r.interesRed, 170.96, 1e-9);
});
t("Ejemplo: 2.420 € (IVA incluido) vencidos 31/12/2025 y pagados 31/01/2026 → 31 días al 10,15 % = 20,86 €", () => {
  const r = B.interes("2.420,00", "2025-12-31", "2026-01-31"); assert.strictEqual(r.dias, 31); near(r.interesRed, 20.86);
});
t("Pago en plazo → 0; tipo pactado sustituye al legal (art. 7.1)", () => {
  assert.ok(B.interes("100", "2025-01-10", "2025-01-10").enPlazo);
  const r = B.interes("1000", "2025-01-01", "2025-12-31", { pactado: "5" }); assert.strictEqual(r.dias, 364); near(r.interesRed, 49.86);
});
t("Fuera de la tabla: antes del 1/7/2013 error; 2027 sin publicar → error salvo «estimar»", () => {
  assert.ok(!B.interes("100", "2013-03-01", "2013-08-01").ok);
  const a = B.interes("1000", "2026-12-15", "2027-01-30"); assert.ok(!a.ok && /2027/.test(a.errors[0]));
  const b = B.interes("1000", "2026-12-15", "2027-01-30", { estimar: true }); assert.ok(b.ok && b.estimado); assert.strictEqual(b.tramos[1].tipo, 10.4);
});
t("Vencimiento (art. 4): 30 días por defecto; pactos > 60 días se limitan a 60", () => {
  assert.strictEqual(B.iso(B.vencimiento("2025-03-01").fecha), "2025-03-31");
  const v = B.vencimiento("2025-03-01", 90); assert.strictEqual(v.dias, 60); assert.strictEqual(v.warnings.length, 1);
});

console.log("Plazo de 4 días (RD 238/2026, arts. 10.3 y 12.3)");
t("Pascua: 2026-04-05, 2027-03-28, 2028-04-16", () => { assert.strictEqual(B.iso(B.pascua(2026)), "2026-04-05"); assert.strictEqual(B.iso(B.pascua(2027)), "2027-03-28"); assert.strictEqual(B.iso(B.pascua(2028)), "2028-04-16"); });
t("Viernes Santo calculado = el de la lista del BOE (2026: 3 abr; 2027: 26 mar)", () => {
  assert.ok(B.FESTIVOS[2026].dias.includes(B.iso(B.addDays(B.pascua(2026), -2)))); assert.ok(B.FESTIVOS[2027].dias.includes(B.iso(B.addDays(B.pascua(2027), -2))));
});
t("Pago el viernes 08/10/2027 → límite viernes 15/10/2027 (salta sábado, domingo y el 12 de octubre)", () => {
  const r = B.plazo4("2027-10-08"); assert.strictEqual(B.iso(r.fecha), "2027-10-15"); assert.strictEqual(r.saltados.length, 3); assert.strictEqual(r.provisional, false);
});
t("Pago el miércoles 22/12/2027 → límite martes 28/12/2027 (salta sábado 25, Navidad, y domingo 26)", () => { const r = B.plazo4("2027-12-22"); assert.strictEqual(B.iso(r.fecha), "2027-12-28"); assert.strictEqual(r.saltados.length, 2); });
t("Pago el jueves 30/12/2027 → límite miércoles 05/01/2028 (provisional: 2028 aún sin lista oficial)", () => { const r = B.plazo4("2027-12-30"); assert.strictEqual(B.iso(r.fecha), "2028-01-05"); assert.ok(r.provisional); });
t("Pago el lunes 06/11/2028 → viernes 10/11/2028 (año sin lista oficial: marcado provisional)", () => { const r = B.plazo4("2028-11-06"); assert.strictEqual(B.iso(r.fecha), "2028-11-10"); assert.ok(r.provisional); });
t("Festivo adicional del usuario (p. ej. autonómico) también se salta", () => { assert.strictEqual(B.iso(B.plazo4("2027-10-08", { extra: ["2027-10-13"] }).fecha), "2027-10-18"); });

console.log("Factura electrónica B2B – RD 238/2026 DF 4.ª, DT 2.ª y 3.ª; Orden HAC/1028/2026 en vigor el 06/10/2026");
t("Fechas: 06/10/2027 (> 8 M€), 06/10/2028 (resto), 06/10/2029 (estados, personas físicas ≤ 8 M€)", () => {
  assert.strictEqual(B.iso(B.ORDEN_VIGOR), "2026-10-06");
  assert.strictEqual(B.iso(B.FECHAS_B2B.grandes), "2027-10-06"); assert.strictEqual(B.iso(B.FECHAS_B2B.resto), "2028-10-06"); assert.strictEqual(B.iso(B.FECHAS_B2B.fisicasEstados), "2029-10-06");
});
t("Checker: grande → 2027 + PDF; sociedad pequeña → 2028; autónomo pequeño → emitir 2028, estados 2029; solo tiques → no emite", () => {
  const g = B.obligacionB2B({ b2b: "si", forma: "juridica", volumen: "mas", simplificadas: "no" });
  assert.strictEqual(B.iso(g.emitir), "2027-10-06"); assert.ok(g.pdf); assert.strictEqual(B.iso(g.estados), "2027-10-06");
  const s = B.obligacionB2B({ b2b: "si", forma: "juridica", volumen: "menos", simplificadas: "no" }); assert.strictEqual(B.iso(s.emitir), "2028-10-06"); assert.strictEqual(B.iso(s.estados), "2028-10-06"); assert.ok(!s.pdf);
  const a = B.obligacionB2B({ b2b: "si", forma: "fisica", volumen: "menos", simplificadas: "no" }); assert.strictEqual(B.iso(a.emitir), "2028-10-06"); assert.strictEqual(B.iso(a.estados), "2029-10-06");
  const q = B.obligacionB2B({ b2b: "si", forma: "fisica", volumen: "menos", simplificadas: "solo" }); assert.strictEqual(q.emitir, null); assert.strictEqual(B.iso(q.recibir), "2028-10-06");
});

console.log("\nResultado: " + pass + " correctas, " + fail + " fallidas");
process.exit(fail ? 1 : 0);
