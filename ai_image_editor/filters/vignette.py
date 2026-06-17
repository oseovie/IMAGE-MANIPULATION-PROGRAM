from PIL import Image, ImageDraw, ImageFilter


def apply(image, strength=0.55):
    overlay = Image.new("RGBA", image.size, (0, 0, 0, 0))
    mask = Image.new("L", image.size, 0)
    draw = ImageDraw.Draw(mask)
    w, h = image.size
    draw.ellipse((-w * 0.15, -h * 0.10, w * 1.15, h * 1.10), fill=255)
    mask = Image.eval(mask.filter(ImageFilter.GaussianBlur(max(w, h) // 8)), lambda px: 255 - px)
    overlay.putalpha(mask.point(lambda px: int(px * strength)))
    return Image.alpha_composite(image.convert("RGBA"), overlay)

