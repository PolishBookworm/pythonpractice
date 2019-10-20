num = int(input('Give me a number\n'))
divisors = [n for n in range(1, num) if num % n == 0]
if num > 1
    if len(divisors) == 0:
        prime = True
    else:
        prime = False
else:
    prime = False
if prime:
    print(str(num) + ' is prime')
else:
    print(str(num) + ' is not prime')