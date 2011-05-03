n = 600851475143

factor2 :: Integer -> Integer -> Integer -> [Integer] -> [Integer]
factor2 cur root n res | cur > root = res
                       | n `mod` cur == 0 = (factor2 (cur+1) root n (cur:res))
                       | otherwise = (factor2 (cur+1) root n res)
	
factor :: Integer -> [Integer]
factor x = let searchUntil = (truncate (sqrt (fromIntegral x)))
	in reverse (factor2 2 searchUntil x [])

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
