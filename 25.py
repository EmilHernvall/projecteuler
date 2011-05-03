# sqrt5=e(l(5)*0.5)
# phi=(1+sqrt5)/2
# l(sqrt5*(10^1000-1/2))/l(phi)
# 4786.64424271985052618151
# correct = 4782

f = 1
g = 1
s = 0
i = 1
while True:
	tmp = g
	g = tmp + f
	f = tmp
	i += 1
	if len(str(f)) >= 1000:
		print str(i) + ": " + str(f)
		break;
