string = input('Hi! Give me a sentence\n')
li = string.split()
li = li[::-1]
result = ' '.join(li)
print(result)