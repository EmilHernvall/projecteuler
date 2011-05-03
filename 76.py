import copy

def permute(den, target, last):
	global cache

	if cache.has_key(target):
		if cache[target].has_key(last):
			return cache[target][last]
	else:
		cache[target] = {}

	sum = 0
	for n in den:
		if n > last:
			continue

		if target == n:
			sum += 1
		elif n < target:
			sum += permute(den, target - n, n)

	cache[target][last] = sum

	return sum

cache = {}
max = 100
den = range(1,max)
den.reverse()
print "sum: " + str(permute(den, max, max))

