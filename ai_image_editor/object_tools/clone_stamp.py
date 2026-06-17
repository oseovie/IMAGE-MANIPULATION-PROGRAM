def apply(image, source_box, target_xy):
    patch = image.crop(source_box)
    result = image.copy()
    result.paste(patch, target_xy)
    return result

