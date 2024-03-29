# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.

import random

while True:
    num = random.randint(1,9)
    while True:
        guess = int(input('Guess my number (1-9)\n'))
        if num == guess:
            print("That's right!")
            break
        elif num > guess:
            print("That's a bit too low")
        else:
            print("Nice try, but that's too high.")
    if input('If you want to stop type "exit". If not just click "enter"\n') == 'exit':
        break