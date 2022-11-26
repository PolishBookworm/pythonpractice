# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
num = int(input('Give me a number\n'))
divisors = []
for n in range(1, num+1):
    if n % num == 0:
        divisors.append(n)
print(divisors)