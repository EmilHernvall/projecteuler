import math

upperBound = 1000000
divisors = {}
for i in range(2, int(math.sqrt(upperBound))+1):
    upper = int(math.floor(upperBound/i))+1
    print i
    for j in range(i, upper):
        v = i*j
        if divisors.has_key(v):
            divisors[v].append(i)
            divisors[v].append(j)
        else:
            divisors[v] = [i, j]


print "done."
print

maxLen = 0
maxV = 0
done = set()
for i in range(2, upperBound):
    if i in done:
        continue

    n = i
    sum = 0
    prev = [n]
    while True:
        sum = 1
        if not divisors.has_key(n):
            prev.append(1)
            break

        for j in divisors[n]:
            sum += j

        if sum > upperBound:
            break

        if sum in prev:
            break

        n = sum
        prev.append(sum)

    if sum == i:
        done = done.union(set(prev))

        print i
        print prev
        if len(prev) > maxLen:
            maxLen = len(prev)
            maxV = min(prev)

print "max: " + str(maxV) + " gives " + str(maxLen) + " steps"

