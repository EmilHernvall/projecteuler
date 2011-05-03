# this was stolen from http://code.activestate.com/recipes/66463/
# see comment #2
def permute(a):
   if len(a)==1:
      yield a
   else:
      for i in range(len(a)):
         this = [a[i]]
         rest = a[:i] + a[i+1:]
         for p in permute(rest):
            yield this + p

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

# permute operators for a set of integers
# to calculate all possible combinations
# for these values
def calculate(values, prev):
    if len(values) == 0:
        if prev < 0:
            prev = -prev

        if prev != int(prev) or prev == 0:
            return set()

        prev = int(prev)
        
        return set([prev])

    funcs = [add,sub,mul,div]
    cur = values[0]

    res = set()
    for func in funcs:
        if prev == None:
            new = cur
        else:
            try:
                new = func(cur, prev)
            except:
                pass
            
        res = res.union(calculate(values[1:], new))

    return res

# permute the provided set of values and calculate the
# boundary for a combined set of all permutations
def boundary(values):
    values = map(lambda x: float(x), values)
    
    calculated = set()
    for p in permute(values):
        res = calculate(p, None)
        calculated = calculated.union(res)

    calculated = list(calculated)
    calculated.sort()
    for i, n in enumerate(calculated):
        if i + 1 != n:
            break

    return i

# calculate sets of integers with the property
# a < b < c < d up to an limit and calculate the
# boundary for each such set. pick the maximum.
def problem93():
    # this is the one arbitrary value in this algorithm. :/
    upper = 9

    maxValues = []
    maxBoundary = 0
    for a in xrange(4, upper):
        for b in xrange(3, a):
            for c in xrange(2, b):
                for d in xrange(1, c):
                    values = [d,c,b,a]
                    b = boundary(values)

                    if b > maxBoundary:
                        maxBoundary = b
                        maxValues = values

    print "max: %s => %d" % (",".join([str(v) for v in maxValues]), maxBoundary)

if __name__ == "__main__":
    problem93()

