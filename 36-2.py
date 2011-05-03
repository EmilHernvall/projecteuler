def reverseBinary(n):
	m = 0
	while n > 0:
		m = (m << 1) | (n & 1)
		n = n >> 1

	return m

def reverseDenary(n):
	m = 0
	while n > 0:
		m = m * 10 + (n % 10)
		n = n / 10

	return m

sum = 0
i = 0
while i < 1000000:
	if i == reverseDenary(i):
		if i == reverseBinary(i):
			sum += i
			print str(i)
	i += 1
print "sum: " + str(sum)
