# -*- coding: utf-8 -*-
"""Plantilla común de Herramientas Verifactu (basada en la de numerksef.dpdns.org)."""
import json, html, hashlib, base64, os, re

# Dirección pública. Con dominio propio: SITE_URL="https://dominio", BASE="".
# En GitHub Pages sin dominio: SITE_URL="https://mydevspace2.github.io/herramientas-verifactu", BASE="/herramientas-verifactu".
SITE_URL = os.environ.get("VF_SITE_URL", "https://mydevspace2.github.io/herramientas-verifactu").rstrip("/")
BASE = os.environ.get("VF_BASE", "/herramientas-verifactu").rstrip("/")
DEFAULT_BRAND = "Herramientas Verifactu"
# Nombre de marca: con dominio propio se puede cambiar con VF_BRAND (p. ej. "VerifactuYa").
BRAND = os.environ.get("VF_BRAND", DEFAULT_BRAND).strip() or DEFAULT_BRAND
SITE = BRAND
UPDATED_ISO = "2026-11-13"  # SIEMPRE AAAA-MM-DD (sitemap <lastmod>, <time datetime>, JSON-LD)
assert re.match(r"^\d{4}-\d{2}-\d{2}$", UPDATED_ISO)
UPDATED_ES = "13 de noviembre de 2026"
ASSET_V = "1"
OG_IMAGE = "/assets/og-verifactu.png"
OG_W, OG_H = 1200, 630
LOGO_PNG = "/assets/logo-512.png"
EMAIL = "topelitemindset1@gmail.com"
# Etiqueta de verificación de Google Search Console: pega aquí el valor de content="..." cuando lo tengas.
GSV_CONTENT = os.environ.get("VF_GSV", "")
ARTICLES = []      # (url, título, descripción) – se rellena en build.py
ARTICLE_MAP = {}

TOOLS = [
    ("/", "¿Estoy obligado a Verifactu?", "¿Obligado?", "Responde 4 preguntas: fecha del BOE (2027) y aplazamiento anunciado (2028)."),
    ("/generador-qr-verifactu/", "Generador de QR tributario", "Generar QR", "QR con nivel M, 30–40 mm, «QR tributario:» y leyenda VERI*FACTU listo para imprimir."),
    ("/validar-qr-verifactu/", "Validar y leer QR Verifactu", "Validar QR", "Pega la URL, sube una foto o usa la cámara: comprueba dominio, parámetros y formato."),
    ("/calcular-huella-verifactu/", "Calcular huella (hash)", "Huella", "SHA-256 de registros de alta, anulación y evento y comprobación de la cadena."),
    ("/ejemplo-xml-verifactu/", "Ejemplo XML de registro de alta", "XML", "Genera un RegistroAlta de ejemplo con su huella y revisa su estructura."),
    ("/factura-electronica-obligatoria/", "Factura electrónica B2B: ¿cuándo me obliga?", "Factura B2B", "Fechas del BOE (6/10/2027 y 6/10/2028), test y plazo de 4 días para informar pagos."),
    ("/periodo-medio-pago-proveedores/", "Calculadora del periodo medio de pago", "PMP", "Método ICAC: ratios de pagadas y pendientes, límite de 60 días, CSV y cuadro de la memoria."),
    ("/intereses-demora-comerciales/", "Intereses de demora (Ley 3/2004)", "Demora", "Tipos del BOE por semestre (BCE + 8) y 40 € por factura, para varias facturas."),
]
OTHER = [
    ("/blog/", "Guías: Verifactu, factura electrónica y morosidad"),
    ("/sobre-nosotros/", "Sobre nosotros"),
    ("/contacto/", "Contacto"),
    ("/aviso-legal/", "Aviso legal y condiciones"),
    ("/privacidad/", "Política de privacidad"),
]
THEME_INIT = ('<script>(function(){try{var t=localStorage.getItem("theme");if(t!=="light"&&t!=="dark")'
              '{t=window.matchMedia&&matchMedia("(prefers-color-scheme: dark)").matches?"dark":"light"}'
              'document.documentElement.setAttribute("data-theme",t)}catch(e){}})();</script>')
THEME_BTN = ('<button class="theme-toggle" type="button" aria-pressed="false" aria-label="Modo oscuro" title="Cambiar modo claro / oscuro">'
             '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="2"/>'
             '<path d="M12 3a9 9 0 0 1 0 18z" fill="currentColor"/></svg></button>')
