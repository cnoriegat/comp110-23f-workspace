"""Structured Wordle."""


__author__ = "730621572"


def contains_char(word_input: str, char: str) -> bool:
    """Check if word input contains character."""
    assert len(char) == 1
    idx: int = 0
    result: bool = False
    while idx < len(word_input):
        if word_input[idx] == char:
            result = True
        idx += 1
    return result


def emojified(guess: str, secret: str) -> str:
    """Print emoji string based on guess."""
    assert len(guess) == len(secret)
    result: str = ""
    white_box: str = "\U00002B1C"
    green_box: str = "\U0001F7E9"
    yellow_box: str = "\U0001F7E8"
    idx: int = 0
    while idx < len(secret):
        if guess[idx] == secret[idx]:
            result += green_box
        elif contains_char(secret, guess[idx]) is True:
            result += yellow_box
        else:
            result += white_box
        idx += 1
    return result


def input_guess(exp_len: int) -> str:
    """Prompt users until correct length."""
    word_guess: str = input(f"Enter a {exp_len} character word: ")
    while len(word_guess) != exp_len:
        word_guess = input(f"That wasn't {exp_len} chars! Try again: ")
    return word_guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    num_turns: int = 1
    max_turns: int = 6
    win: bool = False
    while num_turns <= max_turns and not win:
        print(f"=== Turn {num_turns}/{max_turns} ===")
        word_guess: str = input_guess(len(secret_word))
        print(emojified(word_guess, secret_word))
        if secret_word == word_guess:
            print(f"You won in {num_turns}/{max_turns} turns!")
            win = True
        num_turns += 1
    if not win:
        print(f"X/{max_turns} - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()