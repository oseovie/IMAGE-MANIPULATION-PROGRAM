from PIL import Image, ImageDraw, ImageFilter


def apply(image, radius=8):
    blurred = image.filter(ImageFilter.GaussianBlur(radius=radius))
    w, h = image.size
    mask = Image.new("L", image.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((int(w * 0.18), int(h * 0.12), int(w * 0.82), int(h * 0.9)), fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(max(18, min(w, h) // 18)))
    return Image.composite(image, blurred, mask)

