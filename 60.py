import math

def isPrime(n):
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            return False
        i = i + 1
    return True

def PermuteSetTake2(thisSet):
	res = []
	for i, t in enumerate(thisSet):
		for j, q in enumerate(thisSet[i:]):
			if q == t:
				continue

			res.append([t,q])
	return res

def PermuteSetTake3(thisSet):
	res = []
	for i, t in enumerate(thisSet):
		for j, q in enumerate(thisSet[i:]):
			if q == t:
				continue

			for k, r in enumerate(thisSet[j:]):			
				if r == q or r == t:
					continue

				res.append([t,q,r])
	return res

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

def PermutePrimes(primesSet, p, d):
	if d >= 2:
		return

#	print d*"\t" + str(p)

	resultSet = set()

	strp = str(p)
	plen = len(strp)
	candidates = []
	for j, p2 in enumerate(primesSet):
		if p2 <= p:
			continue

		strp2 = str(p2)
		cand1 = int(strp + strp2)
		cand2 = int(strp2 + strp)
		if cand1 in primesSet and cand2 in primesSet:
#			print "\t"*(d+1) + str(p2)
			resultSet.add(p2)
#			PermutePrimes(primesSet, p2, d+1)

	print

	return resultSet

max = 100000
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

print "done calculating primes"

concatenations = {}
min = 10**100
for p in primes:
	if p > 100:
		break

	print p
	resultSet = PermutePrimes(primesSet, p, 0)
	concatenations[p] = resultSet

	for p2 in concatenations.keys():
		if p2 == p:
			break
		print "\t" + str(p2)

		compResultSet = concatenations[p2]
		isect = resultSet.intersection(compResultSet)
		if len(isect) > 0:
			print "\tintersection count: " + str(len(isect))

			perms = PermuteSetTake3(list(isect))
			for perm in perms:
				realset = [p,p2] + perm
				sum = ConcatPermute(realset)
#				print realset
#				print ConcatPermute(realset)
				if sum == 0:
					continue
				if sum < min:
					min = sum
print "min: " + str(min)
