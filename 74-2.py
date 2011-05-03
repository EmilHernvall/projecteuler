def chain(n, history):
	global chainCache, fCache

	sum = 0
	while n >= 1:
		sum += fCache[n % 10]
		n = int(n/10)

	if sum in history:
		return 1
	else:
		if chainCache.has_key(sum):
			res = chainCache[sum]
		else:
			history.add(sum)
			res = chain(sum, history)
			chainCache[sum] = res

		res += 1
		return res

fCache = [1]
f = 1
i = 1
while i <= 9:
	f *= i
	fCache.append(f)
	i += 1

chainCache = {}
max = 1000000
count = 0
for i in range(1, max):
	if i % 1000 == 0:
		print "progress: " + str(i) + " of " + str(max)

	res = chain(i, set([i]))
	if res == 60:
#		print str(i) + ": " + str(res)
		count += 1
print "count: " + str(count)

