#!/usr/bin/env python3
"""Valida los XML generados contra los XSD oficiales de la AEAT (copia en qa/xsd, SuministroLR.xsd v1.0)
y lee con zxing-cpp los QR generados por qr.js. Ejecutar después de test-core.js."""
import json, os, sys
from lxml import etree
from PIL import Image
import zxingcpp
H = os.path.dirname(os.path.abspath(__file__))
ok = fail = 0
def t(name, cond, info=""):
    global ok, fail
    if cond: ok += 1; print("  ✓", name)
    else: fail += 1; print("  ✗", name, info)
print("XSD oficial AEAT (SuministroLR.xsd + SuministroInformacion.xsd)")
schema = etree.XMLSchema(etree.parse(os.path.join(H, "xsd", "SuministroLR.xsd")))
for f in ("alta-1.xml", "alta-2.xml", "alta-f2.xml"):
    doc = etree.parse(os.path.join(H, "out", f))
    v = schema.validate(doc)
    t(f + " válido contra el XSD", v, str(schema.error_log)[:500])
bad = etree.fromstring(open(os.path.join(H, "out", "alta-1.xml"), "rb").read().replace(b"<sf:TipoFactura>F1", b"<sf:TipoFactura>F9"))
t("control negativo: TipoFactura F9 es rechazado por el XSD", not schema.validate(bad))
print("Lectura de los QR generados (zxing-cpp)")
for i, q in enumerate(json.load(open(os.path.join(H, "out", "qr-matrices.json")))):
    n, s, b = len(q["rows"]), 6, 4
    im = Image.new("L", ((n + 2 * b) * s,) * 2, 255); px = im.load()
    for y, r in enumerate(q["rows"]):
        for x, c in enumerate(r):
            if c == "1":
                for dy in range(s):
                    for dx in range(s): px[(x + b) * s + dx, (y + b) * s + dy] = 0
    res = zxingcpp.read_barcodes(im)
    t("QR %d (v%d, %d módulos) se lee y coincide con la URL" % (i + 1, q["version"], n), bool(res) and res[0].text == q["url"], res[0].text if res else "sin lectura")
    if res: t("QR %d con nivel de corrección M" % (i + 1), res[0].ec_level == "M", res[0].ec_level)
    if i == 0: im.save(os.path.join(H, "out", "qr-ejemplo.png"))
print("Archivos producidos en el navegador (test-browser-csp.js), si existen")
f = os.path.join(H, "out", "xml-desde-navegador.xml")
if os.path.exists(f):
    t("XML generado en Chromium válido contra el XSD", schema.validate(etree.parse(f)), str(schema.error_log)[:400])
f = os.path.join(H, "out", "descarga-qr-600ppp.png")
if os.path.exists(f):
    im = Image.open(f); res = zxingcpp.read_barcodes(im)
    t("PNG descargado (600 ppp, %dx%d px) se lee: %s" % (im.size[0], im.size[1], res[0].text[:45] + "…" if res else "-"), bool(res) and res[0].text.startswith("https://prewww2.aeat.es/wlpl/TIKE-CONT/ValidarQR?nif=89890001K"))
f = os.path.join(H, "out", "descarga-qr.svg")
if os.path.exists(f):
    import re
    sv = open(f).read(); m = re.search(r'width="([\d.]+)mm" height="([\d.]+)mm"', sv); sc = re.search(r"scale\(([\d.]+)\)", sv)
    k = float(sc.group(1)); n = round(35 / k)
    t("SVG descargado en mm: bloque %s × %s mm, QR de %d módulos × %.3f mm = %.2f mm (35 mm pedidos)" % (m.group(1), m.group(2), n, k, n * k), m and (n - 17) % 4 == 0 and abs(n * k - 35) < 0.01)
print("\nResultado: %d correctas, %d fallidas" % (ok, fail))
sys.exit(1 if fail else 0)
