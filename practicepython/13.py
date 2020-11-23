def Fibbonaci(how_many):
    if how_many > 0:
        output = [1, 1]
        for n in range(1, how_many-1):
            output.append(output[n] + output[n-1])
    else:
        output = []
    return output

num = int(input('How many Fibbonaci numbers do you want to generate?\n'))
print(Fibbonaci(num))