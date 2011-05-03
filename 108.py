import math

def factorize(n):
	i = 2
	factors = set([n])
	while i <= math.sqrt(n):
		if n % i == 0:
			factors.add(i)
			factors.add(n/i)
		i = i + 1
	factors.add(1)
	return factors

# 1/x + 1/y = 1/i
# x=a, y=an, i=nm
# 1/a + 1/(an) = 1/(nm)
# n/(an) + 1/(an) = 1/(nm)
# (n + 1)/(an) = 1/(nm)
# m*(n + 1) = a
# n is a factor of i. Then a solution to the equation is:
# m=i/n
# a=m*(n + 1)
# x=a
# y=a*n
def solve(v):
	primeFactors = realFactorize(v)
	factors = factorize(v)
	for n in factors:
#		print n
		m = v/n
		a = m*(n+1)
		print "1/" + str(a) + " + 1/" + str(a*n) + " = 1/" + str(v)	
		if a*n*v + a*v != a*n*a:
			print "wtf"

def solve2(v):
	factors = factorize(v)
	for a in factors:
		c = v/a
		b = c+a

		x = min(a*b,c*b)
		y = max(c*b,a*b)
		n = c*a

		if y*v + x*v == x*y:
			print "1/" + str(x) + " + 1/" + str(y) + " = 1/" + str(v)	

def solve3(v):
	factors = factorize(v)
	xValues = set()
	solutions = []
	for b in factors:
		for c in factors:
			d = v/(b*c)
			a = d*(c + b)
			
			x = min(a*b, a*c)
			y = max(a*b, a*c)
			n = b*c*d

			if not x in xValues and x > 0 and y*v + x*v == x*y:
#				print [b,c,d]
				xValues.add(x)
				solutions.append("1/" + str(x) + " + 1/" + str(y) + " = 1/" + str(v))

	return solutions

def nSol(v):
	factors = factorize(v**2)
	return (len(factors)+1)/2

#print nSol(1260)
#n = 180180
#solutions = solve3(n)
#for solution in solutions:
#	print solution

maxV = 0
v = 1
while True:
	solutions = solve3(v)
	if len(solutions) > maxV:
		print str(v) + ": " + str(len(solutions))
		maxV = len(solutions)

	if len(solutions) > 1000:
		print v
		break
	v += 1
