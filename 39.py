import math

combinations = set()
counts = {}
maxP = 1000
a = 0
while a < maxP:
	a += 1

	b = a
	while b < maxP:
		b += 1
		c = math.sqrt(a**2 + b**2)
		p = a + b + c
		if int(c) != c:
			continue
		if p > maxP:
			break
		l = [a, b, int(c)]
		l.sort()
		s = str(l[0]) + "+" + str(l[1]) + "+" + str(int(l[2])) + "=" + str(int(p))
		if not s in combinations:
			combinations.add(s)
			if not int(p) in counts:
				counts[int(p)] = 1
			else:
				counts[int(p)] = counts[int(p)] + 1

max = 0
maxkey = 0
keys = counts.keys()
keys.sort()
for c in keys:
	v = counts[c]
	if v > 1:
		print str(c) + ": " + str(v)
	if v > max:
		max = v
		maxkey = c

print "max: " + str(maxkey)
