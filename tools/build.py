"""Genera la web completa en site/:
   portada ES (/) y EN (/en/), y 8 páginas de servicio por idioma.
   Uso:  python tools/build.py
"""
import json
import re
import sys
from pathlib import Path
from urllib.parse import quote

sys.path.insert(0, str(Path(__file__).resolve().parent))
from PIL import Image  # noqa: E402

from svg_icons import ICONS, svg, ARROW, WA_ICON, FLAG_ES, FLAG_EN, CHECK  # noqa: E402,F401
from content_data import TERM, RESULTS, REVIEWS  # noqa: E402
from services_data import SERVICES, BOOK_URL, SHOW_PHOTO_PLACEHOLDERS, INCLUDES  # noqa: E402
from ui_text import T, S, PHONE_TXT, PHONE_INT, WA_NUM  # noqa: E402

SITE = Path(__file__).resolve().parent.parent / "site"
IMG = SITE / "assets" / "img"
DOMAIN = "https://www.sculptology.eu"
V = "20261010"  # cache busting: súbelo en cada despliegue
OTHER = {"es": "en", "en": "es"}
BOOK_ATTR = f'href="{BOOK_URL}" target="_blank" rel="noopener"'


# ------------------------------------------------------------------ utilidades
def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def page_path(lang, svc=None):
    if svc is None:
        return T[lang]["path"]
    return f"/servicios/{svc['slug']['es']}/" if lang == "es" else f"/en/services/{svc['slug']['en']}/"


def write_page(path, html):
    out = SITE / path.strip("/") / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")


def img_size(rel):
    return Image.open(IMG / rel).size


def wa_url(lang):
    return f"https://wa.me/{WA_NUM}?text={quote(T[lang]['wa_msg'])}"


def fmt_price(lang, p):
    return f"{p} €" if lang == "es" else f"€{p}"


def trim(text, limit=158):
    text = " ".join(text.split())
    if len(text) <= limit:
        return text
    return text[: limit - 1].rsplit(" ", 1)[0].rstrip(",;:. ") + "…"


def natural(path):
    return [int(x) if x.isdigit() else x for x in re.split(r"(\d+)", path.name)]


# ------------------------------------------------------------------ piezas comunes
def head(lang, title, desc, self_path, es_path, en_path, pre, ld):
    url = DOMAIN + self_path
    ld_html = "\n".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)
    return f'''<!doctype html>
<html lang="{lang}" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="theme-color" content="#14100f">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="es" href="{DOMAIN}{es_path}">
<link rel="alternate" hreflang="en" href="{DOMAIN}{en_path}">
<link rel="alternate" hreflang="x-default" href="{DOMAIN}{es_path}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Sculptology">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:locale" content="{T[lang]["locale"]}">
<meta property="og:image" content="{DOMAIN}/assets/img/treatment.webp">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/svg+xml" href="{pre}assets/img/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Jost:wght@300;400;500&family=Pinyon+Script&family=Playfair+Display:ital,wght@0,400;0,500;0,600;1,400;1,500&display=swap">
<link rel="stylesheet" href="{pre}assets/css/styles.css?v={V}">
{ld_html}
'''


def header(lang, logo_href, pfx, es_href, en_href, solid=False):
    t = T[lang]
    nav = "".join(f'<a href="{pfx}#{k}">{v}</a>' for k, v in t["nav"])
    cur = lambda l: ' aria-current="true"' if l == lang else ""  # noqa: E731
    flags = (f'<a href="{es_href}" hreflang="es" lang="es" title="Español" aria-label="Español"{cur("es")}>{FLAG_ES}</a>'
             f'<a href="{en_href}" hreflang="en" lang="en" title="English" aria-label="English"{cur("en")}>{FLAG_EN}</a>')
    return f'''<a class="skip" href="#main">{t["skip"]}</a>
<header class="header{" solid" if solid else ""}"{" data-solid" if solid else ""}>
  <div class="wrap">
    <a class="logo" href="{logo_href}" aria-label="Sculptology">Sculptology</a>
    <div class="header-right">
      <nav class="nav" id="nav" aria-label="{t["menu"]}">{nav}<a class="btn sm nav-cta" {BOOK_ATTR}>{t["book"]}</a></nav>
      <div class="lang" role="group" aria-label="Language / Idioma">{flags}</div>
      <button class="burger" type="button" aria-label="{t["menu"]}" aria-controls="nav" aria-expanded="false"><span></span></button>
    </div>
  </div>
</header>
'''


