from ai_image_editor.ai.base import require_model


def apply(image, mask):
    require_model("Content-aware fill")

