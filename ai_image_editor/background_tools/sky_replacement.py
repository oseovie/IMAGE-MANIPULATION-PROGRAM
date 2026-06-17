from ai_image_editor.ai.base import require_model


def apply(image, sky_image=None):
    require_model("Sky replacement segmentation")

