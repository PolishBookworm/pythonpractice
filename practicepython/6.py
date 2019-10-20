string = input('Give me a string\n')
gnirts = string[::-1]
if gnirts.lower == string.lower:
    print(string + ' is a palindrome.')
else:
    print(string + ' is not a palindrome.')