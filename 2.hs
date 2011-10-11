fib n = fibhelper 1 1 n
    where fibhelper a b n
              | b < n =
                  let c = a + b
                  in [c] ++ (fibhelper b c (n-1))
              | otherwise = []

evenfibsum n = sum (filter even (fib n))

maxfib = 4000000

main = do
	putStrLn (show (evenfibsum maxfib))
