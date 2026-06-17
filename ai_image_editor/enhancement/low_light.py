from PIL import ImageEnhance


def apply(image, factor=1.35):
    return ImageEnhance.Brightness(image).enhance(factor)

