from PIL import ImageEnhance


def apply(image):
    result = ImageEnhance.Contrast(image).enhance(1.18)
    result = ImageEnhance.Color(result).enhance(0.9)
    return ImageEnhance.Brightness(result).enhance(0.98)

