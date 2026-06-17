from ai_image_editor.transform.resize import apply as resize


def process(images, width, height):
    return [resize(image, width=width, height=height) for image in images]

