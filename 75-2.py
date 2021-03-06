def new1(v):
	a,b,c = v[0],v[1],v[2]
	return [a-2*b+2*c,2*a-b+2*c,2*a-2*b+3*c]

def new2(v):
	a,b,c = v[0],v[1],v[2]
	return [a+2*b+2*c,2*a+b+2*c,2*a+2*b+3*c]

def new3(v):
	a,b,c = v[0],v[1],v[2]
	return [-a+2*b+2*c,-2*a+b+2*c,-2*a+2*b+3*c]

def verify(v):
	return v[0]**2 + v[1]**2 - v[2]**2

def recurse(v, depth):
	global max, result
	
	length = sum(v)
	if length > max:
		return

	if result.has_key(length):
		result[length] += 1
	else:
		result[length] = 1

	recurse(new1(v), depth+1)
	recurse(new2(v), depth+1)
	recurse(new3(v), depth+1)

	# since (na)^2 + (nb)^2 = (nc)^2 <=> a^2 + b^2 = c^2 we need to consider
	# all multiples of the triplett less than max as well
	i = 2
	while length*i < max:
		nlength = length*i
		if result.has_key(nlength):
			result[nlength] += 1
		else:
			result[nlength] = 1
		i += 1

max = 2000000
result = {}
recurse([3,4,5],0)

count = reduce(lambda x,y: int(x)+int(y), map(lambda x: x == 1, result.itervalues()))

print "count: " + str(count)
