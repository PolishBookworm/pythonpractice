# Write a program that takes a list of numbers and makes a new list of only the first and last elements of the given list.

def beg_end (li):
    return [li[0], li[-1]]

a = [5, 10, 15, 20, 25]
answer = beg_end(a)
print(answer)