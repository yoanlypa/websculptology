"""Recorta las fotos reales de los collages originales y las optimiza a WebP."""
from PIL import Image
from pathlib import Path

SRC = Path(r"D:\webSculptology\src-images")
OUT = Path(r"D:\webSculptology\site\assets\img")
OUT.mkdir(parents=True, exist_ok=True)

# nombre -> (imagen origen, (x0, y0, x1, y1))
TILES = {
    # 12 sesiones
    "r12-before": ("06", (35, 488, 391, 1050)),
    "r12-after":  ("06", (416, 488, 758, 1050)),
    # 2 tratamientos
    "r2-fb": ("07", (120, 198, 560, 670)),
    "r2-sb": ("07", (576, 198, 992, 670)),
    "r2-fa": ("07", (120, 684, 560, 1172)),
    "r2-sa": ("07", (576, 684, 992, 1172)),
    # meltdown session
    "melt-before": ("08", (25, 390, 505, 1000)),
    "melt-after":  ("08", (519, 390, 1000, 1000)),
    # 4 tratamientos
    "r4-fb": ("09", (145, 188, 608, 606)),
    "r4-sb": ("09", (622, 188, 1087, 606)),
    "r4-fa": ("09", (145, 618, 608, 1044)),
    "r4-sa": ("09", (622, 618, 1087, 1044)),
    # 1 tratamiento (césped)
    "r1g-fb": ("10", (112, 193, 596, 590)),
    "r1g-sb": ("10", (611, 193, 1098, 590)),
    "r1g-fa": ("10", (112, 602, 596, 1016)),
    "r1g-sa": ("10", (611, 602, 1098, 1016)),
    # super meltdown
    "sm-fb": ("11", (56, 456, 402, 838)),
    "sm-fa": ("11", (422, 456, 764, 838)),
    "sm-sb": ("11", (56, 928, 402, 1350)),
    "sm-sa": ("11", (422, 928, 764, 1350)),
    # 1 tratamiento (fondo blanco)
    "r1w-sb": ("12", (122, 202, 546, 685)),
    "r1w-fb": ("12", (557, 202, 990, 685)),
    "r1w-sa": ("12", (122, 698, 546, 1198)),
    "r1w-fa": ("12", (557, 698, 990, 1198)),
    # real results (3 vistas)
    "rr-fb": ("13", (133, 300, 432, 624)),
    "rr-sb": ("13", (449, 300, 750, 624)),
    "rr-bb": ("13", (766, 300, 1069, 624)),
    "rr-fa": ("13", (133, 640, 432, 962)),
    "rr-sa": ("13", (449, 640, 750, 962)),
    "rr-ba": ("13", (766, 640, 1069, 962)),
    # 5 sesiones
    "r5-fb": ("14", (118, 195, 553, 525)),
    "r5-fa": ("14", (570, 195, 996, 525)),
    "r5-sb": ("14", (118, 540, 553, 872)),
    "r5-sa": ("14", (570, 540, 996, 872)),
    "r5-bb": ("14", (118, 885, 553, 1222)),
    "r5-ba": ("14", (570, 885, 996, 1222)),
    # 3 tratamientos
    "r3-fb": ("15", (161, 176, 603, 620)),
    "r3-sb": ("15", (622, 176, 1064, 620)),
    "r3-fa": ("15", (161, 638, 603, 1083)),
    "r3-sa": ("15", (622, 638, 1064, 1083)),
    # 6 tratamientos
    "r6-before": ("16", (26, 292, 548, 884)),
    "r6-after":  ("16", (574, 292, 1097, 884)),
}

for name, (src, box) in TILES.items():
    x0, y0, x1, y1 = box
    im = Image.open(SRC / f"{src}.png").convert("RGB").crop((x0 + 5, y0 + 5, x1 - 5, y1 - 5))
    im.save(OUT / f"{name}.webp", "WEBP", quality=84, method=6)

# Diana (mitad izquierda de la imagen 02) y foto de tratamiento (03)
im = Image.open(SRC / "02.png").convert("RGB").crop((0, 0, 768, 1086))
im.save(OUT / "diana.webp", "WEBP", quality=86, method=6)
im = Image.open(SRC / "03.png").convert("RGB")
im.save(OUT / "treatment.webp", "WEBP", quality=86, method=6)

# hoja de contacto para revisar los recortes
names = list(TILES)
cols, th = 8, 220
rows = (len(names) + cols - 1) // cols
sheet = Image.new("RGB", (cols * th, rows * th), "white")
for i, n in enumerate(names):
    t = Image.open(OUT / f"{n}.webp")
    t.thumbnail((th - 6, th - 6))
    sheet.paste(t, ((i % cols) * th + 3, (i // cols) * th + 3))
sheet.save(Path(r"D:\webSculptology\tools\contact-sheet.png"))
print("ok", len(names), "tiles")
