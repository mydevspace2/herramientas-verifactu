// Navegador real (Chromium headless, Playwright) con la CSP de cada página aplicada: sin errores JS ni violaciones CSP,
// cada herramienta funciona, modo oscuro, sin desbordamiento horizontal en móvil (375 px).
// Uso: NODE_PATH=/ruta/a/node_modules(playwright) node qa/test-browser-csp.js
const { chromium } = require("playwright");
const http = require("http"), fs = require("fs"), path = require("path");
const ROOT = path.join(__dirname, "../out");
const robots = fs.readFileSync(path.join(ROOT, "robots.txt"), "utf8");
const BASE = new URL(/Sitemap: (\S+)\/sitemap\.xml/.exec(robots)[1] + "/").pathname.replace(/\/$/, "");
const TYPES = { ".html": "text/html; charset=utf-8", ".js": "application/javascript", ".svg": "image/svg+xml", ".png": "image/png", ".xml": "application/xml", ".txt": "text/plain", ".webmanifest": "application/manifest+json" };
const PORT = 8781;
const srv = http.createServer((q, r) => {
  let p = decodeURIComponent(q.url.split("?")[0]);
  if (!p.startsWith(BASE + "/")) { r.writeHead(404); return r.end("fuera de BASE"); }
  p = p.slice(BASE.length); if (p.endsWith("/")) p += "index.html";
  const f = path.join(ROOT, p);
  if (!fs.existsSync(f) || fs.statSync(f).isDirectory()) { r.writeHead(404, { "content-type": TYPES[".html"] }); return r.end(fs.readFileSync(path.join(ROOT, "404.html"))); }
  r.writeHead(200, { "content-type": TYPES[path.extname(f)] || "application/octet-stream" }); r.end(fs.readFileSync(f));
}).listen(PORT);
const OUT = path.join(__dirname, "out"); fs.mkdirSync(OUT, { recursive: true });
let pass = 0, fail = 0;
const ok = (c, m) => { if (c) { pass++; console.log("  ✓ " + m); } else { fail++; console.log("  ✗ " + m); } };
const txt = (p, s) => p.textContent(s).then(x => x || "");
const PAGES = ["/", "/generador-qr-verifactu/", "/validar-qr-verifactu/", "/calcular-huella-verifactu/", "/ejemplo-xml-verifactu/", "/blog/", "/blog/fechas-verifactu-2027-2028/",
  "/blog/verifactu-gratis-aplicacion-aeat/", "/blog/tamano-posicion-qr-verifactu/", "/sobre-nosotros/", "/contacto/", "/aviso-legal/", "/privacidad/", "/no-existe/"];
