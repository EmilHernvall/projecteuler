import math

base = 1020304050607080900
n = base
for i in range(0, 10):
	for j in range(0, 10):
		for k in range(0, 10):
			for l in range(0, 10):
				for m in range(0, 10):
					for n2 in range(0, 10):
						print n
						for o in range(0, 10):
							for p in range(0, 10):
								for q in range(0, 10):
									n = base + i*10**17 + j*10**15 + k*10**13 + l*10**11 + m*10**9 + n2*10**7 + o*10**5 + p*10**3 + q*10**1
									root = int(math.sqrt(n))
									if root*root == n:
										print root
