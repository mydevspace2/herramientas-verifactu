// Pruebas unitarias de assets-src/core.js y qr.js (Node). Uso: node qa/test-core.js
// Requiere @xmldom/xmldom (NODE_PATH con node_modules de qa).
const assert = require("assert"), crypto = require("crypto"), fs = require("fs"), path = require("path");
const VF = require("../build/assets-src/core.js");
const QR = require("../build/assets-src/qr.js");
const { DOMParser } = require("@xmldom/xmldom");
let pass = 0, fail = 0;
function t(name, fn) { try { fn(); pass++; console.log("  ✓ " + name); } catch (e) { fail++; console.log("  ✗ " + name + "\n      " + e.message); } }
const OUTDIR = path.join(__dirname, "out"); fs.mkdirSync(OUTDIR, { recursive: true });

console.log("Huella – ejemplos oficiales AEAT (doc. huella v0.1.2, apdo. 6)");
t("Caso 1 (alta, primer registro) = 3C464DAF…8F12F60", () => {
  const r = VF.huella("alta", ["89890001K", "12345678/G33", "01-01-2024", "F1", "12.35", "123.45", "", "2024-01-01T19:20:30+01:00"]);
  assert.strictEqual(r.cadena, "IDEmisorFactura=89890001K&NumSerieFactura=12345678/G33&FechaExpedicionFactura=01-01-2024&TipoFactura=F1&CuotaTotal=12.35&ImporteTotal=123.45&Huella=&FechaHoraHusoGenRegistro=2024-01-01T19:20:30+01:00");
  assert.strictEqual(r.huella, "3C464DAF61ACB827C65FDA19F352A4E3BDC2C640E9E9FC4CC058073F38F12F60");
});
t("Caso 2 (alta encadenada) = F7B94CFD…802A2B97", () => {
  const r = VF.huella("alta", ["89890001K", "12345679/G34", "01-01-2024", "F1", "12.35", "123.45", "3C464DAF61ACB827C65FDA19F352A4E3BDC2C640E9E9FC4CC058073F38F12F60", "2024-01-01T19:20:35+01:00"]);
  assert.strictEqual(r.huella, "F7B94CFD8924EDFF273501B01EE5153E4CE8F259766F88CF6ACB8935802A2B97");
});
t("Caso 3 (anulación) = 177547C0…88F90C68", () => {
  const r = VF.huella("anulacion", ["89890001K", "12345679/G34", "01-01-2024", "F7B94CFD8924EDFF273501B01EE5153E4CE8F259766F88CF6ACB8935802A2B97", "2024-01-01T19:20:40+01:00"]);
  assert.strictEqual(r.cadena, "IDEmisorFacturaAnulada=89890001K&NumSerieFacturaAnulada=12345679/G34&FechaExpedicionFacturaAnulada=01-01-2024&Huella=F7B94CFD8924EDFF273501B01EE5153E4CE8F259766F88CF6ACB8935802A2B97&FechaHoraHusoGenRegistro=2024-01-01T19:20:40+01:00");
  assert.strictEqual(r.huella, "177547C0D57AC74748561D054A9CEC14B4C4EA23D1BEFD6F2E69E3A388F90C68");
});
t("EJEMPLOS incluidos en la web coinciden con la AEAT", () => VF.EJEMPLOS.forEach(e => assert.strictEqual(VF.huella(e.tipo, e.valores).huella, e.huella)));
t("Recorta espacios iniciales y finales, no los interiores", () => {
  const a = VF.huella("alta", ["  89890001K ", " 12345678 / G33 ", "01-01-2024", "F1", "12.35", "123.45", "", "2024-01-01T19:20:30+01:00"]);
  assert.ok(a.cadena.includes("NumSerieFactura=12345678 / G33&") && a.cadena.startsWith("IDEmisorFactura=89890001K&"));
});
t("Evento: 9 campos en el orden oficial, NIF dos veces, ID vacío", () => {
  const r = VF.huella("evento", ["89890001K", "", "77", "1.0.03", "383", "89890001K", "01", "", "2024-01-01T19:20:30+01:00"]);
  assert.strictEqual(r.cadena, "NIF=89890001K&ID=&IdSistemaInformatico=77&Version=1.0.03&NumeroInstalacion=383&NIF=89890001K&TipoEvento=01&HuellaEvento=&FechaHoraHusoGenEvento=2024-01-01T19:20:30+01:00");
  assert.strictEqual(r.huella, crypto.createHash("sha256").update(r.cadena, "utf8").digest("hex").toUpperCase());
});
t("SHA-256 propio = crypto de Node (200 cadenas aleatorias, UTF-8, varias longitudes)", () => {
  for (let i = 0; i < 200; i++) {
    const s = crypto.randomBytes(i * 3).toString("base64") + (i % 3 ? "ñÁ€😀" : "") + "x".repeat(i % 70);
    assert.strictEqual(VF.sha256(s), crypto.createHash("sha256").update(s, "utf8").digest("hex").toUpperCase());
  }
});
t("avisosHuella detecta fecha sin huso y huella anterior en minúsculas", () => {
  const w = VF.avisosHuella("alta", ["89890001K", "1", "01-01-2024", "F1", "1", "1", "abc", "2024-01-01 19:20"]);
  assert.ok(w.some(x => /Huella/.test(x)) && w.some(x => /FechaHoraHuso/.test(x)));
});

