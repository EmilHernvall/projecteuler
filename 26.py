import math
import primes

# long division
def rep(n):
	a = 10
	i = 0
	while True:
		a = (a % n) * 10

		i += 1
		if a == 10 or a == 0:
			break

	return i

limit = 1000
primes = set(primes.primes(limit))

n = 0
max = 0
for i in xrange(3, limit):
	if not i in primes:
		continue

	m = rep(i)
	if m > max:
		n = i
		max = m

print "max is " + str(n) + " with " + str(max) + " decimals"
