def isBouncy(n):
	m = n
	inc = True
	dec = True
	lastInc = ()
	lastDec = 0
	while m > 0:
		o = m%10
		if o > lastInc:
			dec = False
		if o < lastDec:
			inc = False
		lastInc = o
		lastDec = o
		m /= 10
	return not (inc or dec)

count = 0
i = 2
while True:
	if isBouncy(i):
		if i % 10000 == 0:
			print "bouncy: " + str(i) + ", ratio: " + str(float(count)/float(i))
		count += 1
		if float(count)/float(i) >= 0.99:
			break
	i += 1

print i
