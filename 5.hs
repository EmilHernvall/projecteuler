-- find _all_ factors of a number
factorize :: Int -> [Int]
factorize n =
    let
        findfactor n m b
            | m <= b && n `mod` m == 0 = [m] ++ (findfactor n (m+1) b) ++ [n `div` m]
            | m <= b = findfactor n (m+1) b
            | otherwise = []
        root = round (sqrt (fromIntegral n))
        factors = findfactor n 2 root
    in if factors == [] then [n] else factors

-- eliminate factors that aren't prime by trying to divide them by the other
-- divisors in the list
primefactorize :: Int -> [Int]
primefactorize n =
    let
        factors = factorize n
        isdividable l n = foldr (&&) True [ n `mod` x /= 0 | x <- l, x /= n ]
    in [ x | x <- factors, isdividable factors x ]

-- remove duplicate factors
summarize :: [Int] -> [Int]
summarize l = 
    let
        summarize' (l:ls) res 
            | l `elem` res = summarize' ls res
            | otherwise = summarize' ls (l:res)
        summarize' [] res = res
    in summarize' l []

-- find the exponent of each factor
countfactors :: Int -> [(Int, Int)]
countfactors n =
    let 
        factors = summarize (primefactorize n)

        factorexp n m
            | n `mod` m == 0 = 1 + (factorexp (n `div` m) m)
            | otherwise = 0

        iteratefactors (f:fl) = [(f, factorexp n f)] ++ (iteratefactors fl)
        iteratefactors [] = []
    in iteratefactors factors

-- reduce a list of factors to only contain one entry per base and the maximum exponent
-- in the list.
maxexp :: [(Int, Int)] -> [(Int, Int)]
maxexp factors =
    let
        maxexp' (u:ul) n m
            | (fst u) == n && (snd u) > m = maxexp' ul n (snd u)
            | otherwise = maxexp' ul n m
        maxexp' [] n m = m

        uniquefactors (u:ul) res
            | c `elem` res = uniquefactors ul res
            | otherwise = uniquefactors ul (c:res)
            where c = fst u
        uniquefactors [] res = res

        newfactors = uniquefactors factors []
    in map (\x -> (x, (maxexp' factors x 0))) newfactors

finalproduct l = product $ map (\x -> (fst x) ^ (snd x)) l          

main = do
    print $ finalproduct $ maxexp $ concat $ map countfactors [2..20]
