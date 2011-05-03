import math

def rev(n):
	return (1+math.sqrt(1+24*n))/6

i = 0
pnrs = set()
while True:
	i += 1
	p = i * (3 * i - 1) / 2

	j = 0
	found = False
	for q in pnrs:
		r = p - q
		s = p + q
		n = rev(s)
		if r in pnrs and int(n) == n:
			print str(p) + "-" + str(q) + "=" + str(r)
			print str(p) + "+" + str(q) + "=" + str(s)
			found = True
			break
		
	if found:
		break

	pnrs.add(p)
