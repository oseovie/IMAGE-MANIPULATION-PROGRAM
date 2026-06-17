from PIL import ImageEnhance


def apply(image):
    return ImageEnhance.Brightness(image).enhance(1.05)

