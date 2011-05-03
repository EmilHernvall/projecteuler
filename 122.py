import math

def Power(n):
	if n == 0:
		return 0
	elif n % 2 == 1:
		print "n * n^" + str(n-1)
		return 1 + Power(n-1)
	elif n % 2 == 0:
		print "n^" + str(n/2) + " * n^" + str(n/2)
		return Power(n/2)
	else:
		return 1

count = 0
for i in range(1,200+1):
	c = int(math.ceil(math.log(i, 2)))

	if i % 2 == 1:
		c += 1

	print str(i) + ": " + str(c)

	count += c
print "count: " + str(count)
