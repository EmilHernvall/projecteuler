import math

n = 23
root = math.sqrt(n)
a = int(root)
b = int(root)
num = 1
den = root - a
aList = []
for i in range(1,13):
	num *= root + b
	den = int(round(root**2 - b**2))
	a = int(float(num)/float(den))
	b = int(round(root - (num - den * a)))

	aList.append(str(a))
	print "a: " + str(a)
	print "num: " + str(num)
	print "den: " + str(den)
	print "b: " + str(b)
	print 

	num = den

#print "sqrt(" + str(n) + ") = " + str(n) + ": " + ",".join(aList)
