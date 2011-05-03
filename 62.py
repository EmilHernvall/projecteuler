import math

def mySplit(inStr):
    arr = []
    for c in inStr:
        arr.append(c)

    return arr

i = 1
cubes = []
currentMin = ()
toBeat = ()
minSet = []
while True:
    if i % 100 == 0:
        print str(i) + " (cubes count: " + str(len(cubes)) + ")"
    
    currentCube = i ** 3

    if currentCube > toBeat:
        break

    logCurrentCube = math.floor(math.log(currentCube,10))

    arrCurrentCube = mySplit(str(currentCube))
    arrCurrentCube.sort()
    strSortedCurrentCube = "".join(arrCurrentCube)

    currentSet = [i]
    newCubes = []
    currentMax = 0
    for cube in cubes:

        if math.floor(math.log(cube,10)) == logCurrentCube:
            newCubes.append(cube)
        else:
            continue
        
        arrCube = mySplit(str(cube))
        arrCube.sort()
        strCube = "".join(arrCube)

        if strCube == strSortedCurrentCube:
            currentSet.append(int(round(cube ** (1.0/3.0))))

            arrCube.reverse()
            reversedCube = int("".join(arrCube))
            if reversedCube > currentMax:
                currentMax = reversedCube

    if len(currentSet) == 4:
        if currentCube < currentMin:        
            currentSet.sort()
            print currentSet
            print "searching until " + str(currentMax)
            currentMin = currentCube
            minSet = currentSet
            toBeat = currentMax

    cubes = newCubes
    cubes.append(currentCube)
    i += 1

print "i: " + str(i)
print "min: "
print minSet

