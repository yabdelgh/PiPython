def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """
    Calculate BMI for each pair of height and weight.
    Args:
        height: list of heights (int/float)
        weight: list of weights (int/float)
    Returns:
        list of BMI values (float)
    Raises:
        ValueError: if lists have different lengths or contain non-numeric types.
    """
    if len(height) != len(weight):
        raise ValueError("Height and weight lists must have the same length.")
    if not all(isinstance(x, (int, float)) for x in height) or \
       not all(isinstance(x, (int, float)) for x in weight):
        raise ValueError("All elements must be int or float.")
    return [w / (h ** 2) for h, w in zip(height, weight)]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Apply a limit to a list of BMI values.
    Args:
        bmi: list of BMI values (int/float)
        limit: integer threshold
    Returns:
        list of booleans: True if bmi > limit, else False
    """
    return [b > limit for b in bmi]


def main():
    # Test code
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


if __name__ == "__main__":
    main()

# import numpy as np


# def give_bmi(height: list[int | float],
#              weight: list[int | float]) -> list[int | float]:
#     npH = np.array(height)
#     npW = np.array(weight)
#     assert npH.shape == npW.shape, "bad arguments"
#     assert np.issubdtype(npH.dtype, np.number), "bad arguments"
#     assert np.issubdtype(npW.dtype, np.number), "bad arguments"
#     return list(npW / (npH * npH))


# def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
#     npBmi = np.array(bmi)
#     return list(npBmi > limit)