from ai_image_editor.ai.base import require_model


def apply(image, style="natural"):
    require_model(f"Makeup effect: {style}")

