def up_to_n(n):
	nums = list(range(2,n+1))
	j = 0
	for num in nums:
		j += 1
		for i in nums[j:]:
			if i % num == 0:
				nums.remove(i)
	return nums

def prime(i, primes):
    for prime in primes:
        if not (i == prime or i % prime):
            return False
    primes.add(i)
    return i

def n_primes(n):
    primes = set([2])
    i, p = 2, 0
    while True:
        if prime(i, primes):
            p += 1
            if p == n:
                return list(primes)
        i += 1


if __name__ == "__main__":

	n = int(input())

	print(up_to_n(n))
	print(n_primes(n))