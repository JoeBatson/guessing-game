import random

COLORS = ["R", "G", "B", "Y", "W", "O"]
TRIES = 10
CODE_LENGTH = 4

def generate_code():
    code = []

    for i in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)

    return code

def guess_code():

    while True:
        guess = input("Guess: ").upper().strip().split(" ")

        if len(guess) != CODE_LENGTH:
            print(f"You must enter {CODE_LENGTH} colors.")
            continue
        
        for color in guess:
            if color not in COLORS:
                print(f'Invalid color: "{color}". Try again.')
                break

        else:
            break

    return guess

def check_code(guess, real_code):
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    # collecting how many times a color is in the real code.
    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0 # if color not in dictionary we need to add it - Dictionary_Name[New_Key_Name] = New_Key_Value
        color_counts[color] += 1  # increments the count for that color in the dictionary - Dictionary_Name[New_Key_Name] = New_Key_Value
    
    # colors in the correct position
    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_color:
            correct_pos += 1
            color_counts[guess_color] -= 1 # removes if in the correct position. Now it reflects how many are still in the incorrect position.
    # colors in the incorrect position
    for guess_color, real_color in zip(guess, real_code):
        if guess_color in color_counts and color_counts[guess_color] > 0:
            incorrect_pos += 1
            color_counts[guess_color] -= 1

    return correct_pos, incorrect_pos


def game():
    print(f"Welcome to mastermind, you have {TRIES} tries to guess the code...")
    print("The colors are", *COLORS) # the "*" in front of COLORS removes the brackets of the list and makes is plain text.

    code = generate_code()
    for attempts in range(1, TRIES + 1): # TRIES + 1 is because range is in bettween 1 and 10 but doesn't include 10 so we make it 11.
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)

        if correct_pos == CODE_LENGTH:
            print(f"You guessed the code in {attempts} tries!")
            break

        print(f"Correct positions: {correct_pos} | Incorrect positions: {incorrect_pos}")

    else: 
        print("You ran out of tries, the code was:", *code)


if __name__ == "__main__": # makes sure you're directly running the Python file.
    game()



