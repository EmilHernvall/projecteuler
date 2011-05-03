triangle = []

f = open("67.txt", "r")
txt = f.readline()
while txt != "":
	split = txt.split(" ")
	triangle.append(split)
	txt = f.readline()

maxN = 0
for row in range(1, len(triangle)):
#	print str(row) + ":"
	for col in range(0, len(triangle[row])):
		triangle[row][col] = int(triangle[row][col])
		if col == 0:
			triangle[row][col] += int(triangle[row-1][0])
		elif col == len(triangle[row]) - 1:
			triangle[row][col] += int(triangle[row-1][len(triangle[row-1]) - 1])
		else:
			triangle[row][col] += max(int(triangle[row-1][col]), int(triangle[row-1][col-1]))

		if triangle[row][col] > maxN:
			maxN = triangle[row][col]

#		print triangle[row][col]
#	print

print maxN
