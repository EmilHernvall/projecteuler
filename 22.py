f = open("names3.txt", "r")
names = f.read().split("\n")

pos = 1
sum = 0
for name in names:
	wordScore = 0
	for c in name:
		wordScore += ord(c) - ord("A") + 1
	print name + " " + str(wordScore) + " " + str(pos) + " " + str(pos*wordScore)
	sum += pos * wordScore
	pos += 1

print "total score: " + str(sum)
