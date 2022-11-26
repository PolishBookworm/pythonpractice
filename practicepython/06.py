# Ask the user for a string and print out whether this string is a palindrome or not.
string = input('Give me a string\n')
gnirts = string[::-1]
if gnirts.lower() == string.lower():
    print(string + ' is a palindrome.')
else:
    print(string + ' is not a palindrome.')