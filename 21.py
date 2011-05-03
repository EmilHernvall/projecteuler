def d(n):
	i = 2
	sum = 1
	max = n
	while i <= max:
		if n % i == 0:
			if i == max:
				break

			max = n / i
			sum += i + max
		i = i + 1

	return sum

def amicable(n):
	res = d(n)
	if res == n:
		return False

	if d(res) == n:
		print str(j) + " is amicable with " + str(res) + "."
		return True
	else:
		return False
	
sum = 0
for j in range(1,10001):
	if amicable(j):
		sum += j

print
print "sum: " + str(sum)
