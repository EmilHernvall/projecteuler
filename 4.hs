digitcount :: Integer -> Integer
digitcount n = ceiling (log (fromIntegral n)/(log 10))

palindromize2 :: Integer -> Integer -> Integer
palindromize2 n m | m > 0 = let a = m `div` 10
                                b = m - a * 10
                            in palindromize2 (n*10+b) a
                  | otherwise = n

palindromize :: Integer -> Integer
palindromize n = palindromize2 n n

palindromseries :: Integer -> Integer -> [Integer]
palindromseries n m = map palindromize [n..m]

test = palindromseries 100 999

main = do
	print test
