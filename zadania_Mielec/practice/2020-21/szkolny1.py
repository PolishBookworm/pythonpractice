# Password generator

def check(string):
	if len(string) != 15 and len(string) != 16:
		return True

def process(base_str):
	result = base_str[0]
	result += base_str[2::2]
	result = result[:3] + result[4] + result[3] + result[5:]
	result = result[::-1]
	return result

def main(base_str):
	if check(base_str):
		return "Niepoprawna długość łańcucha"
	return process(base_str)



string = input()

print(main(string))




