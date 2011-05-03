def reverse(str):
	str2 = ""
	for c in str:
		str2 = c + str2
	return str2

max = 0
maxJ = 0
maxK = 0
j = 999
while j >= 100:
	k = 999
	while k >= 100:
		p = j*k
		if str(p) == reverse(str(p)) and p > max:
			max = p
			maxJ = j
			maxK = k
		k = k - 1
	j = j - 1
print str(maxJ) + "*" + str(maxK) + "=" + str(max)
