from PIL import ImageOps


def apply(image):
    alpha = image.getchannel("A") if image.mode == "RGBA" else None
    result = ImageOps.grayscale(image).convert("RGBA")
    if alpha:
        result.putalpha(alpha)
    return result

