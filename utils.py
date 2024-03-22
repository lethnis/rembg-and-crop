import numpy as np
import PIL
from io import BytesIO


def get_coordinates(arr: np.array) -> tuple:
    """Helper function for crop function. Takes an image as np.array and looks
    through every side for non-empty lines"""

    height = arr.shape[0]
    width = arr.shape[1]

    # looks from top to bottom until finds non-empty line
    for i in range(height):
        row = arr[i]
        if not (row == 0).all():
            upper = i
            break

    # looks from bottom to top until finds non-empty line
    for i in range(height):
        row = arr[-i - 1]
        if not (row == 0).all():
            lower = height - i
            break

    # looks from left to right until finds non-empty line
    for i in range(width):
        row = arr[:, i]
        if not (row == 0).all():
            left = i
            break

    # looks from right to left until finds non-empty line
    for i in range(width):
        row = arr[:, -i - 1]
        if not (row == 0).all():
            right = width - i
            break
    
    # returns lines indexes in order that PIL requires
    return left, upper, right, lower


def crop(img: PIL.Image) -> PIL.Image:
    """Crop empty edges by coordinates"""
    arr = np.array(img)
    return img.crop(get_coordinates(arr))


def prepare_to_save(img: PIL.Image) -> BytesIO:
    """Preparing image for saving"""
    buf = BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()


def main():
    pass


if __name__ == "__main__":
    main()