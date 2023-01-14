n = int(input())

result = []

for i in range(n):
	data = list(map(int, input().split()))
	a = data[0]
	a_to_the_bth = 1
	for j in range(data[1]):
		a_to_the_bth *= a
		a_to_the_bth %= 10
	result.append(a_to_the_bth)
	
for item in result:
	print(item)