def cta_band(lang):
    t = T[lang]
    return f'''<div class="cta-band reveal">
      <h2>{t["cta_h"]}</h2>
      <p>{t["cta_p"]}</p>
      <div class="cta-actions">
        <a class="btn" {BOOK_ATTR}>{t["book"]} {ARROW}</a>
        <a class="btn ghost" href="{wa_url(lang)}" target="_blank" rel="noopener">{t["wa_ghost"]}</a>
      </div>
      <p class="cta-note">{t["appt"]}</p>
    </div>'''


def footer_and_widgets(lang, logo_href, pfx, pre):
    t = T[lang]
    nav = "".join(f'<a href="{pfx}#{k}">{v}</a>' for k, v in t["nav"])
    return f'''<footer class="footer">
  <div class="wrap">
    <div class="f-grid">
      <a class="logo" href="{logo_href}" aria-label="Sculptology">Sculptology</a>
      <nav aria-label="Footer">{nav}</nav>
    </div>
    <div class="f-bottom"><span>© 2026 Sculptology · Diana Noris · {t["f_rights"]}</span><span>{t["f_tag"]} · Málaga</span></div>
  </div>
</footer>

<a class="wa" href="{wa_url(lang)}" target="_blank" rel="noopener" aria-label="{t["wa_float"]}" title="{t["wa_float"]}">{WA_ICON}<span class="wa-pill" aria-hidden="true">{t["wa_pill"]}</span></a>

<div class="lightbox" role="dialog" aria-modal="true" aria-hidden="true">
  <button class="lb-close" type="button" aria-label="Close">×</button>
  <button class="lb-prev" type="button" aria-label="Previous">‹</button>
  <img src="" alt="">
  <button class="lb-next" type="button" aria-label="Next">›</button>
  <div class="lb-cap"></div>
</div>

<script src="{pre}assets/js/main.js?v={V}" defer></script>
</body>
</html>
'''


def tile(lang, img_rel, pre, alt, cap, label=None, after=False, extra_cls=""):
    w, h = img_size(img_rel)
    lb = ""
    if label:
        state_txt, view_txt = label
        lb = f'<span class="lb {"after" if after else ""}">{state_txt}' + (f'<span class="v"> · {view_txt}</span>' if view_txt else "") + "</span>"
    return (f'<button class="tile {extra_cls}" type="button" data-cap="{esc(cap)}" style="--ar:{w}/{h}" aria-label="{esc(alt)}">'
            f'<img src="{pre}assets/img/{img_rel}" alt="{esc(alt)}" width="{w}" height="{h}" loading="lazy" decoding="async">{lb}</button>')


def res_card(lang, res, pre, gallery=False):
    t = T[lang]
    i = 0 if lang == "es" else 1
    title, cols, tiles, treats = res
    ttl = title[i]
    html = ""
    for name in tiles:
        suf = name.split("-")[1]
        if suf in ("before", "after"):
            state, view = suf[0], None
        else:
            view, state = suf[0], suf[1]
        state_txt = t["before"] if state == "b" else t["after"]
        view_txt = {"f": t["front"], "s": t["side"], "b": t["back"]}.get(view, "")
        cap = state_txt + (f" · {view_txt}" if view_txt else "")
        html += tile(lang, f"{name}.webp", pre, f"{ttl} – {cap} – Sculptology Málaga", f"{ttl} · {cap}", (state_txt, view_txt), state == "a")
    chips = "".join(f"<span>{TERM[k][i]}</span>" for k in treats)
    g = " data-gallery" if gallery else ""
    return f'<article class="res reveal"{g}><h3>{ttl}</h3><div class="tiles c{cols}">{html}</div><div class="chips">{chips}</div></article>'


