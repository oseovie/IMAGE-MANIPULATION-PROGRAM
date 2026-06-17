from PIL import ImageEnhance
from .sepia import apply as sepia


def apply(image):
    result = sepia(image)
    result = ImageEnhance.Contrast(result).enhance(0.92)
    return ImageEnhance.Color(result).enhance(0.85)

