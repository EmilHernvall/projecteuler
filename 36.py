
def Denary2Binary(n):
    bStr = ''
    if n < 0:  raise ValueError, "must be a positive integer"
    if n == 0: return '0'
    while n > 0:
        bStr = str(n % 2) + bStr
        n = n >> 1
    return bStr

def reverse(str):
	str2 = ""
	for c in str:
		str2 = c + str2
	return str2

sum = 0
i = 0
while i < 1000000:
	if str(i) == reverse(str(i)):
		bin = Denary2Binary(i)
		if bin == reverse(bin):
			sum += i
			print str(i) + " " + bin
	i += 1
print "sum: " + str(sum)
