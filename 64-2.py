# working solution
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

		aList.append(str(a))
#		print "a: " + str(a)
#		print "num: " + str(num)
#		print "den: " + str(den)
#		print "b: " + str(b)
#		print 

		num = den

#	print "sqrt(" + str(n) + ") = " + str(int(root)) + ": " + ",".join(aList)

	return aList

unevenCount = 0
for i in range(2,10000+1):
	root = int(math.sqrt(i))
	if root*root == i:
		continue
	frac = conFrac(i)
	if len(frac) % 2 == 1:
		unevenCount += 1

print "uneven: " + str(unevenCount)
