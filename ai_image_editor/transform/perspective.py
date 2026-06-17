def apply(image, coefficients):
    return image.transform(image.size, method=0, data=coefficients)

