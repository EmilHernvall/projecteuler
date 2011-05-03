import math

def isPrime(n):
	i = 2
	while i <= math.sqrt(n):
		if n % i == 0:
			return False
		i = i + 1
	return True

pl = [41,79,1601]
for p in pl:
	print str(p) + ": " + str(isPrime(p))
