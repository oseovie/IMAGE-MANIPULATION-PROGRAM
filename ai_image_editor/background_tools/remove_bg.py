from ai_image_editor.ai.base import require_model


def apply(image):
    require_model("Background removal", "rembg")

