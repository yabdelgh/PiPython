import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    assert isinstance(family, list) and isinstance(start, int) \
           and isinstance(end, int), "bad arguments"
    arr = np.array(family)
    print(f"My shape is : {arr.shape}")
    newArr = arr[start:end]
    print(f"My new shape is : {newArr.shape}")
    return [x.tolist() for x in newArr]
