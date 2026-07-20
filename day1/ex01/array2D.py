def slice_me(family, start: int, end: int) -> list:
    """
    Slice a 2D array (list of lists) and print its original and new shape.
    Args:
        family: a 2D list (list of lists)
        start: start index for slicing rows
        end: end index for slicing rows
    Returns:
        sliced 2D list
    Raises:
        TypeError: if family is not a list or rows are not lists.
        ValueError: if rows have inconsistent lengths.
    """
    if not isinstance(family, list):
        raise TypeError("family must be a list")
    if not all(isinstance(row, list) for row in family):
        raise TypeError("Each row must be a list")
    if not family:
        print("My shape is : (0, 0)")
        return []
    row_len = len(family[0])
    if not all(len(row) == row_len for row in family):
        raise ValueError("All rows must have the same length")
    print(f"My shape is : ({len(family)}, {row_len})")
    sliced = family[start:end]
    if not sliced:
        print("My new shape is : (0, 0)")
        return []
    new_row_len = len(sliced[0])
    print(f"My new shape is : ({len(sliced)}, {new_row_len})")
    return sliced


def main():
    family = ([1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2])
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
