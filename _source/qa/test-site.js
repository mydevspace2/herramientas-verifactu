// Pruebas estáticas de la web generada (out/): enlaces, meta, JSON-LD, hreflang, CSP, sitemap, robots y extensión del contenido.
// Uso: node qa/test-site.js  (BASE se lee de out/robots.txt)
const fs = require("fs"), path = require("path"), assert = require("assert");
const { JSDOM } = require("jsdom");
const ROOT = path.join(__dirname, "../out");
let pass = 0, fail = 0;
function t(name, fn) { try { fn(); pass++; console.log("  ✓ " + name); } catch (e) { fail++; console.log("  ✗ " + name + "\n      " + e.message); } }
const robots = fs.readFileSync(path.join(ROOT, "robots.txt"), "utf8");
const SITE = /Sitemap: (\S+)\/sitemap\.xml/.exec(robots)[1];
const BASE = new URL(SITE + "/").pathname.replace(/\/$/, "");
const sitemap = fs.readFileSync(path.join(ROOT, "sitemap.xml"), "utf8");
const pages = [];
(function walk(d) { for (const f of fs.readdirSync(d)) { const p = path.join(d, f); if (fs.statSync(p).isDirectory()) walk(p); else if (f.endsWith(".html")) pages.push(p); } })(ROOT);
function toFile(u) {
  u = u.split("#")[0].split("?")[0];
  if (!u.startsWith(BASE + "/")) return null;
  let p = path.join(ROOT, decodeURIComponent(u.slice(BASE.length)));
  if (u.endsWith("/")) p = path.join(p, "index.html");
  return p;
}
const TOOLS = ["/", "/generador-qr-verifactu/", "/validar-qr-verifactu/", "/calcular-huella-verifactu/", "/ejemplo-xml-verifactu/", "/factura-electronica-obligatoria/", "/periodo-medio-pago-proveedores/", "/intereses-demora-comerciales/"];
const titles = {}, descs = {}, words = [];
console.log("Sitio: " + SITE + " (BASE «" + BASE + "») – " + pages.length + " páginas HTML");
t("robots.txt bloquea /_source/ y enlaza el sitemap", () => { assert.ok(robots.includes("Disallow: " + BASE + "/_source/")); assert.ok(robots.includes("Sitemap: " + SITE + "/sitemap.xml")); });
const SM_N = pages.filter(p => !p.endsWith("404.html")).length;
t("sitemap.xml bien formado: una URL por página indexable (" + SM_N + ") y <lastmod> solo AAAA-MM-DD", () => { assert.strictEqual((sitemap.match(/<loc>/g) || []).length, SM_N); const lm = sitemap.match(/<lastmod>[^<]*<\/lastmod>/g) || []; assert.strictEqual(lm.length, SM_N); lm.forEach(x => assert.ok(/^<lastmod>\d{4}-\d{2}-\d{2}<\/lastmod>$/.test(x), x)); assert.ok(sitemap.startsWith('<?xml version="1.0"')); });
for (const file of pages) {
  const rel = "/" + path.relative(ROOT, file).replace(/index\.html$/, "");
  const html = fs.readFileSync(file, "utf8");
  const doc = new JSDOM(html).window.document;
  const is404 = rel.includes("404");
  t(rel + " – enlaces internos existen (con BASE)", () => {
    const bad = [];
    doc.querySelectorAll("a[href], link[href], script[src]").forEach(el => {
      const u = el.getAttribute("href") || el.getAttribute("src");
      if (/^(https?:|mailto:|#)/.test(u)) return;
      const f = toFile(u);
      if (!f || !fs.existsSync(f)) bad.push(u);
    });
    assert.deepStrictEqual(bad, []);
  });
  t(rel + " – anclas #id existen y no hay id duplicados", () => {
    const bad = []; doc.querySelectorAll('a[href^="#"]').forEach(a => { const id = a.getAttribute("href").slice(1); if (id && !doc.getElementById(id)) bad.push(id); });
    assert.deepStrictEqual(bad, []);
    const ids = [...doc.querySelectorAll("[id]")].map(e => e.id); assert.deepStrictEqual(ids.filter((x, i) => ids.indexOf(x) !== i), []);
  });
  t(rel + " – JSON-LD válido (WebApplication/WebPage, BreadcrumbList, FAQPage = FAQ visible)", () => {
    const j = JSON.parse(doc.querySelector('script[type="application/ld+json"]').textContent);
    const types = j["@graph"].map(x => x["@type"]);
    assert.ok(types.includes("BreadcrumbList")); assert.ok(types.includes("WebApplication") || types.includes("WebPage") || types.includes("CollectionPage"));
    const faq = j["@graph"].find(x => x["@type"] === "FAQPage");
    assert.strictEqual(faq ? faq.mainEntity.length : 0, doc.querySelectorAll(".faq details").length);
    if (TOOLS.includes(rel) || rel.startsWith("/blog/") && rel !== "/blog/") assert.ok(faq && faq.mainEntity.length >= 5, "FAQ ≥ 5");
    j["@graph"].forEach(x => { if (x.url) assert.ok(x.url.startsWith(SITE + "/"), x.url); });
  });
  t(rel + " – SEO: Organization + WebSite en JSON-LD, Article con fechas ISO en guías, <img> con alt, <time> ISO", () => {
    const j = JSON.parse(doc.querySelector('script[type="application/ld+json"]').textContent);
    const types = j["@graph"].map(x => x["@type"]);
    assert.ok(types.includes("Organization") && types.includes("WebSite"), types.join());
    if (rel.startsWith("/blog/") && rel !== "/blog/") {
      const a = j["@graph"].find(x => x["@type"] === "Article"); assert.ok(a, "Article");
      assert.ok(/^\d{4}-\d{2}-\d{2}$/.test(a.datePublished) && /^\d{4}-\d{2}-\d{2}$/.test(a.dateModified), a.datePublished + " " + a.dateModified);
      const toolLinks = [...doc.querySelectorAll("article.content a[href]")].map(x => x.getAttribute("href")).filter(h => TOOLS.some(u => h === BASE + u));
      assert.ok(toolLinks.length >= 1, "la guía enlaza al menos una herramienta");
    }
    if (TOOLS.includes(rel)) assert.ok(types.includes("WebApplication"), "WebApplication");
    doc.querySelectorAll("img").forEach(im => assert.ok(im.hasAttribute("alt"), "img sin alt"));
    doc.querySelectorAll("time[datetime]").forEach(tm => assert.ok(/^\d{4}-\d{2}-\d{2}$/.test(tm.getAttribute("datetime")), tm.getAttribute("datetime")));
    if (!is404) assert.ok(doc.querySelectorAll("#guias-relacionadas + .hub a").length >= (rel === "/blog/" || ["/sobre-nosotros/", "/contacto/", "/aviso-legal/", "/privacidad/"].includes(rel) ? 0 : 3), "≥ 3 guías relacionadas");
  });
  t(rel + " – meta: title ≤ 70, description 70–160, canonical, hreflang es/x-default, OG, un H1, lang=es", () => {
    const title = doc.title, desc = doc.querySelector('meta[name="description"]').content;
    assert.ok(title.length > 10 && title.length <= 70, "title " + title.length + ": " + title);
    assert.ok(desc.length >= 70 && desc.length < 160, "desc " + desc.length);
    assert.ok(!titles[title], "title repetido"); titles[title] = 1; assert.ok(!descs[desc], "description repetida"); descs[desc] = 1;
    const can = doc.querySelector('link[rel="canonical"]').getAttribute("href");
    if (!is404) { assert.strictEqual(can, SITE + rel); assert.ok(sitemap.includes("<loc>" + can + "</loc>"), "en sitemap"); }
    assert.strictEqual(doc.querySelector('link[hreflang="es"]').getAttribute("href"), can);
    assert.strictEqual(doc.querySelector('link[hreflang="x-default"]').getAttribute("href"), can);
    ["og:title", "og:description", "og:url", "og:type", "og:image", "og:locale"].forEach(p => assert.ok(doc.querySelector('meta[property="' + p + '"]'), p));
    assert.strictEqual(doc.querySelector('meta[property="og:locale"]').content, "es_ES");
    assert.ok(doc.querySelector('meta[property="og:image"]').content.startsWith(SITE + "/assets/og-verifactu.png"));
    assert.strictEqual(doc.querySelectorAll("h1").length, 1); assert.strictEqual(doc.documentElement.lang, "es");
    assert.strictEqual(doc.querySelector('meta[name="robots"]').content, is404 ? "noindex" : "index,follow,max-image-preview:large");
  });
  t(rel + " – seguridad y rendimiento: CSP, CSS inline, sin style=, sin scripts inline salvo tema/JSON-LD, sin CDN", () => {
    const csp = doc.querySelector('meta[http-equiv="Content-Security-Policy"]').content;
    assert.ok(/default-src 'self'/.test(csp) && /object-src 'none'/.test(csp) && !/unsafe-inline|unsafe-eval/.test(csp));
    assert.ok(doc.querySelector("style").textContent.length > 5000, "CSS inline");
    assert.strictEqual(doc.querySelectorAll('link[rel="stylesheet"]').length, 0);
    assert.strictEqual(doc.querySelectorAll("[style]").length, 0, "atributos style");
    doc.querySelectorAll("script:not([src])").forEach(s => assert.ok(s.type === "application/ld+json" || /localStorage\.getItem\("theme"\)/.test(s.textContent)));
    doc.querySelectorAll("script[src]").forEach(s => assert.ok(s.getAttribute("src").startsWith(BASE + "/assets/") && s.hasAttribute("defer")));
    assert.ok(!/googleapis|gstatic|cdn\.|unpkg|jsdelivr|google-analytics|gtag\(/.test(html));
    assert.ok(!/on(click|load|error)=/i.test(html), "manejadores inline");
  });
  t(rel + " – accesibilidad: campos con etiqueta, botones con texto", () => {
    const un = [];
    doc.querySelectorAll("input:not([type=radio]):not([type=checkbox]), textarea, select").forEach(i => { if (!doc.querySelector('label[for="' + i.id + '"]') && !i.getAttribute("aria-label")) un.push(i.id); });
    assert.deepStrictEqual(un, []);
    doc.querySelectorAll("button").forEach(b => assert.ok(b.textContent.trim() || b.getAttribute("aria-label"), "botón vacío"));
    assert.ok(doc.querySelector('a.skip[href="#contenido"]') && doc.getElementById("contenido"));
  });
  t(rel + " – enlaces visibles a privacidad, aviso legal, contacto y sobre nosotros", () => {
    ["/privacidad/", "/aviso-legal/", "/contacto/", "/sobre-nosotros/"].forEach(u => assert.ok(doc.querySelector('footer a[href="' + BASE + u + '"]'), u));
  });
  const art = doc.querySelector("article.content");
  const n = art ? art.textContent.replace(/\s+/g, " ").trim().split(" ").length : 0;
  words.push([rel, n]);
  if (TOOLS.includes(rel)) t(rel + " – contenido útil bajo la herramienta ≥ 800 palabras (" + n + ")", () => assert.ok(n >= 800, n));
  if (rel.startsWith("/blog/") && rel !== "/blog/") t(rel + " – guía ≥ 700 palabras (" + n + ")", () => assert.ok(n >= 700, n));
}
t("Ninguna página afirma importes de sanciones", () => pages.forEach(f => assert.ok(!/(50\.000|150\.000)\s*(€|euros)/i.test(fs.readFileSync(f, "utf8")), f)));
t("Portada: muestra 1/1/2027, 1/7/2027, octubre 2028, «Última comprobación: 13 de noviembre de 2026» y enlaza BOE + nota de Hacienda", () => {
  const h = fs.readFileSync(path.join(ROOT, "index.html"), "utf8");
  ["1 de enero de 2027", "1 de julio de 2027", "Octubre de 2028", "Última comprobación: 13 de noviembre de 2026", "BOE-A-2023-24840", "nota-informativa-verifactu.pdf"].forEach(s => assert.ok(h.includes(s), s));
});
t("Huella: los tres resultados oficiales aparecen en la página", () => {
  const h = fs.readFileSync(path.join(ROOT, "calcular-huella-verifactu/index.html"), "utf8");
  ["3C464DAF61ACB827C65FDA19F352A4E3BDC2C640E9E9FC4CC058073F38F12F60", "F7B94CFD8924EDFF273501B01EE5153E4CE8F259766F88CF6ACB8935802A2B97", "177547C0D57AC74748561D054A9CEC14B4C4EA23D1BEFD6F2E69E3A388F90C68"].forEach(s => assert.ok(h.includes(s)));
});
t("Navegación: las 8 herramientas y Guías en la cabecera de cada página", () => pages.forEach(f => {
  const doc = new JSDOM(fs.readFileSync(f, "utf8")).window.document;
  TOOLS.concat(["/blog/"]).forEach(u => assert.ok(doc.querySelector('#site-nav a[href="' + BASE + u + '"]'), f + " " + u));
}));
t("Factura B2B: 6/10/2027, 6/10/2028, 6/10/2029, «Última comprobación: 13 de noviembre de 2026», enlaces BOE RD 238/2026 y Orden HAC/1028/2026, art. 12 de 4 días", () => {
  const h = fs.readFileSync(path.join(ROOT, "factura-electronica-obligatoria/index.html"), "utf8");
  ["6 de octubre de 2027", "6 de octubre de 2028", "6 de octubre de 2029", "Última comprobación: 13 de noviembre de 2026", "BOE-A-2026-7295", "BOE-A-2026-20587", "4 días naturales", "excluyendo sábados, domingos y festivos nacionales", "BOE-A-2026-21254"].forEach(s => assert.ok(h.includes(s), s));
});
t("PMP: cita BOE-A-2016-1112, las tres fórmulas del art. 5, el ejemplo (47,60) y el límite de 60 días", () => {
  const h = fs.readFileSync(path.join(ROOT, "periodo-medio-pago-proveedores/index.html"), "utf8");
  ["BOE-A-2016-1112", "Ratio pagadas", "Ratio pendientes", "× 365", "47,60 días", "60 días naturales", "pmp-csv"].forEach(s => assert.ok(h.includes(s), s));
});
t("Intereses de demora: tabla con las 27 resoluciones del BOE (2013-2 a 2026-2), 10,40 %, art. 8.1 citado literalmente y TJUE C-585/20", () => {
  const h = fs.readFileSync(path.join(ROOT, "intereses-demora-comerciales/index.html"), "utf8");
  const boe = JSON.parse(fs.readFileSync(path.join(__dirname, "boe-tipos-demora.json"), "utf8")).filter(x => x.semestre >= "2013-2");
  assert.strictEqual(boe.length, 27);
  boe.forEach(x => { assert.ok(h.includes("txt.php?id=" + x.boe), x.boe); assert.ok(h.includes(x.tipo.toFixed(2).replace(".", ",") + " %"), x.semestre); });
  ["10,40 %", "una cantidad fija de 40 euros, que se añadirá en todo caso y sin necesidad de petición expresa a la deuda principal", "C-585/20", "BOE-A-2004-21830"].forEach(s => assert.ok(h.includes(s), s));
});
t("Las tres herramientas B2B cargan b2b.js y su script propio", () => {
  [["factura-electronica-obligatoria", "page-b2b.js"], ["periodo-medio-pago-proveedores", "page-pmp.js"], ["intereses-demora-comerciales", "page-demora.js"]].forEach(([d, js]) => {
    const h = fs.readFileSync(path.join(ROOT, d, "index.html"), "utf8"); assert.ok(h.includes(BASE + "/assets/b2b.js?") && h.includes(BASE + "/assets/" + js + "?"), d);
  });
});
t("Ningún importe de sanción en la sección B2B (solo se citarían literalmente del BOE)", () => ["factura-electronica-obligatoria", "periodo-medio-pago-proveedores", "intereses-demora-comerciales", "blog/diferencias-verifactu-factura-electronica-b2b", "blog/factura-electronica-obligatoria-autonomos", "blog/calcular-periodo-medio-pago-proveedores-ejemplo", "blog/plazos-pago-ley-morosidad", "blog/verifactu-autonomos"].forEach(d => {
  const h = fs.readFileSync(path.join(ROOT, d, "index.html"), "utf8"); assert.ok(!/(multa|sanci[oó]n)[^.<]{0,60}\d[\d.]*\s*(€|euros)/i.test(h), d);
}));
t("JS de producción minificado y sin eval", () => fs.readdirSync(path.join(ROOT, "assets")).filter(f => f.endsWith(".js")).forEach(f => {
  const s = fs.readFileSync(path.join(ROOT, "assets", f), "utf8"); assert.ok(!/\beval\(|new Function\(/.test(s), f); assert.ok(s.split("\n").length < 40, f + " no minificado");
}));
t("Search Console: meta google-site-verification solo en la portada cuando se compila con VF_GSV", () => {
  const home = fs.readFileSync(path.join(ROOT, "index.html"), "utf8");
  const gsv = process.env.VF_GSV || "";
  if (gsv) assert.ok(home.includes('<meta name="google-site-verification" content="' + gsv + '">'), "falta en portada");
  else assert.ok(!home.includes("google-site-verification"));
  pages.filter(f => path.resolve(f) !== path.resolve(path.join(ROOT, "index.html"))).forEach(f => assert.ok(!fs.readFileSync(f, "utf8").includes("google-site-verification"), f));
});
console.log("\nPalabras en el cuerpo de cada página:"); words.forEach(([r, n]) => console.log("   " + String(n).padStart(5) + "  " + r));
console.log("\nResultado: " + pass + " correctas, " + fail + " fallidas");
process.exit(fail ? 1 : 0);
