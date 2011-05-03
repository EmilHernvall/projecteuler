def mc(col, row):
	return ((col & 0xFFFF) << 16) | (row & 0xFFFF)

def recurse(matrix, col, row, visited):
	if col == 0:
		return matrix[col][row]

	coord = mc(col, row)
	visited.append(coord)

#	print str(col) + " " + str(row)

	v = matrix[col][row]
	m = ()
	go = -1
	if row > 0:
		if matrix[col][row-1] < m and mc(col, row-1) not in visited:
			m = matrix[col][row-1]
			go = 1
	if row < len(matrix) - 1:
		if matrix[col][row+1] < m and mc(col,row+1) not in visited:
			m = matrix[col][row+1]
			go = 2
	if matrix[col-1][row] < m and mc(col-1,row) not in visited:
		m = matrix[col-1][row]
		go = 3

	if go == 1:
		v += recurse(matrix, col, row-1, visited)
	elif go == 2:
		v += recurse(matrix, col, row+1, visited)
	else:
		v += recurse(matrix, col-1, row, visited)

	return v

# load
f = open("81-2.txt", "r")
matrix = []
while True:
	l = f.readline().strip()
	if l == "":
		break
	row = map(lambda x: int(x), l.split(","))
	for i, e in enumerate(row):
		if len(matrix) <= i:
			matrix.append([e])
		else:
			matrix[i].append(e)

dim = len(matrix)
minV = ()
for i, cell in enumerate(matrix[-1]):
	res = recurse(matrix, dim-1, i, [])
	print cell
	print "\t" + str(res)
	minV = min(res, minV)
print "min: " + str(minV)
