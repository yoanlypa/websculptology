"""Recorta las fotos de antes/después de los collages de Drenaje Linfático (se rehacen las etiquetas como texto HTML).
Uso:  python tools/crop_drenaje.py <carpeta con 3.jpg ... 7.jpg>
Genera site/assets/img/dl*.webp
"""
import sys
from pathlib import Path

from PIL import Image

SRC = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
OUT = Path(__file__).resolve().parent.parent / "site" / "assets" / "img"

# nombre -> (archivo, (x0, y0, x1, y1))
# sufijos: fb/fa = frontal antes/después, sb/sa = lateral antes/después
TILES = {
    # 3.jpg  - 3 sesiones (tatuajes). Fila superior frontal, inferior lateral; izquierda antes, derecha después
    "dl3a-fb": ("3.jpg", (70, 346, 550, 782)),
    "dl3a-fa": ("3.jpg", (574, 346, 1056, 782)),
    "dl3a-sb": ("3.jpg", (70, 852, 550, 1294)),
    "dl3a-sa": ("3.jpg", (574, 852, 1056, 1294)),
    # 4.jpg  - 3 sesiones (fondo verde). Fila superior = antes (frontal, lateral); inferior = después
    "dl3b-fb": ("4.jpg", (60, 420, 616, 774)),
    "dl3b-sb": ("4.jpg", (642, 420, 1064, 774)),
    "dl3b-fa": ("4.jpg", (60, 858, 616, 1212)),
    "dl3b-sa": ("4.jpg", (642, 858, 1064, 1212)),
    # 5.jpg  - 3 sesiones (collage en inglés). Se recorta por encima de las etiquetas "Before/After"
    "dl3c-fb": ("5.jpg", (100, 294, 550, 664)),
    "dl3c-fa": ("5.jpg", (574, 294, 1024, 664)),
    "dl3c-sb": ("5.jpg", (100, 746, 550, 1116)),
    "dl3c-sa": ("5.jpg", (574, 746, 1024, 1116)),
    # 6.jpg  - 1 sesión (glúteos). Por encima de las etiquetas "Antes/Después"
    "dl1a-before": ("6.jpg", (8, 100, 288, 420)),
    "dl1a-after": ("6.jpg", (302, 100, 582, 420)),
    # 7.jpg  - 1 sesión (abdomen)
    "dl1b-before": ("7.jpg", (56, 458, 548, 1084)),
    "dl1b-after": ("7.jpg", (580, 458, 1070, 1084)),
}

cols, th = 4, 260
sheet = Image.new("RGB", (cols * th, ((len(TILES) + cols - 1) // cols) * th), "white")
for i, (name, (f, box)) in enumerate(TILES.items()):
    im = Image.open(SRC / f).convert("RGB").crop(box)
    im.save(OUT / f"{name}.webp", "WEBP", quality=86, method=6)
    t = im.copy()
    t.thumbnail((th - 6, th - 6))
    sheet.paste(t, ((i % cols) * th + 3, (i // cols) * th + 3))
    print(name, im.size)
sheet.save(Path(__file__).resolve().parent / "contact-drenaje.png")
