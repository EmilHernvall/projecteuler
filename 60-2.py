import math

def isPrime(n):
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            return False
        i = i + 1
    return True

def ConcatPermute(termList):
	permutations = []
	for i, t in enumerate(termList):
		for j, u in enumerate(termList[i+1:]):
			permutations.append(t+u)
			permutations.append(u+t)
	return permutations

#3
#7
#673
#823
#541
#229
#109

for p in ConcatPermute(["3","7","823","541"]):
	if not isPrime(int(p)):
		print "fail: " + p
	else:
		print p

