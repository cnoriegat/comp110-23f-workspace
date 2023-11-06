"""Dictionary Functions."""


__author__ = "730621572"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Given a dictionary, invert the keys and the values."""
    result: dict[str, str] = {}

    for key in input:
        if input[key] in result:
            raise KeyError("Duplicate keys are not accepted.")
        
        value: str = input[key]
        result[value] = key

    return result


def favorite_color(fav_color: dict[str, str]) -> str:
    """Returns the color that appears most frequently in a dictionary."""
    color_count: dict[str, int] = {}

    for key in fav_color:
        color = fav_color[key]
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1

    pop_color_ins: int = 0
    pop_color: str = ""

    for key in color_count:
        if color_count[key] > pop_color_ins:
            pop_color_ins = color_count[key]
            pop_color = key
    
    return pop_color


def count(input: list[str]) -> dict[str, int]:
    """Counting the frequencies of each value in a list."""
    result: dict[str, int] = {}

    for elem in input:
        if elem in result:
            result[elem] += 1
        else:
            result[elem] = 1
    
    return result


def alphabetizer(input: list[str]) -> dict[str, list[str]]:
    """Function that alphabetizes list."""
    alpha: dict[str, list[str]] = {}
    
    for elem in input:
        elem_check = elem.lower()
        chr1: str = elem_check[0]

        if chr1 in alpha:
            alpha[chr1].append(elem)
        else: 
            new_list: list[str] = [elem]
            alpha[chr1] = new_list
    
    return alpha


def update_attendance(att: dict[str, list[str]], day: str, stu: str) -> dict[str, list[str]]:
    """Dictionary updating student attendance during the week."""
    if day in att:
        if stu not in att[day]:
            att[day].append(stu)
    else:
        new_list: list[str] = [stu]
        att[day] = new_list
    
    return att