from numpy.numarray import array
from numpy.linalg import solve

def calculatePolynom(constants, n):
	res = 0
	for i, c in enumerate(constants):
		res += c * n**(len(constants)-i-1)
	return res

def OP(func, n):
	y = []
	for i in xrange(1, n+1):
		y.append(func(i))

	x = []
	for i in xrange(1, n+1):
		row = []
		for j in xrange(1, n+1):
			row.append(i**(n-j))
		x.append(row)

	constants = solve(array(x), array(y))

	return lambda x: calculatePolynom(list(constants), x)

#func = lambda n: n**3
func = lambda n: 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10
degree = 10

sumOfFITs = 0
for i in xrange(1,degree+1):
	fitFunc = OP(func, i)

	correct = func(i+1)
	FIT = fitFunc(i+1)

	if FIT == correct:
		break

	print "%d: %d" % (i, FIT)
	sumOfFITs += FIT

print "sum of FITs: %d" % (sumOfFITs,)
