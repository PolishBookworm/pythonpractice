# Create a program that will play the “cows and bulls” game with the user. The game works like this:
# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number.
# For every digit that the user guessed correctly in the correct place, they have a “cow”.
# For every digit the user guessed correctly in the wrong place is a “bull.”
# Every time the user makes a guess, tell them how many “cows” and “bulls” they have.
# Once the user guesses the correct number, the game is over.
# Keep track of the number of guesses the user makes throughout the game and tell the user at the end.

# ! unsuscriptable--check the code !

# import random
# print('Welcome to cows and bulls!')
# num = random.randint(1,9999)
# while True:
#     guess = int(input('Guess my number\n'))
#     if guess == num:
#         print("That's right!")
#         break
#     else:
#         cows = 0
#         bulls = 0
#         for n in range(1,5):
#             if num[n] == guess[n]:
#                 cows += 1
#             for i in range(1,5):
#                 if num[i] == guess[n] and i != n:
#                     bulls += 1
#         print(cows + ' cows, ' + bulls + ' bulls.')

from random import sample

print("Welcome to cows and bulls!")

seq = "".join(sample("1234567890", 4))

while True:
    guess = input('Guess my 4-digit number:\n')
    if guess == seq:
        print("That's right!")
        break
    else:
        cows = 0
        bulls = 0
        for n in range(0,4):
            if seq[n] == guess[n]:
                cows += 1
            for i in range(0,4):
                if seq[i] == guess[n] and i != n:
                    bulls += 1
        print(f"You got {cows} cows and {bulls} bulls.\n")