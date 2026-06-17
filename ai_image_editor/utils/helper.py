def clamp(value, low=0, high=255):
    return max(low, min(high, value))
