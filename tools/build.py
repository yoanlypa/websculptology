"""Genera site/index.html (ES) y site/en/index.html (EN) con todo el contenido ya renderizado (mejor para SEO)."""
import json
from pathlib import Path
from urllib.parse import quote
from PIL import Image

SITE = Path(r"D:\webSculptology\site")
IMG = SITE / "assets" / "img"
DOMAIN = "https://www.sculptology.eu"
V = "20261009"
PHONE_TXT, PHONE_INT = "+34 657 780 333", "+34657780333"
WA_NUM = "34657780333"

# ----------------------------------------------------------------- textos UI
T = {
 "es": {
  "lang": "es", "locale": "es_ES", "path": "/", "other": "/en/",
  "title": "Sculptology Málaga | Maderoterapia, Fascia Blasting y Drenaje Linfático",
  "desc": "Estudio de estética y bienestar en Málaga Centro: maderoterapia, Fascia Blasting, cavitación, radiofrecuencia y drenaje linfático. Atención VIP en español e inglés.",
  "skip": "Saltar al contenido",
  "nav": [("about", "Sobre mí"), ("services", "Servicios"), ("results", "Resultados"), ("reviews", "Opiniones"), ("contact", "Contacto")],
  "book": "Reserva tu cita", "wa_msg": "Hola, me gustaría reservar una cita en Sculptology.",
  "eyebrow": "Málaga Centro · Estudio de estética y bienestar",
  "h1": "El arte de <em>moldear</em> tu cuerpo", "en_sub": "The art of sculpting your body",
  "lead": "Maderoterapia, Fascia Blasting, cavitación, radiofrecuencia y drenaje linfático con atención VIP, tiempo y un plan pensado para ti. Atención en español e inglés.",
  "see_results": "Ver resultados",
  "badges": [("20+", "Años de experiencia"), ("EE. UU.", "Formación profesional"), ("ES · EN", "Completamente bilingüe"), ("VIP", "Atención personalizada")],
  "about_k": "Sobre Sculptology", "about_h": "Más que estética, es bienestar <em>real.</em>",
  "about_p": [
   "Soy <strong>Diana Noris</strong>, fundadora de Sculptology. Soy esteticista profesional formada en los Estados Unidos, con más de 20 años de experiencia en la industria de la estética y el bienestar. Me especializo en maderoterapia, Fascia Blasting, cavitación, radiofrecuencia, drenaje linfático, masajes postoperatorios y eye therapy. En mi estudio en Málaga ofrezco una experiencia personalizada, exclusiva y de alto nivel, donde cada clienta recibe atención VIP, tiempo, dedicación y un plan pensado para lograr los mejores resultados posibles.",
   "Soy completamente bilingüe en inglés y español. Mi prioridad es que te sientas cómoda, cuidada y 100% satisfecha con tu tratamiento. Tengo numerosas reseñas de cinco estrellas y trabajo para ayudarte a alcanzar tus objetivos corporales con resultados visibles y reales.",
  ],
  "signature": "Tu cuerpo, en las mejores manos.",
  "pillars": [("lotus", "20+ años", "de experiencia"), ("cap", "Formación", "en Estados Unidos"), ("chat", "Bilingüe", "Español & English"), ("gem", "Atención", "VIP")],
  "tag": ("Diana Noris", "Fundadora"),
  "portrait_alt": "Diana Noris, fundadora de Sculptology, esteticista profesional en Málaga",
  "svc_k": "Servicios", "svc_h": "Tratamientos de <em>contorno corporal</em> y bienestar",
  "svc_p": "Cada plan se diseña según tu cuerpo y tus objetivos, en un estudio privado en el centro de Málaga.",
  "svc_cta": "Pide información por WhatsApp",
  "res_k": "Resultados reales", "res_h": "Antes y <em>después</em>",
  "res_p": "Fotos reales de clientes de Sculptology y del estudio anterior de Diana. Toca una foto para ampliarla.",
  "disclaimer": "Los resultados pueden variar de una persona a otra.",
  "rev_k": "Opiniones de clientes", "rev_h": "Lo que dicen <em>nuestras clientas</em>",
  "rev_p": "Opiniones reales de 5 estrellas de clientes del anterior estudio de Diana en EE. UU.",
  "rev_badge": "5.0 · 13 opiniones de 5 estrellas",
  "sculpt_line": "Esculpe • Tonifica • Drena • Siéntete tu mejor versión", "sculpt_script": "El arte de moldear tu cuerpo.",
  "con_k": "Contacto", "con_h": "Ven a <em>conocernos</em>",
  "con_p": "Estudio privado en el centro de Málaga. Atención en español e inglés.",
  "loc": "Ubicación · Location", "addr": "Calle Santa Lucía 11 · Málaga Centro<br>Piso 1º · Puerta 7",
  "wa_l": "WhatsApp / Tel.", "hours_l": "Horario · Hours", "days": "Lunes a domingo", "days_en": "Monday to Sunday",
  "hours": "10:00–21:00", "hours_alt": "10:00 AM – 9:00 PM",
  "cta_h": "Tu mejor versión empieza aquí", "cta_p": "Escríbenos por WhatsApp y reserva tu cita. Te respondemos en español o inglés.",
  "map_t": "Mapa: Sculptology, Calle Santa Lucía 11, Málaga",
  "f_rights": "Todos los derechos reservados.", "f_tag": "El arte de moldear tu cuerpo",
  "before": "Antes", "after": "Después", "front": "Frontal", "side": "Lateral", "back": "Posterior",
  "wa_aria": "Escribir por WhatsApp", "menu": "Menú", "lang_es": "Español", "lang_en": "English",
 },
 "en": {
  "lang": "en", "locale": "en_GB", "path": "/en/", "other": "/",
  "title": "Sculptology Málaga | Wood Therapy, Fascia Blasting & Lymphatic Drainage",
  "desc": "Body contouring and wellness studio in central Málaga: wood therapy, Fascia Blasting, cavitation, radiofrequency and lymphatic drainage. VIP care in English and Spanish.",
  "skip": "Skip to content",
  "nav": [("about", "About"), ("services", "Services"), ("results", "Results"), ("reviews", "Reviews"), ("contact", "Contact")],
  "book": "Book now", "wa_msg": "Hi, I'd like to book an appointment at Sculptology.",
  "eyebrow": "Central Málaga · Aesthetics & wellness studio",
  "h1": "The art of <em>sculpting</em> your body", "en_sub": "El arte de moldear tu cuerpo",
  "lead": "Wood therapy, Fascia Blasting, cavitation, radiofrequency and lymphatic drainage with VIP attention, time and a plan made for you. Services in English and Spanish.",
  "see_results": "See results",
  "badges": [("20+", "Years of experience"), ("USA", "Professional training"), ("EN · ES", "Fully bilingual"), ("VIP", "Personalised care")],
  "about_k": "About Sculptology", "about_h": "More than aesthetics, it's <em>real</em> wellbeing.",
  "about_p": [
   "I'm <strong>Diana Noris</strong>, founder of Sculptology. I'm a professional aesthetician trained in the United States, with more than 20 years of experience in the aesthetics and wellness industry. I specialise in wood therapy, Fascia Blasting, cavitation, radiofrequency, lymphatic drainage, post-operative massage and eye therapy. In my Málaga studio I offer a personalised, exclusive, high-end experience where every client receives VIP attention, time, dedication and a plan designed to achieve the best possible results.",
   "I'm completely bilingual in English and Spanish. My priority is that you feel comfortable, cared for and 100% satisfied with your treatment. I have numerous five-star reviews and I work to help you reach your body goals with visible, real results.",
  ],
  "signature": "Your body, in the best hands.",
  "pillars": [("lotus", "20+ years", "of experience"), ("cap", "Training", "in the United States"), ("chat", "Bilingual", "English & Español"), ("gem", "VIP", "care")],
  "tag": ("Diana Noris", "Founder"),
  "portrait_alt": "Diana Noris, founder of Sculptology, professional aesthetician in Málaga",
  "svc_k": "Services", "svc_h": "<em>Body contouring</em> and wellness treatments",
  "svc_p": "Every plan is designed around your body and your goals, in a private studio in the centre of Málaga.",
  "svc_cta": "Ask us on WhatsApp",
  "res_k": "Real results", "res_h": "Before & <em>after</em>",
  "res_p": "Real photos of Sculptology clients and of Diana's previous studio. Tap a photo to enlarge it.",
  "disclaimer": "Results may vary from person to person.",
  "rev_k": "Client reviews", "rev_h": "What <em>our clients</em> say",
  "rev_p": "Real 5-star feedback from Diana's previous U.S. studio.",
  "rev_badge": "5.0 · 13 five-star reviews",
  "sculpt_line": "Sculpt • Tone • Drain • Feel your best", "sculpt_script": "El arte de moldear tu cuerpo.",
  "con_k": "Contact", "con_h": "Come and <em>meet us</em>",
  "con_p": "Private studio in the centre of Málaga. Services in English and Spanish.",
  "loc": "Location · Ubicación", "addr": "Calle Santa Lucía 11 · Málaga Centro<br>1st floor · Door 7",
  "wa_l": "WhatsApp / Tel.", "hours_l": "Hours · Horario", "days": "Monday to Sunday", "days_en": "Lunes a domingo",
  "hours": "10:00 AM – 9:00 PM", "hours_alt": "10:00–21:00",
  "cta_h": "Your best self starts here", "cta_p": "Message us on WhatsApp and book your appointment. We reply in English or Spanish.",
  "map_t": "Map: Sculptology, Calle Santa Lucía 11, Málaga",
  "f_rights": "All rights reserved.", "f_tag": "The art of sculpting your body",
  "before": "Before", "after": "After", "front": "Front", "side": "Side", "back": "Back",
  "wa_aria": "Message us on WhatsApp", "menu": "Menu", "lang_es": "Español", "lang_en": "English",
 },
}

