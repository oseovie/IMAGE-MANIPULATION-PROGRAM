def read_metadata(image):
    return {
        "mode": image.mode,
        "width": image.width,
        "height": image.height,
        "resolution": f"{image.width} x {image.height}",
    }
