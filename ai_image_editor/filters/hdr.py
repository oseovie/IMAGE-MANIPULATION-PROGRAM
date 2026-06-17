from PIL import ImageEnhance, ImageFilter


def apply(image):
    result = ImageEnhance.Contrast(image).enhance(1.25)
    result = ImageEnhance.Sharpness(result).enhance(1.35)
    return result.filter(ImageFilter.UnsharpMask(radius=1.5, percent=130, threshold=2))

