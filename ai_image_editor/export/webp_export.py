from ai_image_editor.core.image_saver import save_image


def export(image, path, quality=90):
    return save_image(image, path, quality=quality)