console.log("NIF / NIE / CIF");
t("DNI y NIF especial AEAT de pruebas 89890001K", () => assert.ok(VF.checkNif("89890001K").ok));
t("DNI con letra errónea", () => { const r = VF.checkNif("12345678A"); assert.ok(!r.ok && /Z/.test(r.msg)); });
t("DNI 12345678Z correcto", () => assert.ok(VF.checkNif("12345678z").ok));
t("NIE X1234567L / Y… / Z…", () => { assert.ok(VF.checkNif("X1234567L").ok); assert.ok(!VF.checkNif("X1234567A").ok); });
t("CIF B12345674 correcto, B12345675 incorrecto", () => { assert.ok(VF.checkNif("B12345674").ok); assert.ok(!VF.checkNif("B12345675").ok); });
t("CIF con letra (P, Q, S…) exige letra de control", () => { assert.ok(VF.checkNif("Q2826000H").ok); assert.ok(!VF.checkNif("Q28260008").ok); });
t("Longitud distinta de 9", () => assert.ok(/9 caracteres/.test(VF.checkNif("891K").msg)));

console.log("Importes y fechas");
const imp = (s) => VF.normImporte(s);
t("241,4 → 241.40; 1.234,56 → 1234.56; 1,234.56 → 1234.56; 1210 → 1210.00", () => {
  assert.strictEqual(imp("241,4").value, "241.40"); assert.strictEqual(imp("1.234,56").value, "1234.56");
  assert.strictEqual(imp("1,234.56").value, "1234.56"); assert.strictEqual(imp("1210").value, "1210.00"); assert.strictEqual(imp("241.4").value, "241.40");
});
t("1.234 se interpreta como miles con aviso", () => { const r = imp("1.234"); assert.strictEqual(r.value, "1234.00"); assert.ok(r.warn); });
t("3 decimales con coma y 13 enteros = error; 12.345 = miles", () => { assert.ok(!imp("1,234").ok); assert.strictEqual(imp("12.345").value, "12345.00"); assert.ok(!imp("1234567890123").ok); assert.ok(!imp("12a").ok); });
t("Fechas: 2024-09-01 → 01-09-2024, 1/9/2024 → 01-09-2024, 30-02-2024 inválida", () => {
  assert.strictEqual(VF.normFecha("2024-09-01").value, "01-09-2024"); assert.strictEqual(VF.normFecha("1/9/2024").value, "01-09-2024"); assert.ok(!VF.normFecha("30-02-2024").ok);
});
t("ahoraMadrid() con huso horario", () => {
  const s = VF.ahoraMadrid(new Date(Date.UTC(2026, 10, 13, 10, 0, 0)));
  assert.ok(/^2026-11-13T11:00:00\+01:00$/.test(s), s);
  const v = VF.ahoraMadrid(new Date(Date.UTC(2026, 6, 1, 10, 0, 0)));
  assert.ok(/^2026-07-01T12:00:00\+02:00$/.test(v), v);
});

