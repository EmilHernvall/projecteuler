for a in range(0,1000):
	found = False
	for b in range(0,1000):
		c = 1000 - a - b
		if a**2 + b**2 - c**2 == 0 and a < b and b < c:
			print "a: " + str(a)
			print "b: " + str(b)
			print "c: " + str(c)
			print "abc: " + str(a*b*c)
			found = True
			break
	if found:
		break
