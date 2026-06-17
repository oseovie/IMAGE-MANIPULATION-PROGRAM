from PIL import ImageEnhance


def apply(image):
    return ImageEnhance.Sharpness(image).enhance(1.2)

