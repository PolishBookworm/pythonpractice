# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).

nums = [n for n in range(2000,3201) if n % 7 == 0 and n % 5 != 0]

print(nums)
