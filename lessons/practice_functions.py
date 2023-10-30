"""Question 1: Code Writing."""

def odd_and_even(input: list[int]) -> list[int]:
    new_list: list[int] = []

    for idx in range (0, len(input)):
        elem: int = input[idx]
        
        if (elem % 2 != 0) and (idx % 2 == 0):
            new_list.append(elem)

    return new_list

def value_exists(input: dict[str, int], value: int) -> bool:
    """Function checks if value exists in dictionary."""

    for key in input:
        if input[key] == value:
            return True
    return False

def short_words(input: list[str]) -> list[str]:
    """Returns list of words that are shorter than 5 characters."""
    new_list: list[str] = []

    for word in input:
        if len(word) < 5:
            new_list.append(word)
        else:
            print(f"{word} is too long!")
    return new_list

def contains_substring(words:list[str], substring: str) -> list[str]:
    """Function that returns words that include substring."""
    new_list: list[str] = []

    for word in words:
        if substring in word:
            new_list.append(word)
    return new_list

def find_max_length(words: list[str]) -> int:
    """Return the maximum length of a word in the list."""
    max_len: int = 0

    for word in words:
        if len(word) > max_len:
            max_len = len(word)
    return max_len

def get_even_numbers(numbers: list[int]) -> list[int]:
    """Return new list containing even numbers."""

    even_list: list[int] = []
    for num in numbers:
        if num % 2 == 0:
            even_list.append(num)
    return even_list

def count_vowels(text:str) -> int:
    """Return number of vowels in the text."""
    num_vowels: int = 0

    for idx in range(0, len(text)):
        if "a" == text[idx] or "e" == text[idx] or "i" == text[idx] or "o" == text[idx] or "u" == text[idx]:
            num_vowels += 1
    return num_vowels

def count_vowels2(text:str) -> int:
    """Return number of vowels in the text."""
    num_vowels: int = 0

    for elem in text:
        if elem.lower() in "aeiou":
            num_vowels += 1
    return num_vowels

text = "Hello, how are you?"
print(count_vowels(text))

text = "Hello, how are you?"
print(count_vowels2(text))
