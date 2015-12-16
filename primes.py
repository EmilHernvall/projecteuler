import math

def eprimes(max):
    sieve = range(0, max)
    pos = 2
    primes = []
    while pos != max:
        while pos < max and sieve[pos] == 0:
            pos += 1

        if pos == max:
            break;

        n = sieve[pos]
        sieve[pos] = 0
        primes.append(n)

        i = pos
        while i < max:
            sieve[i] = 0
            i += n

    return primes

def primes2(limit):
    sieve = range(0, limit+1)
    for i in xrange(2, limit+1):
        if sieve[i] == 0: continue
        for j in xrange(2*i, limit+1, i): sieve[j] = 0
    return [x for x in sieve[2:] if x > 0]

def primes(limit):
    sieveBound = (limit-1)/2+1
    crossLimit = (int(math.sqrt(limit))-1) / 2

    sieve = range(0, sieveBound)
    for i in xrange(1, crossLimit + 1):
        if sieve[i] == 0: continue

        for j in xrange(2*i*(i+1), sieveBound, 2*i+1):
            sieve[j] = 0

    return [2] + [2*x+1 for x in sieve[1:sieveBound] if x > 0]

if __name__ == "__main__":
    print primes(20)
    print primes2(20)
