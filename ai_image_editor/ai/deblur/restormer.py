from ai_image_editor.ai.base import require_model


def deblur(image):
    require_model("Restormer deblur", "ai/deblur/model")

