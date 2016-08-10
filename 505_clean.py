from math import floor, log, ceil

def x(k):
    def x_fast(k):
        if k == 0: return 0, 0
        elif k == 1: return 1, 0
        elif k % 2 == 0:
            kp = k/2
            a, b = x_fast(kp)
            return (3*a + 2*b) % (2**60), a
        elif k % 2 == 1:
            kp = (k-1)/2
            a, b = x_fast(kp)
            return (2*a + 3*b) % (2**60), a

    return x_fast(k)[0]

mods = {}
bignum = {}
a,b=1,0
for i in xrange(1,32):
    if i % 2 == 0: b = a+b
    a *= 2
    mods[a] = b
    bignum[a] = i % 2 != 0

def y(n, k):
    bound = n/(pow(2,log(n)/log(10)))
    def y_fast(k):
        if k >= bound and k < n:
            numtwos = 1 << min([i for i in xrange(1, 30) if (1 << i) >= n/float(k)])
            xidx = k*numtwos + mods[numtwos]
            if bignum[numtwos]: return 2**60 - 1 - x(xidx)
            else: return x(xidx)

        if k >= n: return x(k)
        else: return 2**60 - 1 - max(y_fast(2*k), y_fast(2*k+1))

    return y_fast(k)

def A(n):
    return y(n, 1)

n = 1000*1000*1000*1000
#n = 1000
print "A(",n,") =",y(n, 1)
#print "y(",n,", 2 ) =",y(n, 2)

