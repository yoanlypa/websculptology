"""Contenido de las páginas de servicio. Edita aquí los textos, precios y preguntas.

Cada servicio tiene versión ES y EN. Los precios son los del Square de Diana.
`price=None` -> se muestra "Consultar precio al reservar" (pendiente de confirmar).
Las fotos propias de cada servicio van en site/assets/img/servicios/<slug-es>/ (ver tools/add_photos.py).
"""

BOOK_URL = "https://book.squareup.com/appointments/6qqitn5cb9pe3n/location/L9MN4N2H0FFN1/services"
SHOW_PHOTO_PLACEHOLDERS = True  # False -> oculta el bloque "Muy pronto: fotos reales"

# Frase "qué incluye cada sesión" (solo servicios con incluye_square=True)
INCLUDES = {
    "es": ["10 minutos de plataforma vibratoria", "Medidas corporales y fotos de antes y después", "Seguimiento personalizado de tu progreso"],
    "en": ["10 minutes on the vibration plate", "Body measurements and before-and-after photos", "Personalised follow-up of your progress"],
}


def P(es, en, price):
    """Una tarjeta de precio."""
    return {"es": es, "en": en, "price": price}


SERVICES = [
    # ------------------------------------------------------------------ 1
    {
        "id": "wood", "icon": "wood", "key": "wood", "incluye_square": True,
        "slug": {"es": "maderoterapia", "en": "wood-therapy"},
        "name": {"es": "Maderoterapia", "en": "Wood Therapy"},
        "card": {"es": "Maderoterapia", "en": "Wood Therapy"},
        "intro": {
            "es": "Técnica de masaje de origen colombiano que usa instrumentos de madera de distintas formas para trabajar el tejido en profundidad y moldear la silueta. Diana combina la madera con maniobras manuales adaptadas a cada zona de tu cuerpo.",
            "en": "A massage technique of Colombian origin that uses wooden instruments of different shapes to work the tissue deeply and shape the silhouette. Diana combines the wooden tools with hands-on techniques adapted to each area of your body.",
        },
        "benefits": {
            "es": ["Ayuda a moldear y definir la silueta.", "Mejora el aspecto de la celulitis y la piel de naranja.", "Estimula la circulación y la eliminación de líquidos.", "Tonifica y reafirma la piel.", "Sensación de ligereza desde la primera sesión."],
            "en": ["Helps shape and define the silhouette.", "Improves the look of cellulite and orange-peel skin.", "Stimulates circulation and the elimination of fluids.", "Tones and firms the skin.", "A feeling of lightness from the very first session."],
        },
        "steps": {
            "es": ["Valoración, medidas y fotos.", "10 minutos en plataforma vibratoria.", "Trabajo con los instrumentos de madera, zona por zona.", "Recomendaciones y seguimiento."],
            "en": ["Assessment, measurements and photos.", "10 minutes on the vibration plate.", "Work with the wooden instruments, area by area.", "Recommendations and follow-up."],
        },
        "notes": [{
            "title": {"es": "Ideal para", "en": "Ideal for"},
            "body": {"es": "Retención de líquidos, celulitis, abdomen, cintura, glúteos, piernas y brazos.", "en": "Fluid retention, cellulite, abdomen, waist, glutes, legs and arms."},
        }],
        "prices": [P("30 min · 1 zona", "30 min · 1 area", 50), P("60 min · 3 zonas", "60 min · 3 areas", 85)],
        "faq": {
            "es": [("¿Duele?", "Es un masaje intenso, pero la presión se adapta a ti. Es normal notar algo de sensibilidad en las primeras sesiones."),
                   ("¿Cuándo se notan los resultados?", "Muchas clientas notan menos hinchazón y la piel más lisa desde el principio. Los cambios en la silueta llegan con constancia; Diana te recomienda la frecuencia en la valoración."),
                   ("¿Qué hago después?", "Bebe mucha agua y mantente activa para potenciar el efecto drenante.")],
            "en": [("Does it hurt?", "It is an intense massage, but the pressure is adapted to you. Some tenderness in the first sessions is normal."),
                   ("When will I see results?", "Many clients notice less swelling and smoother skin from the start. Changes to the silhouette come with consistency; Diana will recommend how often to come during your assessment."),
                   ("What should I do afterwards?", "Drink plenty of water and stay active to boost the draining effect.")],
        },
        "consult": {
            "es": ["Estás embarazada.", "Tienes varices marcadas o flebitis.", "Tomas anticoagulantes.", "Tienes heridas o infecciones en la piel de la zona."],
            "en": ["You are pregnant.", "You have pronounced varicose veins or phlebitis.", "You take anticoagulants.", "You have wounds or skin infections in the area."],
        },
    },
    # ------------------------------------------------------------------ 2
    {
        "id": "fascia", "icon": "fascia", "key": "fascia", "incluye_square": True,
        "slug": {"es": "fascia-blasting", "en": "fascia-blasting"},
        "name": {"es": "Fascia Blasting", "en": "Fascia Blasting"},
        "card": {"es": "Fascia Blasting", "en": "Fascia Blasting"},
        "intro": {
            "es": "Técnica especializada que trabaja la fascia, el tejido conectivo que envuelve músculos y grasa, con la herramienta FasciaBlaster®. Al liberar las tensiones de la fascia, la piel se ve más lisa y uniforme. Sculptology está especializada en esta técnica.",
            "en": "A specialised technique that works on the fascia, the connective tissue that surrounds muscle and fat, using the FasciaBlaster® tool. By releasing tension in the fascia, the skin looks smoother and more even. Sculptology specialises in this technique.",
        },
        "benefits": {
            "es": ["Mejora visible del aspecto de la celulitis y de la textura de la piel.", "Ayuda con irregularidades y tejido cicatricial.", "Activa la circulación.", "Cuerpo más suelto y ligero.", "Potencia el resultado de otros tratamientos de contorno."],
            "en": ["Visibly improves the look of cellulite and skin texture.", "Helps with irregularities and scar tissue.", "Activates circulation.", "A looser, lighter-feeling body.", "Boosts the results of other contouring treatments."],
        },
        "steps": {
            "es": ["Valoración, medidas y fotos.", "10 minutos en plataforma vibratoria.", "Calentamiento de la zona.", "Trabajo con la herramienta, de forma progresiva.", "Seguimiento."],
            "en": ["Assessment, measurements and photos.", "10 minutes on the vibration plate.", "Warming up the area.", "Gradual work with the tool.", "Follow-up."],
        },
        "notes": [{
            "title": {"es": "Sesiones recomendadas", "en": "Recommended sessions"},
            "body": {"es": "Se recomiendan unas 6 sesiones.", "en": "We recommend around 6 sessions."},
        }],
        "prices": [P("30 min · 1 zona", "30 min · 1 area", 75), P("60 min · 2 zonas", "60 min · 2 areas", 105), P("90 min · 3 zonas", "90 min · 3 areas", 125)],
        "faq": {
            "es": [("¿Salen moratones?", "En las primeras sesiones pueden aparecer hematomas leves. Desaparecen en pocos días y suelen ir a menos con cada sesión."),
                   ("¿Duele?", "Es intenso, pero Diana adapta la presión a tu tolerancia."),
                   ("¿Cuántas sesiones necesito?", "Se recomiendan unas 6; en la valoración te hace un plan personalizado.")],
            "en": [("Will I bruise?", "Mild bruising can appear in the first sessions. It fades within a few days and usually lessens with each session."),
                   ("Does it hurt?", "It is intense, but Diana adapts the pressure to your tolerance."),
                   ("How many sessions do I need?", "Around 6 are recommended; at your assessment she will create a personalised plan for you.")],
        },
        "consult": {
            "es": ["Estás embarazada.", "Tomas anticoagulantes o tienes problemas de coagulación.", "Tienes varices o antecedentes de trombosis.", "Tienes heridas, infecciones o quemaduras solares en la zona."],
            "en": ["You are pregnant.", "You take anticoagulants or have clotting problems.", "You have varicose veins or a history of thrombosis.", "You have wounds, infections or sunburn in the area."],
        },
    },
    # ------------------------------------------------------------------ 3
    {
        "id": "cav", "icon": "cav", "key": "cav", "incluye_square": True,
        "slug": {"es": "cavitacion", "en": "cavitation"},
        "name": {"es": "Cavitación", "en": "Cavitation"},
        "card": {"es": "Cavitación", "en": "Cavitation"},
        "intro": {
            "es": "Tratamiento no invasivo que usa ultrasonidos de baja frecuencia para actuar sobre la grasa localizada y ayudar a remodelar el contorno corporal. Sin agujas, sin cirugía y sin tiempo de recuperación.",
            "en": "A non-invasive treatment that uses low-frequency ultrasound to target localised fat and help reshape the body's contours. No needles, no surgery and no downtime.",
        },
        "benefits": {
            "es": ["Ayuda a reducir la grasa localizada en zonas rebeldes.", "Remodela abdomen, cintura, flancos y piernas.", "No invasivo e indoloro.", "Vuelves a tu rutina al momento.", "Combina muy bien con radiofrecuencia y drenaje."],
            "en": ["Helps reduce localised fat in stubborn areas.", "Reshapes the abdomen, waist, flanks and legs.", "Non-invasive and painless.", "You go straight back to your routine.", "Combines very well with radiofrequency and drainage."],
        },
        "steps": {
            "es": ["Valoración y medidas.", "10 minutos en plataforma vibratoria.", "Aplicación de ultrasonidos con gel conductor.", "Fotos y seguimiento."],
            "en": ["Assessment and measurements.", "10 minutes on the vibration plate.", "Ultrasound applied with conductive gel.", "Photos and follow-up."],
        },
        "notes": [{
            "title": {"es": "Consejos", "en": "Tips"},
            "body": {"es": "Bebe mucha agua antes y después. Evita el alcohol y las comidas muy grasas en los días del tratamiento.",
                     "en": "Drink plenty of water before and after. Avoid alcohol and very fatty meals on the days of your treatment."},
        }],
        "prices": [P("30 min · 1 zona", "30 min · 1 area", 50), P("60 min · 3 zonas", "60 min · 3 areas", 90)],
        "faq": {
            "es": [("¿Duele?", "No. Solo notarás un zumbido y un ligero calor."),
                   ("¿Sirve para adelgazar?", "No es un tratamiento para perder peso, sino para moldear zonas concretas. Funciona mejor acompañado de hábitos saludables."),
                   ("¿Cada cuánto se hace?", "Se dejan unos días entre sesiones en la misma zona; Diana te indica la frecuencia.")],
            "en": [("Does it hurt?", "No. You will only notice a hum and a slight warmth."),
                   ("Is it a weight-loss treatment?", "No. It is not for losing weight but for shaping specific areas, and it works best alongside healthy habits."),
                   ("How often is it done?", "A few days are left between sessions on the same area; Diana will tell you how often to come.")],
        },
        "consult": {
            "es": ["Estás embarazada o en lactancia.", "Llevas marcapasos o implantes metálicos en la zona.", "Tienes enfermedades hepáticas o renales.", "Tienes cáncer activo."],
            "en": ["You are pregnant or breastfeeding.", "You have a pacemaker or metal implants in the area.", "You have liver or kidney disease.", "You have active cancer."],
        },
    },
    # ------------------------------------------------------------------ 4
    {
        "id": "rf", "icon": "rf", "key": "rf", "incluye_square": True,
        "slug": {"es": "radiofrecuencia", "en": "radiofrequency"},
        "name": {"es": "Radiofrecuencia", "en": "Radiofrequency"},
        "card": {"es": "Radiofrecuencia", "en": "Radiofrequency"},
        "intro": {
            "es": "Tratamiento no invasivo que genera un calor controlado en las capas profundas de la piel para estimular el colágeno y la elastina. Mejora el aspecto de la flacidez y deja la piel más firme y tersa.",
            "en": "A non-invasive treatment that produces controlled heat in the deeper layers of the skin to stimulate collagen and elastin. It improves the look of loose skin and leaves it firmer and smoother.",
        },
        "benefits": {
            "es": ["Más firmeza en abdomen, brazos, piernas y glúteos.", "Ideal tras cambios de peso.", "Mejora el aspecto de la celulitis.", "Sensación agradable de calor.", "Sin tiempo de recuperación."],
            "en": ["More firmness in the abdomen, arms, legs and glutes.", "Ideal after weight changes.", "Improves the look of cellulite.", "A pleasant feeling of warmth.", "No downtime."],
        },
        "steps": {
            "es": ["Valoración y medidas.", "10 minutos en plataforma vibratoria.", "Aplicación de radiofrecuencia por zonas.", "Fotos y seguimiento."],
            "en": ["Assessment and measurements.", "10 minutes on the vibration plate.", "Radiofrequency applied area by area.", "Photos and follow-up."],
        },
        "notes": [{
            "title": {"es": "Resultados progresivos", "en": "Progressive results"},
            "body": {"es": "Los resultados son progresivos: el colágeno se sigue formando semanas después, por eso se trabaja en serie de sesiones.",
                     "en": "Results build up gradually: collagen keeps forming for weeks afterwards, which is why we work in a series of sessions."},
        }],
        "prices": [P("30 min · 1 zona", "30 min · 1 area", 50), P("60 min · 3 zonas", "60 min · 3 areas", 90)],
        "faq": {
            "es": [("¿Qué se siente?", "Un calor agradable, como un masaje caliente."),
                   ("¿Cuándo se ven los resultados?", "La piel se nota más tersa al terminar y la firmeza mejora con la serie de sesiones."),
                   ("¿Se puede combinar?", "Sí, es el complemento perfecto de la cavitación.")],
            "en": [("What does it feel like?", "A pleasant warmth, like a hot massage."),
                   ("When will I see results?", "Skin feels smoother straight after the session, and firmness improves over the series of sessions."),
                   ("Can it be combined with other treatments?", "Yes, it is the perfect complement to cavitation.")],
        },
        "consult": {
            "es": ["Estás embarazada.", "Llevas marcapasos, implantes metálicos o prótesis en la zona.", "Tienes cáncer activo.", "Tienes heridas o infecciones en la piel."],
            "en": ["You are pregnant.", "You have a pacemaker, metal implants or a prosthesis in the area.", "You have active cancer.", "You have wounds or skin infections."],
        },
    },
    # ------------------------------------------------------------------ 5 (NUEVO)
    {
        "id": "lipo", "icon": "lipo", "key": "lipo", "incluye_square": True,
        "slug": {"es": "lipolaser", "en": "lipo-laser"},
        "name": {"es": "Lipoláser", "en": "Lipo Laser"},
        "card": {"es": "Lipoláser", "en": "Lipo Laser"},
        "intro": {
            "es": "Láser de baja intensidad que se aplica con placas sobre la zona a tratar. Es no invasivo e indoloro, ayuda a reducir la grasa localizada y a remodelar el contorno. Suele hacerse en varias sesiones y combinarse con otros tratamientos.",
            "en": "A low-level laser applied with pads over the area being treated. It is non-invasive and painless, and helps reduce localised fat and reshape the contours. It is usually done over several sessions and combined with other treatments.",
        },
        "benefits": {
            "es": ["Indoloro: te relajas mientras actúa.", "Pensado para zonas rebeldes.", "Sin tiempo de recuperación.", "Potencia los resultados de la cavitación y la radiofrecuencia."],
            "en": ["Painless: you relax while it works.", "Designed for stubborn areas.", "No downtime.", "Boosts the results of cavitation and radiofrequency."],
        },
        "steps": {
            "es": ["Valoración y medidas.", "10 minutos en plataforma vibratoria.", "Colocación de las placas de láser.", "Fotos y seguimiento."],
            "en": ["Assessment and measurements.", "10 minutes on the vibration plate.", "Laser pads placed on the area.", "Photos and follow-up."],
        },
        "notes": [],
        "prices": [P("1 zona", "1 area", 50), P("2 zonas", "2 areas", 80)],
        "faq": {
            "es": [("¿Qué se siente?", "Prácticamente nada; como mucho, un ligero calor."),
                   ("¿Cuántas sesiones?", "Se trabaja en serie; Diana te propone el plan en la valoración."),
                   ("¿Lo puedo combinar?", "Sí, suele ir con cavitación o radiofrecuencia.")],
            "en": [("What does it feel like?", "Practically nothing; at most, a slight warmth."),
                   ("How many sessions?", "We work in a series; Diana will propose a plan at your assessment."),
                   ("Can I combine it with other treatments?", "Yes, it is usually paired with cavitation or radiofrequency.")],
        },
        "consult": {
            "es": ["Estás embarazada o en lactancia.", "Llevas marcapasos.", "Tienes cáncer activo.", "Tomas medicación fotosensibilizante."],
            "en": ["You are pregnant or breastfeeding.", "You have a pacemaker.", "You have active cancer.", "You take photosensitising medication."],
        },
    },
    # ------------------------------------------------------------------ 6
    {
        "id": "lymph", "icon": "lymph", "key": "lymph", "incluye_square": False,
        "slug": {"es": "drenaje-linfatico", "en": "lymphatic-drainage"},
        "name": {"es": "Drenaje Linfático", "en": "Lymphatic Drainage"},
        "card": {"es": "Drenaje Linfático", "en": "Lymphatic Drainage"},
        "intro": {
            "es": "Masaje suave, lento y rítmico que estimula el sistema linfático para ayudar a eliminar los líquidos retenidos. Deja una sensación inmediata de ligereza y bienestar.",
            "en": "A gentle, slow, rhythmic massage that stimulates the lymphatic system to help eliminate retained fluids. It leaves an immediate feeling of lightness and wellbeing.",
        },
        "benefits": {
            "es": ["Reduce la retención de líquidos y la hinchazón.", "Alivia las piernas cansadas y pesadas.", "Ayuda a desinflamar.", "Favorece la circulación.", "Muy relajante.", "El complemento ideal de los tratamientos de contorno."],
            "en": ["Reduces fluid retention and swelling.", "Relieves tired, heavy legs.", "Helps reduce puffiness.", "Supports circulation.", "Deeply relaxing.", "The ideal complement to contouring treatments."],
        },
        "steps": {
            "es": ["Valoración.", "Maniobras manuales suaves siguiendo el recorrido de la linfa.", "Recomendaciones para casa."],
            "en": ["Assessment.", "Gentle manual techniques following the path of the lymph.", "Recommendations for home."],
        },
        "notes": [],
        "prices": [],  # TODO Diana: confirmar precios del drenaje linfático
        "faq": {
            "es": [("¿Duele?", "No, es una técnica muy suave."),
                   ("¿Cuántas sesiones?", "Muchas personas notan ligereza desde la primera. Para la retención continua se recomiendan sesiones periódicas."),
                   ("¿Es normal ir más al baño después?", "Sí, es señal de que el cuerpo está eliminando líquidos.")],
            "en": [("Does it hurt?", "No, it is a very gentle technique."),
                   ("How many sessions?", "Many people feel lighter after the first. For ongoing fluid retention, regular sessions are recommended."),
                   ("Is it normal to go to the toilet more afterwards?", "Yes, it is a sign that your body is eliminating fluids.")],
        },
        "consult": {
            "es": ["Tienes trombosis o flebitis.", "Tienes insuficiencia cardíaca o renal.", "Tienes fiebre o una infección aguda.", "Tienes cáncer activo sin autorización médica."],
            "en": ["You have thrombosis or phlebitis.", "You have heart or kidney failure.", "You have a fever or an acute infection.", "You have active cancer without medical clearance."],
        },
    },
    # ------------------------------------------------------------------ 7
    {
        "id": "postop", "icon": "lotus", "key": None, "incluye_square": False,
        "featured_review": "Liz Estefania Correa",
        "slug": {"es": "masajes-postoperatorios", "en": "post-op-massage"},
        "name": {"es": "Masajes Postoperatorios", "en": "Post-Op Massages"},
        "card": {"es": "Masajes Postoperatorios", "en": "Post-Op Massages"},
        "intro": {
            "es": "Masajes especializados para después de una cirugía estética: liposucción, lipoescultura, abdominoplastia, BBL, cirugía de mamas… Combinan drenaje linfático manual con técnicas específicas para reducir la inflamación, prevenir la fibrosis y ayudarte a recuperarte mejor.",
            "en": "Specialised massages for after cosmetic surgery: liposuction, liposculpture, tummy tuck, BBL, breast surgery… They combine manual lymphatic drainage with specific techniques to reduce inflammation, prevent fibrosis and help you recover better.",
        },
        "benefits": {
            "es": ["Reduce la inflamación y el edema.", "Previene y trata la fibrosis y los endurecimientos.", "Favorece una buena cicatrización.", "Ayuda a que el resultado de tu cirugía se vea más uniforme.", "Acompañamiento cercano en una etapa delicada."],
            "en": ["Reduces inflammation and oedema.", "Prevents and treats fibrosis and hardened areas.", "Supports good healing.", "Helps your surgical result look more even.", "Close support during a delicate stage."],
        },
        "steps": {
            "es": ["Revisión de tu cirugía y de las indicaciones médicas.", "Drenaje y técnicas para la fibrosis.", "Pautas de cuidado en casa."],
            "en": ["A review of your surgery and your medical instructions.", "Drainage and techniques for fibrosis.", "Aftercare guidance for home."],
        },
        "notes": [
            {"title": {"es": "Cuándo empezar", "en": "When to start"},
             "body": {"es": "Cuando tu cirujano lo autorice, normalmente en los primeros días o semanas. Trae tus indicaciones médicas y tu faja.",
                      "en": "Once your surgeon gives the go-ahead, usually in the first days or weeks. Bring your medical instructions and your compression garment."}},
            {"title": {"es": "Importante", "en": "Important"},
             "body": {"es": "Se necesita la autorización de tu cirujano. Si tienes fiebre, signos de infección o sospecha de trombosis, consulta antes con tu médico.",
                      "en": "Your surgeon's authorisation is required. If you have a fever, signs of infection or suspect a thrombosis, please speak to your doctor first."}},
        ],
        "prices": [],  # TODO Diana: confirmar precios de los masajes postoperatorios
        "faq": {
            "es": [("¿Cuándo empiezo?", "En cuanto tu cirujano te dé el visto bueno."),
                   ("¿Cuántas sesiones necesito?", "Depende de la cirugía y de tu evolución; Diana te hace un plan."),
                   ("¿Traigo la faja?", "Sí, tráela a cada sesión.")],
            "en": [("When do I start?", "As soon as your surgeon gives you the go-ahead."),
                   ("How many sessions do I need?", "It depends on the surgery and how you are healing; Diana will make a plan for you."),
                   ("Should I bring my compression garment?", "Yes, please bring it to every session.")],
        },
        "consult": {
            "es": ["Tu cirujano aún no ha autorizado los masajes.", "Tienes fiebre o signos de infección.", "Sospechas de una trombosis."],
            "en": ["Your surgeon has not yet authorised massage.", "You have a fever or signs of infection.", "You suspect a thrombosis."],
        },
    },
    # ------------------------------------------------------------------ 8
    {
        "id": "relax", "icon": "massage", "key": None, "incluye_square": False,
        "slug": {"es": "masaje-relajante", "en": "relaxing-massage"},
        "name": {"es": "Masaje Relajante Terapéutico de Cuerpo Completo", "en": "Full Body Relaxation Therapeutic Massage"},
        "card": {"es": "Masaje Relajante Terapéutico", "en": "Relaxing Therapeutic Massage"},
        "intro": {
            "es": "Masaje de cuerpo completo para liberar tensiones, relajar la musculatura y desconectar del estrés. Combina maniobras relajantes con presión terapéutica en las zonas de más carga: espalda, cuello y hombros.",
            "en": "A full-body massage to release tension, relax the muscles and switch off from stress. It combines relaxing strokes with therapeutic pressure on the areas that carry the most load: back, neck and shoulders.",
        },
        "benefits": {
            "es": ["Alivia la tensión muscular y las contracturas leves.", "Reduce el estrés y mejora el descanso.", "Activa la circulación.", "Sensación de bienestar general.", "Presión totalmente a tu gusto."],
            "en": ["Relieves muscle tension and mild knots.", "Reduces stress and improves rest.", "Activates circulation.", "A general feeling of wellbeing.", "Pressure entirely to your liking."],
        },
        "steps": {
            "es": ["Charla breve sobre tus zonas de tensión.", "Masaje de cuerpo completo.", "Unos minutos de descanso al terminar."],
            "en": ["A short chat about your areas of tension.", "Full-body massage.", "A few minutes' rest at the end."],
        },
        "notes": [],
        "prices": [],  # TODO Diana: confirmar precios del masaje relajante
        "faq": {
            "es": [("¿Qué presión usáis?", "La que tú prefieras: puede ser suave o más profunda."),
                   ("¿Tengo que traer algo?", "No, todo está incluido."),
                   ("¿Es solo relajante?", "Es relajante y terapéutico a la vez: se insiste en las zonas con más carga.")],
            "en": [("What pressure do you use?", "Whatever you prefer: it can be gentle or deeper."),
                   ("Do I need to bring anything?", "No, everything is included."),
                   ("Is it purely relaxing?", "It is both relaxing and therapeutic: we focus on the areas that carry the most tension.")],
        },
        "consult": {
            "es": ["Tienes fiebre.", "Tienes una infección.", "Tienes una lesión reciente.", "Tienes trombosis."],
            "en": ["You have a fever.", "You have an infection.", "You have a recent injury.", "You have thrombosis."],
        },
    },
]

