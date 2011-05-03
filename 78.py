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

max = 2
cache = {}
while True:
	den = range(1,max+1)
	sum = permute(den, max, max)
	if max % 100 == 0 or max < 10:
		print "progress: p(" + str(max) + ")=" + str(sum)

	if sum % 1000000 == 0:
		print "p(" + str(max) + ")=" + str(sum)
		break
	max += 1
