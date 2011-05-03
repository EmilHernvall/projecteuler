import math

def isPrime(n):
	i = 2
	while i <= math.sqrt(n):
		if n % i == 0:
			return False
		i = i + 1
	return True

totalCount = 1
primeCount = 0
sideLength = 0
i = 1
while True:
	sideLength = i+2
	n = i*i + i + 1
	n2 = (i+1)*(i+1) + (i+1) + 1
	n3 = n+(n2-n)/2
	n4 = n2+(n2-n)/2
	for p in [n,n2,n3,n4]:
		if isPrime(p):
			primeCount += 1
		totalCount += 1
	ratio = float(primeCount) / float(totalCount) * 100.0

	if ratio < 10:
		break

	print str(i) + ": " + str(ratio)

	i += 2

print "sideLength: " + str(sideLength)
