from pathlib import Path


def save_image(image, path, quality=90):
    path = Path(path)
    output = image.convert("RGB") if path.suffix.lower() in {".jpg", ".jpeg", ".bmp"} else image
    output.save(path, quality=quality)
    return path
