from ai_image_editor.ai.base import require_model


def enhance(image):
    require_model("Zero-DCE low-light enhancement", "ai/low_light/model")

