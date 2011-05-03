# working solution
import math
import primes

max = 1000000
primes = primes.primes(max)

print "done calculating primes."

data = [0]*(max+1)
factors = {}
for p in primes:
	data[p] = p - 1
	v = p - 1

	j = 2*p

	nextSquare = p*p
	while j <= max:
		if j == nextSquare:
			v *= p
			data[j] = v
			nextSquare *= p
		else:
			if factors.has_key(j):
				factors[j].add(p)
			else:
				factors[j] = set([p])

		j += p

print "done with primes and powers of primes."

for k, v in factors.iteritems():
	phi = k
	for factor in v:
		phi = (phi * (factor - 1)) / factor
	data[k] = phi

print "done with combinations"

maxN = 0
maxV = 0
maxPhi = 0
for n, phi in enumerate(data):
	if phi == 0:
		continue
	v = float(n) / phi
	if v > maxV:
		maxV = v
		maxN = n
		maxPhi = phi

print "max: " + str(maxN) + "/phi(" + str(maxPhi) + ")=" + str(maxV)