def business_ld(lang):
    return {
        "@context": "https://schema.org",
        "@type": ["HealthAndBeautyBusiness", "LocalBusiness"],
        "@id": DOMAIN + "/#business",
        "name": "Sculptology",
        "slogan": "El arte de moldear tu cuerpo · The art of sculpting your body",
        "description": T[lang]["desc"],
        "url": DOMAIN + T[lang]["path"],
        "image": DOMAIN + "/assets/img/treatment.webp",
        "address": {"@type": "PostalAddress", "streetAddress": "Calle Santa Lucía 11, Piso 1º, Puerta 7", "addressLocality": "Málaga", "addressRegion": "Andalucía", "addressCountry": "ES"},
        "areaServed": "Málaga",
        "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "11:00", "closes": "20:00"}],
        "founder": {"@type": "Person", "name": "Diana Noris", "jobTitle": "Aesthetician"},
        "knowsLanguage": ["es", "en"],
        "makesOffer": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": s["name"]["en"], "url": DOMAIN + page_path("en", s)}} for s in SERVICES],
    }


# ------------------------------------------------------------------ portada
def build_home(lang):
    t = T[lang]
    pre = "" if lang == "es" else "../"
    asset = lambda p: f"{pre}assets/{p}"  # noqa: E731
    wa = wa_url(lang)

    marquee = "".join(f"<span>{s['card'][lang]}</span>" for s in SERVICES[:6])
    badges = "".join(f"<div><strong>{a}</strong>{b}</div>" for a, b in t["badges"])
    pillars = "".join(f"<div>{svg(ic)}<b>{a}</b>{b}</div>" for ic, a, b in t["pillars"])
    about_p = "".join(f"<p>{p}</p>" for p in t["about_p"])

    svc = ""
    for n, s in enumerate(SERVICES):
        main, alt = s["card"][lang], s["card"][OTHER[lang]]
        alt_html = f'<span class="alt">{alt}</span>' if alt != main else ""
        svc += (f'<a class="svc reveal" href="{page_path(lang, s)}" style="--d:{(n % 4) * .08:.2f}s">{svg(s["icon"])}'
                f'<div><h3>{main}</h3>{alt_html}</div><span class="svc-more">{t["svc_more"]} <b aria-hidden="true">→</b></span></a>')

    res = "".join(res_card(lang, r, pre) for r in RESULTS)
    revs = ""
    for n, (name, es, en) in enumerate(REVIEWS):
        revs += f'<figure class="rev reveal" style="--d:{(n % 3) * .08:.2f}s"><div class="stars" aria-label="5/5">★★★★★</div><blockquote>{es if lang == "es" else en}</blockquote><figcaption><cite>{name}</cite></figcaption></figure>'

    head_html = head(lang, t["title"], t["desc"], t["path"], "/", "/en/", pre, [business_ld(lang)])
    html = head_html + f'''</head>
<body id="top">
''' + header(lang, "#top", "", "/", "/en/") + f'''
<main id="main">
<section class="hero">
  <div class="hero-bg" role="img" aria-label="Sculptology Málaga"></div>
  <div class="wrap">
    <div class="hero-inner">
      <p class="eyebrow">{t["eyebrow"]}</p>
      <h1>{t["h1"]}</h1>
      <p class="en-sub" lang="{OTHER[lang]}">{t["en_sub"]}</p>
      <p class="lead">{t["lead"]}</p>
      <div class="hero-cta">
        <a class="btn" {BOOK_ATTR}>{t["book"]} {ARROW}</a>
        <a class="btn ghost" href="#results">{t["see_results"]}</a>
      </div>
      <p class="hero-note">{t["hero_note"]}</p>
    </div>
  </div>
  <div class="scroll-cue" aria-hidden="true"></div>
  <div class="hero-badges"><div class="wrap">{badges}</div></div>
</section>

<div class="marquee" aria-hidden="true"><div class="marquee-track">{marquee}</div></div>

<section class="sec about" id="about">
  <div class="wrap about-grid">
    <div class="portrait reveal">
      <img src="{asset("img/diana.webp")}" alt="{t["portrait_alt"]}" width="1075" height="1520" fetchpriority="low" decoding="async">
      <div class="tag">{t["tag"][0]}<small>{t["tag"][1]}</small></div>
    </div>
    <div class="reveal" style="--d:.12s">
      <span class="kicker">{t["about_k"]}</span>
      <h2>{t["about_h"]}</h2>
      <div class="rule"></div>
      {about_p}
      <div class="signature">{t["signature"]}</div>
      <div class="pillars">{pillars}</div>
      <a class="btn" {BOOK_ATTR}>{t["book"]} {ARROW}</a>
    </div>
  </div>
</section>

<section class="sec services" id="services">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="kicker">{t["svc_k"]}</span>
      <h2>{t["svc_h"]}</h2>
      <div class="divider">{svg("lotus")}</div>
      <p>{t["svc_p"]}</p>
    </div>
    <div class="svc-grid">{svc}</div>
    <div class="svc-note reveal">
      <a class="btn" {BOOK_ATTR}>{t["book"]} {ARROW}</a>
      <p class="link-sub"><a href="{wa}" target="_blank" rel="noopener">{t["wa_link"]}</a></p>
      <p class="appt-note">{t["appt"]}</p>
    </div>
  </div>
</section>

<section class="sec results" id="results">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="kicker">{t["res_k"]}</span>
      <h2>{t["res_h"]}</h2>
      <p>{t["res_p"]}</p>
    </div>
    <div class="res-grid">{res}</div>
    <p class="disclaimer">{t["disclaimer"]}</p>
  </div>
</section>

<section class="sec reviews" id="reviews">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="kicker">{t["rev_k"]}</span>
      <h2>{t["rev_h"]}</h2>
      <p>{t["rev_p"]}</p>
      <div class="rev-score"><span class="stars" aria-hidden="true">★★★★★</span>{t["rev_badge"]}</div>
    </div>
    <div class="rev-grid">{revs}</div>
    <div class="sculpt-line reveal">{t["sculpt_line"]}<em>{t["sculpt_script"]}</em></div>
  </div>
</section>

<section class="sec contact" id="contact">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="kicker">{t["con_k"]}</span>
      <h2>{t["con_h"]}</h2>
      <p>{t["con_p"]}</p>
    </div>
    <div class="contact-grid">
      <div class="c-cards reveal">
        <div class="c-card"><span class="kicker">{t["loc"]}</span><p class="big">{t["addr"]}</p></div>
        <div class="c-card"><span class="kicker">{t["book_l"]}</span><p>{t["book_p"]}</p><a class="btn" {BOOK_ATTR}>{t["book"]} {ARROW}</a></div>
        <div class="c-card"><span class="kicker">{t["hours_l"]}</span><p><strong>{t["days"]}</strong> · <span lang="{OTHER[lang]}">{t["days_en"]}</span></p><p class="big">{t["hours"]}</p><small>{t["hours_alt"]}</small><small class="closed">{t["closed"]}</small></div>
        <div class="c-card"><span class="kicker">{t["wa_l"]}</span><p class="big"><a href="{wa}" target="_blank" rel="noopener">{t["wa_big"]}</a></p><small class="plain">{t["wa_small"]}</small></div>
      </div>
      <div class="map reveal" style="--d:.1s"><iframe title="{t["map_t"]}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q=Calle+Santa+Luc%C3%ADa+11,+M%C3%A1laga&amp;output=embed"></iframe></div>
    </div>
    {cta_band(lang)}
  </div>
</section>
</main>

''' + footer_and_widgets(lang, "#top", "", pre)
    write_page(t["path"], html)


