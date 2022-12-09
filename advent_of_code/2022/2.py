# def pts_for_choice(choice):
# 	if choice == "X":
# 		return 1
# 	if choice == "Y":
# 		return 2
# 	return 3

# def pts_for_result(elf, you):
# 	loses_to = {
# 	"A": "Y",
# 	"B": "Z",
# 	"C": "X"
# 	}
# 	analogy = {
# 	"A": "X",
# 	"B": "Y",
# 	"C": "Z"
# 	}
# 	if analogy[elf] == you:
# 		return 3
# 	if loses_to[elf] == you:
# 		return 6
# 	return 0


with open("2.txt") as f:
    data = f.readlines()


# result = 0
# for datum in data:
# 	result += pts_for_choice(datum[2])
# 	result += pts_for_result(datum[0], datum[2])

# print(result)

translate = {
    "A": 0,
    "B": 1,
    "C": 2
}

# data = ["A Y\n", "B X\n", "C Z\n"]

result = 0
for datum in data:
    if datum[2] == "X":
        result += (translate[datum[0]] - 1) % 3 + 1  # -1
    elif datum[2] == "Y":
        result += 4 + translate[datum[0]]
    else:
        result += 6 + (translate[datum[0]] + 1) % 3 + 1  # + 1

print(result)
