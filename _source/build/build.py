# -*- coding: utf-8 -*-
"""Genera la web estática en ../out.  Uso: python3 build.py
Variables opcionales: VF_SITE_URL, VF_BASE (ver common.py), VF_GSV (etiqueta de Google Search Console)."""
import os, sys, shutil, subprocess, re
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import common
from common import render, SITE_URL, BASE, UPDATED_ISO
from page_home import HOME
from page_qr import GEN, VAL
from page_dev import HUE as HUEP, XMLP
import page_blog as B
import page_b2b as PB
import page_b2b_blog as PBB
import page_blog_2 as PB2

B.POSTS.extend(PBB.POSTS)
B.POSTS.extend(PB2.POSTS)

OUT = os.path.abspath(os.path.join(HERE, "..", "out"))
if os.path.isdir(OUT):
    shutil.rmtree(OUT)
os.makedirs(os.path.join(OUT, "assets"))

# Recursos: JS minificado (terser) y CSS minificado (csso) que se inserta inline
subprocess.run(["node", os.path.join(HERE, "tools", "minify.js")], check=True)
_cssf = os.path.join(OUT, "assets", ".style.min.css")
common.INLINE_CSS = open(_cssf, encoding="utf-8").read().replace("</", "<\\/")
os.remove(_cssf)

common.ARTICLES[:] = [("/blog/%s/" % p["slug"], p["h1"], p["desc"]) for p in B.POSTS]
_b = lambda slug: "/blog/%s/" % slug
F, G, Q = _b("fechas-verifactu-2027-2028"), _b("verifactu-gratis-aplicacion-aeat"), _b("tamano-posicion-qr-verifactu")
DIF, AUT, PMPG = _b("diferencias-verifactu-factura-electronica-b2b"), _b("factura-electronica-obligatoria-autonomos"), _b("calcular-periodo-medio-pago-proveedores-ejemplo")
VAU, MOR = _b("verifactu-autonomos"), _b("plazos-pago-ley-morosidad")
TID, REC, INF = _b("tipo-interes-demora-2026"), _b("reclamar-factura-impagada-intereses"), _b("informar-pago-factura-4-dias")
E27, HOW, PMA = _b("factura-electronica-obligatoria-2027-empresas"), _b("factura-electronica-como-se-hace"), _b("periodo-medio-pago-memoria-abreviada")
SPA, FORAL, PMX = _b("solucion-publica-factura-electronica-aeat"), _b("factura-electronica-pais-vasco-navarra"), _b("periodo-medio-pago-maximo-legal")
DHC, PMEL = _b("intereses-demora-hacienda-vs-comerciales"), _b("periodo-medio-pago-entidades-locales")
ABU = _b("clausulas-abusivas-plazo-pago-morosidad")
QRO, SIMP, HUEL = _b("verifactu-qr-obligatorio"), _b("verifactu-factura-simplificada-ticket"), _b("huella-verifactu-que-es")
SII, REQ, MOD = _b("verifactu-sii-exentos"), _b("verifactu-programa-facturacion-requisitos"), _b("verifactu-modalidad-no-verifactu")
XLS, RCE, TBAI = _b("verifactu-excel-word"), _b("verifactu-recargo-equivalencia"), _b("verifactu-ticketbai-diferencias")
RECT, TPVB, BARES = _b("factura-rectificativa-verifactu"), _b("tpv-verifactu"), _b("verifactu-bares-restaurantes")
MODU, QREJ, QRERR = _b("verifactu-modulos-estimacion-objetiva"), _b("qr-verifactu-ejemplo"), _b("errores-qr-verifactu-1001-2006")
assert all(u in [a[0] for a in common.ARTICLES] for u in (F, G, Q, DIF, AUT, PMPG, VAU, MOR, TID, REC, INF, E27, HOW, PMA, SPA, FORAL, PMX, SII, REQ, MOD, QRO, SIMP, HUEL, XLS, RCE, TBAI, RECT, TPVB, BARES, MODU, QREJ, QRERR, DHC, PMEL, ABU))
# Enlaces internos «Guías relacionadas» (3 por página): herramienta -> guías del mismo tema, guía -> guías hermanas
common.ARTICLE_MAP.update({"/": [VAU, XLS, SII], "/generador-qr-verifactu/": [QREJ, QRO, SIMP], "/validar-qr-verifactu/": [QRERR, QREJ, QRO],
                           "/calcular-huella-verifactu/": [HUEL, F, Q], "/ejemplo-xml-verifactu/": [REQ, Q, G],
                           "/factura-electronica-obligatoria/": [E27, SPA, FORAL], "/periodo-medio-pago-proveedores/": [PMX, PMEL, PMA],
                           "/intereses-demora-comerciales/": [TID, DHC, REC],
                           F: [VAU, G, MOD], G: [VAU, F, Q], Q: [G, VAU, F],
                           DIF: [AUT, VAU, PMPG], AUT: [MODU, XLS, E27], PMPG: [PMA, MOR, DIF],
                           VAU: [F, G, AUT], MOR: [TID, ABU, REC],
                           TID: [DHC, REC, MOR], REC: [TID, ABU, INF], INF: [AUT, REC, DIF], E27: [HOW, SPA, FORAL], HOW: [E27, SPA, DIF], PMA: [PMX, PMEL, TID],
                           SPA: [FORAL, HOW, E27], FORAL: [SPA, TBAI, E27], PMX: [PMA, PMPG, MOR], DHC: [TID, REC, MOR], PMEL: [PMX, PMA, MOR],
                           SII: [REQ, TBAI, VAU], REQ: [MOD, G, SII], MOD: [REQ, Q, G],
                           QRO: [Q, SIMP, HUEL], SIMP: [QRO, RCE, MOD], HUEL: [REQ, MOD, QRO],
                           XLS: [REQ, G, AUT], RCE: [SIMP, MODU, AUT], TBAI: [SII, FORAL, VAU],
                           RECT: [SIMP, HUEL, TPVB], TPVB: [BARES, REQ, QRO], BARES: [TPVB, SIMP, QRO],
                           MODU: [AUT, RCE, SII], QREJ: [QRERR, QRO, Q], QRERR: [QREJ, QRO, MOD], ABU: [MOR, REC, TID]})

