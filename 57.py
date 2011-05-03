a = 1
b = 2
count = 0
for i in range(1, 1000):
#	print "1 + " + str(a) + "/" + str(b) + "=" + str(b+a) + "/" + str(b)
	if len(str(a+b)) > len(str(b)):
		count += 1
#		print "\tHeureka"
	newA = b
	newB = 2*b + a
	a = newA
	b = newB
print "count: " + str(count)
