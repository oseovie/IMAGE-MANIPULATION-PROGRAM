from PIL import ImageFilter


def apply(image, radius=1.2):
    return image.filter(ImageFilter.SMOOTH_MORE).filter(ImageFilter.GaussianBlur(radius=radius))

