import primes

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

target = 5000
i = 2
sum = 0
while sum < target:
	if i % 100 == 0:
		print "progress: " + str(i)

	den = primes.primes(i)
#	print "done calculating primes."
	cache = {}
	sum = permute(den, i, i)
	if sum >= target:
		print str(i) + ": " + str(sum)
		break
	i += 1
