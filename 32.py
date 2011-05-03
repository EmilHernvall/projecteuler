import primes

def d(n):
	i = 2
	divisors = []
	max = n
	while i <= max:
		if n % i == 0:
			if i == max:
				break

			max = n / i
			divisors.append(i)
			if i != max:
				divisors.append(max)
		i = i + 1

	return divisors

sum = 0
primes = primes.primes(10000)
numSet = range(1,9)
for n in range(1000,10000):
	if n in primes:
		continue

	divisors = d(n)
	i = 0
	while i < len(divisors):
		try:
			res = str(divisors[i]) + str(divisors[i+1]) + str(n)
			if len(res) == 9:
				match = True
				for digit in "123456789":
					if not digit in res:
						match = False
				if match:
					sum += n
					print str(divisors[i]) + "*" + str(divisors[i+1]) + "=" + str(n)
					break
		except IndexError:
			pass
		i += 2

print "sum: " + str(sum)
