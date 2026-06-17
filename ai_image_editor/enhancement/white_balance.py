from PIL import ImageOps


def apply(image):
    return ImageOps.autocontrast(image.convert("RGB"), cutoff=1).convert("RGBA")

