def convert(base, decimal):

	in_progress = ""

	n = decimal

	while n > 0:
		in_progress += str(n % base)
		n = int(n / base)

	result = in_progress[::-1]
	
	if not result:
		result = 0

	return result



base = int(input("What number system would you like to convert to ? (Please provide an integer.) "))

decimal = int(input("Please enter an integer in the decimal system. "))

print(f"Your result is: {convert(base, decimal)}")



# 22:2=11r0
# 11:2=5r1
# 5:2=2r1
# 2:2=1r0
# 1:2=0r1
# n:base=new_n r in_progress += self
