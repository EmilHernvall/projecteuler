import math

max = 2000000
sieve = range(0, max)
pos = 2
sum = 0
while pos != max:
    while pos < max and sieve[pos] == 0:
        pos += 1
    if pos == max:
        break;
    
    n = sieve[pos]
    sieve[pos] = 0
    sum += n
    
    i = pos
    while i < max:
        sieve[i] = 0
        i += n

print "sum: " + str(sum)

