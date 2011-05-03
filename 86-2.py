import math

def problem86(side):
	solutions = set()
	for x in xrange(1, side+1):
		for y in xrange(1, side+1):
			for z in xrange(1, side+1):
				a = (x+z)**2 + y**2
				b = (y+z)**2 + x**2

				if int(math.sqrt(a))**2 == a and a < b:
					sol = [x,y,z]
					sol.sort()
					solutions.add(tuple(sol))

				if int(math.sqrt(b))**2 == b and b < a:
					sol = [x,y,z]
					sol.sort()
					solutions.add(tuple(sol))

	print len(solutions)

if __name__ == "__main__":
	problem86(100)
