factorize :: Int -> [Int]
factorize n =
    let
        findfactor n m b
            | m <= b && n `mod` m == 0 = [m] ++ (findfactor n (m+1) b) ++ [n `div` m]
            | m <= b = findfactor n (m+1) b
            | otherwise = []
        root = ceiling (sqrt (fromIntegral n))
    in findfactor n 2 root

palindrome :: Int -> Int
palindrome n = let
    palindrome' n m c
        | n > 0 = palindrome' a b (c+1)
        | otherwise = (m,c)
        where
            a = n `div` 10
            b = 10*m + (n `mod` 10)
    revnum = palindrome' n 0 0
    in n * 10^(snd revnum) + (fst revnum)

largefactors n = 
    let
        factors = factorize n
        filtered = filter (\x -> x >= 100 && x <= 999) factors
        filtered2 = filter (\x -> (n `div` x) >= 100 && (n `div` x) <= 999) filtered
    in (n, filtered2)

main = do
    print $ fst . last $ filter (\x -> (snd x) /= []) $ map (largefactors . palindrome) [100..999]