# ----------------------------------------------------------------- servicios
SERVICES = [  # icono, es, en
 ("wood", "Maderoterapia", "Wood Therapy"),
 ("fascia", "Fascia Blasting", "Fascia Blasting"),
 ("cav", "Cavitación", "Cavitation"),
 ("rf", "Radiofrecuencia", "Radiofrequency"),
 ("lymph", "Drenaje Linfático", "Lymphatic Drainage"),
 ("lotus", "Masajes Postoperatorios", "Post-Op Massages"),
 ("massage", "Masaje Relajante Terapéutico de Cuerpo Completo", "Full Body Relaxation Therapeutic Massage"),
]
ICONS = {
 "wood": '<path d="M22 6C14 20 14 36 24 54M42 6c8 14 8 30-2 48M26 38l6 8 6-8"/><path d="M3 28h12m-4-4 4 4-4 4M61 28H49m4-4-4 4 4 4"/>',
 "fascia": '<path d="M10 54l14-14M40 24 54 10"/><circle cx="32" cy="32" r="7"/><circle cx="24" cy="40" r="5"/><circle cx="40" cy="24" r="5"/><path d="M6 36l-2 6M12 32l-3 5"/>',
 "cav": '<path d="M21 6C13 20 15 34 24 40l8 9 8-9c9-6 11-20 3-34"/><path d="M26 18v8M38 18v8" stroke-dasharray="3 3"/><path d="M3 24h11m-4-4 4 4-4 4M61 24H50m4-4-4 4 4 4"/>',
 "rf": '<circle cx="32" cy="32" r="4"/><path d="M24 24a12 12 0 0 0 0 16M40 24a12 12 0 0 1 0 16M17 17a22 22 0 0 0 0 30M47 17a22 22 0 0 1 0 30M10 10a32 32 0 0 0 0 44M54 10a32 32 0 0 1 0 44"/>',
 "lymph": '<path d="M22 6C12 20 10 28 10 36a12 12 0 0 0 24 0c0-8-2-16-12-30z"/><path d="M42 10c6 7 8 13 8 18"/><path d="M38 38c10 0 16 6 16 16-10 0-16-6-16-16z"/><path d="M16 38a6 6 0 0 0 5 6"/>',
 "lotus": '<path d="M32 54C18 52 8 42 6 28c10 0 20 6 26 16 6-10 16-16 26-16-2 14-12 24-26 26z"/><path d="M32 54C24 44 22 28 32 8c10 20 8 36 0 46z"/>',
 "massage": '<circle cx="14" cy="26" r="7"/><path d="M5 44c10-6 18-4 26-2s18 2 27-6M5 54c10-6 20-4 28-2s16 2 25-4M24 34c10 0 16 4 26 2"/><path d="M44 10c4 0 8 2 8 8-6 0-8-4-8-8z"/>',
 "cap": '<path d="M32 12 4 26l28 14 28-14z"/><path d="M16 33v12c0 4 8 8 16 8s16-4 16-8V33M60 26v16"/>',
 "chat": '<path d="M24 8C13 8 6 15 6 24c0 4 2 8 5 11l-2 9 9-4c2 .6 4 1 6 1 11 0 18-7 18-16S35 8 24 8z"/><path d="M44 22c9 1 14 7 14 14 0 4-2 7-5 10l1 8-8-4c-2 .5-3 .7-5 .7-6 0-11-3-13-8"/>',
 "gem": '<path d="M16 8h32l12 14-28 34L4 22z"/><path d="M4 22h56M24 22 32 56l8-34M24 22l-8-14M40 22l8-14M24 22l8-14 8 14"/>',
}

