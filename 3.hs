factorize :: Integer -> [Integer]
factorize n =
    let 
        findfactor n m b
            | m <= b && n `mod` m == 0 = [m] ++ (findfactor n (m+1) b) ++ [n `div` m]
            | m <= b = findfactor n (m+1) b
            | otherwise = []
        root = ceiling (sqrt (fromIntegral n))
    in findfactor n 2 root

primefactorize :: Integer -> [Integer]
primefactorize n =
    let 
        factors = factorize n
        isdividable l n = foldr (&&) True [ n `mod` x /= 0 | x <- l, x /= n ]
    in [ x | x <- factors, isdividable factors x ]

findmax :: [Integer] -> Integer
findmax x = 
    let 
        maxfilter a b 
            | a > b = a
            | otherwise = b
    in foldr maxfilter 0 x

main = do
    putStrLn (show (findmax (primefactorize 600851475143)))
