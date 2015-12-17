from itertools import permutations, combinations

def is_special_sum_set(a):
    for m1 in xrange(1, 1 << len(a)):
        b = [n for i,n in enumerate(a) if (m1 & (1 << i)) > 0]
        for m2 in xrange(0, 1 << len(a)):
            if (m1 & m2) > 0: continue
            c = [n for i,n in enumerate(a) if (m2 & (1 << i)) > 0]
            if len(b) > len(c) and sum(b) <= sum(c): return False
            #if len(b) != len(c): continue
            #if len(b) == 1 or len(c) == 1: continue
            if sum(b) == sum(c): return False

    return True

with open('p105_sets.txt', 'r') as fh:
    total = 0
    for l in fh:
        s = map(int, l.strip().split(","))
        print len(s), s
        if is_special_sum_set(s):
            total += sum(s)
            print "YES"

    print total