def svg(name, extra=""):
    return f'<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" {extra}>{ICONS[name]}</svg>'

ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 12h16m-6-6 6 6-6 6"/></svg>'
WA_ICON = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M17.47 14.38c-.3-.15-1.76-.87-2.03-.97-.27-.1-.47-.15-.67.15-.2.3-.77.97-.94 1.16-.17.2-.35.22-.65.07-.3-.15-1.26-.46-2.39-1.48-.88-.79-1.48-1.76-1.65-2.06-.17-.3-.02-.46.13-.6.13-.14.3-.35.45-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.03-.52-.07-.15-.67-1.61-.92-2.21-.24-.58-.49-.5-.67-.51h-.57c-.2 0-.52.07-.79.37-.27.3-1.04 1.02-1.04 2.48s1.07 2.88 1.21 3.07c.15.2 2.1 3.2 5.08 4.49.71.3 1.26.49 1.69.63.71.23 1.36.2 1.87.12.57-.08 1.76-.72 2-1.41.25-.7.25-1.29.17-1.41-.07-.12-.27-.2-.57-.35m-5.42 7.4h-.01a9.87 9.87 0 0 1-5.03-1.38l-.36-.21-3.74.98 1-3.65-.24-.37a9.86 9.86 0 0 1-1.51-5.26c0-5.45 4.44-9.88 9.89-9.88 2.64 0 5.12 1.03 6.99 2.9a9.82 9.82 0 0 1 2.89 6.99c0 5.45-4.44 9.89-9.88 9.89m8.41-18.3A11.8 11.8 0 0 0 12.05 0C5.5 0 .16 5.34.16 11.89c0 2.1.55 4.14 1.59 5.95L.06 24l6.3-1.65a11.9 11.9 0 0 0 5.69 1.45h.01c6.55 0 11.89-5.34 11.89-11.89 0-3.18-1.24-6.17-3.48-8.41z"/></svg>'
FLAG_ES = '<svg viewBox="0 0 60 60" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><rect width="60" height="60" fill="#c60b1e"/><rect y="15" width="60" height="30" fill="#ffc400"/></svg>'
FLAG_EN = '<svg viewBox="0 0 60 60" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><rect width="60" height="60" fill="#012169"/><path d="M0 0 60 60M60 0 0 60" stroke="#fff" stroke-width="11"/><path d="M0 0 60 60M60 0 0 60" stroke="#c8102e" stroke-width="4"/><path d="M30 0v60M0 30h60" stroke="#fff" stroke-width="18"/><path d="M30 0v60M0 30h60" stroke="#c8102e" stroke-width="10"/></svg>'

