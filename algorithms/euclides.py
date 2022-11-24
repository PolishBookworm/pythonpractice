def recursive(a, b):
	if (a == b) or (b % a == 0):
		return a
	if a % b == 0:
		return b
	if a > b:
		return recursive(a % b, b)
	return recursive(a, b % a)

def iterable(a, b):
	while (a % b != 0) and (b % a != 0):
		c = min(a, b)
		a = abs(a - b)
		b = c
	if a >= b:
		return b
	return a

if __name__ == "__main__":
	a = int(input())
	b = int(input())
	print(recursive(a, b))
	print(iterable(a, b))