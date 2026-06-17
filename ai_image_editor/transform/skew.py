def apply(image, xshift=0):
    return image.transform(image.size, method=2, data=(1, xshift, 0, 0, 1, 0))

