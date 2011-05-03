def isPandigital(n):
    l = list(str(n))
    l.sort()
    l = map(lambda x: int(x), l)

    return l == [1,2,3,4,5,6,7,8,9]

a = 1
n = 3

lastA, lastB = 1, 1
#for i in range(1, 2753):
while True:
    a = int((a*16180339887498948482+5000000000000000000)/10000000000000000000)
    if a > 10**20:
        a = int(a/10)

    c = (lastA + lastB) % 10**9

    first = int(str(a)[0:9])

    if isPandigital(first) or isPandigital(c):
        print str(n) + ": " + str(first) + "..." + str(c)
        if isPandigital(first):
            print "Pandigital first"

        if isPandigital(c):
            print "Pandigital last"

    if isPandigital(first) and isPandigital(c):
        break

    lastA, lastB = lastB, c
    n += 1

