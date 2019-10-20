def Fibbonaci(how_many):
    if how_many >= 2:
        output = [1, 1]
        for n in range(1, how_many-1):
            output.append(output[len(output)-1] + output[len(output)-2])
    elif how_many == 1:
        output = [1]
    else:
        output = []
    return output

num = int(input('How many Fibbonaci numbers do you want to generate?\n'))
sequence = Fibbonaci(num)
print(sequence)