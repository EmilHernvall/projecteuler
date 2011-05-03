import math

def tri2(a,b,c):

	AO = math.sqrt(a[0]**2 + a[1]**2)
	BO = math.sqrt(b[0]**2 + b[1]**2)
	CO = math.sqrt(c[0]**2 + c[1]**2)

	# AB
	AB = math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
	AB_angle = math.acos((AO**2 + BO**2 - AB**2)/float(2*AO*BO))
#	print "angle: " + str(math.degrees(AB_angle))

	# AC
	AC = math.sqrt((a[0]-c[0])**2 + (a[1]-c[1])**2)
	AC_angle = math.acos((AO**2 + CO**2 - AC**2)/float(2*AO*CO))
#	print "angle: " + str(math.degrees(AC_angle))

	# BC
	BC = math.sqrt((b[0]-c[0])**2 + (b[1]-c[1])**2)
	BC_angle = math.acos((BO**2 + CO**2 - BC**2)/float(2*BO*CO))
#	print "angle: " + str(math.degrees(BC_angle))

#	print str(AB_angle + AC_angle + BC_angle)
#	print str(math.degrees(AB_angle + AC_angle + BC_angle))
	return AB_angle + AC_angle + BC_angle >= 1.999999*math.pi

f = open("102.txt", "r")
count = 0
while True:
	line = f.readline().strip()
	if line == "":
		break
	coords = line.split(",")
	if len(coords) != 6:
		continue

	coords = map(lambda x: int(x), coords)

	a = coords[0:2]
	b = coords[2:4]
	c = coords[4:6]
	print [a,b,c]
	res = tri2(a,b,c)
	print res
	if res:
		count += 1

print "count: " + str(count)
