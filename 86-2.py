from math import sqrt

def pyth(M):
    stack = [(3,4,5)]
    while len(stack) > 0:
        a,b,c = stack.pop()

        if a > M or b > M: continue
        yield a,b,c

        stack.insert(0, (1*a - 2*b + 2*c, 2*a - 1*b + 2*c, 2*a - 2*b + 3*c))
        stack.insert(0, (1*a + 2*b + 2*c, 2*a + 1*b + 2*c, 2*a + 2*b + 3*c))
        stack.insert(0, (-1*a + 2*b + 2*c, -2*a + 1*b + 2*c, -2*a + 2*b + 3*c))

def check_valid(a, b, c):
    d = a**2 + b**2 + c**2 + 2*min(a*b, a*c, b*c)
    ds = int(sqrt(d))
    return ds*ds == d

def get_count_for_cuboid(M):
    total = 0
    for i, (a,b,c) in enumerate(pyth(2*M)):
        n = 1
        while True:
            a2, b2 = min(n*a, n*b), max(n*a, n*b)
            if a2 > M and b2 > M: break
            total += len([1 for x in xrange(1, a2/2+1)
                          if b2 <= M and check_valid(x, a2-x, b2)])
            total += len([1 for x in xrange(1, b2/2+1)
                          if b2-x <= a2 and a2 <= M and check_valid(x, b2-x, a2)])
            n += 1

    return total

M = 1
last_below = M
step_size = 1024
while True:
    num = get_count_for_cuboid(M)
    print M, num
    if num > 1000000:
        if step_size == 1: break
        print "moving back to %d, now stepping with size %d" % (last_below+step_size/2, step_size/2)
        M = last_below+step_size/2
        step_size /= 2
    else:
        last_below = M
        M += step_size
