def gcd(a, b):
	if b == 0:
		return a
	else:
		return gcd(b, a % b)

def cmp(a, b):
	return b[1] * a[0] - a[1] * b[0]

max = 19

res = []
den = 1
for i in range(2, max+1):
	den *= i
	for j in range(1, i):
		if gcd(i, j) == 1:
			res.append([j,i])

res.sort(cmp)
for fraction in res:
	print str(fraction[0]*den/fraction[1]) + "/" + str(den) + "=" + str(fraction[0]) + "/" + str(fraction[1])
