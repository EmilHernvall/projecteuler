import math

max = 0
maxD = 0
for D in range(2, 1000+1):
	root = int(math.sqrt(D))
	if root*root == D:
		continue

	print D
	y = 1
	while True:
		x = math.sqrt(1 + D*y*y)
		print "\t" + str(x) + " " + str(int(x))
		if float(int(x)) == x:
			print "\t" + str(x)
			if x > max:
				max = x
				maxD = D
			break
		y += 1
print "maxD: " + str(maxD)
