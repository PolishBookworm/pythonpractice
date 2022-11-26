# NOT FINISHED!!
# Write a program that asks the user how many Fibonnaci numbers to
# generate and then generates them.

def Fibs(n):
    '''Generates n Fibbonaci numbers'''

    if n <= 0:
        raise ValueError("Values greater than or equal to 0 not allowed.")
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    prev = Fibs(n - 1)
    return prev.append(prev[-1] + prev[-2])


print(Fibs(10))
# print(Fibs(-1))
# print(Fibs(0))
print(Fibs(1))
print(Fibs(2))
