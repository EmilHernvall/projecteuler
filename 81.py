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
for i, row in enumerate(matrix):
	for j, cell in enumerate(row):
		if i == 0:
			if j == 0:
				continue

			matrix[i][j] += matrix[i][j-1]
		else:
			if j == 0:
				matrix[i][j] += matrix[i-1][j]
			else:
				matrix[i][j] += min(matrix[i-1][j], matrix[i][j-1])

#display 
#rows = []
#for i, col in enumerate(matrix):
#	for j, cell in enumerate(col):
#		if len(rows) <= j:
#			rows.append([cell])
#		else:
#			rows[j].append(cell)

#for row in rows:
#	print row

print matrix[-1][-1]
