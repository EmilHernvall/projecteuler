-- Project Euler, Problem 1, second attempt
-- Emil Hernvall, 2011-03-01

a = 3
b = 5
n_max = 1000

-- We only want to include sums smaller than n_max,
-- so in some cases we have to decrease by one.
-- For example 1000/5=200 and 200*5=1000.
-- We want the function to return 199 in this case.
uppervalue max n = let t = max `div` n
	in if t * n >= max 
	then t - 1
	else t

n_1 = uppervalue n_max a
n_2 = uppervalue n_max b
n_3 = uppervalue n_max (a*b)

sumofrange c n = c*n*(n+1) `div` 2

totalsum = sumofrange a n_1 + sumofrange b n_2 - sumofrange (a*b) n_3

main = do
	print totalsum

