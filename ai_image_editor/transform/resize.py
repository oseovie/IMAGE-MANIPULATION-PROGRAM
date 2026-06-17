def apply(image, width=None, height=None, percent=None):
    if percent is not None:
        width = int(image.width * percent / 100)
        height = int(image.height * percent / 100)
    if width is None or height is None:
        raise ValueError("width and height are required")
    return image.resize((width, height))

