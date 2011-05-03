c = ((sqrt(5)+1)/2)^3

evenfibonacci :: [Integer] -> Integer -> [Integer]
evenfibonacci (n:ns) m = let next = round (c*(fromIntegral n))
	in if next < m then evenfibonacci (next:n:ns) m
	else n:ns
evenfibonacci [] m = evenfibonacci [2] m

total = evenfibonacci [] 4000000

main = do
	print c
	print total
	print (sum total)
