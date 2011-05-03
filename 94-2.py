import math

def rec(n):
	if n == 0:
		return 1
	elif n == 1:
		return 1
	elif n == 2:
		return 5
	else:
		return 3*rec(n-1) + 3*rec(n-2) - rec(n-3)

max = 1000000000
i = 1
sum = 0
while True:
	a = rec(i)
	if 3*a - 1 > max:
		break
	
	b = a - 1
	A = math.sqrt(4*a*a - b*b)
	if A == int(A) and b > 0 and A > 0:
		sum += 3*a - 1
		print str(a) + " " + str(a) + " " + str(b) + " => " + str(A)

	b = a + 1
	A = math.sqrt(4*a*a - b*b)
	if A == int(A) and A > 0:
		sum += 3*a + 1
		print str(a) + " " + str(a) + " " + str(b) + " => " + str(A)

	i += 1

print "sum: " + str(sum)
