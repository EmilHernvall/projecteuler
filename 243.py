from factorize import factorize
from itertools import combinations
from primes import primes2

def gcd(a, b):
    if b == 0: return a
    else: return gcd(b, a % b)

def resilience(den):
    return len([1 for num in xrange(0, den) if gcd(den, num) == 1]),float(den-1)

def smallest(bound):
    n = 2
    so_far = 1
    res_cache = {}
    while True:
        num,den = resilience(n)
        r = num/float(den)
        so_far = min(so_far, r)
        if so_far == r:
            #print "*******"
            print n, bound, r, "%d/%d" % (num,den)
        if r < bound: return n
        n += 1

print smallest(4.0/10.0)
print smallest(15499.0/94744.0)
