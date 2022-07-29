# Condition inside print()

print("odd" if int(input("Enter a num: ")) % 2 else "even")

# Conditional lists: all() and any()

a = 1
b = 2
c = 3

conds = [a > 1, b == 2, c % 3 == 0]

print("All good!" if all(conds) else "Something's wrong")

print("Yes!" if any(conds) else "No!")

# Multiple inputs in one go

a, b, c = input("Enter three inputs ").split()

# Swapping

a = 1
b = 2

a, b = b, a
print(a)

# Take out the duplicate data

li = [1, 5, 8, 6, 5, 9, 6, 9, 5, 6, 9, 6, 5, 4]
print(list(set(li)))

# Table of element occurrences

li = [
    1,
    5,
    8,
    6,
    5,
    9,
    6,
    9,
    5,
    6,
    9,
    6,
    5,
    4,
    "a",
    "a",
    "b",
    "b",
    "a",
    "a",
    "a"]
di = {k: li.count(k) for k in li}

# List comprehensions (or generator comprehensions, to save memory)

li = [i**3 for i in range(1, 15) if i % 2 == 0]

# *args and **kwargs

# Reversing

name = "Frodo Baggins"
reverse = name[::-1]

# Concatenating

arr = ['H', 'e', 'l', 'l', 'o']
result = "".join(arr)

# counter(): counts frequency of each unique object in iterable

li = [1, 1, 1, 1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 6, 6, 6, 6]
print(Counter(li))

# List of numbers of unknown length

entered_list = input("Enter a list of numbers separated by space: ").split()
print('Intermediate_list: ', entered_list)

num_list = list(map(int, entered_list))
print('Number List: ', num_list)
print('List sum:', sum(num_list))

# Two-way comparisons

if 1 < x < 10:
    pass

# min() and max()

# get() in dictionaries

# enumerate() in for loops (when in need of indices)

# Masking password input

from pwinput import pwinput

pw = pwinput()
pw = pwinput(mask='X') # Change the mask character.
pw = pwinput(prompt='PW: ', mask='*') # Change the prompt.
pw = pwinput(mask='') # Don't display anything.