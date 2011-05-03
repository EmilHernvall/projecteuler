import math

def rotate(n):
    if len(n) == 1:
        return n
    return n[1:] + n[0]

def isPrime(n):
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            return False
        i = i + 1
    return True

max = 1000000
sieve = range(0, max)
pos = 2
primes = set()
while pos != max:
    while pos < max and sieve[pos] == 0:
        pos += 1
    if pos == max:
        break;
    
    n = sieve[pos]
    sieve[pos] = 0
    primes.add(n)
    
    i = pos
    while i < max:
        if i % n == 0:
            sieve[i] = 0
        i += n

print "done calculating primes."

count = 0
for p in primes:
    q = rotate(str(p))
    circular = True
    while str(p) != q:
        if int(q) < max and not int(q) in primes:
            circular = False
            break
        elif int(q) > max and not isPrime(int(q)):
            circular = False
            break
        q = rotate(q)
    if circular:
        print p
        count += 1
print "count: " + str(count)

