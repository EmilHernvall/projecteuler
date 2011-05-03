# precalculate the continued fraction for e
a = []
for i in range(1, 100):
	for j in range(1,4):
		k = 0
		if j % 2 == 0:
			k = i*2
		else:
			k = 1
		a.append(k)

a = a[:99]
a.reverse()

# calculate the numerator
num = 1
den = a[0]
for n in a[1:]:
	num, den = den, den * n + num

# sum the digits in the numerator
sNum = str(num+2*den)
sum = 0
for c in sNum:
	sum += int(c)

print sum
