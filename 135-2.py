import math

solutions = {}
for i in range(1, 1001):
	print i
	for j in range(1, 1000001):
		n = i*j
		if n > 1000000:
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
	if len(v) == 10:
		print k
		count += 1

print "count: " + str(count)
