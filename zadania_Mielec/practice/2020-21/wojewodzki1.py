# Global constants
LETTERS = "ABCDEFGHIJKLNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
DIGITS = "0123456789"

# Input from keyboard
string = input()

# Counting
num_letters = 0
num_digits = 0

for char in string:
	if char in LETTERS:
		num_letters += 1
	elif char in DIGITS:
		num_digits += 1

# Output
print(f"Liter: {num_letters}")
print(f"Cyfr: {num_digits}")