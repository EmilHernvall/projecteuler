import math

def f(a, b):
	a = str(a)
	b = str(b)
	if len(a) != len(b):
		return False

	arrA, arrB = [], []
	for c in a:
		arrA.append(c)
	for c in b:
		arrB.append(c)

	arrA.sort()
	arrB.sort()

	sA = "".join(arrA)
	sB = "".join(arrB)

	return sA == sB

max = 10000000
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
        sieve[i] = 0
        i += n

print "done calculating primes."

data = [0]*(max+1)
factors = [[]]*(max+1)
for p in primes:
	if p < 1000:
		print "processing prime: " + str(p)

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
			if len(factors[j]) == 0:
				factors[j] = [p]
			else:
				factors[j].append(p)

		j += p

print "done with primes and powers of primes."

for k, v in enumerate(factors):
#	if k % 10000 == 0:
#		print "nonprime: " + str(k)
	if len(v) == 0:
		continue

	v = set(v)
#	print str(k) + ": " + str(len(v))

	phi = k
	for factor in v:
		phi = (phi * (factor - 1)) / factor
	data[k] = phi

print "done with combinations"

minN = 0
minV = ()
minPhi = 0
for n, phi in enumerate(data):
	if phi == 0:
		continue
	if not f(n, phi):
		continue
	v = float(n) / phi
	if v < minV:
		minV = v
		minN = n
		minPhi = phi
#	print "\t" + str(n) + "/" + str(phi) + "=" + str(v)

print "min: " + str(minN) + "/phi(" + str(minPhi) + ")=" + str(minV)

