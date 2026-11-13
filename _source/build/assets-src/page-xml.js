/*! Generador de XML de ejemplo (registro de alta Verifactu) y comprobación estructural básica */
(function () {
  "use strict";
  var VF = window.VF, U = window.UI, $ = U.$;
  var form = $("x-form");
  if (!form) return;
  function v(id) { var el = $(id); return el ? el.value.trim() : ""; }
  function radio(name) { var r = form.querySelector('input[name="' + name + '"]:checked'); return r ? r.value : ""; }
  function toggleAnterior() { $("x-anterior").hidden = radio("enc") !== "anterior"; }
  form.addEventListener("change", function (e) { if (e.target && e.target.name === "enc") toggleAnterior(); });
  toggleAnterior();
  if (!v("x-ts")) $("x-ts").value = VF.ahoraMadrid();
  $("x-now").addEventListener("click", function () { $("x-ts").value = VF.ahoraMadrid(); });

  function datos() {
    var errs = [], warns = [];
    var en = VF.checkNif(v("x-enif"));
    if (en.value.length !== 9) errs.push("NIF del emisor: " + en.msg); else if (!en.ok) warns.push("NIF del emisor: " + en.msg);
    if (!v("x-enom")) errs.push("Falta el nombre o razón social del emisor.");
    var ns = v("x-ns"); if (!ns) errs.push("Falta la serie y número de la factura."); else if (ns.length > 60) errs.push("La serie y número no puede superar 60 caracteres.");
    var fe = VF.normFecha(v("x-fecha")); if (!fe.ok) errs.push("Fecha de expedición: " + fe.msg);
    var tipo = v("x-tipo");
    var dn = v("x-dnif");
    if (tipo === "F1" && !dn) errs.push("Una factura completa (F1) necesita el NIF y nombre del destinatario.");
    if (dn) { var dc = VF.checkNif(dn); if (dc.value.length !== 9) errs.push("NIF del destinatario: " + dc.msg); else if (!dc.ok) warns.push("NIF del destinatario: " + dc.msg); if (!v("x-dnom")) errs.push("Falta el nombre del destinatario."); }
    if (!v("x-desc")) errs.push("Falta la descripción de la operación.");
    var lineas = [];
    [1, 2].forEach(function (i) {
      var b = v("x-l" + i + "-base"); if (!b && i > 1) return;
      var bi = VF.normImporte(b);
      if (!bi.ok) { errs.push("Línea " + i + ", base imponible: " + bi.msg); return; }
      var cal = v("x-l" + i + "-cal"), ex = /^E/.test(cal);
      lineas.push({ impuesto: "01", clave: v("x-l" + i + "-clave") || "01", calificacion: ex ? null : cal, exenta: ex ? cal : null, tipo: /^S/.test(cal) ? v("x-l" + i + "-tipo") : null, base: +bi.value });
    });
    if (!lineas.length && !errs.length) errs.push("Añade al menos una línea con base imponible.");
    var primero = radio("enc") !== "anterior", anterior = null;
    if (!primero) {
      anterior = { nif: v("x-a-nif").toUpperCase(), numSerie: v("x-a-ns"), fecha: VF.normFecha(v("x-a-fecha")).value || v("x-a-fecha"), huella: v("x-a-huella").toUpperCase() };
      if (!VF.RE_HASH.test(anterior.huella)) errs.push("La huella del registro anterior debe tener 64 caracteres hexadecimales.");
      if (!anterior.nif || !anterior.numSerie || !anterior.fecha) errs.push("Completa NIF, serie y número y fecha del registro anterior.");
    }
    var ts = v("x-ts"); if (!/^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}[+-]\d{2}:\d{2}$/.test(ts)) errs.push("Fecha y hora de generación: formato AAAA-MM-DDThh:mm:ss+hh:mm.");
    var sn = VF.checkNif(v("x-s-nif")); if (sn.value.length !== 9) errs.push("NIF del productor del software: " + sn.msg);
    ["x-s-nom", "x-s-name", "x-s-id", "x-s-ver", "x-s-inst"].forEach(function (id) { if (!v(id)) errs.push("Completa los datos del sistema informático (" + $(id).getAttribute("data-name") + ")."); });
    if (v("x-s-id").length > 2) errs.push("IdSistemaInformatico admite como máximo 2 caracteres.");
    return { errs: errs, warns: warns, d: {
      emisorNif: en.value, emisorNombre: v("x-enom"), numSerie: ns, fecha: fe.value, tipoFactura: tipo, descripcion: v("x-desc"),
      destNif: dn ? VF.checkNif(dn).value : "", destNombre: v("x-dnom"), lineas: lineas, primerRegistro: primero, anterior: anterior, fechaHora: ts,
      sif: { nombreRazon: v("x-s-nom"), nif: sn.value, nombre: v("x-s-name"), id: v("x-s-id"), version: v("x-s-ver"), instalacion: v("x-s-inst"), soloVerifactu: "S", multiOT: "N", indicadorMultiOT: "N" } } };
  }
  var hres = $("x-hres"), cres = $("x-res");
  function build(focus) {
    var r = datos();
    if (r.errs.length) { U.statusBox(hres, "bad", "Revisa los datos", { errors: r.errs, warnings: r.warns }); $("x-dl").disabled = true; if (focus) hres.focus(); return null; }
    var out = VF.buildAlta(r.d);
    $("x-in").value = out.xml;
    $("x-dl").disabled = false;
    U.statusBox(hres, r.warns.length ? "warn" : "ok", "XML generado (" + out.xml.length + " caracteres)", { warnings: r.warns,
      notes: ["CuotaTotal " + out.cuotaTotal + " · ImporteTotal " + out.importeTotal, "Huella: " + out.huella, "Es un ejemplo de estructura: falta el sobre SOAP y, en modo no VERI*FACTU, la firma electrónica."] });
    check();
    if (focus) hres.focus();
    return out;
  }
  function check() {
    var r = VF.checkAltaXml($("x-in").value);
    U.statusBox(cres, r.ok ? (r.warnings.length ? "warn" : "ok") : "bad", r.ok ? "Estructura básica correcta (" + r.registros + " registro" + (r.registros === 1 ? "" : "s") + " de alta)" : "Se han encontrado errores", { errors: r.errors, warnings: r.warnings, notes: r.notes });
    return r;
  }
  form.addEventListener("submit", function (e) { e.preventDefault(); build(true); });
  $("x-check").addEventListener("click", function () { check(); cres.focus(); });
  $("x-dl").addEventListener("click", function () { U.download("registro-alta-" + (v("x-ns") || "ejemplo").replace(/[^A-Za-z0-9\-_]+/g, "_") + ".xml", $("x-in").value, "application/xml;charset=utf-8"); });
  $("x-ex").addEventListener("click", function () {
    var set = { "x-enif": "89890001K", "x-enom": "Empresa Ejemplo SL", "x-ns": "2026-A-0001", "x-fecha": "2026-11-13", "x-desc": "Servicios de consultoría", "x-dnif": "B12345674", "x-dnom": "Cliente Ejemplo SL",
      "x-l1-base": "100,00", "x-l2-base": "", "x-s-nom": "Software Ejemplo SL", "x-s-nif": "B12345674", "x-s-name": "FacturaFacil", "x-s-id": "01", "x-s-ver": "1.0", "x-s-inst": "0001" };
    Object.keys(set).forEach(function (k) { $(k).value = set[k]; });
    $("x-tipo").value = "F1"; $("x-l1-cal").value = "S1"; $("x-l1-tipo").value = "21"; $("x-l1-clave").value = "01";
    form.querySelector('input[name="enc"][value="primero"]').checked = true; toggleAnterior();
    $("x-ts").value = VF.ahoraMadrid();
    build(true);
  });
  window.VFX = { build: build, check: check };
})();