# ----------------------------------------------------------------- tratamientos (términos)
TERM = {
 "vib": ("Plataforma vibratoria", "Vibration plate"), "lymph": ("Drenaje linfático", "Lymphatic drainage"),
 "wood": ("Maderoterapia", "Wood therapy"), "fascia": ("Fascia Blast", "Fascia Blast"), "cav": ("Cavitación", "Cavitation"),
 "rf": ("Radiofrecuencia", "Radiofrequency"), "sauna": ("Sauna", "Sauna"), "lipo": ("Lipo láser", "Lipo laser"),
 "ice": ("Ice Sculpting", "Ice Sculpting"), "metal": ("Maderoterapia metálica", "Metal therapy"),
 "vlift": ("Vacuum Lift", "Vacuum Lift"), "bl": ("Vacuum Butt Lift", "Vacuum Butt Lift"),
 "cup": ("Ventosas al vacío", "Vacuum cupping"), "tread": ("Cinta de correr", "Treadmill"),
 "usrf": ("Ultrasonido RF", "RF ultrasound"),
}

# titulo (es, en), columnas, tiles, tratamientos
RESULTS = [
 (("Después de 12 sesiones", "After 12 sessions"), 2, ["r12-before", "r12-after"], ["sauna", "fascia", "cav", "rf", "lipo", "ice", "metal"]),
 (("Después de 1 tratamiento", "After 1 treatment"), 2, ["r1g-fb", "r1g-sb", "r1g-fa", "r1g-sa"], ["vib", "lymph", "fascia", "wood", "metal", "cav", "rf", "lipo"]),
 (("Super Meltdown Session", "Super Meltdown Session"), 2, ["sm-fb", "sm-fa", "sm-sb", "sm-sa"], ["tread", "vib", "sauna", "fascia", "wood", "cav", "rf", "lipo"]),
 (("Después de 5 sesiones", "After 5 sessions"), 2, ["r5-fb", "r5-fa", "r5-sb", "r5-sa", "r5-bb", "r5-ba"], ["vib", "lymph", "fascia", "cup", "metal", "cav", "rf", "usrf", "lipo"]),
 (("The Meltdown Session", "The Meltdown Session"), 2, ["melt-before", "melt-after"], ["sauna", "fascia", "cav", "rf", "ice", "lipo", "bl"]),
 (("Después de 4 tratamientos", "After 4 treatments"), 2, ["r4-fb", "r4-sb", "r4-fa", "r4-sa"], ["vib", "lymph", "wood", "fascia", "cav", "rf", "vlift", "cup"]),
 (("Después de 6 tratamientos", "After 6 treatments"), 2, ["r6-before", "r6-after"], ["vib", "lymph", "wood", "fascia", "cav", "rf", "vlift", "cup"]),
 (("Resultados reales", "Real results"), 3, ["rr-fb", "rr-sb", "rr-bb", "rr-fa", "rr-sa", "rr-ba"], ["vib", "fascia", "lymph", "cav", "rf", "lipo", "bl"]),
 (("Después de 3 tratamientos", "After 3 treatments"), 2, ["r3-fb", "r3-sb", "r3-fa", "r3-sa"], ["vib", "lymph", "wood", "fascia", "cav", "rf", "vlift", "cup"]),
 (("Después de 2 tratamientos", "After 2 treatments"), 2, ["r2-fb", "r2-sb", "r2-fa", "r2-sa"], ["vib", "lymph", "wood", "fascia", "cav", "rf"]),
 (("Después de 1 tratamiento", "After 1 treatment"), 2, ["r1w-sb", "r1w-fb", "r1w-sa", "r1w-fa"], ["fascia", "cav", "rf", "ice"]),
]

