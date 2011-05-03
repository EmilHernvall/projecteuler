import math

def isPrime(n):
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            return False
        i = i + 1
    return True

def intelligentPrimeCheck(primesSet, p):
	if p in primesSet:
		return True
	else:
		if isPrime(p):
			primesSet.add(p)
			return True
		else:
			return False

def ConcatPermute(termList):
	score = 0
	for i, t in enumerate(termList):
		for j, u in enumerate(termList[i+1:]):
			a = int(str(t)+str(u))
			b = int(str(u)+str(t))
			if not isPrime(a) or not isPrime(b):
				return 0
		score += t
	return score

def PermutePrimes(primesSet, primesCache, p, d):
	if d >= 2:
		return

#	print d*"\t" + str(p)

	resultSet = set()

	strp = str(p)
	plen = len(strp)
	candidates = []
	for j, p2 in enumerate(primesSet):
		strp2 = str(p2)
		cand1 = int(strp + strp2)
		cand2 = int(strp2 + strp)
#		if cand1 in primesSet and cand2 in primesSet:
		if intelligentPrimeCheck(primesCache, cand1) and intelligentPrimeCheck(primesCache, cand2):
			resultSet.add(p2)

	return resultSet

max = 1000
sieve = range(0, max)
pos = 2
primes = []
while pos != max:
    while pos < max and sieve[pos] == 0:
        pos += 1
    if pos == max:
        break;

    n = sieve[pos]
    sieve[pos] = 0
    primes.append(n)

    i = pos
    while i < max:
        if i % n == 0:
            sieve[i] = 0
        i += n

primesSet = set(primes)
primesCache = set(primes)

print "done calculating primes"

processed = set()
concatenations = {}
min = 10**100
for p in primes:
	print p
	if not concatenations.has_key(p):
		concatables1 = PermutePrimes(primesSet, primesCache, p, 0)
		concatenations[p] = concatables1
	else:
		concatables1 = concatenations[p]

	for p2 in concatables1:
		if p2 == p:
			break

		print "\t" + str(p2)

		if not concatenations.has_key(p2):
			concatables2 = PermutePrimes(primesSet, primesCache, p2, 0)
			concatenations[p2] = concatables2
		else:
			concatables2 = concatenations[p2]

		intersection1 = concatables1.intersection(concatables2)
		for p3 in intersection1:
			if p3 == p2 or p3 == p:
				continue

			print "\t\t" + str(p3)

			if not concatenations.has_key(p3):
				concatables3 = PermutePrimes(primesSet, primesCache, p3, 0)
				concatenations[p3] = concatables3
			else:
				concatables3 = concatenations[p3]

			intersection2 = intersection1.intersection(concatables3)
			for p4 in intersection2:
				if p4 == p3 or p4 == p2 or p4 == p:
					continue

				print "\t\t\t" + str(p4)

				if not concatenations.has_key(p4):
					concatables4 = PermutePrimes(primesSet, primesCache, p4, 0)
					concatenations[p4] = concatables4
				else:
					concatables4 = concatenations[p4]

				intersection3 = intersection2.intersection(concatables4)
				for t in intersection3:
					print "\t\t\t\tVoila: " + str(t)

