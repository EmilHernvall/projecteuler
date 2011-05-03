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

i = 0
max = 0
maxCount = 0
maxStart = 0
prevMax = 0
for p in primes:
	sum = 0
	j = 0
	for q in primes[i:]:
		sum += q
		j += 1
		if sum in primesSet and j > maxCount:
			maxCount = j
			max = sum
			maxStart = p

	if maxCount > len(primes) - i:
		break

	print "current max: " + str(max) + " with " + str(maxCount) + " steps, starting with " + str(maxStart) + "."

	prevMax = max
	i += 1

print "max: " + str(max) + " with " + str(maxCount) + " steps, starting with " + str(maxStart) + "."
