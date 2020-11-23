# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

def no_dup(li):
    return list(set(li))

a = [1,1,1,1,4,5,3,6,6,5,4,7,8,0,55,4,4]
print(no_dup(a))