from ai_image_editor.ai.base import require_model


def apply(image, *args, **kwargs):
    require_model('motion blur effect')
