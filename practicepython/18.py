import random
print('Welcome to cows and bulls!')
num = random.randint(1,9999)
while True:
    guess = int(input('Guess my number\n'))
    if guess == num:
        print("That's right!")
        break
    else:
        cows = 0
        bulls = 0
        for n in range(1,5):
            if num[n] == guess[n]:
                cows += 1
            for i in range(1,5):
                if num[i] == guess[n] and i != n:
                    bulls += 1
        print(cows + ' cows, ' + bulls + ' bulls.')