console.log("URL del QR tributario (doc. QR v0.5.0)");
t("Ejemplo oficial 8.3 (producción, VERI*FACTU) se reproduce", () => {
  const r = VF.buildQrUrl({ nif: "89890001K", numserie: "12345678-G33", fecha: "01-09-2024", importe: "241.4", entorno: "produccion", verifactu: true });
  assert.strictEqual(r.url, "https://www2.agenciatributaria.gob.es/wlpl/TIKE-CONT/ValidarQR?nif=89890001K&numserie=12345678-G33&fecha=01-09-2024&importe=241.40");
});
t("Rutas: pruebas y NoVerifactu", () => {
  assert.ok(VF.buildQrUrl({ nif: "89890001K", numserie: "A", fecha: "01-09-2024", importe: "1", entorno: "pruebas", verifactu: false }).url.startsWith("https://prewww2.aeat.es/wlpl/TIKE-CONT/ValidarQRNoVerifactu?"));
});
t("«&» se codifica como %26 (ejemplo del apdo. 4)", () => {
  const r = VF.buildQrUrl({ nif: "89890001K", numserie: "12345678&G33", fecha: "01-01-2024", importe: "241.4", entorno: "pruebas" });
  assert.ok(r.url.includes("numserie=12345678%26G33&"));
});
t("Errores 1001–1004, 2002, 2003, 2004, 2005", () => {
  const codes = (d) => VF.buildQrUrl(d).errors.map(e => e.code);
  assert.deepStrictEqual(codes({}).sort(), [1001, 1002, 1003, 1004]);
  assert.ok(codes({ nif: "89890001K", numserie: "x".repeat(61), fecha: "01-01-2024", importe: "1" }).includes(2002));
  assert.ok(codes({ nif: "89890001K", numserie: "Nº 1", fecha: "01-01-2024", importe: "1" }).includes(2003));
  assert.ok(codes({ nif: "89890001K", numserie: "1", fecha: "2024/13/01", importe: "1" }).includes(2004));
  assert.ok(codes({ nif: "89890001K", numserie: "1", fecha: "01-01-2024", importe: "1,234" }).includes(2005));
});
t("parseQrUrl: ejemplo oficial correcto", () => {
  const r = VF.parseQrUrl("https://www2.agenciatributaria.gob.es/wlpl/TIKE-CONT/ValidarQR?nif=89890001K&numserie=12345678-G33&fecha=01-09-2024&importe=241.4");
  assert.ok(r.ok && r.oficial && r.verifactu === true && r.entorno === "produccion", JSON.stringify(r.errors));
  assert.strictEqual(r.params.numserie, "12345678-G33");
});
t("parseQrUrl: & sin codificar + importe con coma (ejemplo erróneo de la AEAT)", () => {
  const r = VF.parseQrUrl("https://prewww2.aeat.es/wlpl/TIKE-CONT/ValidarQR?nif=89890001K&numserie=12345678&G33&fecha=01-01-2024&importe=7,2");
  assert.ok(!r.ok); assert.ok(r.errors.some(e => /no previstos: G33/.test(e.msg))); assert.ok(r.errors.some(e => e.code === 2005));
  assert.ok(r.warnings.some(w => /PRUEBAS/.test(w)));
});
t("parseQrUrl: NIF 891K (ejemplo AEAT) → 2001", () => assert.ok(VF.parseQrUrl("https://www2.agenciatributaria.gob.es/wlpl/TIKE-CONT/ValidarQR?nif=891K&numserie=12345678-G33&fecha=01-01-2024&importe=241.4").errors.some(e => e.code === 2001)));
t("parseQrUrl: dominio que imita a la AEAT → phishing", () => {
  const r = VF.parseQrUrl("https://www2.agenciatributaria.gob.es.validar-factura.example/wlpl/TIKE-CONT/ValidarQR?nif=89890001K&numserie=1&fecha=01-01-2024&importe=1");
  assert.ok(!r.ok && !r.oficial && r.errors.some(e => /phishing/.test(e.msg)));
});
t("parseQrUrl: http, formato=json, idioma inválido, parámetro faltante", () => {
  const r = VF.parseQrUrl("http://www2.agenciatributaria.gob.es/wlpl/TIKE-CONT/ValidarQR?nif=89890001K&numserie=1&fecha=01-01-2024&formato=json&idioma=fr");
  assert.ok(r.errors.some(e => /https/.test(e.msg)) && r.errors.some(e => /formato/.test(e.msg)) && r.errors.some(e => /idioma/.test(e.msg)) && r.errors.some(e => e.code === 1004));
});
t("parseQrUrl: NoVerifactu + idioma válido + espacios como + y %20", () => {
  const r = VF.parseQrUrl("https://www2.agenciatributaria.gob.es/wlpl/TIKE-CONT/ValidarQRNoVerifactu?nif=89890001K&numserie=A+1%202&fecha=29-02-2024&importe=-10.5&idioma=ca");
  assert.ok(r.ok, JSON.stringify(r.errors)); assert.strictEqual(r.verifactu, false); assert.strictEqual(r.params.numserie, "A 1 2");
});
t("Ida y vuelta: buildQrUrl → parseQrUrl con caracteres especiales", () => {
  ["A/1", "12345678&G33", "F 2026 #7", "x+y=z?", "100%"].forEach(ns => {
    const u = VF.buildQrUrl({ nif: "B12345674", numserie: ns, fecha: "13/11/2026", importe: "1.210,00" }).url;
    const p = VF.parseQrUrl(u); assert.ok(p.ok, ns + " " + JSON.stringify(p.errors)); assert.strictEqual(p.params.numserie, ns);
  });
});

