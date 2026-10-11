"""Recorta las fotos de antes/después de los collages de Fascia Blasting (las etiquetas se rehacen como texto HTML).
Uso:  python tools/crop_fascia.py <carpeta con 8.jpg y 9.jpg>
Genera site/assets/img/fbl*.webp
"""
import sys
from pathlib import Path

from PIL import Image

SRC = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
OUT = Path(__file__).resolve().parent.parent / "site" / "assets" / "img"

TILES = {
    # 8.jpg - 8 sesiones (espalda/glúteos). Se corta por encima de las etiquetas ANTES / DESPUÉS
    "fbl8-before": ("8.jpg", (54, 416, 540, 1226)),
    "fbl8-after": ("8.jpg", (580, 416, 1072, 1226)),
    # 9.jpg - 6 sesiones (brazos), antes arriba y después abajo. Se evitan las esquinas redondeadas
    "fbl6-before": ("9.jpg", (88, 260, 938, 718)),
    "fbl6-after": ("9.jpg", (88, 734, 938, 1192)),
    # 10.jpg - rodillas, drenaje + Fascia Blast, 10 sesiones (opcional: solo si existe el archivo).
    # Se corta por encima de las etiquetas "Sin tratar" / "Tratada"
    "dlf10-before": ("10.jpg", (52, 332, 552, 1058)),
    "dlf10-after": ("10.jpg", (572, 332, 1072, 1058)),
}

cols, th = 4, 300
sheet = Image.new("RGB", (cols * th, 2 * th), "white")
for i, (name, (f, box)) in enumerate(TILES.items()):
    if not (SRC / f).exists():
        print("(omitida, falta", f + ")", name)
        continue
    im = Image.open(SRC / f).convert("RGB").crop(box)
    im.save(OUT / f"{name}.webp", "WEBP", quality=86, method=6)
    t = im.copy()
    t.thumbnail((th - 6, th - 6))
    sheet.paste(t, ((i % cols) * th + 3, (i // cols) * th + 3))
    print(name, im.size)
sheet.save(Path(__file__).resolve().parent / "contact-fascia.png")
