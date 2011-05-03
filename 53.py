max = 100

print "precalculating factorials"
factorials = [1]
current = 1
for i in range(1, max + 1):
    current *= i
    factorials.append(current)

print "done.."
print

counter = 0
for n in range(1, max + 1):
    for r in range(1, n):
        over = factorials[n]
        under = factorials[r] * factorials[n-r]

        if over/under >= 1000000:
            counter += 1
print "count: " + str(counter)

