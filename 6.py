end = 100

sum = 0
squareSum = (end/2 * (1 + end))**2
for i in range(0, end+1):
	sum += i**2

print "answer: " + str(squareSum - sum)
