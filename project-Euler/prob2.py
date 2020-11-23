# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

# Generate Fibonaccis
Fibonaccis = [1,1]
while True:
    if Fibonaccis[-1] >= 4000000:
        del(Fibonaccis[-1])
        break
    else:
        Fibonaccis.append(Fibonaccis[-2] + Fibonaccis[-1])

# Even check
even_fibs = [num for num in Fibonaccis if num % 2 == 0]

# Sum up and print result
result = sum(even_fibs)
print(result)
