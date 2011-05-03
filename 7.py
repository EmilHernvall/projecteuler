import math

def isPrime(n):
	i = 2
	while i <= math.sqrt(n):
		if n % i == 0:
			return False
		i = i + 1
	return True

i = 0
n = 1
while i <= 10001:
	if isPrime(n):
#		print str(i) + ": " + str(n)
		i = i + 1
	n = n + 1
print str(i-1) + ": " + str(n-1)
