from ai_image_editor.core.image_saver import save_image


def process(images, output_paths, quality=90):
    return [save_image(image, path, quality=quality) for image, path in zip(images, output_paths)]

