import random

COLORS = ["P", "W", "Y", "G", "B", "R"]
CODE_LENGTH = 4


def generate_code():
    '''Generates the secret code and returns the code as a list.'''
    code = []

    for _ in range(CODE_LENGTH):
        code.append(random.choice(COLORS))
    return code


def guess_code():
    '''Fetches the guessed code from the user and returns the code as a list.'''
    print('Guess the colors:')
    # Ensuring that input is in capital letters and splitting into list.
    guessed_code = input().upper().split()

    return guessed_code


guess_code()
