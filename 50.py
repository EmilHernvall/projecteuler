max = 1000000
sieve = range(0, max)
pos = 2
primes = []
primesSet = set()
while pos != max:
    while pos < max and sieve[pos] == 0:
        pos += 1
    if pos == max:
        break;
    
    n = sieve[pos]
    sieve[pos] = 0
    primes.append(n)
    primesSet.add(n)
    
    i = pos
    while i < max:
        if i % n == 0:
            sieve[i] = 0
        i += n

print "done calculating primes: " + str(len(primes))

sums = {}
counts = {}
max = 0
maxPrime = 0
for i, p in enumerate(primes):
	if i % 100 == 0:
		print p
	for key in primes:
		if key >= p:
			break

		sums[key] += p
		counts[key] += 1
		if sums[key] in primesSet and counts[key] > max:
			max = counts[key]
			maxPrime = sums[key]
	sums[p] = p
	counts[p] = 1
	print maxPrime

print "max is " + str(maxPrime) + " with " + str(max) + " steps."
