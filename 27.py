import math

def isPrime(n):
	n = abs(n)
	i = 2
	while i <= math.sqrt(n):
		if n % i == 0:
			return False
		i = i + 1
	return True

def testSeq(a,b):
	n = 0
	while isPrime(n*n + a*n + b):
		n += 1
	return n

primes = []
for i in range(-1000,1000):
	if isPrime(i):
		primes.append(i)

a = 0
b = 0
max = 0
for i in primes:
	for j in primes:
		l = testSeq(i,j)
#		print str(i) + ", " + str(j) + ": " + str(l)
		if l > max:
			max = l
			a = i
			b = j

print "n^2 + " + str(a) + "n + " + str(b) + ": " + str(max)
print "product: ab=" + str(a*b)
