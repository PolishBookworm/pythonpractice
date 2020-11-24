# RAW: Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
number = int(input('A number, please\n'))
if number % 2 == 0:
    print(str(number) + ' is even')
else:
    print(str(number) + ' is odd')

# EXTRA 1: If the number is a multiple of 4, print out a different message.
if number % 4 == 0:
    print(str(number) + ' is a multiple of 4')
else:
    print(str(number) + ' is not a multiple of 4')

# EXTRA 2: Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
num = int(input("I'd like a number, please\n"))
check = int(input('And another one\n'))
if num % check == 0:
    print(str(num) + ' is a multiple of ' + str(check))
else:
    print(str(num) + ' is not a multiple of ' + str(check))
