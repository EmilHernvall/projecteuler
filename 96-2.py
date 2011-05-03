import math
import copy

def stringToArr(s, endline):
	rows = []
	for j, strRow in enumerate(s.split(endline)):
		row = []
		for i, c in enumerate(strRow):
			row.append(int(c))
		rows.append(row)	
	return rows

def solve(inRows, debug):
	if debug:
		print "Processing puzzle"

	rows = copy.deepcopy(inRows)

	columns, boxes = [], []
	for j, row in enumerate(rows):
		for i, c in enumerate(row):
			if len(columns) <= i:
				columns.append([c])
			else:
				columns[i].append(c)
			box = int(3*(math.ceil((j+1)/3.0)-1)+math.ceil((i+1)/3.0)-1)
			if len(boxes) <= box:
				boxes.append([c])
			else:
				boxes[box].append(c)

	baseSet = set(range(1,10))
	prev = 0
	unsolvable = False
	ps = {}
	while True:
		unsolved = 0
		for i, row in enumerate(rows):
			sRow = ""
			for j, cell in enumerate(row):
				if cell == 0:
					box = int(3*(math.ceil((i+1)/3.0)-1)+math.ceil((j+1)/3.0)-1)
					p = baseSet.difference(set(row)).difference(set(columns[j])).difference(set(boxes[box]))
					if len(p) == 0:
						unsolvable = True

					if not ps.has_key(i):
						ps[i] = {j: p}
					else:
						ps[i][j] = p

					if len(p) == 1:
						n = p.pop()
						sRow += str(n)
						rows[i][j] = n
						columns[j][i] = n
						boxes[box].append(n)
					else:
						for n in p:
							sRow += str(n)
						unsolved += 1
					sRow += "\t"
				else:
					sRow += str(cell) + "\t"
			if debug:
				print sRow

		if debug:
			print
		if unsolvable:
			return []

		if prev == unsolved:
			break

		if unsolved == 0:
			return rows

		prev = unsolved

	col = set()
	while col == set():
		i, row = ps.popitem()
		if len(row) == 0:
			continue

		while col == set():
			if len(row) == 0:
				break

			j, col = row.popitem()

	if debug:
		print "Permuting " + str(i) + ", " + str(j) + ":"

	for n in col:
		rows[i][j] = n
		res = solve(rows, debug)
		if len(res) != 0:
			return res

	return []

s = """000000907
000420180
000705026
100904000
050000040
000507009
920108000
034059000
507000000"""

solution = solve(stringToArr(s, "\n"), False)
for row in solution:
	print row
