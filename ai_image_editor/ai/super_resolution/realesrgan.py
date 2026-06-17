from ai_image_editor.ai.base import require_model


def upscale(image, scale=2):
    require_model(f"Real-ESRGAN {scale}x super resolution", "ai/super_resolution/model")