# Logotipo: cuadrado verde azulado con un QR estilizado y una marca de verificación
LOGO_INNER = ('<rect width="32" height="32" rx="8" fill="#0a6b60"/>'
              '<rect x="7" y="7" width="7" height="7" rx="1.2" fill="#fff"/><rect x="9.2" y="9.2" width="2.6" height="2.6" fill="#0a6b60"/>'
              '<rect x="18" y="7" width="7" height="7" rx="1.2" fill="#fff"/><rect x="20.2" y="9.2" width="2.6" height="2.6" fill="#0a6b60"/>'
              '<rect x="7" y="18" width="7" height="7" rx="1.2" fill="#fff"/><rect x="9.2" y="20.2" width="2.6" height="2.6" fill="#0a6b60"/>'
              '<circle cx="22.5" cy="22.5" r="5.5" fill="#f59e0b" stroke="#fff" stroke-width="1.4"/>'
              '<path d="M20 22.6l1.7 1.7 3.1-3.3" fill="none" stroke="#fff" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/>')
LOGO = '<svg viewBox="0 0 32 32" aria-hidden="true" focusable="false">' + LOGO_INNER + '</svg>'
FAVICON = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">' + LOGO_INNER + '</svg>\n'
PRIVACY_NOTE = "Los datos no salen de tu navegador."
INLINE_CSS = ""  # se rellena en build.py (CSS minificado insertado inline)


def L(path):
    """Ruta interna con el prefijo BASE (GitHub Pages sin dominio propio)."""
    return BASE + path


def csp_hash(text):
    return "'sha256-%s'" % base64.b64encode(hashlib.sha256(text.encode("utf-8")).digest()).decode()


def csp_meta():
    theme_js = THEME_INIT[len("<script>"):-len("</script>")]
    pol = ("default-src 'self'; script-src 'self' %s; style-src 'self' %s; img-src 'self' data: blob:; "
           "media-src 'self' blob: mediastream:; connect-src 'self'; object-src 'none'; base-uri 'self'; form-action 'self'") % (csp_hash(theme_js), csp_hash(INLINE_CSS))
    return '<meta http-equiv="Content-Security-Policy" content="%s">' % pol


def e(s):
    return html.escape(s, quote=True)


def header(path):
    items = "".join('<li><a href="%s"%s>%s</a></li>' % (u, ' aria-current="page"' if u == path else "", e(short)) for (u, _l, short, _d) in TOOLS)
    items += '<li><a href="/blog/"%s>Guías</a></li>' % (' aria-current="page"' if path.startswith("/blog/") else "")
    return ('<a class="skip" href="#contenido">Saltar al contenido</a>'
            '<header class="site-head"><div class="wrap">'
            '<a class="brand" href="/" aria-label="%s – inicio">%s<span>%s<small>gratis · sin registro · en tu navegador</small></span></a>'
            '<button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav">Menú</button>'
            '<nav id="site-nav" class="site-nav" aria-label="Herramientas"><ul>%s</ul></nav>%s'
            '</div></header>') % (BRAND, LOGO, BRAND, items, THEME_BTN)


def footer():
    tools = "".join('<li><a href="%s">%s</a></li>' % (u, e(l)) for (u, l, _s, _d) in TOOLS)
    other = "".join('<li><a href="%s">%s</a></li>' % (u, e(l)) for (u, l) in OTHER)
    return ('<footer class="site-foot"><div class="wrap"><div class="foot-grid">'
            '<div><h2>%s</h2><p>Herramientas gratuitas para cumplir Verifactu, la factura electrónica B2B y la Ley de morosidad: obligación, QR tributario, huella, XML, periodo medio de pago e intereses de demora. '
            'Sin registro y sin cookies. Todo se calcula en tu navegador: %s</p>'
            '<p>Web independiente, sin relación con la Agencia Tributaria (AEAT) ni con el Ministerio de Hacienda. Información orientativa: no es asesoramiento fiscal.</p></div>'
            '<div><h2>Herramientas</h2><ul>%s</ul></div>'
            '<div><h2>Web y fuentes oficiales</h2><ul>%s'
            '<li><a href="https://sede.agenciatributaria.gob.es/Sede/iva/sistemas-informaticos-facturacion-verifactu.html" rel="noopener" target="_blank">Verifactu en la sede de la AEAT</a></li>'
            '<li><a href="https://www.boe.es/buscar/act.php?id=BOE-A-2023-24840" rel="noopener" target="_blank">RD 1007/2023 (texto consolidado, BOE)</a></li>'
            '<li><a href="https://www.boe.es/buscar/act.php?id=BOE-A-2026-7295" rel="noopener" target="_blank">RD 238/2026, factura electrónica B2B (BOE)</a></li>'
            '<li><a href="/sitemap.xml">Mapa del sitio</a></li></ul></div>'
            '</div><p class="foot-note">© 2026 %s · Última revisión: %s · Sin servidor, sin cookies y sin seguimiento.</p></div></footer>'
            '<p id="live" class="sr-only" aria-live="polite"></p><div id="print-sheet" aria-hidden="true"></div>'
            ) % (SITE, PRIVACY_NOTE, tools, other, BRAND, UPDATED_ES)