# ----------------------------------------------------------------- opiniones (es, en)
REVIEWS = [
 ("M T", "No puedo hablar lo suficiente de Diana. Su experiencia y compromiso se notan en cada sesión. Recomiendo Sculpt by Noris con todo mi corazón.",
         "I cannot speak highly enough of Diana. Her expertise and commitment are evident in every session. I wholeheartedly recommend Sculpt by Noris!"),
 ("Liz Estefania Correa", "Después de mi cirugía luchaba con la fibrosis, y sus masajes han hecho una gran diferencia. Personaliza cada sesión según lo que mi cuerpo necesita y realmente quiere ayudar.",
         "After my surgery I struggled with fibrosis, and her massages have made a huge difference. She customizes each session and truly wants to help."),
 ("Natasha Marquez", "Desde el momento en que entré, me sentí bienvenida y bien cuidada. Diana es una profesional increíble y ofrece resultados impresionantes.",
         "From the moment I walked in, I felt welcomed and cared for. Diana is an absolute professional and delivers amazing results."),
 ("DL Smith", "Compré el paquete Super Meltdown y estoy más que feliz con mis resultados. He perdido más de 4 pulgadas y gran parte de mi celulitis ha desaparecido.",
         "I purchased the Super Meltdown Package and am beyond thrilled with my results! I've lost over 4 inches and a lot of my cellulite has disappeared."),
 ("John Mosby", "Hice el paquete Super Meltdown, 8 sesiones, y bajé al menos 3 pulgadas. Me veo más delgado, más firme y la grasa rebelde finalmente se fue.",
         "I did the Super Meltdown Package, 8 sessions, and dropped at least 3 inches. I look leaner, tighter, and the stubborn fat is finally gone."),
 ("Fran Militao", "He tenido una experiencia increíble con Diana. Sus métodos de contorno corporal realmente funcionan; he visto resultados reales y visibles que superaron mis expectativas.",
         "I've had an amazing experience with Diana. Her body contouring methods truly work — I've seen real, visible results that exceeded my expectations."),
 ("David Sharpe", "Siendo hombre, no me sentía cómodo hablando de mi cuerpo. Diana me ha ayudado mucho con las áreas que me inseguraban. He perdido aproximadamente 3 pulgadas de mi abdomen.",
         "Being a man, I'm not comfortable talking about my body. Diana has helped greatly with the areas I was insecure about. I've lost about 3 inches from my belly."),
 ("Gage", "He tenido algunas sesiones y ya me siento más tonificado. Ella es muy profesional y explica cada parte del procedimiento.",
         "I've had a few sessions and already feel more toned. She is knowledgeable and explains every part of the procedure."),
 ("Jessica Saiontz", "Estudio privado y muy cómodo. Compré un paquete de 8 visitas y perdí una pulgada después del primer tratamiento. ¡Lo recomiendo mucho!",
         "Private studio and very comfortable. I bought a package for 8 visits and lost an inch after the first treatment! Highly recommend!"),
 ("Valeria Santana", "Experiencia increíble. Diana realmente encuentra la manera de conectar y personalizar sus servicios para cada cliente. He visto muchos cambios en mi cuerpo gracias a ella.",
         "Amazing experience. Diana really finds a way to connect and tailor her services to the client! I have seen so many changes in my body thanks to her."),
 ("Samantha Olivas", "¡Body by Noris es increíble! He perdido 4 pulgadas alrededor de mi estómago desde que empecé con ella. ¡La recomiendo mucho!",
         "Body by Noris is amazing!! I've lost 4 inches around my stomach since seeing her! Highly recommend."),
 ("Heather Susan Carr", "Qué experiencia tan increíble con Sculpt by Noris. Recomiendo sus servicios para obtener resultados fabulosos en tu cuerpo.",
         "What an amazing experience with Sculpt by Noris. I recommend her services for fabulous results on your body."),
 ("Rachael Olivas", "¡Maravillosa experiencia y realmente funciona! ¡Pierdo al menos una pulgada cada vez que voy!",
         "Wonderful experience and it works! I lose at least an inch every time I go!"),
]

