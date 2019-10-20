a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
num = int(input('Give me a number\n'))
c = []
for b in a:
    if b < num:
        c.append(b)
print(c)