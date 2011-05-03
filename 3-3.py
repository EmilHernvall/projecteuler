import factorize

max = 0
for factor in factorize.factorize(600851475143):
	if factor > max:
		max = factor
	print factor
print "max: " + str(max)
