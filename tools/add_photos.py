"""Añade fotos a la página de un servicio.

Uso:
    python tools/add_photos.py <slug-es> <carpeta_origen> [--build]

    <slug-es>  maderoterapia | fascia-blasting | cavitacion | radiofrecuencia |
               lipolaser | drenaje-linfatico | masajes-postoperatorios | masaje-relajante

Cómo nombra los archivos (según el NOMBRE del archivo de origen):
    antes*.jpg     -> antes-N.webp      (N = 1, 2, 3...)
    despues*.jpg   -> despues-N.webp    (también "después", "after")
    cualquier otro -> foto-N.webp
Los "antes" y "después" se emparejan por orden (antes-1 con despues-1, etc.).
Las nuevas fotos continúan la numeración de las que ya existan.

Convierte JPG/PNG/WEBP (y HEIC si está instalado `pillow-heif`: pip install pillow-heif)
a WebP, máximo 1600 px de lado, calidad 82, y corrige la rotación del móvil (EXIF).
Con --build regenera la web al terminar.
"""
import re
import sys
import unicodedata
from pathlib import Path

from PIL import Image, ImageOps

try:
    from pillow_heif import register_heif_opener
    register_heif_opener()
    HEIC = True
except Exception:  # pillow-heif no instalado
    HEIC = False

ROOT = Path(__file__).resolve().parent.parent
OUT_BASE = ROOT / "site" / "assets" / "img" / "servicios"
EXT = {".jpg", ".jpeg", ".png", ".webp", ".heic", ".heif"}
MAX_SIDE, QUALITY = 1600, 82


def norm(s):
    return unicodedata.normalize("NFD", s.lower()).encode("ascii", "ignore").decode()


def natural(p):
    return [int(x) if x.isdigit() else x for x in re.split(r"(\d+)", p.name.lower())]


def next_index(folder, prefix):
    nums = [int(m.group(1)) for f in folder.glob(f"{prefix}-*.webp") if (m := re.match(rf"{prefix}-(\d+)$", f.stem))]
    return max(nums, default=0) + 1


def convert(src, dst):
    im = Image.open(src)
    im = ImageOps.exif_transpose(im)
    im = im.convert("RGB")
    im.thumbnail((MAX_SIDE, MAX_SIDE), Image.LANCZOS)
    im.save(dst, "WEBP", quality=QUALITY, method=6)
    return im.size


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) != 2:
        print(__doc__)
        sys.exit(1)
    slug, src_dir = args[0], Path(args[1])
    if not src_dir.is_dir():
        sys.exit(f"No existe la carpeta de origen: {src_dir}")
    dst = OUT_BASE / slug
    dst.mkdir(parents=True, exist_ok=True)

    files = sorted([f for f in src_dir.iterdir() if f.suffix.lower() in EXT], key=natural)
    if not files:
        sys.exit("No hay imágenes (jpg, png, webp, heic) en esa carpeta.")
    groups = {"antes": [], "despues": [], "foto": []}
    for f in files:
        n = norm(f.stem)
        key = "antes" if n.startswith(("antes", "before")) else "despues" if n.startswith(("despues", "after")) else "foto"
        groups[key].append(f)

    # antes/después se numeran juntos para que los pares coincidan
    ia, idp, ifo = next_index(dst, "antes"), next_index(dst, "despues"), next_index(dst, "foto")
    start = max(ia, idp)
    done = 0
    for kind, start_n in (("antes", start), ("despues", start), ("foto", ifo)):
        for k, f in enumerate(groups[kind]):
            if f.suffix.lower() in (".heic", ".heif") and not HEIC:
                print(f"  ! {f.name}: HEIC no soportado (pip install pillow-heif, o exporta a JPG)")
                continue
            target = dst / f"{kind}-{start_n + k}.webp"
            w, h = convert(f, target)
            print(f"  {f.name} -> {target.relative_to(ROOT).as_posix()} ({w}x{h})")
            done += 1
    if len(groups["antes"]) != len(groups["despues"]):
        print("  ! Aviso: hay distinto número de 'antes' y 'después'; solo se muestran los pares completos.")
    print(f"{done} imagen(es) añadida(s) a {slug}.")
    if "--build" in sys.argv:
        import subprocess
        subprocess.run([sys.executable, str(ROOT / "tools" / "build.py")], check=True)
    else:
        print("Ejecuta: python tools/build.py")


if __name__ == "__main__":
    main()
