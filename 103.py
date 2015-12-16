from itertools import permutations, combinations

def is_special_sum_set(a):
    pairs, eqtest = 0, 0
    for m1 in xrange(1, 1 << len(a)):
        b = [n for i,n in enumerate(a) if (m1 & (1 << i)) > 0]
        for m2 in xrange(1, 1 << len(a)):
            if (m1 & m2) > 0: continue
            c = [n for i,n in enumerate(a) if (m2 & (1 << i)) > 0]
            if len(b) > len(c) and sum(b) <= sum(c): return False
            if sum(b) == sum(c): return False

    return True

def set_iterator():
    yield [1]

    s = [1, 2]
    while True:
        yield s

        p = len(s)/2
        n = s[p]
        s = [n] + [x+n for x in s]

def find_min():

    #bounds = {}
    #for i,x in enumerate(set_iterator()):
    #    if i > 10: break
    #    print i+1, x, sum(x)
    #    bounds[i+1] = sum(x)

    def build_set(n, r, l):
        if n == 0:
            if is_special_sum_set(l):
                return [l]

        s = len(l) > 0 and l[-1] or 1
        result = []
        for x in xrange(s, r+1):
            if x in l: continue
            for l2 in build_set(n-1, r-x, l + [x]):
                result.append(l2)

        return result

    me = 50
    pairs = [(x, y) for x in xrange(1, me) for y in xrange(x, me) if x != y]
    triplets1 = [(x, y, z) for x, y in pairs for z in xrange(y, 40) if x+y != z]
    triplets2 = [(x, y, z) for x, y in pairs for z in xrange(y, me) if x+y != z and x >= 39]

    def check_quad(p):
        if p[0]+p[2] == p[1]: return False
        if p[0]+p[1] == p[3]: return False
        if p[0]+p[1] == p[2] + p[3]: return False
        if p[0]+p[2] == p[1] + p[3]: return False
        if p[0]+p[3] == p[1] + p[2]: return False
        if p[0]+p[1] < p[3]: return False
        if p[0]+p[2] < p[3]: return False
        if p[1]+p[2] < p[3]: return False

        return True

    quads = set()
    print "doing four"
    for i, p1 in enumerate(pairs):
        for p2 in pairs:
            if p1[-1] >= p2[0]: continue
            p3 = p1 + p2
            if not check_quad(p3): continue
            quads.add(p3)

    print "%d quads" % (len(quads),)

    print "doing six"
    sixlets = []
    for i, p1 in enumerate(triplets1):
        if i % 1000 == 0: print "%d/%d" % (i,len(triplets1))

        for p2 in triplets2:
            if p1[-1] >= p2[0]: continue
            p3 = p1 + p2
            if not p3[0:4] in quads: continue
            if not tuple(p3[1:5]) in quads: continue
            if not tuple(p3[2:6]) in quads: continue
            if is_special_sum_set(p3):
                sixlets.append(p3)
                #print p3, sum(p3)

    print "%d sixlets" % (len(sixlets),)

    print "doing seven"
    for i, p1 in enumerate(sixlets):
        for n in xrange(p1[-1], 60):
            p2 = list(p1) + [n]
            if is_special_sum_set(p2):
                print p2, sum(p2)
                return p2

find_min()
