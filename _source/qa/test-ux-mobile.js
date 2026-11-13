// UX móvil 375×812 (13/11/2026): test visible sin desplazarse, resultado automático + Enter + scroll + copiar,
// sin desplazamiento lateral tras los resultados, campos ≥ 16 px, botones ≥ 44 px, distintivos ≥ 13 px.
// Uso: NODE_PATH=/ruta/node_modules(playwright) node qa/test-ux-mobile.js
const { chromium } = require("playwright");
const http = require("http"), fs = require("fs"), path = require("path");
const ROOT = path.join(__dirname, "../out");
const robots = fs.readFileSync(path.join(ROOT, "robots.txt"), "utf8");
const BASE = new URL(/Sitemap: (\S+)\/sitemap\.xml/.exec(robots)[1] + "/").pathname.replace(/\/$/, "");
const T = { ".html": "text/html; charset=utf-8", ".js": "application/javascript", ".svg": "image/svg+xml", ".png": "image/png" };
const PORT = 8782;
const srv = http.createServer((q, r) => {
  let p = decodeURIComponent(q.url.split("?")[0]);
  if (!p.startsWith(BASE + "/")) { r.writeHead(404); return r.end(); }
  p = p.slice(BASE.length); if (p.endsWith("/")) p += "index.html";
  const f = path.join(ROOT, p);
  if (!fs.existsSync(f)) { r.writeHead(404); return r.end(); }
  r.writeHead(200, { "content-type": T[path.extname(f)] || "application/octet-stream" }); r.end(fs.readFileSync(f));
}).listen(PORT);
let pass = 0, fail = 0;
const ok = (c, m) => { if (c) { pass++; console.log("  ✓ " + m); } else { fail++; console.log("  ✗ " + m); } };
const U = u => "http://localhost:" + PORT + BASE + u;
const sw = p => p.evaluate(() => document.documentElement.scrollWidth);
const top = (p, s) => p.evaluate(s => { const e = document.querySelector(s); return e ? Math.round(e.getBoundingClientRect().top + scrollY) : 99999; }, s);
const inView = (p, s) => p.evaluate(s => { const r = document.querySelector(s).getBoundingClientRect(); return r.top < innerHeight && r.bottom > 0 && r.height > 0; }, s);
const sizes = p => p.evaluate(() => {
  const vis = e => { const r = e.getBoundingClientRect(); return r.width > 0 && r.height > 0 && getComputedStyle(e).visibility !== "hidden"; };
  const fs = e => parseFloat(getComputedStyle(e).fontSize);
  const inp = [...document.querySelectorAll('main input:not([type=checkbox]):not([type=radio]):not([type=file]), main select, main textarea')].filter(vis).filter(e => fs(e) < 16).map(e => e.id + ":" + fs(e));
  const btn = [...document.querySelectorAll("main button, main .btn")].filter(vis).filter(e => e.getBoundingClientRect().height < 43.5).map(e => (e.id || e.textContent.trim().slice(0, 20)) + ":" + Math.round(e.getBoundingClientRect().height));
  const bad = [...document.querySelectorAll(".badge, .tag, .trust li")].filter(vis).filter(e => fs(e) < 12.95).map(e => e.textContent.trim().slice(0, 20) + ":" + fs(e));
  return { inp, btn, bad };
});
(async () => {
  const b = await chromium.launch();
  const ctx = await b.newContext({ viewport: { width: 375, height: 812 }, deviceScaleFactor: 2, isMobile: true, hasTouch: true });
  await ctx.grantPermissions(["clipboard-read", "clipboard-write"], { origin: "http://localhost:" + PORT });
  const p = await ctx.newPage();
  const errs = []; p.on("pageerror", e => errs.push(e.message)); p.on("console", m => { if (m.type() === "error") errs.push(m.text()); });

  console.log("Portada – test ¿estoy obligado?");
  await p.goto(U("/"));
  const tHome = await top(p, 'section[aria-labelledby="ob-h"]'), q1 = await top(p, "#ob-form fieldset");
  ok(tHome < 812 && q1 < 812, "test visible sin desplazarse en 375×812 (tarjeta a " + tHome + " px, 1.ª pregunta a " + q1 + " px)");
  ok((await top(p, 'section[aria-labelledby="estado-h"]')) > tHome, "tarjeta de fechas debajo del test");
  await p.check('input[name="tipo"][value="autonomo"]');
  ok((await p.textContent("#ob-out")).trim() === "", "sin resultado mientras falta una respuesta");
  await p.check('input[name="emi"][value="programa"]'); await p.waitForTimeout(900);
  const a = await p.textContent("#ob-out");
  ok(/estás obligado/.test(a) && /1 de julio de 2027/.test(a), "resultado automático al responder todo (sin pulsar el botón)");
  ok(await inView(p, "#ob-out .status-head"), "el resultado se desplaza a la vista");
  ok(await p.isVisible('#ob-form button[type="submit"]'), "el botón «Ver mi resultado» sigue ahí");
  ok((await sw(p)) <= 375, "sin desplazamiento lateral tras el resultado (" + (await sw(p)) + ")");
  await p.click("#ob-out [data-copy-text]"); await p.waitForTimeout(200);
  const clip = await p.evaluate(() => navigator.clipboard.readText().catch(() => ""));
  ok(/estás obligado/.test(clip) && /1 de julio de 2027/.test(clip) && /Fuente: http/.test(clip), "«Copiar resultado» copia el texto del resultado");
  await p.click('#ob-form button[type="reset"]');
  ok((await p.textContent("#ob-out")).trim() === "", "«Empezar de nuevo» borra el resultado");
  await p.check('input[name="tipo"][value="sociedad"]'); await p.focus('input[name="tipo"][value="sociedad"]'); await p.keyboard.press("Enter"); await p.waitForTimeout(300);
  ok(/Falta responder: cómo emites/.test(await p.textContent("#ob-out")), "Enter en una opción envía el test");
  await p.check('input[name="emi"][value="programa"]'); await p.focus('input[name="emi"][value="programa"]'); await p.keyboard.press("Enter"); await p.waitForTimeout(300);
  ok(/1 de enero de 2027/.test(await p.textContent("#ob-out")), "Enter con todo respondido muestra el resultado (sociedad → 1/1/2027)");
  const s0 = await sizes(p); ok(!s0.inp.length && !s0.btn.length && !s0.bad.length, "portada: campos ≥16 px, botones ≥44 px, distintivos ≥13 px " + JSON.stringify(s0));
  const trust = await p.textContent(".trust"); ok(/Gratis, sin registro/.test(trust) && !/publicidad/i.test(trust), "distintivo sin «publicidad» (" + trust.trim() + ")");

  console.log("Factura electrónica B2B");
  await p.goto(U("/factura-electronica-obligatoria/"));
  const tB = await top(p, 'section[aria-labelledby="fe-h"]'), qB = await top(p, "#fe-form fieldset");
  ok(tB < 812 && qB < 812, "test visible sin desplazarse en 375×812 (tarjeta a " + tB + " px, 1.ª pregunta a " + qB + " px)");
  await p.check('input[name="forma"][value="juridica"]'); await p.check('input[name="vol"][value="mas"]'); await p.waitForTimeout(900);
  const fb = await p.textContent("#fe-out");
  ok(/6 de octubre de 2027/.test(fb), "resultado automático al responder todo");
  ok(await inView(p, "#fe-out .status-head"), "el resultado se desplaza a la vista");
  ok(await p.isVisible("#fe-out [data-copy-text]"), "botón «Copiar resultado» en el resultado B2B");
  await p.check('input[name="vol"][value="menos"]'); await p.focus('input[name="vol"][value="menos"]'); await p.keyboard.press("Enter"); await p.waitForTimeout(300);
  ok(/6 de octubre de 2028/.test(await p.textContent("#fe-out")), "Enter actualiza el resultado (≤ 8 M€ → 6/10/2028)");
  await p.click('#p4-form button[type="submit"]'); await p.waitForTimeout(600);
  ok(/15 de octubre de 2027/.test(await p.textContent("#p4-out")) && await inView(p, "#p4-out .status-head"), "plazo de 4 días: 08/10/2027 → 15/10/2027, a la vista");
  ok((await sw(p)) <= 375, "sin desplazamiento lateral tras los resultados (" + (await sw(p)) + ")");
  const s1 = await sizes(p); ok(!s1.inp.length && !s1.btn.length && !s1.bad.length, "B2B: tamaños " + JSON.stringify(s1));

  for (const [u, steps, name] of [
    ["/ejemplo-xml-verifactu/", ["#x-ex", '#x-form button[type="submit"]', "#x-check"], "Ejemplo XML"],
    ["/calcular-huella-verifactu/", ["#h-ex1", "#h-ex2", "#c-ex"], "Calcular huella"],
    ["/intereses-demora-comerciales/", ["#dm-ex", "#dm-go"], "Intereses de demora"],
    ["/periodo-medio-pago-proveedores/", ["#pmp-ex", "#pmp-go"], "Periodo medio de pago"],
    ["/generador-qr-verifactu/", ["#q-ex"], "Generador QR"],
    ["/validar-qr-verifactu/", ["#v-ex-ok"], "Validar QR"]]) {
    console.log(name);
    await p.goto(U(u));
    for (const s of steps) { if (await p.$(s)) { await p.click(s); await p.waitForTimeout(250); } }
    const w = await sw(p); ok(w <= 375, name + ": sin desplazamiento lateral tras los resultados (" + w + ")");
    const s = await sizes(p); ok(!s.inp.length && !s.btn.length && !s.bad.length, name + ": campos ≥16 px, botones ≥44 px, distintivos ≥13 px " + JSON.stringify(s));
  }
  ok(!errs.length, "sin errores JS " + JSON.stringify(errs));
  await p.screenshot({ path: path.join(__dirname, "out", "movil-375-portada-fold.png") });
  await b.close(); srv.close();
  console.log("\nResultado: " + pass + " correctas, " + fail + " fallidas");
  process.exit(fail ? 1 : 0);
})();
