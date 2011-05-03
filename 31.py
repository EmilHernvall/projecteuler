def permute(den, target, last):
	sum = 0
	for n in den:
		if n > last: continue

		if target == n: sum += 1
		elif n < target:
			sum += permute(den, target - n, n)
	return sum

den = [ 200, 100, 50, 20, 10, 5, 2, 1 ]
print "sum: " + str(permute(den, 200, 200))

