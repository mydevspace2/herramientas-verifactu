/*! Herramientas Verifactu – elementos comunes de la interfaz */
(function () {
  "use strict";
  var K = window.VF;
  function $(id) { return document.getElementById(id); }

  // menú móvil
  var tg = document.querySelector(".nav-toggle"), nav = document.getElementById("site-nav");
  if (tg && nav) {
    tg.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      tg.setAttribute("aria-expanded", open ? "true" : "false");
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && nav.classList.contains("open")) { nav.classList.remove("open"); tg.setAttribute("aria-expanded", "false"); tg.focus(); }
    });
  }

  // modo claro / oscuro: prefers-color-scheme + elección guardada (localStorage "theme")
  var root = document.documentElement, thBtn = document.querySelector(".theme-toggle");
  function stored() { try { var t = localStorage.getItem("theme"); return t === "dark" || t === "light" ? t : null; } catch (e) { return null; } }
  function sysDark() { return !!(window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches); }
  function applyTheme(t) {
    root.setAttribute("data-theme", t);
    if (thBtn) { thBtn.setAttribute("aria-pressed", t === "dark" ? "true" : "false"); thBtn.setAttribute("aria-label", t === "dark" ? "Modo claro" : "Modo oscuro"); }
  }
  applyTheme(stored() || root.getAttribute("data-theme") || (sysDark() ? "dark" : "light"));
  if (thBtn) thBtn.addEventListener("click", function () {
    var t = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
    applyTheme(t);
    try { localStorage.setItem("theme", t); } catch (e) {}
  });
  if (window.matchMedia) {
    var mq = window.matchMedia("(prefers-color-scheme: dark)");
    var onSys = function (ev) { if (!stored()) applyTheme(ev.matches ? "dark" : "light"); };
    if (mq.addEventListener) mq.addEventListener("change", onSys); else if (mq.addListener) mq.addListener(onSys);
  }

  function copyText(text, btn) {
    if (!text) return;
    function done(ok) {
      if (!btn) return;
      var old = btn.getAttribute("data-label") || btn.textContent;
      btn.setAttribute("data-label", old);
      btn.textContent = ok ? "Copiado ✓" : "Selecciona y Ctrl+C";
      btn.classList.add("copied-btn");
      var live = $("live");
      if (live) live.textContent = ok ? "Copiado al portapapeles" : "No se ha podido copiar";
      setTimeout(function () { btn.textContent = old; }, 1600);
    }
    function fallback() {
      var ta = document.createElement("textarea");
      ta.value = text; ta.setAttribute("readonly", ""); ta.style.position = "fixed"; ta.style.opacity = "0";
      document.body.appendChild(ta); ta.select();
      var ok = false;
      try { ok = document.execCommand("copy"); } catch (e) {}
      document.body.removeChild(ta);
      done(ok);
    }
    if (navigator.clipboard && window.isSecureContext) navigator.clipboard.writeText(text).then(function () { done(true); }, fallback);
    else fallback();
  }
  // botones con data-copy="id del elemento" o data-copy-text
  document.addEventListener("click", function (e) {
    var b = e.target.closest && e.target.closest("[data-copy],[data-copy-text]");
    if (!b) return;
    var t = b.getAttribute("data-copy-text");
    if (t == null) { var el = $(b.getAttribute("data-copy")); t = el ? (el.getAttribute("data-value") || el.value || el.textContent) : ""; }
    if (t) copyText(t, b);
  });

  var ICON = { ok: "✓", bad: "✕", warn: "!", info: "i" };
  function statusBox(el, level, head, opts) {
    opts = opts || {};
    if (!level) { el.className = "status"; el.innerHTML = ""; return; }
    var h = '<p class="status-head"><span class="ico" aria-hidden="true">' + ICON[level] + "</span>" + K.esc(head) + "</p>";
    if (opts.errors && opts.errors.length) h += '<ul class="reasons-bad">' + opts.errors.map(function (x) { return "<li>" + K.esc(x) + "</li>"; }).join("") + "</ul>";
    if (opts.warnings && opts.warnings.length) h += '<ul class="reasons-warn">' + opts.warnings.map(function (x) { return "<li>" + K.esc(x) + "</li>"; }).join("") + "</ul>";
    if (opts.notes && opts.notes.length) h += "<ul>" + opts.notes.map(function (x) { return "<li>" + K.esc(x) + "</li>"; }).join("") + "</ul>";
    if (opts.html) h += opts.html;
    if (opts.copy) h += '<div class="btns copy-row"><button class="btn ghost small" type="button" data-copy-text="' + K.esc(resultText(head, opts)) + '">' + K.esc(opts.copy === true ? "Copiar resultado" : opts.copy) + "</button></div>";
    el.className = "status " + level;
    el.innerHTML = h;
  }
  // Texto plano del resultado (para pegarlo en un correo a la asesoría)
  function resultText(head, opts) {
    var lines = [head];
    (opts.errors || []).concat(opts.warnings || [], opts.notes || []).forEach(function (x) { lines.push("- " + x); });
    if (opts.html) {
      var d = document.createElement("div"); d.innerHTML = opts.html;
      var cards = d.querySelectorAll(".date-card");
      if (cards.length) Array.prototype.forEach.call(cards, function (c) {
        lines.push("- " + Array.prototype.map.call(c.children, function (x) { return x.textContent.trim(); }).filter(Boolean).join(": "));
      });
      else if (d.textContent.trim()) lines.push(d.textContent.trim());
    }
    lines.push("", "Fuente: " + location.href.split("#")[0]);
    return lines.join("\n");
  }
  // Muestra el resultado sin que lo tape la cabecera fija; con focus=true mueve también el foco (lectores de pantalla)
  function reveal(el, focus) {
    if (!el) return;
    var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    if (focus) { if (!el.hasAttribute("tabindex")) el.setAttribute("tabindex", "-1"); try { el.focus({ preventScroll: true }); } catch (e) { el.focus(); } }
    if (el.scrollIntoView) el.scrollIntoView({ behavior: reduce ? "auto" : "smooth", block: "nearest" });
  }
  // Cuestionarios de opciones: resultado en cuanto todo está respondido, Enter envía
  function autoForm(form, isComplete, run) {
    form.addEventListener("change", function (e) {
      if (e.target && e.target.type === "radio" && isComplete()) run(false);
    });
    form.addEventListener("keydown", function (e) {
      if (e.key !== "Enter" || !e.target || (e.target.type !== "radio" && e.target.type !== "checkbox")) return;
      e.preventDefault();
      if (form.requestSubmit) form.requestSubmit(); else { var b = form.querySelector('[type="submit"]'); if (b) b.click(); }
    });
  }
  function mark(v) {
    if (v === true) return ' <span class="yes" aria-label="correcto">✓</span>';
    if (v === false) return ' <span class="no" aria-label="incorrecto">✕</span>';
    return ' <span class="maybe" aria-label="revisar">?</span>';
  }
  function parts(rows) {
    return '<dl class="parts">' + rows.map(function (r) { return "<div><dt>" + r[0] + "</dt><dd>" + r[1] + "</dd></div>"; }).join("") + "</dl>";
  }

  function readFile(file, asText) {
    return new Promise(function (res, rej) {
      var fr = new FileReader();
      fr.onload = function () { res(fr.result); };
      fr.onerror = function () { rej(fr.error); };
      if (asText) fr.readAsText(file, "utf-8"); else fr.readAsArrayBuffer(file);
    });
  }
  function dropZone(zone, input, onFiles) {
    if (!zone) return;
    ["dragenter", "dragover"].forEach(function (ev) { zone.addEventListener(ev, function (e) { e.preventDefault(); zone.classList.add("drag"); }); });
    ["dragleave", "drop"].forEach(function (ev) { zone.addEventListener(ev, function (e) { e.preventDefault(); zone.classList.remove("drag"); }); });
    zone.addEventListener("drop", function (e) { if (e.dataTransfer && e.dataTransfer.files.length) onFiles(e.dataTransfer.files); });
    input.addEventListener("change", function () { if (input.files.length) onFiles(input.files); });
  }
  function download(name, content, type) {
    var blob = new Blob([content], { type: type || "text/csv;charset=utf-8" });
    var a = document.createElement("a");
    a.href = URL.createObjectURL(blob); a.download = name;
    document.body.appendChild(a); a.click();
    setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 500);
  }

  window.UI = { $: $, copyText: copyText, statusBox: statusBox, reveal: reveal, autoForm: autoForm, mark: mark, parts: parts,
    readFile: readFile, dropZone: dropZone, download: download };
})();
