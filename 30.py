# 5*9^5 < 99999
# 6*9^6 > 999999

sum = 0
for i in range(10, 6*9**6):
	s = str(i)
	sum2 = 0
	for c in s:
		d = int(c)
		sum2 += d**5
	if sum2 == i:
		print i
		sum += i
print 
print "sum: " + str(sum)
