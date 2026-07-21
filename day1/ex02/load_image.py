# from PIL import Image
# from numpy import array


# def ft_load(path: str) -> array or None:
#     try:
#         assert isinstance(path, str) and path != "", "Error: bad argument"
#         image = Image.open(path)
#         npImage = array(image)
#         print(f"The shape of image is {npImage.shape}\n{npImage}")
#         return npImage
#     except Exception as e:
#         return e


import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """
    Load an image from a file and return its pixel data as a numpy array.
    Supports JPG and JPEG formats.
    Args:
        path: path to the image file
    Returns:
        numpy array of shape (height, width, channels) with RGB values
    Raises:
        FileNotFoundError: if the file does not exist
        ValueError: if the file is not a JPG/JPEG image
    """
    try:
        img = Image.open(path)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {path}")
    except Exception as e:
        raise ValueError(f"Could not open image: {e}")

    # Check format
    if img.format not in ("JPEG", "JPG"):
        raise ValueError("Only JPG/JPEG formats are supported")

    # Convert to RGB if not already
    if img.mode != "RGB":
        img = img.convert("RGB")

    # Convert to numpy array
    arr = np.array(img)
    print(f"The shape of image is: {arr.shape}")
    return arr


def main():
    print(ft_load("landscape.jpg"))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
