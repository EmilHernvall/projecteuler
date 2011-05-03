def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

max = 10000
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
        sieve[i] = 0
        i += n

print "done calculating primes."

lNum, lDen = 1, 3
bNum, bDen = 1, 2

den = 2
count = 0
while den <= max:

	num = int(float(lNum)/float(lDen) * den)

	if den % 100 == 0:
		print "progress: " + str(den) + " of " + str(max)

	while num * bDen < den * bNum:
		if num * lDen > den * lNum and (num in primes or den in primes or gcd(num, den) == 1):
			count += 1
		num += 1

	den += 1

print "count: " + str(count)
