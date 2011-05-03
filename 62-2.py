import math

def mySplit(inStr):
    arr = []
    for c in inStr:
        arr.append(c)

    return arr

i = 1
counts = {}
while True:
    currentCube = i ** 3

    logCurrentCube = math.floor(math.log(currentCube,10))

    arrCurrentCube = mySplit(str(currentCube))
    arrCurrentCube.sort()
    strSortedCurrentCube = "".join(arrCurrentCube)

    if counts.has_key(strSortedCurrentCube):
        if not i in counts[strSortedCurrentCube]:
            counts[strSortedCurrentCube].append(i)
    else:
        counts[strSortedCurrentCube] = [i]

    if len(counts[strSortedCurrentCube]) == 5:
        print counts[strSortedCurrentCube]
        print "Mincube: " + str(counts[strSortedCurrentCube][0] ** 3)
        break

    i += 1
