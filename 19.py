days = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
wDays = [ "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun" ]

wDay = 0
i = 0
for y in range(1900, 2001):
	for m in range(1, 13):
		daysInMonth = days[m-1]
		if m == 2 and y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
			daysInMonth += 1

		for d in range(1, daysInMonth + 1):
			if wDay == 6 and d == 1:
				print str(y) + "-" + str(m) + "-" + str(d) + " " + wDays[wDay]
				if y >= 1901 and y <= 2000:
					i += 1

			wDay = (wDay + 1) % 7

print "days: " + str(i)
