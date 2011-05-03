import math

def P(n):
	global cache
	if n < 0:
		return 0

	if n == 0:
		return 1

	if cache.has_key(n):
		return cache[n]

	sum = 0
	for k in range(1, int(math.sqrt(n))+1):
		n_1 = n - k*(3*k-1) / 2
		n_2 = n - k*(3*k+1) / 2

		Pn_1 = P(n_1)
		Pn_2 = P(n_2)

		if k % 2 == 1:
			sum += Pn_1 + Pn_2
		else:
			sum -= Pn_1 + Pn_2

	cache[n] = sum

	return sum

cache = {}
print P(100)-1
