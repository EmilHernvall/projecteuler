def find_min(matrix, x0, y0, path):
    if cache.has_key((x0, y0)): return cache[(x0,y0)]
    if (x0, y0) in path: return 0xFFFFFFFF
    if x0 == len(matrix) or y0 == len(matrix): return 0xFFFFFFFF
    if y0 < 0 or x0 < 0: return 0xFFFFFFFF
    if y0 == 0 and x0 == 0: return matrix[y0][x0]

    path.append((x0, y0))

    res = matrix[y0][x0] + min(find_min(matrix, x0-1, y0, path),
                               find_min(matrix, x0, y0-1, path),
                               find_min(matrix, x0, y0+1, path))

    path.pop()

    return res

def find_min2(matrix, x0, y0, path):
    if (x0, y0) in path: return 0xFFFFFFFF
    if x0 == len(matrix) or y0 == len(matrix): return 0xFFFFFFFF
    if y0 < 0 or x0 < 0: return 0xFFFFFFFF
    if y0 == 0 and x0 == 0: return matrix[y0][x0]

    path.append((x0, y0))

    res = matrix[y0][x0] + min(find_min(matrix, x0-1, y0, path),
                               find_min(matrix, x0, y0-1, path),
                               find_min(matrix, x0, y0+1, path),
                               find_min2(matrix, x0+1, y0, path))

    path.pop()

    return res

matrix = []
with open('p083_matrix.txt', 'r') as fh:
#with open('p082_matrix_simple.txt', 'r') as fh:
    for l in fh:
        l = l.strip()
        matrix.append([int(x) for x in l.split(",")])

cache = {}
for x in xrange(0, len(matrix)):
    for y in xrange(0, len(matrix)):
        res = find_min(matrix, x, y, [])
        cache[(x,y)] = res

for x in xrange(0, len(matrix)):
    for y in xrange(0, len(matrix)):
        res = find_min2(matrix, x, y, [])
        cache[(x,y)] = res

print cache[(len(matrix)-1,len(matrix)-1)]
