# Take a list and write a program that prints out all the elements of the list that are less than a number given by the user.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
num = int(input('Give me a number\n'))
b = [a[i] for i in a if i < num]
print(b)