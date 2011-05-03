f = 1
g = 1
s = 0
while True:
	tmp = g
	g = tmp + f
	f = tmp
	if f > 4000000:
		break;
	#print f
	if f % 2 == 0:
		s += f
print "sum : " + str(s)
