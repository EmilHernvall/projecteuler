def factorize(v, cache):
	n = v
	i = 2
	factors = set()
	while n > 1:
		if cache.has_key(n):
			factors = factors.union(cache[n])
			break

		if n % i == 0:
			if not i in factors:
				factors.add(i)
			n = n / i
		else:
			i = i + 1
	
	if cache.has_key(v):
		cache[v] = factors

	return factors

def phi(n, factorCache):
	factors = factorize(n, factorCache)
	count = n
	for factor in factors:
		count = (count * (factor - 1)) / factor
	return count

max = 10
sieve = range(0, max)
pos = 2
primes = set()
while pos != max:
    while pos < max and sieve[pos] == 0:
        pos += 1
    if pos == max:
        break;

    n = sieve[pos]
    sieve[pos] = 0
    primes.add(n)

    i = pos
    while i < max:
        if i % n == 0:
            sieve[i] = 0
        i += n

print "done calculating primes."

factorCache = {}
maxV = 0
maxN = 0
n = max + 1
while n > 1:
	if n in primes:
		phi_n = n - 1
	else:
		phi_n = phi(n, factorCache)

	v = float(n) / phi_n
	if v > maxV:
		maxV = v
		maxN = n

	if n % 100 == 0:
		print "phi(" + str(n) + ")=" + str(phi_n) + ", " + str(n) + "/phi(" + str(n) + ") = " + str(v)

	n -= 1

print "max: " + str(maxN)
