i = 100
s = 1
while (i > 1):
	s *= i
	i -= 1

sum = 0
for c in str(s):
	sum += int(c)

print sum
