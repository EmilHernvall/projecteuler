keyLSD = { 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 
	11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty' }
keyTen = { 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety' }

sum = 0
for i in range(1, 1000):
	num = ""
	if (i >= 100):
		tmp = i - i % 100 
		num += keyLSD[tmp/100] + " hundred"
		if i%100 > 0:
			num += " and "

	if ((i%100) > 20):
		tmp = i % 100
		tmp = tmp - (tmp % 10)
		num += keyTen[tmp]
		if i % 10 != 0:
			num += "-" + keyLSD[i%10]
	elif i%100 == 20:
		num += keyLSD[20]
	elif i%20 != 0:
		num += keyLSD[i%20]

	numLen = len(num.replace(" ","").replace("-",""))
	print num + ": " + str(numLen)
	sum += numLen

sum += len("one thousand") - 1

print "len: " + str(sum)
