import random

COLORS = ["P", "W", "Y", "G", "B", "R"]
CODE_LENGTH = 4
TRIES = 5


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
    correct = 0
    wrong = 0
    for i in range(CODE_LENGTH):
        if secret_code[i] == guessed_code[i]:
            correct += 1
        else:
            wrong += 1
    return [correct, wrong]


print("Welcome to MasterMind! The available colors are R, B, G, W, Y, P.")
game_on = True
# Generating the secret code
secret_code = generate_code()
# Allowing the number of tries to the user.
for x in range(TRIES):
    guessed_code = guess_code()
    res = compare_code(secret_code, guessed_code)
    # If there are no wrong positions then game won.
    if res[1] == 0:
        print(f"Congrats! You cracked the code in {x+1} tries!")
        game_on = False
        break
    else:
        # Else printing the number of correct and wrong positions.
        print(f"Correct positions = {res[0]} | Wrong positions = {res[1]}")

# If user runs out of the number of tries, then the game is lost.
if game_on:
    print(f"You lost! You couldn't guess the secret code in {TRIES} tries.")
