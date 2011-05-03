def f(n, lookup):
    if n == 1 or n == 89:
        return n

    sum = 0
    for c in str(n):
        sum += int(c)**2

    if lookup.has_key(sum):
        return lookup[sum]

    res = f(sum, lookup)
    lookup[sum] = res
    return res

lookup = {}
count = 0
for i in range(1, 10000000):
    if i % 100000 == 0:
        print i
    v = f(i, lookup)
    if v == 89:
        count += 1

print "count: " + str(count)

