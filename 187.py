f = open("50mprimes.txt", "r")

primes = []
while True:
	l = f.readline()
	if l == "":
		break
	primes.append(int(l))

print "finished loading primes: " + str(len(primes))

counter = 0
for p in primes:
	print p
	if p*p > 100000000:
		break

	for q in primes:
		if q < p:
			continue
		n = p*q
		if n > 100000000:
			break
		counter += 1
print "count: " + str(counter)
