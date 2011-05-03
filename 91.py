class coordinate(object):

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __cmp__(self, other):
		if other.x > self.x:
			return -1
		elif other.x < self.x:
			return 1
		else:
			if other.y > self.y:
				return -1
			elif other.y < self.y:
				return 1
			else:
				return 0

	def is_perpendicular(self, other):
		return self.x * other.x + self.y * other.y == 0

	def __str__(self):
		return "(%d, %d)" % (self.x, self.y)

	def __sub__(self, other):
		return coordinate(self.x - other.x, self.y - other.y)

class triangle(object):

	def __init__(self, c_1, c_2, c_3):
		coordinates = [c_1, c_2, c_3]
		coordinates.sort()

		#print [str(c) for c in coordinates]
		self.c_1, self.c_2, self.c_3 = coordinates

	def __hash__(self):
		v = 0
		for i, c in enumerate((self.c_3, self.c_2)):
			v += 100**(2*i) * (c.x+1) + 100**(2*i+1) * (c.y+1)
		#print "%s %d" % (self, v)
		return v

	def __eq__(self, other):
		return self.__hash__() == other.__hash__()

	def __str__(self):
		return "%s - %s - %s" % (self.c_1, self.c_2, self.c_3)

def problem91(nr):
	coords = []
	for x in xrange(0,nr+1):
		for y in xrange(0,nr+1):
			coords.append(coordinate(x,y));

	base_coord = coordinate(0,0)
	triangles = set()
	for c_1 in coords:
		for c_2 in coords:
			if base_coord == c_1 or base_coord == c_2 or c_1 == c_2:
				continue

			c_3 = c_2 - c_1

			if c_3.is_perpendicular(c_1) or c_3.is_perpendicular(c_2) or c_1.is_perpendicular(c_2):
				t = triangle(base_coord, c_1, c_2)
				triangles.add(t)

	return triangles

if __name__ == "__main__":
	res = list(problem91(30))
	res.sort()
	for t in res:
		print t
	print "total count: %d" % (len(res))
