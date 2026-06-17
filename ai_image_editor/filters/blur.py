from PIL import ImageFilter


def apply(image, radius=2):
    return image.filter(ImageFilter.GaussianBlur(radius=radius))

