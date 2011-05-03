# http://www.research.att.com/~njas/sequences/A018892

def factorize(n):
    i = 2
    factors = []
    while n > 1:
        if n % i == 0:
            factors.append(i)
            n = n / i
        else:
            i = i + 1
    return factors

def nSol(n):
	factors = factorize(n)
	factors2 = {}
	for factor in factors:
		if factors2.has_key(factor):
			factors2[factor] += 1
		else:
			factors2[factor] = 1

	a = 1
	for k in factors2:
		a *= 2*factors2[k]+1
	a += 1
	a /= 2

	return a

print nSol(2*3*5*7*11*13*17*19*23*29*31*37*41*43*47)
print nSol(2*2*2*3*5*7*11*13*17*19*23*29*31*37*41*43)
print nSol(2*2*2*2*2*2*2*2*3*5*7*11*13*17*19*23*29*31*37*41)
print nSol(2*2*2*2*2*2*2*2*3*3*3*3*5*7*11*13*17*19*23*29*31*37)
print nSol(2*2*2*2*2*2*3*3*3*3*3*5*7*11*13*17*19*23*29*31*37)
print nSol(2*2*2*2*3*3*3*3*3*5*5*7*11*13*17*19*23*29*31*37)
print nSol(2*2*2*2*3*3*3*5*5*5*7*11*13*17*19*23*29*31*37)
print nSol(2*2*2*2*2*3*3*5*5*7*7*11*13*17*19*23*29*31*37)
print nSol(2*2*2*3*3*3*5*5*7*7*11*13*17*19*23*29*31*37)
