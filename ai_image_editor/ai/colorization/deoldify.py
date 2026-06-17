from ai_image_editor.ai.base import require_model


def colorize(image):
    require_model("DeOldify colorization", "ai/colorization/model")

