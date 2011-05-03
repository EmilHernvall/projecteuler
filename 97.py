calc = 7830457
i = 0
sum = 1
while i < calc:
	if i % 10000 == 0:
		print i
	newSum = sum * 2
	sum = newSum % 100000000000
	i += 1
print str(28433*sum+1)[-10:]
