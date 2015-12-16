from factorize import factorize
from itertools import combinations_with_replacement, groupby
from primes import primes2
from operator import mul

def smallest(bound):
    so_far = 1
    primelist = primes2(1000000)
    primeset = set(primelist)
    for i in xrange(1, len(primeset)):
        # i+2 arbitrarily chosen because it happens to give correct answer
        for n in combinations_with_replacement(primelist[0:i], i+2):
            n = reduce(mul, n)
            den = n-1
            if n in primeset: num = n-1
            else: num = reduce(mul, [(a-1) * a**(len(list(b))-1)
                                     for a,b in groupby(factorize(n), lambda x: x)])

            r = num/float(den)

            so_far = min(so_far, r)
            if so_far == r: print n, bound, r, "%d/%d" % (num,den)

            if r < bound: return n

print smallest(15499.0/94744.0)
