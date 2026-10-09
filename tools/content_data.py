"""Tratamientos (términos), resultados antes/después y opiniones."""
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

