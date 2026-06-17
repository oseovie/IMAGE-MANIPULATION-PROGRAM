from ai_image_editor.ai.base import require_model


def detect(image):
    require_model("YOLO object detection", "ai/object_detection/model")

