import math

def revT(n):
    return (math.sqrt(1+8*n)-1)/2

def revP(n):
    return (1+math.sqrt(1+24*n))/6

nh = 143
while True:
	nh += 1
	H = nh * (2 * nh - 1)
	np = revP(H)
	if int(np) == np: # and int(nt) == nt:
		# all hexagonal numbers are also triangle numbers
		nt = revT(H)
		print str(int(nt)) + " " + str(int(np)) + " " + str(nh) + " " + str(H)
		break
