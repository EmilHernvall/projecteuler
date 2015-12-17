from itertools import permutations, combinations
from collections import defaultdict, Counter

def find_sss_comparisons(a):
    total, test_count = 0, 0
    for m1 in xrange(1, 1 << len(a)):
        b = [n for i,n in enumerate(a) if (m1 & (1 << i)) > 0]
        b2 = [i for i,n in enumerate(a) if (m1 & (1 << i)) > 0]
        for m2 in xrange(m1+1, 1 << len(a)):
            if (m1 & m2) > 0: continue
            total += 1
            c = [n for i,n in enumerate(a) if (m2 & (1 << i)) > 0]
            c2 = [i for i,n in enumerate(a) if (m2 & (1 << i)) > 0]
            # sets of the different size are guaranteed to be unequal
            if len(b) != len(c): continue
            # we need only consider subsets which do not overlap
            if not False in [p < q for p,q in zip(b2, c2)]: continue
            test_count += 1
            if sum(b) == sum(c): return False
            #print b,sum(b),c,sum(c),sum(b)-sum(c)

    return total, test_count

print "n=12 total=%d comparisons=%d" % find_sss_comparisons(sorted([1219, 1183, 1182, 1115, 1035, 1186, 591, 1197, 1167, 887, 1184, 1175]))
print "n=7 total=%d comparisons=%d" % find_sss_comparisons(sorted([81,88,75,42,87,84,86]))
print "n=6 total=%d comparisons=%d" % find_sss_comparisons(sorted([81,88,75,42,87,84]))
print "n=5 total=%d comparisons=%d" % find_sss_comparisons(sorted([81,88,75,42,87]))
print "n=4 total=%d comparisons=%d" % find_sss_comparisons(sorted([81,88,75,42]))
