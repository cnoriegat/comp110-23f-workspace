"""Dictionary Functions."""


__author__ = "730621572"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Given a dictionary, invert the keys and the values."""
    result: dict[str, str] = {}
    for key in input:
        value: str = input[key]
        if value in result.values(): # DOES NOT WORK
            raise KeyError(f"Duplicate value: {value}")
        else:
            result[value] = key
    
    return result

def favorite_color(fav_color: dict[str, str]) -> str:
    """Returns the color that appears most frequently in a dictionary."""
    pop_color: str = ""
    

    for keys in favorite_color:
