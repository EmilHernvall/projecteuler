import math

def a(n):
	if n == 0:
		return 1
	elif n == 1:
		return 4
	else:
		return 6*a(n-1)-a(n-2)-2

i = 2
while True:
	n = a(i)
	v = (1+math.sqrt(2*n*n-2*n+1))/2

	print str(n) + ": " + str(int(v))

	if math.log(n, 10) > 12:
		break

	i += 1
