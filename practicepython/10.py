import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# list_length = random.randint(5,15)
# while len(a) < list_length:
#     a.append(random.randint(1,75))
# list_length = random.randint(5,15)
# while len(b) < list_length:
#     b.append(random.randint(1,75))

nums = [num for num in set(a) if num in b]
print(nums)