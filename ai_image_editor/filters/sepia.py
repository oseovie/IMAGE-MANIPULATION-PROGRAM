from PIL import ImageOps


def apply(image):
    gray = ImageOps.grayscale(image)
    return ImageOps.colorize(gray, "#2f1b0c", "#f4d39b").convert("RGBA")

