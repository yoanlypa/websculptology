/* Sculptology — comportamiento. Clásico (IIFE), sin módulos ni dependencias. */
(function () {
  "use strict";
  var doc = document, root = doc.documentElement;
  root.classList.remove("no-js");

  function safe(fn, name) { try { fn(); } catch (e) { if (window.console) console.warn("[sculptology] " + name, e); } }
  function $(s, c) { return (c || doc).querySelector(s); }
  function $$(s, c) { return Array.prototype.slice.call((c || doc).querySelectorAll(s)); }
  var reduced = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* idioma: recuerda la elección de las banderas */
  safe(function () {
    var lang = root.getAttribute("lang") === "en" ? "en" : "es";
    $$(".lang a").forEach(function (a) {
      a.addEventListener("click", function () { try { localStorage.setItem("sculpt-lang", a.getAttribute("hreflang")); } catch (e) {} });
    });
    var saved = null;
    try { saved = localStorage.getItem("sculpt-lang"); } catch (e) {}
    /* Solo se redirige desde la portada (/) a /en/ si la persona eligió inglés antes.
       Una visita directa a /en/ (Google, enlace) nunca se redirige. */
    var fromOwnSite = doc.referrer.indexOf(location.host) !== -1;
    if (lang === "es" && saved === "en" && !fromOwnSite && location.pathname === "/") {
      var target = $('.lang a[hreflang="en"]');
      if (target) location.replace(target.getAttribute("href") + (location.hash || ""));
    }
  }, "lang");

  /* cabecera sólida al hacer scroll + menú móvil */
  safe(function () {
    var header = $(".header");
    function onScroll() { header.classList.toggle("solid", window.scrollY > 40 || header.hasAttribute("data-solid")); }
    onScroll(); window.addEventListener("scroll", onScroll, { passive: true });
    var burger = $(".burger");
    burger.addEventListener("click", function () {
      var open = root.classList.toggle("menu-open");
      burger.setAttribute("aria-expanded", open ? "true" : "false");
    });
    $$(".nav a").forEach(function (a) { a.addEventListener("click", function () { root.classList.remove("menu-open"); burger.setAttribute("aria-expanded", "false"); }); });
  }, "header");

  /* aparición al hacer scroll (umbral bajo + red de seguridad) */
  safe(function () {
    var els = $$(".reveal");
    if (!("IntersectionObserver" in window)) { els.forEach(function (e) { e.classList.add("in"); }); return; }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); } });
    }, { threshold: 0.04, rootMargin: "0px 0px -4% 0px" });
    els.forEach(function (e) { io.observe(e); });
    setTimeout(function () { els.forEach(function (e) { e.classList.add("in"); }); }, 6000);
  }, "reveal");

  /* parallax suave del hero */
  safe(function () {
    var bg = $(".hero-bg"); if (!bg || reduced) return;
    var ticking = false;
    window.addEventListener("scroll", function () {
      if (ticking) return; ticking = true;
      requestAnimationFrame(function () {
        var y = Math.min(window.scrollY, window.innerHeight);
        bg.style.transform = "translate3d(0," + (y * 0.22).toFixed(1) + "px,0) scale(1.04)";
        ticking = false;
      });
    }, { passive: true });
  }, "parallax");

  /* duplicar marquesina para bucle continuo */
  safe(function () {
    var t = $(".marquee-track"); if (!t || t.dataset.dup) return;
    t.innerHTML += t.innerHTML; t.dataset.dup = "1";
  }, "marquee");

  /* vídeo: se reproduce en silencio solo mientras está a la vista (no si el sistema pide menos movimiento) */
  safe(function () {
    var vids = $$("video[data-autoplay]"); if (!vids.length || reduced || !("IntersectionObserver" in window)) return;
    var vio = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        var v = en.target;
        if (en.isIntersecting) { var p = v.play(); if (p && p.catch) p.catch(function () {}); } else { v.pause(); }
      });
    }, { threshold: 0.35 });
    vids.forEach(function (v) { vio.observe(v); });
  }, "video");

  /* visor de fotos */
  safe(function () {
    var lb = $(".lightbox"); if (!lb) return;
    var img = $("img", lb), cap = $(".lb-cap", lb), group = [], idx = 0;
    function show(i) {
      idx = (i + group.length) % group.length;
      var t = group[idx], im = $("img", t);
      img.src = im.currentSrc || im.src; img.alt = im.alt;
      cap.textContent = t.getAttribute("data-cap") || "";
    }
    function open(tile) {
      group = $$(".tile", tile.closest("[data-gallery], .res"));
      show(group.indexOf(tile)); lb.classList.add("open"); lb.setAttribute("aria-hidden", "false"); doc.body.style.overflow = "hidden";
    }
    function close() { lb.classList.remove("open"); lb.setAttribute("aria-hidden", "true"); doc.body.style.overflow = ""; }
    $$(".tile").forEach(function (t) { t.addEventListener("click", function () { open(t); }); });
    $(".lb-close", lb).addEventListener("click", close);
    $(".lb-prev", lb).addEventListener("click", function () { show(idx - 1); });
    $(".lb-next", lb).addEventListener("click", function () { show(idx + 1); });
    lb.addEventListener("click", function (e) { if (e.target === lb) close(); });
    doc.addEventListener("keydown", function (e) {
      if (!lb.classList.contains("open")) return;
      if (e.key === "Escape") close(); else if (e.key === "ArrowLeft") show(idx - 1); else if (e.key === "ArrowRight") show(idx + 1);
    });
  }, "lightbox");
})();
