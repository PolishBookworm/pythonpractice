#RAW
number = int(input('A number, please\n'))
if number % 2 == 0:
    even = True
else:
    even = False
if even:
    print(str(number) + ' is even')
else:
    print(str(number) + ' is odd')
#EXTRA 1
if number % 4 == 0:
    multiple = True
else:
    multiple = False
if multiple:
    print(str(number) + ' is a multiple of 4')
else:
    print(str(number) + ' is not a multiple of 4')
#EXTRA 2
num = int(input("I'd like a number, please\n"))
check = int(input('And another one\n'))
if num % check == 0:
    multiple2 = True
else:
    multiple2 = False
if multiple2:
    print(str(num) + ' is a multiple of ' + str(check))
else:
    print(str(num) + ' is not a multiple of ' + str(check))