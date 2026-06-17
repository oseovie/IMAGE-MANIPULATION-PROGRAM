from PIL import ImageEnhance


def apply(image, factor=1.4):
    return ImageEnhance.Sharpness(image).enhance(factor)

