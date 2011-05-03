sum = 1
for i in range(1,1000,2):
	n = i*i + i + 1
	n2 = (i+1)*(i+1) + (i+1) + 1
	sum += n + n2 + n+(n2-n)/2 + n2+(n2-n)/2
print sum
