import math

def conFrac(n):
	root = math.sqrt(n)
	a = int(root)
	b = int(root)
	num = 1
	den = root - a
	firstNum = 0
	firstDen = 0
	aList = []
	while True:
		den = round((root**2 - b**2)/num)
		num = root + b
	
		ratio = float(num)/float(den)
		a = int(ratio)
		b = round(root - (num - den * a))

		if num == firstNum and den == firstDen:
			break
		elif firstNum == 0:
			firstNum = num
			firstDen = den

		aList.append(a)

		num = den

	return aList

def solveForD(find):
	findRoot = math.sqrt(find)
	a = conFrac(find)

	num = 1
	den = a[0]
	realNum = num+int(findRoot)*den

	i = 1
	while realNum**2 - find * den**2 != 1:
		n = a[i%len(a)]
		num, den = den, den * n + num
		realNum = num+int(findRoot)*den
		i += 1

	return realNum, den

maxX = 0
maxD = 0
for i in range(2, 1001):
	rootI = int(math.sqrt(i))
	if rootI*rootI == i:
		continue

	x, y = solveForD(i)
	print "D: " + str(i) + ", x: " + str(x) + ", y: " + str(y)

	if x > maxX:
		maxX = x
		maxD = i

print "maxD: " + str(maxD) + " => x = " + str(maxX)
