"""Wordle"""

__author__ = "730670964"


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
"""YELLOW_BOX does not look yellow but I copied the color code from the instructions"""


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop.
    variable turn is makes the while loop simple"""

    turn = 1
    correct_guess = False
    game_over = 6

    while turn <= game_over and not correct_guess:
        print(f"=== Turn {turn}/6 ===")

        guess = input_guess(len(secret))
        emoji = emojified(guess, secret)
        print(emoji)

        if guess == secret:
            print(f"You won in {turn}/6 turns!")
            correct_guess = True
        else:
            turn = turn + 1
        """ends the game if the guess is correct
        if not it progresses towards game_over (6 turns)"""

    if not correct_guess:
        print("X/6 - Sorry, try again tomorrow!")
        "if turn > 6 and correct_guess is false, print the game over message"


def contains_char(word: str, letter: str) -> bool:
    """does the guess have a character match with the secret?"""
    assert len(letter) == 1, f"len('{letter}') is not 1"

    index = 0
    while index < len(word):
        if word[index] == letter:
            return True
        index = index + 1

    return False


def emojified(guess: str, secret: str) -> str:
    """turns the guess into boxes indicating correctness.
    white for no connection,
    yellow for character in word
    green for correct character and position.
    """
    assert len(guess) == len(secret), """Guess must be same length as secret"""

    emoji = ""
    index = 0

    while index < len(guess):
        if guess[index] == secret[index]:
            emoji = emoji + GREEN_BOX
        elif contains_char(secret, guess[index]):
            emoji = emoji + YELLOW_BOX
        else:
            emoji = emoji + WHITE_BOX
        index = index + 1
    return emoji


def input_guess(expected_length: int) -> str:
    "ensure length of guess matches length of secret"

    guess = input(f"Enter a {expected_length} character word:")

    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again:")

    return guess


if __name__ == "__main__":
    main(secret="codes")
