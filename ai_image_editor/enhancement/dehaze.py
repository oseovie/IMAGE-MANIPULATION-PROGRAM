from PIL import ImageEnhance


def apply(image):
    return ImageEnhance.Contrast(image).enhance(1.18)

