import math

def match(w1, w2, n):
	l = {}
	for i, m in enumerate(str(n)):
		if int(m) in l.values():
			return 0

		l[w1[i]] = int(m)

	n2 = 0
	length = len(w2)
	for i, c in enumerate(w2):
		n2 += l[c] * 10**(length-i-1)

	if len(str(n2)) != len(str(n)):
		return 0

	root = int(math.sqrt(n2))
	if root*root == n2:
		return n2
	else:
		return 0

f = open("words.txt", "r")
words = f.read().split(",")

lookup = {}
for word in words:
	characters = list(word)
	characters.sort()
	sorted = "".join(characters)

	if lookup.has_key(sorted):
		lookup[sorted].append(word)
	else:
		lookup[sorted] = [word]

maxLen = 0
anagrams = []
for k, v in lookup.iteritems():
	if len(v) == 2:
		maxLen = max(maxLen, len(v[0]))
		anagrams.append(v)

squares = []
i = 1
while True:
	square = i**2
	if square > 10**(maxLen+1):
		break

	squares.append(square)

	i += 1

maxMatch = 0
for anagram in anagrams:
	lower = 10**(len(anagram[0])-1)
	upper = 10**len(anagram[0])
	matches = 0
	for square in squares:
		if square >= lower and square < upper:
			other =  match(anagram[0], anagram[1], square)
			if other > 0:
				matches = max(matches, square, other)

	maxMatch = max(matches, maxMatch)

	if matches:
		print ",".join(anagram) + ": matches, " + str(matches)
	else:
		print ",".join(anagram) + ": doesn't match"

print "max: " + str(maxMatch)
