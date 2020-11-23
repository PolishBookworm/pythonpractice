# Take a list and write a program that prints out all the elements of the list that are less than 5.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
num = int(input('Give me a number\n'))
c = []
for b in a:
    if b < num:
        c.append(b)
print(c)