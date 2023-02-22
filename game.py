import random

COLORS = ["P", "W", "Y", "G", "B", "R"]
CODE_LENGTH = 4
TRIES = 10


def generate_code() -> list:
    '''Generates the secret code and returns the code as a list.'''
    code = []

    for _ in range(CODE_LENGTH):
        code.append(random.choice(COLORS))
    return code


def guess_code() -> list:
    '''Fetches the guessed code from the user and returns the code as a list.'''
    while True:
        print('Guess the colors:')
        # Ensuring that input is in capital letters and splitting into list.
        guessed_code = input().upper().split()

        if(len(guessed_code) != CODE_LENGTH):
            print(f"You need to guess {CODE_LENGTH} colors.")
            # This continue ensures that the user is prompted to guess again.
            continue

        # To ensure all the colors are in the allowed colors.
        for color in guessed_code:
            if color not in COLORS:
                print(
                    f"This {color} is not available. Please select the colors again.")
                break
        else:
            # Executes when the for loop runs completely and break statement inside if wasn't encountered.
            break

    return guessed_code


def compare_code(secret_code, guessed_code) -> list:
    '''Compares the code and returns the number of correct and wrong positions as a list.'''
    counts = {}
    correct = 0
    wrong = 0

    # Counting all the colors present in the secret code
    for color in secret_code:
        if color not in counts.keys():
            counts[color] = 0
        counts[color] += 1

    # Finding the correct positions
    for guess_color, secret_color in zip(guessed_code, secret_code):
        if guess_color == secret_color:
            correct += 1
            counts[guess_color] -= 1

    # Finding the incorrect positions
    for guess_color, secret_color in zip(guessed_code, secret_code):
        if guess_color in counts.keys() and counts[guess_color] > 0:
            wrong += 1
            counts[guess_color] -= 1

    return [correct, wrong]


def game():
    print("Welcome to MasterMind! The available colors are ", *COLORS)
    print(f"You have {TRIES} tries to guess the correct code.")
    # Generating the secret code
    secret_code = generate_code()

    # Allowing the number of tries to the user.
    for x in range(TRIES):
        guessed_code = guess_code()
        res = compare_code(secret_code, guessed_code)
        # If the number of correct positions is equal to the code length then game won.
        if res[0] == CODE_LENGTH:
            print(f"Congrats! You cracked the code in {x+1} tries!")
            break
        else:
            # Else printing the number of correct and wrong positions.
            print(f"Correct positions = {res[0]} | Wrong positions = {res[1]}")

    # If user runs out of the number of tries, then the game is terminated.
    else:
        print(
            f"You lost! You couldn't guess the secret code in {TRIES} tries.")
        print("The code was:", *secret_code)


game()
