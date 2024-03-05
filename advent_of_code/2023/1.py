NUMS = "0123456789"
WORDS = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

with open("1.txt") as f:
    data = f.readlines()

# data = ["1abc2",
# "pqr3stu8vwx",
# "a1b2c3d4e5f",
# "treb7uchet"]

res = 0

# for datum in data:
#     for char in datum:
#         if char in NUMS:
#             res += 10*int(char)
#             break
#     for char in datum[::-1]:
#         if char in NUMS:
#             res += int(char)
#             break

for datum in data:
    for i in range(len(datum)):
        if datum[i] in NUMS:n
            tmp = i           
            break
    for

    for char in datum[::-1]:
        if char in NUMS:
            res += int(char)
            break

print(res)