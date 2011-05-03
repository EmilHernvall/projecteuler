import math

for i in range(1, 100000):
	v = (1+math.sqrt(2*i*i-2*i+1))/2
	if int(v) == v:
		print str(i) + " " + str(v)

# http://www.research.att.com/~njas/sequences/?q=1%2C4%2C21%2C120%2C697&sort=0&fmt=0&language=english&go=Search

