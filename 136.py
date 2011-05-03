import math

find = 100
solutions = {}
for i in range(1, int(math.sqrt(find))+1):
	print i
	for j in range(i, find+1):
		n = i*j
		if n > find:
			break

		d = (i+j)/4.0

		if int(d) == d and i - d > 0:
			if solutions.has_key(n):
				solutions[n].add(i)
			else:
				solutions[n] = set([i])

		if int(d) == d and j - d > 0:
			if solutions.has_key(n):
				solutions[n].add(j)
			else:
				solutions[n] = set([j])

print
count = 0
for k, v in solutions.iteritems():
	if len(v) == 1:
		print k
		count += 1

print "count: " + str(count)
