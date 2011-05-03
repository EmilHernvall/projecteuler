import copy

def mc(col, row):
    return ((col & 0xFFFF) << 16) | (row & 0xFFFF)

def recurse(matrix, values, col, row, visited):
    if col == 0:
        return values[col][row]

    coord = mc(col, row)
    visited.append(coord)

#   print str(col) + " " + str(row)

    v = values[col][row]
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
        v += recurse(matrix, values, col, row-1, visited)
    elif go == 2:
        v += recurse(matrix, values, col, row+1, visited)
    else:
        v += recurse(matrix, values, col-1, row, visited)

    return v

# load
f = open("81.txt", "r")
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
path = copy.deepcopy(matrix)
for i, row in enumerate(matrix):
	for j, cell in enumerate(row):
		if i > 0:
			if j == 0:
				path[i][j] += min(matrix[i-1][j], matrix[i][j+1])
			elif j == dim -1:
				path[i][j] += min(matrix[i-1][j], matrix[i][j-1])
			else:
				path[i][j] += min(matrix[i-1][j], matrix[i][j+1], matrix[i][j-1])

#display 
#rows = []
#for i, col in enumerate(path):
#	for j, cell in enumerate(col):
#		if len(rows) <= j:
#			rows.append([cell])
#		else:
#			rows[j].append(cell)

#for row in rows:
#	print row

#print matrix[-1][-1]

dim = len(matrix)
minV = ()
for i, cell in enumerate(matrix[-1]):
    res = recurse(path, matrix, dim-1, i, [])
    print cell
    print "\t" + str(res)
    minV = min(res, minV)
print "min: " + str(minV)

