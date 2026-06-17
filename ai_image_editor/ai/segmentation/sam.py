from ai_image_editor.ai.base import require_model


def segment(image, prompt=None):
    require_model("Segment Anything segmentation", "ai/segmentation/model")

