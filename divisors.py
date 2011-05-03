def d(n):
	i = 2
	divisors = []
	max = n
	while i <= max:
		if n % i == 0:
			if i == max:
				break

			max = n / i
			divisors.append(i)
			if i != max:
				divisors.append(max)
		i = i + 1

	return divisors

