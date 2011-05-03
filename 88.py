import math
import factorize
import copy

def product(a):
    return reduce(lambda x,y: x*y, a)

def solve(n):
	i = 2*n
	log2 = math.floor(math.log(n, 2))
	minSum = n + log2
	minSol = ()
	while i > minSum:
		factors = factorize.factorize(i)
		if sum(factors) > i:
			i -= 1
			continue
		if len(factors) <= 1:
			i -= 1
			continue
		if len(factors) == 2 and sum(factors) + n - 2 != i:
			i -= 1
			continue
		print i
#		for factor in factors:
#			print "\t" + str(factor)
		if sum(factors) + n - len(factors) == i:
			minSol = min(minSol, i)
			print "\tsolution: " + str(i)
			i -= 1
			continue
		if valid(i, n):
			minSol = min(minSol, i)
			print "\tsolution: " + str(i)
		i -= 1
	print "min: " + str(n) + " => " + str(minSol)

def valid(n, p):
	divisors = factorize.divisors(n)
	return validRecurse(divisors, [], p)
	
def validRecurse(divisors, usedDivisors, p):
#	print usedDivisors

	avai = list(set(divisors).difference(set(usedDivisors)))
	avai.sort()

#	print usedDivisors

	if len(usedDivisors) > 0:
		currentProduct = product(usedDivisors)
		currentSum = sum(usedDivisors)
		if currentProduct == currentSum + p - len(usedDivisors):
			return True
		elif currentProduct > currentSum + p - len(usedDivisors):
			return False
		m = max(usedDivisors)
	else:
		currentProduct = 1
		currentSum = 0
		m = 0

	for divisor in avai:
		if divisor < m or currentProduct * divisor > 2*p:
			continue

		if validRecurse(divisors, usedDivisors+[divisor], p):
			return True

	return False

solve(12000)
#for i in range(1,50):
#	solve(i)
#print valid(30, 19)
