"""Utility Functions."""


__author__ = "730621572"


def all(input: list[int], num: int) -> bool:
    """Compare numbers in list to separate number."""
    if not input:
        return False
    idx: int = 0
    while idx < len(input):
        if input[idx] != num:
            return False
        idx += 1
    return True


def max(input: list[int]) -> int:
    """Return largest number."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    idx: int = 0
    max_value: int = input[0]
    while idx < len(input):
        if input[idx] > max_value:
            max_value = input[idx]
        idx += 1
    return max_value


def is_equal(input1: list[int], input2: list[int]) -> bool:
    """Compare if lists are identical."""
    idx: int = 0
    if len(input1) != len(input2):
        return False
    while idx < len(input1):
        if input1[idx] != input2[idx]:
            return False
        idx += 1
    return True