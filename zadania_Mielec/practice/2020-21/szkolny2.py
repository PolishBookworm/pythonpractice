def gcd_sub(a,b):
	"""returns num_iterations: int"""
	i = 0
	while a != b:
		i += 1
		if b > a:
			c = a
			a = b
			b = c
		c = b
		b = a - c
		a = c
	return i


def gcd_div(a,b):
	"""returns list: [GCD: int, num_iterations: int]"""
	i = 0
	while b != 0:
		i += 1
		if b > a:
			c = a
			a = b
			b = c
		c = a % b
		a = b
		b = c
	return [a, i]


a = int(input())
b = int(input())

print(f"NWD = {gcd_div(a,b)[0]}")
print(f"L_iteracji (I metoda) = {gcd_div(a,b)[1]}")
print(f"L_iteracji (II metoda) = {gcd_sub(a,b)}")