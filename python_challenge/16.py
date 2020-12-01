# Use a list comprehension to square each odd number in a list. 
# e. g. 
# [1,2,3,4,5,6,7,8,9]
# Then, the output should be:
# [1,9,25,49,81]

li = [1,2,3,4,5,6,7,8,9]

squares = [i**2 for i in li if i % 2 != 0]

print(squares)
