// Minificación de recursos: build/assets-src (fuentes legibles) -> out/assets (producción).
// JS: terser (sin eval y sin renombrar globales). CSS: csso -> out/assets/.style.min.css (se inserta inline en cada página).
const fs = require("fs"), path = require("path");
const { minify } = require("terser");
const csso = require("csso");
const SRC = path.join(__dirname, "..", "assets-src");
const OUT = path.join(__dirname, "..", "..", "out", "assets");
(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  let before = 0, after = 0;
  for (const f of fs.readdirSync(SRC)) {
    const src = fs.readFileSync(path.join(SRC, f), "utf8");
    if (f.endsWith(".js")) {
      const r = await minify(src, { ecma: 2015, compress: { passes: 2 }, mangle: true, format: { comments: /^!/ } });
      fs.writeFileSync(path.join(OUT, f), r.code);
      before += src.length; after += r.code.length;
    } else if (f.endsWith(".css")) {
      fs.writeFileSync(path.join(OUT, ".style.min.css"), csso.minify(src).css);
    } else {
      fs.copyFileSync(path.join(SRC, f), path.join(OUT, f));
    }
  }
  console.log("js: " + before + " -> " + after + " B");
})().catch(e => { console.error(e); process.exit(1); });
