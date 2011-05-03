import math

f = open("99.txt", "r")
max = 0
line = 0
i = 1
while True:
	l = f.readline()
	if l == "":
		break
	arr = l.split(",")
	base = int(arr[0])
	exp = int(arr[1])

	tenExp = math.log(base) * exp
	if tenExp > max:
		max = tenExp
		line = i

#	print str(base) + "^" + str(exp) + " = 10^" + str(tenExp)
	i += 1

print "max is 10^" + str(tenExp) + " on line " + str(line)
