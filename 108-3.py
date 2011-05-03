# http://www.research.att.com/~njas/sequences/A018892

def calcPrimes(max):
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

    return primes

def nSol2(factors):
	a = 1
	for k in factors:
		a *= 2*factors[k]+1
	a += 1
	a /= 2

	return a

def permute(inFactors, find):
	factors = inFactors.copy()
	#print factors
	sols = nSol2(factors)

	n = 1
	maxK = 0
	for k, v in factors.iteritems():
		n *= k**v
		maxK = max(maxK, k)

	if sols > find:
		print str(n) + ": " + str(sols)

	if sols > 2*find:
		return

	del factors[maxK]

	for k in factors:
		factors[k] += 1
		permute(factors, find)
		factors[k] -= 1

find = 1000
primes = calcPrimes(find)
factors = {}
for p in primes:
	factors[p] = 1
	sols = nSol2(factors)
	if sols > find:
#		print sols
		break

permute(factors, find)
