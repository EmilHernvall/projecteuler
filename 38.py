max = 0
for n in range(2, 7):
	print str(n)
	i = 0
	while True:
		i += 1
		s = ""
		for k in range(1, n+1):
			s += str(i*k)
#			print s
			if len(s) == 9:
				match = True
				for j in range(1, 10):
					if not str(j) in s:
						match = False
						break
				if match:
					print "match: " + str(i) + " " + s
					if int(s) > max:
						max = int(s)
				break
			elif len(s) > 9:
				continue
		if len(str(i)) > 9/n:
			break

print "max: " + str(max)
