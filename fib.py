def fib(n):
	def fibiter(a, b, p, q, count):
		if count == 0: return b
		elif count % 2 == 0: return fibiter(a, b, p*p+q*q, 2*p*q+q*q, count / 2)
		else: return fibiter(b*q+a*q+a*p, b*p+a*q, p, q, count-1)

	return fibiter(1, 0, 0, 1, n)
  
		
print fib(100000)
