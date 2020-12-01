# Write a program that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order.

string = input('Hi! Give me a sentence\n')
li = string.split()
li.reverse()
result = ' '.join(li)
print(result)