# ------------------------------------------------------------------ páginas de servicio
def service_photos(svc):
    folder = IMG / "servicios" / svc["slug"]["es"]
    fotos = sorted(folder.glob("foto-*.webp"), key=natural) if folder.exists() else []
    pairs = []
    if folder.exists():
        for a in sorted(folder.glob("antes-*.webp"), key=natural):
            n = a.stem.split("-")[1]
            d = folder / f"despues-{n}.webp"
            if d.exists():
                pairs.append((a, d))
    return fotos, pairs


def _paras(items):
    return "".join(f"<p>{p}</p>" for p in items)


def video_html(lang, svc):
    v = svc.get("video")
    if not v:
        return ""
    cap = v["caption"][lang]
    base = "/assets/video/"
    return (f'<section class="sp"><div class="wrap narrow"><figure class="video">'
            f'<video controls muted loop playsinline preload="metadata" poster="{base}{v["poster"]}" aria-label="{esc(cap)}" data-autoplay>'
            f'<source src="{base}{v["file"]}" type="video/mp4">{esc(cap)}</video>'
            f'<figcaption>{cap}</figcaption></figure></div></section>')


def story_html(lang, svc):
    """Texto en primera persona de Diana (si el servicio lo tiene). Sustituye a la lista genérica de beneficios."""
    st, u = svc["story"], S[lang]
    intro = (f'<section class="sp alt story"><div class="wrap narrow"><span class="kicker">{st["kicker"][lang]}</span>'
             f'<h2>{st["title"][lang]}</h2><p class="story-sub">{st["subtitle"][lang]}</p>{_paras(st["intro"][lang])}</div></section>')
    li = "".join(f"<li>{CHECK}<span>{b}</span></li>" for b in st["benefits"][lang])
    benefits = (f'<section class="sp alt story"><div class="wrap narrow"><h2>{st["benefits_title"][lang]}</h2>'
                f'<p>{st["benefits_intro"][lang]}</p><ul class="checks">{li}</ul><p class="disclaimer left">{u["may_vary"]}</p></div></section>')
    secs = ""
    for n, sec in enumerate(st["sections"]):
        body = _paras(sec["paras"][lang])
        if "pull" in sec:
            body += f'<p>{sec["pull_intro"][lang]}</p><blockquote class="pull">{sec["pull"][lang]}</blockquote>'
        body += _paras(sec.get("after", {}).get(lang, []))
        secs += f'<section class="sp{" alt" if n % 2 else ""} story"><div class="wrap narrow"><h2>{sec["title"][lang]}</h2>{body}</div></section>'
    c = st["closing"]
    closing = (f'<section class="sp story-end"><div class="wrap narrow"><h2>{c["title"][lang]}</h2>{_paras(c["paras"][lang])}'
               f'<p class="sig">{c["signature"][lang]}</p><p class="sig-sub">{c["signature_sub"][lang]}</p></div></section>')
    return intro, video_html(lang, svc), benefits, secs + closing