console.log("Codificador QR (nivel M) – lectura con zxing-cpp en test-qr.py");
const sample = VF.buildQrUrl({ nif: "89890001K", numserie: "12345678-G33", fecha: "01-09-2024", importe: "241.4" }).url;
const longest = VF.buildQrUrl({ nif: "B12345674", numserie: "X".repeat(60), fecha: "01-09-2024", importe: "999999999999.99" }).url;
const pruebas = VF.buildQrUrl({ nif: "89890001K", numserie: "12345678&G33", fecha: "01-01-2024", importe: "241.4", entorno: "pruebas", verifactu: false }).url;
const qrs = [sample, longest, pruebas].map(u => { const q = QR.encode(u, "M"); return { url: u, version: q.version, size: q.size, rows: q.modules.map(r => r.map(b => (b ? 1 : 0)).join("")) }; });
t("Nivel M y versión 7–8 para una URL normal (45–49 módulos)", () => { assert.ok(qrs[0].version >= 7 && qrs[0].version <= 8, "v" + qrs[0].version); assert.strictEqual(QR.encode(sample, "M").ecl, "M"); });
t("La URL más larga posible cabe (versión ≤ 10)", () => assert.ok(qrs[1].version <= 10, "v" + qrs[1].version));
fs.writeFileSync(path.join(OUTDIR, "qr-matrices.json"), JSON.stringify(qrs));

console.log("XML de alta, comprobación estructural y cadena");
const base = { emisorNif: "89890001K", emisorNombre: "Empresa Ejemplo SL", numSerie: "2026-A-0001", fecha: "13-11-2026", tipoFactura: "F1", descripcion: "Servicios & consultoría <test>",
  destNif: "B12345674", destNombre: "Cliente SL", lineas: [{ calificacion: "S1", tipo: "21", base: 100 }, { exenta: "E1", base: 50 }], primerRegistro: true,
  fechaHora: "2026-11-13T11:00:00+01:00", sif: { nombreRazon: "Software SL", nif: "B12345674", nombre: "Facturador", id: "01", version: "1.0", instalacion: "0001" } };
