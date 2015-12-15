from itertools import combinations

SQUARES = [("%02d" % (x*x,)).replace("6","x").replace("9","x") for x in xrange(1, 10)]

def normalize(p): return [x in (6,9) and "x" or str(x) for x in p]
def check_solution(p,q):
    p, q = normalize(p), normalize(q)
    return len([1 for a,b in SQUARES if (a in p and b in q) or
                                        (a in q and b in p)]) == len(SQUARES)

digits = [int(x) for x in "0123456789"]
solutions = set()
for x in combinations(digits, 6):
    for y in combinations(digits, 6):
        if (y, x) in solutions: continue
        if check_solution(x,y):
            solutions.add((x, y))

print len(solutions)