def build_service(lang, svc):
    t, u = T[lang], S[lang]
    pre = "/"
    other = OTHER[lang]
    home = "/" if lang == "es" else "/en/"
    name, name_alt = svc["name"][lang], svc["name"][other]
    path = page_path(lang, svc)
    es_path, en_path = page_path("es", svc), page_path("en", svc)
    url = DOMAIN + path
    wa = wa_url(lang)
    tag = svc["tagline"][lang]
    gal = svc["slug"]["es"]

    title = u["title"].format(name=name)
    lead_in = f"{name} en Málaga. " if lang == "es" else f"{name} in Málaga. "
    desc = trim(svc["meta"][lang]) if svc.get("meta") else trim(lead_in + svc["intro"][lang])

    price_offers = [{"@type": "Offer", "name": p[lang], "price": str(p["price"]), "priceCurrency": "EUR"} for p in svc["prices"]]
    ld_service = {
        "@context": "https://schema.org", "@type": "Service", "name": name, "description": svc["intro"][lang],
        "serviceType": name, "url": url, "inLanguage": lang,
        "provider": {"@type": "HealthAndBeautyBusiness", "@id": DOMAIN + "/#business", "name": "Sculptology"},
        "areaServed": {"@type": "City", "name": "Málaga"},
    }
    if price_offers:
        ld_service["offers"] = price_offers
    ld_bc = {
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": u["home"], "item": DOMAIN + home},
            {"@type": "ListItem", "position": 2, "name": u["services"], "item": DOMAIN + home + "#services"},
            {"@type": "ListItem", "position": 3, "name": name, "item": url},
        ],
    }

    sub = f'<p class="en-sub" lang="{other}">{name_alt}</p>' if name_alt != name else ""
    benefits = "".join(f"<li>{CHECK}<span>{b}</span></li>" for b in svc["benefits"][lang])
    if svc.get("story"):
        s_intro, s_video, s_benefits, s_rest = story_html(lang, svc)
        story_block = s_intro + s_video + s_benefits + s_rest
    else:
        story_block = (f'<section class="sp alt"><div class="wrap narrow"><h2>{u["benefits"]}</h2><ul class="checks">{benefits}</ul>'
                       f'<p class="disclaimer left">{u["may_vary"]}</p></div></section>')
    steps = "".join(f'<li><span class="n" aria-hidden="true">{n}</span><span>{s}</span></li>' for n, s in enumerate(svc["steps"][lang], 1))
    notes = "".join(f'<div class="note"><b>{n["title"][lang]}</b><p>{n["body"][lang]}</p></div>' for n in svc["notes"])

    if svc["prices"]:
        cards = "".join(f'<div class="price"><span class="price-l">{p[lang]}</span><span class="price-v">{fmt_price(lang, p["price"])}</span></div>' for p in svc["prices"])
    else:
        cards = f'<div class="price tbc"><span class="price-v">{u["price_tbc"]}</span></div>'  # TODO Diana: precio a confirmar
    prices_html = f'''<section class="sp alt" id="prices"><div class="wrap narrow">
      <h2>{u["prices"]}</h2>
      <div class="price-grid">{cards}</div>
      <div class="sp-cta"><a class="btn" {BOOK_ATTR}>{t["book"]} {ARROW}</a><p class="appt-note">{t["appt"]}</p></div>
    </div></section>'''

    includes_html = ""
    if svc["incluye_square"]:
        li = "".join(f"<li>{CHECK}<span>{x}</span></li>" for x in INCLUDES[lang])
        includes_html = f'<section class="sp"><div class="wrap narrow"><h2>{u["includes"]}</h2><ul class="checks">{li}</ul></div></section>'

    fotos, pairs = service_photos(svc)
    photos_html = ""
    if fotos:
        tiles = "".join(tile(lang, f"servicios/{gal}/{p.name}", pre, f"{name} – Sculptology Málaga", name) for p in fotos)
        photos_html = f'<section class="sp"><div class="wrap"><h2>{u["photos"]}</h2><div class="photo-grid" data-gallery>{tiles}</div></div></section>'

    ba_html, ba_note = "", ""
    if pairs:
        for a, d in pairs:
            ts = (tile(lang, f"servicios/{gal}/{a.name}", pre, f"{name} – {t['before']} – Sculptology Málaga", f"{name} · {t['before']}", (t["before"], ""), False)
                  + tile(lang, f"servicios/{gal}/{d.name}", pre, f"{name} – {t['after']} – Sculptology Málaga", f"{name} · {t['after']}", (t["after"], ""), True))
            ba_html += f'<article class="res" data-gallery><div class="tiles c2">{ts}</div></article>'
        ba_note = u["may_vary"]
    elif svc["key"]:
        matches = [r for r in RESULTS if svc["key"] in r[3]][:3]
        ba_html = "".join(res_card(lang, r, pre, gallery=True) for r in matches)
        ba_note = u["combined"].format(name=name)
    ba_section = ""
    if ba_html:
        ba_section = f'<section class="sp alt"><div class="wrap"><h2>{u["ba"]}</h2><div class="ba-grid">{ba_html}</div><p class="disclaimer">{ba_note}</p></div></section>'
    placeholder = ""
    if not fotos and not ba_html and SHOW_PHOTO_PLACEHOLDERS:
        placeholder = f'<section class="sp"><div class="wrap narrow"><div class="soon">{svg(svc["icon"])}<p>{u["soon"]}</p></div></div></section>'

    faq = "".join(f'<details class="faq"><summary>{q}</summary><p>{a}</p></details>' for q, a in svc["faq"][lang])
    consult = "".join(f"<li>{x}</li>" for x in svc["consult"][lang])

    review_html = ""
    if svc.get("featured_review"):
        for rn, r_es, r_en in REVIEWS:
            if rn == svc["featured_review"]:
                txt = r_es if lang == "es" else r_en
                review_html = (f'<section class="sp reviews one"><div class="wrap narrow"><span class="kicker">{u["review"]}</span>'
                               f'<figure class="rev"><div class="stars" aria-label="5/5">★★★★★</div><blockquote>{txt}</blockquote><figcaption><cite>{rn}</cite></figcaption></figure></div></section>')

    others = "".join(f'<a class="mini" href="{page_path(lang, o)}">{svg(o["icon"])}<span>{o["card"][lang]}</span></a>' for o in SERVICES if o is not svc)
    faq_cls = "sp" if review_html else "sp alt"

    ld_all = [ld_service, ld_bc]
    if svc.get("video"):
        v = svc["video"]
        ld_all.append({"@context": "https://schema.org", "@type": "VideoObject", "name": v["caption"][lang], "description": v["desc"][lang],
                       "thumbnailUrl": f"{DOMAIN}/assets/video/{v['poster']}", "contentUrl": f"{DOMAIN}/assets/video/{v['file']}",
                       "uploadDate": v["uploaded"], "duration": v["duration"], "inLanguage": lang})
    head_html = head(lang, title, desc, path, es_path, en_path, pre, ld_all)
    html = head_html + f'''</head>
<body id="top">
''' + header(lang, home, home, es_path, en_path, solid=True) + f'''
<main id="main">
<section class="s-hero">
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><ol>
      <li><a href="{home}">{u["home"]}</a></li><li><a href="{home}#services">{u["services"]}</a></li><li aria-current="page">{name}</li>
    </ol></nav>
    <div class="s-hero-grid">
      <div class="s-icon" aria-hidden="true">{svg(svc["icon"])}</div>
      <div>
        <span class="kicker">{u["kicker"]}</span>
        <h1>{name}</h1>
        {sub}
        <p class="lead">{tag}</p>
        <div class="hero-cta">
          <a class="btn" {BOOK_ATTR}>{t["book"]} {ARROW}</a>
          <a class="btn dark-ghost" href="{wa}" target="_blank" rel="noopener">{t["wa_ghost"]}</a>
        </div>
        <p class="appt-note">{t["appt"]}</p>
      </div>
    </div>
  </div>
</section>

<section class="sp"><div class="wrap narrow">
  <h2>{u["what"]}</h2>
  <p class="intro">{svc["intro"][lang]}</p>
</div></section>

{story_block}

<section class="sp"><div class="wrap narrow">
  <h2>{u["session"]}</h2>
  <ol class="steps">{steps}</ol>
  {notes}
</div></section>

{prices_html}
{includes_html}
{photos_html}
{ba_section}
{placeholder}
{review_html}

<section class="{faq_cls}"><div class="wrap narrow">
  <h2>{u["faq"]}</h2>
  <div class="faq-list">{faq}</div>
</div></section>

<section class="sp"><div class="wrap narrow">
  <h2>{u["consult"]}</h2>
  <ul class="dots">{consult}</ul>
  <p class="med">{u["med"]}</p>
  <div class="sp-cta"><a class="btn" {BOOK_ATTR}>{t["book"]} {ARROW}</a><p class="appt-note">{t["appt"]}</p></div>
</div></section>

<section class="sp alt"><div class="wrap">
  <h2>{u["others"]}</h2>
  <div class="mini-grid">{others}</div>
</div></section>

<section class="sec contact"><div class="wrap">{cta_band(lang)}</div></section>
</main>

''' + footer_and_widgets(lang, home, home, pre)
    write_page(path, html)


