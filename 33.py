# (10a+b)/(10b+c)=a/c

for a in range(1,10):
	for b in range(1, 10):
		c = 10*a*b / (10*a + b - a)
		if a == c or b == c:
			continue
		if (10.0*float(a)+float(b))/(10.0*float(b)+float(c)) == float(a)/float(c):
			print str(10*a+b) + "/" + str(10*b+c) + "=" + str(a) + "/" + str(c)
