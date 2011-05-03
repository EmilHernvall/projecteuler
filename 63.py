import math

count = 0
j = 1
while True:
	i = 1
	print str(j)
	while True:
		p = j**i
		if math.floor(math.log(p, 10))+1 != i:
			break
		print "\t" + str(i) + ": " + str(p)
		count += 1
		i += 1
	if i == 1:
		break
	j += 1
print "count: " + str(count)