const ACTIONS = {
  "/": async p => {
    const cd = await txt(p, "#cd-is");
    await p.check('input[name="tipo"][value="sociedad"]'); await p.check('input[name="emi"][value="programa"]'); await p.click('#ob-form button[type="submit"]');
    const a = await txt(p, "#ob-out");
    await p.check('input[name="tipo"][value="autonomo"]'); await p.check('input[name="sii"][value="si"]'); await p.click('#ob-form button[type="submit"]');
    const b = await txt(p, "#ob-out");
    await p.check('input[name="sii"][value="no"]'); await p.check('input[name="dom"][value="pv"]'); await p.click('#ob-form button[type="submit"]');
    const c = await txt(p, "#ob-out");
    return /quedan \d+ días/.test(cd) && /1 de enero de 2027/.test(a) && /octubre de 2028/.test(a) && /NO está publicado en el BOE/.test(a) && /SII/.test(b) && /TicketBAI/.test(c);
  },
  "/generador-qr-verifactu/": async (p, ctx) => {
    await p.click("#q-ex"); await p.waitForSelector("#q-preview svg");
    const url = await txt(p, "#q-url");
    const okUrl = url === "https://prewww2.aeat.es/wlpl/TIKE-CONT/ValidarQR?nif=89890001K&numserie=12345678-G33&fecha=01-09-2024&importe=241.40";
    const d1 = p.waitForEvent("download"); await p.click("#q-svg"); const svgDl = await d1; await svgDl.saveAs(path.join(OUT, "descarga-qr.svg"));
    const d2 = p.waitForEvent("download"); await p.click("#q-png"); const pngDl = await d2; await pngDl.saveAs(path.join(OUT, "descarga-qr-600ppp.png"));
    const svg = fs.readFileSync(path.join(OUT, "descarga-qr.svg"), "utf8");
    await p.evaluate(() => { window.print = () => { window.__printed = document.getElementById("print-sheet").innerHTML; }; });
    await p.click("#q-print");
    const printed = await p.evaluate(() => window.__printed || "");
    // modo No VERI*FACTU: sin leyenda
    await p.check('input[name="modo"][value="no"]'); await p.waitForTimeout(100);
    const noVf = await txt(p, "#q-url"); const prevNo = await p.innerHTML("#q-preview");
    // 40 mm + leyenda larga sobre tique de 57 mm
    await p.check('input[name="modo"][value="verifactu"]'); await p.selectOption("#q-size", "40"); await p.selectOption("#q-paper", "t57"); await p.check('input[name="leyenda"][value="larga"]'); await p.waitForTimeout(100);
    const prev57 = await p.innerHTML("#q-preview");
    return okUrl && /width="[\d.]+mm"/.test(svg) && svg.includes("QR tributario:") && svg.includes("VERI*FACTU") && printed.includes("mm\"") &&
      noVf.includes("ValidarQRNoVerifactu") && !prevNo.includes("VERI*FACTU</text>") && prev57.includes("sede electrónica") && fs.statSync(path.join(OUT, "descarga-qr-600ppp.png")).size > 5000;
  },
  "/validar-qr-verifactu/": async p => {
    await p.click("#v-ex-ok"); const a = await p.getAttribute("#v-res", "class");
    await p.click("#v-ex-amp"); const b = await txt(p, "#v-res");
    await p.click("#v-ex-bad"); const c = await txt(p, "#v-res");
    await p.setInputFiles("#v-file", path.join(OUT, "qr-ejemplo.png"));
    await p.waitForFunction(() => /cumple el formato oficial/.test(document.getElementById("v-res").textContent), null, { timeout: 8000 });
    const d = await p.inputValue("#v-url");
    return /\bok\b/.test(a) && /2005/.test(b) && /G33/.test(b) && /phishing/.test(c) && d.startsWith("https://www2.agenciatributaria.gob.es/wlpl/TIKE-CONT/ValidarQR?nif=89890001K");
  },
  "/calcular-huella-verifactu/": async p => {
    const r = [];
    for (const [b, h] of [["#h-ex1", "3C464DAF61ACB827C65FDA19F352A4E3BDC2C640E9E9FC4CC058073F38F12F60"], ["#h-ex2", "F7B94CFD8924EDFF273501B01EE5153E4CE8F259766F88CF6ACB8935802A2B97"], ["#h-ex3", "177547C0D57AC74748561D054A9CEC14B4C4EA23D1BEFD6F2E69E3A388F90C68"]]) {
      await p.click(b); r.push((await txt(p, "#h-hash")) === h && /Coincide exactamente/.test(await txt(p, "#h-out")));
    }
    await p.click("#h-ex-ev"); const ev = (await txt(p, "#h-hash")).length === 64;
    await p.click("#h-next"); const chained = (await p.inputValue("#h-evento-7")).length === 64;
    await p.click("#c-ex"); const c1 = await p.getAttribute("#c-res", "class");
    await p.click("#c-ex-bad"); const c2 = await p.getAttribute("#c-res", "class");
    return r.every(Boolean) && ev && chained && /\bok\b/.test(c1) && /\bbad\b/.test(c2);
  },
  "/ejemplo-xml-verifactu/": async p => {
    await p.click("#x-ex"); await p.waitForTimeout(100);
    const x = await p.inputValue("#x-in"); fs.writeFileSync(path.join(OUT, "xml-desde-navegador.xml"), x);
    const res = await txt(p, "#x-res");
    const d = p.waitForEvent("download"); await p.click("#x-dl"); await d;
    await p.fill("#x-in", x.replace("<sf:TipoFactura>F1</sf:TipoFactura>", "<sf:TipoFactura>F9</sf:TipoFactura>")); await p.click("#x-check");
    const bad = await txt(p, "#x-res");
    return x.includes("<sfLR:RegFactuSistemaFacturacion") && /Estructura básica correcta/.test(res) && /F9/.test(bad);
  },
  "/no-existe/": async p => /Página no encontrada/.test(await txt(p, "h1")),
};
(async () => {
  const b = await chromium.launch();
  for (const u of PAGES) {
    for (const mobile of [false, true]) {
      const ctx = await b.newContext(mobile ? { viewport: { width: 375, height: 740 }, deviceScaleFactor: 2, isMobile: true, hasTouch: true, acceptDownloads: true } : { acceptDownloads: true });
      const p = await ctx.newPage(); const errs = [];
      p.on("console", m => { if (m.type() === "error" && !(u === "/no-existe/" && /404/.test(m.text()))) errs.push(m.text()); });
      p.on("pageerror", e => errs.push(String(e)));
      await p.addInitScript(() => document.addEventListener("securitypolicyviolation", e => console.error("CSP: " + e.violatedDirective + " " + e.blockedURI)));
      const resp = await p.goto("http://127.0.0.1:" + PORT + BASE + u, { waitUntil: "load" });
      const label = u + (mobile ? " [móvil 375px]" : "");
      if (!mobile) {
        const css = await p.evaluate(() => ({ theme: document.documentElement.getAttribute("data-theme"), wrap: getComputedStyle(document.querySelector(".wrap")).maxWidth }));
        ok(css.theme && css.wrap === "1080px", label + " – CSS inline aplicado (" + css.theme + ")");
        if (ACTIONS[u]) { let r = false; try { r = await ACTIONS[u](p, ctx); } catch (e) { errs.push("acción: " + e.message.split("\n")[0]); } ok(r, label + " – la herramienta funciona en Chromium"); }
        if (u === "/no-existe/") ok(resp.status() === 404, label + " – responde 404 con la página 404");
        const t1 = await p.evaluate(() => document.documentElement.getAttribute("data-theme")); await p.click("button.theme-toggle");
        const t2 = await p.evaluate(() => [document.documentElement.getAttribute("data-theme"), getComputedStyle(document.body).backgroundColor]);
        ok(t2[0] !== t1, label + " – conmutador de tema (" + t1 + " → " + t2[0] + ", fondo " + t2[1] + ")");
      } else {
        const sw = await p.evaluate(() => document.documentElement.scrollWidth);
        ok(sw <= 376, label + " – sin desbordamiento horizontal (scrollWidth " + sw + ")");
        await p.click(".nav-toggle"); ok(await p.isVisible("#site-nav"), label + " – menú móvil se abre");
        if (u === "/generador-qr-verifactu/") { await p.click("#q-ex"); await p.waitForSelector("#q-preview svg"); const sw2 = await p.evaluate(() => document.documentElement.scrollWidth); ok(sw2 <= 376, label + " – vista previa A4 cabe en móvil (" + sw2 + ")"); await p.screenshot({ path: path.join(OUT, "movil-generador.png"), fullPage: false }); }
        if (u === "/") await p.screenshot({ path: path.join(OUT, "movil-portada.png") });
      }
      ok(errs.length === 0, label + " – sin errores JS ni violaciones CSP" + (errs.length ? ": " + errs.join(" | ") : ""));
      if (!mobile && u === "/") await p.screenshot({ path: path.join(OUT, "escritorio-portada.png"), fullPage: false });
      await ctx.close();
    }
  }
  await b.close(); srv.close();
  console.log("\nResultado: " + pass + " correctas, " + fail + " fallidas"); process.exit(fail ? 1 : 0);
})();
