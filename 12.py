import math

t = 0
j = 0
maxCount = 0
while True:
	t += j

	i = 2
	n = t
	factorCount = 0
	max = n
	while i <= max:
		if n % i == 0:
			max = n / i
			factorCount += 2
		i = i + 1

	if n > 0 and math.floor(math.sqrt(n))**2 == n:
		factorCount += 1

	if factorCount >= 500:
		print "Found: " + str(t)
		break

	if factorCount > maxCount:
		maxCount = factorCount
		print str(j) + ": " + str(t) + ": " + str(factorCount)

	j += 1
