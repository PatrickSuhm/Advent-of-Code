
lines = open("data.txt", "r").readlines()

def getNumbers():
    pairs = l.split(",")
    first = pairs[0].split("-")
    sec = pairs[1].split("-")
    return int(first[0]), int(first[1]), int(sec[0]), int(sec[1])

#--- Part 1
cnt = 0
for l in lines:
    a,b,c,d = getNumbers()
    if a<=c and b>=d or c<=a and d>=b:
        cnt+=1
print("Part 1:", cnt)

#--- Part 2
cnt = 0
for l in lines:
    a,b,c,d = getNumbers()
    if a<=d and c<=b:
        cnt+=1
print("Part 2:", cnt)




