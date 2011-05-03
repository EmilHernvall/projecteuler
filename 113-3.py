count = 0
for i in range(0, 9):
	for j in range(i, 9):
		for k in range(0, j+1):
			count += 1
		for k in range(i, 9):
			count += 1
		count += 2
	count += 1

print "count: " + str(count)
