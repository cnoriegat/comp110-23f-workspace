"""Practice with Loops."""

from random import randint

secret: int = randint(0,10)
guess: int = int(input("Guess a number between 1 and 10: "))
num_tries: int = 0
max_tries: int = 2

while (guess != secret) and (num_tries < max_tries):
    print("Wrong")
    # if guess is too low, tell them:
    if (guess < 1) or (guess > 10):
        print("That's not between 1 and 10!")
    if guess < secret:
        print("Too low")
    # if guess is too high, tell them:
    else:
        print("Too high")
    # ask for a different guess
    print(f"Remaining tries: {max_tries - num_tries}")
    guess = int(input("Guess again: "))
    num_tries += 1
# if you've reached this point, guess == secret OR you ran out of tries
if guess == secret:
    print("You guessed correctly!")
else:
    print("You lose :(")
print(f"The number was {secret}")