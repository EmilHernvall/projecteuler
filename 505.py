from math import floor, log, ceil

def x_real(k, depth):
    if k == 0: return 0
    elif k == 1: return 1
    elif k % 2 == 0:
        kp = k/2
        res = (3*x_real(kp, depth+1)+2*x_real(floor(kp/2), depth+1))
    elif k % 2 == 1:
        kp = (k-1)/2
        res = (2*x_real(kp, depth+1)+3*x_real(floor(kp/2), depth+1))

    #print "  "*depth + "x(%d)=%d" % (k,res)
    return res

def x_real2(k, depth):
    if k == 0: return 0, 0
    elif k == 1: return 1, 0
    elif k % 2 == 0:
        kp = k/2
        a, b = x_real2(kp, depth+1)
        res = (3*a + 2*b) % (2**60), a % (2**60)
        return res
    elif k % 2 == 1:
        kp = (k-1)/2
        a, b = x_real2(kp, depth+1)
        res = (2*a + 3*b) % (2**60), a % (2**60)
        return res

x_cache = {}
def x(k):
    #return x_real(k, 0)
    res = x_real2(k, 0)[0]
    #x_cache[res] = k
    return res

y_cache2 = {}
#mods = {2:0, 4:2, 8:2, 16:10, 32:10, 64:42, 128:42, 256:170, 512:170, 1024:682, 2048:682, 4096:2730, 8192:2730, 16384:10922, 32768:10922}
#bignum = {2:True, 4:False, 8:True, 16:False, 32:True, 64:False, 128:True, 256:False, 512:True, 1024:False, 2048:True, 4096:False, 8192:True, 16384:False, 32768:True}
mods = {}
bignum = {}
a,b=1,0
for i in xrange(1,32):
    if i % 2 == 0: b = a+b
    a *= 2
    #print a,b, i % 2 != 0
    mods[a] = b
    bignum[a] = i % 2 != 0

def y_fast(n, k, depth, bound):
    res = -1
    if k >= bound and k < n:
        numtwos = 1 << min([i for i in xrange(1, 30) if (1 << i) >= n/float(k)])
        xidx = k*numtwos + mods[numtwos]
        if bignum[numtwos]:
            #print k, numtwos, mods[numtwos], xidx, 2**60 - 1 - x(xidx)
            res = 2**60 - 1 - x(xidx)
        else:
            #print k, numtwos, mods[numtwos], xidx, x(xidx)
            res = x(xidx)

    if k >= n:
        res = x(k)
        return res
    elif res == -1:
        a, b = y_fast(n, 2*k, depth+1, bound), y_fast(n, 2*k+1, depth+1, bound)
        res = 2**60 - 1 - max(a, b)

    #y_cache2[k] = res
    return res

y_cache = {}
def y_real(n, k, depth):
    #print "  "*depth + "k=%d, treshold=%d" % (k, k >= n)
    if k >= n:
        res = x(k)
        #y_cache[k] = res
        return res
    else:
        a, b = y_real(n, 2*k, depth+1), y_real(n, 2*k+1, depth+1)
        #print a, b, a > b, k % 2 == 0
        res = 2**60 - 1 - max(a, b)
        #print "  "*depth + "a=%d,b=%d,res=%d" % (a,b,res)
        #y_cache[k] = res
        return res

def y(n, k):
    return y_real(n, k, 0)

def y2(n, k):
    return y_fast(n, k, 0, n/(pow(2,log(n)/log(10)+4)))

def A(n, y):
    return y(n, 1)

#print "x(2)=",x(2)
#print "x(3)=",x(3)
#print "x(4)=",x(4)
#print "y4(4)=",y(4,4)
#print "y4(3)=",y(4,3)-2**60
#print "y4(2)=",y(4,2)-2**60
#print "y4(1)=",y(4,1)
#print "A(10)=",A(10, y)-2**60
#print "A(100)=",A(100, y)
#print "A(10000)=",A(10000, y)
#print "A(10^12)=",A(10**12, y)

n = 1000*1000*1000*1000
#n = 10*1000*1000*1000
#print "A(",n,") =",A(n, y)
print "A(",n,") =",A(n, y2)

print "x_cache=" , len(x_cache)
print "y_cache=" , len(y_cache)
print "y_cache2=" , len(y_cache2)

#for k,y in y_cache.items():
#    if not x_cache.has_key(y):
#        v = x_cache[2**60-1-y]
#        print k,y,v,2**60-1-y,v/k,v%k
#    else:
#        v = x_cache[y]
#        print k,y,v,v/k,v%k

for k,y in y_cache.items():
    if y_cache2.has_key(k) and y != y_cache2[k]:
        print k,y,y_cache2[k],y==y_cache2[k]

#print
#for x, k in x_cache.items(): print k, ":", x
#print
#for n, k in y_calls: print n, ",", k

# 8957 8407 6555

#2 > n/k => 2 0
#4 > n/k => 4 2
#8 > n/k => 8 2