def ratio(name):
    w, h = Image.open(IMG / f"{name}.webp").size
    return w, h

def build(lang):
    t = T[lang]; i = 0 if lang == "es" else 1
    pre = "" if lang == "es" else "../"
    asset = lambda p: f"{pre}assets/{p}"
    url = DOMAIN + t["path"]
    wa = f"https://wa.me/{WA_NUM}?text={quote(t['wa_msg'])}"

    nav = "".join(f'<a href="#{k}">{v}</a>' for k, v in t["nav"])
    flags = (
        f'<a href="/" hreflang="es" lang="es" title="Español" aria-label="Español"{" aria-current=\"true\"" if lang=="es" else ""}>{FLAG_ES}</a>'
        f'<a href="/en/" hreflang="en" lang="en" title="English" aria-label="English"{" aria-current=\"true\"" if lang=="en" else ""}>{FLAG_EN}</a>'
    )
    marquee = "".join(f"<span>{s[1+i]}</span>" for s in SERVICES[:6])

    badges = "".join(f"<div><strong>{a}</strong>{b}</div>" for a, b in t["badges"])
    pillars = "".join(f'<div>{svg(ic)}<b>{a}</b>{b}</div>' for ic, a, b in t["pillars"])
    about_p = "".join(f"<p>{p}</p>" for p in t["about_p"])

    svc = ""
    for n, (ic, es, en) in enumerate(SERVICES):
        main, alt = (es, en) if lang == "es" else (en, es)
        wide = " wide" if n == len(SERVICES) - 1 else ""
        alt_html = f'<span class="alt">{alt}</span>' if alt != main else ""
        svc += f'<article class="svc{wide} reveal" style="--d:{(n%4)*.08:.2f}s">{svg(ic)}<div><h3>{main}</h3>{alt_html}</div></article>'

    res = ""
    for (title, cols, tiles, treats) in RESULTS:
        ttl = title[i]
        tiles_html = ""
        for name in tiles:
            suf = name.split("-")[1]
            if suf in ("before", "after"):
                state, view = suf[0], None
            else:
                view, state = suf[0], suf[1]
            state_txt = t["before"] if state == "b" else t["after"]
            view_txt = {"f": t["front"], "s": t["side"], "b": t["back"]}.get(view, "")
            cap = state_txt + (f" · {view_txt}" if view_txt else "")
            w, h = ratio(name)
            alt = f"{ttl} – {cap} – Sculptology Málaga"
            cls = "after" if state == "a" else ""
            tiles_html += (f'<button class="tile" type="button" data-cap="{ttl} · {cap}" style="--ar:{w}/{h}" aria-label="{alt}">'
                           f'<img src="{asset("img/"+name+".webp")}" alt="{alt}" width="{w}" height="{h}" loading="lazy" decoding="async">'
                           f'<span class="lb {cls}">{state_txt}' + (f'<span class="v"> · {view_txt}</span>' if view_txt else '') + '</span></button>')
        chips = "".join(f"<span>{TERM[k][i]}</span>" for k in treats)
        res += f'<article class="res reveal"><h3>{ttl}</h3><div class="tiles c{cols}">{tiles_html}</div><div class="chips">{chips}</div></article>'

    revs = ""
    for n, (name, es, en) in enumerate(REVIEWS):
        txt = es if lang == "es" else en
        revs += f'<figure class="rev reveal" style="--d:{(n%3)*.08:.2f}s"><div class="stars" aria-label="5/5">★★★★★</div><blockquote>{txt}</blockquote><figcaption><cite>{name}</cite></figcaption></figure>'

    h1_plain = t["h1"].replace("<em>", "").replace("</em>", "")
    ld = {
     "@context": "https://schema.org",
     "@type": ["HealthAndBeautyBusiness", "LocalBusiness"],
     "@id": DOMAIN + "/#business",
     "name": "Sculptology",
     "slogan": "El arte de moldear tu cuerpo · The art of sculpting your body",
     "description": t["desc"],
     "url": url,
     "image": DOMAIN + "/assets/img/treatment.webp",
     "telephone": PHONE_INT,
     "address": {"@type": "PostalAddress", "streetAddress": "Calle Santa Lucía 11, Piso 1º, Puerta 7", "addressLocality": "Málaga", "addressRegion": "Andalucía", "addressCountry": "ES"},
     "areaServed": "Málaga",
     "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], "opens": "10:00", "closes": "21:00"}],
     "founder": {"@type": "Person", "name": "Diana Noris", "jobTitle": "Aesthetician"},
     "knowsLanguage": ["es", "en"],
     "makesOffer": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": s[2]}} for s in SERVICES],
    }

    html = f'''<!doctype html>
<html lang="{t["lang"]}" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t["title"]}</title>
<meta name="description" content="{t["desc"]}">
<meta name="theme-color" content="#14100f">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="es" href="{DOMAIN}/">
<link rel="alternate" hreflang="en" href="{DOMAIN}/en/">
<link rel="alternate" hreflang="x-default" href="{DOMAIN}/">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Sculptology">
<meta property="og:title" content="{t["title"]}">
<meta property="og:description" content="{t["desc"]}">
<meta property="og:url" content="{url}">
<meta property="og:locale" content="{t["locale"]}">
<meta property="og:image" content="{DOMAIN}/assets/img/treatment.webp">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/svg+xml" href="{asset("img/favicon.svg")}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" as="image" href="{asset("img/treatment.webp")}" type="image/webp">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Jost:wght@300;400;500&family=Pinyon+Script&family=Playfair+Display:ital,wght@0,400;0,500;0,600;1,400;1,500&display=swap">
<link rel="stylesheet" href="{asset("css/styles.css")}?v={V}">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body id="top">
<a class="skip" href="#main">{t["skip"]}</a>
<header class="header">
  <div class="wrap">
    <a class="logo" href="#top" aria-label="Sculptology">Sculptology</a>
    <div class="header-right">
      <nav class="nav" id="nav" aria-label="{t["menu"]}">{nav}<a class="btn sm nav-cta" href="{wa}" target="_blank" rel="noopener">{t["book"]}</a></nav>
      <div class="lang" role="group" aria-label="Language / Idioma">{flags}</div>
      <button class="burger" type="button" aria-label="{t["menu"]}" aria-controls="nav" aria-expanded="false"><span></span></button>
    </div>
  </div>
</header>

<main id="main">
<section class="hero">
  <div class="hero-bg" role="img" aria-label="Sculptology Málaga"></div>
  <div class="wrap">
    <div class="hero-inner">
      <p class="eyebrow">{t["eyebrow"]}</p>
      <h1>{t["h1"]}</h1>
      <p class="en-sub" lang="{"en" if lang=="es" else "es"}">{t["en_sub"]}</p>
      <p class="lead">{t["lead"]}</p>
      <div class="hero-cta">
        <a class="btn" href="{wa}" target="_blank" rel="noopener">{t["book"]} {ARROW}</a>
        <a class="btn ghost" href="#results">{t["see_results"]}</a>
      </div>
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
      <a class="btn" href="{wa}" target="_blank" rel="noopener">{t["book"]} {ARROW}</a>
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
    <div class="svc-note reveal"><a class="btn dark-ghost" href="{wa}" target="_blank" rel="noopener">{t["svc_cta"]} {ARROW}</a></div>
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
        <div class="c-card"><span class="kicker">{t["wa_l"]}</span><p class="big"><a href="{wa}" target="_blank" rel="noopener">{PHONE_TXT}</a></p></div>
        <div class="c-card"><span class="kicker">{t["hours_l"]}</span><p><strong>{t["days"]}</strong> · <span lang="{"en" if lang=="es" else "es"}">{t["days_en"]}</span></p><p class="big">{t["hours"]}</p><small>{t["hours_alt"]}</small></div>
      </div>
      <div class="map reveal" style="--d:.1s"><iframe title="{t["map_t"]}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q=Calle+Santa+Luc%C3%ADa+11,+M%C3%A1laga&amp;output=embed"></iframe></div>
    </div>
    <div class="cta-band reveal">
      <h2>{t["cta_h"]}</h2>
      <p>{t["cta_p"]}</p>
      <a class="btn" href="{wa}" target="_blank" rel="noopener">{t["book"]} {ARROW}</a>
    </div>
  </div>
</section>
</main>

<footer class="footer">
  <div class="wrap">
    <div class="f-grid">
      <a class="logo" href="#top" aria-label="Sculptology">Sculptology</a>
      <nav aria-label="Footer">{nav}</nav>
    </div>
    <div class="f-bottom"><span>© 2026 Sculptology · Diana Noris · {t["f_rights"]}</span><span>{t["f_tag"]} · Málaga</span></div>
  </div>
</footer>

<a class="wa" href="{wa}" target="_blank" rel="noopener" aria-label="{t["wa_aria"]}">{WA_ICON}</a>

<div class="lightbox" role="dialog" aria-modal="true" aria-hidden="true">
  <button class="lb-close" type="button" aria-label="Close">×</button>
  <button class="lb-prev" type="button" aria-label="Previous">‹</button>
  <img src="" alt="">
  <button class="lb-next" type="button" aria-label="Next">›</button>
  <div class="lb-cap"></div>
</div>

<script src="{asset("js/main.js")}?v={V}" defer></script>
</body>
</html>
'''
    out = SITE / ("index.html" if lang == "es" else "en/index.html")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")

for l in ("es", "en"):
    build(l)

# ---- archivos de apoyo
(SITE / "assets/img/favicon.svg").write_text(
 '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#14100f"/><rect x="8" y="8" width="48" height="48" fill="none" stroke="#b85a69" stroke-width="3"/><text x="32" y="43" font-family="Georgia,serif" font-size="32" fill="#fff" text-anchor="middle">S</text></svg>', encoding="utf-8")
(SITE / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n", encoding="utf-8")
(SITE / "sitemap.xml").write_text(f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
  <url><loc>{DOMAIN}/</loc>
    <xhtml:link rel="alternate" hreflang="es" href="{DOMAIN}/"/>
    <xhtml:link rel="alternate" hreflang="en" href="{DOMAIN}/en/"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="{DOMAIN}/"/></url>
  <url><loc>{DOMAIN}/en/</loc>
    <xhtml:link rel="alternate" hreflang="es" href="{DOMAIN}/"/>
    <xhtml:link rel="alternate" hreflang="en" href="{DOMAIN}/en/"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="{DOMAIN}/"/></url>
</urlset>
''', encoding="utf-8")
print("built")
