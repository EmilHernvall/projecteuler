import math

def factorize(m):
    n = m
    i = 2
    factors = 1
    found = 0
    while n > 1:
        if n % i == 0:
            if factors % i != 0:
                factors *= i
                found += 1
            n = n / i
        else:
            i = i + 1

    return found

i = 1
consecutive = 0
n = 3
while True:
    if i % 1000 == 0:
        print "Progress: " + str(i)

    factors = factorize(i)
    if factors == n:
        consecutive += 1
        if consecutive == n:
            print i - n + 1
            break
    else:
        consecutive = 0
    i += 1
