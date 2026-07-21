from PIL import Image
from numpy import array
import matplotlib.pyplot as plt


def main():
    """
    Docstring for main
    """
    img = Image.open("animal.jpeg")
    img = img.crop((400, 100, 800, 500)).convert("L")
    arr = array(img).reshape(img.size[0], img.size[1], 1)
    print(f"The shape of image is: {arr.shape} or {img.size}\n{arr[:2, :2]}")
    tArr = arr.copy()
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            tArr[j][i] = arr[i][j]
    tArr = tArr.squeeze(axis=2)
    print(f"The shape after Transpose: {tArr.shape}\n{tArr[:2, :2]}")
    plt.imshow(tArr, cmap="gray")
    plt.show()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
