from ai_image_editor.ai.base import require_model


def restore(image):
    require_model("GFPGAN face restoration", "ai/face_restoration/model")

