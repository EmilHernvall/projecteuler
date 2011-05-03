import math

f = open("words.txt")
file = f.read()
words = file.split(",")

nr = 0
for word in words:
	sum = 0
	for c in word:
		sum += ord(c) - ord("A") + 1
	r = (math.sqrt(1+8*sum)-1)/2
	if r - int(r) == 0:
		print word + ": " + str(r)
		nr += 1
print "nr triangle words: " + str(nr)
