from random import randint

results = [randint(0,10) for n in range(1,19)]
print(results)

sum_results = [results[n] + results [n+1] + results[n+2] for n in range(0,18,3)]
print(sum_results)

print(sorted(sum_results)[::-1])