def gcd_sub(a,b):
	"""returns num_iterations: int"""
	c = 1
	i = 0
	while a != b:
		i += 1
		c = b
		b = a - c
		a = c
	return i


def gcd_div(a,b):
	"""returns list: [GCD: int, num_iterations: int]"""
	pass 


# num1 = int(input())
# num2 = int(input())

# if num1 > num2:
# 	a = num1
# 	b = num2
# else:
# 	a = num2
# 	b = num1

# print(f"NWD = {gcd_div(a,b)[0]}")