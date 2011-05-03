import math
import primes

find = 50000000
max2 = int(math.ceil(find**(1/2.0)))
max3 = int(math.ceil(find**(1/3.0)))
max4 = int(math.ceil(find**(1/4.0)))

primes2 = primes.primes(max2)
primes3 = primes.primes(max3)
primes4 = primes.primes(max4)
print "got primes"

count = 0
unique = set()
for i in primes2:
	squareI = i**2
	for j in primes3:
		IJ = squareI + j**3

		for n, k in enumerate(primes4):
			s = IJ + k**4
			if s > find:
				break
			else:
				unique.add(s)

print "count: " + str(len(unique))
