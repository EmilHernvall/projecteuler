import factorize

def product(a):
    return reduce(lambda x,y: x*y, a)

def validRecurse(divisors, usedDivisors):
    global upper, nums, prodSums

    if len(usedDivisors) > 0:
#        print usedDivisors
        currentProduct = product(usedDivisors)
        currentSum = sum(usedDivisors)
        if currentProduct > 2 * upper:
            return False
        p = currentProduct - currentSum + len(usedDivisors)
        if p in nums:
            nums.remove(p)
        if prodSums.has_key(p):
            prodSums[p] = min(prodSums[p], currentProduct)
        else:
            prodSums[p] = currentProduct
#        print "\t" + str(p)
        m = max(usedDivisors)
    else:
        currentProduct = 1
        currentSum = 0
        m = 0

    for divisor in divisors:
        if divisor < m or currentProduct * divisor > 2*upper:
            continue

        if validRecurse(divisors, usedDivisors+[divisor]):
            pass

    return False

upper = 12000
nums = set(range(3, upper+1))
prodSums = {}

i = 2
while i < upper:
    print i
#	divisors = factorize.multipleDivisors(i)
    divisors = set(factorize.divisors(i))
    divisors.remove(1)
    validRecurse(list(divisors), [])
#	print nums
    i += 1

res = set()
for k, v in prodSums.iteritems():
	if k >= 2 and k <= upper:
		res.add(v)

print res
print sum(res)
