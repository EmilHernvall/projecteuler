lNum, lDen = 2, 5
bNum, bDen = 3, 7

den = bDen + 1
while den <= 1000000:

	num = int(float(bNum)/float(bDen) * den)

	if den % 100000 == 0:
		print str(num) + "/" + str(den)

	if num * lDen > den * lNum and num * bDen < den * bNum:
		lNum = num
		lDen = den
#		break
#		print str(lNum) + "/" + str(lDen)
	den += 1
print "answer: " + str(lNum) + "/" + str(lDen)
