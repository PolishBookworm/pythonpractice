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


def Fibs(amount):
    '''Generates amount of Fibbonaci numbers'''

    result = [1]

    while len(result) < amount:
        result.append()