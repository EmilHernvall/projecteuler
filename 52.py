n = 6
i = 0
while True:
    start = 10**i
    max = 10**(i+1)/6
    found = False
    for j in range(start, max):
        match = True
        nrstr = str(j)
        for k in range(2, n+1):
            nrstr2 = str(j*k)
            for c in nrstr:
                if not c in nrstr2:
                    match = False
                    break
            if not match:
                break
        if match:
            found = True
            print j
    if found:
        break
    i += 1
