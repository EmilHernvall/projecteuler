import primes

def replace(permstr, digit, depth, resset):
    if depth >= len(permstr):
        return

    for i in range(0, len(permstr)):
        newstr = permstr[0:i] + digit + permstr[i+1:]
        if not newstr in resset:
            resset.add(newstr)
            replace(newstr, digit, depth+1, resset)

    return resset

def validate(a, b):
    first = ""
    for i, c in enumerate(a):
        if b[i] == "x":
            if first == "":
                first = c
            elif c != first:
                return False
    return True

max = 1000000
primes = primes.primes(max)
        
print "done calculating primes"

tbl = {}
for p in primes:
    found = False
    permSet = replace(str(p), "x", 0, set())
    for perm in permSet:
        if not validate(str(p), perm):
            continue
        
        if tbl.has_key(perm):
            tbl[perm].append(p)
            if len(tbl[perm]) == 8:
                for p in tbl[perm]:
                    print p
                found = True
                break
        else:
            tbl[perm] = [p]
    if found:
        break


