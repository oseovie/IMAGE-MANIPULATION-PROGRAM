from ai_image_editor.ai.base import require_model


def restore(image, fidelity=0.7):
    require_model("CodeFormer face restoration", "ai/face_restoration/model")