# TODO Diana: fotos propias de cada servicio -> tools/add_photos.py <slug-es> <carpeta>
# TODO Diana: confirmar los textos de todas las páginas (son una propuesta).

# Frase corta bajo el título de cada página (propuesta, Diana la confirmará)
TAGLINES = {
    "wood": {"es": "Moldea tu silueta con madera y manos expertas.", "en": "Shape your silhouette with wooden tools and expert hands."},
    "fascia": {"es": "Libera la fascia y deja la piel más lisa y uniforme.", "en": "Release the fascia for smoother, more even-looking skin."},
    "cav": {"es": "Ultrasonidos para remodelar zonas rebeldes, sin agujas ni cirugía.", "en": "Ultrasound to reshape stubborn areas, with no needles and no surgery."},
    "rf": {"es": "Calor controlado para una piel más firme y tersa.", "en": "Controlled heat for firmer, smoother skin."},
    "lipo": {"es": "Láser indoloro para remodelar tu contorno.", "en": "Painless laser to reshape your contours."},
    "lymph": {"es": "Ligereza y bienestar desde la primera sesión.", "en": "Lightness and wellbeing from the first session."},
    "postop": {"es": "Te acompañamos en tu recuperación tras la cirugía.", "en": "Supporting your recovery after surgery."},
    "relax": {"es": "Desconecta del estrés con la presión que a ti te guste.", "en": "Switch off from stress with the pressure you like."},
}
for _s in SERVICES:
    _s["tagline"] = TAGLINES[_s["id"]]
