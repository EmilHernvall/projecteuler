import math

prev = set(range(10,100))
max = 101
i = 3
count = 99
while i < max:
	cur = set()
	for n in prev:
		if n < 10:
			first = n
		else:
			first = n / (10**int(math.log(n, 10)))

		last = n % 10

		# insert before
		if first >= last:
			for m in range(first, 10):
				cur.add(10**int(math.log(n,10)+1)*m + n)

		# insert after
		if first <= last:
			for m in range(last, 10):
				cur.add(m + 10*n)
		else:
			cur.add(10*n)
			
	curCount = len(cur)
	count += len(cur)
	print str(i) + ": " + str(count) + "\t\t" + str(curCount) + "\t\t" + str(curCount/float(len(prev))*100)
	prev = cur
	i += 1

print
print "count: " + str(count)
