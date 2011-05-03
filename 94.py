import math

max = 1000000000
i = 1
while i < max:
	a = i
	
	b = a - 1
	A = b*math.sqrt(4*a*a - b*b)/4
	if A == int(A):
		print str(a) + " " + str(a) + " " + str(b)

	b = a + 1
	A = b*math.sqrt(4*a*a - b*b)/4
	if A == int(A):
		print str(a) + " " + str(a) + " " + str(b)

	i += 1

# http://www.research.att.com/~njas/sequences/?q=1%2C5%2C17%2C65%2C241&sort=0&fmt=0&language=english&go=Search
# http://www.research.att.com/~njas/sequences/?q=12%2C120%2C1848%2C25080&sort=0&fmt=0&language=english&go=Search
