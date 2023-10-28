"""Combining two lists into a dictionary."""


__author__ = "730621572"


def zip(list1: list[str], list2: list[int]) -> dict[str, int]:
    """Function to combine lists into a dictionary."""
    result: dict[str, int] = dict()
    if len(list1) != len(list2) or (list1 == list()) or (list2 == list()):
        return dict()
    else:
        for idx in range(0, len(list1)):
            key: str = list1[idx]
            value: int = list2[idx]
            result[key] = value
    return result

print(zip(["Happy", "Tuesday"],[1,2]))