TYPES = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

with open("3.txt") as f:
    data = f.readlines()

# data = [
# 	"vJrwpWtwJgWrhcsFMMfFFhFp\n",
# 	"jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\n",
# 	"PmmdzqPrVvPwwTWBwg\n",
# 	"wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\n",
# 	"ttgJtRGJQctTZtZT\n",
# 	"CrZsJsPPZsGzwwsLwLmpwMDw\n"
# 	]

# result = 0
# for datum in data:
# 	c1 = datum[:int(len(datum)/2)]
# 	c2 = datum[int(len(datum)/2):]
# 	for item in c1:
# 		if item in c2:
# 			result += TYPES.index(item) + 1
# 			break
# print(result)

result = 0
i = 1
group = []
for datum in data:
    group.append(datum[:-1])
    if i % 3 == 0:
        for item in group[0]:
            if item in group[1] and item in group[2]:
                result += TYPES.index(item) + 1
                break
        group = []
    i += 1

print(result)
