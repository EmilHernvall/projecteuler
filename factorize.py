import math

def factorize(num):

	n = num

	factors = []
	product = 1
	while n % 2 == 0:
		n /= 2
		product *= 2
		factors.append(2)

	i = 3
	maxFactor = math.sqrt(n)
	while n > 1 and i <= maxFactor:

		if n % i == 0:
			factors.append(i)
			n = n / i
			product *= i
			maxFactor = math.sqrt(n)
		else:
			i = i + 2

	if maxFactor < i and num / product != 1:
		factors.append(num / product)

	return factors

def divisors(num):

	divisors = []
	i = 1
	max = int(math.sqrt(num))
	while i <= max:

		if num % i == 0:
			divisors.append(i)
			divisors.append(num/i)

		i += 1

	return divisors

def multipleDivisors(num):

	divisors = []
	i = 2
	max = int(math.sqrt(num))
	while i <= max:

		n = 1
		while num % (i**n) == 0:
			divisors.append(i)
			if n > 1:
				divisors.append(i**n)
			n += 1

		if num % i == 0:
			divisors.append(num/i)

		i += 1

	return divisors

