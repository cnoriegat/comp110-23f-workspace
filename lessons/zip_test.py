"""Test my zip function"""


__author__ = "730621572"


from lessons.zip import zip


def test_empty_lists() -> None:
    """Edge case testing - zip([]) should return empty dictionary."""
    assert zip([], []) == {}


def test_dif_len_lists() -> None:
    """Use case testing - lists of different lengths should return an empty dictionary."""
    test_list1: str = ["Hello", "COMP", "110"]
    test_list2: int = [1, 2, 3, 4]
    assert zip(test_list1, test_list2) == {}

def test_same_len_lists() -> None:
    """Use case testing - lists of same lengths should a dictionary with both lists."""
    test_list1: str = ["Happy", "Friday"]
    test_list2: int = [1, 2]
    assert zip(test_list1, test_list2) == {"Happy": 1, "Friday": 2}