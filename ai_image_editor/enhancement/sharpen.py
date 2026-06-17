from PIL import ImageFilter


def apply(image, radius=2, percent=165, threshold=3):
    return image.filter(ImageFilter.UnsharpMask(radius=radius, percent=percent, threshold=threshold))

