from random import randint
from ascii_art import ascii

print(ascii("Welcome to . . ."))
print(ascii("the Ultimate Guessing Game!"))

play_again = "y"
while play_again == "y":
    num = randint(1,10)
    guess = None
    while guess != num:
        try:
            guess = int(input("What's your guess? (1-10) "))
        except ValueError:
            print("Your guess must be a number!")
        else:
            if guess < num:
                print("Too low. Try again.")
            elif guess > num:
                print("Too high. Try again.")
    print("Correct!")
    play_again = input("Do you want to play again? (y/n) ")
    