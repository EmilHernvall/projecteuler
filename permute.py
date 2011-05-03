def PermuteSetTake2(thisSet):
	for i, t in enumerate(thisSet):
		for j, q in enumerate(thisSet[i:]):
			if q == t:
				continue

			print t
			print q
			print 

def PermuteSetTake3(thisSet):
	for i, t in enumerate(thisSet):
		for j, q in enumerate(thisSet[i:]):
			if q == t:
				continue

			for k, r in enumerate(thisSet[j:]):			
				if r == q or r == t:
					continue

				print t
				print q
				print r
				print 

thisSet = [673, 823, 541, 229, 109]
PermuteSetTake3(thisSet)
