from PIL import ImageEnhance


def apply(image, factor=1.1):
    return ImageEnhance.Color(image).enhance(factor)

