from PIL import ImageEnhance


def apply(image, factor=1.1):
    return ImageEnhance.Contrast(image).enhance(factor)

