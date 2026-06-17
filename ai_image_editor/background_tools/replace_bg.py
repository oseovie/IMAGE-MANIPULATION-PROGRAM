from PIL import Image


def with_color(image, color=(255, 255, 255)):
    bg = Image.new("RGBA", image.size, color + (255,))
    return Image.alpha_composite(bg, image.convert("RGBA"))

