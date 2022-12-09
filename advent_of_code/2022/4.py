with open("4.txt") as f:
    data = f.readlines()

# data = [
#     "2-4,6-8\n",
#     "2-3,4-5\n",
#     "5-7,7-9\n",
#     "2-8,3-7\n",
#     "6-6,4-6\n",
#     "2-6,4-8\n"
# ]

result = 0
for datum in data:
    datum = list(map(int, datum.strip().replace("-", ",").split(",")))
    # if (datum[0] <= datum[2] and datum[1] >= datum[3]) or (
    #         datum[0] >= datum[2] and datum[1] <= datum[3]):
    #     result += 1
    if datum[0] in range(datum[2], datum[3] + 1) or datum[1] in range(datum[2], datum[3] + 1) or datum[2] in range(datum[0], datum[1] + 1):
        result += 1

print(result)