PAGES = [("/", HOME), ("/generador-qr-verifactu/", GEN), ("/validar-qr-verifactu/", VAL), ("/calcular-huella-verifactu/", HUEP),
         ("/ejemplo-xml-verifactu/", XMLP),
         ("/factura-electronica-obligatoria/", PB.B2B), ("/periodo-medio-pago-proveedores/", PB.PMP), ("/intereses-demora-comerciales/", PB.DEM),
         ("/blog/", B.blog_index())]
for p in B.POSTS:
    page, url = B.post_page(p)
    PAGES.append((url, page))
PAGES += [("/sobre-nosotros/", B.ABOUT), ("/contacto/", B.CONTACT), ("/aviso-legal/", B.TERMS), ("/privacidad/", B.PRIV)]


def write(rel, content, binary=False):
    p = os.path.join(OUT, rel.lstrip("/"))
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "wb" if binary else "w", **({} if binary else {"encoding": "utf-8"})) as f:
        f.write(content)


for path, page in PAGES:
    write(path + "index.html", render(page, path))

NF = dict(title="Página no encontrada (404) – Herramientas Verifactu",
          desc="Esta página no existe. Ve a las herramientas Verifactu gratuitas: test de obligación, generador y validador de QR, huella y XML.",
          app=False, trust=False, noindex=True, h1="Página no encontrada",
          intro="Puede que la dirección haya cambiado o tenga una errata. Elige una herramienta:",
          trail=[("Inicio", "/"), ("Error 404", "/404.html")],
          content='<p><a class="btn" href="/">Ir al test «¿estoy obligado a Verifactu?»</a></p>')