const b1 = VF.buildAlta(base);
const b2 = VF.buildAlta(Object.assign({}, base, { numSerie: "2026-A-0002", primerRegistro: false, anterior: { nif: "89890001K", numSerie: "2026-A-0001", fecha: "13-11-2026", huella: b1.huella }, fechaHora: "2026-11-13T11:05:00+01:00", lineas: [{ calificacion: "S1", tipo: "10", base: 10 }] }));
const b3 = VF.buildAlta(Object.assign({}, base, { tipoFactura: "F2", destNif: "", destNombre: "", lineas: [{ calificacion: "S1", tipo: "4", base: 9.99 }] }));
fs.writeFileSync(path.join(OUTDIR, "alta-1.xml"), b1.xml); fs.writeFileSync(path.join(OUTDIR, "alta-2.xml"), b2.xml); fs.writeFileSync(path.join(OUTDIR, "alta-f2.xml"), b3.xml);
t("Totales: cuota 21.00, importe 171.00", () => { assert.strictEqual(b1.cuotaTotal, "21.00"); assert.strictEqual(b1.importeTotal, "171.00"); });
t("Huella del XML = huella de la cadena oficial", () => assert.strictEqual(b1.huella, VF.huella("alta", ["89890001K", "2026-A-0001", "13-11-2026", "F1", "21.00", "171.00", "", "2026-11-13T11:00:00+01:00"]).huella));
t("Caracteres especiales escapados en el XML", () => assert.ok(b1.xml.includes("Servicios &amp; consultoría &lt;test&gt;")));
t("checkAltaXml: XML generado sin errores (F1, F1 encadenada, F2)", () => [b1, b2, b3].forEach(b => { const r = VF.checkAltaXml(b.xml, DOMParser); assert.ok(r.ok, JSON.stringify(r.errors)); }));
t("checkAltaXml: detecta huella alterada, orden y obligatorios", () => {
  const r = VF.checkAltaXml(b1.xml.replace("<sf:CuotaTotal>21.00</sf:CuotaTotal>", "<sf:CuotaTotal>21.01</sf:CuotaTotal>"), DOMParser);
  assert.ok(!r.ok && r.errors.some(e => /Huella no coincide/.test(e)));
  const r2 = VF.checkAltaXml(b1.xml.replace(/<sf:TipoFactura>F1<\/sf:TipoFactura>\n/, "").replace("<sf:Desglose>", "<sf:TipoFactura>F1</sf:TipoFactura><sf:Desglose>"), DOMParser);
  assert.ok(r2.errors.some(e => /Orden incorrecto/.test(e)), JSON.stringify(r2.errors));
  const r3 = VF.checkAltaXml(b1.xml.replace(/<sf:DescripcionOperacion>.*<\/sf:DescripcionOperacion>\n/, ""), DOMParser);
  assert.ok(r3.errors.some(e => /DescripcionOperacion/.test(e)));
});
t("checkAltaXml: XML mal formado", () => assert.ok(!VF.checkAltaXml("<a><b></a>", DOMParser).ok));
t("checkChain: ejemplos AEAT en XML → cadena correcta", () => {
  const e = VF.EJEMPLOS, ns = 'xmlns:sf="' + VF.NS_SF + '"';
  const alta = (v, prev) => `<sf:RegistroAlta><sf:IDFactura><sf:IDEmisorFactura>${v[0]}</sf:IDEmisorFactura><sf:NumSerieFactura>${v[1]}</sf:NumSerieFactura><sf:FechaExpedicionFactura>${v[2]}</sf:FechaExpedicionFactura></sf:IDFactura><sf:TipoFactura>${v[3]}</sf:TipoFactura><sf:CuotaTotal>${v[4]}</sf:CuotaTotal><sf:ImporteTotal>${v[5]}</sf:ImporteTotal><sf:Encadenamiento>${prev ? `<sf:RegistroAnterior><sf:Huella>${v[6]}</sf:Huella></sf:RegistroAnterior>` : "<sf:PrimerRegistro>S</sf:PrimerRegistro>"}</sf:Encadenamiento><sf:FechaHoraHusoGenRegistro>${v[7]}</sf:FechaHoraHusoGenRegistro><sf:Huella>${VF.huella("alta", v).huella}</sf:Huella></sf:RegistroAlta>`;
  const an = e[2].valores;
  const xml = `<R ${ns}>${alta(e[0].valores)}${alta(e[1].valores, 1)}<sf:RegistroAnulacion><sf:IDFactura><sf:IDEmisorFacturaAnulada>${an[0]}</sf:IDEmisorFacturaAnulada><sf:NumSerieFacturaAnulada>${an[1]}</sf:NumSerieFacturaAnulada><sf:FechaExpedicionFacturaAnulada>${an[2]}</sf:FechaExpedicionFacturaAnulada></sf:IDFactura><sf:Encadenamiento><sf:RegistroAnterior><sf:Huella>${an[3]}</sf:Huella></sf:RegistroAnterior></sf:Encadenamiento><sf:FechaHoraHusoGenRegistro>${an[4]}</sf:FechaHoraHusoGenRegistro><sf:Huella>${e[2].huella}</sf:Huella></sf:RegistroAnulacion></R>`;
  const r = VF.checkChain(xml, DOMParser);
  assert.ok(r.ok, JSON.stringify(r.rows.map(x => x.problemas)));
  assert.deepStrictEqual(r.rows.map(x => x.guardada), e.map(x => x.huella));
  const bad = VF.checkChain(xml.replace("<sf:CuotaTotal>12.35</sf:CuotaTotal>", "<sf:CuotaTotal>12.36</sf:CuotaTotal>"), DOMParser);
  assert.ok(!bad.ok && bad.rows[0].problemas.length);
});
t("checkChain: registros generados encadenados (b1 → b2) correctos", () => {
  const x = b1.xml.replace(/<\/sfLR:RegistroFactura>[\s\S]*$/, "</sfLR:RegistroFactura>") + b2.xml.replace(/^[\s\S]*?<sfLR:RegistroFactura>/, "<sfLR:RegistroFactura>");
  const r = VF.checkChain(x, DOMParser); assert.ok(r.ok, JSON.stringify(r.rows.map(x => x.problemas)));
});
t("checkChain: importe 123.4 vs 123.40 → aviso de decimales, no error", () => {
  const v = ["89890001K", "1", "01-01-2024", "F1", "12.3", "123.4", "", "2024-01-01T19:20:30+01:00"];
  const h = VF.huella("alta", v).huella;
  const xml = `<sf:RegistroAlta xmlns:sf="${VF.NS_SF}"><sf:IDFactura><sf:IDEmisorFactura>89890001K</sf:IDEmisorFactura><sf:NumSerieFactura>1</sf:NumSerieFactura><sf:FechaExpedicionFactura>01-01-2024</sf:FechaExpedicionFactura></sf:IDFactura><sf:TipoFactura>F1</sf:TipoFactura><sf:CuotaTotal>12.30</sf:CuotaTotal><sf:ImporteTotal>123.40</sf:ImporteTotal><sf:Encadenamiento><sf:PrimerRegistro>S</sf:PrimerRegistro></sf:Encadenamiento><sf:FechaHoraHusoGenRegistro>2024-01-01T19:20:30+01:00</sf:FechaHoraHusoGenRegistro><sf:Huella>${h}</sf:Huella></sf:RegistroAlta>`;
  const r = VF.checkChain(xml, DOMParser); assert.ok(r.ok && r.rows[0].avisos.length, JSON.stringify(r.rows));
});

console.log("\nResultado: " + pass + " correctas, " + fail + " fallidas");
process.exit(fail ? 1 : 0);
