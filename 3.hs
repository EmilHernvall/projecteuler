n = 600851475143

factor :: Integer -> [Integer]
factor x = let searchUntil = (truncate (sqrt (fromIntegral x)))
	in filter (\y -> x `mod` y == 0) [2..searchUntil]

primefactor2 :: [Integer] -> [Integer] -> [Integer]
primefactor2 x (y:ys) = let rem = (filter (\s -> y `mod` s == 0) x)
                            next = (primefactor2 (y:x) ys)
	in if (length rem) == 0 then [y] ++ next
	else next
primefactor2 x [] = []

primefactor :: Integer -> [Integer]
primefactor n = primefactor2 [] (factor n)

factors = primefactor n
maxfactor = last factors

main = do
	print maxfactor
