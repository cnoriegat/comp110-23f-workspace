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

def sum1(vals: list[float]) -> float:
    """Using a while loop."""
    i: int = 0
    result: float = 0.0
    while i < (len(vals)):
        result += vals[i]
        i += 1
    return result

def sum2(vals: list[float]) -> float:
    """Using a for...in loop."""
    result: float = 0.0
    for elem in vals:
        result += elem
    return result

def sum3(vals: list[float]) -> float:
    """Using for...range loop."""
    result: float = 0.0
    for idx in range(len(vals)):
        result += vals[idx]
    return result

print(sum1([1.1, 0.9, 1.0]))
print(sum2([1.1, 0.9, 1.0]))
print(sum3([1.1, 0.9, 1.0]))