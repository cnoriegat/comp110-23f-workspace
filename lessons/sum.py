"""Summing the elements of a list using different loops."""


__author__ = "730621572"


def w_sum(vals: list[float]) -> float:
    """Sum of all elements using while loops."""
    idx: int = 0
    sum: float = 0.0
    while idx < len(vals):
        sum += vals[idx]
        idx += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Sum of all elements using for loops."""
    sum: float = 0.0
    for elem in vals:
        sum += elem
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Sum of all elements using for loops and range."""
    sum: float = 0.0
    for elem in range(len(vals)):
        sum += vals[elem]
    return sum

my_list = ["w", "x", "y", "z"]

for idx in range(0, len(my_list)):
    print(idx)