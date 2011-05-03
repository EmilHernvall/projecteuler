import math

def rect(r, c):
	sum = 0
	for i in range(1, r+1):
		for j in range(1, c+1):
#			n = int(math.ceil(float(r)/i)*math.ceil(float(c)/j))
			n = (r-i+1)*(c-j+1)
#			print str(i) + "x" + str(j)
#			print "\t" + str(n)
			sum += n
	return sum

#print rect(3,4)

target = 2000000

i = 1
while True:
	if i % 10 == 0:
		print i

	nSol = rect(i, i)
	if nSol > target:
		i -= 1
		print str(i) + "x" + str(i)
		print str(nSol)
		break

	i += 1

print

#i = 216
delta = target - rect(i, i)
while True:
	print str(i)
	j = i
	while True:
		nSol = rect(i, j)
		nDelta = abs(target - nSol)
#		print "\t" + str(nDelta)
		if nDelta < delta:
			delta = nDelta
			print "\t" + str(i) + "x" + str(j) + " => " + str(nSol) + " => " + str(delta)

		if nSol < target:
			break

		j -= 1

	i += 1
