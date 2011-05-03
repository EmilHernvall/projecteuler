import copy

def product(a):
	return reduce(lambda x,y: x*y, a)

def recurse(inputA, k, pos, start):
	if pos == k:
		return 0

#	a = copy.copy(inputA)
	a = inputA
	if k > 100 and pos < 8:
		print a[0:20]

	a[pos] = 1
	startS = sum(a)
	startP = product(a)
	max = startS - startP
	i = start
	while i <= start + max + 1:
		a[pos] = i

		p = startP * i
		s = startS + i - 1

		if p == s:
			print ",".join(map(lambda x: str(x), a)) + " = " + str(s)
			break
		elif p > s:
			break
		elif s > 2*k:
			break

		if recurse(a, k, pos + 1, i) == 0:
			i += 1
		else:
			i += 1

	a[pos] = 1
	return i - start

def minSol(k):
	a = []
	for i in range(0, k):
		a.append(1)

	recurse(a, k, 0, 2)
	
for i in range(1, 20):
	print i
	minSol(i)

#minSol(12000)

