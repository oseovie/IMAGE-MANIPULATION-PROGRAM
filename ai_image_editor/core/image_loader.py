from pathlib import Path
from PIL import Image, ImageOps


def load_image(path):
    return ImageOps.exif_transpose(Image.open(path)).convert("RGBA")


def validate_image_path(path):
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(path)
    return path
