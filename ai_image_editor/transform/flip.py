from PIL import Image


def horizontal(image):
    return image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)


def vertical(image):
    return image.transpose(Image.Transpose.FLIP_TOP_BOTTOM)

