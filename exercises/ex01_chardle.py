"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730621572"

# prompting word
word_insert: str = input("Enter a 5-character word: ")
if len(word_insert) != 5:
    print("Error: Word must contain 5 characters")
    exit()

# prompting character
character_insert: str = input("Enter a single character: ")
if len(character_insert) != 1:
    print("Error: Character must be a single character.")
    exit()

# character match count
num_matches: int = 0

# early exit for invalid inputs
if len(word_insert) != 5:
    print("Error: Word must contain 5 characters")
    exit()

print("Searching for " + character_insert + " in " + word_insert)

# checking indices for matches
if character_insert == (word_insert[0]):
    print(character_insert + " found at index 0")
    num_matches = num_matches + 1

if character_insert == (word_insert[1]):
    print(character_insert + " found at index 1")
    num_matches = num_matches + 1

if character_insert == (word_insert[2]):
    print(character_insert + " found at index 2")
    num_matches = num_matches + 1

if character_insert == (word_insert[3]):
    print(character_insert + " found at index 3")
    num_matches = num_matches + 1

if character_insert == (word_insert[4]):
    print(character_insert + " found at index 4")
    num_matches = num_matches + 1

# matching indices
if num_matches == 0:
    print("No instances of " + character_insert + " found in " + word_insert)

if num_matches == 1:
    print(str(num_matches) + " instance of " + character_insert + " found in " + word_insert)

if num_matches > 1:
    print(str(num_matches) + " instances of " + character_insert + " found in " + word_insert)