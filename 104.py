import math

def isPandigital(n):
	l = list(str(n))
	l.sort()
	l = map(lambda x: int(x), l)

	return l == [1,2,3,4,5,6,7,8,9]

a, b = 1, 1
i = 3
while True:
	c = a + b

	firstC = int(str(c)[0:9])
	lastC = c % 10**9
	if isPandigital(firstC):
		print str(i) + ": " + str(firstC) + " ... " + str(lastC)
		print "pandigital first"
#	if isPandigital(lastC):
#		print str(i) + ": " + str(firstC) + " ... " + str(lastC)
#		print "pandigital last"

	if isPandigital(firstC) and isPandigital(lastC):
		break

	a, b = b, c
	i += 1
