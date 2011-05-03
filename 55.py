def reverse(n):
	nlist = list(str(n))
	nlist.reverse()
	return int("".join(nlist))

def isLychrel(n):
	cur = n
	for i in range(0, 50):
		cur = cur + reverse(cur)
		if cur == reverse(cur):
#			print "n
			return True
	return False

count = 0
for i in range(0, 10000):
	if not isLychrel(i):
#		print i
		count += 1

print "count: " + str(count)
