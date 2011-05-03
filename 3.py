import math

n = 600851475143
#n = 9192631770

i = 2
primes = []
product = 1
while i < n:
	if n % i == 0:
		factor = False
		for p in primes:
			if i % p == 0:
				factor = True
		if not factor:
			print "factor: " + str(i)
			product = product * i
			primes.append(i)
			if product == n:
				break;
	i += 1

print ""
print "n: " + str(n)
print "product: " + str(product)
print "largest factor: " + str(primes.pop())
