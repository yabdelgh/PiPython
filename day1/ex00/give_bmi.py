import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    npH = np.array(height)
    npW = np.array(weight)
    assert npH.shape == npW.shape, "bad arguments"
    assert np.issubdtype(npH.dtype, np.number), "bad arguments"
    assert np.issubdtype(npW.dtype, np.number), "bad arguments"
    return list(npW / (npH * npH))


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    npBmi = np.array(bmi)
    return list(npBmi > limit)
