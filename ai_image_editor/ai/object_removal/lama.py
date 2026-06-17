from ai_image_editor.ai.base import require_model


def remove(image, mask):
    require_model("LaMa object removal", "ai/object_removal/model")

