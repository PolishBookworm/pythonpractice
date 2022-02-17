# NOT FINISHED!! (make it recursive)

# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.

def Fibs(amount):
    '''Generates amount of Fibbonaci numbers'''

    if amount <= 0:
        raise ValueError("Values greater than or equal to 0 not allowed.")
    if amount == 1:
        return [1]
    if amount == 2:
        return [1, 1]
    


print(Fibs(10))
print(Fibs(-1))
print(Fibs(0))
print(Fibs(1))
print(Fibs(2))