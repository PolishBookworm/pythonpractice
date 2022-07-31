from math import floor

MIESIAC_PARYSZTY = 12
MIESIAC_NIEPARZYSTY_P = 16
MIESIAC_NIEPARZYSTY_N = 15
ROK_PARZYSTY = MIESIAC_PARYSZTY * 5 + MIESIAC_NIEPARZYSTY_P * 5
ROK_NIEPARZYSTY = MIESIAC_PARYSZTY * 5 + MIESIAC_NIEPARZYSTY_N * 5

def main(r, m, d):
	result = 0
	if r % 2 == 0:
		result += ROK_NIEPARZYSTY * (r / 2) + ROK_PARZYSTY * (r / 2 - 1)
		if m % 2 == 0:
			result += MIESIAC_PARYSZTY * (m / 2 - 1) + MIESIAC_NIEPARZYSTY_P * (m / 2)
		else:
			result += MIESIAC_PARYSZTY * (floor(m / 2)) + MIESIAC_NIEPARZYSTY_P * (floor(m / 2))
	else:
		result += ROK_NIEPARZYSTY * (floor(r / 2)) + ROK_PARZYSTY * (floor(r / 2))
		if m % 2 == 0:
			result += MIESIAC_PARYSZTY * (m / 2 - 1) + MIESIAC_NIEPARZYSTY_N * (m / 2)
		else:
			result += MIESIAC_PARYSZTY * (floor(m / 2)) + MIESIAC_NIEPARZYSTY_N * (floor(m / 2))
	result += (d - 1)
	return int(result)

r = int(input())
m = int(input())
d = int(input())

print(main(r, m, d))