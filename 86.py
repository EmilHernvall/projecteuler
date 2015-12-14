# (a+b)^2 + c^2
# (a+c)^2 + b^2
# (b+c)^2 + a^2

from math import sqrt

M = 100
total = 0
for a in xrange(1, M+1):
    for b in xrange(a, M+1):
        for c in xrange(b, M+1):
            d = min((a+b)**2 + c**2,
                    (a+c)**2 + b**2,
                    (b+c)**2 + a**2)

            ds = int(sqrt(d))
            if ds*ds == d: total += 1

print total
