def main(y, skok):
	pos = 0
	i = 0
	while pos < y:
		i += 1
		pos += skok
		if i % 10 == 9:
			skok -= 1
			if skok == 0:
				return -1
	return i

y = int(input())
skok = int(input())

print(main(y, skok))