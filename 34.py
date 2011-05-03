def factorial(f):
    if f == 0:
        return 1
    elif f == 1:
        return 1
    else:
        return f*factorial(f-1)

factorials = []
for i in range(0,10):
    factorials.append(factorial(i))

totalSum = 0
max = 7*factorials[9]
i = 10
while i < max:
    sum = 0
    for c in str(i):
        n = ord(c) - ord("0")
        f = factorials[n]
        if f > i:
            break
        sum += f
    if sum == i:
        print "\tmatch: " + str(i)
        totalSum += sum
    i += 1
print "totalsum: " + str(totalSum)

