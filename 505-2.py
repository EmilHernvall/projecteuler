from math import floor

def x(n, depth=0):
    if n == 0: return 0
    elif n == 1: return 1
    elif n % 2 == 0:
        k = n/2.0
        return (3*x(k) + 2*x(floor(k/2))) % 2**60
    elif n % 2 == 1:
        k = (n-1)/2.0
        return (2*x(k) + 3*x(floor(k/2))) % 2**60

def fastx(n,debug=False):
    def helper(n):
        if debug: print "\t",n
        if n == 0: return 0, 0
        elif n == 1: return 1, 0
        elif n % 2 == 0:
            a, b = helper(n/2.0)
            return (3*a + 2*b) % 2**60, a
        elif n % 2 == 1:
            a, b = helper((n-1)/2.0)
            return (2*a + 3*b) % 2**60, a

    return helper(n)[0]

def y(n, k, depth=0, x0 = 0, x1 = 0):
    if k == 0: x = 0
    elif k == 1: x = 1
    elif k % 2 == 0: x = 2*x0 + 3*x1
    else: x = 3*x0 + 2*x1

    if k >= n:
        #res, reslist = fastx(k), []
        res, reslist = x, []
        print "  "*depth + "x(%d)=%d" % (k,res)
    else:
        (a,l1),(b,l2) = y(n, 2*k, depth=depth+1,x0=x1, x1=x), y(n, 2*k+1, depth=depth+1, x0=x1, x1=x)
        if a > b:
            res, reslist = 2**60 - 1 - a, l1
        else:
            res, reslist = 2**60 - 1 - b, l2
        print "  "*depth + "y(%d)=%d (%d), x=%d" % (k,res, (2**60 - 1 - res), x)

    reslist.append((k, res))
    return res, reslist

def y2(n, k, x0 = 0, x1 = 0, depth=0):
    if k == 0: x = 0
    elif k == 1: x = 1
    elif k % 2 == 0: x = 2*x0 + 3*x1
    else: x = 3*x0 + 2*x1

    if k >= n: return x
    else: return 2**60 - 1 - max(y2(n, 2*k, x0=x1, x1=x),
                                 y2(n, 2*k+1, x0=x1, x1=x))
    #else:
    #    if depth % 2 == 0:
    #        if x0 <= x1:
    #            a = y2(n, 2*k, x0=x1, x1=x, depth=depth+1)
    #        else:
    #            a = y2(n, 2*k+1, x0=x1, x1=x, depth=depth+1)
    #    else:
    #        if x0 >= x1:
    #            a = y2(n, 2*k, x0=x1, x1=x, depth=depth+1)
    #        else:
    #            a = y2(n, 2*k+1, x0=x1, x1=x, depth=depth+1)

    #    return 2**60 - 1 - a

def A(n, y):
    return y(n, 1)

n = 10
print A(n, y)
#print A(n, y2)
print

#for n in [1,2,3,4,5,6,7,8,9]: #xrange(1, 100):
#    res = fastx(n,debug=False)
#    print n,res
#for a in xrange(1, 100):
#    for b in xrange(1, 100):
#        if b > a: continue
#        print a,b,x(a),x(b),x(a+b),x(a-b),x(a*b),x(a)*x(b),a*x(b),b*x(a)
