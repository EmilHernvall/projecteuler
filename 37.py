import math

def isPrime(n):
	if n == 1:
		return False
	i = 2
	while i <= math.sqrt(n):
		if n % i == 0:
			return False
		i = i + 1
	return True

def truncate(s):
	if not isPrime(int(s)):
		return False

	if len(s) == 1:
		return True
	else:
		return truncate(s[1:])

def recurse(s):
	sum = 0
	for i in range(1, 10):
		t = s + str(i)
		if isPrime(int(t)):
			if truncate(t) and len(t) > 1:
				print t
				sum += int(t)
			sum += recurse(t)
	return sum

print "sum: " + str(recurse(""))
