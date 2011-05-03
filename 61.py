import math

triangle = 0
square = 0
pentagonal = 0
hexagonal = 0
heptagonal = 0
octagonal = 0

n = 0
nums = []
lookupTable = {}
types = {}
while triangle < 10000:
    triangle = n * (n + 1) / 2
    square = n ** 2
    pentagonal = n * (3 * n - 1) / 2
    hexagonal = n * (2 * n - 1)
    heptagonal = n * (5 * n - 3) / 2
    octagonal = n * (3 * n - 2)

    for i, num in enumerate([triangle, square, pentagonal,
                             hexagonal, heptagonal, octagonal]):
        
        if num >= 1000 and num < 10000 and not num in nums:
            nums.append(num)
            sNum = str(num)
            key = sNum[0:2]
            if not lookupTable.has_key(key):
                newSet = set()
                newSet.add(num)
                lookupTable[key] = newSet
            else:
                lookupTable[key].add(num)
                
            if not types.has_key(num):
                types[num] = 1 << i
            else:
                types[num] = types[num] | (i << i)
    
    n += 1

nums.sort()

def recurse(lookupTable, num, arr, level):
    if level > 5:
        return [arr]
    
    result = []
    sNum = str(num)
    key = sNum[2:]
    if lookupTable.has_key(key):
        for match in lookupTable[key]:
            if match in arr:
                continue
            result += recurse(lookupTable, match, arr + [match], level + 1)

    return result
            

candidates = []
for num in nums:
    arr = [ num ]
    results = recurse(lookupTable, num, arr, 1)
    for result in results:
        if len(result) == 0:
            continue
        
        if not str(result[0])[0:2] == str(result[-1])[2:]:
            continue

        strArr = []
        for n in result:
            strArr.append(str(n))

        strArr.sort()
        strResult = ",".join(strArr)

        if strResult not in candidates:
            typesInResult = set()
            for n in result:
                typesInResult.add(types[n])

            if len(typesInResult) == len(result):
                print result
                sum = 0
                for n in result:
                    sum += n
                    print "\t" + str(n) + ": " + str(int(math.log(types[n],2)+2))
                candidates.append(strResult)
                print "\tsum: " + str(sum)