# ------------------------------------------------------------------ archivos de apoyo
def write_support():
    (IMG / "favicon.svg").write_text(
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#14100f"/><rect x="8" y="8" width="48" height="48" fill="none" stroke="#b85a69" stroke-width="3"/><text x="32" y="43" font-family="Georgia,serif" font-size="32" fill="#fff" text-anchor="middle">S</text></svg>', encoding="utf-8")
    (SITE / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n", encoding="utf-8")

    def entry(es_p, en_p, own):
        return (f"  <url><loc>{DOMAIN}{own}</loc>\n"
                f'    <xhtml:link rel="alternate" hreflang="es" href="{DOMAIN}{es_p}"/>\n'
                f'    <xhtml:link rel="alternate" hreflang="en" href="{DOMAIN}{en_p}"/>\n'
                f'    <xhtml:link rel="alternate" hreflang="x-default" href="{DOMAIN}{es_p}"/></url>\n')

    body = entry("/", "/en/", "/") + entry("/", "/en/", "/en/")
    for s in SERVICES:
        e, n = page_path("es", s), page_path("en", s)
        body += entry(e, n, e) + entry(e, n, n)
    (SITE / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + body + "</urlset>\n",
        encoding="utf-8")


if __name__ == "__main__":
    for l in ("es", "en"):
        build_home(l)
        for s in SERVICES:
            build_service(l, s)
    write_support()
    print(f"built: 2 home + {2 * len(SERVICES)} service pages")
