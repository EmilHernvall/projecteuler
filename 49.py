import primes

def f(a, b):
    a = str(a)
    b = str(b)
    if len(a) != len(b):
        return False

    ok = True
    for c in a:
        if not c in b:
            ok = False
            break

    for c in b:
        if not c in a:
            ok = False
            break

    return ok

primes = primes.primes(10000)
print "done calculating primes: " + str(len(primes))

for p in primes:
    if p < 1000:
        continue
    for q in primes:
        if q <= p:
            continue
        if f(p, q):
            r = 2 * q - p
            if f(r, p) and r in primes:
                print str(p) + " " + str(q) + " " + str(r)
