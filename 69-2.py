max = 20
processed = [set()]*(max+1)
data = range(0, max + 1)
maxV = 0
maxPhi = 0
maxI = 0
for i,n in enumerate(data):
	if i == 0 or i == 1:
		continue

	c = 0
	if len(processed[i]) > 0:
		c = len(processed[i])
	else:
		c = 1

	data[i] = i - c
	v = float(i) / data[i]
	if v > maxV:
		maxPhi = data[i]
		maxV = v
		maxI = i

#	if i % 100 == 0:
	print "phi(" + str(i) + ")=" + str(data[i])
	print "\t" + str(i) + "/phi(" + str(i) + ")=" + str(v)

	j = 2*i
	c = 1
	prev = set([i])
	while j < max + 1:
		prev.add(j)
#		if len(processed[j]) > 0:
		processed[j] = processed[j].union(prev)
		j += i

print "max: " + str(maxI) + "/phi(" + str(maxPhi) + ")=" + str(maxV)

print data
print [0,1,1,2,2,4,2,6,4,6,4,10,4,12,6,8,8,16,6,18]

