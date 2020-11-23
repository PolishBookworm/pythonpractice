def num_divisors(n):
  for i in range(n):
    x = len([i for i in range(1,n+1) if not n % i])
  return x

num = int(input('Give me a number\n'))
if num_divisors(num) == 2:
    print(str(num) + ' is prime')
else:
    print(str(num) + ' is not prime')