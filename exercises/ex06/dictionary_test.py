"""Testing Dictionary Functions."""


__author__ = "730621572"


# importing my dictionary functions
from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance


# testing invert function
def test_empty_invert() -> None:
    """Edge case testing - invert({}) should return empty dictionary."""
    assert invert({}) == {}


def test_short_dict() -> None:
    """Use case testing - testing on a single value pair."""
    test_dict: str = {"Hola": "Hello"}
    assert invert(test_dict) == {"Hello": "Hola"}


def test_long_dict() -> None:
    """Use case testing - testing on multiple value pairs."""
    test_dict: str = {"Luna": "Moon", "Cielo": "Sky", "Mar": "Sea", "Sol": "Sun", "Montañas": "Mountains"}
    assert invert(test_dict) == {"Moon": "Luna", "Sky": "Cielo", "Sea": "Mar", "Sun": "Sol", "Mountains": "Montañas"}


# testing favorite_color function
def test_empty_color() -> None:
    """Edge case testing - favorite_color({}) should return empty dictionary."""
    assert favorite_color({}) == ""


def test_compound_colors() -> None:
    """Use case testing - testing using compund color names."""
    test_dict: str = {"Mia": "Light blue", "Cate": "Blue", "Nico": "Navy blue", "Gus": "Light blue"}
    assert favorite_color(test_dict) == "Light blue"


def test_tie() -> None:
    """Use case testing - testing with tie."""
    test_dict: str = {"Mia": "Light blue", "Lia": "Magenta", "Cate": "Navy Blue", "Nico": "Navy blue", "Gus": "Light blue"}
    assert favorite_color(test_dict) == "Light blue"


# testing count function
def test_empty_count() -> None:
    """Edge case testing - count([]) should return empty dictionary."""
    assert count([]) == {}


def test_repeat_value() -> None:
    """Use case testing - testing with same value."""
    test_list: str = ["Sea", "Sea", "Sea", "Sea", "Sea",]
    assert count(test_list) == {"Sea": 5}


def test_dif_values() -> None:
    """Use case testing - testing with different values."""
    test_list: str = ["Sea", "Ocean", "Lake", "Pool"]
    assert count(test_list) == {"Sea": 1, "Ocean": 1, "Lake": 1, "Pool": 1}


# testing alphabetizer function
def test_empty_alpha() -> None:
    """Edge case testing - alphabetizer([]) should return empty dictionary."""
    assert alphabetizer([]) == {}


def test_capitalized() -> None:
    """Use case testing - testing with capitalized values."""
    test_list: list[str] = ["SEA", "OCEAN", "LAKE", "POOL", "SAND", "BEACH", "SEA"]
    assert alphabetizer(test_list) == {"s": ['sea', 'sand', 'sea'], "o": ['ocean'], "l": ['lake'], "p": ['pool'], "b": ['beach']}


def test_case_2() -> None:
    """Use case testing - no duplicate first letters."""
    test_list: list[str] = ["Sea", "Ocean", "Lake", "Pool"]
    assert alphabetizer(test_list) == {"s": ['sea'], "o": ['ocean'], "l": ['lake'], "p": ['pool']}


# testing update_attendance function
def test_empty_dict() -> None:
    """Edge case testing - attendance({}, "", "") should return empty dictionary."""
    assert update_attendance({}, "", "") == {'': ['']}


def test_no_att() -> None:
    """Use case testing - no attendance on Friday."""
    test_dict: dict[str] = {"Monday": ["Harry"], "Tuesday": ["Ron"], "Wednesday": ["Hermionie"], "Thursday": ["Neville"]}
    assert update_attendance(test_dict, "Friday", "") == {'Monday': ['Harry'], 'Tuesday': ['Ron'], 'Wednesday': ['Hermionie'], 'Thursday': ['Neville'], 'Friday': ['']}


def test_case_1() -> None:
    """Use case testing - no attendance on Monday."""
    test_dict: dict[str] = {}
    assert update_attendance(test_dict, "Tuesday", "Hermionie") == {'Tuesday': ['Hermionie']}