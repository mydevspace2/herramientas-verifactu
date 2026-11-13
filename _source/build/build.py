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
from page_dev import HUE, XMLP
import page_blog as B

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
F, G, Q = ["/blog/%s/" % p["slug"] for p in B.POSTS]
common.ARTICLE_MAP.update({"/": [F, G, Q], "/generador-qr-verifactu/": [Q, F, G], "/validar-qr-verifactu/": [Q, G, F],
                           "/calcular-huella-verifactu/": [F, Q, G], "/ejemplo-xml-verifactu/": [F, Q, G]})

PAGES = [("/", HOME), ("/generador-qr-verifactu/", GEN), ("/validar-qr-verifactu/", VAL), ("/calcular-huella-verifactu/", HUE),
         ("/ejemplo-xml-verifactu/", XMLP), ("/blog/", B.blog_index())]
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

sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for u, _p in PAGES:
    pr = "1.0" if u == "/" else ("0.3" if u in ("/privacidad/", "/sobre-nosotros/", "/contacto/", "/aviso-legal/") else ("0.7" if u.startswith("/blog/") else "0.9"))
    sm.append("  <url><loc>%s%s</loc><lastmod>%s</lastmod><priority>%s</priority></url>" % (SITE_URL, u, UPDATED_ISO, pr))
sm.append("</urlset>\n")
write("/sitemap.xml", "\n".join(sm))
write("/robots.txt", "User-agent: *\nAllow: /\nDisallow: %s/_source/\n\nSitemap: %s/sitemap.xml\n" % (BASE, SITE_URL))
write("/favicon.svg", common.FAVICON)
write("/site.webmanifest", """{
  "name": "Herramientas Verifactu",
  "short_name": "Verifactu",
  "description": "¿Verifactu es obligatorio? Test, QR tributario, huella SHA-256 y XML. Gratis y en tu navegador.",
  "lang": "es-ES",
  "start_url": "%s/",
  "scope": "%s/",
  "display": "standalone",
  "background_color": "#f6f8fb",
  "theme_color": "#0a6b60",
  "icons": [{ "src": "%s/favicon.svg", "sizes": "any", "type": "image/svg+xml", "purpose": "any" },
            { "src": "%s/assets/logo-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any" }]
}
""" % (BASE, BASE, BASE, BASE))
write("/.nojekyll", "")
if os.environ.get("VF_CNAME"):
    write("/CNAME", os.environ["VF_CNAME"].strip() + "\n")
import og_image
og_image.og(os.path.join(OUT, "assets", "og-verifactu.png"))
og_image.logo(os.path.join(OUT, "assets", "logo-512.png"))
print("built", OUT, "SITE_URL=%s BASE=%s" % (SITE_URL, BASE))