write("/404.html", render(NF, "/404.html"))

assert re.match(r"^\d{4}-\d{2}-\d{2}$", UPDATED_ISO), "lastmod debe ser AAAA-MM-DD"
# lastmod por página: la fecha solo cambia si la página cambió respecto a la copia publicada (../repo),
# sin contar la fecha de «Última revisión»/dateModified que cambia en cada build.
REPO_DIR = os.path.abspath(os.path.join(OUT, "..", "repo"))
_OLD_LM = {}
try:
    for _loc, _lm in re.findall(r"<loc>([^<]+)</loc><lastmod>([^<]+)</lastmod>", open(os.path.join(REPO_DIR, "sitemap.xml"), encoding="utf-8").read()):
        if _loc.startswith(SITE_URL) and re.match(r"^\d{4}-\d{2}-\d{2}$", _lm):
            _OLD_LM[_loc[len(SITE_URL):]] = _lm
except OSError:
    pass
_DATE_RX = re.compile(r'"dateModified": ?"\d{4}-\d{2}-\d{2}"|Última revisión: (<time datetime="\d{4}-\d{2}-\d{2}">)?\d{1,2} de [a-z]+ de \d{4}')
def _norm(t):
    return _DATE_RX.sub("", t)
def lastmod(u):
    try:
        a = open(os.path.join(OUT, u.lstrip("/"), "index.html"), encoding="utf-8").read()
        b = open(os.path.join(REPO_DIR, u.lstrip("/"), "index.html"), encoding="utf-8").read()
        if u in _OLD_LM and _norm(a) == _norm(b):
            return _OLD_LM[u]
    except OSError:
        pass
    return UPDATED_ISO

sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for u, _p in PAGES:
    pr = "1.0" if u == "/" else ("0.3" if u in ("/privacidad/", "/sobre-nosotros/", "/contacto/", "/aviso-legal/") else ("0.7" if u.startswith("/blog/") else "0.9"))
    sm.append("  <url><loc>%s%s</loc><lastmod>%s</lastmod><priority>%s</priority></url>" % (SITE_URL, u, lastmod(u), pr))
sm.append("</urlset>\n")
write("/sitemap.xml", "\n".join(sm))
INDEXNOW_KEY = "c4e8a1f7b3d94e2a8f6c0b5d7e1a9f32"
write("/%s.txt" % INDEXNOW_KEY, INDEXNOW_KEY)
write("/robots.txt", "User-agent: *\nAllow: /\nDisallow: %s/_source/\n\nSitemap: %s/sitemap.xml\n" % (BASE, SITE_URL))
write("/favicon.svg", common.FAVICON)
write("/site.webmanifest", """{
  "name": "%s",
  "short_name": "%s",
  "description": "Verifactu, factura electrónica B2B y morosidad: test, QR tributario, huella, XML, periodo medio de pago e intereses de demora. Gratis y en tu navegador.",
  "lang": "es-ES",
  "start_url": "%s/",
  "scope": "%s/",
  "display": "standalone",
  "background_color": "#f6f8fb",
  "theme_color": "#0a6b60",
  "icons": [{ "src": "%s/favicon.svg", "sizes": "any", "type": "image/svg+xml", "purpose": "any" },
            { "src": "%s/assets/logo-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any" }]
}
""" % (common.BRAND, "Verifactu" if common.BRAND == common.DEFAULT_BRAND else common.BRAND, BASE, BASE, BASE, BASE))
write("/.nojekyll", "")
if os.environ.get("VF_CNAME"):
    write("/CNAME", os.environ["VF_CNAME"].strip() + "\n")
import og_image
og_image.og(os.path.join(OUT, "assets", "og-verifactu.png"), common.BRAND)
og_image.logo(os.path.join(OUT, "assets", "logo-512.png"))
print("built", OUT, "SITE_URL=%s BASE=%s BRAND=%s" % (SITE_URL, BASE, common.BRAND))
