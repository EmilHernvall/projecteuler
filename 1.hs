-- Project Euler, Problem 1
-- Emil Hernvall, 2011-03-01

a = 3
b = 5
n_max = 1000

uppervalue max n = fromIntegral (ceiling (max / n) - 1)

n_1 = uppervalue n_max a
n_2 = uppervalue n_max b
n_3 = uppervalue n_max (a*b)

sumofrange c n = c*n*(n+1)/2

totalsum = (sumofrange a n_1) + (sumofrange b n_2) - (sumofrange (a*b) n_3)

main = do
	print totalsum

