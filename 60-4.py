# this is the working solution
# 20 seconds on screamer

import math

def recurse(primesSet, primesCache, concatenations, previousSet, path):
	if len(previousSet) == 0:
		if len(path) == 5:
			sum = 0
			for p in path:
				sum += int(p)
			return sum
		return 0

	min = 0
	for p in previousSet:
		if str(p) in path:
			break

		if not concatenations.has_key(p):
			concatables = set()

			strp = str(p)
			plen = len(strp)
			candidates = []
			for j, p2 in enumerate(primesSet):
				strp2 = str(p2)
				cand1 = int(strp + strp2)
				cand2 = int(strp2 + strp)
				if cand1 in primesCache and cand2 in primesCache:
					concatables.add(p2)

			concatenations[p] = concatables
		else:
			concatables = concatenations[p]

		intersection = previousSet.intersection(concatables)
		searchRes = recurse(primesSet, primesCache, concatenations, intersection, path + [str(p)])
		if searchRes != 0:
			if searchRes < min or min == 0:
				min = searchRes

	return min

limit = 0
f = open("primes.txt", "r")
primes = []
while True:
	d = f.readline()
	if d == "":
		break
	if int(d) < 10000:
		limit += 1
	primes.append(int(d))

primesSet = set(primes[0:limit])
primesCache = set(primes)

print "read " + str(len(primes)) + " primes."

processed = set()
concatenations = {}
print "min: " + str(recurse(primesSet, primesCache, concatenations, primesSet, []))
