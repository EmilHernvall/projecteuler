def permute(list, curSet):
	if len(curSet) == len(list):
		res = []
		minOuterPos = 0
		minOuterValue = ()
		for i in range(0, len(curSet)/2):
			inner = curSet[i]
			middle = curSet[(i+1)%(len(curSet)/2)]
			outer = curSet[(i+1)%(len(curSet)/2)+len(curSet)/2]

			if outer < minOuterValue:
				minOuterValue = outer
				minOuterPos = i

			sum = inner + middle + outer

			res.append(sum)

		first = res[0]
		for v in res[1:]:
			if v != first:
				return set()

		solution, readableSolution = "", ""
		for j in range(0, len(curSet)/2):
			i = (minOuterPos + j) % (len(curSet)/2)
			thisSet = []
			thisSet.append(str(curSet[(i+1)%(len(curSet)/2)+len(curSet)/2]))
			thisSet.append(str(curSet[i]))
			thisSet.append(str(curSet[(i+1)%(len(curSet)/2)]))
			readableSolution += ",".join(thisSet) + ";"
			solution += "".join(thisSet)

		print str(res[0]) + "\t" + readableSolution
		return set([int(solution)])

	res = set()
	for i, n in enumerate(list):
		if n == 0:
			continue

		tmp = n
		list[i] = 0
		res = res.union(permute(list, curSet + [n]))
		list[i] = tmp

	return res

size = 5
digits = range(1,2*size+1)
results = permute(digits, [])
max = 0
for result in results:
	if result > max and len(str(result)) == 16:
		max = result
print "max: " + str(max)
