f = open("79.txt","r")
text = f.read()
logins = text.split("\r\n")

res = []
for i in range(0, 10):
    before, after = set(), set()
    for login in logins:
        possibly = set()
        found = False
        for c in login:
            if int(c) == i:
                found = True
            else:
                if not found:
                    possibly.add(int(c))
                else:
                    after.add(int(c))

        if found:
            before = before.union(possibly)

    if len(after) > 0 or len(before) > 0:
        res.append([i, len(before)])

out = range(0, len(res))
for digit in res:
    out[digit[1]] = str(digit[0])
    
print "min code is: " + "".join(out)

