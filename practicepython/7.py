import random

num_list = []
list_length = random.randint(5,15)
while len(num_list) < list_length:
    num_list.append(random.randint(1,75))

even_list = [num for num in num_list if num % 2 == 0]
print(num_list)
print(even_list)