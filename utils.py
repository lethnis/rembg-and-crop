import numpy as np
from PIL import Image
from io import BytesIO


def get_coordinates(arr: np.array) -> tuple:

    height = arr.shape[0]
    width = arr.shape[1]

    for i in range(height):
        row = arr[i]
        if not (row == 0).all():
            upper = i
            break

    for i in range(height):
        row = arr[-i - 1]
        if not (row == 0).all():
            lower = height - i
            break

    for i in range(width):
        row = arr[:, i]
        if not (row == 0).all():
            left = i
            break

    for i in range(width):
        row = arr[:, -i - 1]
        if not (row == 0).all():
            right = width - i
            break

    return left, upper, right, lower


def crop(img: Image) -> Image:
    arr = np.array(img)
    return img.crop(get_coordinates(arr))


def prepare_to_save(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()
