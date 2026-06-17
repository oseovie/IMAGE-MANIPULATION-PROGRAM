from ai_image_editor.enhancement.sharpen import apply as sharpen


def process(images):
    return [sharpen(image) for image in images]

