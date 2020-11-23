# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
multiples_three = [num for num in range(1, 101) if num % 3 == 0]
print(multiples_three)
multiples_five = [num for num in range(1, 101) if num % 5 == 0]
print(multiples_five)
multiples = set(multiples_five + multiples_three)
print(multiples)
result = sum(multiples)
print(result)