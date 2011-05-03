max = 1000
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

sums = range(0, len(primes), 1)
counts = range(0, len(primes), 1)
i = 0
while i < len(sums):
	sums[i] = 0
	counts[i] = 0
	i += 1

max = 0
maxPrime = 0
startI = 0
j = 0
while startI < len(primes):
#	print str(startI) + " " + str(len(primes))
	j = 0
	for i, p in enumerate(primes[startI:]):
		if sums[j] != 0:
			sums[j] += p
			counts[j] += 1
		else:
			sums[j] = p
			counts[j] = 1

#		print str(p) + " " + str(sums[j])

		if counts[j] > max and sums[j] in primesSet:
			max = counts[j] 
			maxPrime = sums[j]

		j += 1
	print maxPrime
	startI += 1
	

print "max is " + str(maxPrime) + " with " + str(max) + " steps."
