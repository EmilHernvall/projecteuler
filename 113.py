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

inc = 0
dec = 0
i = 1
while i < 1000:
	if not isBouncy(i):
		print i
	i += 1

