"""EX02 - One-Shot Wordle"""

__author__ = "730621572"

secret_word: str = "python"
word_guess: str = input(f"What is your {len(secret_word)}-letter guess? ")

white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"

idx: int = 0
result: str = ""

# prompting for guess
while len(word_guess) != len(secret_word):
    word_guess = input(f"That was not {len(secret_word)} letters! Try again: " )

# emoji output (green, yellow, white)
while idx < len(secret_word):
    if word_guess[idx] == secret_word[idx]:
        result += green_box
    else:
        chr_found: bool = False 
        alt_idx: int = 0
        while not chr_found and (alt_idx < len(secret_word)):
          if word_guess[idx] == secret_word[alt_idx]:
            chr_found = True
          else:
            alt_idx += 1
        if chr_found == True:
            result += yellow_box 
        else:
            result += white_box  
    idx += 1     
print(result)

# game ending - correct or incorrect answers
if len(word_guess) == len(secret_word):
    if word_guess == secret_word:
        print("Woo! You got it!")
        exit()
    elif len(word_guess) == len(secret_word):
        print("Not quite. Play again soon!")
        exit()