import math

def isPrime(n):
	if n == 2:
		return True
	if n == 5:
		return True

	end = n % 10
	if end != 1 and end != 3 and end != 7 and end != 9:
		return False

	i = 3
	while i <= math.sqrt(n):
		if n % i == 0:
			return False
		i = i + 2
	return True

i = 3
sum = 2
while i <= 2000000:
	if isPrime(i):
#		print i
		sum += i
	if i % 1001 == 0:
		print i
	i = i + 2

print
print "sum: " + str(sum)
