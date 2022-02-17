def main(a):
	print(a)
	if a != 100:
		main(a+1)

if __name__ == "__main__":
	main(1)