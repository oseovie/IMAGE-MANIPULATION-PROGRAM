class FeatureUnavailable(RuntimeError):
    """Raised when an optional AI model or dependency is not installed."""


def require_model(feature_name, model_path=None):
    target = f" at {model_path}" if model_path else ""
    raise FeatureUnavailable(
        f"{feature_name} is scaffolded but needs its model/dependencies{target} before it can run."
    )
