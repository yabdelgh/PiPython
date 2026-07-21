from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array: np.ndarray) -> np.ndarray:
    """
    Inverts the color of the image received.
    Allowed operators: =, +, -, *
    """
    inverted = 255 - array
    return inverted


def ft_red(array: np.ndarray) -> np.ndarray:
    """
    Applies a red filter to the image.
    Allowed operators: =, *
    """
    red = array.copy()
    red[:, :, 1] = 0  # green
    red[:, :, 2] = 0  # blue
    return red


def ft_green(array: np.ndarray) -> np.ndarray:
    """
    Applies a green filter to the image.
    Allowed operators: =, -
    """
    green = array.copy()
    green[:, :, 0] = 0  # red
    green[:, :, 2] = 0  # blue
    return green


def ft_blue(array: np.ndarray) -> np.ndarray:
    """
    Applies a blue filter to the image.
    Allowed operators: =
    """
    blue = array.copy()
    blue[:, :, 0] = 0  # red
    blue[:, :, 1] = 0  # green
    return blue


def ft_grey(array: np.ndarray) -> np.ndarray:
    """
    Converts the image to grayscale by taking the green channel and replicating it.
    Allowed operators: =, /
    """
    grey = array.copy()
    green = grey[:, :, 1]
    grey[:, :, 0] = green
    grey[:, :, 2] = green
    return grey


def display_image(arr, title):
    """
    Docstring for display_image

    :param arr: Description
    :param title: Description
    """
    plt.imshow(arr)
    plt.title(title)
    plt.axis("off")
    plt.show()


def main():
    """
    Docstring for main
    """
    try:
        arr = ft_load("landscape.jpg")
        print(arr[:5, :5])

        display_image(arr, "Original")
        filters = [ft_invert, ft_red, ft_green, ft_blue, ft_grey]
        titles = ["Invert", "Red", "Green", "Blue", "Grey"]
        for func, title in zip(filters, titles):
            filtered = func(arr)
            print(f"{title}: {func.__doc__}")
            display_image(filtered, title)

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
