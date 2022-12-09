with open("1.txt") as f:
    data = f.readlines()

sums = []
sing = 0

for datum in data:
    if datum.strip():
        sing += int(datum.strip())
    else:
        sums.append(sing)
        sing = 0

sum_top_3 = 0

for n in range(3):
    sum_top_3 += max(sums)
    sums.remove(max(sums))

print(sum_top_3)
