import math

def pieces(tiles, pieceSize, nr):
	global cache

	key = "%d-%d-%d" % (tiles, pieceSize, nr)
	if cache.has_key(key):
		return cache[key]

	if nr == 0:
		return 0
	if nr*pieceSize > tiles:
		return 0

	sum = 0
	for i in xrange(0, tiles-pieceSize*nr+1):
		nextTileSize = tiles-i-pieceSize
		v = 1
		if nextTileSize >= (nr-1)*pieceSize + 1 and nr - 1 > 0:
			v = pieces(nextTileSize,pieceSize,nr-1)
		sum += 1 * v

	cache[key] = sum

	return sum

def problem116(tiles, lengths):
	sum = 0
	for length in lengths:
		fitNr = int(math.floor(tiles / length))
		for i in xrange(1, fitNr + 1):
			v = pieces(tiles, length, i)
			sum += v
	return sum

if __name__ == "__main__":
	cache = {}
	print problem116(50, [2,3,4])