def crumbs_html(trail):
    lis = []
    for i, (name, url) in enumerate(trail):
        lis.append('<li aria-current="page">%s</li>' % e(name) if i == len(trail) - 1 else '<li><a href="%s">%s</a></li>' % (url, e(name)))
    return '<nav class="crumbs" aria-label="Ruta de navegación"><ol>%s</ol></nav>' % "".join(lis)


def faq_html(faq):
    return '<div class="faq">' + "".join('<details><summary>%s</summary><p>%s</p></details>' % (e(q), a) for q, a in faq) + "</div>"


def strip_tags(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s))


def org_ref():
    return {"@type": "Organization", "@id": SITE_URL + "/#organization", "name": BRAND, "url": SITE_URL + "/",
            "logo": {"@type": "ImageObject", "url": SITE_URL + LOGO_PNG, "width": 512, "height": 512}}


def jsonld(page, path):
    url = SITE_URL + path
    site_ref = {"@id": SITE_URL + "/#website"}
    graph = []
    if page.get("app", True):
        graph.append({"@type": "WebApplication", "@id": url + "#app", "name": page["app_name"], "url": url, "description": page["desc"],
                      "applicationCategory": "BusinessApplication", "operatingSystem": "Cualquiera (navegador web)",
                      "browserRequirements": "Requiere JavaScript", "inLanguage": "es-ES", "isAccessibleForFree": True,
                      "offers": {"@type": "Offer", "price": "0", "priceCurrency": "EUR"}, "dateModified": UPDATED_ISO,
                      "image": SITE_URL + OG_IMAGE, "publisher": {"@id": SITE_URL + "/#organization"}, "isPartOf": site_ref})
    else:
        graph.append({"@type": "CollectionPage" if path == "/blog/" else "WebPage", "@id": url + "#webpage", "name": page["title"], "url": url,
                      "description": page["desc"], "inLanguage": "es-ES", "dateModified": UPDATED_ISO, "isPartOf": site_ref})
    # Organización y sitio web en todas las páginas (mismo @id): Google las une en un único nodo.
    graph.append({"@type": "Organization", "@id": SITE_URL + "/#organization", "name": BRAND, "url": SITE_URL + "/",
                  "logo": {"@type": "ImageObject", "url": SITE_URL + LOGO_PNG, "width": 512, "height": 512},
                  "email": EMAIL,
                  "description": "Web independiente con herramientas gratuitas para Verifactu, la factura electrónica B2B y la morosidad. Sin relación con la AEAT."})
    graph.append({"@type": "WebSite", "@id": SITE_URL + "/#website", "name": SITE, "url": SITE_URL + "/", "inLanguage": "es-ES",
                  "description": "Herramientas y guías gratuitas sobre Verifactu, factura electrónica obligatoria y morosidad.",
                  "publisher": {"@id": SITE_URL + "/#organization"}})
    if page.get("article"):
        pub = page.get("published", UPDATED_ISO)
        mod = page.get("modified", UPDATED_ISO)
        assert re.match(r"^\d{4}-\d{2}-\d{2}$", pub) and re.match(r"^\d{4}-\d{2}-\d{2}$", mod), "fechas ISO"
        graph.append({"@type": "Article", "@id": url + "#article", "headline": page["h1"][:110], "description": page["desc"], "url": url,
                      "mainEntityOfPage": url, "inLanguage": "es-ES", "datePublished": pub, "dateModified": max(pub, mod),
                      "author": {"@id": SITE_URL + "/#organization"}, "publisher": {"@id": SITE_URL + "/#organization"},
                      "isPartOf": site_ref, "isAccessibleForFree": True, "image": SITE_URL + OG_IMAGE})
    if page.get("faq"):
        graph.append({"@type": "FAQPage", "@id": url + "#faq", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}} for q, a in page["faq"]]})
    graph.append({"@type": "BreadcrumbList", "@id": url + "#breadcrumb", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": SITE_URL + u} for i, (n, u) in enumerate(page["trail"])]})
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=1)


def related(path):
    cards = "".join('<a href="%s"><strong>%s</strong><span>%s</span></a>' % (u, e(l), e(d)) for (u, l, _s, d) in TOOLS if u != path)
    return '<h2 id="otras-herramientas">Otras herramientas gratis: Verifactu, factura electrónica y morosidad</h2><div class="hub">%s</div>' % cards


def related_articles(path):
    order = ARTICLE_MAP.get(path) or [u for (u, _t, _d) in ARTICLES]
    by = {u: (u, t, d) for (u, t, d) in ARTICLES}
    items = [by[u] for u in order if u in by and u != path][:3]
    if not items:
        return ""
    return '<h2 id="guias-relacionadas">Guías relacionadas</h2><div class="hub">%s</div>' % "".join(
        '<a href="%s"><strong>%s</strong><span>%s</span></a>' % (u, e(t), e(d)) for (u, t, d) in items)


def sources_html(src):
    return '<h2 id="fuentes">Fuentes oficiales</h2><ul class="sources">' + "".join(
        '<li><a href="%s" rel="noopener" target="_blank">%s</a>%s</li>' % (u, e(t), (" – " + n) if n else "") for (t, u, n) in src) + "</ul>"


def prefix_links(doc):
    """Añade BASE a href/src/action internos (los que empiezan por una sola barra)."""
    if not BASE:
        return doc
    return re.sub(r'(\s(?:href|src|action))="/(?!/)', r'\1="' + BASE + '/', doc)


def render(page, path):
    title, desc, url = page["title"], page["desc"], SITE_URL + path
    scripts = "".join('<script src="/assets/%s?v=%s" defer></script>' % (s, ASSET_V) for s in page.get("scripts", []))
    robots = '<meta name="robots" content="noindex">' if page.get("noindex") else '<meta name="robots" content="index,follow,max-image-preview:large">'
    parts = [crumbs_html(page["trail"]) if len(page["trail"]) > 1 else ""]
    parts.append('<div class="hero"><h1>%s</h1><p class="lead">%s</p>' % (e(page["h1"]), page["intro"]))
    if page.get("trust", True):
        parts.append('<ul class="trust"><li>Gratis, sin registro</li><li>%s</li></ul>' % PRIVACY_NOTE)
    parts.append("</div>")
    parts.append(page.get("tool", ""))
    content = page.get("content", "")
    if page.get("faq"):
        content += '<h2 id="preguntas-frecuentes">Preguntas frecuentes</h2>' + faq_html(page["faq"])
    if page.get("sources"):
        content += sources_html(page["sources"])
    if page.get("related", True):
        content += related(path) + related_articles(path)
    content += '<p class="updated">Última revisión: <time datetime="%s">%s</time> · %s</p>' % (UPDATED_ISO, UPDATED_ES, PRIVACY_NOTE)
    parts.append('<article class="content">%s</article>' % content)
    gsv = ('\n<meta name="google-site-verification" content="%s">' % e(GSV_CONTENT)) if (GSV_CONTENT and path == "/") else ""
    doc = """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">{gsv}
{csp}
<meta name="referrer" content="strict-origin-when-cross-origin">
<meta name="viewport" content="width=device-width, initial-scale=1">
{theme}
<title>{title}</title>
<meta name="description" content="{desc}">
{robots}
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="es" href="{url}">
<link rel="alternate" hreflang="x-default" href="{url}">
<meta name="theme-color" content="#0a6b60">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{logo}">
<link rel="manifest" href="/site.webmanifest">
<meta property="og:type" content="{ogtype}">
<meta property="og:locale" content="es_ES">
<meta property="og:site_name" content="{site}">
<meta property="og:title" content="{ogt}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{ogimg}">
<meta property="og:image:type" content="image/png">
<meta property="og:image:width" content="{ogw}">
<meta property="og:image:height" content="{ogh}">
<meta property="og:image:alt" content="{site} gratis: Verifactu, factura electrónica B2B, QR tributario, huella y morosidad">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{ogt}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{ogimg}">
<style>{css}</style>
<script type="application/ld+json">
{ld}
</script>
</head>
<body>
{header}
<main id="contenido" class="wrap" tabindex="-1">
{body}
</main>
{footer}
<script src="/assets/core.js?v={v}" defer></script>
<script src="/assets/ui.js?v={v}" defer></script>
{scripts}
</body>
</html>
""".format(gsv=gsv, theme=THEME_INIT, ogtype="article" if page.get("article") else "website", title=e(title), desc=e(desc), csp=csp_meta(),
           css=INLINE_CSS, ogimg=SITE_URL + OG_IMAGE, ogw=OG_W, ogh=OG_H, logo=LOGO_PNG, robots=robots, url=url, site=e(SITE),
           ogt=e(page.get("og_title", title)), v=ASSET_V, ld=jsonld(page, path).replace("</", "<\\/"), header=header(path),
           body="\n".join(parts), footer=footer(), scripts=scripts)
    if BRAND != DEFAULT_BRAND:
        doc = doc.replace(DEFAULT_BRAND, BRAND)
    return prefix_links(doc)
