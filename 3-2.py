def factorize(n):
    i = 2
    factors = []
    while n > 1:
        if n % i == 0:
            factors.append(i)
            n = n / i
        else:
            i = i + 1
    print "max: " + str(i)
    return factors

max = 0
for factor in factorize(9192631770):
#for factor in factorize(600851475143):
	if factor > max:
		max = factor
	print factor
print "max: " + str(max)
