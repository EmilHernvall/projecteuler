c = ((sqrt(5)+1)/2)^3

evenseries :: Integer -> Integer -> Integer
evenseries n m = let next = round (c*(fromIntegral n))
	in if next < m then next + evenseries next m
	else 0
evenfibonacci m = 2 + evenseries 2 m

total = evenfibonacci 4000000

main = do
	print c
	print total
