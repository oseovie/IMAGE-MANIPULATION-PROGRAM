def apply(image, box):
    return image.crop(box)


def square_center(image):
    side = min(image.width, image.height)
    left = (image.width - side) // 2
    top = (image.height - side) // 2
    return image.crop((left, top, left + side, top + side))

