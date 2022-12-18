with open("5.txt") as f:
    data = f.readlines()

# data = [
# 	"    [D]    ",
# 	"[N] [C]    ",
# 	"[Z] [M] [P]",
# 	" 1   2   3 ",
# 	"\n",
# 	"move 1 from 2 to 1",
# 	"move 3 from 1 to 3",
# 	"move 2 from 2 to 1",
# 	"move 1 from 1 to 2"
# ]

num_stacks = int(data[data.index("\n") - 1].split()[-1])
stack_arrangement = data[:data.index("\n") - 1]
stacks = [[i[4 * n + 1] for i in stack_arrangement if i[4 * n + 1]
           != " "][::-1] for n in range(num_stacks)]
data = data[data.index("\n") + 1:]

for datum in data:
    datum = datum.split()
    count = int(datum[1])
    source = int(datum[3]) - 1
    destination = int(datum[5]) - 1
    # while count:
    # 	stacks[destination].append(stacks[source].pop())
    # 	count -= 1
    for item in stacks[source][-count:]:
        stacks[destination].append(item)
    stacks[source] = stacks[source][:-count]

result = ""
for stack in stacks:
    result += stack[-1]
print(result)
