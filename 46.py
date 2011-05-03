import math

def isPrime(n):
	if n < 2:
		return False
	i = 2
	while i <= math.sqrt(n):
		if n % i == 0:
			return False
		i = i + 1
	return True

primes = []
i = 2
run = True
while run:
	if isPrime(i):
		primes.append(i)
	elif i % 2 == 1:
		match = False
		for p in primes:
			base = math.sqrt((i - p)/2)
			if int(base) != base:
				continue
			if p + 2 * base * base == i:
				match = True
				break
		if not match:
			print "answer: " + str(i)
			run = False

	i += 1

