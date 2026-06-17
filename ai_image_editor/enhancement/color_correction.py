from PIL import ImageEnhance


def apply(image, color=1.05, contrast=1.05):
    return ImageEnhance.Contrast(ImageEnhance.Color(image).enhance(color)).enhance(contrast)

