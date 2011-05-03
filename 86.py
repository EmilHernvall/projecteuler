def gcd(a, b):
	while b != 0:
		t = b
		b = a % b
		a = t
	return a

def triplets(side):
	m = 2
	tc = 0
	while True:
		validCount = 0
		for n in xrange(1, m+1):
			if gcd(m, n) != 1:
				continue

			a = m*m - n*n
			b = 2*m*n
			c = m*m + n*n

			if a > side or b > side:
				break

			yield (a,b,c)
			tc += 1

			for k in xrange(2, min(int(side/a), int(side/b))+1):
				tc += 1
				yield (k*a,k*b,k*c)

			validCount += 1

		if validCount == 0:
			break

		m += 1

	return

def problem86(side):
	c = 0
	for triplet in triplets(side):
		#print triplet
		c += triplet[0] - 1

	print c

if __name__ == "__main__":
	problem86(100)
