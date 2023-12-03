
#--- Part 1
lines = open("data.txt", "r").readlines()

rows = []
for l in lines:
    ints = []
    for c in l[:-1]:
        ints.append(int(c))
    rows.append(ints)

def checkSmallerIdx(ar, i):
    for k in range(i):
        if ar[i] <= ar[k]:
            return False
    return True

def checkBiggerIdx(ar, i):
    for k in range(i+1,len(ar)):
        if ar[i] <= ar[k]:
            return False
    return True

def transpose(inp):
    out = []
    ac = []
    for i,v in enumerate(inp):
        for r in inp:
            ac.append(r[i])
        out.append(ac)
        ac = []
    return out

tr = transpose(rows)

numCols = len(rows[0])
numRows = len(rows)
cnt = 2 * (numRows + numCols) - 4

for i,row in enumerate(rows):               
    for j,val in enumerate(row):            
        if i > 0 and j > 0 and i < numRows-1 and j < numCols-1:
            if (checkSmallerIdx(row,j) or      # west
                checkBiggerIdx(row,j) or       # east      
                checkSmallerIdx(tr[j],i) or    # north
                checkBiggerIdx(tr[j], i)):     # south
                cnt += 1
            
print("Part 1:", cnt)

#--- Part 2   
def getViewingDistanceSouthOrEast(ar, i):
    dist = 0
    if i == len(ar)-1:
        return 0
    if i == len(ar)-2:
        return 1
    for k in range(i+1,len(ar)):
        if ar[k] < ar[i]:
            dist += 1
            if k == len(ar)-1:
                return dist
        else:
            return dist + 1

def getViewingDistanceNorthOrWest(ar, i):
    dist = 0
    if i == 0:
        return 0
    if i == 1:
        return 1
    for k in range(i):
        if ar[i-k-1] < ar[i]:
            dist += 1
            if k == i-1:
                return dist
        else:
            return dist + 1

maxIdx = 0
for i,row in enumerate(rows):                           
    for j, val in enumerate(row):                       
        w = getViewingDistanceNorthOrWest(row,j)        # west
        e = getViewingDistanceSouthOrEast(row,j)        # east      
        n = getViewingDistanceNorthOrWest(tr[j],i)      # north
        s = getViewingDistanceSouthOrEast(tr[j], i)     # south
        idx = w*e*n*s
        maxIdx = max(maxIdx, idx)

print("Part 2:", maxIdx)