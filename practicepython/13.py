# # Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.

# # def Fibbonaci(how_many):
# #     if how_many > 0:
# #         output = [1, 1]
# #         for n in range(1, how_many-1):
# #             output.append(output[n] + output[n-1])
# #     else:
# #         output = []
# #     return output

# # num = int(input('How many Fibbonaci numbers do you want to generate?\n'))
# # print(Fibbonaci(num))

# def Fibs(amount):
#     result = [1]
#     i = 0
#     if amount == 1:
#         return result
#     else:
#         result.append(result[i] + result[i-1])
#         i += 1
#         Fibs(amount-1)


# def f(n):
#     if n <= 2:
#         return 1
#     else:
#         return f(n-1) + f(n-2)

# for i in range(1,10):
#     print(i, " --> ", f(i))


# def Fibs(amount):
#     '''Generates amount of Fibbonaci numbers'''

#     if amount <= 0:
#         return []

#     result = [1]

#     if amount == 1:
#         return result

#     result.append(1)

#     while len(result) < amount:
#         result.append(result[-1] + result[-2])

#     return result

def Fibs(amount):
    '''Generates amount of Fibbonaci numbers'''

    if amount <= 0:
        raise ValueError("Values greater than or equal to 0 not allowed.")
    if amount == 1:
        return [1]
    if amount == 2:
        return [1, 1]
    before = Fibs(amount-1)
    try:
        return before.append(before[-1] + before[-2])
    except(AttributeError):
        pass

print(Fibs(10))
print(Fibs(-1))
print(Fibs(0))
print(Fibs(1))
print(Fibs(2))