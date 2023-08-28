from load_image import ft_load
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def main() -> int:
    array = ft_load('/home/yabdelgh/Desktop/animal.jpeg')
    array = array[100:500, 450:850]
    image = Image.fromarray(array).convert("L")
    array = np.array(image)

    # This code is only meant to satisfy the incomprehensible expected output.
    reshapedArray = array.reshape(array.shape[0], array.shape[1], 1)
    print(f'New shape after slicing: {reshapedArray.shape} or {array.shape}')
    print(reshapedArray)
    # end

    plt.imshow(reshapedArray, cmap="gray")
    plt.show()
    return 0

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)