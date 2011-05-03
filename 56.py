maxSum = 0
maxA = 0
maxB = 0
for a in range(1, 100):
	print a
	for b in range(1, 100):
		current = str(a**b)
		sum = 0
		for c in current:
			sum += int(c)
		if sum > maxSum:
			maxSum = sum
			maxA = a
			maxB = b
print "answer: " + str(maxA) + "^" + str(maxB) + "=" + str(maxSum)
